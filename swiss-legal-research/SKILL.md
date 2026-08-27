---
name: swiss-legal-research
description: Swiss legal research workflows for federal legislation (Fedlex), cantonal law (LexFind), and case law (Entscheidsuche/BGE). Use for any query requiring authoritative Swiss legal sources.
allowed-tools: resolve_fedlex_statute get_fedlex_article get_fedlex_text get_fedlex_outline list_fedlex_versions search_entscheidsuche get_entscheidsuche_document get_entscheidsuche_citations search_cantonal_law get_cantonal_law
---

## Source‑of‑truth rule (mandatory)

Never cite, quote, or rely on legal text from memory or prior model knowledge. Always retrieve the current official source via iuslink before using any statute or case.

## Fail loudly — never guess a substitute

If a lookup returns no confident match, say so explicitly: state what you searched and why it didn't resolve. Do not substitute a similarly-named article, a different case, or another canton's law to fill the gap, and do not fall back on general knowledge. An unresolved citation is a correct outcome; a wrong one presented as certain is not.

The tools already do part of this work for you — use it instead of re-guessing:
- `resolve_fedlex_statute` on an ambiguous name (e.g. "Datenschutzgesetz") returns multiple candidates plus a `hint` telling you to refine or pick one explicitly. Treat that hint as a stop-and-clarify signal, not noise — don't just take the first result.
- `get_fedlex_article` with a wrong or non-existent article number fails with a list of nearby valid article numbers (e.g. asking for `28bis` on the ZGB returns an error listing `28, 28a, 28b, 28c, ...`). Use that list before calling `get_fedlex_outline` again from scratch.

## Repealed law can still show up in search results

`search_cantonal_law` does **not** filter to currently-active law by default — repealed and superseded enactments are returned alongside current ones (confirmed: an Aargau "Baugesetz" search returned both the active `Gesetz über Raumentwicklung und Bauwesen` and an inactive `Allgemeine Verordnung zum Baugesetz`, `is_active: false`). Always check the `is_active` field on every result yourself; never assume the first or top-ranked hit is in force.

## Version-awareness — the part that actually matters

Law is a moving target: the current text of a statute is not necessarily the text that applied at the time a contract was signed, an incident occurred, or a filing was made. Before treating a statute as authoritative for a fact pattern, identify the relevant date (signature, incident, filing) and retrieve the article as of *that* date:

```text
get_fedlex_text --as_of YYYY-MM-DD
or
list_fedlex_versions → pick version_uri → get_fedlex_text
```

Defaulting to the current version without checking the relevant date is the single most common way to get a technically-real but legally-wrong citation.

Not every historical version has retrievable text — `list_fedlex_versions` returns a `hint` telling you to pick a version with `has_text: true` before calling `get_fedlex_text`/`get_fedlex_article` on it; older versions can be metadata-only.

## Known edge cases

- **Article suffixes are letters, not Latin ordinals**: inserted articles are numbered `28, 28a, 28b, 28c, ...` — confirmed identical in German *and* French Fedlex text (`Art. 28a` in both ZGB and the Code civil). Legacy `bis`/`ter` notation (`28bis`) is not accepted and returns an error — if a source you're working from uses that older style, drop it and try the plain number or letter suffix instead.
- **Cantonal name collisions**: federal abbreviations (`OR`, `ZGB`, `StGB`, `BV`) are effectively unique nationally, but cantons can reuse generic names (multiple cantons each have a "Baugesetz") for unrelated laws. Always pass the canton explicitly to `search_cantonal_law` — never resolve cantonal law by name alone.
- **Ambiguous case citations**: if a citation doesn't parse cleanly against the formats in `references/citation-formats.md`, run `search_entscheidsuche` with the raw string first to surface candidates before assuming a format.
- **None of iuslink's search tools accept natural language**: `resolve_fedlex_statute` wants an alias, title fragment, or SR number (`StGB`, `Datenschutzgesetz`, `SR 311.0`); `search_entscheidsuche` wants short legal keywords or a citation/docket number, not a phrased question. This isn't a style preference — a natural-language question to `search_entscheidsuche` returns **zero results** (confirmed: "what happens when a tenant terminates a lease early without justification" → 0 hits with a hint to use shorter terms), where the equivalent keyword query (`Mietrecht Kündigung`) returns hundreds. Rephrase as keywords before concluding nothing exists.

