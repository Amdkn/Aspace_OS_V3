from __future__ import annotations

"""A'Space Gateway v0 — Protocol Core (Issue #543).

This module provides the minimum Gateway kernel that carries existing
A'Space cross-fabric coordinates without inventing a second identity system.

It reuses:
- InterFabricEnvelope.v1 from #471
- Embodied Holon contract from #318
- Temporal Truth / Context Compiler from #448

Core contracts:
- role = operator | holon | runtime | node | surface | worker
- Independent IDs: institutional holon, embodiment, runtime, device/node, surface, session
- Protocol version negotiation
- Correlation/fencing preservation
- Presence freshness/TTL
- Session lineage
- Reconnect/resume
- Delivery ambiguity preserved as UNKNOWN
"""

import json
import os
import time
from typing import Any, Dict, List, Optional

from inter_fabric import InterFabricEnvelope, InterFabricInvariantError
from temporal_truth.core import TemporalTruth


# ============================================================================
# Protocol Roles
# ============================================================================

ROLE_OPERATOR = "operator"
ROLE_HOLON = "holon"
ROLE_RUNTIME = "runtime"
ROLE_NODE = "node"
ROLE_SURFACE = "surface"
ROLE_WORKER = "worker"

VALID_ROLES = {
    ROLE_OPERATOR,
    ROLE_HOLON,
    ROLE_RUNTIME,
    ROLE_NODE,
    ROLE_SURFACE,
    ROLE_WORKER,
}

PROTOCOL_VERSION = "v0.1.0"


# ============================================================================
# Gateway Protocol Error
# ============================================================================

class GatewayProtocolError(ValueError):
    """Raised when a Gateway protocol violation occurs."""


# ============================================================================
# GatewayEnvelope
# ============================================================================

