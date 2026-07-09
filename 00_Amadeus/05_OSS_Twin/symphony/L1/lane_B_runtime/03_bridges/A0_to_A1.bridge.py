#!/usr/bin/env python3
"""
A0_to_A1.bridge.py — Symphony Lane B runtime wiring for A0 (Amadeus) -> A1 (Beth/Morty).

A'Space OS V2 — Sovereign Twin Runtime.
Companion spec: A0_to_A1.bridge.md (same dir).
Created 2026-06-15 by A0 mandate (Symphony Phase 2).

Usage:
    "C:/Python314/python.exe" A0_to_A1.bridge.py
    # or import as module
    from A0_to_A1_bridge import emit_intent
"""
from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal

# Canon paths (env-overridable for portability)
BASE_DIR = Path(
    os.environ.get(
        "ASPACE_BRIDGE_BASE",
        r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki",
    )
)
BETH_LOG_DIR = Path(
    os.environ.get(
        "ASPACE_BETH_LOG_DIR",
        str(BASE_DIR / "wiki" / "hand_offs" / "Beth_Alignment_Log"),
    )
)
SUNDAY_UPLINK_DIR = Path(
    os.environ.get(
        "ASPACE_SUNDAY_UPLINK_DIR",
        str(BASE_DIR / "wiki" / "hand_offs" / "Sunday_Uplink_Protocols"),
    )
)

# Triage states (A1 Beth conscience — 5 états)
ClearanceState = Literal["GREEN", "ORANGE", "RED", "HALT_LD03", "HALT_LD04"]


@dataclass(frozen=True)
class Intent:
    """A0 Amadeus Intent — immutable DTO (PEP 8, frozen dataclass)."""
    intent_id: str
    channel: str  # "sunday_uplink" | "adhoc_mission" | "crisis_escalation"
    summary: str
    source: str  # e.g. "A0 Amadeus"
    created_at: str
    payload: dict


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _ensure_dirs() -> None:
    BETH_LOG_DIR.mkdir(parents=True, exist_ok=True)
    SUNDAY_UPLINK_DIR.mkdir(parents=True, exist_ok=True)


def _beth_triage(intent: Intent) -> ClearanceState:
    """
    Beth's conscience-level triage (5 états canon).
    Heuristics on intent.channel + payload (deterministic, no ML).
    """
    if intent.channel == "crisis_escalation":
        if "LD03" in intent.summary or "health" in intent.payload.get("tags", []):
            return "HALT_LD03"
        if "LD04" in intent.summary or "cognition" in intent.payload.get("tags", []):
            return "HALT_LD04"
        return "RED"
    if intent.channel == "sunday_uplink":
        return "GREEN"
    # adhoc_mission
    risk = intent.payload.get("risk", "low")
    if risk == "high":
        return "ORANGE"
    return "GREEN"


def _write_alignment_log(intent: Intent, clearance: ClearanceState) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = BETH_LOG_DIR / f"{stamp}_{intent.intent_id}_{clearance}.json"
    doc = {
        "bridge": "A0_to_A1",
        "ts": _now_iso(),
        "intent": asdict(intent),
        "beth_clearance": clearance,
    }
    out.write_text(json.dumps(doc, indent=2, ensure_ascii=False), encoding="utf-8")
    return out


def emit_intent(intent: dict) -> str:
    """
    Emit an A0 Intent to A1 Beth/Morty. Returns Beth's clearance string.

    Args:
        intent: dict matching Intent fields (intent_id, channel, summary, source, payload).

    Returns:
        beth_clearance: one of "GREEN" | "ORANGE" | "RED" | "HALT_LD03" | "HALT_LD04".

    Side effects:
        Writes alignment log to BETH_LOG_DIR.
    """
    _ensure_dirs()
    dto = Intent(
        intent_id=intent.get("intent_id") or f"intent_{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}",
        channel=intent.get("channel", "adhoc_mission"),
        summary=intent.get("summary", ""),
        source=intent.get("source", "A0 Amadeus"),
        created_at=_now_iso(),
        payload=dict(intent.get("payload") or {}),
    )
    clearance = _beth_triage(dto)
    log_path = _write_alignment_log(dto, clearance)
    print(f"[+] A0_to_A1: {dto.intent_id} -> {clearance} (log: {log_path.name})")
    return clearance


if __name__ == "__main__":
    sample = {
        "intent_id": "demo_sunday_uplink",
        "channel": "sunday_uplink",
        "summary": "Weekly state of 6 ships and 8 LDs",
        "source": "A0 Amadeus",
        "payload": {"week": "2026-W24", "ships": 6, "ld": 8},
    }
    result = emit_intent(sample)
    print(f"[+] A0_to_A1.bridge.py ready — last clearance: {result}")
