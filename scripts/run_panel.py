"""Run (or resume) the panel in a new Claude Code session isolated inside panel/.

Usage:
    python run_panel.py <path/to/panel> [--open]

The run cannot happen in the session that prepared the panel, because that session sees the
concept, the code and what was removed from the inputs. This script starts `claude -p` with the
working directory in panel/, where the read blocking, the CLAUDE.md exclusions and the absence of
git state apply (see check_isolation.py), and allows only the tools the method needs. There are no
stops: the moderator goes all the way to the report and only stops if an isolation test fails.

If rounds/ already holds an unfinished run, the new session resumes it from progress.md.

Output saved in panel/runs/<date-time>.txt. Exit codes:
    0  finished: there is a new report.html
    2  interrupted (usage limit, failed isolation or another reason): see the output
    1  could not start
"""

import argparse
import shutil
import subprocess
import sys
import time
import webbrowser
from datetime import datetime
from pathlib import Path

TOOLS = ",".join([
    "Read", "Write", "Edit", "Glob", "Grep", "Agent", "WebSearch", "WebFetch",
    "Bash(python method/scripts/*)", "Bash(python3 method/scripts/*)",
    "Bash(python -I method/scripts/*)", "Bash(python3 -I method/scripts/*)",
    "Bash(claude --version)",
])

PROMPT = """Read method/run.md and follow it to run this panel to the end, with no stops.

If rounds/ already holds an unfinished run (progress.md without round 5 finished), resume it as the method's resume section says. Otherwise, start a new run.

The author is not available during the run and must not be asked anything. Only stop if an isolation test fails; in that case, explain what happened and do not work around it.

When you finish, answer in the language set in config.md with: the full path of report.html, a ten-line summary of what the panel concluded, and a short list of what you found ambiguous, contradictory or hard to follow in the method itself."""


def reports(panel: Path) -> dict:
    return {p: p.stat().st_mtime for p in (panel / "rounds").glob("*/report.html")}


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("panel")
    ap.add_argument("--open", action="store_true", help="open the report in the browser when done")
    a = ap.parse_args()

    panel = Path(a.panel).resolve()
    if not (panel / "method" / "run.md").exists() or not (panel / ".claude" / "settings.json").exists():
        print(f"ERROR: {panel} is not an assembled panel (method/ or .claude/settings.json is missing).")
        return 1
    claude = shutil.which("claude")
    if not claude:
        print("ERROR: the 'claude' command was not found on PATH.")
        return 1

    check = subprocess.run([sys.executable, "-I", "method/scripts/check_isolation.py"],
                           cwd=panel, capture_output=True, text=True, encoding="utf-8")
    if check.returncode != 0:
        print(check.stdout + check.stderr)
        print("ERROR: the context exclusions do not match this folder. Run assemble_panel.py again.")
        return 1

    before = reports(panel)
    (panel / "runs").mkdir(exist_ok=True)
    log = panel / "runs" / (datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt")
    start = time.time()
    print(f"Isolated run started in {panel} (output in {log}). It can take from tens of minutes to hours.")
    sys.stdout.flush()
    with open(log, "w", encoding="utf-8") as out:
        proc = subprocess.run([claude, "-p", PROMPT, "--allowedTools", TOOLS, "--output-format", "text"],
                              cwd=panel, stdout=out, stderr=subprocess.STDOUT, text=True, encoding="utf-8")
    text = log.read_text(encoding="utf-8")
    minutes = round((time.time() - start) / 60)

    new = [p for p, t in reports(panel).items() if p not in before or t > before[p]]
    if proc.returncode == 0 and new:
        report = max(new, key=lambda p: p.stat().st_mtime)
        print(f"Finished in {minutes} min. Report: {report}")
        if a.open:
            webbrowser.open(report.as_uri())
        print("\n--- moderator's answer ---\n" + text[-6000:])
        return 0

    limit = "limit" in text.lower() and ("hit" in text.lower() or "reset" in text.lower())
    reason = "plan usage limit" if limit else f"code {proc.returncode}, no new report"
    print(f"Interrupted after {minutes} min ({reason}).")
    print("To resume: run this script again (or /mock-jury run at the project root)"
          + (" after the limit resets." if limit else "."))
    print("\n--- end of output ---\n" + text[-3000:])
    return 2


if __name__ == "__main__":
    sys.exit(main())
