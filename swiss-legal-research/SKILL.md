---
name: swiss-legal-research
description: Swiss legal research workflows for federal legislation (Fedlex), cantonal law (LexFind), and case law (Entscheidsuche/BGE). Use for any query requiring authoritative Swiss legal sources.
allowed-tools: resolve_fedlex_statute get_fedlex_article get_fedlex_text get_fedlex_outline list_fedlex_versions search_entscheidsuche get_entscheidsuche_document get_entscheidsuche_citations search_cantonal_law get_cantonal_law
---

## Source‑of‑truth rule (mandatory)

Never cite, quote, or rely on legal text from memory or prior model knowledge. Always retrieve the current official source via iuslink before using any statute or case.

## Fail loudly — never guess a substitute

If a lookup returns no confident match, say so explicitly: state what you searched and why it didn't resolve. Do not substitute a similarly-named article, a different case, or another canton's law to fill the gap, and do not fall back on general knowledge. An unresolved citation is a correct outcome; a wrong one presented as certain is not.

## Version-awareness — the part that actually matters

Law is a moving target: the current text of a statute is not necessarily the text that applied at the time a contract was signed, an incident occurred, or a filing was made. Before treating a statute as authoritative for a fact pattern, identify the relevant date (signature, incident, filing) and retrieve the article as of *that* date:

```text
get_fedlex_text --as_of YYYY-MM-DD
or
list_fedlex_versions → pick version_uri → get_fedlex_text
```

Defaulting to the current version without checking the relevant date is the single most common way to get a technically-real but legally-wrong citation.

## Known edge cases

- **`bis`/`ter`/`quater` article suffixes**: these mark distinct articles inserted after the original enactment (`Art. 8`, `8bis`, `8ter` are three separate articles, not versions of one article). Treat the suffix as part of the identifier — never strip it, and don't assume article numbers are gapless. When unsure which one applies, use `get_fedlex_outline` rather than guessing.
- **Cantonal name collisions**: federal abbreviations (`OR`, `ZGB`, `StGB`, `BV`) are effectively unique nationally, but cantons can reuse generic names (multiple cantons each have a "Baugesetz") for unrelated laws. Always pass the canton explicitly to `search_cantonal_law` — never resolve cantonal law by name alone.
- **Ambiguous case citations**: if a citation doesn't parse cleanly against the formats in `references/citation-formats.md`, run `search_entscheidsuche` with the raw string first to surface candidates before assuming a format.

## Tool selection at a glance

| Task | Call sequence |
|---|---|
| Statute, article known | `resolve_fedlex_statute` → `get_fedlex_article` |
| Statute, full text | `resolve_fedlex_statute` → `get_fedlex_text` |
| Statute, article unknown | `resolve_fedlex_statute` → `get_fedlex_outline` → `get_fedlex_article` |
| Statute, historical version | `get_fedlex_text --as_of <date>` or `list_fedlex_versions` → `get_fedlex_text` |
| Case law, citation known | `search_entscheidsuche "<citation>"` → `get_entscheidsuche_document` |
| Case law, citation chain | `get_entscheidsuche_citations` (follow references) |
| Cantonal law | `search_cantonal_law "<term>" --canton <code>` → `get_cantonal_law` |

## Reference material

See `references/citation-formats.md` for citation formats and canton codes.
