#!/usr/bin/env python3
"""Graham Embodied Holon — State/Provenance/Replay runtime adapter.

This module provides the durable Graham holon embodiment with:
- Memory namespace (SQLite WAL)
- Evidence namespace (append-only event log)
- Provenance policy enforcement
- Replay/recall tools
- Checkpoint management
- Lineage tracking

Graham is NOT the database. The runtime enters Graham's office.
The holon is not recreated inside the runtime.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sqlite3
import uuid
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

HERE = Path(__file__).resolve().parent
DB = os.environ.get("ASPACE_DB", HERE / "uc.db")
CKPT_DIR = HERE / "checkpoints"

# Graham's four-state presence model (not a single boolean)
class PresenceState:
    INSTITUTIONAL_STATE = "ACTIVE"
    EMBODIMENT_STATE = "READY"
    RUNTIME_STATE = "ONLINE"
    WORKLOAD_STATE = "IDLE"


def _connect(db_path: str | Path) -> sqlite3.Connection:
    con = sqlite3.connect(Path(db_path), timeout=10)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys=ON")
    con.execute("PRAGMA busy_timeout=5000")
    return con


def _stable_hash(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, default=str).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()[:16]


# ============================================================================
# Graham Core Capabilities
# ============================================================================

def get_holon_identity() -> Dict[str, Any]:
    """Return Graham's institutional identity (never changes)."""
    return {
        "id": "S3-Graham-State",
        "name": "Graham",
        "rank": "S3",
        "doctor": "13th",
        "jurisdiction": "Kernel Core — Memory/Provenance/State",
        "stewardship": "state_plane",
        "embodied_holon_contract": "v4-holon",
        "capability_profile": {
            "skills": [
                "recall_retriever",
                "provenance_checker",
                "replay_verifier",
                "checkpoint_manager",
            ],
            "tools": [
                "graham_holon.graham_holon",
                "graham_checkpoint.py",
            ],
            "mcp": ["supabase", "temporal_graph"],
            "deterministic_helpers": [
                "uc.db SQLite WAL",
                "event append-only log",
                "claim/fencing system",
            ],
            "forbidden_operations": [
                "create_work_from_snapshot",
                "choose_next_actions",
                "arbitrate_semantic_coherence",
            ],
        },
    }


def get_presence_state(db_path: str | Path | None = None) -> Dict[str, str]:
    """Return Graham's four-axis presence state.

    The db_path argument is accepted for interface consistency butGraham's
    presence state is determined by the holon contract, not the database state.
    """
    return {
        "institutional_state": PresenceState.INSTITUTIONAL_STATE,
        "embodiment_state": PresenceState.EMBODIMENT_STATE,
        "runtime_state": PresenceState.RUNTIME_STATE,
        "workload_state": PresenceState.WORKLOAD_STATE,
    }


def checkpoint_save(db_path: str | Path, work_id: int) -> Dict[str, Any]:
    """Create a WAL checkpoint for the given work_id."""
    os.makedirs(CKPT_DIR, exist_ok=True)
    ckpt_path = CKPT_DIR / f"uc_work{work_id}.db"

    with closing(_connect(db_path)) as con:
        # Force WAL checkpoint
        wal_status = con.execute("PRAGMA wal_checkpoint(TRUNCATE)").fetchone()

        # Backup uc.db to checkpoint
        backup_con = sqlite3.connect(ckpt_path)
        con.backup(backup_con)
        backup_con.commit()
        backup_con.close()

        # Record checkpoint event
        con.execute(
            "INSERT INTO event(work_id, harness, kind, payload) VALUES(?, ?, ?, ?)",
            (work_id, "graham_holon", "checkpoint_save", json.dumps({
                "path": str(ckpt_path),
                "wal_checkpoint": list(wal_status),
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }))
        )

    return {
        "ok": True,
        "work_id": work_id,
        "checkpoint_path": str(ckpt_path),
        "wal_busy": bool(wal_status[0]),
        "wal_pages": wal_status[1],
    }


def prove_lineage(db_path: str | Path, work_id: int,
                  before_time: Optional[str] = None,
                  after_time: Optional[str] = None) -> Dict[str, Any]:
    """Proove the lineage/continuity of events for a work item.

    This is Graham's primary function - proving where claims came from,
    not declaring them true.
    """
    with closing(_connect(db_path)) as con:
        events = con.execute(
            """SELECT id, harness, kind, payload, at
               FROM event
               WHERE work_id = ?
               ORDER BY id""",
            (work_id,)
        ).fetchall()

    events_data = []
    for e in events:
        try:
            payload = json.loads(e["payload"]) if e["payload"] else {}
        except json.JSONDecodeError:
            payload = {"_invalid_json": True, "_raw": e["payload"]}
        events_data.append({
            "id": e["id"],
            "harness": e["harness"],
            "kind": e["kind"],
            "payload": payload,
            "at": e["at"],
        })

    # Build lineage chain
    claim_events = [e for e in events_data if e["kind"] in ("dispatch_envelope", "harness_execution_receipt",
                                                              "mission_runtime_migrated", "embodiment_migration_receipt")]
    binding_events = [e for e in events_data if e["kind"] == "fleet_dispatch_attempt"]
    continuity_events = [e for e in events_data if "migration" in e["kind"].lower() or "continuation" in e["kind"].lower()]

    return {
        "ok": True,
        "work_id": work_id,
        "event_count": len(events_data),
        "claim_events": claim_events,
        "binding_events": binding_events,
        "continuity_events": continuity_events,
        "lineage_fingerprint": _stable_hash([e["id"] for e in events_data]),
        "has_migration_receipt": any("migration_receipt" in e["kind"] for e in events_data),
        "has_continuity": len(continuity_events) > 0,
    }


