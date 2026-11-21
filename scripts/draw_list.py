"""Draw the order of the rows of a Markdown-table list, one order per agent.

Usage:
    python method/scripts/draw_list.py input/03-list.md --agents casual,skeptic,publishing \
        --seed 20261120 --out rounds/v1/list-draw.json

Reads the first Markdown table in the file (header, separator and rows). The item is the first cell
of each row, without markup. Each agent's order depends only on the seed and the agent id, so the
draw is reproducible. Writes a JSON with each agent's order and the table ready for its prompt, and
prints the tables.
"""

import argparse
import json
import random
import re
import sys
from pathlib import Path


def read_table(text: str):
    lines = text.splitlines()
    for i in range(len(lines) - 1):
        if lines[i].strip().startswith("|") and re.match(r"^\s*\|?\s*:?-{3,}", lines[i + 1]):
            header, separator = lines[i], lines[i + 1]
            body = []
            for line in lines[i + 2:]:
                if not line.strip().startswith("|"):
                    break
                body.append(line)
            return header, separator, body
    raise SystemExit("No Markdown table found in the file.")


def item_of(line: str) -> str:
    first = line.strip().strip("|").split("|")[0]
    return re.sub(r"[*_`]", "", first).strip()


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("list")
    ap.add_argument("--agents", required=True, help="comma-separated ids")
    ap.add_argument("--seed", required=True, type=int)
    ap.add_argument("--output", "--out", dest="out", required=True)
    a = ap.parse_args()

    header, separator, body = read_table(Path(a.list).read_text(encoding="utf-8"))
    if len(body) < 2:
        raise SystemExit("The table needs at least two rows to draw.")
    items = [item_of(l) for l in body]
    if len(set(items)) != len(items):
        raise SystemExit("There are repeated items in the first column.")

    agents = [x.strip() for x in a.agents.split(",") if x.strip()]
    result = {"file": a.list, "seed": a.seed, "items": items, "agents": {}}
    for agent in agents:
        rng = random.Random(f"{a.seed}:{agent}")
        idx = list(range(len(body)))
        rng.shuffle(idx)
        table = "\n".join([header, separator] + [body[i] for i in idx])
        result["agents"][agent] = {"order": [items[i] for i in idx], "table": table}

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    for agent, data in result["agents"].items():
        print(f"## {agent}\n{data['table']}\n")
    print(f"Seed {a.seed}; draw saved to {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
