# Citation formats

## Published Federal Supreme Court decisions (BGE / ATF / DTF)

- Format: `BGE <volume> <part> <page>`
- Example: `BGE 140 III 86`
- Parts: I constitutional law, II administrative law, III civil law and debt enforcement, IV criminal law, V social insurance law.
- Pinpoint a consideration with `E.` (German) or `consid.` (French), e.g. `BGE 140 III 86 E. 2.3`.
- iuslink court code for this collection: `CH_BGE`.

## Unpublished / all Federal Supreme Court decisions by docket number

- Format: `<division code>_<number>/<year>`
- Example: `6B_123/2022` (a decision of the Federal Supreme Court, not a cantonal court).
- Cite with date and consideration, e.g. `Urteil des Bundesgerichts 6B_123/2022 vom <date> E. 1.2`.
- The letter-digit prefix identifies the deciding division; the year is the filing year. Do not interpret the prefix from memory: resolve the docket through `search_entscheidsuche`.
- iuslink court code: `CH_BGer`.

## Cantonal court decisions

There is no uniform format. Every canton and court uses its own docket scheme, and citation practice differs between them. Do not force a cantonal reference into the federal pattern. Resolve the raw string with `search_entscheidsuche` (optionally filtered to the relevant court) and cite what the retrieved record shows: court, docket, date, consideration.

## Legislation (SR / RS numbers)

- Format: `SR <number>`
- Example: `SR 220` (Obligationenrecht)
- Article citations: `Art. 28a Abs. 1 ZGB`. Inserted articles use letters, not Latin ordinals (`28a`, not `28bis`).

## Ambiguous citations

If a citation does not parse cleanly, follow the ambiguity rule in `../SKILL.md` (search the raw string first).

## Canton codes for the `cantons` argument of `search_cantonal_law`

| Code | Canton |
|---|---|
| CH | Federal law as indexed by LexFind (metadata only; use the Fedlex tools for federal statutes) |
| AG | Aargau |
| AI | Appenzell Innerrhoden |
| AR | Appenzell Ausserrhoden |
| BE | Bern |
| BL | Basel-Landschaft |
| BS | Basel-Stadt |
| FR | Fribourg |
| GE | Genève |
| GL | Glarus |
| GR | Graubünden |
| JU | Jura |
| LU | Luzern |
| NE | Neuchâtel |
| NW | Nidwalden |
| OW | Obwalden |
| SG | St. Gallen |
| SH | Schaffhausen |
| SO | Solothurn |
| SZ | Schwyz |
| TG | Thurgau |
| TI | Ticino |
| UR | Uri |
| VD | Vaud |
| VS | Valais |
| ZG | Zug |
| ZH | Zürich |
