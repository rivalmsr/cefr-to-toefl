# Quiz Evaluation — Weakness Tracker (/quiz)

Updated automatically by the `/quiz` skill after each session. Tracks accuracy **per
grammar/skill tag**, **per error type**, and **per unit**, then ranks the **weak areas**.

**Status thresholds:** accuracy <60% 🔴 WEAK · 60–79% 🟡 · ≥80% 🟢
(needs at least **3 attempts** before a status is computed; below that = ⚪ not enough data)

_Seeded 2026-08-23 from `/diagnostic` (16 items). Updated 2026-10-29 after `/quiz` #1 (Unit 1,
12 items, 10/12) and `/quiz-t` #1 (translate, Unit 1, 4 items, 2/4). Below 3 attempts = ⚪ not enough data._

---

## Per grammar/skill tag
| Tag | Correct | Total | Accuracy | Status |
|-----|---------|-------|----------|--------|
| `A2-present-simple` | 4 | 7 | 57% | 🔴 (agreement with plural subject: *my cousins goes*, *they brings*, *my parent drinks* for "orang tua"; doesn't/does OK) |
| `A2-present-perfect` | 3 | 4 | 75% | 🟡 (production: *I have this coat for 3 years* → **have had**) |
| `SK-vocab` | 7 | 7 | 100% | 🟢 |
| `SK-reading` | 6 | 6 | 100% | 🟢 |
| `SK-paraphrase` | 1 | 1 | — | ⚪ |
| `SK-writing` | 2 | 5 | 40% | 🔴 (A2 sample: verb-form, dropped subjects, articles; translate 2/4) |

## Per error type
| Tag | Correct | Total | Accuracy | Status |
|-----|---------|-------|----------|--------|
| `ERR-agreement` | 4 | 8 | 50% | 🔴 (plural subject + -s: *my cousins goes*, *they brings*, *my parent drinks*) |
| `ERR-tense` | 3 | 6 | 50% | 🔴 (diagnostic misses; production: present simple instead of present perfect — *I have this coat for 3 years*) |
| `ERR-prep` | 1 | 1 | — | ⚪ (for/since) |
| `ERR-wordorder` | 1 | 1 | — | ⚪ (adverb of frequency position) |

## Per unit
| Unit | Correct | Total | Accuracy | Status |
|------|---------|-------|----------|--------|
| Unit 1 | 12 | 16 | 75% | 🟡 |

---

## Weak areas (priority for next questions)

1. 🔴 **`A2-present-simple` — subject–verb agreement** (50%, `ERR-agreement` 40%) — plural
   subject takes the base verb. Quiz errors: *~~My cousins goes~~ to the gym* → **go**; missed
   *~~they brings~~ her some cake* in error identification → **bring**; translate: *~~my parent
   drinks~~* for "orang tua" → **My parents drink** (plural noun + base verb). Negatives/questions
   (*doesn't / does*) correct in production too.
2. 🔴 **First conditional** (from diagnostic) — present simple in the *if*-clause (*If it rains,
   we will stay*). No unit yet → not testable; future tag e.g. `B1-first-conditional`.
3. 🟡 **`A2-present-perfect` in production** (75%, `ERR-tense` 50%) — recognizes it in MCQ (3/3)
   but wrote *~~I have this coat for 3 years~~* → **I have had this coat for three years**.
4. 🔴 **Writing accuracy** (`SK-writing` 40%) — verb form after prepositions (*to pray*), dropped
   subjects (*until I reach*), articles/capitalization (*Japanese*, *Saturday*, sentence-initial *My/I*).

**Strengths (de-prioritize):** `SK-vocab` 🟢, `SK-reading` 🟢 — pull richer B1/B2 material for
vocab/reading.
