# Quiz Evaluation — Weakness Tracker (/quiz)

Updated automatically by the `/quiz` skill after each session. Tracks accuracy **per
grammar/skill tag**, **per error type**, and **per unit**, then ranks the **weak areas**.

**Status thresholds:** accuracy <60% 🔴 WEAK · 60–79% 🟡 · ≥80% 🟢
(needs at least **3 attempts** before a status is computed; below that = ⚪ not enough data)

_Seeded 2026-08-23 from `/diagnostic` (16 items). Updated 2026-11-02 after `/quiz` #4 (Unit 1,
12 items, 10/12); earlier: `/quiz-t` #3 (2026-11-01, 2/4), `/quiz` #3 (2026-11-01, 9/12), `/quiz-t` #2 (2026-10-30, 4/4), `/quiz` #2 (2026-10-30, 11/12), `/quiz` #1 (2026-10-29, 10/12), `/quiz-t` #1 (2026-10-29, 2/4).
Below 3 attempts = ⚪ not enough data._

---

## Per grammar/skill tag
| Tag | Correct | Total | Accuracy | Status |
|-----|---------|-------|----------|--------|
| `A2-present-simple` | 18 | 25 | 72% | 🟡 (MCQ 3/4 on 2026-11-02: *usually goes*, *Kenji and his sister play*, *Do your friends* ✅; ✗ again *~~Rina has always happy~~* → **is always happy**; translate 1/3 on 2026-11-01: *Does your sister often wear* ✅; ✗ *~~has always late~~* → **is always late**, ✗ *~~has usually cook~~* → **usually cooks** — adds *has* before the adverb; MCQ 3/4 on 2026-11-01: agreement/doesn't/Do all ✅, missed adverb position *~~Priya always is late~~* → *is always late*; translate 3/3 on 2026-10-30: *my two cousins watch*, *doesn't drink*, *Does your sister work*; MCQ 4/4 same day; earlier: *my cousins goes*, *they brings*, *my parent drinks* for "orang tua") |
| `A2-present-perfect` | 12 | 15 | 80% | 🟢 (MCQ 1/2 on 2026-11-02: *How long has Maya played* ✅; ✗ *~~We don't go to the cinema since March~~* → **haven't been**; translate 2026-11-01: *How long have you known Andi?* ✅; MCQ 2/3 on 2026-11-01: *has studied since*, *have had this coat* ✅; missed *~~How long do you known~~* → *How long have you known*; production fixed 2026-10-30: *I have had this bike since 2019* ✅; earlier slip *I have this coat for 3 years*) |
| `SK-vocab` | 11 | 11 | 100% | 🟢 |
| `SK-reading` | 11 | 12 | 92% | 🟢 (2/2 on 2026-11-02 & 2026-11-01 incl. main idea & inference; earlier missed main idea: picked a detail-based topic) |
| `SK-collocation` | 2 | 3 | 67% | 🟡 (*take a break* ✅ 2026-11-02; *~~take attention~~* → **pay attention**) |
| `SK-paraphrase` | 4 | 4 | 100% | 🟢 |
| `SK-writing` | 8 | 13 | 62% | 🟡 (translate 2/4 on 2026-11-01, slips: *borther*, *sunday*; translate 4/4 on 2026-10-30; still slips: sentence-initial capital, *exciting film* → films; earlier: verb-form, dropped subjects, articles) |

## Per error type
| Tag | Correct | Total | Accuracy | Status |
|-----|---------|-------|----------|--------|
| `ERR-agreement` | 19 | 24 | 79% | 🟡 (MCQ 3/3 on 2026-11-02; translate 2026-11-01: *Does your sister wear* ✅, *~~my mother has usually cook~~* ✗; MCQ 3/3 on 2026-11-01; production 3/3 on 2026-10-30; earlier *my parent drinks*) |
| `ERR-tense` | 15 | 23 | 65% | 🟡 (MCQ 3/5 on 2026-11-02: ✗ *~~has always happy~~*, ✗ *~~don't go … since March~~* → haven't been; translate 2026-11-01: *How long have you known* ✅ (fixed); ✗ *has* inserted into present simple: *~~has always late~~*, *~~has usually cook~~*; MCQ 2026-11-01: *How long do you known* ✗; *have had* now correct in production; earlier *I have this coat for 3 years*) |
| `ERR-wordorder` | 4 | 5 | 80% | 🟢 (translate 2026-11-01: *Does your sister often wear* ✅; *~~always is late~~* → *is always late*: adverb goes after *be*) |
| `ERR-prep` | 3 | 3 | 100% | 🟢 (for/since) |
| `ERR-wordchoice` | 2 | 3 | 67% | 🟡 (take a break ✅; do the housework ✅; *~~take attention~~* → pay attention) |

## Per unit
| Unit | Correct | Total | Accuracy | Status |
|------|---------|-------|----------|--------|
| Unit 1 | 48 | 60 | 80% | 🟢 |

---

## Weak areas (priority for next questions)

1. 🟡 **Writing accuracy** (`SK-writing` 62%) — remaining slips:
   capital letter at sentence start (*~~my~~ My*), plural after *exciting* (*~~exciting film~~* →
   **exciting films**); earlier: verb form after prepositions (*to pray*), dropped
   subjects (*until I reach*), articles/capitalization (*Japanese*, *Saturday*, sentence-initial
   *My/I*); translate: *~~my parent drinks~~* → **My parents drink**.
2. 🔴 **First conditional** (from diagnostic) — present simple in the *if*-clause (*If it rains,
   we will stay*). No unit yet → not testable; future tag e.g. `B1-first-conditional`.
3. 🟡 **`A2-present-simple`** (72%, `ERR-agreement` 79%) — **REPEATED pattern (translate 2026-11-01,
   MCQ 2026-11-02 *~~Rina has always happy~~*): adds *has* before an adverb of frequency** → *~~My brother has always late~~* → **is always
   late** (adjective → use *be*); *~~My mother has usually cook~~* → **usually cooks** (no *has*,
   verb + -s). Rule: adverb goes **before the main verb**, **after _be_** — no extra *has*. Questions
   OK (*Does your sister often wear…?* ✅). Earlier slip = **adverb of frequency with _be_**: *~~Priya always is late~~* →
   **Priya is always late** (`ERR-wordorder` 75%). Earlier: translate 3/3 on 2026-10-30, MCQ 4/4 on
   2026-10-30 (*my grandparents cook*, *Do your brothers…?*, *Daniel doesn't drink*), but earlier
   errors *~~My cousins goes~~*, *~~they brings~~*, *~~my parent drinks~~* → keep checking,
   especially in production (`/quiz-t`).

4. 🟡 **`ERR-tense`** (65%) — *has* leaking into present simple (see 3), and present simple with
   *since* (*~~We don't go to the cinema since March~~* → **haven't been**, 2026-11-02). *How long*
   questions improving: *How long have you known Andi?* ✅ in production (2026-11-01) after MCQ
   ✗ *~~How long do you known~~*; MCQ *How long has Maya played* ✅ (2026-11-02).
5. 🟡 **`SK-collocation`** (67%) — *take a break* ✅; earlier *~~take attention~~* → **pay attention**.

**Strengths (de-prioritize):** `A2-present-perfect` 🟢 80% (watch *How long have…?* and *have had*
in production), `SK-vocab` 🟢, `SK-reading` 🟢, `SK-paraphrase` 🟢, `ERR-prep` 🟢 — pull richer B1/B2 material
for vocab/reading.
