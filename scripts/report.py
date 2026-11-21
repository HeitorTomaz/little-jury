"""Build and validate the panel's visual report.

Usage:
    python method/scripts/report.py build <data.json> --template template/report-template.html --out <report.html>
    python method/scripts/report.py validate <report.html> --template template/report-template.html

"build" validates the data, puts it in the <script id="panel-data"> block of a copy of the template,
checks that the rest of the file is identical to the template (including the default-labels block)
and copies the template's fonts/ folder next to the report. "validate" runs the same checks on a
report that already exists. Errors stop the build; warnings don't.

Labels: every UI string has an English default in the template's default-labels block. When
meta.language is not English, data.labels must translate every key.
"""

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

DATA_BLOCK = re.compile(r'(<script type="application/json" id="panel-data">\n)(.*?)(\n</script>)', re.S)
LABELS_BLOCK = re.compile(r'<script type="application/json" id="default-labels">\n(.*?)\n</script>', re.S)
EVIDENCE = {"observation", "hypothesis", "proven problem"}
CLASSIFICATIONS = {"hypothesis", "proven problem"}
PRIORITIES = {"high", "medium", "low"}
CATEGORIES = {"design", "audience", "production", "scope", "market"}
TYPES = {"concept", "system", "change"}


def split(html: str):
    found = DATA_BLOCK.findall(html)
    if len(found) != 1:
        raise SystemExit(f"The file should have exactly one panel-data block; it has {len(found)}.")
    m = DATA_BLOCK.search(html)
    return html[: m.start(2)], m.group(2), html[m.end(2):]


def strings(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, dict):
        for v in x.values():
            yield from strings(v)
    elif isinstance(x, list):
        for v in x:
            yield from strings(v)


def is_english(language) -> bool:
    return str(language or "English").strip().lower() in {"english", "en", "en-us", "en-gb"}


def validate(d: dict, example: dict, default_labels: dict):
    errors, warnings = [], []

    def level(value, where, lim=(1, 3)):
        if not (isinstance(value, int) and lim[0] <= value <= lim[1]):
            errors.append(f"{where}: must be an integer from {lim[0]} to {lim[1]} (got {value!r})")

    meta = d.get("meta", {})
    if meta.get("example") is not False:
        errors.append("meta.example must be false")
    for k in ["concept", "version", "date", "composition", "language"]:
        if not meta.get(k):
            errors.append(f"meta.{k} is empty")
    if meta.get("type") not in TYPES:
        errors.append(f"meta.type must be concept, system or change (got {meta.get('type')!r})")

    labels = d.get("labels") or {}
    unknown = sorted(k for k in labels if k not in default_labels)
    for k in unknown:
        errors.append(f"labels: unknown key '{k}'")
    if not is_english(meta.get("language")):
        missing = sorted(k for k in default_labels if not labels.get(k))
        if missing:
            errors.append(f"meta.language is {meta.get('language')!r}: labels must translate every key; "
                          f"{len(missing)} missing, e.g. {', '.join(missing[:5])}")
    for k, v in labels.items():
        if k in default_labels:
            needed = set(re.findall(r"\{(\w+)\}", default_labels[k]))
            have = set(re.findall(r"\{(\w+)\}", v))
            if needed - have:
                errors.append(f"labels.{k}: missing placeholder(s) {sorted(needed - have)}")

    summary = d.get("summary", [])
    if not 3 <= len(summary) <= 5:
        warnings.append(f"summary has {len(summary)} sentences; 3 to 5 are expected")

    dims = d.get("dimensions", [])
    dim_ids = [x.get("id") for x in dims]
    if not dims or not all(x.get("id") and x.get("name") for x in dims):
        errors.append("dimensions empty or without id/name")

    ids = {}
    for group, name_field in [("users", "name"), ("experts", "role"), ("adversaries", "role")]:
        lst = d.get(group, [])
        if not lst:
            errors.append(f"{group} is empty")
        for x in lst:
            i = x.get("id")
            if not i:
                errors.append(f"{group}: item without id")
                continue
            if i in ids:
                errors.append(f"repeated id: {i}")
            ids[i] = group
            if not x.get(name_field):
                errors.append(f"{group}/{i}: missing {name_field}")

    def check_ids(lst, where):
        for q in lst or []:
            if q not in ids:
                errors.append(f"{where}: unknown id '{q}'")

    for u in d.get("users", []):
        scores = u.get("scores", {})
        for k, v in scores.items():
            if k not in dim_ids:
                errors.append(f"users/{u.get('id')}: score for a dimension that does not exist '{k}'")
            level(v, f"users/{u.get('id')}.scores.{k}", (1, 5))
        missing = [k for k in dim_ids if k not in scores]
        if missing:
            warnings.append(f"users/{u.get('id')}: no score for {', '.join(missing)}")
        for k in ["understood", "attracted", "putOff", "dropOut"]:
            if not u.get(k):
                warnings.append(f"users/{u.get('id')}: '{k}' is empty")
    for dim in dim_ids:
        vals = [u.get("scores", {}).get(dim) for u in d.get("users", []) if dim in u.get("scores", {})]
        if len(vals) >= 3 and len(set(vals)) == 1:
            warnings.append(f"every '{dim}' score is {vals[0]}: a signal to look into in diversity.md")

    for i, t in enumerate(d.get("tensions", [])):
        where = f"tensions[{i}]"
        if t.get("evidence") not in EVIDENCE:
            errors.append(f"{where}.evidence is invalid: {t.get('evidence')!r}")
        level(t.get("severity"), f"{where}.severity")
        for side in ["for", "against"]:
            check_ids((t.get(side) or {}).get("who"), f"{where}.{side}.who")
        for k in ["proposal", "loss", "experiment"]:
            if not t.get(k):
                errors.append(f"{where}: missing '{k}' (every recommendation says what it proposes, what is lost and how to test it)")

    for i, r in enumerate(d.get("risks", [])):
        where = f"risks[{i}]"
        level(r.get("severity"), f"{where}.severity")
        level(r.get("likelihood"), f"{where}.likelihood")
        if r.get("category") not in CATEGORIES:
            warnings.append(f"{where}.category outside the expected values: {r.get('category')!r}")
        check_ids(r.get("who"), f"{where}.who")

    for i, f in enumerate(d.get("strengths", [])):
        check_ids(f.get("who"), f"strengths[{i}].who")
    for i, c in enumerate(d.get("scenarios", [])):
        if c.get("classification") not in CLASSIFICATIONS:
            errors.append(f"scenarios[{i}].classification is invalid: {c.get('classification')!r}")
    for i, h in enumerate(d.get("hypotheses", [])):
        if h.get("priority") not in PRIORITIES:
            errors.append(f"hypotheses[{i}].priority is invalid: {h.get('priority')!r}")

    launch = d.get("launch")
    if launch:
        for p in launch.get("preferences", []):
            check_ids([p.get("who")], "launch.preferences")
    lst = d.get("list")
    if lst:
        for i, x in enumerate(lst.get("order", [])):
            check_ids(x.get("first"), f"list.order[{i}].first")
            check_ids(x.get("rejected"), f"list.order[{i}].rejected")

    for k in ["tensions", "risks", "strengths", "scenarios", "hypotheses", "gaps"]:
        if not d.get(k):
            warnings.append(f"section '{k}' is empty")

    # Example markers: strings that say "example" and the placeholder names (User A, Item A...).
    # Legitimate terms repeated in any report (ids, "hypothesis", dimension names) don't count.
    markers = {t for t in strings(example) if "example" in t.lower()}
    markers |= {u.get("name") for u in example.get("users", [])}
    markers |= {e.get("role") for e in example.get("experts", [])}
    markers |= {x.get("name") for x in (example.get("list") or {}).get("order", [])}
    markers.discard(None)
    leftovers = sorted({t for t in strings({k: v for k, v in d.items() if k != "labels"}) if t in markers})
    for t in leftovers:
        errors.append(f"text from the example data reused: {t!r}")
    return errors, warnings


