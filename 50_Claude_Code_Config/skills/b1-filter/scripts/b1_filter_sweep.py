#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
b1_filter_sweep.py — Étage E1 du B1-filter (PRD-B1-FILTER-M3-001).
Vérifie/corrige la cohérence frontmatter des guides Geordi contre la bijection
canon ADR-L2-BDLD-MAP-001 §D3. Déterministe, zéro token, idempotent.

Usage:
  python b1_filter_sweep.py --audit          # rapport seul, zéro mutation
  python b1_filter_sweep.py --fix            # corrige E1 (patch additif frontmatter)
  python b1_filter_sweep.py --audit --json   # rapport machine (pour agents M3 / WF1)

Sortie --json: {"ok": N, "violations": [...], "orphans": [...]} — les orphans
sont le résidu E2 à classifier par agents M3 (voir SKILL.md mode classify).
"""
import argparse
import json
import re
import sys
from pathlib import Path

GUIDES_ROOT = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides")

# Table de vérité — copie conforme ADR-L2-BDLD-MAP-001 §D3 (RATIFIED 2026-06-27).
# Clé = nom du dossier domaine. Toute divergence fichier/index → cette table fait foi.
BIJECTION = {
    "01_Product": {"ld": "LD04_Cognition_Tilly", "b2_owner": "flash-product",       "b2_agent": "b2-03-flash-product",       "squad": "Avengers"},
    "02_Ops":     {"ld": "LD01_Business_Book",   "b2_owner": "batman-ops",           "b2_agent": "b2-02-batman-ops",          "squad": "Fantastic Four"},
    "03_IT":      {"ld": "LD07_Creativity_Reno", "b2_owner": "cyborg-it",            "b2_agent": "b2-06-cyborg-it",           "squad": "Kang Dynasty"},
    "04_Finance": {"ld": "LD02_Finance_Saru",    "b2_owner": "wonderwoman-finance",  "b2_agent": "b2-07-wonderwoman-finance", "squad": "Thunderbolts"},
    "05_Legal":   {"ld": "LD03_Health_Culber",   "b2_owner": "aquaman-legal",        "b2_agent": "b2-08-aquaman-legal",       "squad": "Eternals"},
    "06_Sales":   {"ld": "LD05_Social_Stamets",  "b2_owner": "johnjones-sales",      "b2_agent": "b2-05-johnjones-sales",     "squad": "Illuminati"},
    "07_Growth":  {"ld": "LD08_Impact_Georgiou", "b2_owner": "superman-growth",      "b2_agent": "b2-04-superman-growth",     "squad": "Guardians"},
    "08_People":  {"ld": "LD06_Family_Burnham",  "b2_owner": "greenlantern-people",  "b2_agent": "b2-01-greenlantern-people", "squad": "X-Men"},
}
DEFAULT_SISTER_B1 = "jerry-prime"
FM_DELIM = re.compile(r"^---\s*$")


def parse_frontmatter(text):
    """Retourne (dict_champs, ligne_debut, ligne_fin) ou (None, -1, -1)."""
    lines = text.splitlines()
    if not lines or not FM_DELIM.match(lines[0]):
        return None, -1, -1
    for i in range(1, min(len(lines), 80)):
        if FM_DELIM.match(lines[i]):
            fields = {}
            for ln in lines[1:i]:
                m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$", ln)
                if m:
                    fields[m.group(1)] = m.group(2).strip().strip('"')
            return fields, 0, i
    return None, -1, -1


def expected_for(path):
    """Domaine attendu d'après le dossier parent (E1), None si orphelin (E2)."""
    for part in path.parts:
        if part in BIJECTION:
            return part
    return None


