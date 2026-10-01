#!/usr/bin/env python3
"""Capability dispatch + durable return routing over the canonical WorkGraph.

No second scheduler and no new database:
- ownership is acquired through the existing uc.py claim command;
- inter-process dispatch serialization reuses fleet_ownership.dispatch_lock;
- MissionCell/AgentPresence are projections from #293/#294;
- Rory decisions become append-only continuation_routed events;
- UNKNOWN never becomes a blind retry.
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import uuid
from pathlib import Path
from typing import Any

from fleet_ownership import DB, canonical, dispatch_lock
from mission_continuity import MissionContinuityError, project_mission_cell

SAFE_CAPABILITY_STATES = {"AVAILABLE", "PASS", "READY", "available", "pass", "ready"}
SAFE_PRESENCE_STATES = {"AVAILABLE"}

VERDICT_ROUTES = {
    "ACCEPT_CONTINUE": ("NEXT_FLOW", None),
    "COMPLETE": ("DONE", None),
    "RECOVER_UNKNOWN": ("RECOVER", "DONNA"),
    "REOPEN_BUILD": ("REOPEN", "RYAN"),
    "REOPEN_DESIGN": ("REOPEN", "CLARA"),
    "HOLD": ("WAIT", None),
}


class DispatchRoutingError(RuntimeError):
    pass


def _connect(db_path: str | Path) -> sqlite3.Connection:
    con = sqlite3.connect(Path(db_path), timeout=10)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys=ON")
    return con


def _json(raw: str | None) -> dict[str, Any]:
    if not raw:
        return {}
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise DispatchRoutingError("invalid durable event payload") from exc
    return value if isinstance(value, dict) else {"value": value}


def select_runtime(
    required_capability: str,
    candidates: list[dict[str, Any]],
) -> dict[str, Any]:
    """Choose a deterministic safe runtime or return explicit backpressure."""
    safe: list[dict[str, Any]] = []
    rejected: list[dict[str, str]] = []

    for candidate in candidates:
        runtime_id = str(candidate.get("runtime_id") or candidate.get("id") or "")
        if not runtime_id:
            rejected.append({"runtime_id": "", "reason": "missing_runtime_identity"})
            continue

        presence = str(candidate.get("presence_state") or "UNKNOWN").upper()
        if presence not in SAFE_PRESENCE_STATES:
            rejected.append({"runtime_id": runtime_id, "reason": f"presence_{presence.lower()}"})
            continue

        capabilities = candidate.get("capabilities") or {}
        capability_state = capabilities.get(required_capability)
        if capability_state not in SAFE_CAPABILITY_STATES:
            rejected.append({"runtime_id": runtime_id, "reason": "capability_unavailable"})
            continue

        if candidate.get("healthy", True) is not True:
            rejected.append({"runtime_id": runtime_id, "reason": "runtime_unhealthy"})
            continue

        if candidate.get("quota_ok", True) is not True:
            rejected.append({"runtime_id": runtime_id, "reason": "quota_backpressure"})
            continue

        safe.append(candidate)

    if not safe:
        return {
            "decision": "BACKPRESSURE",
            "required_capability": required_capability,
            "reason": "no_safe_runtime",
            "rejected": rejected,
        }

    safe.sort(
        key=lambda item: (
            -int(item.get("priority", 0)),
            str(item.get("harness") or ""),
            str(item.get("runtime_id") or item.get("id") or ""),
        )
    )
    chosen = safe[0]
    return {
        "decision": "DISPATCH",
        "required_capability": required_capability,
        "runtime_id": str(chosen.get("runtime_id") or chosen.get("id")),
        "harness": str(chosen.get("harness") or "unknown"),
        "candidate": chosen,
    }


def _dependency_blockers(con: sqlite3.Connection, work_id: int) -> list[int]:
    rows = con.execute(
        """SELECT d.depends_on_id
           FROM work_dependency d
           JOIN work w ON w.id=d.depends_on_id
           WHERE d.work_id=?
             AND d.kind IN ('blocks','requires')
             AND w.status!='done'
           ORDER BY d.depends_on_id""",
        (work_id,),
    ).fetchall()
    return [int(row["depends_on_id"]) for row in rows]


def _unresolved_dispatch_attempt(con: sqlite3.Connection, work_id: int) -> sqlite3.Row | None:
    return con.execute(
        """SELECT e.id,e.payload
           FROM event e
           WHERE e.work_id=? AND e.kind='fleet_dispatch_attempt'
             AND NOT EXISTS (
               SELECT 1 FROM event r
               WHERE r.work_id=e.work_id
                 AND r.kind='fleet_dispatch_resolved'
                 AND r.id>e.id
             )
           ORDER BY e.id DESC LIMIT 1""",
        (work_id,),
    ).fetchone()


def _append_event(
    con: sqlite3.Connection,
    work_id: int,
    harness: str | None,
    kind: str,
    payload: dict[str, Any],
) -> int:
    cur = con.execute(
        "INSERT INTO event(work_id,harness,kind,payload) VALUES(?,?,?,?)",
        (work_id, harness, kind, json.dumps(payload, sort_keys=True)),
    )
    return int(cur.lastrowid)


def record_backpressure(
    db_path: str | Path,
    work_id: int,
    *,
    required_capability: str,
    reason: str,
    correlation_id: str | None,
    return_route: dict[str, Any] | None,
    rejected: list[dict[str, Any]] | None = None,
    not_before: str | None = None,
) -> dict[str, Any]:
    cell = project_mission_cell(db_path, work_id)
    stable_correlation = cell.get("correlation_id") or correlation_id or str(uuid.uuid4())
    stable_return = cell.get("return_to") or return_route
    if not stable_return:
        raise DispatchRoutingError("initial backpressure requires explicit return_route")

    payload = {
        "schema": "aspace.dispatch-backpressure.v1",
        "correlation_id": stable_correlation,
        "return_route": stable_return,
        "required_capability": required_capability,
        "reason": reason,
        "rejected": rejected or [],
        "not_before": not_before,
    }
    with _connect(db_path) as con, con:
        event_id = _append_event(con, work_id, "nardole-dispatch", "dispatch_backpressure", payload)
    return {"event_id": event_id, **payload}


def reserve_dispatch(
    db_path: str | Path,
    work_id: int,
    *,
    required_capability: str,
    candidates: list[dict[str, Any]],
    return_route: dict[str, Any] | None = None,
    correlation_id: str | None = None,
    lease_seconds: int = 900,
    lock_path: str | Path | None = None,
) -> dict[str, Any]:
    """Select a safe runtime, acquire canonical claim, and durably record dispatch."""
    with dispatch_lock(lock_path):
        cell = project_mission_cell(db_path, work_id)

        if cell["ownership"]["ambiguous_binding"]:
            raise DispatchRoutingError("multiple active bindings require reconciliation")
        if cell["ownership"]["claim_live"]:
            raise DispatchRoutingError("live owner already exists")
        if cell["ownership"]["binding"]:
            raise DispatchRoutingError("existing session binding must be reconciled")

        with _connect(db_path) as con:
            blockers = _dependency_blockers(con, work_id)
            unresolved = _unresolved_dispatch_attempt(con, work_id)

        stable_correlation = cell.get("correlation_id") or correlation_id or str(uuid.uuid4())
        stable_return = cell.get("return_to") or return_route
        if not stable_return:
            raise DispatchRoutingError("initial dispatch requires explicit return_route")

        if blockers:
            return {
                "decision": "BACKPRESSURE",
                "backpressure": record_backpressure(
                    db_path,
                    work_id,
                    required_capability=required_capability,
                    reason="dependency_blocked",
                    rejected=[{"work_id": value} for value in blockers],
                    correlation_id=stable_correlation,
                    return_route=stable_return,
                ),
            }

        if unresolved:
            raise DispatchRoutingError(
                f"unresolved prior dispatch attempt requires reconciliation: event {unresolved['id']}"
            )

        allowed = {"DISPATCH_READY", "DISPATCH_RETRY", "BACKPRESSURE"}
        if cell["next_action"].get("action") not in allowed:
            raise DispatchRoutingError(
                f"mission cell is not dispatchable: {cell['next_action'].get('action')}"
            )

        decision = select_runtime(required_capability, candidates)
        if decision["decision"] == "BACKPRESSURE":
            return {
                "decision": "BACKPRESSURE",
                "backpressure": record_backpressure(
                    db_path,
                    work_id,
                    required_capability=required_capability,
                    reason=decision["reason"],
                    rejected=decision["rejected"],
                    correlation_id=stable_correlation,
                    return_route=stable_return,
                ),
            }

        harness = decision["harness"]
        claim = canonical(
            "uc.py",
            "claim",
            "--work",
            work_id,
            "--harness",
            harness,
            "--lease",
            lease_seconds,
            db_path=db_path,
        )
        work = claim.get("work")
        if not work or int(work.get("id")) != int(work_id):
            raise DispatchRoutingError("atomic claim was not acquired")

        dispatch_id = str(uuid.uuid4())
        retry = cell["next_action"].get("action") == "DISPATCH_RETRY"
        payload = {
            "schema": "aspace.dispatch-envelope.v2",
            "dispatch_id": dispatch_id,
            "work_id": work_id,
            "correlation_id": stable_correlation,
            "return_route": stable_return,
            "required_capability": required_capability,
            "target_runtime": decision["runtime_id"],
            "target_harness": harness,
            "retry": retry,
            "prior_receipt_event_id": (
                (cell["continuity"].get("receipt") or {}).get("id")
            ),
        }

        with _connect(db_path) as con, con:
            envelope_id = _append_event(
                con, work_id, "nardole-dispatch", "dispatch_envelope", payload
            )
            attempt_id = _append_event(
                con, work_id, harness, "fleet_dispatch_attempt", payload
            )

        return {
            "decision": "DISPATCH",
            "work_id": work_id,
            "claim": work,
            "dispatch_event_id": envelope_id,
            "attempt_event_id": attempt_id,
            "envelope": payload,
        }

def resolve_dispatch_attempt(
    db_path: str | Path,
    work_id: int,
    *,
    dispatch_id: str,
    outcome: str,
    session_key: str | None = None,
) -> dict[str, Any]:
    payload = {
        "schema": "aspace.dispatch-resolution.v1",
        "dispatch_id": dispatch_id,
        "outcome": outcome,
        "session_key": session_key,
    }
    with _connect(db_path) as con, con:
        event_id = _append_event(
            con, work_id, "nardole-dispatch", "fleet_dispatch_resolved", payload
        )
    return {"event_id": event_id, **payload}


def _latest_event(con: sqlite3.Connection, work_id: int, kind: str) -> sqlite3.Row | None:
    return con.execute(
        "SELECT id,harness,kind,payload,at FROM event WHERE work_id=? AND kind=? ORDER BY id DESC LIMIT 1",
        (work_id, kind),
    ).fetchone()


def route_reconcile_decision(db_path: str | Path, work_id: int) -> dict[str, Any]:
    """Materialize exactly one continuation_routed event for the latest Rory decision."""
    cell = project_mission_cell(db_path, work_id)

    with _connect(db_path) as con:
        reconcile_row = _latest_event(con, work_id, "rory_reconcile_decision")
        receipt_row = _latest_event(con, work_id, "harness_execution_receipt")
        routed_row = _latest_event(con, work_id, "continuation_routed")

    if not reconcile_row:
        raise DispatchRoutingError("no Rory reconcile decision to route")

    if routed_row and int(routed_row["id"]) > int(reconcile_row["id"]):
        payload = _json(routed_row["payload"])
        return {"event_id": int(routed_row["id"]), "idempotent": True, **payload}

    reconcile = _json(reconcile_row["payload"])
    receipt = _json(receipt_row["payload"]) if receipt_row else {}
    verdict = str(reconcile.get("verdict") or "").upper()
    correlation_id = (
        reconcile.get("correlation_id")
        or cell.get("correlation_id")
        or receipt.get("correlation_id")
    )
    return_route = reconcile.get("return_route") or cell.get("return_to")

    if not correlation_id:
        raise DispatchRoutingError("reconcile decision has no stable correlation_id")
    if not return_route:
        raise DispatchRoutingError("reconcile decision has no return_route")

    if verdict == "RETRY_SAFE":
        effect_state = str(receipt.get("effect_state") or "").upper()
        retry_safe = receipt.get("retry_safe") is True
        if effect_state == "UNKNOWN" or not retry_safe:
            raise DispatchRoutingError("RETRY_SAFE contradicts receipt effect semantics")
        route_class = "RETRY"
        target = (
            reconcile.get("target_capability")
            or ((cell["continuity"].get("dispatch") or {}).get("payload") or {}).get(
                "required_capability"
            )
        )
    else:
        mapped = VERDICT_ROUTES.get(verdict)
        if not mapped:
            raise DispatchRoutingError(f"unsupported reconcile verdict: {verdict or '<empty>'}")
        route_class, default_target = mapped
        target = reconcile.get("target_capability") or default_target
        if verdict == "ACCEPT_CONTINUE" and not target:
            if isinstance(return_route, dict):
                target = return_route.get("capability") or return_route.get("target_capability")

    payload = {
        "schema": "aspace.continuation-route.v2",
        "correlation_id": str(correlation_id),
        "return_route": return_route,
        "route_class": route_class,
        "target_capability": target,
        "verdict": verdict,
        "source_reconcile_event_id": int(reconcile_row["id"]),
        "source_receipt_event_id": int(receipt_row["id"]) if receipt_row else None,
        "retry_safe": receipt.get("retry_safe"),
        "effect_state": receipt.get("effect_state"),
        "reopen_cell": reconcile.get("reopen_cell"),
    }

    with _connect(db_path) as con, con:
        event_id = _append_event(
            con, work_id, "nardole-dispatch", "continuation_routed", payload
        )
    return {"event_id": event_id, "idempotent": False, **payload}


def _load_json(path: str) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="A'Space capability dispatch + return router")
    parser.add_argument("--db", default=str(DB))
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("select")
    p.add_argument("--capability", required=True)
    p.add_argument("--candidates", required=True, help="JSON file containing candidate runtime array")

    p = sub.add_parser("reserve")
    p.add_argument("--work", type=int, required=True)
    p.add_argument("--capability", required=True)
    p.add_argument("--candidates", required=True)
    p.add_argument("--return-route", help="JSON file; required for first dispatch")
    p.add_argument("--correlation-id")
    p.add_argument("--lease", type=int, default=900)

    p = sub.add_parser("route")
    p.add_argument("--work", type=int, required=True)

    args = parser.parse_args()

    if args.cmd == "select":
        print(json.dumps(select_runtime(args.capability, _load_json(args.candidates)), indent=2))
        return 0
    if args.cmd == "reserve":
        return_route = _load_json(args.return_route) if args.return_route else None
        result = reserve_dispatch(
            args.db,
            args.work,
            required_capability=args.capability,
            candidates=_load_json(args.candidates),
            return_route=return_route,
            correlation_id=args.correlation_id,
            lease_seconds=args.lease,
        )
        print(json.dumps(result, indent=2))
        return 0
    if args.cmd == "route":
        print(json.dumps(route_reconcile_decision(args.db, args.work), indent=2))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
