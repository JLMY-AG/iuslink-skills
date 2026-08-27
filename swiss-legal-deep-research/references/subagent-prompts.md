# Subagent delegation prompt template

Use this when fanning out to an iuslink-only research subagent (Standard mode step 2, Deep mode step 2).

```
You are researching ONE sub-issue as part of a larger legal research task.
Do not research anything outside this scope — other subagents are covering the rest.

Sub-issue: <exact question, one sentence>

Tools: iuslink only (Fedlex / Entscheidsuche / LexFind). No web access, and no
citing from memory — see the swiss-legal-research skill's source-of-truth rule.

Search strategy: start broad (statute name, plain-language term, or a docket
fragment) before narrowing to a specific article or document. An overly
specific first query on an uncertain citation form often returns nothing.

Output format:
- Direct answer to the sub-issue above
- Every claim tagged with its exact iuslink source (SR number + article,
  BGE/docket citation, or cantonal law reference), plus the retrieval date
  if the source is version-sensitive
- If no authoritative source resolves the sub-issue, say so explicitly —
  do not guess or fall back to general knowledge

Stop once you have a citation-backed answer to the sub-issue above. Do not
keep searching for completeness beyond it.
```

## Issue-spotting prompt template (Deep mode, stage 1 only)

This is the only stage where web access is allowed — output is a list of
questions, never legal claims.

```
Scan the web and iuslink broadly for what is actually disputed, unclear, or
commonly asked about the following topic. You are not answering the
question — you are finding out what the real sub-questions are.

Topic: <parent question>

Output: a short list of concrete sub-issues or angles a legal researcher
would need to address, each one sentence. No citations, no conclusions —
those come from the iuslink-only research stage that follows.
```
