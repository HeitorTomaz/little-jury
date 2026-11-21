"""Answer-shape statistics for diversity.md.

Usage:
    python method/scripts/stats.py rounds/v<version>

Counts the words of each saved answer (r1-*.md, r2-*.md, r3-*.md and r4-*-v*.md replies), reads the
model from the three-line header the moderator writes, and shows the mean per round and per model,
and how many answers have the same number of headings (a sign of uniform shape).
Does not count the moderator's files (scenarios, agenda, pack, debate, syntheses).
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

ANSWER = re.compile(r"^(r[123])-(?!scenarios)[a-z0-9-]+\.md$|^(r4)-[^-]+-[a-z0-9-]+-v\d+\.md$")


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    folder = Path(sys.argv[1])
    rows = []
    for f in sorted(folder.glob("r*.md")):
        m = ANSWER.match(f.name)
        if not m:
            continue
        rnd = m.group(1) or m.group(2)
        text = f.read_text(encoding="utf-8")
        head = "\n".join(text.splitlines()[:5]).lower()
        mm = re.search(r"model[^a-z]*([a-z0-9.-]+)", head)
        model = mm.group(1) if mm else "?"
        words = len(re.findall(r"\w+", text))
        headings = len(re.findall(r"^#{1,6} ", text, re.M))
        rows.append((rnd, f.name, model, words, headings))

    if not rows:
        print("No answers found.")
        return 1
    print("file | round | model | words | headings")
    for rnd, name, model, words, headings in rows:
        print(f"{name} | {rnd} | {model} | {words} | {headings}")

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
