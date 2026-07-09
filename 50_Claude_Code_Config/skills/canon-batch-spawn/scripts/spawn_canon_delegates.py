#!/usr/bin/env python3
"""
spawn_canon_delegates.py — D6 root cause first + parallel sub-agent spawn

Reads plan_canon_batch_<DATE>.json, identifies cross-variant contrasts (D6),
and emits a parallel sub-agent dispatch manifest (NOT actual agent spawning —
that requires Claude Code Agent tool which is unavailable in stdlib).

Outputs dispatch_manifest_<DATE>.json listant :
- 5 agents (Morty/Beth/A0) avec livrables assignés
- Parallel sequencing (parallel block + sequential gate)
- Sister canon refs per agent

Stdlib-only. Run from any CWD.

Usage:
  python spawn_canon_delegates.py --plan plan_canon_batch_2026-06-24.json
  python spawn_canon_delegates.py --plan plan.json --parallel True --audit-beth True
"""

import argparse
import json
import sys
from datetime import date
from pathlib import Path


# 5-agent orchestration pattern (D1 receipts from session 2026-06-24 success)
AGENT_TEMPLATES = [
    {
        "agent_id": "A1-Morty-001",
        "role": "Exécution patterns (sister Morty execution protocol)",
        "parallel_block": 1,
        "livrables": "N ADRs + N JTBDs + 1 wiki handoff",
        "sub_agents_per_variant": True,
        "estimated_minutes": 20,
    },
    {
        "agent_id": "A1-Beth-Audit-002",
        "role": "Audit cohérence canon (sister A1 Beth Veto)",
        "parallel_block": 2,
        "livrables": "Verdict CONDITIONAL GO/NO-GO + gaps list",
        "sub_agents_per_variant": False,
        "estimated_minutes": 5,
    },
    {
        "agent_id": "A1-Beth-NotionSync-003",
        "role": "Notion sync reco (HITL ready-to-coller)",
        "parallel_block": 2,
        "livrables": "Playbook Notion 15 min sub-agent HITL",
        "sub_agents_per_variant": False,
        "estimated_minutes": 3,
    },
    {
        "agent_id": "A0-Amadeus-Review-004",
        "role": "Review final + décisions (META-OS PASSIF)",
        "parallel_block": 3,
        "livrables": "Pick next options + authorize fix HIGH gap",
        "sub_agents_per_variant": False,
        "estimated_minutes": 5,
    },
    {
        "agent_id": "A1-Morty-Close-005",
        "role": "Session close (wiki log + MEMORY.md + meta-skill si nouveau pattern)",
        "parallel_block": 4,
        "livrables": "wiki/log.md entry + MEMORY.md topic rows + /canon-batch-spawn skill (Hermes-style Phase 2)",
        "sub_agents_per_variant": False,
        "estimated_minutes": 5,
    },
]


def detect_cross_variant_drift(plan: dict) -> list[dict]:
    """D6 root cause — identify variants with overlapping persona/mantra/marché.

    Anti-pattern : 2 variants avec même persona_archétype ou même mantra = fusionner.
    Returns list of drift findings.
    """
    drift = []
    variants = plan.get("variants", [])
    if len(variants) < 2:
        return drift
    # D6 heuristic : si 2 variants ont <5 takeout hits ET 0 ADR sisters distincts
    # → probable redondance, à fusionner
    for i, v1 in enumerate(variants):
        for j, v2 in enumerate(variants[i+1:], start=i+1):
            if (v1["takeout_verbatim_count"] < 5 and v2["takeout_verbatim_count"] < 5
                    and len(v1["adr_sister_refs"]) == 0 and len(v2["adr_sister_refs"]) == 0):
                drift.append({
                    "type": "low_signal_both_variants",
                    "v1": v1["name"],
                    "v2": v2["name"],
                    "recommendation": "consider fusion or deeper D2 research",
                })
    return drift


def build_dispatch_manifest(plan: dict, parallel: bool, audit_beth: bool) -> dict:
    """Build parallel sub-agent dispatch manifest from plan."""
    variants = plan.get("variants", [])
    manifest = {
        "domain": plan.get("domain"),
        "date": str(date.today()),
        "parallel_mode": parallel,
        "audit_beth_enabled": audit_beth,
        "notion_sync_enabled": True,  # always recommend
        "variants_count": len(variants),
        "agents": AGENT_TEMPLATES.copy(),
        "drift_findings": detect_cross_variant_drift(plan),
        "sister_canon_refs": plan.get("sister_canon_refs", []),
        "estimated_total_minutes": sum(a["estimated_minutes"] for a in AGENT_TEMPLATES),
    }
    # Disable Beth audit agent if --no-audit-beth
    if not audit_beth:
        manifest["agents"] = [a for a in manifest["agents"] if "Audit" not in a["agent_id"]]
    # Annotate Agent 1 with per-variant sub-agents
    for agent in manifest["agents"]:
        if agent["agent_id"] == "A1-Morty-001":
            agent["sub_agent_count"] = len(variants)
            agent["sub_agent_targets"] = [v["name"] for v in variants]
    return manifest


def main():
    parser = argparse.ArgumentParser(description="Spawn canon batch delegate manifest")
    parser.add_argument("--plan", required=True, help="Path to plan_canon_batch_<DATE>.json")
    parser.add_argument("--parallel", default="True", help="Parallel mode (True/False)")
    parser.add_argument("--audit-beth", default="True", help="Enable Beth audit agent (True/False)")
    parser.add_argument("--output", default=None, help="Output manifest path (default: dispatch_manifest_<DATE>.json)")
    args = parser.parse_args()
    plan_path = Path(args.plan)
    if not plan_path.exists():
        print(f"[spawn_canon_delegates] ERROR: plan file not found: {args.plan}", file=sys.stderr)
        return 1
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    parallel = args.parallel.lower() in ("true", "1", "yes")
    audit_beth = args.audit_beth.lower() in ("true", "1", "yes")
    manifest = build_dispatch_manifest(plan, parallel, audit_beth)
    output_path = args.output or f"dispatch_manifest_{date.today()}.json"
    Path(output_path).write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    # D1 receipt summary
    print(f"[spawn_canon_delegates] domain={manifest['domain']}")
    print(f"[spawn_canon_delegates] variants={manifest['variants_count']} parallel={parallel} audit_beth={audit_beth}")
    print(f"[spawn_canon_delegates] agents_dispatched={len(manifest['agents'])}")
    for agent in manifest["agents"]:
        print(f"  - {agent['agent_id']} (block {agent['parallel_block']}): {agent['livrables']}")
    if manifest["drift_findings"]:
        print(f"[spawn_canon_delegates] DRIFT FINDINGS ({len(manifest['drift_findings'])}):")
        for d in manifest["drift_findings"]:
            print(f"  ! {d['type']}: {d['v1']} <-> {d['v2']}")
    print(f"[spawn_canon_delegates] estimated_total={manifest['estimated_total_minutes']}min")
    print(f"[spawn_canon_delegates] output={output_path}")
    print(f"[spawn_canon_delegates] NOTE: this script emits manifest only.")
    print(f"[spawn_canon_delegates] Actual agent spawning requires Claude Code Agent tool (out of stdlib scope).")
    return 0


if __name__ == "__main__":
    sys.exit(main())