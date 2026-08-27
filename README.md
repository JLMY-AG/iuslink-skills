# iuslink-skills

[Claude Code Agent Skills](https://docs.claude.com/en/docs/claude-code/skills) for working with [iuslink](https://github.com/kevinzehnder/iuslink) — the deterministic, version-aware MCP server for Swiss legal primary sources (Fedlex, Entscheidsuche/BGE, LexFind).

iuslink is the retrieval layer; these skills are the workflows on top of it — how to pick the right tool, resolve a citation, pull a historical version of a statute, or walk a case-law citation chain, without the agent guessing or citing from memory.

## Install

Copy the skill folder you want into your project's or global `.claude/skills/` directory:

```bash
git clone https://github.com/kevinzehnder/iuslink-skills.git
cp -r iuslink-skills/swiss-legal-research ~/.claude/skills/
```

Or clone the whole repo into `.claude/skills/` if you want every skill available.

## Skills

| Skill | Description |
|---|---|
| [`swiss-legal-research`](./swiss-legal-research/SKILL.md) | Swiss legal research workflows for federal legislation (Fedlex), cantonal law (LexFind), and case law (Entscheidsuche/BGE). |

## License

MIT — see [LICENSE](./LICENSE).
