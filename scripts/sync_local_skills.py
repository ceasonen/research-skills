#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = Path("~/.codex/skills").expanduser()
DEFAULT_DEST = REPO_ROOT / "skills"
DEFAULT_CATALOG = REPO_ROOT / "catalog.json"
SKIP_NAMES = {".DS_Store", "__pycache__"}


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


def ignore_entries(_: str, names: list[str]) -> list[str]:
    return [name for name in names if name in SKIP_NAMES]


def list_skill_dirs(source: Path, include_system: bool) -> list[Path]:
    skill_dirs: list[Path] = []
    for entry in sorted(source.iterdir()):
        if not entry.is_dir():
            continue
        if entry.name.startswith(".") and not (include_system and entry.name == ".system"):
            continue
        if entry.name == ".system" and not include_system:
            continue
        if (entry / "SKILL.md").is_file():
            skill_dirs.append(entry)
    return skill_dirs


def count_files(directory: Path) -> int:
    return sum(1 for path in directory.rglob("*") if path.is_file() and path.name not in SKIP_NAMES)


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


def sync_skills(source: Path, dest: Path, include_system: bool, clean: bool) -> list[dict[str, object]]:
    if not source.is_dir():
        raise FileNotFoundError(f"source directory does not exist: {source}")

    dest.mkdir(parents=True, exist_ok=True)
    source_skills = list_skill_dirs(source, include_system=include_system)
    source_names = {skill_dir.name for skill_dir in source_skills}

    if clean:
        for existing in dest.iterdir():
            if existing.is_dir() and existing.name not in source_names:
                shutil.rmtree(existing)

    for skill_dir in source_skills:
        target_dir = dest / skill_dir.name
        if target_dir.exists():
            shutil.rmtree(target_dir)
        shutil.copytree(skill_dir, target_dir, ignore=ignore_entries)

    return [build_catalog_entry(dest / skill_dir.name) for skill_dir in source_skills]


def write_catalog(path: Path, catalog_entries: list[dict[str, object]]) -> None:
    payload = {
        "skill_count": len(catalog_entries),
        "skills": sorted(catalog_entries, key=lambda entry: str(entry["name"])),
    }
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync local Codex skills into this repository.")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE, help="Source skills directory.")
    parser.add_argument("--dest", type=Path, default=DEFAULT_DEST, help="Destination skills directory.")
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG, help="Catalog JSON output path.")
    parser.add_argument("--clean", action="store_true", help="Remove destination skill folders that no longer exist in source.")
    parser.add_argument("--include-system", action="store_true", help="Include .system skills in the sync.")
    args = parser.parse_args()

    catalog_entries = sync_skills(
        source=args.source.expanduser().resolve(),
        dest=args.dest.resolve(),
        include_system=args.include_system,
        clean=args.clean,
    )
    write_catalog(args.catalog.resolve(), catalog_entries)

    print(f"Synced {len(catalog_entries)} skills into {args.dest.resolve()}")
    print(f"Wrote catalog to {args.catalog.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
