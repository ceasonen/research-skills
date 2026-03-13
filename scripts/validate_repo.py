#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SKILLS_DIR = REPO_ROOT / "skills"
DEFAULT_CATALOG = REPO_ROOT / "catalog.json"
BLOCKED_SKILL_PATTERNS = ("/Users/", "~/.codex/skills", ".codex/skills/")
TEXT_SUFFIXES = {".json", ".md", ".py", ".txt", ".yaml", ".yml"}


def parse_frontmatter(skill_file: Path) -> dict[str, str]:
    lines = skill_file.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"{skill_file} is missing YAML frontmatter")

    data: dict[str, str] = {}
    for line in lines[1:]:
        stripped = line.strip()
        if stripped == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def count_files(directory: Path) -> int:
    return sum(1 for path in directory.rglob("*") if path.is_file() and path.name != ".DS_Store")


def validate_openai_yaml(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    required_markers = (
        "interface:",
        "display_name:",
        "short_description:",
        "default_prompt:",
    )
    for marker in required_markers:
        if marker not in text:
            errors.append(f"{path}: missing `{marker}`")
    return errors


def scan_for_blocked_patterns(skills_dir: Path) -> list[str]:
    errors: list[str] = []
    for file_path in sorted(skills_dir.rglob("*")):
        if not file_path.is_file():
            continue
        if file_path.suffix not in TEXT_SUFFIXES:
            continue
        text = file_path.read_text(encoding="utf-8")
        for pattern in BLOCKED_SKILL_PATTERNS:
            if pattern in text:
                errors.append(f"{file_path}: contains blocked pattern `{pattern}`")
    return errors


def build_catalog_entry(skill_dir: Path) -> dict[str, object]:
    metadata = parse_frontmatter(skill_dir / "SKILL.md")
    name = metadata.get("name")
    description = metadata.get("description")
    if not name or not description:
        raise ValueError(f"{skill_dir}/SKILL.md is missing name or description")
    return {
        "name": name,
        "description": description,
        "path": f"skills/{skill_dir.name}",
        "resources": {
            "agents": (skill_dir / "agents" / "openai.yaml").is_file(),
            "references": (skill_dir / "references").is_dir(),
            "scripts": (skill_dir / "scripts").is_dir(),
            "assets": (skill_dir / "assets").is_dir(),
        },
        "file_count": count_files(skill_dir),
    }


def validate_repo(skills_dir: Path, catalog_path: Path) -> tuple[list[str], list[dict[str, object]]]:
    errors: list[str] = []
    skill_entries: list[dict[str, object]] = []

    if not skills_dir.is_dir():
        return [f"skills directory does not exist: {skills_dir}"], []

    for skill_dir in sorted(path for path in skills_dir.iterdir() if path.is_dir()):
        skill_file = skill_dir / "SKILL.md"
        skill_errors: list[str] = []
        if not skill_file.is_file():
            errors.append(f"{skill_dir}: missing SKILL.md")
            continue

        try:
            metadata = parse_frontmatter(skill_file)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        name = metadata.get("name")
        description = metadata.get("description")
        if not name:
            skill_errors.append(f"{skill_file}: missing `name` in frontmatter")
        if not description:
            skill_errors.append(f"{skill_file}: missing `description` in frontmatter")
        if name and name != skill_dir.name:
            skill_errors.append(f"{skill_file}: frontmatter name `{name}` does not match folder `{skill_dir.name}`")

        openai_yaml = skill_dir / "agents" / "openai.yaml"
        if openai_yaml.exists():
            skill_errors.extend(validate_openai_yaml(openai_yaml))

        errors.extend(skill_errors)
        if not skill_errors:
            try:
                skill_entries.append(build_catalog_entry(skill_dir))
            except ValueError as exc:
                errors.append(str(exc))

    errors.extend(scan_for_blocked_patterns(skills_dir))

    if not catalog_path.is_file():
        errors.append(f"catalog is missing: {catalog_path}")
        return errors, skill_entries

    try:
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"{catalog_path}: invalid JSON ({exc})")
        return errors, skill_entries

    expected_catalog = {
        "skill_count": len(skill_entries),
        "skills": sorted(skill_entries, key=lambda entry: str(entry["name"])),
    }
    if catalog != expected_catalog:
        errors.append(f"{catalog_path}: catalog does not match the current skills directory")

    return errors, skill_entries


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the published skills repository.")
    parser.add_argument("--skills-dir", type=Path, default=DEFAULT_SKILLS_DIR, help="Directory that contains published skill folders.")
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG, help="Catalog JSON file.")
    args = parser.parse_args()

    errors, skill_entries = validate_repo(args.skills_dir.resolve(), args.catalog.resolve())
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    with_references = sum(1 for entry in skill_entries if entry["resources"]["references"])
    with_scripts = sum(1 for entry in skill_entries if entry["resources"]["scripts"])
    print(
        "Validated "
        f"{len(skill_entries)} skills "
        f"({with_references} with references, {with_scripts} with scripts)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
