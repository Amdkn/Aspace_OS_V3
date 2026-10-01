#!/usr/bin/env python3
"""Deterministic mission watcher over canonical WorkGraph bindings.

This module does not run an LLM and does not create another scheduler.
It converts provider observations into durable transition/wake events:
binding -> provider observation -> transition -> selective manager wake request.

A separate manager adapter consumes manager_wake_requested events. P4 proves
the real manager wake/rebind path end-to-end.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import urllib.error
import urllib.request
from contextlib import closing
from pathlib import Path
from typing import Any

from fleet_ownership import DB
from mission_continuity import project_mission_cell

WAKE_TRANSITIONS = {
    "PR_READY",
    "FAILED",
    "AWAITING_USER_FEEDBACK",
    "CI_FAILURE",
    "EVIDENCE_READY",
    "UNKNOWN",
}
QUIET_PROVIDER_STATES = {
    "IN_PROGRESS",
    "ACTIVE",
    "QUEUED",
    "PENDING",
    "STARTING",
}
FAILED_PROVIDER_STATES = {"FAILED", "CANCELLED", "CANCELED"}


class MissionWatcherError(RuntimeError):
    pass


def _connect(db_path: str | Path) -> sqlite3.Connection:
    con = sqlite3.connect(Path(db_path), timeout=10)
    con.row_factory = sqlite3.Row
    return con


def _normalize_session(value: Any) -> str:
    return str(value or "").removeprefix("sessions/")


def _observation_session(observation: dict[str, Any]) -> str:
    return _normalize_session(
        observation.get("id")
        or observation.get("sessionId")
        or observation.get("name")
    )


def _pull_requests(observation: dict[str, Any]) -> list[str]:
    urls: list[str] = []
    for output in observation.get("outputs") or []:
        if not isinstance(output, dict):
            continue
        pr = output.get("pullRequest") or output.get("pull_request")
        if isinstance(pr, dict):
            url = pr.get("url") or pr.get("html_url")
        else:
            url = pr
        if url:
            urls.append(str(url))
    return sorted(set(urls))


def _has_evidence(observation: dict[str, Any]) -> bool:
    for output in observation.get("outputs") or []:
        if not isinstance(output, dict):
            continue
        if output.get("changeSet") or output.get("change_set"):
            return True
        if output.get("artifacts") or output.get("evidence"):
            return True
        if output.get("pullRequest") or output.get("pull_request"):
            return True
    return False


def _ci_failed(observation: dict[str, Any]) -> bool:
    values = [
        observation.get("ci_state"),
        observation.get("ciStatus"),
        observation.get("check_state"),
    ]
    for value in values:
        if str(value or "").upper() in {"FAILED", "FAILURE", "ERROR", "TIMED_OUT"}:
            return True
    return False


def classify_observation(
    expected_session: str,
    observation: dict[str, Any],
) -> dict[str, Any]:
    observed_session = _observation_session(observation)
    state = str(observation.get("state") or "UNKNOWN").upper()
    prs = _pull_requests(observation)
    evidence = _has_evidence(observation)

    if observed_session != _normalize_session(expected_session):
        return {
            "transition": "UNKNOWN",
            "reason": "binding_session_mismatch",
            "fenced": True,
            "manager_wake_required": True,
            "same_session_resume_safe": False,
            "provider_state": state,
            "pull_requests": prs,
            "evidence_present": evidence,
        }

    if _ci_failed(observation):
        transition = "CI_FAILURE"
    elif state == "AWAITING_USER_FEEDBACK":
        transition = "AWAITING_USER_FEEDBACK"
    elif state in FAILED_PROVIDER_STATES:
        transition = "FAILED"
    elif state == "COMPLETED":
        transition = "PR_READY" if prs else "EVIDENCE_READY"
    elif state in QUIET_PROVIDER_STATES:
        transition = "IN_PROGRESS"
    else:
        transition = "UNKNOWN"

    return {
        "transition": transition,
        "reason": "provider_state",
        "fenced": False,
        "manager_wake_required": transition in WAKE_TRANSITIONS,
        "same_session_resume_safe": transition in {
            "AWAITING_USER_FEEDBACK",
            "CI_FAILURE",
            "IN_PROGRESS",
        },
        "provider_state": state,
        "pull_requests": prs,
        "evidence_present": evidence,
    }


def _fingerprint(
    expected_session: str,
    observation: dict[str, Any],
    classified: dict[str, Any],
) -> str:
    material = {
        "expected_session": _normalize_session(expected_session),
        "observed_session": _observation_session(observation),
        "provider_state": classified["provider_state"],
        "transition": classified["transition"],
        "provider_updated_at": observation.get("updateTime") or observation.get("updated_at"),
        "pull_requests": classified["pull_requests"],
        "evidence_present": classified["evidence_present"],
        "ci_state": observation.get("ci_state") or observation.get("ciStatus"),
        "error": observation.get("error"),
    }
    raw = json.dumps(material, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def _latest_event(
    con: sqlite3.Connection,
    work_id: int,
    kind: str,
) -> sqlite3.Row | None:
    return con.execute(
        "SELECT id,harness,kind,payload,at FROM event "
        "WHERE work_id=? AND kind=? ORDER BY id DESC LIMIT 1",
        (work_id, kind),
    ).fetchone()


def _json(raw: str | None) -> dict[str, Any]:
    if not raw:
        return {}
    try:
        value = json.loads(raw)
    except json.JSONDecodeError:
        return {}
    return value if isinstance(value, dict) else {}


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


def observe_bound_worker(
    db_path: str | Path,
    work_id: int,
    observation: dict[str, Any],
    *,
    manager_target: str = "ANTIGRAVITY",
) -> dict[str, Any]:
    cell = project_mission_cell(db_path, work_id)
    binding = cell["ownership"].get("binding")
    if not binding:
        raise MissionWatcherError("work has no active/idle session binding to observe")

    expected_session = _normalize_session(binding.get("session_key"))
    classified = classify_observation(expected_session, observation)
    fingerprint = _fingerprint(expected_session, observation, classified)

    payload = {
        "schema": "aspace.worker-transition.v1",
        "correlation_id": cell.get("correlation_id"),
        "return_route": cell.get("return_to"),
        "work_id": work_id,
        "session_key": expected_session,
        "harness": binding.get("harness"),
        "observed_session": _observation_session(observation),
        "provider_state": classified["provider_state"],
        "provider_updated_at": observation.get("updateTime") or observation.get("updated_at"),
        "transition": classified["transition"],
        "reason": classified["reason"],
        "fenced": classified["fenced"],
        "pull_requests": classified["pull_requests"],
        "evidence_present": classified["evidence_present"],
        "manager_wake_required": classified["manager_wake_required"],
        "same_session_resume_safe": classified["same_session_resume_safe"],
        "fingerprint": fingerprint,
    }

    with closing(_connect(db_path)) as con, con:
        latest = _latest_event(con, work_id, "worker_transition_observed")
        if latest and _json(latest["payload"]).get("fingerprint") == fingerprint:
            return {
                "idempotent": True,
                "transition_event_id": int(latest["id"]),
                "wake_event_id": None,
                **payload,
            }

        transition_event_id = _append_event(
            con,
            work_id,
            str(binding.get("harness") or "watcher"),
            "worker_transition_observed",
            payload,
        )

        wake_event_id = None
        if classified["manager_wake_required"]:
            wake_payload = {
                "schema": "aspace.manager-wake-request.v1",
                "correlation_id": cell.get("correlation_id"),
                "return_route": cell.get("return_to"),
                "work_id": work_id,
                "session_key": expected_session,
                "manager_target": manager_target,
                "reason": classified["transition"],
                "source_transition_event_id": transition_event_id,
                "transition_fingerprint": fingerprint,
                "same_session_resume_safe": classified["same_session_resume_safe"],
                "fenced": classified["fenced"],
            }
            wake_event_id = _append_event(
                con,
                work_id,
                "mission-watcher",
                "manager_wake_requested",
                wake_payload,
            )

    return {
        "idempotent": False,
        "transition_event_id": transition_event_id,
        "wake_event_id": wake_event_id,
        **payload,
    }


def resolve_manager_wake(
    db_path: str | Path,
    work_id: int,
    *,
    source_transition_event_id: int,
    outcome: str,
    manager_target: str = "ANTIGRAVITY",
) -> dict[str, Any]:
    payload = {
        "schema": "aspace.manager-wake-resolution.v1",
        "source_transition_event_id": int(source_transition_event_id),
        "manager_target": manager_target,
        "outcome": str(outcome),
    }
    with closing(_connect(db_path)) as con, con:
        latest = _latest_event(con, work_id, "manager_wake_resolved")
        if latest:
            current = _json(latest["payload"])
            if (
                int(current.get("source_transition_event_id") or -1)
                == int(source_transition_event_id)
                and current.get("manager_target") == manager_target
                and current.get("outcome") == str(outcome)
            ):
                return {"idempotent": True, "event_id": int(latest["id"]), **current}

        event_id = _append_event(
            con,
            work_id,
            "mission-watcher",
            "manager_wake_resolved",
            payload,
        )
    return {"idempotent": False, "event_id": event_id, **payload}


def active_bindings(db_path: str | Path) -> list[dict[str, Any]]:
    with closing(_connect(db_path)) as con:
        rows = con.execute(
            """SELECT work_id,session_key,harness,capability,external_ref,status
               FROM session_binding
               WHERE status IN ('active','idle') AND ended_at IS NULL
               ORDER BY work_id, id"""
        ).fetchall()
    return [dict(row) for row in rows]


def _http_json(url: str, timeout: float) -> dict[str, Any]:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        value = json.load(response)
    if not isinstance(value, dict):
        raise MissionWatcherError("provider observation must be a JSON object")
    return value


def jules_tick(
    db_path: str | Path,
    *,
    provider_base: str = "http://127.0.0.1:43118",
    timeout: float = 5.0,
    manager_target: str = "ANTIGRAVITY",
) -> dict[str, Any]:
    results: list[dict[str, Any]] = []
    for binding in active_bindings(db_path):
        if str(binding.get("harness") or "").lower() != "jules":
            continue
        session = _normalize_session(binding.get("session_key"))
        try:
            observation = _http_json(
                provider_base.rstrip("/") + "/sessions/" + session,
                timeout,
            )
        except (OSError, urllib.error.URLError, json.JSONDecodeError) as exc:
            observation = {
                "id": session,
                "state": "UNKNOWN",
                "error": f"{type(exc).__name__}: {exc}",
            }
        results.append(
            observe_bound_worker(
                db_path,
                int(binding["work_id"]),
                observation,
                manager_target=manager_target,
            )
        )
    return {
        "schema": "aspace.mission-watcher-tick.v1",
        "observed": len(results),
        "wake_requests": sum(1 for item in results if item.get("wake_event_id")),
        "results": results,
    }


def _load_json(path: str) -> dict[str, Any]:
    value = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise MissionWatcherError("observation file must contain a JSON object")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description="A'Space deterministic mission watcher")
    parser.add_argument("--db", default=str(DB))
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("observe")
    p.add_argument("--work", type=int, required=True)
    p.add_argument("--observation", required=True)
    p.add_argument("--manager-target", default="ANTIGRAVITY")

    p = sub.add_parser("jules-tick")
    p.add_argument("--provider-base", default="http://127.0.0.1:43118")
    p.add_argument("--timeout", type=float, default=5.0)
    p.add_argument("--manager-target", default="ANTIGRAVITY")

    p = sub.add_parser("resolve-wake")
    p.add_argument("--work", type=int, required=True)
    p.add_argument("--source-transition-event", type=int, required=True)
    p.add_argument("--outcome", required=True)
    p.add_argument("--manager-target", default="ANTIGRAVITY")

    args = parser.parse_args()
    if args.cmd == "observe":
        print(json.dumps(
            observe_bound_worker(
                args.db,
                args.work,
                _load_json(args.observation),
                manager_target=args.manager_target,
            ),
            indent=2,
        ))
        return 0
    if args.cmd == "jules-tick":
        print(json.dumps(
            jules_tick(
                args.db,
                provider_base=args.provider_base,
                timeout=args.timeout,
                manager_target=args.manager_target,
            ),
            indent=2,
        ))
        return 0
    if args.cmd == "resolve-wake":
        print(json.dumps(
            resolve_manager_wake(
                args.db,
                args.work,
                source_transition_event_id=args.source_transition_event,
                outcome=args.outcome,
                manager_target=args.manager_target,
            ),
            indent=2,
        ))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
