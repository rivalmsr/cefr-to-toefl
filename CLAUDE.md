# CLAUDE.md — Project Context (cefr-to-toefl)

> Always-loaded context hub: only what every session needs. Details live in the linked docs.

## Project

Personal English knowledge base, read in **Obsidian**. Goals: (1) **fluent English**, (2) an
official **TOEFL iBT** score for S2 admission at the **Institute of Science Tokyo**.

- **Secondary project** (primary = Japanese, `../../learn-japan/minna-no-nihongo-i`) → keep it
  **light**: short sessions, no dense targets, no large material dumps.
- **Claude writes all material** in `lessons/` (the user has no notes; they study Oxford 3000
  **A1 in Anki, not finished** → early units reinforce A1). Active level: `progress/diagnostic.md`.
- **Language:** explanations, feedback & docs in **easy Indonesian**; study content (examples,
  vocab, reading, questions) stays **English**, graded by CEFR.

## Map

| Where | What |
|---|---|
| `README.md` | full file map, how to use, A1→C1 roadmap + unit status |
| `docs/cara-kerja.md` | how the KB works (flows, diagrams, scoring) |
| `docs/konvensi-unit.md` | **read before writing/editing a unit** |
| `docs/perbaikan-kb.md` | fix log (template inside) |
| `reference/official-sources.md` | official CEFR/Oxford/Core Inventory/AWL/ETS references |
| `.claude/skills/*/SKILL.md` | full skill operations |

## Skills

| Skill | Does | Writes |
|---|---|---|
| `/diagnostic` | CEFR placement (no hints) | `diagnostic.md`, seeds `evaluation.md` |
| `/quiz` · `/quiz-t` | daily adaptive drills (12 MCQ) · translation production ID→EN (4) | `evaluation.md`, `history.md` |
| `/toefl` | text-based TOEFL iBT **2026** mock (`toefl-2026-spec.md`) | **only** `toefl-evaluation.md` + `TOEFL` row in `history.md` (may read, never touch `evaluation.md`) |
| `/lesson` | read a unit section verbatim in chat (read-only, no questions) | nothing |
| `/sync-anki` | `bash scripts/sync-anki.sh` (ask: Anki desktop synced?) | `anki-weak-items.md` (AUTO-GENERATED) |

## Core rules (MANDATORY)

1. **Grammar source of truth = `lessons/`** — test only points in written units. Vocab from
   `oxford-vocabulary.md` / `academic-vocabulary.md`; tags only from `reference/quiz-taxonomy.md`.
2. **Official references over memory** — CEFR levels of words/grammar and TOEFL format come from
   `reference/official-sources.md` / `toefl-2026-spec.md`, never from model recall.
3. **Exam mode:** answer all questions first; corrections at the end. Question as `#` heading in
   chat, answers via AskUserQuestion (≤4/panel); productive tasks = free-text + rubric.
4. **Adaptive & honest:** weight toward 🔴/🟡 tags; **compute scores explicitly** (old + session),
   never fabricate. Anki weak words = soft bias for filler words only.
5. **Hint fading:** option hints fade with mastery per tag (🔴/🟡/⚪ full → 🟢 none); the chat
   question always stays complete. `/diagnostic` uses no hints.
6. **Token thrift:** read a unit's **anchor** (~20 lines), details via `Grep`. Batch independent
   reads into one command; don't use `echo =====` as a separator (zsh).
7. **Preserve material:** never drop content when editing; **report every change**.
8. **Fix log:** every rule/skill/reference fix (not new material or scores) → 1 entry at the top
   of `docs/perbaikan-kb.md`.
