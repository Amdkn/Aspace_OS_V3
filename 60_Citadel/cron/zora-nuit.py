"""
zora-nuit.py — Zora nightly digest (Plan Citadelle §6, 8 dimensions Jack).

Génère ≤4 recommandations/nuit, append-only dans cron/output/.

GATING (FREIN À MAIN) : REFUSE de tourner sans le flag
  decisions/enable_zora.flag
posé par A0 HITL explicite. Posture C = no cron without GO.

Usage :
  python zora-nuit.py [--dry-run]

Date : 2026-07-04 · Auteur : Mavis (MC/L1) — Plan Citadelle A0 P3 backend
Source : ~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §6 Zora nocturne
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).parent.parent
FLAG = ROOT / "decisions" / "enable_zora.flag"
OUTPUT_DIR = ROOT / "cron" / "output"
CONFIG = ROOT / "cron" / "zora-config.json"
MAX_RECOS = 4


def require_flag() -> bool:
    """Posture C strict — no cron sans A0 HITL GO.
    12WY-ON-PAUSE check FIRST : Tony pré-ratification 12 sem bypass individual gates.
    """
    twelve_wy_pause = FLAG.parent / "12WY_ON_PAUSE.flag"
    if twelve_wy_pause.exists():
        return True
    return FLAG.exists()


def ensure_dirs() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def read_stats() -> dict:
    stats_p = ROOT / "data" / "12_zora.json"
    if not stats_p.exists():
        return {"warning": "12_zora.json missing — run collect first"}
    try:
        return json.loads(stats_p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {"warning": "12_zora.json unreadable"}


def generate_recos(stats: dict) -> list[dict]:
    """Génère ≤4 recommandations. Idempotent : même stats → même recos.
    Discipline Gwyn D11 ≠ 0 : on ne marque 'fait' qu'après action A0 HITL."""
    recos = []
    dimensions = stats.get("dimensions", {})

    # 1. Memory health — si pas assez de frontmatter coverage
    mem = dimensions.get("4_memory_health", {})
    if isinstance(mem, dict) and mem.get("frontmatter_coverage") == "TBD E3 audit":
        recos.append({
            "id": "zora-mem-lint",
            "label": "Lancer wiki-lint E3 pour mesurer frontmatter coverage (memory health)",
            "payload": {"script": "wiki-lint", "metric": "frontmatter_coverage"},
            "source_dimension": "4_memory_health",
            "roi_estimate": "memory health ↑ → Eero observational memory effectiveness ↑",
        })
    # 2. Skill performance — toujours utile (LESSONS.md append-only)
    skills = dimensions.get("3_skill_performance", {})
    if isinstance(skills, dict):
        recos.append({
            "id": "zora-skills-rot",
            "label": "Identifier skills morts via RUNS.log (rot-rate check)",
            "payload": {"check": "runs_log_count_vs_total_skills", "threshold": 0.1},
            "source_dimension": "3_skill_performance",
            "roi_estimate": "savings de tokens — kill skills non-utilisés",
        })
    # 3. Cost intelligence
    cost = dimensions.get("2_cost_intelligence", {})
    if isinstance(cost, dict) and "TBD" in cost.get("hermes_costs", ""):
        recos.append({
            "id": "zora-cost-hermes",
            "label": "Mesurer les costs Hermes (coût réel vs MiniMax Year-3000)",
            "payload": {"tool": "analyze-usage", "target": "hermes"},
            "source_dimension": "2_cost_intelligence",
            "roi_estimate": "cohérence Year-3000 cost reality",
        })
    # 4. Business outcomes — toujours 1 recos sur signaux/handoffs ratio
    biz = dimensions.get("8_business_outcomes", {})
    if isinstance(biz, dict):
        recos.append({
            "id": "zora-biz-ratio",
            "label": "Mesurer ratio signaux marché / handoffs (Strategy Session metric)",
            "payload": {"metric": "signaux/handoffs", "baseline_57_handovers_7j": "voir W3 strategy session"},
            "source_dimension": "8_business_outcomes",
            "roi_estimate": "détection des signaux faibles → leverage Direction",
        })

    return recos[:MAX_RECOS]


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    dry_run = "--dry-run" in argv

    if not require_flag():
        print(f"REFUSED: missing {FLAG} — A0 HITL gate required (Posture C — no cron without GO)")
        print("To enable: New-Item -ItemType File '{}'".format(str(FLAG).replace("/", "\\")))
        return 2

    ensure_dirs()
    stats = read_stats()
    recos = generate_recos(stats)

    ts = time.strftime("%Y%m%d-%H%M")
    payload = {
        "ran_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "config_version": "0.1",
        "stats_snapshot": stats.get("summary", {}),
        "recos": recos,
        "count": len(recos),
        "max_recos": MAX_RECOS,
        "doctrine": "lecture seule — append-only — anti-Ultron — pas d'auto-approval",
        "status": "DECIDED" if not dry_run else "DRY-RUN",
    }

    if dry_run:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 0

    out_path = OUTPUT_DIR / f"zora-{ts}.json"
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"zora-nuit OK → {out_path} ({out_path.stat().st_size} b) — {len(recos)} recos max {MAX_RECOS}")
    for r in recos:
        print(f"  [{r['id']}] {r['label']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())