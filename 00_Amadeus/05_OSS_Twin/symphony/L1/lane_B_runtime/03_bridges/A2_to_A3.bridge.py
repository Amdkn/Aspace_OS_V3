#!/usr/bin/env python3
"""
A2_to_A3.bridge.py — Symphony Lane B runtime wiring for A2 (Ships) -> A3 (Crews).

A'Space OS V2 — Sovereign Twin Runtime.
Companion spec: A2_to_A3.bridge.md (same dir).
Created 2026-06-15 by A0 mandate (Symphony Phase 2).

Usage:
    "C:/Python314/python.exe" A2_to_A3.bridge.py
    # or import as module
    from A2_to_A3_bridge import delegate_to_crew
"""
from __future__ import annotations

import json
import os
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
CREW_DELEGATION_DIR = Path(
    os.environ.get(
        "ASPACE_CREW_DELEGATION_DIR",
        str(BASE_DIR / "wiki" / "hand_offs" / "Crew_Delegation_Log"),
    )
)

Domain = Literal["LD01", "LD02", "LD03", "LD04", "LD05", "LD06", "LD07", "LD08"]


@dataclass(frozen=True)
class A3Crew:
    """An A3 crew member — domain-scoped, ship-bound (no cross-ship)."""
    name: str
    ship: str
    domain: str  # LD0x or framework role
    role: str


# 35 A3 crews across 6 ships (per A2_to_A3.bridge.md canon).
# Anti-patterns guarded:
#   - A3 promoted to A2 (role is frozen, see ROUTING_MATRIX below)
#   - A3 cross-ship (each crew stays in its ship)
#   - A3 silent escalation to Beth (must escalate to A2)
#   - Picard/Freeman-as-A2 (those are A3 crew names, NOT the A2)
#   - HoloJaneway typo (correct: "Holo Janeway" with space)
ROUTING_MATRIX: dict[str, dict[str, str]] = {
    # Orville: Pilars (4) + Horizons (5) — Ikigai scope
    "Orville": {
        "pilar_ed": "Ed", "pilar_kelly": "Kelly", "pilar_gordon": "Gordon", "pilar_claire": "Claire",
        "horizon_isaac": "Isaac", "horizon_john": "John", "horizon_bortus": "Bortus",
        "horizon_alara": "Alara", "horizon_klyden": "Klyden",
    },
    # Discovery: 8 LDs (one crew per LD, with LD03/LD04 ⚠️ critical)
    "Discovery": {
        "LD01": "Book", "LD02": "Saru",
        "LD03": "Culber",  # health, critical
        "LD04": "Tilly",   # cognition, critical
        "LD05": "Stamets", "LD06": "Burnham", "LD07": "Reno", "LD08": "Georgiou",
    },
    # Curie SNW: 5 crews (12WY cadence)
    "Curie_SNW": {
        "captain": "Pike", "xo": "Una", "medical": "M'Benga", "chief": "Chapel", "conn": "Ortegas",
    },
    # Computer Enterprise: 4 crews (PARA canonisation)
    # Picard = A3 crew of Computer Enterprise, NOT the A2 (A2 = LCARS Computer)
    "Computer_Enterprise": {
        "captain": "Picard", "first_officer": "Spock", "engineer": "Geordi", "ops": "Data",
    },
    # HoloDeck Cerritos: 5 crews (GTD lifecycle)
    # Freeman = A3 crew of Holo Deck Cerritos, NOT the A2 (A2 = Holo Deck Cerritos ship intelligence)
    "HoloDeck_Cerritos": {
        "inbox_mariner": "Mariner", "clarify_boimler": "Boimler",
        "organize_rutherford": "Rutherford", "review_tendi": "Tendi", "engage_freeman": "Freeman",
    },
    # HoloJaneway Protostar: 4 crews (DEAL pipeline)
    # Correct: "Holo Janeway" with space. Holo Janeway = ship intelligence (A2), not captain.
    "HoloJaneway_Protostar": {
        "define_dal": "Dal", "eliminate_rok_tahk": "Rok-Tahk",
        "automate_zero": "Zero", "liberate_gwyn": "Gwyn",
    },
}

# Discovery LD-criticality flag
DISCOVERY_CRITICAL = {"LD03", "LD04"}


def _ensure_dirs() -> None:
    CREW_DELEGATION_DIR.mkdir(parents=True, exist_ok=True)


def _resolve_discovery(ship: str, domain: str) -> str:
    if ship == "Discovery":
        ld = domain if domain in ROUTING_MATRIX["Discovery"] else f"LD0{domain[-1]}" if domain.startswith("LD") else "LD01"
        return ROUTING_MATRIX["Discovery"].get(ld, "Book")
    return ""


def _resolve_other_ship(ship: str, domain: str) -> str:
    table = ROUTING_MATRIX.get(ship, {})
    # Try direct key
    if domain in table:
        return table[domain]
    # Try lowercase
    if domain.lower() in table:
        return table[domain.lower()]
    # Try first match
    if table:
        return next(iter(table.values()))
    return "Unknown"


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _write_delegation_log(ship: str, domain: str, a3: str, mission: dict) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = CREW_DELEGATION_DIR / f"{stamp}_{ship}_{domain}_{a3}.json"
    doc = {
        "bridge": "A2_to_A3",
        "ts": _now_iso(),
        "ship": ship,
        "domain": domain,
        "a3_name": a3,
        "critical": ship == "Discovery" and domain in DISCOVERY_CRITICAL,
        "mission": mission,
    }
    out.write_text(json.dumps(doc, indent=2, ensure_ascii=False), encoding="utf-8")
    return out


def delegate_to_crew(ship: str, domain: str) -> str:
    """
    Delegate a domain-scoped mission from an A2 ship to a specific A3 crew.

    Args:
        ship: A2 ship intelligence name (e.g. "Discovery", "HoloJaneway_Protostar").
        domain: For Discovery: LD01..LD08. For others: a routing key (captain, xo, etc.)
                or a domain token matching a table key.

    Returns:
        a3_name: name of the A3 crew member assigned.

    Raises:
        ValueError: if ship is not in ROUTING_MATRIX.
    """
    _ensure_dirs()
    if ship not in ROUTING_MATRIX:
        raise ValueError(f"Unknown A2 ship: {ship!r}. Known: {sorted(ROUTING_MATRIX)}")
    if ship == "Discovery":
        a3 = _resolve_discovery(ship, domain)
    else:
        a3 = _resolve_other_ship(ship, domain)
    log_path = _write_delegation_log(
        ship=ship,
        domain=domain,
        a3=a3,
        mission={"summary": f"Delegated to {a3} on {ship}/{domain}"},
    )
    warn = " [CRITICAL]" if ship == "Discovery" and domain in DISCOVERY_CRITICAL else ""
    print(f"[+] A2_to_A3: {ship} + {domain} -> {a3}{warn} (log: {log_path.name})")
    return a3


if __name__ == "__main__":
    print("[+] A2_to_A3.bridge.py ready — sample delegations:")
    print("    Discovery + LD02 ->", delegate_to_crew("Discovery", "LD02"))
    print("    HoloJaneway_Protostar + automate_zero ->", delegate_to_crew("HoloJaneway_Protostar", "automate_zero"))
    print("    Computer_Enterprise + captain ->", delegate_to_crew("Computer_Enterprise", "captain"))
