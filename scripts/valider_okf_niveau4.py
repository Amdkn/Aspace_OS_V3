#!/usr/bin/env python3
"""
Niveau 4 — auto-validation des concepts OKF.

Regle (canon OKF v0.2) :
  - frontmatter present, avec `type`, `title`, `description`, `tags`,
    `generated`, `sources`, `okf_version`.
  - `verified` present et non vide.
  - au moins un `verified.by` commençant par `human:` (revu par un humain),
    sinon le concept est en « confiance: machine » et doit etre journalise.
  - chaque `sources` a un `last_modified` present.
  - pas de date de validite (valide_de / valide_jusqu_a) -> avertissement,
    pas un rejet (le champ est une decision, pas un fait).

Sortie : tableau + JSON sur stdout. Exit 1 si un concept est en defaut
critique (pas de `verified` du tout).

Usage :
    python scripts/valider_okf_niveau4.py [--bundle 40_Memory_Wiki_OKF]
"""

import argparse
import json
import os
import re
import sys

ROOT = r"C:\Users\amado\ASpace_OS_V3"


def parse_frontmatter(path):
    """Renvoie (meta dict, corps) ou (None, None) si pas de frontmatter YAML."""
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except OSError:
        return None, None
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S | re.M)
    if not m:
        return None, text
    fm = m.group(1)
    body = text[m.end():]
    meta, _ = _parse_yaml_block(fm, 0)
    return meta or {}, body


def _parse_yaml_block(s, depth=0):
    """Parseur YAML mineur — suffisant pour les meta OKF (plats, listes, objets)."""
    meta = {}
    lines = s.split("\n")
    i = 0
    current_key = None
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.strip().startswith("#"):
            i += 1
            continue
        m = re.match(r"^(\s*)([\w_]+):\s*(.*)$", line)
        if m:
            indent, key, val = m.group(1), m.group(2), m.group(3).strip()
            if not val:
                # bloc ou liste
                i += 1
                block_lines = []
                while i < len(lines) and (lines[i].startswith(" " * (len(indent) + 2)) or not lines[i].strip()):
                    if lines[i].strip():
                        block_lines.append(lines[i][len(indent) + 2:])
                    i += 1
                block = "\n".join(block_lines)
                if block_lines and re.match(r"^\s*- ", block_lines[0]):
                    items = []
                    for bl in block_lines:
                        mm = re.match(r"^\s*-\s*(.*)$", bl)
                        if mm:
                            items.append(mm.group(1).strip())
                    meta[key] = items
                else:
                    sub, _ = _parse_yaml_block(block, depth + 1)
                    meta[key] = sub
                continue
            else:
                meta[key] = val
                i += 1
                continue
        i += 1
    return meta, i


def check_concept(path):
    meta, body = parse_frontmatter(path)
    problems = []

    if meta is None:
        return {"path": path, "ok": False, "problems": ["pas de frontmatter"]}

    required = ["type", "title", "description", "tags", "sources", "okf_version"]
    for k in required:
        if k not in meta or meta[k] in (None, "", []):
            problems.append(f"champ '{k}' absent ou vide")

    verified = meta.get("verified")
    if not verified:
        problems.append("champ 'verified' absent ou vide -> confiance: machine")
    else:
        if not isinstance(verified, list) or not verified:
            problems.append("'verified' non vide mais mal forme")
        else:
            human = [v for v in verified if isinstance(v, str) and v.startswith("human:")]
            if not human:
                problems.append("pas de verified.by human: -> confiance: machine, journaliser")

    # validite
    if "valide_de" not in meta and "valide_jusqu_a" not in meta:
        problems.append("pas de date de validite (avertissement)")

    # sources.last_modified
    sources = meta.get("sources")
    if sources and isinstance(sources, list):
        for i, s in enumerate(sources):
            if isinstance(s, dict) and "last_modified" not in s:
                problems.append(f"sources[{i}] sans last_modified")

    return {"path": os.path.relpath(path, ROOT), "ok": not problems,
            "problems": problems}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bundle", default=os.path.join(ROOT, "40_Memory_Wiki_OKF"))
    args = ap.parse_args()

    bundle = args.bundle
    if not os.path.isdir(bundle):
        print("Bundle absent :", bundle)
        return 2

    results = []
    for dirpath, _dirs, files in os.walk(bundle):
        for f in files:
            if f.endswith(".md") and not f.startswith("."):
                results.append(check_concept(os.path.join(dirpath, f)))

    ok = [r for r in results if r["ok"]]
    bad = [r for r in results if not r["ok"]]

    print(f"Concepts       : {len(results)}")
    print(f"Valides        : {len(ok)}")
    print(f"En defaut      : {len(bad)}")
    for r in bad:
        print(f"  {r['path']}")
        for p in r["problems"]:
            print(f"      - {p}")

    out = {"total": len(results), "ok": len(ok), "bad": len(bad), "items": results}
    print("\n" + json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())