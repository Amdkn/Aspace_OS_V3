#!/usr/bin/env python3
"""
A1_to_A2.bridge.py — Symphony Lane B runtime wiring for A1 (Beth/Morty) -> A2 (Ships).

A'Space OS V2 — Sovereign Twin Runtime.
Companion spec: A1_to_A2.bridge.md (same dir).
Created 2026-06-15 by A0 mandate (Symphony Phase 2).

Usage:
    "C:/Python314/python.exe" A1_to_A2.bridge.py
    # or import as module
    from A1_to_A2_bridge import route_to_ship
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(
    os.environ.get(
        "ASPACE_BRIDGE_BASE",
        r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki",
    )
)
MORTY_QUEUE_DIR = Path(
    os.environ.get(
        "ASPACE_MORTY_QUEUE_DIR",
        str(BASE_DIR / "wiki" / "hand_offs" / "Morty_Global_Queue"),
    )
)


@dataclass(frozen=True)
class ShipIntelligence:
    """An A2 ship intelligence (NOT a ship captain — A2 = intelligence layer)."""
    name: str
    framework: str
    trigger_keywords: tuple[str, ...]
    description: str


# 6 A2 ship intelligences (one per dominant framework)
# Anti-patterns guarded:
#   - Picard-as-A2 (Picard = A3 crew of Computer Enterprise, NOT the A2)
#   - Freeman-as-A2 (Freeman = A3 crew of HoloDeck Cerritos, NOT the A2)
#   - Sia-as-Discovery (Sia = not canon, A2 Discovery = ZORA)
#   - "Ship Captain" framing (A2 = the ship's intelligence, not its captain)
#   - HoloJaneway hyphen (correct: Holo Janeway with space)
#   - "Holo Deck" as captain (Holo Deck = simulation room, not intelligence)
SHIPS: dict[str, ShipIntelligence] = {
    "Orville": ShipIntelligence(
        name="Orville",
        framework="Ikigai",
        trigger_keywords=("purpose", "ikigai", "pillars", "horizons"),
        description="Orville ship intelligence — Ikigai planning (sense, Pilars, Horizons H1/H3/H10/H30/H90).",
    ),
    "Discovery": ShipIntelligence(
        name="Discovery",
        framework="Life Wheel",
        trigger_keywords=("wheel", "ld01", "ld02", "ld03", "ld04", "ld05", "ld06", "ld07", "ld08", "balance", "drift"),
        description="Discovery ship intelligence ZORA — 8 Life Domains balance scan.",
    ),
    "Curie_SNW": ShipIntelligence(
        name="Curie_SNW",
        framework="12-Week Year",
        trigger_keywords=("12wy", "sprint", "scorecard", "weekly", "12-week"),
        description="Curie SNW ship intelligence — 12-Week Year cadence + scorecard.",
    ),
    "Computer_Enterprise": ShipIntelligence(
        name="Computer_Enterprise",
        framework="PARA",
        trigger_keywords=("para", "project", "area", "resource", "archive"),
        description="LCARS Computer Enterprise — PARA canonisation, Projects/Areas/Resources/Archives.",
    ),
    "HoloDeck_Cerritos": ShipIntelligence(
        name="HoloDeck_Cerritos",
        framework="GTD",
        trigger_keywords=("gtd", "inbox", "next action", "context", "capture", "clarify", "organize", "review", "engage"),
        description="Holo Deck Cerritos ship intelligence — GTD capture/clarify/organize/review/engage.",
    ),
    "HoloJaneway_Protostar": ShipIntelligence(
        name="HoloJaneway_Protostar",
        framework="D.E.A.L",
        trigger_keywords=("deal", "automate", "eliminate", "4h", "liberate", "define"),
        description="Holo Janeway Protostar ship intelligence — DEAL Define/Eliminate/Automate/Liberate, 4h Work Week audit.",
    ),
}


def _detect_framework(context_pack: dict) -> str:
    """Detect dominant framework from context_pack['framework'] or trigger keywords."""
    if context_pack.get("framework"):
        f = str(context_pack["framework"]).lower()
        for ship in SHIPS.values():
            if ship.framework.lower().replace("-", "").replace(".", "") == f.replace("-", "").replace(".", ""):
                return ship.name
    text = " ".join(
        [
            str(context_pack.get("summary", "")),
            str(context_pack.get("framework", "")),
            " ".join(context_pack.get("tags") or []),
        ]
    ).lower()
    best: tuple[int, str] = (0, "Computer_Enterprise")
    for ship in SHIPS.values():
        hits = sum(1 for kw in ship.trigger_keywords if kw in text)
        if hits > best[0]:
            best = (hits, ship.name)
    return best[1]


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _ensure_dirs() -> None:
    MORTY_QUEUE_DIR.mkdir(parents=True, exist_ok=True)


def _write_morty_queue(context_pack: dict, ship: ShipIntelligence, beth_clearance: str) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = MORTY_QUEUE_DIR / f"{stamp}_to_{ship.name}.json"
    doc = {
        "bridge": "A1_to_A2",
        "ts": _now_iso(),
        "context_pack": context_pack,
        "beth_clearance": beth_clearance,
        "ship_intelligence": ship.name,
        "framework": ship.framework,
    }
    out.write_text(json.dumps(doc, indent=2, ensure_ascii=False), encoding="utf-8")
    return out


def route_to_ship(framework: str, beth_clearance: str) -> str:
    """
    Route a Beth/Morty context pack to the appropriate A2 ship intelligence.

    Args:
        framework: dominant framework name OR raw context_pack dict (overload accepted).
        beth_clearance: Beth's clearance state from A0_to_A1 bridge.

    Returns:
        ship_intelligence: name of the A2 ship intelligence.
    """
    _ensure_dirs()
    # Accept either a framework string or a full context_pack dict.
    if isinstance(framework, dict):
        context_pack = framework
        framework_hint = context_pack.get("framework")
    else:
        context_pack = {"framework": framework}
        framework_hint = framework

    ship_name = _detect_framework(context_pack)
    ship = SHIPS[ship_name]
    log_path = _write_morty_queue(
        context_pack={"framework": framework_hint, "raw": context_pack},
        ship=ship,
        beth_clearance=beth_clearance,
    )
    print(f"[+] A1_to_A2: {beth_clearance} -> {ship.name} ({ship.framework}) log: {log_path.name}")
    return ship.name


if __name__ == "__main__":
    cp = {"framework": "12-Week Year", "summary": "Sprint W24 scorecard", "tags": ["sprint", "scorecard"]}
    result = route_to_ship(cp, "GREEN")
    print(f"[+] A1_to_A2.bridge.py ready — last ship: {result}")
