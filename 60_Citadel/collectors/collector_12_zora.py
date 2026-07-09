"""
collector_12_zora.py — Pilier Zora nightly (Dreaming) pour Citadelle A0.

État des 8 dimensions Jack version A'Space (Plan §6) :
  1. Conversation analysis → turn-journal + sessions .jsonl
  2. Cost intelligence → usage M3 vs tiers
  3. Skill performance → RUNS.log + LESSONS.md
  4. Memory health → wiki-lint + frontmatter coverage
  5. Session hygiene → tokens/session, zombies
  6. Workflow patterns → doublons
  7. External opportunities → veuille gated (WebSearch nocturne)
  8. Business outcomes → ratio signaux marché/handoffs

Sortie : 4 recommandations max/nuit (discipline Gwyn D11), lecture seule,
output append-only dans cron/output/.

Date : 2026-07-04 · Auteur : Mavis (MC/L1) — Plan Citadelle A0 P3 backend
Source : ~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §6 Zora nocturne
Gating : enable_zora.flag A0 HITL — sans flag : aucun auto-run.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

ROOT = Path(r"C:\Users\amado")
OUTPUT = Path(r"C:\Users\amado\agent-os\citadel\data\12_zora.json")
ZORA_FLAG = Path(r"C:\Users\amado\agent-os\citadel\decisions\enable_zora.flag")
ZORA_OUTPUT = Path(r"C:\Users\amado\agent-os\citadel\cron\output")
ZORA_CONFIG = Path(r"C:\Users\amado\agent-os\citadel\cron\zora-config.json")


def detect_zora_state() -> dict:
    """Lecture seule — état actuel des 8 dimensions Jack (sans produire de recommandations)."""
    return {
        "cron_enabled": ZORA_FLAG.exists(),
        "config_exists": ZORA_CONFIG.exists(),
        "output_dir_exists": ZORA_OUTPUT.exists(),
        "last_run_state": _last_run_state(),
        "dimensions": {
            "1_conversation_analysis": {"turn_journal": _count("00_Amadeus/turn-journal.md"),
                                          "sessions_jsonl": _count_glob("C:/Users/amado/.mavis/sessions/mvs_*/*.jsonl"),
                                          "note": "skill candidate — Skill Creator Reflex mécanisé"},
            "2_cost_intelligence": {"minimax_usage_api": "~3% rolling 5h per ADR-LD01-005",
                                      "hermes_costs": "TBD",
                                      "note": "ratio Opus-prices-for-Haiku-jobs"},
            "3_skill_performance": {"runs_log_count": 1, "lessons_md_count": 2,
                                      "note": "skills morts à tuer — rot-rate"},
            "4_memory_health": {"wiki_pages": _count("wiki", "*.md"),
                                  "memory_md_exists": (ROOT / ".mavis/agents/mavis/memory/MEMORY.md").exists(),
                                  "frontmatter_coverage": "TBD E3 audit"},
            "5_session_hygiene": {"tokens_per_session": "TBD average",
                                    "zombie_sessions": _count_glob("C:/Users/amado/.mavis/sessions/mvs_*")},
            "6_workflow_patterns": {"doublons_observed": "Posture: 4× competitive research recurrence"},
            "7_external_opportunities": {"websearch_nocturne": "gated par enable_zora.flag",
                                            "posture_c": "no cron sans GO A0"},
            "8_business_outcomes": {"signaux_marche": "Strategy Session metric",
                                      "handoffs": "57 handoffs/7j baseline"},
        },
    }


def _count(path: str, ext: str = "") -> int:
    p = ROOT / path
    if not p.exists():
        return 0
    if p.is_file():
        return 1
    return sum(1 for _ in p.rglob(ext or "*"))


def _count_glob(pattern: str) -> int:
    from glob import glob
    return len(glob(pattern))


def _last_run_state() -> dict:
    """État du dernier run Zora — si output existe, lit le plus récent."""
    if not ZORA_OUTPUT.exists():
        return {"last_run": "never", "recos_last_run": 0, "format": "discipline Gwyn D11 = 4 recos max"}
    runs = sorted(ZORA_OUTPUT.glob("zora-*.json"))
    if not runs:
        return {"last_run": "never"}
    last = runs[-1]
    try:
        data = json.loads(last.read_text(encoding="utf-8"))
        return {"last_run_file": last.name, "last_run_at": data.get("ran_at"),
                "recos_last_run": len(data.get("recos", [])), "format": "4 max"}
    except (json.JSONDecodeError, OSError):
        return {"last_run_file": last.name, "last_run": "unreadable"}


def main() -> int:
    state = detect_zora_state()
    payload = {
        "collector": "12_zora",
        "pillar": 12,
        "pillar_name": "Zora nightly (🌙 Dreaming)",
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "source": "~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §6 Zora nocturne (8 dimensions Jack)",
        "doctrine": "lecture seule — pas d'auto-approval — 4 recos max/nuit discipline Gwyn D11 — gated par enable_zora.flag",
        "cron_enabled": state["cron_enabled"],
        "config_exists": state["config_exists"],
        "output_dir_exists": state["output_dir_exists"],
        "last_run_state": state["last_run_state"],
        "dimensions": state["dimensions"],
        "summary": {
            "cron_enabled": state["cron_enabled"],
            "dimensions_tracked": len(state["dimensions"]),
            "recos_format": "4 max/nuit per Gwyn D11",
        },
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[12_zora] OK → {OUTPUT} ({OUTPUT.stat().st_size} b)")
    print(f"  cron_enabled={payload['cron_enabled']} output_dir={payload['output_dir_exists']} last_run={state['last_run_state'].get('last_run')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())