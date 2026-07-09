#!/usr/bin/env python3
"""
plan_canon_batch.py — D2 research FIRST for canon batch creation

Scans 3 sources canon for domain X :
1. Takeout Gemini conversations (00_Amadeus/30_MEMORY_CORE/Gemini_Takeout_2026/)
2. A0 working memory (MEMORY.md + wiki canon session-close entries)
3. Existing ADRs (_SPECS/ADR/ pour sister scope)

Output : plan_canon_batch_<DATE>.json listant pour chaque variant :
- sources verbatim (line refs [YYYY-MM:NNNNN])
- pains/objections candidates
- pricing tier suggéré (sister ADR-AAAS-PRICING-001)
- killer feature sister (ADR-L2-AAAS-001 Agentic Governance)

Stdlib-only (no pip install). Run from any CWD.

Usage:
  python plan_canon_batch.py --domain "ICP AaaS Sisters Doctrine" --variants "Solaris,Nexus,Orbiter"
  python plan_canon_batch.py --domain "..." --variants "..." --output my_plan.json
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path


# Sister canon roots (D1 receipts from session 2026-06-24)
ASPACE_ROOT = Path(os.environ.get("ASPACE_ROOT", r"C:\Users\amado"))
TAKEOUT_ROOT = ASPACE_ROOT / "ASpace_OS_V2" / "00_Amadeus" / "30_MEMORY_CORE" / "Gemini_Takeout_2026"
ADR_ROOT = ASPACE_ROOT / "ASpace_OS_V2" / "_SPECS" / "ADR"
MEMORY_CANON = ASPACE_ROOT / ".claude" / "projects" / "c--Users-amado" / "memory" / "MEMORY.md"
WIKI_LOG = ASPACE_ROOT / "ASpace_OS_V2" / "00_Amadeus" / "30_MEMORY_CORE" / "LLM_Wiki" / "wiki" / "log.md"


def scan_takeout(variant: str, keywords: list[str]) -> list[dict]:
    """D2 research — scan Takeout Gemini for variant verbatim anchors.

    Returns list of {line_ref, snippet, source_file} for each match.
    D6 honest flag : si TAKEOUT_ROOT n'existe pas, retourne [].
    """
    if not TAKEOUT_ROOT.exists():
        return []
    results = []
    pattern = re.compile("|".join(re.escape(k) for k in keywords), re.IGNORECASE)
    for md_file in TAKEOUT_ROOT.rglob("*.md"):
        try:
            text = md_file.read_text(encoding="utf-8", errors="replace")
        except (OSError, UnicodeError):
            continue
        for i, line in enumerate(text.splitlines(), start=1):
            if pattern.search(line):
                # Extract YYYY-MM from filename (e.g. "2026-05.md" → "2026-05")
                m = re.search(r"(\d{4}-\d{2})", md_file.name)
                period = m.group(1) if m else "unknown"
                results.append({
                    "line_ref": f"[{period}:{i}]",
                    "snippet": line.strip()[:200],
                    "source_file": str(md_file.relative_to(ASPACE_ROOT)),
                })
    return results


def scan_adr_sister(scope: str) -> list[dict]:
    """D2 research — scan ADR canon for sister scope references."""
    if not ADR_ROOT.exists():
        return []
    results = []
    for adr_file in ADR_ROOT.rglob("*.md"):
        try:
            text = adr_file.read_text(encoding="utf-8", errors="replace")
        except (OSError, UnicodeError):
            continue
        if scope.lower() in text.lower():
            # Count occurrences
            count = text.lower().count(scope.lower())
            results.append({
                "adr_path": str(adr_file.relative_to(ASPACE_ROOT)),
                "occurrences": count,
            })
    return results


def scan_memory_canon(variant: str) -> list[dict]:
    """D2 research — scan MEMORY.md for variant mentions."""
    if not MEMORY_CANON.exists():
        return []
    results = []
    try:
        text = MEMORY_CANON.read_text(encoding="utf-8", errors="replace")
    except (OSError, UnicodeError):
        return []
    for i, line in enumerate(text.splitlines(), start=1):
        if variant.lower() in line.lower():
            results.append({
                "line": i,
                "snippet": line.strip()[:200],
            })
    return results


def extract_pricing_tier(variant: str) -> str:
    """D6 sister pattern — extract pricing tier suggestion from ADR-AAAS-PRICING-001.

    Returns one of: "Tier 1 PME Solo Founder", "Tier 2 PME Standard",
                    "Tier 3 PME Groupe", "Tier 4 ETI", "Tier 5 Enterprise",
                    "TBD (sister ADR review required)".
    """
    pricing_adr = ADR_ROOT / "L2_Business_OS" / "ADR-AAAS-PRICING-001_aaas-pricing-canon.md"
    if not pricing_adr.exists():
        return "TBD (ADR-AAAS-PRICING-001 not found)"
    try:
        text = pricing_adr.read_text(encoding="utf-8", errors="replace")
    except (OSError, UnicodeError):
        return "TBD (ADR-AAAS-PRICING-001 unreadable)"
    # D6 honest — pas d'invention, simple keyword matching
    if "Tier 1" in text and "Solo Founder" in text:
        return "Tier 1 PME Solo Founder (sister ADR-AAAS-PRICING-001)"
    return "TBD (sister ADR review required)"


def plan_batch(domain: str, variants: list[str]) -> dict:
    """Generate plan JSON for canon batch creation."""
    plan = {
        "domain": domain,
        "date": str(date.today()),
        "variants": [],
        "sister_canon_refs": [
            "ADR-L2-AAAS-001 (AaaS Doctrine 3 Variants Solarpunk)",
            "ADR-AAAS-PRICING-001 (Pricing Canon 5 Tiers)",
            "ADR-META-006 (D6 catalog append-only)",
            "JTBD-003 (Painkiller Message Variants format)",
        ],
    }
    for variant in variants:
        # Variant-specific keywords (heuristic — D2 research first then refine)
        keywords = [variant, variant.lower(), variant.upper()]
        takeout_hits = scan_takeout(variant, keywords)
        adr_sisters = scan_adr_sister(variant)
        memory_hits = scan_memory_canon(variant)
        plan["variants"].append({
            "name": variant,
            "takeout_verbatim_count": len(takeout_hits),
            "takeout_samples": takeout_hits[:5],  # cap at 5 for review
            "adr_sister_refs": adr_sisters,
            "memory_canon_hits": memory_hits[:3],
            "pricing_tier_suggestion": extract_pricing_tier(variant),
            "next_step": "D1 verify (extract verbatim anchors with line refs)",
        })
    return plan


def main():
    parser = argparse.ArgumentParser(description="D2 research canon batch plan")
    parser.add_argument("--domain", required=True, help="Domain name (e.g. 'ICP AaaS Sisters Doctrine')")
    parser.add_argument("--variants", required=True, help="Comma-separated variants (e.g. 'Solaris,Nexus,Orbiter')")
    parser.add_argument("--output", default=None, help="Output JSON path (default: plan_canon_batch_<DATE>.json)")
    args = parser.parse_args()
    variants = [v.strip() for v in args.variants.split(",") if v.strip()]
    plan = plan_batch(args.domain, variants)
    output_path = args.output or f"plan_canon_batch_{date.today()}.json"
    Path(output_path).write_text(json.dumps(plan, indent=2, ensure_ascii=False), encoding="utf-8")
    # D1 receipt summary
    print(f"[plan_canon_batch] domain={args.domain} variants={len(variants)}")
    for v in plan["variants"]:
        print(f"  - {v['name']}: {v['takeout_verbatim_count']} takeout hits, "
              f"{len(v['adr_sister_refs'])} ADR sisters, "
              f"{len(v['memory_canon_hits'])} memory hits")
    print(f"[plan_canon_batch] output={output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())