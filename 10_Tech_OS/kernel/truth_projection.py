#!/usr/bin/env python3
"""Truth/provenance envelope for human-facing projections.

This module implements the smallest CG1 + CG2 vertical slice from Wargame #323:
machine truth -> Amy/Agent OS/Linear/GWS human projection (TB09).

It does not decide business truth. It only states whether a value is CURRENT,
STALE, or UNKNOWN based on explicit provenance and freshness evidence.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any

TRUTH_STATES = {"CURRENT", "STALE", "UNKNOWN"}


def _parse_time(value: Any) -> datetime | None:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        seconds = float(value)
        if seconds > 10_000_000_000:
            seconds /= 1000.0
        return datetime.fromtimestamp(seconds, tz=timezone.utc)
    text = str(value).strip().replace("Z", "+00:00")
    if not text:
        return None
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def project_truth(
    *,
    value: Any,
    source: str | None,
    authority: str | None,
    observed_at: Any,
    evidence_refs: list[str] | tuple[str, ...] | None,
    freshness_seconds: float | int | None = None,
    expires_at: Any = None,
    confidence: float | int | None = None,
    now: datetime | None = None,
    correlation_id: str | None = None,
    work_id: int | str | None = None,
    operation_id: str | None = None,
) -> dict[str, Any]:
    """Project a value through a provenance/freshness contract.

    CURRENT requires:
    - non-empty source;
    - non-empty authority;
    - parseable observed_at;
    - at least one evidence ref;
    - an explicit freshness bound through expires_at or freshness_seconds.

    Missing proof never becomes CURRENT. Stale proof remains authentic but STALE.
    """
    current = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    observed = _parse_time(observed_at)
    expires = _parse_time(expires_at)
    evidence = sorted({str(x).strip() for x in (evidence_refs or []) if str(x).strip()})

    if expires is None and observed is not None and freshness_seconds is not None:
        try:
            ttl = float(freshness_seconds)
            if ttl > 0:
                expires = observed + timedelta(seconds=ttl)
        except (TypeError, ValueError):
            expires = None

    missing: list[str] = []
    if not source:
        missing.append("source")
    if not authority:
        missing.append("authority")
    if observed is None:
        missing.append("observed_at")
    if not evidence:
        missing.append("evidence_refs")
    if expires is None:
        missing.append("freshness")

    if missing:
        state = "UNKNOWN"
        reason = "missing_required_provenance:" + ",".join(missing)
    elif expires <= current:
        state = "STALE"
        reason = "evidence_freshness_expired"
    else:
        state = "CURRENT"
        reason = "provenance_and_freshness_valid"

    confidence_value: float | None
    try:
        confidence_value = float(confidence) if confidence is not None else None
    except (TypeError, ValueError):
        confidence_value = None
    if confidence_value is not None and not 0.0 <= confidence_value <= 1.0:
        confidence_value = None

    result = {
        "schema": "aspace.truth-projection.v1",
        "value": value,
        "truth_state": state,
        "reason": reason,
        "source": source,
        "authority": authority,
        "observed_at": observed.isoformat() if observed else None,
        "expires_at": expires.isoformat() if expires else None,
        "freshness_seconds": (
            max(0.0, (expires - observed).total_seconds())
            if observed is not None and expires is not None
            else None
        ),
        "evidence_refs": evidence,
        "confidence": confidence_value,
        "confidence_state": "KNOWN" if confidence_value is not None else "UNKNOWN",
        "correlation_id": correlation_id,
        "work_id": work_id,
        "operation_id": operation_id,
    }
    if state not in TRUTH_STATES:
        raise RuntimeError(f"invalid truth state: {state}")
    return result


def project_agent_os_display(
    *,
    actor_id: str,
    institutional_role: str,
    runtime_choice: str,
    provider_name: str,
    model_name: str,
    total_token_budget: int,
    consumed_tokens: int,
) -> dict[str, Any]:
    """Display runtime choice and remaining resource budget separately from identity."""
    remaining_budget = max(0, total_token_budget - consumed_tokens)
    return {
        "schema": "aspace.agent-os-display.v1",
        "identity": {
            "actor_id": actor_id,
            "institutional_role": institutional_role,
        },
        "runtime_choice": {
            "runtime_id": runtime_choice,
            "provider": provider_name,
            "model": model_name,
        },
        "resource_budget": {
            "total_token_budget": total_token_budget,
            "consumed_tokens": consumed_tokens,
            "remaining_budget": remaining_budget,
            "quota_status": "EXHAUSTED" if remaining_budget == 0 else "OK",
        },
    }
