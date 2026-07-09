#!/usr/bin/env python3
"""
L0_to_L1.bridge.py — Symphony Lane B runtime wiring for Shadow L0 (IA) -> L1 Life OS.

A'Space OS V2 — Sovereign Twin Runtime.
Companion spec: L0_to_L1.bridge.md (same dir).
Created 2026-06-15 by A0 mandate (Symphony Phase 2).

Usage:
    "C:/Python314/python.exe" L0_to_L1.bridge.py
    # or import as module
    from L0_to_L1_bridge import handoff_l0_to_l1
"""
from __future__ import annotations

import json
import os
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal

BASE_DIR = Path(
    os.environ.get(
        "ASPACE_BRIDGE_BASE",
        r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki",
    )
)
SHADOW_L0_DIR = Path(
    os.environ.get(
        "ASPACE_SHADOW_L0_DIR",
        r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony_antigravity",
    )
)
A0_INBOX_DIR = Path(
    os.environ.get(
        "ASPACE_A0_INBOX_DIR",
        str(BASE_DIR / "wiki" / "hand_offs" / "Shadow_L0" / "A0_inbox"),
    )
)
A2_INTAKE_DIR = Path(
    os.environ.get(
        "ASPACE_A2_INTAKE_DIR",
        str(BASE_DIR / "wiki" / "hand_offs" / "A2_Intake"),
    )
)

# Shadow L0 sources (Codex, Claude Code, Gemini CLI, Antigravity)
ShadowL0Source = Literal["codex", "claude_code", "gemini_cli", "antigravity", "other"]


@dataclass(frozen=True)
class A2Intake:
    """A2 intake packet — what an A2 ship receives after Beth GREEN-clearance."""
    intake_id: str
    artifact: dict
    source: str
    detected_framework: str
    proposed_ship: str
    ts: str
    status: str  # "pending_beth_clearance" — Beth must validate before A3 execution


# Local framework detection — mirrors A1_to_A2.bridge.py's SHIPS table
_SHIP_KEYWORDS: dict[str, tuple[str, ...]] = {
    "Orville": ("purpose", "ikigai", "pillars", "horizons"),
    "Discovery": ("wheel", "ld01", "ld02", "ld03", "ld04", "ld05", "ld06", "ld07", "ld08", "balance", "drift"),
    "Curie_SNW": ("12wy", "sprint", "scorecard", "weekly"),
    "Computer_Enterprise": ("para", "project", "area", "resource", "archive"),
    "HoloDeck_Cerritos": ("gtd", "inbox", "next action", "context", "capture"),
    "HoloJaneway_Protostar": ("deal", "automate", "eliminate", "4h", "liberate", "define"),
}


def _detect_ship(artifact: dict) -> tuple[str, str]:
    """Return (proposed_ship, detected_framework) from artifact body."""
    text = " ".join(
        [
            str(artifact.get("framework", "")),
            str(artifact.get("summary", "")),
            str(artifact.get("type", "")),
            " ".join(artifact.get("tags") or []),
        ]
    ).lower()
    best: tuple[int, str, str] = (0, "Computer_Enterprise", "PARA")
    for ship, keywords in _SHIP_KEYWORDS.items():
        hits = sum(1 for kw in keywords if kw in text)
        if hits > best[0]:
            best = (hits, ship, _framework_of(ship))
    return best[1], best[2]


def _framework_of(ship: str) -> str:
    return {
        "Orville": "Ikigai",
        "Discovery": "Life Wheel",
        "Curie_SNW": "12-Week Year",
        "Computer_Enterprise": "PARA",
        "HoloDeck_Cerritos": "GTD",
        "HoloJaneway_Protostar": "D.E.A.L",
    }.get(ship, "PARA")


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _ensure_dirs() -> None:
    A0_INBOX_DIR.mkdir(parents=True, exist_ok=True)
    A2_INTAKE_DIR.mkdir(parents=True, exist_ok=True)


def _drop_to_a0_inbox(l0_artifact: dict, intake_id: str) -> Path:
    """Step 1: drop into Shadow_L0/A0_inbox/ for Beth to triage."""
    out = A0_INBOX_DIR / f"{intake_id}.json"
    out.write_text(
        json.dumps(
            {
                "ts": _now_iso(),
                "status": "awaiting_beth_triage",
                "source": l0_artifact.get("source", "unknown"),
                "raw": l0_artifact,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    return out


def _write_a2_intake(intake: A2Intake) -> Path:
    out = A2_INTAKE_DIR / f"{intake.intake_id}.json"
    out.write_text(
        json.dumps(
            {
                "intake_id": intake.intake_id,
                "source": intake.source,
                "detected_framework": intake.detected_framework,
                "proposed_ship": intake.proposed_ship,
                "status": intake.status,
                "ts": intake.ts,
                "artifact": intake.artifact,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    return out


def handoff_l0_to_l1(l0_artifact: dict) -> dict:
    """
    Handoff a Shadow L0 mission_result to the L1 Life OS via the canonical 2-step flow:
      1) drop into A0 inbox (Shadow_L0/A0_inbox/) — Beth must triage
      2) build A2 intake packet (pending_beth_clearance) — Morty then routes to A2 ship

    Anti-patterns guarded:
      - No L0 -> A3 direct (A2_intake.status = pending_beth_clearance)
      - No auto-clearance (Beth must validate)
      - No drop into Hermes Agent (Hermes = closed folder, no writes)

    Args:
        l0_artifact: dict with at least {source, summary, framework?}.

    Returns:
        a2_intake: dict with intake_id, proposed_ship, status, ts.
    """
    _ensure_dirs()
    intake_id = f"l0intake_{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}_{uuid.uuid4().hex[:8]}"
    source = str(l0_artifact.get("source", "other"))
    proposed_ship, detected_framework = _detect_ship(l0_artifact)
    intake = A2Intake(
        intake_id=intake_id,
        artifact=dict(l0_artifact),
        source=source,
        detected_framework=detected_framework,
        proposed_ship=proposed_ship,
        ts=_now_iso(),
        status="pending_beth_clearance",
    )
    inbox_path = _drop_to_a0_inbox(l0_artifact, intake_id)
    intake_path = _write_a2_intake(intake)
    print(
        f"[+] L0_to_L1: {source} -> {proposed_ship} (intake {intake_id}, "
        f"inbox: {inbox_path.name}, intake: {intake_path.name})"
    )
    return {
        "intake_id": intake_id,
        "proposed_ship": proposed_ship,
        "detected_framework": detected_framework,
        "status": intake.status,
        "ts": intake.ts,
    }


if __name__ == "__main__":
    artifact = {
        "source": "antigravity",
        "summary": "GTD inbox review — 14 new items",
        "framework": "GTD",
        "tags": ["gtd", "inbox"],
        "shadow_l0_dir": str(SHADOW_L0_DIR),
    }
    result = handoff_l0_to_l1(artifact)
    print(f"[+] L0_to_L1.bridge.py ready — last intake: {result['intake_id']}")
