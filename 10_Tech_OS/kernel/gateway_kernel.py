#!/usr/bin/env python3
"""Gateway Kernel: Protocol Core + identity/presence/session.

Carries existing A'Space cross-fabric coordinates without inventing a second
identity system. Reuses:
  - InterFabricEnvelope.v1 from #471
  - Embodied Holon contract from #318
  - Temporal Truth / Context Compiler from #448

This kernel provides the minimal protocol for:
  - protocol/version negotiation
  - correlation/fencing preservation
  - presence freshness/TTL
  - session lineage
  - reconnect/resume
  - delivery ambiguity preserved as UNKNOWN

Golden invariant (from #542): A runtime may die and a surface may disconnect;
  the institutional holon, work/correlation identity, authority, evidence lineage
  and return_to must survive.
"""
from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone
from typing import Any, Dict, Optional

from inter_fabric import InterFabricEnvelope, InterFabricInvariantError
from temporal_truth.compiler import ContextCompiler
from temporal_truth.temporal_truth import TemporalCanonGraph


# ── Protocol version ────────────────────────────────────────────────────────

GATEWAY_PROTOCOL_VERSION = "v1.0.0"


# ── Session lineage ────────────────────────────────────────────────────────

class SessionLineage:
    """Tracks session lifecycle without mutating institutional identity."""

    def __init__(
        self,
        correlation_id: str,
        work_id: int,
        return_to: str,
        session_id: str,
        parent_session_id: Optional[str] = None,
    ):
        self.correlation_id = correlation_id
        self.work_id = work_id
        self.return_to = return_to
        self.session_id = session_id
        self.parent_session_id = parent_session_id
        self.reconnect_count = 0
        self.first_observed_at: Optional[datetime] = None
        self.last_seen_at: Optional[datetime] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "correlation_id": self.correlation_id,
            "work_id": self.work_id,
            "return_to": self.return_to,
            "session_id": self.session_id,
            "parent_session_id": self.parent_session_id,
            "reconnect_count": self.reconnect_count,
            "first_observed_at": (
                self.first_observed_at.isoformat() if self.first_observed_at else None
            ),
            "last_seen_at": self.last_seen_at.isoformat() if self.last_seen_at else None,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SessionLineage":
        return cls(
            correlation_id=data["correlation_id"],
            work_id=data["work_id"],
            return_to=data["return_to"],
            session_id=data["session_id"],
            parent_session_id=data.get("parent_session_id"),
        )

    def verify_identity_preserved(
        self,
        old_envelope: Dict[str, Any],
        new_envelope: Dict[str, Any],
    ) -> bool:
        """Verify reconnect did not mutate institutional identity or authority."""

        # Holon identity must be invariant
        if old_envelope.get("identity", {}).get("holon_id") != (
            new_envelope.get("identity", {}).get("holon_id")
        ):
            return False

        # Correlation ID must be preserved
        if old_envelope.get("mission", {}).get("correlation_id") != (
            new_envelope.get("mission", {}).get("correlation_id")
        ):
            return False

        # Work ID must be preserved
        if old_envelope.get("mission", {}).get("work_id") != (
            new_envelope.get("mission", {}).get("work_id")
        ):
            return False

        # Return_to must be preserved
        if old_envelope.get("routing", {}).get("return_to") != (
            new_envelope.get("routing", {}).get("return_to")
        ):
            return False

        # Authority must be preserved (scope and policy_ref)
        old_auth = old_envelope.get("authority", {})
        new_auth = new_envelope.get("authority", {})
        if old_auth.get("authority_scope") != new_auth.get("authority_scope"):
            return False
        if old_auth.get("policy_ref") != new_auth.get("policy_ref"):
            return False

        # Evidence lineage must not shrink
        old_evidence = set(old_envelope.get("truth", {}).get("evidence_refs", []))
        new_evidence = set(new_envelope.get("truth", {}).get("evidence_refs", []))
        if not old_evidence.issubset(new_evidence):
            return False

        return True


# ── Presence TTL ───────────────────────────────────────────────────────────

PRESENCE_TTL_SECONDS = 300  # 5 minutes default freshness window


def compute_freshness(
    observed_at: Optional[str],
    expires_at: Optional[str],
) -> Dict[str, str]:
    """Compute epistemic_state and freshness based on TTL.

    Returns {"epistemic_state": "KNOWN"|"UNKNOWN"|"CONTRADICTED",
              "freshness": "FRESH"|"STALE"|"UNKNOWN"}
    """
    now = datetime.now(timezone.utc)

    if observed_at is None:
        return {"epistemic_state": "UNKNOWN", "freshness": "UNKNOWN"}

    try:
        observed_dt = datetime.fromisoformat(
            observed_at.replace("Z", "+00:00")
        )
    except (ValueError, AttributeError):
        return {"epistemic_state": "UNKNOWN", "freshness": "UNKNOWN"}

    if expires_at is not None:
        try:
            expires_dt = datetime.fromisoformat(
                expires_at.replace("Z", "+00:00")
            )
            is_fresh = expires_dt > now
        except (ValueError, AttributeError):
            is_fresh = False
    else:
        # No explicit expiry; fresh if observed within TTL window
        age_seconds = (now - observed_dt).total_seconds()
        is_fresh = age_seconds <= PRESENCE_TTL_SECONDS

    epistemic = "KNOWN" if is_fresh else "UNKNOWN"
    freshness = "FRESH" if is_fresh else "STALE"

    return {"epistemic_state": epistemic, "freshness": freshness}


