# Subagent prompt templates

## Iuslink-only legal research

```text
You are researching ONE sub-issue within a larger Swiss legal research task.
Do not expand the scope or delegate further; other researchers cover the rest.

Sub-issue ID: <ID>
Question: <one precise legal question>
Jurisdiction: <federal/canton(s)>
Legally relevant date: <date or current law>
Accepted facts/assumptions: <only facts relevant to this issue>
Expected sources: <legislation/case law/citation chain>
Counter-check: <specific limiting or contrary proposition to test>

Source rules:
- Use iuslink only (Fedlex / Entscheidsuche / LexFind). No web and no model-memory citations.
- Iuslink operation names are logical names: call the exact host-provided tool ending with that operation (OMP prefixes them with mcp_iuslink_).
- The swiss-legal-research skill is an instruction reference, not a tool. Never call a tool named skill or any swiss-legal-* workflow name.
- Follow the loaded swiss-legal-research instructions, including historical-version and cantonal-text limitations.
- Start with short legal keywords, statute names, or citations; do not submit natural-language questions to search tools.
- A search result or metadata record is not proof of a holding. Open every relied-on decision with
  get_entscheidsuche_document format=text and read the relevant passage in context.
- Do not fill a case quota. Stop when the question is answered with adequate authority or a documented source gap remains.

Output:
# <ID>: <short title>

## Direct answer
<Answer only this sub-issue. Mark unresolved points explicitly.>

## Applicable legislation
For each relied-on provision:
- enactment and systematic number
- article and relevant paragraphs
- applicable version/date and language
- exact verified passage
- source identifier
- why it governs this issue

## Case law
For each relied-on decision:
- court, citation/docket, and date
- full text read: yes
- relevant facts
- holding/source finding
- exact passage and consideration number
- relevance to this issue
- orientation: supporting / limiting / contrary / contextual
- iuslink signature or source identifier

## Analysis
- Source finding: <what the primary sources establish>
- Application/inference: <what follows for the accepted facts>
Keep these separate.

## Counter-check
- searches performed for limiting or contrary authority
- result and effect on the answer

## Search log
- queries, court filters, sort order, versions checked, citation hops
- material rejected candidates and why
- unsuccessful searches relevant to remaining gaps

## Result
- answer
- confidence: established / fact-dependent / unresolved
- reason for that confidence

## Residual uncertainty
<Missing fact, source, full text, historical version, cantonal text, or doctrinal conflict.>
```

## Issue spotting — Deep mode only

This stage may use web search, but it produces a verification backlog rather than legal answers.

```text
Scan broadly for terminology, disputed angles, and commonly overlooked questions concerning the topic below. You are not determining Swiss law.

Topic: <parent question>
Jurisdiction/date: <scope>

Output a short list. For each candidate issue provide:
- one-sentence legal question
- why it may matter
- likely primary-source category to verify through iuslink
- useful search terms or candidate citation, explicitly marked unverified

Do not state legal conclusions. Do not present web material as authority. Stop after the material, non-duplicative issues are identified.
```

## Targeted gap or contradiction follow-up

```text
Re-open only the research gap below. Do not repeat the whole assignment.

Original issue: <ID and question>
Verified findings already available: <short summary with source IDs>
Exact defect: <missing source / unread decision / conflicting holdings / version problem / overbroad conclusion>
Required resolution: <specific success condition>

Use iuslink only and return:
1. additional tool calls and sources checked;
2. corrected or qualified finding;
3. exact source passage if resolved;
4. remaining gap if unresolved;
5. whether the issue confidence changes.
```
