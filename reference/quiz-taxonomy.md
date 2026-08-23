# Quiz Taxonomy — Grammar, Skill & Error Tags (learn-english)

The set of **stable tags** used by the `/practice` and `/toefl` skills to label each question,
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

## TOEFL subtype tags (used by `/toefl`, NOT `/practice`)

Tracked separately in `progress/toefl-evaluation.md`.

| Tag | Section | Subtype |
|-----|---------|---------|
| `RD-mainidea` | Reading | Main idea / author's purpose |
| `RD-detail` | Reading | Detail & facts |
| `RD-inference` | Reading | Inference |
| `RD-vocab` | Reading | Word meaning in context |
| `RD-paraphrase` | Reading | Sentence simplification / paraphrase |
| `LS-gist` | Listening | Gist / main topic (transcript) |
| `LS-detail` | Listening | Detail (transcript) |
| `LS-function` | Listening | Speaker function/attitude (transcript) |
| `SP-independent` | Speaking | Independent task (free-text) |
| `SP-integrated` | Speaking | Integrated task (free-text) |
| `WR-integrated` | Writing | Integrated essay (free-text) |
| `WR-independent` | Writing | Independent essay (free-text) |
