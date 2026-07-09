"""
collector_14_warmode.py — Observabilité War Mode pour la Citadelle.

NO-HITL ≠ NO-VISIBILITY : quand A0-Amodei tourne en autonomie (12WY_ON_PAUSE),
A+ ne veut pas intervenir mais veut VOIR. Ce collector agrège l'état war-mode
depuis les fichiers append-only (inaliénable #4 rendu visible) → data/14_warmode.json
+ un digest texte poussable à Telegram.

Pur stdlib, idempotent, lecture seule. Sortie :
  - data/14_warmode.json  (servi par serve.py à /api/data/14_warmode)
  - data/14_warmode_digest.txt  (le texte poussé à Telegram)
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path

CITADEL = Path(__file__).resolve().parent.parent
DECISIONS = CITADEL / "decisions"
DATA = CITADEL / "data"
FLAG = DECISIONS / "12WY_ON_PAUSE.flag"


def _now() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def war_mode_active() -> bool:
    if not FLAG.exists():
        return False
    try:
        return "WAR_MODE=ON" in FLAG.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False


def read_decisions() -> list[dict]:
    """Toutes les décisions append-only, plus récentes d'abord (par mtime)."""
    out: list[dict] = []
    if not DECISIONS.exists():
        return out
    for f in sorted(DECISIONS.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        d["_file"] = f.name
        d["_mtime"] = datetime.fromtimestamp(f.stat().st_mtime, timezone.utc).astimezone().isoformat(timespec="seconds")
        out.append(d)
    return out


def active_flags() -> list[dict]:
    return [{"flag": f.name, "active": True}
            for f in sorted(DECISIONS.glob("*.flag"))] if DECISIONS.exists() else []


def kill_switches() -> dict:
    """ClaudeClaw Mission Control : défaut ON, interrupteurs d'urgence granulaires."""
    cfg = CITADEL / "mission_control.json"
    try:
        d = json.loads(cfg.read_text(encoding="utf-8"))
        sw = d.get("kill_switches", {})
        return {"switches": sw, "meaning": d.get("switch_meaning", {}),
                "any_off": any(v is False for v in sw.values())}
    except (OSError, json.JSONDecodeError):
        return {"switches": {}, "meaning": {}, "any_off": False}


def hive_mind_log(decisions: list[dict]) -> list[dict]:
    """Cross-agent activity log (ClaudeClaw pattern) : qui a fait quoi, quand."""
    log = []
    for d in decisions:
        actor = (d.get("generated_by") or d.get("actor") or d.get("ratified_by")
                 or ("A0-Amodei" if "warmode" in d.get("_file", "").lower() or "PAUSE" in d.get("_file", "")
                     else "system"))
        actor = str(actor).split("(")[0].strip()[:40]
        log.append({"agent": actor, "when": d.get("_mtime"),
                    "action": d.get("action", d.get("choice", "decision")),
                    "summary": str(d.get("decision") or d.get("doctrine") or d.get("title")
                                    or d.get("a0_intent_verbatim") or d.get("_file"))[:140]})
    return log[:20]


def mission_tasks() -> list[dict]:
    """Dark Factory J1-J7 (mission_tasks pattern) depuis les decisions darkfactory."""
    tasks = []
    for f in sorted(DECISIONS.glob("*darkfactory*.json"), key=lambda p: p.name):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        tasks.append({"task": f.stem, "state": d.get("state", "done"),
                      "summary": (d.get("decision") or d.get("doctrine") or "")[:120]})
    return tasks


def build() -> dict:
    active = war_mode_active()
    decisions = read_decisions()
    # Compte par type d'action A0 (ratify/bypass/delegate/extend/darkfactory/warmode)
    by_action: dict[str, int] = {}
    for d in decisions:
        a = d.get("action") or ("warmode" if "WARMODE" in d.get("_file", "").upper() or "PAUSE" in d.get("_file", "") else "decision")
        by_action[a] = by_action.get(a, 0) + 1
    last10 = [{"file": d["_file"], "when": d.get("_mtime"),
               "action": d.get("action", "decision"),
               "summary": str(d.get("decision") or d.get("doctrine") or d.get("a0_intent_verbatim") or "")[:180]}
              for d in decisions[:10]]
    return {
        "generated_at": _now(),
        "war_mode": "ON" if active else "OFF",
        "flag_file": str(FLAG.relative_to(CITADEL)) if FLAG.exists() else None,
        "active_flags": active_flags(),
        "decisions_total": len(decisions),
        "decisions_by_action": by_action,
        "kill_switches": kill_switches(),
        "hive_mind_log": hive_mind_log(decisions),
        "mission_tasks": mission_tasks(),
        "last_10_decisions": last10,
        "veto_unique": "Beth — vie/santé A+ (SEUL veto inaliénable)",
        "portes_a_ouvrir": [
            "Porte 0 — Bypass par défaut : ouvert = anti-panique (fermer = paniquer)",
            "Porte Rick — sobriété-LEVIER, plus un veto : ouvre au lieu de bloquer",
            "Porte /ship — deploy outward = porte à rendre sûre-à-ouvrir (pas de Stark, il est B3)",
            "Porte append-only — fenêtre d'observation (NO-HITL ≠ NO-VISIBILITY), infra pas frein",
        ],
    }


def digest_text(state: dict) -> str:
    lines = [
        f"🔴 WAR MODE {state['war_mode']} — Citadelle A0 · {state['generated_at']}",
        f"Décisions autonomes A0 : {state['decisions_total']} "
        f"({', '.join(f'{k}:{v}' for k, v in state['decisions_by_action'].items())})",
        "",
        "Dernières décisions (append-only, A+ observe, n'intervient pas) :",
    ]
    for d in state["last_10_decisions"][:5]:
        lines.append(f"  • [{d['action']}] {d['file']} — {d['summary']}")
    airlock_f = DATA / "airlock_line.txt"
    if airlock_f.exists():
        lines.append(airlock_f.read_text(encoding="utf-8").strip())
    lines += ["", "Veto unique : Beth vie/santé. Le reste = PORTES à ouvrir (HxH), plus des freins.",
              "http://127.0.0.1:8770/warmode"]
    return "\n".join(lines)


def main() -> int:
    DATA.mkdir(exist_ok=True)
    state = build()
    (DATA / "14_warmode.json").write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    (DATA / "14_warmode_digest.txt").write_text(digest_text(state), encoding="utf-8")
    print(digest_text(state))
    print(f"\n[warmode] -> data/14_warmode.json + data/14_warmode_digest.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
