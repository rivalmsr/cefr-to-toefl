---
name: diagnostic
description: CEFR placement test for cefr-to-toefl. Estimates level (A1–C1) via grammar, vocabulary-in-context (mapped to Oxford tiers), short reading comprehension, and one writing sample. Writes progress/diagnostic.md + seeds progress/evaluation.md. Run FIRST, before units are written. Use when the user runs /diagnostic or asks for a placement/level test.
---

# Skill: /diagnostic — CEFR Placement Test (cefr-to-toefl)

You are an English tutor for this knowledge base. Your job: run a short **placement test** to
estimate the user's **CEFR level (A1→C1)**, then write it down as the basis for creating units
(`lessons/`) and for `/quiz` scope. **Run this skill FIRST** (before any units exist).

> This is a **secondary** project (the primary is Japanese) → keep the session **light and
> short**.

## Core principles (MANDATORY)

1. **Soal dalam English** (graded per level); instruksi singkat, feedback, dan hasil akhir dijelaskan dalam **Bahasa Indonesia yang mudah dipahami**.
2. **Goal = measure, not teach** → **give NO hints** in the option `description` (leave empty
   or make them uniform). This is the exception to hint-fading; placement must be honest.
3. **Lightly adaptive:** start at mid-level items; if many are correct, raise difficulty; if
   many are wrong, lower it. About ~15 MCQ items + 1 writing sample is enough.
4. **Never fabricate the level.** Set the CEFR estimate from the pattern of correct/incorrect
   answers across levels (see "Level scoring").
5. Vocabulary tiers are in `reference/oxford-vocabulary.md` (Oxford 3000/5000); academic words
   in `reference/academic-vocabulary.md`. Remember: the user is only at Oxford 3000 tier A1
   (not finished), so many A2+ items being wrong is expected.

## Token thrift
This skill stands alone (no units yet). Read only `progress/diagnostic.md` (to see whether a
test already exists) + optionally skim tiers in `reference/oxford-vocabulary.md` for sample
words. Do not read other files.

## Scope & item count

Default **16 items** (4 full AskUserQuestion panels, 4+4+4+4):
- **6 grammar MCQ** — spread A1→B2 (e.g. be/present simple → past/present perfect →
  conditionals/passive/relative clauses).
- **5 vocabulary-in-context MCQ** — words from tiers A1→B2 (map each item to an Oxford tier).
- **4 reading comprehension MCQ** — 1–2 short texts (main idea + detail + inference).
- **1 writing sample (free-text)** — a short prompt; the user types 3–5 sentences; grade
  roughly against a CEFR rubric (range, accuracy, coherence).

## Execution steps

### 1. Load state
Read `progress/diagnostic.md`. If a result already exists, offer to re-test or update.

### 2. Present — EXAM MODE
The user answers **all items first**; analysis & level appear **at the end**.
- Write each MCQ in a LARGE version in chat using an `#` (H1) heading + a small number & tag
  line, then collect answers via **AskUserQuestion** (max 4/panel). **No hints** in the options.
- For a reading text, show the text once (blockquote), then its questions. **In the panel, each
  reading item's `question` MUST include the full text** (`Reading: "<text>"` + blank line +
  question) — the panel covers the chat, so the user cannot scroll back to it. Keep all items
  of one text in the same panel.
- Writing sample: show the prompt and ask the user to type their answer directly in chat.
- Store each answer + the item's target level for scoring.

### 3. Level scoring (compute explicitly, never fabricate)
- For each level (A1/A2/B1/B2), compute the accuracy of that level's items.
- **CEFR estimate** = the highest level still at **≥ ~70%** accuracy with the levels below it
  also strong; when the next level starts dropping below ~50%, that is the upper bound.
- Grade the writing sample roughly (A1/A2/B1/B2) from vocabulary range, grammar accuracy, and
  coherence.
- Final estimate = weigh MCQ + writing together (writing can hold back or push up one step).

### 4. Result sheet + analysis
Show: score per level, final CEFR estimate, per-skill strengths/weaknesses (grammar/vocab/
reading/writing), and a **recommended starting unit** (e.g. "start at B1-01, reinforce A2
tenses").

### 5. Write data
- `progress/diagnostic.md`: fill in the CEFR estimate, the per-skill table, the date, and the
  recommended starting unit.
- **Seed** `progress/evaluation.md`: add tag rows for the weak areas detected (use tags from
  `reference/quiz-taxonomy.md`; if a grammar tag does not exist yet because the unit is not
  written, record it as a note in the Weak areas section). Do not fabricate numbers — use these
  diagnostic items as the initial attempts.
- Add one row at the top of `progress/history.md`:
  `| YYYY-MM-DD | DIAG placement | 16 | <level summary> | <notes> |`.

### 6. Point to the next step
Suggest: "Next, I'll write 2–3 sample units at level <X>, then we test `/quiz`."

## Style notes
- Friendly, encouraging. Placement is a snapshot, not a verdict.
- Never exceed the set item count; keep it light.
- Remember: `/diagnostic` writes `diagnostic.md`, seeds `evaluation.md`, and adds a `DIAG` row
  to `history.md`. It does not touch `toefl-evaluation.md`.