def reconcile_continuity(db_path: str | Path, work_id: int,
                         identity_version: str,
                         correlation_id: str,
                         return_to: Dict[str, Any],
                         authority_hash: str,
                         context_hash: str,
                         workspace_fingerprint: str,
                         evidence_head: List[str]) -> Dict[str, Any]:
    """Reconcile a continuity claim from a prior embodiment."""
    with closing(_connect(db_path)) as con:
        # Check for existing claim
        claim = con.execute(
            "SELECT harness, institutional_owner, runtime_id FROM claim WHERE work_id = ?",
            (work_id,)
        ).fetchone()

        if claim:
            return {
                "ok": False,
                "reason": "active_claim_exists",
                "current_claim": dict(claim),
            }

        # Record the reconciliation
        receipt = {
            "schema": "aspace.embodiment-migration-receipt.v1",
            "actor_id": "graham",
            "work_id": work_id,
            "correlation_id": correlation_id,
            "identity_version": identity_version,
            "authority_hash": authority_hash,
            "context_hash": context_hash,
            "workspace_fingerprint": workspace_fingerprint,
            "evidence_head": evidence_head,
            "return_to": return_to,
            "continuity_result": "PRESERVED",
            "reconciled_at": datetime.now(timezone.utc).isoformat(),
        }

        con.execute(
            """INSERT INTO event(work_id, harness, kind, payload)
               VALUES (?, ?, ?, ?)""",
            (work_id, "graham_holon", "embodiment_migration_receipt", json.dumps(receipt))
        )

        # Acquire claim for the new runtime
        new_runtime_id = f"graham-{uuid.uuid4().hex[:8]}"
        con.execute(
            """INSERT INTO claim(work_id, harness, institutional_owner, runtime_id, expires_at)
               VALUES (?, ?, ?, ?, datetime('now', '+900 seconds'))""",
            (work_id, "claude_code", "graham", new_runtime_id)
        )

    return {
        "ok": True,
        "work_id": work_id,
        "receipt": receipt,
        "new_runtime_id": new_runtime_id,
    }


# ============================================================================
# CLI Interface
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Graham Embodied Holon — State/Provenance/Replay runtime adapter"
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    # identity command
    p = sub.add_parser("identity")
    p.set_defaults(f=lambda a: print(json.dumps(get_holon_identity(), indent=2)))

    # presence command
    p = sub.add_parser("presence")
    p.add_argument("--db", default=str(DB))
    p.set_defaults(f=lambda a: print(json.dumps(get_presence_state(a.db), indent=2)))

    # checkpoint command
    p = sub.add_parser("checkpoint")
    p.add_argument("--work", type=int, required=True)
    p.add_argument("--db", default=str(DB))
    p.set_defaults(f=lambda a: print(json.dumps(checkpoint_save(a.db, a.work), indent=2)))

    # lineage command
    p = sub.add_parser("lineage")
    p.add_argument("--work", type=int, required=True)
    p.add_argument("--db", default=str(DB))
    p.add_argument("--before")
    p.add_argument("--after")
    p.set_defaults(f=lambda a: print(json.dumps(prove_lineage(a.db, a.work, a.before, a.after), indent=2)))

    # reconcile command
    p = sub.add_parser("reconcile")
    p.add_argument("--work", type=int, required=True)
    p.add_argument("--db", default=str(DB))
    p.add_argument("--identity-version", required=True)
    p.add_argument("--correlation-id", required=True)
    p.add_argument("--return-to", required=True)
    p.add_argument("--authority-hash", required=True)
    p.add_argument("--context-hash", required=True)
    p.add_argument("--workspace-fingerprint", required=True)
    p.add_argument("--evidence-head", required=True)
    p.set_defaults(f=lambda a: print(json.dumps(
        reconcile_continuity(
            a.db, a.work,
            a.identity_version, a.correlation_id,
            json.loads(a.return_to), a.authority_hash,
            a.context_hash, a.workspace_fingerprint,
            json.loads(a.evidence_head)
        ), indent=2)))

    args = parser.parse_args()
    args.f(args)


if __name__ == "__main__":
    main()