# ── Reconnect / Resume ─────────────────────────────────────────────────────

def attempt_reconnect(
    existing_lineage: SessionLineage,
    new_observation: Dict[str, Any],
    envelope: InterFabricEnvelope,
) -> Dict[str, Any]:
    """Attempt session reconnect, preserving identity invariants.

    Returns a result dict with:
      - success: bool
      - preserved_identity: bool
      - new_envelope: InterFabricEnvelope | None
      - reason: str
    """
    # Verify identity preservation
    if not existing_lineage.verify_identity_preserved(
        envelope.to_dict(), new_observation.get("envelope", {})
    ):
        return {
            "success": False,
            "preserved_identity": False,
            "new_envelope": None,
            "reason": "identity_mutation_on_reconnect",
        }

    # Update lineage
    lineage = existing_lineage
    lineage.reconnect_count += 1
    lineage.last_seen_at = datetime.now(timezone.utc)

    # Build new envelope preserving all invariants
    new_raw = envelope.to_dict()
    # Preserve all identity-critical fields; only update payload/realtime data
    new_raw["payload"] = new_observation.get("payload", {})

    try:
        new_envelope = InterFabricEnvelope(new_raw)
        return {
            "success": True,
            "preserved_identity": True,
            "new_envelope": new_envelope,
            "reason": "reconnect_preserved",
        }
    except InterFabricInvariantError as exc:
        return {
            "success": False,
            "preserved_identity": False,
            "new_envelope": None,
            "reason": f"invariant_violation:{exc}",
        }


# ── Protocol negotiation ───────────────────────────────────────────────────

def negotiate_protocol(
    proposed_version: str,
    minimum_supported: str = GATEWAY_PROTOCOL_VERSION,
) -> str:
    """Negotiate protocol version, falling back to minimum supported."""

    # Simple version ordering: major.minor.patch compared lexicographically
    if proposed_version == minimum_supported:
        return proposed_version
    if proposed_version < minimum_supported:
        # Client is behind; bump to minimum
        return minimum_supported
    # Client is ahead; accept but mark for migration
    return proposed_version


# ── Core envelope creation ────────────────────────────────────────────────

def create_gateway_envelope(
    *,
    holon_id: str,
    institutional_rank: str,
    mission_id: str,
    work_id: int,
    cell_id: str,
    correlation_id: str,
    parent_correlation_id: Optional[str],
    capability_id: Optional[str],
    capability_version: Optional[str],
    authority_scope: str,
    policy_ref: str,
    resource_lease_ref: Optional[str],
    budget_lease_ref: Optional[str],
    operation_id: str,
    effect_id: Optional[str],
    effect_class: str,
    idempotency_key: str,
    replay_semantics: str,
    evidence_refs: list[str],
    observed_at: str,
    epistemic_state: str,
    freshness: str,
    origin_layer: str,
    return_to: str,
    payload: Dict[str, Any],
) -> InterFabricEnvelope:
    """Create a minimal Gateway envelope carrying cross-fabric coordinates.

    This reuses the InterFabricEnvelope schema from #471 and does NOT invent
    a second identity system. All fields map directly to existing schema
    positions; no synthetic fields are introduced.
    """
    # Build identity: holon_id + institutional_rank + optional embodiment_ref + session_ref
    identity: Dict[str, Any] = {
        "holon_id": holon_id,
        "institutional_rank": institutional_rank,
    }
    # session_ref is deliberately NOT invariant — a Holon must survive runtime/
    # session replacement without changing identity (per inter_fabric.py line 57-58)

    # Build mission
    mission: Dict[str, Any] = {
        "mission_id": mission_id,
        "work_id": str(work_id),  # schema accepts string|integer
        "cell_id": cell_id,
        "correlation_id": correlation_id,
        "parent_correlation_id": parent_correlation_id,
    }

    # Build capability (may be null)
    capability: Optional[Dict[str, Any]] = None
    if capability_id is not None:
        capability = {
            "capability_id": capability_id,
            "capability_version": capability_version or "v1",
            "contract_ref": None,  # optional, left null for minimal gateway
        }

    # Build authority
    authority: Dict[str, Any] = {
        "authority_scope": authority_scope,
        "policy_ref": policy_ref,
        "policy_version": None,
        "mutation_lease": None,
        "fencing_key": None,
    }

    # Build resource (may be null)
    resource: Optional[Dict[str, Any]] = None
    if resource_lease_ref is not None:
        resource = {
            "resource_lease_ref": resource_lease_ref,
            "budget_lease_ref": budget_lease_ref or None,
        }

    # Build effect
    effect: Dict[str, Any] = {
        "operation_id": operation_id,
        "effect_id": effect_id,
        "effect_class": effect_class,
        "idempotency_key": idempotency_key,
        "replay_semantics": replay_semantics,
    }

    # Build truth
    truth: Dict[str, Any] = {
        "evidence_refs": evidence_refs,
        "observed_at": observed_at,
        "source_authority": "gateway-kernel",  # provenance source
        "freshness": freshness,
        "epistemic_state": epistemic_state,
        "age_seconds": None,  # computed on demand
    }

    # Build routing
    routing: Dict[str, Any] = {
        "origin_layer": origin_layer,
        "return_to": return_to,
        "blocked_outcome": None,
        "recovery_hint": None,
    }

    # Build compatibility
    compatibility: Dict[str, Any] = {
        "envelope_version": "v1",
        "payload_schema": "gateway-kernel-v1",
        "payload_version": GATEWAY_PROTOCOL_VERSION,
        "lossy_fields": [],
    }

    # Construct raw dict — InterFabricEnvelope.__init__ will validate via schema
    raw: Dict[str, Any] = {
        "identity": identity,
        "mission": mission,
        "capability": capability,
        "authority": authority,
        "resource": resource,
        "effect": effect,
        "truth": truth,
        "routing": routing,
        "compatibility": compatibility,
        "payload": payload,
    }

    envelope = InterFabricEnvelope(raw)
    return envelope


