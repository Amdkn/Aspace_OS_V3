"""
collector_01_harnesses.py — Pilier 1 (Models/Harnesses) pour Citadelle A0.

Lit l'état réel des harnesses A'Space (CC, Hermes, MC, Codex, Omnigent) + 2 dormants
(Paperclip AI, Multica). Écrit un JSON dans agent-os/citadel/data/01_harnesses.json.

Idempotent : re-run safe (overwrite le fichier destination).

DOCTRINE : lecture seule sur sources canoniques. Écriture = UNIQUEMENT
data/01_harnesses.json. Aucune mutation ailleurs.

Date : 2026-07-04 · Auteur : Mavis (MC/L1) — Plan Citadelle A0 P0
Source : ~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §2 Pilier 1
Sister : LD01/30_decisions/ADR-LD01-007_citadelle_agent_os_jarvis_pattern.md §1
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(r"C:\Users\amado")
OUTPUT = Path(r"C:\Users\amado\agent-os\citadel\data\01_harnesses.json")


def detect_cc() -> dict:
    p = ROOT / ".claude" / "settings.json"
    if not p.exists():
        return {"status": "absent", "path": str(p)}
    try:
        sz = p.stat().st_size
        return {"status": "active", "path": str(p), "size_bytes": sz, "model_hint": "opus-equivalent via Fable 5 quota"}
    except OSError as e:
        return {"status": "error", "path": str(p), "error": str(e)}


def detect_hermes() -> dict:
    p = ROOT / ".hermes"
    if not p.exists():
        return {"status": "absent", "path": str(p)}
    cfg = p / "config.yaml"
    processes = p / "processes.json"
    auth = p / "auth.json"
    return {
        "status": "active",
        "path": str(p),
        "has_config": cfg.exists(),
        "has_processes": processes.exists(),
        "has_auth": auth.exists(),
        "note": "Desktop + VPS dual presence",
    }


def detect_mc() -> dict:
    p = ROOT / ".mavis"
    if not p.exists():
        return {"status": "absent", "path": str(p)}
    cfg = p / "config.yaml"
    agents_dir = p / "agents"
    return {
        "status": "active",
        "path": str(p),
        "model": "MiniMax-M3 (default per config.yaml)",
        "agent_count": len([d for d in agents_dir.iterdir() if d.is_dir()]) if agents_dir.exists() else 0,
        "has_nexus": (p / "nexus.db").exists(),
        "note": "MC = L1 per plan-L2 §13 permutation",
    }


def detect_codex() -> dict:
    p = ROOT / ".codex"
    if not p.exists():
        return {"status": "absent", "path": str(p), "note": "GPT banni in A'Space — Codex = M3-only"}
    return {"status": "active", "path": str(p)}


def detect_omnigent() -> dict:
    p = ROOT / "shadow-l0-omnigent"  # placeholder path (verifier with reality)
    candidates = [ROOT / "shadow-l0-omnigent", ROOT / ".omnigent", ROOT / "shadow-omnigent"]
    found = next((c for c in candidates if c.exists()), None)
    if found:
        return {"status": "active", "path": str(found), "note": "shadow-l0, E1 in-loop"}
    return {"status": "absent", "path": "n/a", "note": "shadow harness, E1 in-loop per Plan Citadelle §1"}


def detect_paperclip() -> dict:
    """Paperclip AI = dormant anti-pattern. MUST stay absent."""
    candidates = [ROOT / ".paperclip", ROOT / "paperclip", ROOT / ".paperclip-ai"]
    found = next((c for c in candidates if c.exists()), None)
    return {
        "status": "dormant",
        "path": str(found) if found else "n/a",
        "note": "DORMANT per Plan Citadelle §1 + §9 Gate #6. Anti-Ultron structurel.",
        "doctrine": "Le fait que 'Paperclip AI' soit littéralement le nom d'un harness dormant n'est pas une coïncidence : il reste dormant.",
    }


def detect_multica() -> dict:
    """Multica = dormant anti-pattern. MUST stay absent."""
    candidates = [ROOT / ".multica", ROOT / "multica"]
    found = next((c for c in candidates if c.exists()), None)
    return {
        "status": "dormant",
        "path": str(found) if found else "n/a",
        "note": "DORMANT per Plan Citadelle §1 + §9 Gate #6.",
    }


def main() -> int:
    harnesses = {
        "claude_code": detect_cc(),
        "hermes": detect_hermes(),
        "minimax_code": detect_mc(),
        "codex": detect_codex(),
        "omnigent": detect_omnigent(),
        "paperclip_ai": detect_paperclip(),
        "multica": detect_multica(),
    }
    payload = {
        "collector": "01_harnesses",
        "pillar": 1,
        "pillar_name": "Models / Harnesses",
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "source": "~/.claude/plans/plan-a0-dashboard-citadel-agent-os.md §2",
        "doctrine": "lecture seule — anti-Ultron — dormants affichés dormants",
        "harnesses": harnesses,
        "summary": {
            "active_count": sum(1 for h in harnesses.values() if h.get("status") == "active"),
            "absent_count": sum(1 for h in harnesses.values() if h.get("status") == "absent"),
            "dormant_count": sum(1 for h in harnesses.values() if h.get("status") == "dormant"),
            "dormants_displayed_grey": True,
        },
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[01_harnesses] OK → {OUTPUT} ({OUTPUT.stat().st_size} b)")
    print(f"  active={payload['summary']['active_count']} absent={payload['summary']['absent_count']} dormant={payload['summary']['dormant_count']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())