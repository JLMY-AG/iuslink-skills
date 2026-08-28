---
name: swiss-legal-gutachten
description: Produces a neutral, source-grounded Swiss legal opinion (Gutachten/Rechtsgutachten/legal opinion) from stated facts and verified iuslink research. Use when the user wants legal assessment and application, not merely source retrieval or a court pleading.
allowed-tools: Agent WebSearch resolve_fedlex_statute get_fedlex_article get_fedlex_text get_fedlex_outline list_fedlex_versions search_entscheidsuche get_entscheidsuche_document get_entscheidsuche_citations search_cantonal_law get_cantonal_law
---

# Swiss legal Gutachten

Prepare a reviewable, neutral legal opinion. The task is not to maximise support for one side, but to identify the governing law, apply it to the stated facts, expose material counterarguments, and calibrate the conclusion to the evidence.

Use the user's language. In German, write Swiss Standard German (`ss`, not `ß`).

## Dependencies and boundaries

- Follow `swiss-legal-research` for every source lookup. Never cite legal text or a decision from memory.
- Use `swiss-legal-deep-research` when the opinion has multiple, comparative, unclear, or unsettled issues.
- For one clean issue, research directly; orchestration overhead is unnecessary.
- This skill does not draft pleadings, mirror an opponent's brief, manage evidence exhibits, or render DOCX/PDF.

If required iuslink tools are unavailable, do not manufacture a legal opinion. State the research blocker and, if useful, provide only a clearly labelled issue outline.

## 1. Define the mandate

Establish only what is material:

- the legal question and desired decision or practical use;
- federal and/or cantonal jurisdiction;
- the legally relevant date, especially for events governed by historical law;
- intended audience, language, and requested depth;
- supplied facts, disputed facts, assumptions, and open facts;
- explicit exclusions.

Ask only blocking questions. If the request is abstract, proceed without invented facts and state that the opinion is doctrinal rather than fact-specific. If a missing fact changes only one branch, analyse both branches instead of stopping the whole task.

## 2. Create the issue and fact map

Turn the mandate into non-overlapping questions. For each issue record internally:

- the precise legal question;
- the facts or assumptions on which it depends;
- the relevant date and jurisdiction;
- the expected legal consequence;
- the necessary sources and material counter-check.

Keep these categories separate throughout:

- **Fact:** supplied by the user or a cited record;
- **Assumption:** used because a fact is unavailable;
- **Source finding:** verified statutory text or judicial holding;
- **Application:** reasoning that connects law and facts;
- **Open point:** fact or authority not established.

## 3. Research proportionately

Route each issue:

- one known provision or citation → `swiss-legal-research`;
- several independent, comparative, or unsettled issues → `swiss-legal-deep-research`.

Research the applicable version of federal law, not automatically the current version. Read every relied-on decision in full text and capture the relevant consideration in context. Search for limiting or contrary authority where it could materially change the result.

For cantonal legislation, iuslink supplies metadata and the official link, not verified statutory text. Do not quote or paraphrase the provision as retrieved law. Identify the limitation and keep any text-dependent conclusion open until the official text has actually been read through an authorised source.

Web search may help discover issues in Deep mode. It may not support a legal proposition in the opinion.

## 4. Pass the evidence gate

Before drafting, test every material proposed claim:

| Claim | Fact basis | Primary source | Verified content | Application | Contrary/limiting material | Status |
|---|---|---|---|---|---|---|

A claim is:

- `verified` when the cited source supports it at the stated breadth;
- `qualified` when it depends on disputed facts, source hierarchy, time, court, or unresolved tension;
- `open` when an adequate source or material fact is missing.

Do not draft an open point as a conclusion. Do not turn an unsuccessful search into the absolute claim that no law or case exists; report the search scope and limitation instead.

## 5. Analyse in Gutachten style

For each legal question:

1. give a short provisional answer;
2. identify the governing verified rules;
3. explain any interpretation material to the outcome;
4. apply each legal requirement to the supplied facts or explicit assumptions;
5. address the strongest plausible counterargument and limiting authority;
6. state an issue conclusion and confidence:
   - **established:** controlling sources and material facts support the result;
   - **fact-dependent:** the rule is identifiable but the result turns on facts, discretion, or analogy;
   - **unresolved:** the available primary sources do not justify a reliable conclusion.

Use the classic rule/application/result sequence where it clarifies the analysis, but do not add empty formulaic sections.

## 6. Adversarial preflight

Before finalising, check:

- Is every legal proposition traceable to an actual iuslink retrieval?
- Was the legally applicable statutory version used?
- Was every cited decision read in `format=text`, including the relevant context?
- Are judicial holdings separated from this opinion's inferences?
- Are facts, assumptions, and disputed facts visibly distinct?
- Is material contrary authority fairly addressed?
- Does any cantonal-law claim exceed iuslink's metadata-only coverage?
- Are negative-search claims appropriately limited?
- Is each conclusion no stronger than its sources and facts?
- Does the executive summary match the detailed analysis?

Repair concrete defects only; do not expand the mandate for completeness's sake.

## 7. Deliverable

Use `references/opinion-template.md`, adapting headings to the mandate. The final opinion should normally contain:

1. executive summary and short answer;
2. mandate, questions, scope, and relevant date;
3. facts, assumptions, disputed matters, and missing information;
4. issue-by-issue legal assessment;
5. overall conclusion with calibrated confidence;
6. practical recommendations tied to the analysis;
7. research limitations and a primary-source register.

Do not expose internal agent logs or the full evidence matrix unless requested. Do not add generic disclaimers, client metadata, signatures, or document-production markup unless the user asks for them.