def report_out(errors, warnings) -> int:
    for w in warnings:
        print(f"WARNING: {w}")
    for e in errors:
        print(f"ERROR: {e}")
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s).")
    return 1 if errors else 0


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
    ap.add_argument("action", choices=["build", "validate"])
    ap.add_argument("file")
    ap.add_argument("--template", required=True)
    ap.add_argument("--output", "--out", dest="out")
    a = ap.parse_args()
    a.template, a.file = confined(a.template), confined(a.file)
    if a.out:
        a.out = confined(a.out, write=True)

    template_html = Path(a.template).read_text(encoding="utf-8")
    before_t, block_t, after_t = split(template_html)
    example = json.loads(block_t)
    lm = LABELS_BLOCK.search(template_html)
    if not lm:
        raise SystemExit("The template has no default-labels block.")
    default_labels = json.loads(lm.group(1))

    if a.action == "build":
        if not a.out:
            raise SystemExit("--out is required for build")
        try:
            data = json.loads(Path(a.file).read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            raise SystemExit(f"Invalid JSON in {a.file}: {e}")
        errors, warnings = validate(data, example, default_labels)
        if errors:
            print("Report NOT built.")
            return report_out(errors, warnings)
        text = json.dumps(data, ensure_ascii=False, indent=2).replace("</", "<\\/")
        html = before_t + text + after_t
        Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        Path(a.out).write_text(html, encoding="utf-8", newline="\n")
        before, block, after = split(html)
        assert before == before_t and after == after_t and json.loads(block) == data
        fonts = Path(a.template).parent / "fonts"
        if fonts.is_dir():
            shutil.copytree(fonts, Path(a.out).parent / "fonts", dirs_exist_ok=True)
        else:
            warnings.append("the template has no fonts/ folder; the report will use system fonts")
        print(f"Report built at {a.out} (with the fonts/ folder next to it)")
        return report_out(errors, warnings)

    before, block, after = split(Path(a.file).read_text(encoding="utf-8"))
    errors, warnings = [], []
    if before != before_t or after != after_t:
        errors.append("the HTML outside the data block differs from the template (only the data block may change)")
    if not (Path(a.file).parent / "fonts").is_dir():
        warnings.append("the fonts/ folder is missing next to the report; it will use system fonts")
    try:
        data = json.loads(block)
    except json.JSONDecodeError as e:
        errors.append(f"the data block is not valid JSON: {e}")
        return report_out(errors, warnings)
    e2, w2 = validate(data, example, default_labels)
    return report_out(errors + e2, warnings + w2)


if __name__ == "__main__":
    sys.exit(main())
