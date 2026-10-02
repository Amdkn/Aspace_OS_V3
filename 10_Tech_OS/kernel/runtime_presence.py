#!/usr/bin/env python3
"""Derive truthful AgentPresence from existing runtime + WorkGraph evidence.

This module does not create another scheduler or persistence layer.
It projects:
- RuntimeObservation (machine/harness evidence with TTL)
- WorkGraph claim/session_binding truth
- MissionCell continuation state

into the canonical presence states used by Agent OS:
OFFLINE | AVAILABLE | BOUND | EXECUTING | STALE | DEGRADED | UNKNOWN.
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from mission_continuity import project_mission_cell
from truth_projection import project_truth

PRESENCE_STATES = {
    "OFFLINE",
    "AVAILABLE",
    "BOUND",
    "EXECUTING",
    "STALE",
    "DEGRADED",
    "UNKNOWN",
}

EXECUTING_WORK_STATES = {"running", "in_progress", "active", "executing"}


def _parse_time(value: Any) -> datetime | None:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        # Accept milliseconds or seconds since epoch.
        seconds = float(value)
        if seconds > 10_000_000_000:
            seconds /= 1000.0
        return datetime.fromtimestamp(seconds, tz=timezone.utc)
    text = str(value).strip().replace("Z", "+00:00")
    if not text:
        return None
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _pick(mapping: dict[str, Any], snake: str, camel: str, default: Any = None) -> Any:
    if snake in mapping:
        return mapping[snake]
    if camel in mapping:
        return mapping[camel]
    return default


def normalize_runtime_observation(observation: dict[str, Any] | None) -> dict[str, Any] | None:
    """Normalize existing Machine Fabric / Agent OS observation shapes.

    The adapter intentionally accepts both snake_case runtime receipts and the
    camelCase Agent OS RuntimePresence vocabulary. It does not invent liveness.
    """
    if not observation:
        return None

    observed_at = _parse_time(_pick(observation, "observed_at", "observedAt"))
    expires_at = _parse_time(_pick(observation, "expires_at", "expiresAt"))
    ttl_seconds = _pick(observation, "ttl_seconds", "ttlSeconds")

    if expires_at is None and observed_at is not None and ttl_seconds:
        try:
            from datetime import timedelta
            expires_at = observed_at + timedelta(seconds=float(ttl_seconds))
        except (TypeError, ValueError):
            expires_at = None

    available = observation.get("available")
    if available is None:
        # Existing Machine Fabric presence uses active, Agent OS uses a
        # RuntimePresence object whose freshness determines liveness.
        if "active" in observation:
            available = observation.get("active") is True
        elif observation.get("health") in {"ONLINE", "UP", "AVAILABLE"}:
            available = True
        elif observation.get("health") in {"OFFLINE", "DOWN", "UNAVAILABLE"}:
            available = False

    return {
        "schema": observation.get("schema", "aspace.runtime-observation.v1"),
        "identity": observation.get("identity")
        or observation.get("worker_id")
        or observation.get("workerId")
        or observation.get("session_id")
        or observation.get("sessionId"),
        "provenance": observation.get("provenance", "runtime-observation"),
        "observed_at": observed_at,
        "expires_at": expires_at,
        "available": available,
        "degraded_reason": _pick(observation, "degraded_reason", "degradedReason"),
        "capabilities": observation.get("capabilities") or {},
        "evidence_refs": _pick(observation, "evidence_refs", "evidenceRefs", []) or [],
        "fencing_lease_identity": _pick(
            observation,
            "fencing_lease_identity",
            "fencingLeaseIdentity",
            "",
        )
        or "",
        "raw": observation,
    }


def _derive_state(
    *,
    work_status: str,
    claim_live: bool,
    binding: dict[str, Any] | None,
    ambiguous_binding: bool,
    runtime: dict[str, Any] | None,
    now: datetime,
) -> tuple[str, str]:
    if ambiguous_binding:
        return "DEGRADED", "multiple_active_bindings"

    if runtime:
        observed_at = runtime.get("observed_at")
        expires_at = runtime.get("expires_at")
        if expires_at is not None and expires_at <= now:
            return "STALE", "runtime_observation_ttl_expired"
        if observed_at is None and expires_at is None:
            return "UNKNOWN", "runtime_observation_has_no_freshness"

        if runtime.get("degraded_reason"):
            return "DEGRADED", str(runtime["degraded_reason"])

        if runtime.get("available") is False:
            if claim_live or binding:
                return "DEGRADED", "runtime_offline_with_work_binding"
            return "OFFLINE", "runtime_observed_offline"

    if binding and not claim_live:
        return "DEGRADED", "binding_without_live_claim"

    if claim_live and binding:
        if work_status in EXECUTING_WORK_STATES:
            return "EXECUTING", "fresh_runtime_live_claim_and_executing_work"
        return "BOUND", "fresh_runtime_live_claim_and_binding"

    if runtime and runtime.get("available") is True:
        return "AVAILABLE", "fresh_runtime_available_without_work_binding"

    if claim_live and not binding:
        return "DEGRADED", "live_claim_without_session_binding"

    if binding:
        return "BOUND", "binding_present_without_runtime_observation"

    return "UNKNOWN", "no_runtime_or_binding_evidence"


def project_agent_presence(
    db_path: str | Path,
    work_id: int,
    runtime_observation: dict[str, Any] | None,
    *,
    now: datetime | None = None,
) -> dict[str, Any]:
    """Project one work cell into truthful AgentPresence."""
    current_time = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    cell = project_mission_cell(db_path, work_id, now=current_time)
    ownership = cell["ownership"]
    runtime = normalize_runtime_observation(runtime_observation)

    state, reason = _derive_state(
        work_status=str(cell["work"]["status"]),
        claim_live=bool(ownership["claim_live"]),
        binding=ownership["binding"],
        ambiguous_binding=bool(ownership["ambiguous_binding"]),
        runtime=runtime,
        now=current_time,
    )

    evidence_refs: list[str] = []
    if runtime:
        evidence_refs.extend(str(x) for x in runtime["evidence_refs"])
    for key in (
        "dispatch",
        "request",
        "receipt",
        "reconcile_decision",
        "continuation",
        "continuation_resolved",
    ):
        event = cell["continuity"].get(key)
        if event:
            evidence_refs.append(f"workgraph:event:{event['id']}")

    binding = ownership["binding"]
    claim = ownership["claim"]
    identity = (
        (runtime or {}).get("identity")
        or (binding or {}).get("session_key")
        or (claim or {}).get("harness")
        or f"work:{work_id}"
    )

    observed_at = (runtime or {}).get("observed_at")
    expires_at = (runtime or {}).get("expires_at")

    result = {
        "schema": "aspace.agent-presence.v1",
        "identity": identity,
        "state": state,
        "reason": reason,
        "provenance": (runtime or {}).get("provenance") or "workgraph",
        "observed_at": observed_at.isoformat() if observed_at else None,
        "expires_at": expires_at.isoformat() if expires_at else None,
        "evidence_refs": sorted(set(evidence_refs)),
        "fencing_lease_identity": (runtime or {}).get("fencing_lease_identity") or "",
        "capabilities": (runtime or {}).get("capabilities") or {},
        "work_id": work_id,
        "correlation_id": cell.get("correlation_id"),
        "return_to": cell.get("return_to"),
        "ownership": {
            "claim_live": ownership["claim_live"],
            "claim": claim,
            "binding": binding,
            "ambiguous_binding": ownership["ambiguous_binding"],
        },
        "next_action": cell["next_action"],
    }

    if state not in PRESENCE_STATES:
        raise RuntimeError(f"invalid derived presence state: {state}")
    return result


def project_agent_presence_for_human(
    db_path: str | Path,
    work_id: int,
    runtime_observation: dict[str, Any] | None,
    *,
    now: datetime | None = None,
) -> dict[str, Any]:
    """TB09 adapter: machine presence truth -> provenance-safe human projection.

    This is intentionally thin. Agent OS, Linear and GWS may render the same
    envelope differently, but none may erase source/authority/freshness/evidence.
    """
    current_time = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    presence = project_agent_presence(
        db_path,
        work_id,
        runtime_observation,
        now=current_time,
    )

    evidence = list(presence.get("evidence_refs") or [])
    source = presence.get("provenance")
    observed_at = presence.get("observed_at")
    expires_at = presence.get("expires_at")

    # WorkGraph-derived truth without a runtime timestamp remains UNKNOWN at
    # the human-projection boundary unless a stronger evidence receipt exists.
    return project_truth(
        value={
            "identity": presence.get("identity"),
            "presence_state": presence.get("state"),
            "reason": presence.get("reason"),
            "capabilities": presence.get("capabilities") or {},
            "next_action": presence.get("next_action"),
            "return_to": presence.get("return_to"),
        },
        source=source,
        authority="workgraph+runtime_presence",
        observed_at=observed_at,
        expires_at=expires_at,
        evidence_refs=evidence,
        confidence=None,
        now=current_time,
        correlation_id=presence.get("correlation_id"),
        work_id=work_id,
    )
