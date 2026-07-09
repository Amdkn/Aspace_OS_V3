"""
collect_metrics.py — Sweep D1 mécanique de la semaine pour la Strategy Session.

Agnostique : pur Python stdlib, invocable par n'importe quel harness ou terminal.
Sort un metrics JSON dans sessions/ (persistant) + résumé stdout.
L'agent (CC/Codex/Gemini/Hermes) lit ce JSON pour AUTEURER questions.json —
les questions doivent viser des faits MESURÉS, jamais du coaching générique.

Env :
  WIKI_ROOT     default ASpace wiki
  ADR_ROOT      default ASpace _SPECS/ADR
  PLANS_DIR     default ~/.claude/plans
  STRATEGY_DIR  default ASpace 00_Amadeus/strategy_sessions
  GEORDI_ROOT   default ASpace 03_Resources_Geordi
  WEEK_DAYS     default 7 (fenêtre de sweep)
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
ASPACE = Path(r"C:\Users\amado\ASpace_OS_V2")
DEFAULTS = {
    "WIKI_ROOT": ASPACE / "00_Amadeus" / "30_MEMORY_CORE" / "LLM_Wiki" / "wiki",
    "ADR_ROOT": ASPACE / "_SPECS" / "ADR",
    "PLANS_DIR": Path.home() / ".claude" / "plans",
    "STRATEGY_DIR": ASPACE / "00_Amadeus" / "strategy_sessions",
    "GEORDI_ROOT": ASPACE / "20_Life_OS" / "24_PARA_Enterprise" / "03_Resources_Geordi",
}


def _p(name: str) -> Path:
    return Path(os.environ.get(name, DEFAULTS[name]))


def recent(paths, cutoff: float):
    return [p for p in paths if p.is_file() and p.stat().st_mtime >= cutoff]


def adr_statuses(adr_root: Path) -> dict:
    out: dict[str, list[str]] = {}
    for f in adr_root.rglob("ADR-*.md"):
        try:
            head = f.read_text(encoding="utf-8", errors="replace")[:2000]
        except OSError:
            continue
        m = re.search(r"^status:\s*(\S+)", head, re.MULTILINE | re.IGNORECASE)
        status = (m.group(1).upper() if m else "UNKNOWN")
        out.setdefault(status, []).append(f.name)
    return out


def main() -> int:
    week_days = int(os.environ.get("WEEK_DAYS", "7"))
    cutoff = time.time() - week_days * 86400
    wiki, adr_root = _p("WIKI_ROOT"), _p("ADR_ROOT")
    plans_dir, strat_dir, geordi = _p("PLANS_DIR"), _p("STRATEGY_DIR"), _p("GEORDI_ROOT")

    handoffs = recent((wiki / "hand_offs").glob("*.md"), cutoff)
    signals = recent((wiki / "hand_offs").glob("signal*.md"), cutoff)
    plans_touched = recent(plans_dir.glob("*.md"), cutoff)
    adrs = adr_statuses(adr_root)
    geordi_files = list((geordi / "09_Life_OS").rglob("*.md")) if geordi.exists() else []
    prior_sessions = sorted(strat_dir.glob("*_strategy_session.html")) if strat_dir.exists() else []

    # Marqueurs "GO ouvert" dans les plans touchés (proxy backlog décisions A0)
    open_gos = 0
    for p in plans_touched:
        try:
            open_gos += len(re.findall(r"gated?\s+A0|GO\s+(?:requis|pending|attendu)|attend\s+GO",
                                       p.read_text(encoding="utf-8", errors="replace"), re.IGNORECASE))
        except OSError:
            pass

    metrics = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "window_days": week_days,
        "handoffs_week": len(handoffs),
        "handoff_names": sorted(p.name for p in handoffs),
        "signals_week": len(signals),
        "plans_touched_week": sorted(p.name for p in plans_touched),
        "adr_by_status": {k: len(v) for k, v in sorted(adrs.items())},
        "adr_proposed_list": sorted(adrs.get("PROPOSED", [])),
        "open_go_markers": open_gos,
        "geordi_resources_total": len(geordi_files),
        "prior_sessions": [p.name for p in prior_sessions],
    }

    sessions_dir = SKILL_DIR / "sessions"
    sessions_dir.mkdir(exist_ok=True)
    out = sessions_dir / f"metrics-{time.strftime('%Y-%m-%d')}.json"
    out.write_text(json.dumps(metrics, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(metrics, indent=2, ensure_ascii=False))
    print(f"\n[metrics] -> {out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
