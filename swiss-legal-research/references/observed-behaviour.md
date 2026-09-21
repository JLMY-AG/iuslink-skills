# Observed behaviour of the live iuslink server (as of 2026-08-27)

One dated bullet per observation. These are the concrete runs behind the rules in `../SKILL.md`; they describe the server at the time noted and may change.

- 2026-08-27 — `get_fedlex_article` asked for `28bis` on the ZGB returned an error listing the valid neighbours `28, 28a, 28b, 28c, ...`; the same letter suffixes (`Art. 28a`) appear in the German ZGB and the French Code civil text.
- 2026-08-27 — `search_cantonal_law` for "Baugesetz" in Aargau returned both the active `Gesetz über Raumentwicklung und Bauwesen` and the inactive `Allgemeine Verordnung zum Baugesetz` (`is_active: false`) in one result list.
- 2026-08-27 — `search_entscheidsuche` with the natural-language query "what happens when a tenant terminates a lease early without justification" returned 0 hits with a hint to use shorter terms; the keyword query `Mietrecht Kündigung` returned hundreds.
- 2026-08-27 — `search_entscheidsuche` for `Mietrecht Kündigung` with no filters returned 907 results, the top hits coming from a St. Gallen insurance court and an Aargau commercial court, with no Bundesgericht decision in the top 3. Adding `courts: ["CH_BGer"]` and `sort: "relevance"` reduced this to 162 results with the top 3 all on-point Bundesgericht decisions on lease termination.
- 2026-08-27 — `get_entscheidsuche_document`: the tool description stated a default `format` of `json` (metadata only) while the schema enforced `text` (full body).
- 2026-08-27 — `get_entscheidsuche_document` with `format: "json"` returned structured metadata (abstract in three languages, docket references) for a Bundesgericht/BGE decision but no body at all for a cantonal Handelsgericht decision whose full text was available with `format: "text"`.
- 2026-08-27 — `get_entscheidsuche_document` with an unresolvable signature failed with "document text was not found; verify signature/spider or use search_entscheidsuche first" instead of returning nulls.
- 2026-08-27 — `search_cantonal_law` with `cantons: ["ZH", "BE"]` returned one result block per canton, concatenated in the order given.
