"""Compute and check the panel's context exclusions.

Usage (in the run session, inside panel/):
    python method/scripts/check_isolation.py

Claude Code loads CLAUDE.md, CLAUDE.local.md and .claude/rules/ from the folders ABOVE the working
directory, and puts the git state (branch, recent commits) in the context. For a panel inside a
repository, that would bring the project's instructions and decision history into the run session.
The panel's .claude/settings.json prevents it with:
  - "claudeMdExcludes": one pattern per possible instruction file in each folder above;
  - "includeGitInstructions": false.

This script only does arithmetic on the folder path: it does not read or list anything outside it.
It checks that settings.json has the patterns that match the panel's CURRENT location (if the folder
was moved, the old patterns no longer apply) and exits with code 1 if anything is missing.

The .claude/ in the user's home folder (their global instructions) is not excluded.
"""

import json
import sys
from pathlib import Path

FILES = ["CLAUDE.md", "CLAUDE.local.md", ".claude/CLAUDE.md", ".claude/rules/**"]


def exclusion_patterns(panel: Path) -> list[str]:
    panel = panel.resolve()
    home = Path.home().resolve()
    patterns = []
    for folder in panel.parents:
        base = folder.as_posix().rstrip("/")
        no_drive = base.split(":", 1)[1] if ":" in base[:3] else base
        for name in FILES:
            if folder == home and name.startswith(".claude/"):
                continue  # the user's global instructions stay
            patterns.append(f"{base}/{name}")
            # Variant without the drive letter, in case the path is compared in another format.
            if no_drive != base:
                patterns.append(f"**{no_drive}/{name}")
    return patterns


def expected_settings(panel: Path) -> dict:
    return {
        "permissions": {"blockReadsOutsideWorkingDirectories": True},
        "includeGitInstructions": False,
        "claudeMdExcludes": exclusion_patterns(panel),
    }


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    panel = Path.cwd()
    settings_file = panel / ".claude" / "settings.json"
    if not settings_file.exists():
        print("ERROR: .claude/settings.json does not exist in this folder.")
        return 1
    current = json.loads(settings_file.read_text(encoding="utf-8"))
    expected = expected_settings(panel)
    errors = []
    if current.get("permissions", {}).get("blockReadsOutsideWorkingDirectories") is not True:
        errors.append("permissions.blockReadsOutsideWorkingDirectories is not true")
    if current.get("includeGitInstructions") is not False:
        errors.append("includeGitInstructions is not false (the git state would enter the context)")
    missing = [p for p in expected["claudeMdExcludes"] if p not in current.get("claudeMdExcludes", [])]
    if missing:
        errors.append(f"{len(missing)} claudeMdExcludes pattern(s) missing for the current location "
                      f"(was the folder moved?), for example: {missing[0]}")
    for e in errors:
        print(f"ERROR: {e}")
    if errors:
        print("Fix it by running the skill's assemble_panel.py again from the prepare session, or ask the author.")
        return 1
    print(f"Exclusions checked: {len(expected['claudeMdExcludes'])} patterns, read blocking on, "
          "git state out of the context.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
