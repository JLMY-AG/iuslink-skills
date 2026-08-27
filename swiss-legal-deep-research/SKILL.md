---
name: swiss-legal-deep-research
description: Multi-agent research orchestration for complex, comparative, or unsettled Swiss legal questions — fans out to parallel research agents and fuses their findings, with a hard boundary between open-web issue-spotting and iuslink-only legal determination. Use for multi-part, cross-jurisdiction, or genuinely unclear questions; not for a single citation or statute lookup (use swiss-legal-research for that).
allowed-tools: resolve_fedlex_statute get_fedlex_article get_fedlex_text get_fedlex_outline list_fedlex_versions search_entscheidsuche get_entscheidsuche_document get_entscheidsuche_citations search_cantonal_law get_cantonal_law
---

## When to use this vs. `swiss-legal-research`

- Single citation, single statute, one clean question → use `swiss-legal-research` directly. Orchestration overhead isn't worth it.
- Multi-part or comparative question (e.g. "how does this differ under Zurich vs. Aargau law"), or a genuinely unclear/unsettled question where you don't yet know what the sub-issues even are → use this skill.

Effort should scale to the question, not default to maximum every time:

| Question shape | Approach |
|---|---|
| One fact, one source | Single lookup — skip this skill |
| 2–4 distinct sub-questions, scope already clear | **Standard mode** below |
| Broad, unclear scope, multi-jurisdiction, or high-stakes | **Deep mode** below |

## The core rule: web finds the questions, iuslink answers them

Web search is only ever used to figure out *what to research* — never to answer the legal question itself. Every claim in the final synthesis must trace back to an actual iuslink tool call (Fedlex / Entscheidsuche / LexFind), exactly per the source‑of‑truth rule in `swiss-legal-research`. A web-sourced fact is never a substitute for a primary-source citation, no matter how confidently it reads.

## Standard mode (default — 2–4 subagents, no web fan-out)

1. Read the question yourself and split it into 2–4 distinct sub-issues. Keep each one scoped tightly enough that two subagents can't end up researching the same thing.
2. Fan out to 2–4 parallel subagents, **iuslink tools only, no web access**. Delegate using the template in `references/subagent-prompts.md` — each subagent gets one sub-issue, explicit tool guidance, and a required output format.
3. Fuse the results yourself. If one sub-issue comes back thin or contradictory, send a single targeted follow-up to that subagent — don't re-run the whole batch.

## Deep mode (broad or unclear-scope questions)

1. **Issue-spotting fan-out** (web + iuslink allowed, a fast/small model is fine here): 2–3 agents scan the web and iuslink broadly for what's actually disputed or unclear about the question. Output is a list of concrete sub-issues, never answers — this stage produces no citable claims.
2. **Legal research fan-out** (iuslink only, no web): one subagent per sub-issue identified in stage 1, same rules and template as Standard mode above.
3. **Fusion**: synthesize all findings. If synthesis exposes a gap or contradiction, spin up one more targeted stage-2 subagent rather than restarting the pipeline.

## Avoiding the common failure modes

- **Duplicate work** — the most common failure. Name exactly what each subagent owns; a vague shared prompt like "research topic X" causes overlapping searches. Give each subagent the exact sub-issue, not the parent question.
- **Runaway fan-out** — more agents on a simple question burns tokens without improving the answer. Match agent count to the table above.
- **Search too narrow, too early** — inside a subagent, start with a short/broad query (statute name, plain-language term, docket fragment) before narrowing to a specific article or document. An overly specific first query on an uncertain citation form often returns nothing.
- **No stopping condition** — a subagent stops once it has a citation-backed answer to its one sub-issue, not once it has read everything available on the topic.

## Reference material

See `references/subagent-prompts.md` for the delegation-prompt template used in step 2 of both modes.
