# Quiz Taxonomy — Grammar, Skill & Error Tags (learn-english)

The set of **stable tags** used by the `/quiz` and `/toefl` skills to label each question,
so the analysis in `progress/*.md` stays consistent across sessions. Every question gets at
least one **grammar/skill tag** + (when relevant) an **error type** + the **unit** it came from.

> Rule: question material may **only** come from points written in the in-scope `lessons/`.
> Do not invent new tags while grading; use the ones here. Add tags first when a new unit is
> written.

## Grammar tags (per level; filled in as units are written)

Tag format: `<level>-<slug>`, e.g. `A2-past-simple`. Added when the related unit is created.

| Tag | Unit | Pattern/Point |
|-----|------|---------------|
| `A2-present-simple` | Unit 1 | Present simple: subject–verb agreement (base verb vs. -s), don't/doesn't, do/does, adverbs of frequency |
| `A2-present-perfect` | Unit 1 | Present perfect with for/since (situation continuing to now); contrast with present continuous |

## Skill tags (cross-level)
| Tag | Skill |
|-----|-------|
| `SK-vocab` | Vocabulary in context (Oxford/AWL) |
| `SK-collocation` | Collocation / word partnership |
| `SK-paraphrase` | Paraphrase / sentence transformation |
| `SK-reading` | Reading comprehension (main idea, detail, inference) |
| `SK-writing` | Micro-writing / productive writing (free-text) |
| `SK-speaking` | Speaking response (free-text outline/script) |

## Error-type tags (for analysis)
| Tag | Error |
|-----|-------|
| `ERR-tense` | Wrong tense choice/form |
| `ERR-article` | a/an/the/∅ |
| `ERR-prep` | Preposition |
| `ERR-agreement` | Subject–verb / noun agreement |
| `ERR-wordform` | Word form (noun/verb/adj/adv) |
| `ERR-wordchoice` | Word choice / collocation |
| `ERR-wordorder` | Word order |

## TOEFL subtype tags (used by `/toefl`, NOT `/quiz`)

Tracked separately in `progress/toefl-evaluation.md`. **Format TOEFL iBT 2026** (task resmi ETS,
lihat `reference/toefl-2026-spec.md`). Tiap soal `/toefl` = **1 subtype** (task) + (opsional,
Reading/Listening MCQ) **1 focus tag**.

### Subtype = task resmi (dilacak per baris di tracker)
| Tag | Section | Task (nama resmi ETS) | Format di `/toefl` |
|-----|---------|-----------------------|--------------------|
| `RD-words` | Reading | Complete the Words | free-text (lengkapi huruf) |
| `RD-daily` | Reading | Read in Daily Life | MCQ |
| `RD-academic` | Reading | Read an Academic Passage | MCQ |
| `LS-response` | Listening | Listen and Choose a Response | MCQ (transkrip) |
| `LS-conversation` | Listening | Listen to a Conversation | MCQ (transkrip) |
| `LS-announcement` | Listening | Listen to an Announcement | MCQ (transkrip) |
| `LS-talk` | Listening | Listen to an Academic Talk | MCQ (transkrip) |
| `WR-build` | Writing | Build a Sentence | free-text (susun kalimat) |
| `WR-email` | Writing | Write an Email | free-text, rubrik 0–5 |
| `WR-discussion` | Writing | Write for an Academic Discussion | free-text, rubrik 0–5 |
| `SP-interview` | Speaking | Take an Interview | free-text (skrip), rubrik 0–5 |

_`Listen and Repeat` (Speaking) di luar cakupan — butuh audio._

### Focus tag (opsional, untuk analisis MCQ Reading/Listening)
| Tag | Fokus soal |
|-----|------------|
| `RD-mainidea` | Main idea / author's purpose |
| `RD-detail` | Detail & facts |
| `RD-inference` | Inference |
| `RD-vocab` | Word meaning in context |
| `RD-paraphrase` | Sentence simplification / paraphrase |
| `LS-gist` | Gist / main topic (transcript) |
| `LS-detail` | Detail (transcript) |
| `LS-function` | Speaker function/attitude (transcript) |
