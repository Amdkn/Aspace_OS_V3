#!/usr/bin/env python3
"""
derive_killer_feature.py — D6 root cause for the 4 mécanismes Agentic Governance.

Identifies Killer Feature verdict (4 mécanismes pack Agentic Governance) +
driver légal urgency from Takeout Gemini + ADR canon sister scope.

D6 root cause first : the Killer Feature = differentiator that justifies pricing
premium + time-to-market window. Without it, market study canon is incomplete.

Usage:
    python derive_killer_feature.py --sections sections_anchors.json --output killer_feature_verdict.json
    python derive_killer_feature.py --source takeout_2026-05.md --output killer_feature_verdict.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path


# 4 mécanismes canon Agentic Governance (sister ADR-ICP-SOLARIS-001 Pilier 5)
# D6 tuned after Takeout Gemini 2026-05 real-test (verbatim phrasing detection)
MECANISMES_CANON: dict[str, str] = {
    "Action Space Bounding": r"(?i)action space bounding|p[ée]rim[èe]tre d.{0,3}action.*agent|scope creep|boundary.*action|auto.?approve|auto.?dispatch",
    "Sandboxing": r"(?i)sandboxing|isolation.*ex[ée]cution|blast radius|bac.*[àa] sable|isolement|sandbox",
    "HITL Dynamique": r"(?i)HITL|human.?in.?the.?loop|human in the loop|approbation humaine|approval.*dynamique|manuel.?approve|validation humaine|manuel.?validation|escalade",
    "Traçabilité AI-Act": r"(?i)tra[çc]abilit[ée]|registre.*AI|article 12|audit.*conformit[ée]|non.?r[ée]pudiation|conformit[ée].*AI.?Act|AI.?Act.*conformit[ée]|preuve.*conformit[ée]",
}

# Mécanismes additionnels Nexus (5 vs 4)
MECANISMES_NEXUS_EXT: dict[str, str] = {
    "Zero-PII Sanitization": r"(?i)zero.?PII|sanitization.*PII|Makkari|anonymisation.*donn[ée]es sensibles|scrubber",
}

# Mécanismes additionnels Orbiter (5 terrain)
MECANISMES_ORBITER_EXT: dict[str, str] = {
    "God's Eye View 3D": r"(?i)god.?s eye view|god eye view|interface 3D.*temps r[ée]el|Bilawal Sidhu",
    "Ant-Man Route Optimizer": r"(?i)Ant-Man|Ant Man|optimis.*routage|recalcul.*itin[ée]raire",
    "Vision Dispatcher": r"(?i)Vision.*dispatcher|dispatcher.*omniscient|assignation.*ticket",
    "Quicksilver SMS Reroutage": r"(?i)Quicksilver|communicateur.*transit|SMS.*reroutage|reroutage.*chauffeur",
    "Songbird Billing": r"(?i)Songbird|billing.*kilom[ée]trique|facturation.*kilom[èe]tre",
}

# Driver légal patterns (D6 tuned after Takeout Gemini 2026-05 real-test)
DRIVER_LEGAL_CANON: dict[str, str] = {
    "AI-Act août 2026": r"(?i)AI Act.*ao[uû]t|AI Act application totale|r[ée]glement.*IA|application.*totale.*AI.?Act|AI.?Act.*2026",
    "RGPD/HIPAA": r"(?i)RGPD|HIPAA|secret professionnel|protection.*donn[ée]es|conformit[ée].*RGPD",
    "84 Trilliards Transfert": r"(?i)84 trilliards|transfert g[ée]n[ée]rationnel|baby.?boomers.*patrimoine|plus grand transfert",
    "Domination hyper-locale": r"(?i)domination hyper.?locale|hyper.?local|conqu[êe]te.*locale|domination.*locale",
    "Zones blanches 4G": r"(?i)zones blanches|sans 4G|offline|panne mat[ée]rielle|zone blanche",
}


def detect_mecanismes(
    sources: dict,
    mecanisme_patterns: dict[str, str],
) -> dict[str, dict]:
    """Detect each mécanisme and return anchor count + sample refs."""
    results: dict[str, dict] = {}
    # Combine all anchors from input
    all_anchors: list[dict] = []
    for key in ("sections_anchors", "killer_feature_anchors", "driver_legal_anchors", "keyword_anchors"):
        if key in sources:
            if isinstance(sources[key], dict):
                # sections_anchors is nested
                for section_anchors in sources[key].values():
                    all_anchors.extend(section_anchors)
            else:
                all_anchors.extend(sources[key])

    for name, pat in mecanisme_patterns.items():
        compiled = re.compile(pat)
        matches: list[dict] = []
        for anchor in all_anchors:
            excerpt = anchor.get("verbatim_excerpt", "")
            if compiled.search(excerpt):
                matches.append({
                    "line_ref": anchor.get("line_ref", ""),
                    "excerpt": excerpt[:200],
                })
        results[name] = {
            "count": len(matches),
            "line_refs": [m["line_ref"] for m in matches[:10]],
            "sample_excerpts": [m["excerpt"] for m in matches[:5]],
        }
    return results


def detect_driver_legal(sources: dict) -> dict[str, dict]:
    """Detect driver légal urgency."""
    return detect_mecanismes(sources, DRIVER_LEGAL_CANON)


def compute_killer_feature_verdict(
    mecanismes_solaris: dict[str, dict],
    mecanismes_nexus_ext: dict[str, dict],
    mecanismes_orbiter_ext: dict[str, dict],
) -> dict:
    """D6 root cause verdict on Killer Feature."""
    solaris_4_count = sum(m["count"] for m in mecanismes_solaris.values())
    nexus_5_count = solaris_4_count + sum(m["count"] for m in mecanismes_nexus_ext.values())
    orbiter_5_count = sum(m["count"] for m in mecanismes_orbiter_ext.values())

    # Verdict: at least 4 mécanismes found in canon = Killer Feature confirmed
    solaris_confirmed = sum(1 for m in mecanismes_solaris.values() if m["count"] > 0) >= 4
    nexus_confirmed = sum(1 for m in {**mecanismes_solaris, **mecanismes_nexus_ext}.values() if m["count"] > 0) >= 5
    orbiter_confirmed = sum(1 for m in mecanismes_orbiter_ext.values() if m["count"] > 0) >= 5

    return {
        "solaris_4_mecanismes": solaris_4_count,
        "nexus_5_mecanismes_total": nexus_5_count,
        "orbiter_5_mecanismes_total": orbiter_5_count,
        "solaris_killer_feature_confirmed": solaris_confirmed,
        "nexus_killer_feature_confirmed": nexus_confirmed,
        "orbiter_killer_feature_confirmed": orbiter_confirmed,
        "verdict": "Agentic Governance 4 mécanismes canon confirmé" if solaris_confirmed else "Killer Feature NOT confirmed — D6 root cause investigation required",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="D6 root cause Killer Feature 4 mécanismes Agentic Governance")
    parser.add_argument("--sections", help="Path to sections_anchors.json from extract_sections.py")
    parser.add_argument("--source", help="Path to Takeout Gemini .md file (alternative to --sections)")
    parser.add_argument("--killer_feature_pattern", default="", help="Custom regex pattern for killer feature detection")
    parser.add_argument("--driver_legal_pattern", default="", help="Custom regex pattern for driver légal detection")
    parser.add_argument("--output", required=True, help="Output JSON file")
    args = parser.parse_args()

    sources: dict = {}
    if args.sections:
        sections_path = Path(args.sections)
        if not sections_path.exists():
            print(f"ERROR: sections file not found: {args.sections}", file=sys.stderr)
            return 1
        sources = json.loads(sections_path.read_text(encoding="utf-8"))
    elif args.source:
        # Direct source mode: re-run extract_sections logic minimally
        from extract_sections import (
            index_lines_with_refs,
            extract_year_month,
            find_killer_feature_mechanisms,
            find_driver_legal,
            extract_table_anchors,
            find_section_anchors,
            SECTION_PATTERNS,
        )
        source_path = Path(args.source)
        if not source_path.exists():
            print(f"ERROR: source not found: {args.source}", file=sys.stderr)
            return 1
        year_month = extract_year_month(source_path)
        lines = index_lines_with_refs(source_path)
        sections_anchors = {
            name: find_section_anchors(lines, name, pat, year_month)
            for name, pat in SECTION_PATTERNS.items()
        }
        sources = {
            "year_month": year_month,
            "total_lines_scanned": len(lines),
            "sections_anchors": sections_anchors,
            "killer_feature_anchors": find_killer_feature_mechanisms(lines, year_month),
            "driver_legal_anchors": find_driver_legal(lines, year_month),
            "tables": extract_table_anchors(lines, year_month),
        }
    else:
        print("ERROR: provide either --sections or --source", file=sys.stderr)
        return 1

    # Detect mécanismes
    mecanismes_solaris = detect_mecanismes(sources, MECANISMES_CANON)
    mecanismes_nexus_ext = detect_mecanismes(sources, MECANISMES_NEXUS_EXT)
    mecanismes_orbiter_ext = detect_mecanismes(sources, MECANISMES_ORBITER_EXT)

    # Driver légal
    driver_legal = detect_driver_legal(sources)

    # Verdict
    verdict = compute_killer_feature_verdict(
        mecanismes_solaris,
        mecanismes_nexus_ext,
        mecanismes_orbiter_ext,
    )

    output = {
        "source": args.sections or args.source,
        "year_month": sources.get("year_month", "unknown"),
        "total_lines_scanned": sources.get("total_lines_scanned", 0),
        "mecanismes_solaris_4_canon": mecanismes_solaris,
        "mecanismes_nexus_5_ext": mecanismes_nexus_ext,
        "mecanismes_orbiter_5_ext": mecanismes_orbiter_ext,
        "driver_legal_canon": driver_legal,
        "killer_feature_verdict": verdict,
    }

    output_path = Path(args.output)
    output_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")

    # D1 receipt summary
    print(f"[D6] Killer Feature root cause verdict:")
    print(f"  Source: {args.sections or args.source}")
    print(f"  Year-month: {sources.get('year_month', 'unknown')}")
    print(f"  Solaris 4 mécanismes canon:")
    for name, info in mecanismes_solaris.items():
        print(f"    - {name}: {info['count']} anchors")
    print(f"  Nexus 5 mécanismes ext:")
    for name, info in mecanismes_nexus_ext.items():
        print(f"    - {name}: {info['count']} anchors")
    print(f"  Orbiter 5 mécanismes ext:")
    for name, info in mecanismes_orbiter_ext.items():
        print(f"    - {name}: {info['count']} anchors")
    print(f"  Driver légal canon:")
    for name, info in driver_legal.items():
        print(f"    - {name}: {info['count']} anchors")
    print(f"  Verdict: {verdict['verdict']}")
    print(f"  Output: {output_path.absolute()}")

    return 0


if __name__ == "__main__":
    sys.exit(main())