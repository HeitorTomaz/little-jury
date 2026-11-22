"""Assemble or update a project's panel/ folder.

Usage:
    python assemble_panel.py <path/to/panel>

What it does:
- generates .claude/settings.json for the folder's current location: blocks reads outside it,
  excludes the CLAUDE.md, CLAUDE.local.md and .claude/rules/ of the folders above, and keeps the git
  state out of the context (see check_isolation.py);
- copies the agent definitions, template/ (report template and fonts) and README.md, replacing
  previous versions (they belong to the skill);
- replaces method/ with the skill's current method plus the run scripts, and warns if the method
  version changed;
- creates input/, input/external/README.md, moderator/ and rounds/ if they don't exist.

Never changes: input/*.md (except creating external/README.md), moderator/, personas.md,
config.md, rounds/.
"""

import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_isolation import expected_settings  # noqa: E402

SKILL = Path(__file__).resolve().parent.parent
PANEL_TEMPLATE = SKILL / "assets" / "panel-template"
METHOD = SKILL / "references" / "method"
RUN_SCRIPTS = ["draw_list.py", "analyze_list.py", "report.py", "check_isolation.py", "stats.py"]

# Skill files: always replaced.
FROM_SKILL = [
    ".claude/agents/persona-isolated.md",
    ".claude/agents/persona-web.md",
    "template/report-template.html",
    "README.md",
]
# Created only if missing.
IF_MISSING = ["input/external/README.md"]


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    target = Path(sys.argv[1]).resolve()
    if target.name != "panel":
        print(f"Warning: the folder is named '{target.name}', not 'panel'. The instructions assume 'panel/'.")
    target.mkdir(parents=True, exist_ok=True)

    settings = target / ".claude" / "settings.json"
    settings.parent.mkdir(parents=True, exist_ok=True)
    data = expected_settings(target)
    settings.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"generated   .claude/settings.json ({len(data['claudeMdExcludes'])} exclusions of CLAUDE.md/rules above the folder)")

    for rel in FROM_SKILL:
        dest = target / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(PANEL_TEMPLATE / rel, dest)
        print(f"copied      {rel}")
    shutil.copytree(PANEL_TEMPLATE / "template" / "fonts", target / "template" / "fonts", dirs_exist_ok=True)
    print("copied      template/fonts/ (report fonts and licenses)")

    for rel in IF_MISSING:
        dest = target / rel
        if dest.exists():
            print(f"kept        {rel}")
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(PANEL_TEMPLATE / rel, dest)
            print(f"created     {rel}")

    method_dest = target / "method"
    new_version = (METHOD / "VERSION.txt").read_text(encoding="utf-8").strip()
    old_version = None
    if (method_dest / "VERSION.txt").exists():
        old_version = (method_dest / "VERSION.txt").read_text(encoding="utf-8").strip()
    if method_dest.exists():
        shutil.rmtree(method_dest)
    shutil.copytree(METHOD, method_dest)
    (method_dest / "scripts").mkdir(exist_ok=True)
    for name in RUN_SCRIPTS:
        shutil.copyfile(SKILL / "scripts" / name, method_dest / "scripts" / name)
    print("copied      method/ (method and run scripts)")
    if old_version and old_version != new_version:
        print("\nWARNING: the method version changed. Tell the author: old and new runs of this")
        print("panel are not directly comparable.")
        print(f"  before: {old_version.splitlines()[0]}")
        print(f"  now:    {new_version.splitlines()[0]}")

    for folder in ["input", "moderator", "rounds"]:
        (target / folder).mkdir(exist_ok=True)

    missing = [
        rel
        for rel in [
            "config.md",
            "personas.md",
            "input/01-short-pitch.md",
            "input/02-full-description.md",
            "moderator/author-concerns.md",
        ]
        if not (target / rel).exists()
        # type work puts the work itself in input/02-work.md (or 02-work-*.md) instead of a description
        and not (rel == "input/02-full-description.md" and any((target / "input").glob("02-work*.md")))
    ]
    if missing:
        print("\nStill missing (write them now):")
        for rel in missing:
            print(f"  {rel}")
        print("  input/03-list.md  (only if there is a list to rank)")
        print("  input/03-criteria.md  (criteria family, only if the author gave the criteria)")
    print(f"\nPanel assembled at {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
