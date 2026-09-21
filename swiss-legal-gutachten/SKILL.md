---
name: swiss-legal-gutachten
description: "Produces a neutral Swiss legal opinion (Gutachten, Rechtsgutachten, avis de droit, parere legale) that applies verified primary sources to stated facts, issue by issue, with counterarguments and calibrated confidence. Use for legal assessment and application of Swiss federal or cantonal law to a case (Sachverhalt, rechtliche Würdigung, Fallbeurteilung). Not for direct source retrieval (use swiss-legal-research) and not for drafting a court pleading."
license: MIT
compatibility: Requires the iuslink MCP tools (Fedlex, Entscheidsuche, LexFind) exposed by the host.
metadata:
  version: "0.2.0"
---

# Swiss legal Gutachten

Prepare a reviewable, neutral legal opinion. The task is not to maximise support for one side, but to identify the governing law, apply it to the stated facts, expose material counterarguments, and calibrate the conclusion to the evidence.

Follow the language rules of `swiss-legal-research` (user's language; Swiss Standard German with `ss`).

## Dependencies

This skill builds on `swiss-legal-research` and, for multiple, comparative, unclear, or unsettled issues, on `swiss-legal-deep-research`; it follows their rules without restating them. Load them with the host's skill-loading tool (for example Claude Code's `Skill` tool) or by reading `../swiss-legal-research/SKILL.md` and `../swiss-legal-deep-research/SKILL.md`; if neither works, report that the installation is incomplete and stop. If the required iuslink tools are unavailable, do not manufacture a legal opinion: state the research blocker and, if useful, provide only a clearly labelled issue outline.

## Scope and boundaries

- For one clean issue, research directly under the loaded source rules.
- For multiple, comparative, unclear, or unsettled issues, follow `swiss-legal-deep-research` when it is installed; otherwise research the narrow issues sequentially.
- This skill does not draft pleadings, mirror an opponent's brief, manage evidence exhibits, or render DOCX/PDF.

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

For one known provision or citation, research directly under the loaded source rules. For several independent, comparative, or unsettled issues, follow the installed deep-research workflow or research the narrow issues sequentially. Search for limiting or contrary authority where it could materially change the result.

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

Apply the loaded source-verification checks, then confirm that facts, assumptions, source findings, and applications remain distinct; material contrary authority is addressed; every conclusion matches its evidence; and the executive summary matches the detailed analysis. Repair concrete defects only; do not expand the mandate for completeness's sake.

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
