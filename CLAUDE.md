# CLAUDE.md — Project Context (learn-english)

> Context hub that is **always loaded** each session. Concise but complete; long details live
> in the docs it points to. Full skill operations are in `.claude/skills/*/SKILL.md`.

## Project idea

A personal knowledge base for learning **English**. Two goals:
1. **Become fluent in English.**
2. **Reach an official TOEFL iBT score** for graduate (S2) admission at the **Institute of
   Science Tokyo**.

Materials are read/organized in **Obsidian**. **All docs are written in English** — including
learning material and operational docs (this file, README, SKILL.md, trackers). Learning
explanations use **immersion English**, graded by level (simpler at low levels, richer as the
level rises).

> **Priority:** this is a **SECONDARY** project. The user's primary focus is Japanese
> (`../learn-japan/minna-no-nihongo-i`). Keep the design and pacing **light, incremental, and
> low-pressure** — short sessions, no dense targets, no large material dumps at once.

## Key difference from the Japanese project

In the Japanese project, `lessons/` are the user's own notes (the source of truth). **Here the
user has no notes** — they only study **Oxford 3000 tier A1 in Anki (still in progress, not
fully memorized)**. So **Claude writes all curriculum material** (staged, standard CEFR,
TOEFL-oriented). Claude's material in `lessons/` is the **source of truth** for the skills.
Because A1 is not finished, early units also **reinforce tier A1 vocabulary** — do not assume
A1 is complete.

## Structure (full index → `README.md`)

```
lessons/unit-XX.md         themed integrated unit (grammar+vocab+reading+phrases) — WRITTEN BY CLAUDE, source of truth
reference/
  quiz-taxonomy.md         grammar/skill/error-type tags for the skills (index)
  oxford-vocabulary.md     Oxford 3000/5000 pool (CEFR-tagged) — vocab source for skills
  academic-vocabulary.md   AWL / academic vocabulary for TOEFL
  collocations.md          common collocations & chunks
  grammar-reference.md     cross-level grammar summary
  synonyms.md              synonym/paraphrase pairs (vocab & TOEFL)
  toefl-templates.md       templates + model answers + Writing/Speaking rubrics
progress/
  diagnostic.md            placement result + current CEFR estimate
  evaluation.md            /practice weakness tracker (per grammar/skill/area)
  toefl-evaluation.md      /toefl tracker (per section/subtype)
  history.md               session log (one prefix per skill)
.claude/skills/
  diagnostic/SKILL.md      placement test → set CEFR level (RUN FIRST)
  practice/SKILL.md        daily adaptive drills (analogous to the Japanese /quiz)
  toefl/SKILL.md           text-based TOEFL iBT mock, 4 sections (analogous to /jlpt)
```

The full syllabus roadmap (A1→C1) plus unit status is in the table in `README.md`.

## Three skills (summary — details in each SKILL.md)

- **`/diagnostic`** — CEFR placement. **Run first**, before units are written. Writes
  `progress/diagnostic.md` and seeds `progress/evaluation.md`.
- **`/practice`** — daily adaptive drills. Grammar source of truth = `lessons/`; vocabulary =
  `oxford-vocabulary.md` + `academic-vocabulary.md`. Default **12 questions**, weighted toward
  weak areas in `evaluation.md`. Writes `evaluation.md` + `history.md`.
- **`/toefl`** — text-based TOEFL iBT mock, 4 sections (Listening uses a transcript; real audio
  is out of scope). Writes **only** `toefl-evaluation.md` + a `TOEFL`-labeled row in
  `history.md`; it **may read** `evaluation.md` but **must not touch it**.

## Core rules (MANDATORY — all skills)

1. **Grammar source of truth = `lessons/`.** Skills only test material already written in the
   in-scope units. Vocabulary comes from `oxford-vocabulary.md` / `academic-vocabulary.md`.
2. **Exam mode (default):** answer **all questions first**; corrections & analysis appear **at
   the end**.
3. **Large display:** each question sentence uses an `#` (H1) heading in chat for emphasis and
   spacing; answers are clicked via **AskUserQuestion** panels (max 4 questions/panel).
   Productive skills (Writing/Speaking) use **free-text** — the user types a response and
   Claude grades it against a rubric.
4. **Adaptive weighting:** add more questions for tags marked 🔴/🟡 in the tracker. **Compute
   scores explicitly** from old numbers + this session's results (never fabricate).
5. **Hint fading (scaffolding):** the amount of hint in an option's `description` **fades
   gradually** with mastery — 🔴/🟡/⚪ → full hints; approaching 🟢 → neutral hints; solid 🟢 →
   no hints (bare options, exam-style). Decide per tag from the tracker; never cut abruptly.
   The large version of the question in chat always stays complete. (Exception: `/diagnostic`
   uses no hints, to measure honestly.)
6. **Token thrift:** read the **anchor** of a unit (title + Focus + "Quick summary", ~20
   lines), not the whole file. Read pattern/vocab details on demand via `Grep`.
7. **Preserve material integrity.** When editing a unit, do not remove content; **report every
   change** you make.

## Unit writing conventions (`lessons/unit-XX.md`)

- Structure: title `# Unit X — <Theme> (CEFR <level>)`, a **Focus** block, a blockquote
  **> Quick summary:** (naming ALL points in the unit), then sections **Grammar** (Rules/
  Examples/Notes), **Vocabulary** (themed Oxford/AWL batch + examples), **Reading** (short
  text), **Speaking/Writing phrases**, **TOEFL link**. This anchor convention is what makes
  token-thrifty reading valid — always follow it.
- **When adding a new unit**, also update: `README.md` (roadmap + status) and
  `reference/quiz-taxonomy.md` (new tags — REQUIRED before the skills use them). Add the
  related vocabulary batch to `reference/oxford-vocabulary.md` / `academic-vocabulary.md`.
