"""
collector_13_harnesses_live.py — Pilier Harnesses live (🛰️ runtime state) pour Citadelle A0.

État temps-réel des harnesses : sessions count, last activity, processes actifs.
Sources : ~/.claude/sessions/*.jsonl + ~/.mavis/sessions/mvs_*/ + ~/.hermes/sessions/
         + ~/.hermes/processes.json

DOCTRINE : lecture seule. Aucune mutation. Pid detection lecture.

Date : 2026-07-04 · Auteur : Mavis (MC/L1) — Plan Citadelle A0 P3 backend
Source : ~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §3 page Harnesses + §5
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

ROOT = Path(r"C:\Users\amado")
OUTPUT = Path(r"C:\Users\amado\agent-os\citadel\data\13_harnesses_live.json")


def _count_sessions(base: Path, glob_pat: str) -> dict:
    if not base.exists():
        return {"count": 0, "last_modified": "n/a"}
    files = sorted(base.glob(glob_pat))
    if not files:
        return {"count": 0, "last_modified": "n/a"}
    last = max(files, key=lambda f: f.stat().st_mtime)
    return {"count": len(files), "last_modified": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(last.stat().st_mtime)),
            "last_path": str(last.name)[:60]}


def detect_claude_code_live() -> dict:
    base = ROOT / ".claude" / "projects"
    return {"label": "Claude Code (Mavis runtime + Fable 5)",
             "status": "active",
             "sessions": _count_sessions(base, "*/*.jsonl"),
             "settings_path": str(ROOT / ".claude" / "settings.json")}


def detect_hermes_live() -> dict:
    base = ROOT / ".hermes" / "sessions"
    processes = ROOT / ".hermes" / "processes.json"
    return {"label": "Hermes (Desktop + VPS)",
             "status": "active",
             "sessions": _count_sessions(base, "*.json"),
             "processes_count": _read_hermes_processes(processes)}


def detect_mavis_live() -> dict:
    base = ROOT / ".mavis" / "sessions"
    return {"label": "MiniMax Code (Mavis runtime + 22 agents)",
             "status": "active",
             "sessions": _count_sessions(base, "mvs_*/"),
             "agent_count": 22}


def _read_hermes_processes(p: Path) -> int:
    if not p.exists():
        return 0
    try:
        raw = json.loads(p.read_text(encoding="utf-8"))
        return len(raw) if isinstance(raw, list) else 0
    except (json.JSONDecodeError, OSError):
        return 0


def detect_dormants() -> dict:
    return {
        "paperclip_ai": {
            "label": "Paperclip AI",
            "status": "dormant",
            "doctrine": "DORMANT per Plan §1 + §9 Gate #6. Anti-Ultron structurel.",
            "wake_unlock": "jamais sans nouveau plan + gate Rick",
        },
        "multica": {
            "label": "Multica",
            "status": "dormant",
            "doctrine": "DORMANT per Plan §1 + §9 Gate #6.",
            "wake_unlock": "jamais sans nouveau plan + gate Rick",
        },
    }


def main() -> int:
    harnesses = {
        "claude_code": detect_claude_code_live(),
        "hermes": detect_hermes_live(),
        "mavis": detect_mavis_live(),
        **detect_dormants(),
    }
    payload = {
        "collector": "13_harnesses_live",
        "pillar": 13,
        "pillar_name": "Harnesses live (🛰️ runtime state — page contrôle sessions)",
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "source": "~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §3 page Harnesses",
        "doctrine": "lecture seule — runtime state — dormants affichés DORMANT en gris",
        "harnesses": harnesses,
        "summary": {
            "active_count": sum(1 for h in harnesses.values() if h.get("status") == "active"),
            "dormant_count": sum(1 for h in harnesses.values() if h.get("status") == "dormant"),
            "total_sessions": sum(h.get("sessions", {}).get("count", 0) for h in harnesses.values()),
        },
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[13_harnesses_live] OK → {OUTPUT} ({OUTPUT.stat().st_size} b)")
    s = payload["summary"]
    print(f"  active={s['active_count']} dormant={s['dormant_count']} total_sessions={s['total_sessions']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())