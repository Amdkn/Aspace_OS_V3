"""
collector_08_agents.py — Pilier Agents (👥) pour Citadelle A0.

Dresse l'inventaire des agents A'Space : A1(2)/A2(6)/A3(35) + B1(2)/B2(8)/B3(53)
per Plan source §3 architecture pages. Source : ~/.mavis/agents/ + registry canon.

Date : 2026-07-04 · Auteur : Mavis (MC/L1) — Plan Citadelle A0 P2
Source : ~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §3 page Agents
"""
from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(r"C:\Users\amado\.mavis\agents")
OUTPUT = Path(r"C:\Users\amado\agent-os\citadel\data\08_agents.json")


def scan_tier(tier: str, base: Path) -> list[dict]:
    if not base.exists():
        return []
    out = []
    for entry in sorted(base.iterdir()):
        if not entry.is_dir() or entry.name.startswith("_"):
            continue
        # Per agent: AGENTS.md + goal.md v2 + memory/
        ag = entry / "AGENTS.md"
        goal = entry / "goal.md"
        mem = entry / "memory"
        out.append({
            "name": entry.name,
            "tier": tier,
            "has_agents_md": ag.exists(),
            "has_goal": goal.exists(),
            "has_memory_dir": mem.exists(),
            "is_captain": "captain" in entry.name or entry.name in ("mavis", "b1-jerry-emyth"),
        })
    return out


def main() -> int:
    a1 = scan_tier("A1", ROOT / "A1" if (ROOT / "A1").exists() else ROOT)
    a2 = scan_tier("A2", ROOT / "A2" if (ROOT / "A2").exists() else ROOT)
    a3 = scan_tier("A3", ROOT / "A3" if (ROOT / "A3").exists() else ROOT)
    b1 = scan_tier("B1", ROOT)
    b2 = scan_tier("B2", ROOT)
    b3 = scan_tier("B3", ROOT)
    sys_agents = []
    for n in ("coder", "general", "mavis", "verifier"):
        p = ROOT / n
        if p.exists() and p.is_dir():
            sys_agents.append({"name": n, "tier": "SYS", "has_agents_md": (p / "AGENTS.md").exists(),
                               "has_goal": False, "has_memory_dir": (p / "memory").exists(),
                               "is_captain": n in ("mavis",)})

    all_agents = a1 + a2 + a3 + b1 + b2 + b3 + sys_agents
    payload = {
        "collector": "08_agents",
        "pillar": 8,
        "pillar_name": "Agents (👥)",
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "source": "~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §3 page Agents",
        "doctrine": "lecture seule — ne réveille JAMAIS les agents dormants — capitaine=Mavis",
        "tiers": {
            "A1": a1, "A2": a2, "A3": a3, "B1": b1, "B2": b2, "B3": b3, "SYS": sys_agents,
        },
        "all_agents": all_agents,
        "summary": {
            "total": len(all_agents),
            "A1": len(a1), "A2": len(a2), "A3": len(a3),
            "B1": len(b1), "B2": len(b2), "B3": len(b3),
            "SYS": len(sys_agents),
            "with_goal_v2": sum(1 for a in all_agents if a.get("has_goal")),
            "captains": sum(1 for a in all_agents if a.get("is_captain")),
            "plan_target": "A1(2)/A2(6)/A3(35) + B1(2)/B2(8)/B3(53) = 81 + 4 SYS = ~85",
        },
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[08_agents] OK → {OUTPUT} ({OUTPUT.stat().st_size} b)")
    s = payload["summary"]
    print(f"  total={s['total']} A1={s['A1']} A2={s['A2']} A3={s['A3']} B1={s['B1']} B2={s['B2']} B3={s['B3']} SYS={s['SYS']} captains={s['captains']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())