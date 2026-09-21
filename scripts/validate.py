#!/usr/bin/env python3
"""Validate the iuslink-skills repository.

Standard library only. Checks every */SKILL.md frontmatter, the relative
paths quoted in backticks, version consistency across the three manifests
and the skills' metadata.version, and the README skills table.
Exit status is non-zero when any check fails.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MANIFESTS = {
    "package.json": lambda d: d["version"],
    ".claude-plugin/plugin.json": lambda d: d["version"],
    ".claude-plugin/marketplace.json": lambda d: d["plugins"][0]["version"],
}

failures: list[str] = []
passes: list[str] = []


def ok(msg: str) -> None:
    passes.append(msg)


def fail(msg: str) -> None:
    failures.append(msg)


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse_frontmatter(text: str) -> dict | None:
    """Minimal line-based YAML parser for the frontmatter shape used here.

    Supports `key: value` at the top level and a single level of nested
    `key:` blocks with two-space indented `sub: value` lines.
    """
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    block = text[4:end]
    data: dict = {}
    current: str | None = None
    for raw in block.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith("  ") and current is not None:
            key, sep, value = raw.strip().partition(":")
            if not sep:
                return None
            data[current][key.strip()] = unquote(value)
            continue
        if raw.startswith((" ", "\t")):
            return None
        key, sep, value = raw.partition(":")
        if not sep:
            return None
        key = key.strip()
        if value.strip() == "":
            data[key] = {}
            current = key
        else:
            data[key] = unquote(value)
            current = None
    return data


def check_skill(skill_dir: Path) -> dict | None:
    rel = skill_dir.name + "/SKILL.md"
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    if fm is None:
        fail(f"{rel}: missing or invalid frontmatter")
        return None
    ok(f"{rel}: frontmatter parses")

    name = fm.get("name")
    if not isinstance(name, str) or not name:
        fail(f"{rel}: frontmatter has no name")
    else:
        if name != skill_dir.name:
            fail(f"{rel}: name {name!r} differs from directory name {skill_dir.name!r}")
        else:
            ok(f"{rel}: name matches directory")
        if not NAME_RE.match(name) or len(name) > 64:
            fail(f"{rel}: name {name!r} must match {NAME_RE.pattern} and be at most 64 characters")
        else:
            ok(f"{rel}: name is well-formed")

    desc = fm.get("description")
    if not isinstance(desc, str) or not desc.strip():
        fail(f"{rel}: description missing")
    elif len(desc) > 1024:
        fail(f"{rel}: description is {len(desc)} characters (limit 1024)")
    else:
        ok(f"{rel}: description present ({len(desc)} characters)")

    check_paths(skill_dir, text, rel)
    for ref in skill_dir.glob("references/*.md"):
        check_paths(ref.parent, ref.read_text(encoding="utf-8"), f"{skill_dir.name}/references/{ref.name}")
    return fm


PATH_RE = re.compile(r"`((?:\.\./[a-z0-9-]+/SKILL\.md)|(?:(?:\.\./)?references/[A-Za-z0-9_./-]+))`")


def check_paths(base: Path, text: str, rel: str) -> None:
    seen = set()
    for match in PATH_RE.finditer(text):
        target = match.group(1)
        if target in seen:
            continue
        seen.add(target)
        if not (base / target).is_file():
            fail(f"{rel}: referenced path `{target}` does not exist")
        else:
            ok(f"{rel}: `{target}` exists")


def check_versions(skill_versions: dict[str, str | None]) -> None:
    versions: dict[str, str] = {}
    for path, getter in MANIFESTS.items():
        try:
            versions[path] = getter(json.loads((ROOT / path).read_text(encoding="utf-8")))
        except (OSError, KeyError, IndexError, json.JSONDecodeError) as exc:
            fail(f"{path}: cannot read version ({exc})")
    for skill, version in skill_versions.items():
        if version is None:
            fail(f"{skill}/SKILL.md: metadata.version missing")
        else:
            versions[f"{skill}/SKILL.md (metadata.version)"] = version
    distinct = set(versions.values())
    if len(distinct) == 1 and versions:
        ok(f"version {distinct.pop()} is consistent across {len(versions)} files")
    elif versions:
        fail("version mismatch: " + ", ".join(f"{k}={v}" for k, v in sorted(versions.items())))


def check_readme(skills: dict[str, dict | None]) -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    rows: dict[str, str] = {}
    for line in readme.splitlines():
        m = re.match(r"^\|\s*\[`([a-z0-9-]+)`\]\([^)]*\)\s*\|\s*(.*?)\s*\|\s*$", line)
        if m:
            rows[m.group(1)] = m.group(2)
    for skill, fm in skills.items():
        if skill not in rows:
            fail(f"README.md: skills table has no row for {skill}")
            continue
        expected = (fm or {}).get("description")
        if expected is None:
            continue
        if rows[skill] != expected:
            fail(f"README.md: description for {skill} differs from its frontmatter description")
        else:
            ok(f"README.md: row for {skill} matches frontmatter")


def main() -> int:
    skill_dirs = sorted(p.parent for p in ROOT.glob("*/SKILL.md"))
    if not skill_dirs:
        fail("no */SKILL.md found")
    skills: dict[str, dict | None] = {}
    for skill_dir in skill_dirs:
        skills[skill_dir.name] = check_skill(skill_dir)
    check_versions({
        name: (fm or {}).get("metadata", {}).get("version") if isinstance((fm or {}).get("metadata"), dict) else None
        for name, fm in skills.items()
    })
    check_readme(skills)

    for msg in passes:
        print(f"PASS  {msg}")
    for msg in failures:
        print(f"FAIL  {msg}")
    print(f"\n{len(passes)} passed, {len(failures)} failed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