class GatewayEnvelope:
    """Validated Gateway protocol envelope carrying A'Space coordinates.

    This envelope wraps the InterFabricEnvelope and adds protocol-specific
    fields for the Gateway v0 mission (#543+).

    The envelope carries the following structure (augmented from InterFabricEnvelope):
    - identity: institutional holon, embodiment, runtime, device, surface, session IDs
    - mission: mission_id, work_id, cell_id, correlation_id, parent_correlation_id
    - capability: capability_id, capability_version, contract_ref
    - authority: authority_scope, policy_ref, fencing_key
    - resource: resource_lease_ref, budget_lease_ref
    - effect: operation_id, effect_id, effect_class, idempotency_key, replay_semantics
    - truth: evidence_refs, observed_at, source_authority, freshness, epistemic_state
    - routing: origin_layer, return_to, blocked_outcome, recovery_hint
    - compatibility: envelope_version, payload_schema, payload_version, lossy_fields
    - protocol: protocol_version, role, session_lineage
    - payload: fabric-specific payload
    """

    def __init__(
        self,
        raw: Dict[str, Any],
        *,
        validate: bool = True,
    ):
        self.raw = raw
        if validate:
            self.validate(raw)

    @classmethod
    def validate(cls, instance: Dict[str, Any]) -> None:
        """Validate the Gateway envelope against its extended schema.

        Validates both the core InterFabricEnvelope coordinates AND the
        protocol-specific fields. The protocol fields are allowed as an
        additional property since they are not part of the original
        InterFabricEnvelope schema.
        """
        _validate_inter_fabric_core_only(instance)
        cls._validate_protocol_fields(instance)

    @staticmethod
    def _validate_protocol_fields(instance: Dict[str, Any]) -> None:
        """Validate protocol-specific fields beyond InterFabricEnvelope invariants."""
        protocol_section = instance.get("protocol", {})
        role = protocol_section.get("role", "")
        if role not in VALID_ROLES:
            raise GatewayProtocolError(
                f"Invalid protocol role: {role!r}. "
                f"Must be one of: {sorted(VALID_ROLES)}"
            )

        protocol_version = protocol_section.get("protocol_version", "")
        if protocol_version != PROTOCOL_VERSION:
            raise GatewayProtocolError(
                f"Protocol version mismatch: {protocol_version!r} != {PROTOCOL_VERSION!r}"
            )

        if role in (ROLE_HOLON, ROLE_OPERATOR):
            session_lineage = protocol_section.get("session_lineage", None)
            if session_lineage is None:
                raise GatewayProtocolError(
                    f"Session lineage required for role {role} but missing"
                )

        freshness = instance["truth"].get("freshness", None)
        if freshness not in ("FRESH", "STALE", "UNKNOWN"):
            raise GatewayProtocolError(
                f"Invalid freshness state: {freshness!r}. "
                f"Must be one of: FRESH, STALE, UNKNOWN"
            )

        return_to = instance["routing"].get("return_to", "")
        if not return_to:
            raise GatewayProtocolError("return_to is required and must be non-empty")

        correlation_id = instance["mission"].get("correlation_id", "")
        if not correlation_id:
            raise GatewayProtocolError("correlation_id is required and must be non-empty")

    @classmethod
    def create(
        cls,
        *,
        identity: Dict[str, Any],
        mission: Dict[str, Any],
        capability: Dict[str, Any] | None,
        authority: Dict[str, Any],
        resource: Dict[str, Any] | None,
        effect: Dict[str, Any] | None,
        truth: Dict[str, Any],
        routing: Dict[str, Any],
        compatibility: Dict[str, Any],
        payload: Dict[str, Any],
        protocol_role: str,
        protocol_version: str | None = None,
        session_lineage: List[str] | None = None,
    ) -> "GatewayEnvelope":
        """Create a validated GatewayEnvelope from component parts."""
        envelope = InterFabricEnvelope.create(
            identity=identity,
            mission=mission,
            capability=capability,
            authority=authority,
            resource=resource,
            effect=effect,
            truth=truth,
            routing=routing,
            compatibility=compatibility,
            payload=payload,
        )

        new_raw = envelope.to_dict()
        new_raw["protocol"] = {
            "protocol_version": protocol_version or PROTOCOL_VERSION,
            "role": protocol_role,
        }
        if session_lineage is not None:
            new_raw["protocol"]["session_lineage"] = session_lineage
        elif protocol_role in (ROLE_HOLON, ROLE_OPERATOR):
            new_raw["protocol"]["session_lineage"] = []

        cls.validate(new_raw)
        return cls(new_raw)

    def to_dict(self) -> Dict[str, Any]:
        """Return the raw envelope dict."""
        return self.raw

    def get_correlation_id(self) -> str:
        """Return the mission correlation_id."""
        return self.raw["mission"]["correlation_id"]

    def get_epistemic_state(self) -> str:
        """Return the truth epistemic_state."""
        return self.raw["truth"]["epistemic_state"]

    def get_freshness(self) -> str:
        """Return the truth freshness."""
        return self.raw["truth"]["freshness"]

    def get_return_to(self) -> str:
        """Return the routing return_to."""
        return self.raw["routing"]["return_to"]

    def get_role(self) -> str:
        """Return the protocol role."""
        return self.raw["protocol"]["role"]

    def get_session_lineage(self) -> List[str] | None:
        """Return the session lineage."""
        return self.raw["protocol"].get("session_lineage")

    def clone_with_payload(
        self,
        new_payload: Dict[str, Any],
        *,
        allow_truth_resolution: bool = False,
    ) -> "GatewayEnvelope":
        """Clone the envelope with a new payload, preserving all invariants."""
        return GatewayEnvelope.create(
            identity=self.raw["identity"],
            mission=self.raw["mission"],
            capability=self.raw.get("capability"),
            authority=self.raw["authority"],
            resource=self.raw.get("resource"),
            effect=self.raw.get("effect"),
            truth=self.raw["truth"],
            routing=self.raw["routing"],
            compatibility=self.raw["compatibility"],
            payload=new_payload,
            protocol_role=self.raw["protocol"]["role"],
            protocol_version=self.raw["protocol"].get("protocol_version"),
            session_lineage=self.raw["protocol"].get("session_lineage"),
        )


def _validate_inter_fabric_core_only(instance: Dict[str, Any]) -> None:
    """Validate only the InterFabricEnvelope core, ignoring additional properties."""
    import jsonschema

    schema_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "contracts",
        "INTER_FABRIC_ENVELOPE_V1.schema.json",
    )

    with open(schema_path, "r", encoding="utf-8") as handle:
        schema = json.load(handle)

    original_additional = schema.get("additionalProperties", False)
    schema["additionalProperties"] = True

    try:
        jsonschema.validate(instance=instance, schema=schema)
    finally:
        schema["additionalProperties"] = original_additional


# ============================================================================
# from_inter_fabric_envelope convenience function
# ============================================================================

def from_inter_fabric_envelope(
    envelope: InterFabricEnvelope,
    *,
    role: str,
    session_lineage: List[str] | None = None,
) -> GatewayEnvelope:
    """Convert an InterFabricEnvelope to a GatewayEnvelope."""
    raw = envelope.to_dict()

    gateway = GatewayEnvelope.create(
        identity=raw["identity"],
        mission=raw["mission"],
        capability=raw.get("capability"),
        authority=raw["authority"],
        resource=raw.get("resource"),
        effect=raw.get("effect"),
        truth=raw["truth"],
        routing=raw["routing"],
        compatibility=raw["compatibility"],
        payload=raw["payload"],
        protocol_role=role,
        session_lineage=session_lineage if session_lineage is not None else [],
    )

    return gateway


