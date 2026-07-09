"""
collector_09_frameworks.py — Pilier Frameworks Life OS (🎡) pour Citadelle A0.

Russian doll pattern : 12WY ⊃ PARA ⊃ DEAL + GTD + Ikigai + Life Wheel.
Lit depuis ASpace OS V2 sources canoniques.

Date : 2026-07-04 · Auteur : Mavis (MC/L1) — Plan Citadelle A0 P2
Source : ~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §3 page Frameworks
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

ROOT = Path(r"C:\Users\amado\ASpace_OS_V2\20_Life_OS")
LD01 = ROOT / "22_Wheel_Discovery" / "LD01_Business_Book"
OUTPUT = Path(r"C:\Users\amado\agent-os\citadel\data\09_frameworks.json")


def detect_framework(name: str, paths: list[Path], description: str) -> dict:
    present = any(p.exists() for p in paths)
    return {
        "name": name,
        "description": description,
        "paths": [str(p) for p in paths],
        "present": present,
    }


def main() -> int:
    frameworks = [
        detect_framework(
            "12WY (12 Week Year)",
            [ROOT / "24_PARA_Enterprise" / "01_PARA" / "12_Week_Year"],
            "Objectif: Execution 12 semaines. Source canon: Life OS V0.6.2.",
        ),
        detect_framework(
            "PARA",
            [ROOT / "24_PARA_Enterprise" / "01_PARA"],
            "Projects · Areas · Resources · Archives. Russian doll parent.",
        ),
        detect_framework(
            "DEAL",
            [ROOT / "21_DEAL"],
            "Direction · Execution · Analytics · Learning. Cynefin-aware.",
        ),
        detect_framework(
            "GTD (Getting Things Done)",
            [Path(r"C:\Users\amado\.claude\skills\multi-routines-12wy"),
             Path(r"C:\Users\amado\.claude\skills\multi-goal")],
            "Capture · Clarify · Organize · Reflect · Engage.",
        ),
        detect_framework(
            "Ikigai",
            [ROOT / "22_Wheel_Discovery"],
            "Purpose · Vocation · Profession · Passion intersection.",
        ),
        detect_framework(
            "Life Wheel (Morty/Beth Russian doll)",
            [ROOT / "22_Wheel_Discovery" / "LD01_Business_Book" / "20_skeleton"],
            "Wheel-of-Life 9-cell matrix : Health · Work · Relationships × 3 sub-scores each.",
        ),
    ]
    payload = {
        "collector": "09_frameworks",
        "pillar": 9,
        "pillar_name": "Frameworks Life OS (🎡 — russian doll)",
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "source": "~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §3 page Frameworks Life OS",
        "doctrine": "lecture seule — russian doll parent ⊃ child — pas de duplication",
        "frameworks": frameworks,
        "summary": {
            "total": len(frameworks),
            "present": sum(1 for f in frameworks if f["present"]),
            "russian_doll_chain": "12WY ⊃ PARA ⊃ DEAL + GTD + Ikigai + Life Wheel",
        },
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[09_frameworks] OK → {OUTPUT} ({OUTPUT.stat().st_size} b)")
    print(f"  total={payload['summary']['total']} present={payload['summary']['present']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())