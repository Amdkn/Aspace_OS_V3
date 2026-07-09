#!/usr/bin/env python3
"""
extract_sections.py — Extract 4 sections canon from Takeout Gemini conversations.

D2 research FIRST doctrine : extract 4 sections canon (La Mutation / L'Offre E-Myth /
Services Hybrides / Les 3 Modèles) + 2 tables (Pricing + KPIs) from Takeout Gemini
before generating ADR-MARKET-STUDY-NNN canon.

D1 verify receipts : each section anchored with verbatim line refs [YYYY-MM:NNNNN].

Usage:
    python extract_sections.py --source takeout_2026-05.md --output sections.json
    python extract_sections.py --source takeout_2026-05.md --sections "Mutation,E-Myth" --output sections.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path


# 4 sections canon regex patterns (FR+EN)
SECTION_PATTERNS: dict[str, str] = {
    "La Mutation": r"(?i)(mutation|transition digitale|transformation digitale|marché en (transition|mutation)|accélération digitale|post-2024)",
    "L'Offre E-Myth": r"(?i)(E-Myth|technicien fondateur|80% des agences|agence E-Myth|dépendance (au client|fondateur)|angoisse du prochain mois)",
    "Services Hybrides": r"(?i)(services hybrides|mix SaaS services|AI agents (commodité|comme)|conformité by design|self-serve prioritaire)",
    "Les 3 Modèles": r"(?i)(3 modèles|Solo Founder|Standard|Groupe|pricing canon|path upsell|mid-market|enterprise)",
}

# 2 tables canon (Pricing + KPIs)
TABLE_PATTERNS: dict[str, str] = {
    "Modèles pricing": r"(?i)(modèle|pricing|tarif|prix).*(canon|standard|canonique|fixe)",
    "KPIs 2026": r"(?i)(KPI|indicateur|metric).*2026|TAM|SAM|SOM|chiffre clé",
}

# Killer Feature 4 mécanismes Agentic Governance
KILLER_FEATURE_PATTERNS: list[str] = [
    r"(?i)action space bounding",
    r"(?i)sandboxing",
    r"(?i)HITL dynamique|HITL adaptatif",
    r"(?i)tra[çc]abilité AI.?Act|registre AI.?Act",
    r"(?i)zero.?PII|sanitization PII",
    r"(?i)god.?s eye view|palantir constructif",
    r"(?i)bare.?metal zero.?knowledge|self.?hosting parano[iï]aque",
]

# Driver légal patterns
DRIVER_LEGAL_PATTERNS: list[str] = [
    r"(?i)AI Act.*ao[uû]t 2026|AI Act application totale",
    r"(?i)RGPD|HIPAA",
    r"(?i)secret professionnel",
    r"(?i)84 trilliards|transfert g[ée]n[ée]rationnel",
    r"(?i)domination hyper.?locale",
]


def index_lines_with_refs(source_path: Path) -> list[tuple[int, str]]:
    """Index all lines with 1-based line numbers for D1 receipt refs."""
    text = source_path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    return [(idx + 1, line) for idx, line in enumerate(lines)]


def extract_year_month(source_path: Path) -> str:
    """Extract YYYY-MM from filename pattern like 2026-05_conversations.md."""
    name = source_path.stem  # e.g. '2026-05_conversations'
    m = re.match(r"(\d{4})-(\d{2})", name)
    if m:
        return f"{m.group(1)}-{m.group(2)}"
    return "YYYY-MM"


def find_section_anchors(
    lines: list[tuple[int, str]],
    section_name: str,
    pattern: str,
    year_month: str,
) -> list[dict[str, str]]:
    """Find all matches of a section pattern with line refs."""
    compiled = re.compile(pattern)
    anchors: list[dict[str, str]] = []
    for lineno, text in lines:
        match = compiled.search(text)
        if match:
            anchors.append({
                "line_ref": f"[{year_month}:{lineno}]",
                "section": section_name,
                "verbatim_excerpt": text.strip()[:300],
                "match": match.group(0),
            })
    return anchors


def find_killer_feature_mechanisms(
    lines: list[tuple[int, str]],
    year_month: str,
) -> list[dict[str, str]]:
    """Find Killer Feature 4 mécanismes canon."""
    matches: list[dict[str, str]] = []
    for lineno, text in lines:
        for pat in KILLER_FEATURE_PATTERNS:
            m = re.search(pat, text)
            if m:
                matches.append({
                    "line_ref": f"[{year_month}:{lineno}]",
                    "match": m.group(0),
                    "verbatim_excerpt": text.strip()[:200],
                    "type": "killer_feature_mechanism",
                })
                break  # 1 match per line OK
    return matches


def find_driver_legal(
    lines: list[tuple[int, str]],
    year_month: str,
) -> list[dict[str, str]]:
    """Find driver légal (AI-Act, RGPD, secret pro, 84 Trilliards, hyper-locale)."""
    matches: list[dict[str, str]] = []
    for lineno, text in lines:
        for pat in DRIVER_LEGAL_PATTERNS:
            m = re.search(pat, text)
            if m:
                matches.append({
                    "line_ref": f"[{year_month}:{lineno}]",
                    "match": m.group(0),
                    "verbatim_excerpt": text.strip()[:200],
                    "type": "driver_legal",
                })
                break
    return matches


def extract_table_anchors(
    lines: list[tuple[int, str]],
    year_month: str,
) -> dict[str, list[dict[str, str]]]:
    """Find pricing + KPIs tables."""
    tables: dict[str, list[dict[str, str]]] = {}
    for table_name, pat in TABLE_PATTERNS.items():
        compiled = re.compile(pat)
        anchors: list[dict[str, str]] = []
        for lineno, text in lines:
            if compiled.search(text):
                anchors.append({
                    "line_ref": f"[{year_month}:{lineno}]",
                    "table_name": table_name,
                    "verbatim_excerpt": text.strip()[:300],
                })
        tables[table_name] = anchors
    return tables


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract 4 sections canon from Takeout Gemini")
    parser.add_argument("--source", required=True, help="Path to Takeout Gemini .md file")
    parser.add_argument("--sections", default="", help="Comma-separated filter: Mutation,E-Myth,Hybrides,Modeles")
    parser.add_argument("--keywords", default="", help="Comma-separated additional keywords to anchor on")
    parser.add_argument("--output", required=True, help="Output JSON file")
    args = parser.parse_args()

    source_path = Path(args.source)
    if not source_path.exists():
        print(f"ERROR: source not found: {args.source}", file=sys.stderr)
        return 1

    year_month = extract_year_month(source_path)
    lines = index_lines_with_refs(source_path)

    # Filter sections if specified
    sections_to_extract = SECTION_PATTERNS
    if args.sections:
        requested = {s.strip() for s in args.sections.split(",")}
        sections_to_extract = {k: v for k, v in SECTION_PATTERNS.items() if k in requested}

    # Extract sections
    sections_extracted: dict[str, list[dict[str, str]]] = {}
    for name, pat in sections_to_extract.items():
        anchors = find_section_anchors(lines, name, pat, year_month)
        sections_extracted[name] = anchors

    # Extract tables
    tables = extract_table_anchors(lines, year_month)

    # Extract Killer Feature
    killer_feature = find_killer_feature_mechanisms(lines, year_month)

    # Extract driver légal
    driver_legal = find_driver_legal(lines, year_month)

    # Extract keyword anchors if provided
    keyword_anchors: list[dict[str, str]] = []
    if args.keywords:
        keywords = [k.strip() for k in args.keywords.split(",")]
        text_lower = "\n".join(line for _, line in lines).lower()
        for kw in keywords:
            kw_lower = kw.lower()
            idx = 0
            while True:
                pos = text_lower.find(kw_lower, idx)
                if pos == -1:
                    break
                # Find line number for this position
                cumulative = 0
                for lineno, line in lines:
                    line_len = len(line) + 1
                    if cumulative + line_len > pos:
                        keyword_anchors.append({
                            "line_ref": f"[{year_month}:{lineno}]",
                            "keyword": kw,
                            "verbatim_excerpt": line.strip()[:200],
                        })
                        break
                    cumulative += line_len
                idx = pos + 1

    output = {
        "source_file": str(source_path.absolute()),
        "year_month": year_month,
        "total_lines_scanned": len(lines),
        "sections_extracted": {k: len(v) for k, v in sections_extracted.items()},
        "sections_anchors": sections_extracted,
        "tables": tables,
        "killer_feature_count": len(killer_feature),
        "killer_feature_anchors": killer_feature[:30],
        "driver_legal_count": len(driver_legal),
        "driver_legal_anchors": driver_legal[:20],
        "keyword_anchors_count": len(keyword_anchors),
        "keyword_anchors": keyword_anchors[:30],
    }

    output_path = Path(args.output)
    output_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")

    # D1 receipt summary
    print(f"[D1] Sections canon extracted:")
    print(f"  Source: {source_path.absolute()}")
    print(f"  Year-month: {year_month}")
    print(f"  Lines scanned: {len(lines):,}")
    print(f"  Sections found:")
    for name, anchors in sections_extracted.items():
        print(f"    - {name}: {len(anchors)} anchors")
    print(f"  Tables: {sum(len(v) for v in tables.values())} anchors total")
    print(f"  Killer Feature mécanismes: {len(killer_feature)} anchors")
    print(f"  Driver légal: {len(driver_legal)} anchors")
    print(f"  Keyword anchors: {len(keyword_anchors)}")
    print(f"  Output: {output_path.absolute()}")

    return 0


if __name__ == "__main__":
    sys.exit(main())