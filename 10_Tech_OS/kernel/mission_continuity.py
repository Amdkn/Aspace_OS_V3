#!/usr/bin/env python3
"""Durable MissionCell projection over the existing WorkGraph.

This module does not create a second scheduler or persistence model.
It reconstructs continuation truth from canonical uc.db surfaces:
work, claim, session_binding and append-only event.
"""
from __future__ import annotations

import json
import sqlite3
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

CONTINUITY_KINDS = (
    "dispatch_envelope",
    "harness_execution_requested",
    "harness_execution_receipt",
    "rory_reconcile_decision",
    "continuation_routed",
    "continuation_resolved",
    "fleet_dispatch_attempt",
    "fleet_dispatch_resolved",
    "dispatch_backpressure",
    "worker_transition_observed",
    "manager_wake_requested",
    "manager_wake_resolved",
)

ROUTE_TERMINAL = {"DONE"}
ROUTE_WAIT = {"WAIT"}
ROUTE_RETRY = {"RETRY"}


class MissionContinuityError(RuntimeError):
    pass


def _connect(db_path: str | Path) -> sqlite3.Connection:
    con = sqlite3.connect(Path(db_path), timeout=10)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys=ON")
    return con


def _payload(raw: str | None) -> dict[str, Any]:
    if not raw:
        return {}
    try:
        value = json.loads(raw)
    except json.JSONDecodeError:
        return {"_invalid_json": True, "_raw": raw}
    return value if isinstance(value, dict) else {"value": value}


def _parse_time(value: str | None) -> datetime | None:
    if not value:
        return None
    text = value.strip().replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _claim_is_live(expires_at: str | None, now: datetime) -> bool:
    expiry = _parse_time(expires_at)
    return bool(expiry and expiry > now)


def _event_dict(row: sqlite3.Row | None) -> dict[str, Any] | None:
    if not row:
        return None
    return {
        "id": row["id"],
        "kind": row["kind"],
        "harness": row["harness"],
        "at": row["at"],
        "payload": _payload(row["payload"]),
    }


def _latest(rows: list[sqlite3.Row], kind: str) -> dict[str, Any] | None:
    for row in reversed(rows):
        if row["kind"] == kind:
            return _event_dict(row)
    return None


def _latest_continuity_identity(events: list[dict[str, Any] | None]) -> tuple[str | None, dict[str, Any] | None]:
    candidates = [
        event for event in events
        if event and event["payload"].get("correlation_id")
    ]
    if not candidates:
        return None, None
    event = max(candidates, key=lambda item: int(item["id"]))
    payload = event["payload"]
    return str(payload["correlation_id"]), payload.get("return_route")


def _derive_next_action(
    work_status: str,
    claim_live: bool,
    binding: dict[str, Any] | None,
    dispatch: dict[str, Any] | None,
    receipt: dict[str, Any] | None,
    reconcile: dict[str, Any] | None,
    continuation: dict[str, Any] | None,
    backpressure: dict[str, Any] | None,
) -> dict[str, Any]:
    if work_status == "done":
        return {"action": "TERMINAL", "reason": "work_done"}

    continuation_id = continuation["id"] if continuation else -1
    reconcile_id = reconcile["id"] if reconcile else -1
    receipt_id = receipt["id"] if receipt else -1
    dispatch_id = dispatch["id"] if dispatch else -1
    backpressure_id = backpressure["id"] if backpressure else -1

    if continuation and continuation_id >= reconcile_id and continuation_id >= receipt_id:
        payload = continuation["payload"]
        route_class = payload.get("route_class")
        target = payload.get("target_capability")

        if route_class in ROUTE_TERMINAL:
            return {"action": "TERMINAL", "route_class": route_class, "target_capability": target}
        if route_class in ROUTE_WAIT:
            return {"action": "WAIT", "route_class": route_class, "target_capability": target}
        if route_class in ROUTE_RETRY:
            return {"action": "DISPATCH_RETRY", "route_class": route_class, "target_capability": target}
        return {"action": "ROUTE_CONTINUATION", "route_class": route_class, "target_capability": target}

    if reconcile and reconcile_id > continuation_id and reconcile_id >= receipt_id:
        return {
            "action": "ROUTE_RECONCILE_DECISION",
            "verdict": reconcile["payload"].get("verdict"),
            "reopen_cell": reconcile["payload"].get("reopen_cell"),
        }

    if receipt and receipt_id > reconcile_id:
        return {
            "action": "RECONCILE_RECEIPT",
            "effect_state": receipt["payload"].get("effect_state"),
            "retry_safe": receipt["payload"].get("retry_safe"),
        }

    if (
        backpressure
        and backpressure_id > dispatch_id
        and backpressure_id > continuation_id
        and backpressure_id > reconcile_id
        and backpressure_id > receipt_id
        and not claim_live
    ):
        payload = backpressure["payload"]
        return {
            "action": "BACKPRESSURE",
            "reason": payload.get("reason"),
            "required_capability": payload.get("required_capability"),
            "not_before": payload.get("not_before"),
        }

    if claim_live and binding:
        return {
            "action": "OBSERVE_BOUND_WORKER",
            "session_key": binding.get("session_key"),
            "harness": binding.get("harness"),
        }

    if binding and not claim_live:
        return {
            "action": "RECONCILE_BINDING",
            "session_key": binding.get("session_key"),
            "harness": binding.get("harness"),
            "reason": "binding_without_live_claim",
        }

    if claim_live and not binding:
        return {
            "action": "WAIT_BINDING",
            "reason": "live_claim_without_session_binding",
        }

    if work_status == "claimed" and not claim_live:
        return {
            "action": "RECONCILE_CLAIM",
            "reason": "claimed_work_without_live_claim",
        }

    if work_status in {"waiting", "blocked"}:
        return {"action": "WAIT", "reason": f"work_{work_status}"}

    if work_status == "failed":
        return {"action": "RECOVER_OR_RECONCILE", "reason": "work_failed"}

    return {"action": "DISPATCH_READY", "reason": "no_live_owner_or_terminal_continuation"}


