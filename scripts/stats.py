"""Answer-shape statistics for diversity.md.

Usage:
    python method/scripts/stats.py rounds/v<version>

Reads the one-file-per-round layout (r1.md, r2.md, r3.md and r4-debate-replies.md). Each answer is a
section that starts with a `## ` heading followed by a `- Model: <model> (<agent type>)` line; headings
inside an answer are part of the answer, not new sections. Counts the words of each answer and shows
the mean per round and per model, and how many answers have the same number of headings (a sign of
uniform shape). Does not count the moderator's files (scenarios, agenda, pack, debate synthesis).
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

ROUND_FILES = (("r1", "r1.md"), ("r2", "r2.md"), ("r3", "r3.md"), ("r4", "r4-debate-replies.md"))
MODEL_LINE = re.compile(r"^-\s*Model:\s*([A-Za-z0-9.-]+)", re.I)


def confined(path_str, write=False):
    """Resolve a path and refuse it unless it is inside the current folder.

    During a run the current folder is panel/, and these scripts are allowed to run without asking.
    They must not become a way around the read block (reading files outside the panel) or around
    the write protection (overwriting the method, its scripts or the settings).
    """
    base = Path.cwd().resolve()
    target = Path(path_str).resolve()
    try:
        rel = target.relative_to(base)
    except ValueError:
        raise SystemExit(f"Refusing {path_str}: it is outside the current folder ({base}).")
    if write and rel.parts and rel.parts[0].lower() in ("method", ".claude"):
        raise SystemExit(f"Refusing to write {path_str}: method/ and .claude/ are read-only.")
    return path_str


def sections(text: str):
    """Yield (title, model, body) for each answer section of a round file."""
    lines = text.splitlines()
    starts = []
    for i, line in enumerate(lines):
        if not line.startswith("## "):
            continue
        following = [l for l in lines[i + 1:i + 4] if l.strip()]
        if following and MODEL_LINE.match(following[0]):
            starts.append(i)
    for k, i in enumerate(starts):
        end = starts[k + 1] if k + 1 < len(starts) else len(lines)
        block = lines[i + 1:end]
        model = "?"
        body = []
        for line in block:
            mm = MODEL_LINE.match(line)
            if mm and model == "?":
                model = mm.group(1).lower()
                continue
            if model != "?" and not body and re.match(r"^-\s*Date:", line, re.I):
                continue
            body.append(line)
        yield lines[i][3:].strip(), model, "\n".join(body)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    folder = Path(confined(sys.argv[1]))
    rows = []
    for rnd, name in ROUND_FILES:
        f = folder / name
        if not f.exists():
            continue
        for title, model, body in sections(f.read_text(encoding="utf-8")):
            words = len(re.findall(r"\w+", body))
            headings = len(re.findall(r"^#{1,6} ", body, re.M))
            rows.append((rnd, title, model, words, headings))

    if not rows:
        print("No answers found.")
        return 1
    print("answer | round | model | words | headings")
    for rnd, title, model, words, headings in rows:
        print(f"{title} | {rnd} | {model} | {words} | {headings}")

    def means(k):
        groups = defaultdict(list)
        for r in rows:
            groups[k(r)].append(r[3])
        return {g: (round(sum(v) / len(v)), len(v)) for g, v in sorted(groups.items())}

    print("\nMean words per round:", {g: f"{m} ({n})" for g, (m, n) in means(lambda r: r[0]).items()})
    print("Mean words per round and model:",
          {g: f"{m} ({n})" for g, (m, n) in means(lambda r: f"{r[0]}/{r[2]}").items()})
    per_round = defaultdict(list)
    for r in rows:
        per_round[r[0]].append(r[4])
    for rnd, hs in sorted(per_round.items()):
        most = max(set(hs), key=hs.count)
        print(f"{rnd}: {hs.count(most)} of {len(hs)} answers with {most} headings")
    return 0


if __name__ == "__main__":
    sys.exit(main())
