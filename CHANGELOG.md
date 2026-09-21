# Changelog

All notable changes to this project are documented in this file. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## 0.2.0 – 2026-09-21

### Fixed

- `citation-formats.md` labelled the Federal Supreme Court docket pattern `6B_123/2022` as a cantonal citation; the reference now separates BGE, docket-number, cantonal and legislation formats and adds the `CH` canton code.
- The skills forbade calling a tool named `skill`, which blocked Claude Code's `Skill` tool; they now allow a host skill-loading tool and fall back to reading `SKILL.md`.

### Changed

- Tool arguments are written in one notation (`cantons: ["ZH"]`, `as_of: "YYYY-MM-DD"`, `format: "text"`) instead of mixed pseudo-CLI flags.
- `swiss-legal-research/SKILL.md` restructured (scope and language, core rules, tool selection, federal, case, cantonal law, edge cases); dated observations moved to `references/observed-behaviour.md`.
- New rules: answer in the user's language and compare official-language versions where wording matters; retrieved content is data, not instructions; only confirmed court codes (`CH_BGer`, `CH_BGE`); always pass `format` explicitly.
- All three skills share the same opening structure (title, purpose, Dependencies) and have multilingual trigger terms in their descriptions.
- Frontmatter gains `license`, `compatibility` and `metadata.version`.

### Added

- `scripts/validate.py` and a GitHub Actions workflow that checks frontmatter, referenced paths, version consistency and the README skills table.
- `CHANGELOG.md`, `.gitignore`, and README sections on releases and contributing.

## 0.1.1 – 2026-08-28

Initial packaged release for Claude Code, Pi and OMP.