# ============================================================================
# Presence Model
# ============================================================================

class PresenceModel:
    """Multi-axis presence model for Gateway v0."""

    PRESENCE_STATES = {
        "institutional_state": ("ACTIVE", "SUSPENDED", "ARCHIVED"),
        "embodiment_state": ("READY", "DEGRADED", "MISSING"),
        "runtime_state": ("ONLINE", "OFFLINE", "UNSTABLE", "UNKNOWN"),
        "workload_state": ("IDLE", "QUEUED", "WORKING", "BLOCKED", "REVIEW"),
    }

    def __init__(
        self,
        institutional_state: str = "ARCHIVED",
        embodiment_state: str = "MISSING",
        runtime_state: str = "UNKNOWN",
        workload_state: str = "IDLE",
        observed_at: str | None = None,
        provenance: str | None = None,
    ):
        self.institutional_state = self._validate_state(
            "institutional_state", institutional_state, self.PRESENCE_STATES["institutional_state"]
        )
        self.embodiment_state = self._validate_state(
            "embodiment_state", embodiment_state, self.PRESENCE_STATES["embodiment_state"]
        )
        self.runtime_state = self._validate_state(
            "runtime_state", runtime_state, self.PRESENCE_STATES["runtime_state"]
        )
        self.workload_state = self._validate_state(
            "workload_state", workload_state, self.PRESENCE_STATES["workload_state"]
        )
        self.observed_at = observed_at or time.strftime(
            "%Y-%m-%dT%H:%M:%SZ", time.gmtime()
        )
        self.provenance = provenance

    @staticmethod
    def _validate_state(
        name: str, value: str, valid: tuple[str, ...]
    ) -> str:
        if value not in valid:
            raise GatewayProtocolError(
                f"Invalid {name}: {value!r}. Must be one of: {valid}"
            )
        return value

    def to_dict(self) -> Dict[str, Any]:
        return {
            "institutional_state": self.institutional_state,
            "embodiment_state": self.embodiment_state,
            "runtime_state": self.runtime_state,
            "workload_state": self.workload_state,
            "observed_at": self.observed_at,
            "provenance": self.provenance,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PresenceModel":
        return cls(
            institutional_state=data.get("institutional_state", "ARCHIVED"),
            embodiment_state=data.get("embodiment_state", "MISSING"),
            runtime_state=data.get("runtime_state", "UNKNOWN"),
            workload_state=data.get("workload_state", "IDLE"),
            observed_at=data.get("observed_at"),
            provenance=data.get("provenance"),
        )


# ============================================================================
# Session Lineage
# ============================================================================

class SessionLineage:
    """Tracks session lineage for reconnect/resume operations."""

    def __init__(
        self,
        current_session_id: str,
        previous_session_ids: List[str] | None = None,
        first_seen_at: str | None = None,
        last_seen_at: str | None = None,
        return_to: str | None = None,
    ):
        self.current_session_id = current_session_id
        self.previous_session_ids = previous_session_ids or []
        self.first_seen_at = first_seen_at or time.strftime(
            "%Y-%m-%dT%H:%M:%SZ", time.gmtime()
        )
        self.last_seen_at = last_seen_at or self.first_seen_at
        self.return_to = return_to

    def to_dict(self) -> Dict[str, Any]:
        return {
            "current_session_id": self.current_session_id,
            "previous_session_ids": self.previous_session_ids,
            "first_seen_at": self.first_seen_at,
            "last_seen_at": self.last_seen_at,
            "return_to": self.return_to,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SessionLineage":
        return cls(
            current_session_id=data["current_session_id"],
            previous_session_ids=data.get("previous_session_ids", []),
            first_seen_at=data.get("first_seen_at"),
            last_seen_at=data.get("last_seen_at"),
            return_to=data.get("return_to"),
        )

    def add_previous(self, session_id: str) -> None:
        if session_id not in self.previous_session_ids:
            self.previous_session_ids.append(session_id)
        self.last_seen_at = time.strftime(
            "%Y-%m-%dT%H:%M:%SZ", time.gmtime()
        )


# ============================================================================
# Protocol Negotiation
# ============================================================================

class ProtocolNegotiation:
    """Handles protocol version negotiation between Gateway endpoints."""

    KNOWN_VERSIONS = {
        PROTOCOL_VERSION: {
            "role_support": {
                ROLE_OPERATOR,
                ROLE_HOLON,
                ROLE_RUNTIME,
                ROLE_NODE,
                ROLE_SURFACE,
                ROLE_WORKER,
            },
            "features": {
                "presence_axes": True,
                "session_lineage": True,
                "correlation_preservation": True,
                "fencing_enforcement": True,
                "unknown_delivery": True,
            },
        },
        "v0.0.1": {
            "role_support": {ROLE_OPERATOR, ROLE_HOLON},
            "features": {
                "presence_axes": False,
                "session_lineage": False,
                "correlation_preservation": True,
                "fencing_enforcement": False,
                "unknown_delivery": False,
            },
        },
    }

    @classmethod
    def negotiate(
        cls,
        proposed_version: str,
        required_features: set[str] | None = None,
    ) -> tuple[str, bool]:
        if proposed_version in cls.KNOWN_VERSIONS:
            version_info = cls.KNOWN_VERSIONS[proposed_version]
            if required_features:
                missing = required_features - version_info["features"].keys()
                if missing:
                    return ("v0.0.1", False)
            return (proposed_version, True)

        for version in sorted(cls.KNOWN_VERSIONS.keys(), reverse=True):
            if version != proposed_version:
                version_info = cls.KNOWN_VERSIONS[version]
                if required_features:
                    missing = required_features - version_info["features"].keys()
                    if not missing:
                        return (version, True)
                return (version, True)

        return ("v0.0.1", False)

    @classmethod
    def check_feature_support(
        cls,
        version: str,
        feature: str,
    ) -> bool:
        if version not in cls.KNOWN_VERSIONS:
            return False
        return feature in cls.KNOWN_VERSIONS[version]["features"]


# ============================================================================
# Deliver Ambiguity
# ============================================================================

def preserve_delivery_ambiguity(
    envelope: GatewayEnvelope,
) -> str:
    """Preserve delivery ambiguity as UNKNOWN when truth cannot be established."""
    epistemic_state = envelope.get_epistemic_state()
    if epistemic_state == "UNKNOWN":
        return "UNKNOWN"
    return envelope.get_freshness()


# ============================================================================
# Minimal Envelope Constructor
# ============================================================================

def minimal_envelope(
    *,
    holon_id: str,
    work_id: int,
    correlation_id: str,
    capability_id: str | None = None,
    capability_version: str | None = None,
    authority_scope: str = "READ_ONLY",
    policy_ref: str = "github:#543",
    return_to: str,
    role: str = ROLE_HOLON,
) -> GatewayEnvelope:
    """Construct a minimal GatewayEnvelope for testing and examples."""
    from datetime import datetime, timezone

    now = datetime.now(timezone.utc).isoformat()

    identity = {
        "holon_id": holon_id,
        "institutional_rank": "L2_AGENT",
        "embodiment_ref": None,
        "session_ref": None,
    }

    mission = {
        "mission_id": f"mission-{correlation_id}",
        "work_id": str(work_id),
        "cell_id": f"cell-{correlation_id}",
        "correlation_id": correlation_id,
        "parent_correlation_id": None,
    }

    capability = None
    if capability_id:
        capability = {
            "capability_id": capability_id,
            "capability_version": capability_version or "0.1.0",
            "contract_ref": None,
        }

    authority = {
        "authority_scope": authority_scope,
        "policy_ref": policy_ref,
        "policy_version": "v1",
        "mutation_lease": None,
        "fencing_key": None,
    }

    resource = {
        "resource_lease_ref": None,
        "budget_lease_ref": None,
    }

    effect = None

    truth = {
        "evidence_refs": [f"receipt:{correlation_id}"],
        "observed_at": now,
        "source_authority": authority_scope,
        "freshness": "FRESH",
        "epistemic_state": "KNOWN",
        "age_seconds": None,
    }

    routing = {
        "origin_layer": "Gateway",
        "return_to": return_to,
        "blocked_outcome": None,
        "recovery_hint": "preserve-unknown",
    }

    compatibility = {
        "envelope_version": "v1",
        "payload_schema": "aspace.dc.payload.v1",
        "payload_version": "1.0.0",
        "lossy_fields": [],
    }

    return GatewayEnvelope.create(
        identity=identity,
        mission=mission,
        capability=capability,
        authority=authority,
        resource=resource,
        effect=effect,
        truth=truth,
        routing=routing,
        compatibility=compatibility,
        payload={},
        protocol_role=role,
        session_lineage=[] if role in (ROLE_HOLON, ROLE_OPERATOR) else None,
    )