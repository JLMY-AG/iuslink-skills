---
name: swiss-legal-deep-research
description: Multi-agent research orchestration for complex, comparative, or unsettled Swiss legal questions. Decomposes the question, delegates narrow iuslink-only research assignments, and fuses verified primary-source findings. Web search is permitted only for issue-spotting. Use for multi-part, cross-jurisdiction, or genuinely unclear questions; not for a single citation or statute lookup.
---

## Boundary with `swiss-legal-research`

- One fact, citation, statute, or clean legal question → skip orchestration and perform direct iuslink research using the sibling source instructions.
- Two to four already-defined sub-questions → use **Standard mode**.
- Broad, unclear, comparative, multi-jurisdictional, unsettled, or high-stakes question → use **Deep mode**.

At the start, use the host's file-reading tool to read `../swiss-legal-research/SKILL.md` if that sibling file exists. It is an instruction file, not a callable tool. Never call tools named `skill`, `swiss-legal-research`, `swiss-legal-deep-research`, or an invented workflow phase. This skill adds orchestration; it does not weaken the source rules.

Iuslink operation names are host-specific. Use the exact available tool whose name ends with the requested operation; OMP, for example, prefixes them with `mcp_iuslink_`.

## Core rule: web finds questions, iuslink answers them

Web search may identify terminology, possible disputes, or candidate issues. It never establishes Swiss law. Every legal claim in the synthesis must trace to a primary source actually retrieved through iuslink. Keep web findings explicitly unverified until confirmed.

## 1. Frame the research

Before delegating, identify:

- the precise parent question and requested output;
- jurisdiction and legally relevant date;
- supplied facts, assumptions, disputed facts, and material unknowns;
- exclusions and desired depth.

Ask only for missing information that would materially change the research. For an abstract doctrinal question, state that no fact-specific application is being made.

## 2. Build a non-overlapping issue map

For each sub-issue record:

- `ID` and one-sentence legal question;
- priority and why it matters;
- jurisdiction and relevant date;
- accepted facts or assumptions needed for that issue;
- expected sources: federal legislation, cantonal law, case law, or citation chain;
- a distinct counter-check for limiting or contrary authority.

Do not delegate broad topics. Each assignment must be answerable independently without duplicating another assignment.

## Standard mode

Delegate 2–4 issue-map entries in parallel using `references/subagent-prompts.md` and the host's actual subagent mechanism. Legal-research agents receive iuslink tools only and write separate reports. If parallel agents are unavailable, run the same assignments sequentially rather than inventing an agent or skill tool.

## Deep mode

1. **Issue spotting:** optionally fan out 2–3 fast web/iuslink scouts. Their only output is candidate issues and verification tasks, never legal conclusions.
2. **Issue map:** deduplicate, prioritise, and convert the useful candidates into narrow research assignments.
3. **Legal research:** delegate one iuslink-only agent per material issue.
4. **Gap repair:** send a targeted follow-up only for a concrete missing source, contradiction, or overbroad conclusion. Do not restart the whole batch.

## 3. Require a verified research packet

Each research report must contain:

- direct answer to its exact sub-question;
- applicable statutory text with identifier, article, language, version/date, and exact relevant passage;
- for every relied-on decision: court, citation, date, full-text status, relevant facts, holding, exact passage with consideration reference, and issue-specific relevance;
- clear separation of **source finding** from **application or inference**;
- supporting and, where material, limiting or contrary authority;
- search log, including material unsuccessful searches;
- residual uncertainty and a reasoned confidence label: `established`, `fact-dependent`, or `unresolved`.

A search result or metadata record is not authority for a holding. Every cited decision must be opened in `format=text` and read far enough to verify the relevant passage in context. Do not impose case-count quotas; stop when the issue has an adequate, citation-backed answer or the documented search has reached a genuine source gap.

For cantonal legislation, remember that iuslink returns metadata and the official link, not the statute text. Never quote or paraphrase cantonal provisions as verified text unless the text was obtained from an authorised source outside iuslink and clearly identified as such.

## 4. Fuse through a claim-evidence matrix

Before writing the synthesis, test each material proposition internally:

| Proposed claim | Primary source | Verified source content | Application/inference | Limiting authority | Status |
|---|---|---|---|---|---|

- `verified`: the source supports the claim at the stated breadth;
- `qualified`: support exists but depends on facts, date, court, or unresolved tension;
- `open`: no adequate source; the final answer must say so.

Resolve contradictions by checking source hierarchy, date, procedural context, and factual similarity. Never average incompatible reports into false certainty.

## 5. Synthesis gate

The final synthesis must:

- answer each issue separately before giving an overall conclusion;
- cite only sources actually verified in the research packets;
- distinguish statutory text, judicial holding, and the synthesis's own application;
- state relevant dates and version limits;
- present material contrary authority or explain the documented search gap;
- preserve unresolved facts and source gaps;
- use confidence no stronger than the evidence permits.

Run one adversarial preflight: identify unsupported claims, unread decisions, missing historical versions, overbroad negative conclusions (such as “no case exists”), and the strongest plausible counter-reading. Repair only the identified defects.

## Common failure modes

- **Duplicate work:** assign exact sub-questions, not the parent topic.
- **Runaway fan-out:** match agent count to genuinely independent issues.
- **Natural-language database searches:** convert questions into short legal keywords or citations.
- **Recency bias:** prefer controlling and factually relevant authority over merely recent authority.
- **Quota filling:** never add irrelevant decisions to reach an arbitrary number.
- **False negative claims:** report the databases, queries, filters, and limits searched instead of claiming exhaustive absence.
- **Premature completion:** metadata-only decisions, unverified cantonal text, or unresolved contradictions keep the affected claim open.

## Reference material

Use `references/subagent-prompts.md` for issue-spotting, legal-research, and targeted follow-up prompts.
