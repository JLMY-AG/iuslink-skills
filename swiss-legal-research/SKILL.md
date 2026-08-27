---
name: swiss-legal-research
description: Swiss legal research workflows for federal legislation (Fedlex), cantonal law (LexFind), and case law (Entscheidsuche/BGE). Use for any query requiring authoritative Swiss legal sources.
allowed-tools: resolve_fedlex_statute get_fedlex_article get_fedlex_text get_fedlex_outline list_fedlex_versions search_entscheidsuche get_entscheidsuche_document get_entscheidsuche_citations search_cantonal_law get_cantonal_law
---

## Source‑of‑Truth Rule (mandatory)

Never cite, quote, or rely on legal text from memory or prior model knowledge. Always retrieve the current official source via iuslink before using any statute or case.

## Tool‑selection guardrails

- **Fedlex** – use for federal statutes (SR numbers, abbreviations like ZGB, OR, BV, StGB). 
- **LexFind** – use for cantonal legislation or when a cross‑jurisdiction search is required. 
- **Entscheidsuche** – use for jurisprudence (BGE, ATF, DTF, docket numbers).

## Typical workflows

1. **Statute lookup**
   ```text
   resolve_fedlex_statute → get_fedlex_article   (single article)
   resolve_fedlex_statute → get_fedlex_text      (full text)
   resolve_fedlex_statute → get_fedlex_outline → get_fedlex_article   (unknown article)
   ```
2. **Historical version**
   ```text
   get_fedlex_text --as_of YYYY‑MM‑DD
   or
   list_fedlex_versions → pick version_uri → get_fedlex_text
   ```
3. **Case law search**
   ```text
   search_entscheidsuche "BGE 140 III 86" → get_entscheidsuche_document (format=text)
   get_entscheidsuche_citations → follow citation chain
   ```
4. **Cantonal law**
   ```text
   search_cantonal_law "Baugesetz" --canton ZH → get_cantonal_law
   ```

## Reference material

When the agent needs to parse citation formats or canton codes, consult the files in the `references/` folder.