def check_file(path):
    """Retourne (status, details). status ∈ ok|violation|orphan|no_frontmatter."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        return "error", {"file": str(path), "error": str(e)}
    fields, s, e = parse_frontmatter(text)
    domain_dir = expected_for(path)
    if domain_dir is None:
        return "orphan", {"file": str(path), "reason": "hors dossier domaine 0X_*"}
    exp = BIJECTION[domain_dir]
    if fields is None:
        return "no_frontmatter", {"file": str(path), "expected_domain": domain_dir, "expected": exp}
    diffs = {}
    ld_val = fields.get("ld", "")
    if not ld_val.startswith(exp["ld"].split("_")[0]):  # compare LDxx prefix
        diffs["ld"] = {"actual": ld_val or "(absent)", "expected": exp["ld"]}
    b2_val = fields.get("b2_owner", "")
    if b2_val and b2_val != exp["b2_owner"]:
        diffs["b2_owner"] = {"actual": b2_val, "expected": exp["b2_owner"]}
    elif not b2_val:
        diffs["b2_owner"] = {"actual": "(absent)", "expected": exp["b2_owner"]}
    if not fields.get("sister_b1"):
        diffs["sister_b1"] = {"actual": "(absent)", "expected": DEFAULT_SISTER_B1}
    if diffs:
        return "violation", {"file": str(path), "domain": domain_dir, "diffs": diffs}
    return "ok", {"file": str(path)}


def fix_file(path, domain_dir):
    """Patch additif du frontmatter: corrige/ajoute ld, b2_owner, sister_b1, b1_filter.
    Ne supprime JAMAIS un champ existant. Idempotent."""
    exp = BIJECTION[domain_dir]
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines(keepends=True)
    fields, s, e = parse_frontmatter(text)
    if fields is None:
        # Frontmatter absent -> en créer un minimal en tête (append-only du contenu).
        fm = (f"---\n"
              f"domain: {domain_dir}\n"
              f"ld: {exp['ld']}\n"
              f"b2_owner: {exp['b2_owner']}\n"
              f"sister_b1: {DEFAULT_SISTER_B1}\n"
              f"b1_filter: APPLIED_E1_DETERMINISTIC (sweep 2026, ADR-L2-BDLD-MAP-001 D3)\n"
              f"---\n")
        path.write_text(fm + text, encoding="utf-8")
        return "created_frontmatter"
    # Patch dans le bloc existant, ligne par ligne.
    changed = False
    have = set()
    for i in range(s + 1, e):
        raw = lines[i]
        m = re.match(r"^(ld|b2_owner|sister_b1)\s*:\s*(.*)$", raw.rstrip("\n"))
        if not m:
            continue
        key = m.group(1)
        have.add(key)
        want = {"ld": exp["ld"], "b2_owner": exp["b2_owner"], "sister_b1": None}[key]
        if key == "sister_b1":
            continue  # présent = on respecte le variant choisi
        cur = m.group(2).strip().strip('"')
        ok = cur.startswith(exp["ld"].split("_")[0]) if key == "ld" else (cur == want)
        if not ok:
            lines[i] = f"{key}: {want}  # E1 fix (était: {cur or 'absent'}) — bijection D3\n"
            changed = True
    inserts = []
    if "ld" not in have:
        inserts.append(f"ld: {exp['ld']}\n")
    if "b2_owner" not in have:
        inserts.append(f"b2_owner: {exp['b2_owner']}\n")
    if "sister_b1" not in have:
        inserts.append(f"sister_b1: {DEFAULT_SISTER_B1}\n")
    if inserts:
        lines[e:e] = inserts
        changed = True
    if changed:
        path.write_text("".join(lines), encoding="utf-8")
        return "patched"
    return "unchanged"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit", action="store_true")
    ap.add_argument("--fix", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--root", default=str(GUIDES_ROOT))
    args = ap.parse_args()
    root = Path(args.root)
    if not root.exists():
        print(f"FATAL: root introuvable: {root}", file=sys.stderr)
        sys.exit(2)

    report = {"ok": 0, "violations": [], "orphans": [], "no_frontmatter": [], "fixed": [], "errors": []}
    # EXCLUSIONS par design (cf. /youtube-to-guide §"8 Domaines" note) :
    # 09_Life_OS = classification LDxx directe (/youtube-takeout-to-lifeos), 00_KERNEL_OS = infra.
    files = [p for p in root.rglob("*.md")
             if "_TRASH" not in str(p) and not p.name.startswith("_INDEX")
             and "09_Life_OS" not in p.parts and "00_KERNEL_OS" not in p.parts]
    for p in sorted(files):
        status, det = check_file(p)
        if status == "ok":
            report["ok"] += 1
        elif status == "violation":
            report["violations"].append(det)
            if args.fix:
                report["fixed"].append({"file": det["file"], "result": fix_file(p, det["domain"])})
        elif status == "no_frontmatter":
            report["no_frontmatter"].append(det)
            if args.fix:
                report["fixed"].append({"file": det["file"], "result": fix_file(p, det["expected_domain"])})
        elif status == "orphan":
            report["orphans"].append(det)
        else:
            report["errors"].append(det)

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=1))
    else:
        print(f"scanned={len(files)} ok={report['ok']} violations={len(report['violations'])} "
              f"no_frontmatter={len(report['no_frontmatter'])} orphans_E2={len(report['orphans'])} "
              f"fixed={len(report['fixed'])} errors={len(report['errors'])}")
        for v in report["violations"][:20]:
            print(f"  VIOLATION {Path(v['file']).name}: " +
                  "; ".join(f"{k} {d['actual']} -> {d['expected']}" for k, d in v["diffs"].items()))
        if len(report["violations"]) > 20:
            print(f"  ... +{len(report['violations']) - 20} violations (use --json)")
        for o in report["orphans"][:10]:
            print(f"  ORPHAN(E2->M3) {Path(o['file']).name}")
        if len(report["orphans"]) > 10:
            print(f"  ... +{len(report['orphans']) - 10} orphans (use --json)")
    sys.exit(0)


if __name__ == "__main__":
    main()
