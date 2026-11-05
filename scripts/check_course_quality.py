#!/usr/bin/env python3
"""Run lightweight, non-destructive checks for the Python 200-program course."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = set(range(1, 201))
EXCLUDED_PARTS = {".git", ".venv", "venv", "env", "__pycache__"}
RANGE_PATTERN = re.compile(r"^(\d+)-(\d+)$")


def folder_bounds(folder_name: str) -> tuple[int, int] | None:
    if folder_name.lower() == "basic_first_10":
        return (1, 10)
    match = RANGE_PATTERN.match(folder_name)
    if match:
        return int(match.group(1)), int(match.group(2))
    return None


def exercise_number(path: Path) -> int | None:
    # Accept a numeric filename (for example, 21.py) or a challenge filename
    # ending in its number (for example, challenge21.py).
    match = re.search(r"(\d+)\D*$", path.stem)
    if match is None:
        return None
    raw_number = int(match.group(1))
    folder_name = path.parent.parent.name if "challenge" in path.parent.name.lower() else path.parent.name
    bounds = folder_bounds(folder_name)
    if bounds is None:
        return None
    lower, upper = bounds
    if lower <= raw_number <= upper:
        return raw_number
    return None


def collect_numbered(paths: list[Path]) -> tuple[dict[int, Path], int]:
    found: dict[int, Path] = {}
    duplicates = 0
    for path in sorted(paths):
        number = exercise_number(path)
        if number is None:
            # Ignore helper files without an exercise number, but flag a
            # numbered file whose number does not belong to its folder.
            if re.search(r"\d+\D*$", path.stem):
                print(f"INVALID numbered exercise file: {path.relative_to(ROOT)}")
                duplicates += 1
            continue
        if number in found:
            print(f"DUPLICATE {number}: {found[number].relative_to(ROOT)} and {path.relative_to(ROOT)}")
            duplicates += 1
        else:
            found[number] = path
    return found, duplicates


def is_excluded(path: Path) -> bool:
    return any(part in EXCLUDED_PARTS for part in path.parts)


def main() -> int:
    program_paths = [
        p for p in ROOT.glob("*/*.py")
        if not any("challenge" in part.lower() for part in p.parts)
        and folder_bounds(p.parent.name) is not None
    ]
    challenge_paths = [
        p for p in ROOT.rglob("*.py")
        if "challenge" in p.parent.name.lower()
        and folder_bounds(p.parent.parent.name) is not None
        and not is_excluded(p.relative_to(ROOT))
    ]

    programs, duplicate_programs = collect_numbered(program_paths)
    challenges, duplicate_challenges = collect_numbered(challenge_paths)
    problems = duplicate_programs + duplicate_challenges

    for label, found in (("programs", programs), ("challenges", challenges)):
        missing = sorted(EXPECTED - set(found))
        extra = sorted(set(found) - EXPECTED)
        print(f"{label.title()}: found {len(found)} of 200 numbered files")
        if missing:
            print(f"  Missing {label}: {missing}")
            problems += 1
        if extra:
            print(f"  Unexpected {label}: {extra}")
            problems += 1

    python_files = [
        p for p in ROOT.rglob("*.py")
        if not is_excluded(p.relative_to(ROOT))
    ]
    syntax_errors = []
    for path in python_files:
        try:
            source = path.read_text(encoding="utf-8")
            compile(source, str(path), "exec")
        except (OSError, UnicodeError, SyntaxError) as exc:
            syntax_errors.append((path, exc))

    print(f"Python syntax: checked {len(python_files)} files")
    if syntax_errors:
        for path, exc in syntax_errors:
            print(f"  SYNTAX/READ ERROR {path.relative_to(ROOT)}: {exc}")
        problems += len(syntax_errors)

    try:
        tracked_bytecode = subprocess.run(
            ["git", "-C", str(ROOT), "ls-files", "*.pyc", "*.pyo"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.splitlines()
    except (OSError, subprocess.CalledProcessError):
        tracked_bytecode = []
        print("Tracked compiled Python files: skipped (Git metadata unavailable)")
    else:
        print(f"Tracked compiled Python files: {len(tracked_bytecode)}")
        if tracked_bytecode:
            for item in tracked_bytecode:
                print(f"  TRACKED BYTECODE: {item}")
            problems += len(tracked_bytecode)

    if problems:
        print(f"\nCHECKS FAILED: {problems} issue(s) found.")
        return 1

    print("\nCHECKS PASSED: numbering, syntax, and tracked bytecode look good.")
    print("Note: this checker does not execute exercises or verify runtime behaviour.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
