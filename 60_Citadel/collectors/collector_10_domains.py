"""
collector_10_domains.py — Pilier Domaines Business OS (🏢) pour Citadelle A0.

Matrice 8 domaines Jerry × 3 Captains Summers = 53 B3 rosters canon.
Lit depuis LD01/30_Business_OS (sister canon).

Date : 2026-07-04 · Auteur : Mavis (MC/L1) — Plan Citadelle A0 P2
Source : ~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §3 page Domaines Business OS
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

ROOT = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\30_Business_OS")
OUTPUT = Path(r"C:\Users\amado\agent-os\citadel\data\10_domains.json")


def main() -> int:
    # 8 domaines Jerry × 3 Captains Summers
    domains = []
    for d in ["01_Sales", "02_Marketing", "03_Operations", "04_Finance",
              "05_Legal", "06_People", "07_Product", "08_IT"]:
        p = ROOT / d
        domains.append({
            "jerry_domain": d,
            "path": str(p),
            "exists": p.exists(),
            "has_roster": (p / "_ROSTER.md").exists() if p.exists() else False,
            "b3_count_target": 53 // 8,  # approximation
        })
    payload = {
        "collector": "10_domains",
        "pillar": 10,
        "pillar_name": "Domaines Business OS (🏢)",
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "source": "~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §3 page Domaines",
        "doctrine": "lecture seule — matrice 8 × 3 = 53 B3 rosters canon",
        "domains": domains,
        "captains_summers": ["summers_product", "summers_growth", "summers_ops"],
        "summary": {
            "total": len(domains),
            "exists_count": sum(1 for d in domains if d["exists"]),
            "plan_target": "8 domaines Jerry × 3 Captains = matrice 53 B3 rosters",
            "russian_doll": "PARA ⊃ domain ⊃ icp ⊃ roster",
        },
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[10_domains] OK → {OUTPUT} ({OUTPUT.stat().st_size} b)")
    print(f"  total={payload['summary']['total']} exists={payload['summary']['exists_count']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())