#!/usr/bin/env python3
"""
A3_DLQ.bridge.py — Symphony Lane B runtime wiring for A3 (Crew) -> Donna DLQ.

A'Space OS V2 — Sovereign Twin Runtime.
Companion spec: A3_DLQ.bridge.md (same dir).
Created 2026-06-15 by A0 mandate (Symphony Phase 2).

Usage:
    "C:/Python314/python.exe" A3_DLQ.bridge.py
    # or import as module
    from A3_DLQ_bridge import send_to_dlq
"""
from __future__ import annotations

import json
import os
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(
    os.environ.get(
        "ASPACE_BRIDGE_BASE",
        r"C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki",
    )
)
DLQ_DIR = Path(
    os.environ.get(
        "ASPACE_DLQ_DIR",
        str(BASE_DIR / "wiki" / "hand_offs" / "L0" / "A3_Donna_DLQ"),
    )
)

VALID_REASONS = {
    "canon_contradiction",   # contredit le canon du ship
    "out_of_scope_drift",    # hors-périmètre (drift)
    "incoherent_peer_finding",  # incohérent avec un autre finding du même LD/domain
    "beth_veto",             # rejeté par Beth (HALT_LD03/LD04, RED)
}


@dataclass(frozen=True)
class DLQEntry:
    """An immutable DLQ record (no hard delete — doctrine _TRASH)."""
    dlq_id: str
    a3_name: str
    reason: str
    finding: dict
    ts: str
    reviewer: str  # "Donna" | "Beth" | "A0"


def _ensure_dirs() -> None:
    DLQ_DIR.mkdir(parents=True, exist_ok=True)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _default_reviewer(reason: str) -> str:
    if reason == "beth_veto":
        return "Beth"
    return "Donna"


def _write_dlq_entry(entry: DLQEntry) -> Path:
    out = DLQ_DIR / f"{entry.dlq_id}.json"
    out.write_text(
        json.dumps(
            {
                "bridge": "A3_DLQ",
                "dlq_id": entry.dlq_id,
                "a3_name": entry.a3_name,
                "reason": entry.reason,
                "finding": entry.finding,
                "ts": entry.ts,
                "reviewer": entry.reviewer,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    return out


def send_to_dlq(a3_name: str, finding: dict, reason: str) -> str:
    """
    Send a rejected A3 finding to Donna's DLQ.

    Args:
        a3_name: name of the A3 crew that produced the rejected finding.
        finding: the rejected finding payload (dict).
        reason: one of {canon_contradiction, out_of_scope_drift, incoherent_peer_finding, beth_veto}.

    Returns:
        dlq_id: unique identifier of the DLQ entry.

    Raises:
        ValueError: if reason is not in VALID_REASONS.
    """
    _ensure_dirs()
    if reason not in VALID_REASONS:
        raise ValueError(
            f"Invalid DLQ reason: {reason!r}. Valid: {sorted(VALID_REASONS)}"
        )
    dlq_id = f"dlq_{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}_{uuid.uuid4().hex[:8]}"
    entry = DLQEntry(
        dlq_id=dlq_id,
        a3_name=a3_name,
        reason=reason,
        finding=dict(finding),
        ts=_now_iso(),
        reviewer=_default_reviewer(reason),
    )
    out = _write_dlq_entry(entry)
    print(f"[+] A3_DLQ: {a3_name} -> {dlq_id} ({reason}, reviewer={entry.reviewer})")
    return dlq_id


if __name__ == "__main__":
    sample_finding = {
        "ship": "Discovery",
        "domain": "LD02",
        "summary": "Saru flagged budget drift — rejected as out-of-scope (LD02 is finance)",
        "tags": ["drift", "out_of_scope"],
    }
    did = send_to_dlq("Saru", sample_finding, "out_of_scope_drift")
    print(f"[+] A3_DLQ.bridge.py ready — last dlq_id: {did}")