def project_mission_cell(
    db_path: str | Path,
    work_id: int,
    *,
    now: datetime | None = None,
) -> dict[str, Any]:
    """Reconstruct the current continuation state for one canonical work cell."""
    current_time = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)

    with closing(_connect(db_path)) as con:
        work = con.execute(
            "SELECT id,title,layer,status,parent_id,attempts,created_at,updated_at FROM work WHERE id=?",
            (work_id,),
        ).fetchone()
        if not work:
            raise MissionContinuityError(f"work_id does not exist: {work_id}")

        claim = con.execute(
            "SELECT work_id,harness,claimed_at,expires_at FROM claim WHERE work_id=?",
            (work_id,),
        ).fetchone()

        bindings = con.execute(
            """SELECT id,work_id,session_key,harness,capability,external_ref,status,started_at,ended_at
               FROM session_binding
               WHERE work_id=?
               ORDER BY id""",
            (work_id,),
        ).fetchall()
        active_bindings = [
            dict(row) for row in bindings
            if row["status"] in ("active", "idle") and not row["ended_at"]
        ]
        binding = active_bindings[-1] if active_bindings else None

        marks = ",".join("?" for _ in CONTINUITY_KINDS)
        rows = con.execute(
            f"""SELECT id,work_id,harness,kind,payload,at
                FROM event
                WHERE work_id=? AND kind IN ({marks})
                ORDER BY id""",
            (work_id, *CONTINUITY_KINDS),
        ).fetchall()

    claim_dict = dict(claim) if claim else None
    claim_live = bool(claim_dict and _claim_is_live(claim_dict.get("expires_at"), current_time))

    dispatch = _latest(rows, "dispatch_envelope")
    request = _latest(rows, "harness_execution_requested")
    receipt = _latest(rows, "harness_execution_receipt")
    reconcile = _latest(rows, "rory_reconcile_decision")
    continuation = _latest(rows, "continuation_routed")
    resolved = _latest(rows, "continuation_resolved")
    backpressure = _latest(rows, "dispatch_backpressure")
    worker_transition = _latest(rows, "worker_transition_observed")
    manager_wake_request = _latest(rows, "manager_wake_requested")
    manager_wake_resolution = _latest(rows, "manager_wake_resolved")

    correlation_id, return_route = _latest_continuity_identity(
        [backpressure, continuation, reconcile, receipt, request, dispatch]
    )

    next_action = _derive_next_action(
        work["status"],
        claim_live,
        binding,
        dispatch,
        receipt,
        reconcile,
        continuation,
        backpressure,
    )

    return {
        "schema": "aspace.mission-cell-projection.v1",
        "projected_at": current_time.isoformat(),
        "work": dict(work),
        "correlation_id": correlation_id,
        "return_to": return_route,
        "ownership": {
            "claim": claim_dict,
            "claim_live": claim_live,
            "binding": binding,
            "active_binding_count": len(active_bindings),
            "ambiguous_binding": len(active_bindings) > 1,
        },
        "continuity": {
            "dispatch": dispatch,
            "request": request,
            "receipt": receipt,
            "reconcile_decision": reconcile,
            "continuation": continuation,
            "continuation_resolved": resolved,
            "backpressure": backpressure,
            "worker_transition": worker_transition,
            "manager_wake_request": manager_wake_request,
            "manager_wake_resolution": manager_wake_resolution,
        },
        "next_action": next_action,
    }
