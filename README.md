# iuslink-skills

[Claude Code Agent Skills](https://docs.claude.com/en/docs/claude-code/skills) for working with [iuslink](https://github.com/kevinzehnder/iuslink) — the deterministic, version-aware MCP server for Swiss legal primary sources (Fedlex, Entscheidsuche/BGE, LexFind).

iuslink is the retrieval layer; these skills are the workflows on top of it — how to pick the right tool, resolve a citation, pull a historical version of a statute, or walk a case-law citation chain, without the agent guessing or citing from memory.

## Prerequisite

Install and configure the [iuslink](https://github.com/kevinzehnder/iuslink) tools in your agent harness first. This package installs workflows, not the retrieval server.

## Install

### Claude Code plugin

Run inside Claude Code:

```text
/plugin marketplace add JLMY-AG/iuslink-skills
/plugin install iuslink-skills@iuslink-skills
```

### Pi package

Run in your shell:

```bash
pi install git:github.com/JLMY-AG/iuslink-skills
```

For a local checkout instead:

```bash
pi install /absolute/path/to/iuslink-skills
```

Restart Pi or run `/reload`, then invoke `/skill:swiss-legal-gutachten` or let Pi select a skill from its description.

### OMP plugin

Pi and OMP keep separate package registries. Install the same marketplace plugin explicitly in OMP:

```bash
omp plugin marketplace add JLMY-AG/iuslink-skills
omp plugin install iuslink-skills@iuslink-skills
omp plugin list
```

To update an existing installation:

```bash
omp plugin marketplace update iuslink-skills
omp plugin upgrade iuslink-skills@iuslink-skills
```

Restart OMP, then invoke `/skill:swiss-legal-gutachten`.

### Manual Agent Skills installation

Copy individual skill directories into a supported skills location such as `~/.claude/skills/`, `~/.pi/agent/skills/`, or a project-local equivalent. `swiss-legal-deep-research` builds on `swiss-legal-research`; `swiss-legal-gutachten` uses both, so install all three for the complete opinion workflow.

## Skills

| Skill | Description |
|---|---|
| [`swiss-legal-research`](./swiss-legal-research/SKILL.md) | Swiss legal research workflows for federal legislation (Fedlex), cantonal law (LexFind), and case law (Entscheidsuche/BGE) via the iuslink tools. Use when a query needs authoritative Swiss legal sources: statutes and articles (OR, ZGB, StGB, BV, SR numbers, Bundesgesetz, Verordnung, loi fédérale, ordonnance), historical versions, Bundesgericht/BGE/Tribunal fédéral decisions, or cantonal enactments (kantonales Recht, droit cantonal). For multi-issue or comparative research use swiss-legal-deep-research; for a legal opinion (Gutachten) use swiss-legal-gutachten. |
| [`swiss-legal-deep-research`](./swiss-legal-deep-research/SKILL.md) | Orchestrates primary-source research for complex, comparative, or unsettled Swiss legal questions (Rechtsfrage, question juridique) across federal and cantonal law, building on swiss-legal-research and the iuslink tools. Use for multi-part, cross-jurisdiction (mehrere Kantone, interkantonal), or genuinely unclear questions. Not for direct statute, citation, or single-issue retrieval (use swiss-legal-research) and not for a full legal opinion (use swiss-legal-gutachten). |
| [`swiss-legal-gutachten`](./swiss-legal-gutachten/SKILL.md) | Produces a neutral Swiss legal opinion (Gutachten, Rechtsgutachten, avis de droit, parere legale) that applies verified primary sources to stated facts, issue by issue, with counterarguments and calibrated confidence. Use for legal assessment and application of Swiss federal or cantonal law to a case (Sachverhalt, rechtliche Würdigung, Fallbeurteilung). Not for direct source retrieval (use swiss-legal-research) and not for drafting a court pleading. |

## License

MIT — see [LICENSE](./LICENSE).