# ── Convenience: project presence from envelope ────────────────────────────

def project_presence_from_envelope(
    envelope: InterFabricEnvelope,
) -> Dict[str, Any]:
    """Project agent presence from an InterFabricEnvelope.

    Derives truth state and freshness from the envelope's truth section,
    then projects through the truth projection contract.
    """
    truth = envelope.to_dict().get("truth", {})

    freshness_result = compute_freshness(
        truth.get("observed_at"), truth.get("age_seconds")
    )

    return {
        "schema": "aspace.agent-presence.v1",
        "identity": {
            "holon_id": envelope.to_dict()["identity"]["holon_id"],
            "institutional_rank": envelope.to_dict()["identity"][
                "institutional_rank"
            ],
        },
        "state": freshness_result["epistemic_state"],
        "reason": f"gateway_kernel_freshness:{freshness_result['freshness'].lower()}",
        "observed_at": truth.get("observed_at"),
        "expires_at": None,
        "evidence_refs": truth.get("evidence_refs", []),
        "fencing_lease_identity": envelope.to_dict().get("identity", {}).get(
            "session_ref"
        ),
        "capabilities": envelope.to_dict().get("capability", {}).get(
            "capability_id"
        ),
        "work_id": envelope.to_dict()["mission"]["work_id"],
        "correlation_id": envelope.to_dict()["mission"]["correlation_id"],
        "return_to": envelope.to_dict()["routing"]["return_to"],
    }


# ── Test ──────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Minimal integration test
    envelope = create_gateway_envelope(
        holon_id="Ryan",
        institutional_rank="L2_AGENT",
        mission_id="mission-471",
        work_id=471,
        cell_id="cell-abc",
        correlation_id="corr-471",
        parent_correlation_id=None,
        capability_id="harness.list",
        capability_version="1.0.0",
        authority_scope="L2_READ",
        policy_ref="policy-44",
        resource_lease_ref="resource-5",
        budget_lease_ref="budget-5",
        operation_id="op-88",
        effect_id=None,
        effect_class="READ_ONLY",
        idempotency_key="idem-441",
        replay_semantics="SAFE",
        evidence_refs=["runtime:receipt:1", "prov:22"],
        observed_at=datetime.now(timezone.utc).isoformat(),
        epistemic_state="KNOWN",
        freshness="FRESH",
        origin_layer="Nardole",
        return_to="github:#471",
        payload={"stage": "capability"},
    )

    print("Envelope created successfully")
    print(f"correlation_id: {envelope.get_correlation_id()}")
    print(f"epistemic_state: {envelope.get_epistemic_state()}")
    print(f"holon_id: {envelope.to_dict()['identity']['holon_id']}")

    # Test reconnect preservation
    lineage = SessionLineage(
        correlation_id="corr-471",
        work_id=471,
        return_to="github:#471",
        session_id="sess-991",
    )

    result = attempt_reconnect(
        existing_lineage=lineage,
        new_observation={"envelope": envelope.to_dict(), "payload": {"stage": "resource"}},
        envelope=envelope,
    )

    print(f"\nReconnect result: {result['success']}")
    print(f"Preserved identity: {result['preserved_identity']}")
    print(f"Reason: {result['reason']}")