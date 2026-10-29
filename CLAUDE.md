# CLAUDE.md — Project Context (learn-english)

> Context hub that is **always loaded** each session. Concise but complete; long details live
> in the docs it points to. Full skill operations are in `.claude/skills/*/SKILL.md`.

## Project idea

A personal knowledge base for learning **English**. Two goals:
1. **Become fluent in English.**
2. **Reach an official TOEFL iBT score** for graduate (S2) admission at the **Institute of
   Science Tokyo**.

Materials are read/organized in **Obsidian**. **Bahasa:** penjelasan dan dokumentasi ditulis
dalam **Bahasa Indonesia yang mudah dipahami** (penjelasan grammar, catatan, feedback/koreksi,
dan dokumen operasional: file ini, README, SKILL.md, tracker). **Konten yang dipelajari tetap
English** — contoh kalimat, vocabulary, Reading, frasa Speaking/Writing, dan soal kuis/TOEFL
(level English-nya tetap disesuaikan CEFR).

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
  toefl-templates.md       TOEFL 2026 templates + model answers + rubrics (free-text tasks)
  toefl-2026-spec.md       official TOEFL iBT 2026 structure + band ↔ CEFR tables (ETS)
  official-sources.md      official A1–C1 references (CEFR, Core Inventory, Oxford, AWL, ETS) + links
  sources/                 downloaded official PDFs (gitignored)
progress/
  diagnostic.md            placement result + current CEFR estimate
  evaluation.md            /quiz weakness tracker (per grammar/skill/area)
  toefl-evaluation.md      /toefl tracker (per section/subtype)
  history.md               session log (one prefix per skill)
  anki-weak-items.md       weak Oxford 3000 words from Anki (lapses/leech) — AUTO-GENERATED
scripts/
  sync-anki.sh             regenerates progress/anki-weak-items.md from Anki desktop
.claude/skills/
  diagnostic/SKILL.md      placement test → set CEFR level (RUN FIRST)
  quiz/SKILL.md            daily adaptive drills (same as the Japanese /quiz); ref/translate.md = translate mode
  quiz-t/SKILL.md          alias for /quiz translate (Indonesian → English production)
  toefl/SKILL.md           text-based TOEFL iBT 2026 mock, 4 sections (same as the Japanese /jlpt)
  sync-anki/SKILL.md       refresh Anki weak items (same as the Japanese /sync-anki)
```

The full syllabus roadmap (A1→C1) plus unit status is in the table in `README.md`.

## Skills (summary — details in each SKILL.md)

- **`/diagnostic`** — CEFR placement. **Run first**, before units are written. Writes
  `progress/diagnostic.md` and seeds `progress/evaluation.md`.
- **`/quiz`** — daily adaptive drills. Grammar source of truth = `lessons/`; vocabulary =
  `oxford-vocabulary.md` + `academic-vocabulary.md`. Default **12 questions**, weighted toward
  weak areas in `evaluation.md`. Writes `evaluation.md` + `history.md`. **`/quiz-t`** = `/quiz
  translate`: 4 free-text Indonesian → English production items, 1 per panel.
- **`/toefl`** — text-based **TOEFL iBT 2026** mock (official task types, spec in
  `toefl-2026-spec.md`), 4 sections (Listening uses a transcript; Listen and Repeat and real audio
  are out of scope). Writes **only** `toefl-evaluation.md` + a `TOEFL`-labeled row in
  `history.md`; it **may read** `evaluation.md` but **must not touch it**.
- **`/sync-anki`** — runs `bash scripts/sync-anki.sh` to regenerate
  `progress/anki-weak-items.md` from Anki desktop (deck `Oxford 3000 <level>`). Ask the user to
  **open Anki desktop & Sync first**. `/quiz` & `/toefl` read only its anchor and apply a **soft
  bias**: prefer those words as sentence fillers when natural (never replacing weak tags from the
  trackers).

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
  **> Quick summary:** (naming ALL points in the unit), then sections **Grammar** (Aturan/
  Contoh/Catatan — penjelasan dalam Bahasa Indonesia, contoh kalimat tetap English),
  **Vocabulary** (themed Oxford/AWL batch; kolom Meaning (EN) + Arti (ID) + Example), **Reading** (short
  text), **Speaking/Writing phrases**, **TOEFL link**. This anchor convention is what makes
  token-thrifty reading valid — always follow it.
- **When adding a new unit**, also update: `README.md` (roadmap + status) and
  `reference/quiz-taxonomy.md` (new tags — REQUIRED before the skills use them). Add the
  related vocabulary batch to `reference/oxford-vocabulary.md` / `academic-vocabulary.md`.