## Case-law search — lexical, not semantic, and recency-sorted by default

`search_entscheidsuche` is keyword search, not semantic — it also **sorts by date, newest first, by default**, across every court. An unfiltered query doesn't surface the leading Bundesgericht precedent first; it surfaces whatever recent cantonal decision happens to mention the same words. Confirmed: `"Mietrecht Kündigung"` with no filters returned 907 results, top hits from a St. Gallen insurance court and an Aargau commercial court — nothing from the Bundesgericht in the top 3. Adding `courts: [CH_BGer]` and `sort: relevance` dropped it to 162 results, with the top 3 all on-point Bundesgericht decisions on lease termination.

To find the actual leading case rather than the most recent mention: filter `courts` (`CH_BGer` for the Federal Supreme Court, `CH_BGE` for its published landmark decisions) and set `sort: relevance` explicitly. Don't treat the first hit of a default search as "the" case on a topic.

## Retrieving a decision's text

- Pass `format` explicitly on `get_entscheidsuche_document` — don't rely on the default. The tool's own schema documents the default as `json` (metadata only), but the observed default actually returns the full `text` body; the two disagree, so an implicit call is not reliably reproducible.
- `format=json` is not guaranteed to exist for every court. It returned rich structured metadata (abstract in all three languages, docket references, etc.) for a Bundesgericht/BGE decision, but came back with **no body at all** for a cantonal Handelsgericht decision — the same decision's full text was available under `format=text`. For cantonal courts, use `format=text` (or `html`) to reliably get content; don't conclude a decision has no content just because `format=json` came back empty.
- Long decisions are paginated — use `has_more`, `next_offset`, and `total_chars` from the response to know whether to fetch another chunk, rather than assuming one call returned everything.
- An unresolvable signature fails loudly with a clear message ("document text was not found; verify signature/spider or use search_entscheidsuche first") rather than silent nulls — if you hit this, go back to `search_entscheidsuche` rather than guessing a `spider` value.

## Case-law citation chains

`get_entscheidsuche_citations` returns one flat list of directly related citations (both what the case cites and what cites it) in a single call — it does not recursively walk the citation network for you. To go further than one hop, call it again on one of the returned citations.

## Tool selection at a glance

| Task | Call sequence |
|---|---|
| Statute, article known | `resolve_fedlex_statute` → `get_fedlex_article` |
| Statute, full text | `resolve_fedlex_statute` → `get_fedlex_text` |
| Statute, article unknown, alias known | `get_fedlex_outline` (pass the alias directly as `query`, e.g. `StGB`) → `get_fedlex_article` using the `eli_uri` the outline call returns |
| Statute, article unknown, name unclear | `resolve_fedlex_statute` → `get_fedlex_outline` → `get_fedlex_article` |
| Statute, historical version | `get_fedlex_text --as_of <date>` or `list_fedlex_versions` → `get_fedlex_text` |
| Case law, leading precedent on a topic | `search_entscheidsuche` with `courts: [CH_BGer]` and `sort: relevance` → `get_entscheidsuche_document --format text` |
| Case law, citation known | `search_entscheidsuche "<citation>"` → `get_entscheidsuche_document --format text` |
| Case law, citation chain | `get_entscheidsuche_citations` (single hop — call again on a result to go further) |
| Cantonal law | `search_cantonal_law "<term>" --canton <code>` → `get_cantonal_law` |

Only `get_fedlex_outline` and `resolve_fedlex_statute` accept a bare alias — `get_fedlex_text`, `get_fedlex_article`, and `list_fedlex_versions` all require the exact `eli_uri`. For a well-known abbreviation, calling `get_fedlex_outline` directly is one hop shorter than resolving first, since its response already includes the `eli_uri` you need for the follow-up call.

## Reference material

See `references/citation-formats.md` for citation formats and canton codes.
