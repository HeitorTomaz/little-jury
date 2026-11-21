"""Analyze the panel's rankings of a list, including the order effect.

Usage:
    python method/scripts/analyze_list.py rounds/v1/list-draw.json \
        rounds/v1/list-rankings.json --out rounds/v1/list-analysis.json

list-rankings.json:
    {"casual": ["Item B", "Item A", ...], "skeptic": [...],
     "rejections": {"skeptic": ["Item C"]}}

Computes, per item: mean position, first places (and whose), rejections, how many times the item was
received in the first row and how many of those times it was ranked first. Overall: how many agents
ranked first the item they received in the first row, against what chance would give.
"""

import argparse
import json
import sys
import unicodedata
from pathlib import Path


def key(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return "".join(ch for ch in s.lower() if ch.isalnum())


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


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("draw")
    ap.add_argument("rankings")
    ap.add_argument("--output", "--out", dest="out", required=True)
    a = ap.parse_args()
    a.draw, a.rankings = confined(a.draw), confined(a.rankings)
    a.out = confined(a.out, write=True)

    draw = json.loads(Path(a.draw).read_text(encoding="utf-8"))
    data = json.loads(Path(a.rankings).read_text(encoding="utf-8"))
    rejections = data.pop("rejections", {})
    items = draw["items"]
    by_key = {key(i): i for i in items}
    n = len(items)

    problems = []
    rankings = {}
    for agent, order in data.items():
        normal = [by_key.get(key(x)) for x in order]
        if None in normal or sorted(normal) != sorted(items):
            problems.append(f"{agent}: the ranking does not match the list items exactly ({order})")
            continue
        rankings[agent] = normal
    for agent in rankings:
        if agent not in draw["agents"]:
            problems.append(f"{agent}: not in the draw; left out of the order-effect analysis")

    per_item = {
        i: {"positions": [], "first": [], "rejected": [], "received_in_row_1": 0, "received_in_row_1_and_ranked_1st": 0}
        for i in items
    }
    effect = []
    for agent, order in rankings.items():
        for pos, item in enumerate(order, start=1):
            per_item[item]["positions"].append(pos)
        per_item[order[0]]["first"].append(agent)
        received = draw["agents"].get(agent)
        if received:
            first_received = received["order"][0]
            per_item[first_received]["received_in_row_1"] += 1
            if order[0] == first_received:
                per_item[first_received]["received_in_row_1_and_ranked_1st"] += 1
                effect.append(agent)
    for agent, lst in rejections.items():
        for x in lst:
            item = by_key.get(key(x))
            if item:
                per_item[item]["rejected"].append(agent)
            else:
                problems.append(f"{agent}: rejection of unknown item '{x}'")

    with_draw = [ag for ag in rankings if ag in draw["agents"]]
    summary = []
    for item, d in per_item.items():
        pos = d.pop("positions")
        summary.append({"item": item, "mean_position": round(sum(pos) / len(pos), 2) if pos else None, **d})
    summary.sort(key=lambda x: (x["mean_position"] is None, x["mean_position"]))

    result = {
        "seed": draw["seed"],
        "agents_analyzed": len(rankings),
        "items": summary,
        "order_effect": {
            "agents_who_ranked_first_the_row_1_item": effect,
            "observed": len(effect),
            "expected_by_chance": round(len(with_draw) / n, 2),
            "base": len(with_draw),
        },
        "problems": problems,
    }
    Path(a.out).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    print("Item | mean position | 1st places | rejections | received in row 1 (ranked 1st)")
    for x in summary:
        print(f"{x['item']} | {x['mean_position']} | {len(x['first'])} | {len(x['rejected'])} | "
              f"{x['received_in_row_1']} ({x['received_in_row_1_and_ranked_1st']})")
    e = result["order_effect"]
    print(f"\nOrder effect: {e['observed']} of {e['base']} agents ranked first the item in row 1; "
          f"expected by chance ≈ {e['expected_by_chance']}.")
    for p in problems:
        print(f"PROBLEM: {p}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
