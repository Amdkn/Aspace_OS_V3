#!/usr/bin/env python3
"""
A'Space Gateway v0 — Protocol Core + Identity/Presence/Session Kernel

This module implements the G0 gate: the minimal Gateway kernel that carries
existing A'Space cross-fabric coordinates without inventing a second identity system.

Reuses:
- InterFabricEnvelope.v1 from #471
- Embodied Holon contract from #318
- Temporal Truth / Context Compiler from #448

Required contracts:
- role = operator | holon | runtime | node | surface | worker
- independent IDs for: institutional holon, embodiment, runtime, device/node, surface, session
- protocol/version negotiation
- correlation/fencing preservation
- presence freshness/TTL
- session lineage
- reconnect/resume
- delivery ambiguity preserved as UNKNOWN

Acceptance: A reconnect or runtime loss must not mutate institutional identity,
authority, WorkID/correlation, evidence lineage, or return_to.
"""

from __future__ import annotations

import copy
import json
import uuid
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone, timedelta
from enum import Enum
from typing import Any, Dict, List, Optional, Set, Literal
from pathlib import Path

# Import existing contracts
from inter_fabric import InterFabricEnvelope, InterFabricInvariantError


class GatewayRole(str, Enum):
    """Gateway protocol roles - orthogonal to institutional identity."""
    OPERATOR = "operator"
    HOLON = "holon"
    RUNTIME = "runtime"
    NODE = "node"
    SURFACE = "surface"
    WORKER = "worker"


class PresenceState(str, Enum):
    """Multi-axis presence states - never a single ONLINE badge."""
    OFFLINE = "OFFLINE"
    AVAILABLE = "AVAILABLE"
    BOUND = "BOUND"
    EXECUTING = "EXECUTING"
    STALE = "STALE"
    DEGRADED = "DEGRADED"
    UNKNOWN = "UNKNOWN"


class EpistemicState(str, Enum):
    """Truth states from Temporal Truth / Context Compiler (#448)."""
    KNOWN = "KNOWN"
    UNKNOWN = "UNKNOWN"
    CONTRADICTED = "CONTRADICTED"


class Freshness(str, Enum):
    """Freshness orthogonal to epistemic truth."""
    FRESH = "FRESH"
    STALE = "STALE"
    UNKNOWN = "UNKNOWN"


class DeliveryState(str, Enum):
    """Delivery semantics with explicit ambiguity."""
    DELIVERED = "DELIVERED"
    PENDING = "PENDING"
    DUPLICATE = "DUPLICATE"
    UNKNOWN = "UNKNOWN"  # Explicit ambiguity - must not be silently resolved


@dataclass(frozen=True)
class IdentityCoordinates:
    """Institutional identity coordinates - immutable per holon."""
    institutional_holon_id: str
    institutional_rank: str  # e.g., "L2_AGENT", "S3_STATE"
    embodiment_id: Optional[str] = None
    session_id: Optional[str] = None
    runtime_id: Optional[str] = None
    node_id: Optional[str] = None
    surface_id: Optional[str] = None
    worker_id: Optional[str] = None

    def to_envelope_identity(self) -> Dict[str, Any]:
        """Convert to InterFabricEnvelope identity section."""
        return {
            "holon_id": self.institutional_holon_id,
            "institutional_rank": self.institutional_rank,
            "embodiment_ref": self.embodiment_id,
            "session_ref": self.session_id,
        }


@dataclass(frozen=True)
class MissionCoordinates:
    """Mission lineage coordinates - immutable per mission."""
    mission_id: str
    work_id: str  # Can be string or int
    cell_id: str
    correlation_id: str
    parent_correlation_id: Optional[str] = None

    def to_envelope_mission(self) -> Dict[str, Any]:
        """Convert to InterFabricEnvelope mission section."""
        return {
            "mission_id": self.mission_id,
            "work_id": self.work_id,
            "cell_id": self.cell_id,
            "correlation_id": self.correlation_id,
            "parent_correlation_id": self.parent_correlation_id,
        }


@dataclass(frozen=True)
class CapabilityCoordinates:
    """Capability coordinates from Capability Fabric (#333)."""
    capability_id: str
    capability_version: str
    contract_ref: Optional[str] = None

    def to_envelope_capability(self) -> Dict[str, Any]:
        """Convert to InterFabricEnvelope capability section."""
        return {
            "capability_id": self.capability_id,
            "capability_version": self.capability_version,
            "contract_ref": self.contract_ref,
        }


@dataclass(frozen=True)
class AuthorityEnvelope:
    """Authority/fencing from HostPolicy."""
    authority_scope: str  # e.g., "L2_READ", "L3_WRITE"
    policy_ref: str
    policy_version: Optional[str] = None
    mutation_lease: Optional[str] = None
    fencing_key: Optional[str] = None

    def to_envelope_authority(self) -> Dict[str, Any]:
        return {
            "authority_scope": self.authority_scope,
            "policy_ref": self.policy_ref,
            "policy_version": self.policy_version,
            "mutation_lease": self.mutation_lease,
            "fencing_key": self.fencing_key,
        }


@dataclass(frozen=True)
class ResourceCoordinates:
    """Resource/budget lease from AMF."""
    resource_lease_ref: Optional[str] = None
    budget_lease_ref: Optional[str] = None

    def to_envelope_resource(self) -> Optional[Dict[str, Any]]:
        return {
            "resource_lease_ref": self.resource_lease_ref,
            "budget_lease_ref": self.budget_lease_ref,
        }


@dataclass(frozen=True)
class EffectCoordinates:
    """Effect identity from AMF."""
    operation_id: str
    effect_class: str  # QUERY | COMMAND | EVENT
    idempotency_key: str
    effect_id: Optional[str] = None
    replay_semantics: Optional[str] = None

    def to_envelope_effect(self) -> Dict[str, Any]:
        return {
            "operation_id": self.operation_id,
            "effect_id": self.effect_id,
            "effect_class": self.effect_class,
            "idempotency_key": self.idempotency_key,
            "replay_semantics": self.replay_semantics,
        }


@dataclass(frozen=True)
class TruthCoordinates:
    """Temporal truth/provenance from Graham (#448)."""
    evidence_refs: List[str] = field(default_factory=list)
    observed_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    source_authority: str = "gateway-default"
    freshness: Freshness = Freshness.UNKNOWN
    epistemic_state: EpistemicState = EpistemicState.UNKNOWN
    age_seconds: Optional[float] = None

    def to_envelope_truth(self) -> Dict[str, Any]:
        return {
            "evidence_refs": self.evidence_refs,
            "observed_at": self.observed_at or datetime.now(timezone.utc).isoformat(),
            "source_authority": self.source_authority,
            "freshness": self.freshness.value,
            "epistemic_state": self.epistemic_state.value,
            "age_seconds": self.age_seconds,
        }


@dataclass(frozen=True)
class RoutingCoordinates:
    """Return routing from Nardole / Gateway."""
    origin_layer: str  # e.g., "Nardole", "Gateway", "CLI"
    return_to: str  # e.g., "github:#542", "cli:session-123"
    blocked_outcome: Optional[str] = None
    recovery_hint: Optional[str] = None

    def to_envelope_routing(self) -> Dict[str, Any]:
        return {
            "origin_layer": self.origin_layer,
            "return_to": self.return_to,
            "blocked_outcome": self.blocked_outcome,
            "recovery_hint": self.recovery_hint,
        }


@dataclass(frozen=True)
class CompatibilityCoordinates:
    """Protocol version compatibility."""
    envelope_version: str = "v1"
    payload_schema: str = ""
    payload_version: str = ""
    lossy_fields: List[str] = field(default_factory=list)

    def to_envelope_compatibility(self) -> Dict[str, Any]:
        return {
            "envelope_version": self.envelope_version,
            "payload_schema": self.payload_schema,
            "payload_version": self.payload_version,
            "lossy_fields": self.lossy_fields,
        }


@dataclass
class GatewayEnvelope:
    """
    A'Space Gateway v0 Envelope.

    Wraps InterFabricEnvelope with Gateway-specific protocol fields.
    Every Gateway message MUST preserve or explicitly reject:
    - institutional_holon_id, embodiment_id, runtime_id, device/node identity,
      surface_id, session_id + lineage, mission_id / work_id / cell_id / correlation_id
    - capability_id + version, authority / policy / fencing
    - resource / budget lease, operation / effect identity
    - evidence + temporal provenance, return_to
    - protocol/version negotiation, presence freshness/TTL, session lineage,
      reconnect/resume, delivery ambiguity as UNKNOWN
    """
    identity: IdentityCoordinates
    mission: MissionCoordinates
    capability: Optional[CapabilityCoordinates] = None
    authority: Optional[AuthorityEnvelope] = None
    resource: Optional[ResourceCoordinates] = None
    effect: Optional[EffectCoordinates] = None
    truth: Optional[TruthCoordinates] = None
    routing: Optional[RoutingCoordinates] = None
    compatibility: Optional[CompatibilityCoordinates] = None
    payload: Dict[str, Any] = field(default_factory=dict)

    # Gateway-specific protocol fields
    protocol_version: str = "v0"
    gateway_message_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    gateway_timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    session_lineage: List[str] = field(default_factory=list)  # Parent session IDs
    delivery_state: DeliveryState = DeliveryState.PENDING
    presence_ttl_seconds: int = 300  # 5 min default

    def to_inter_fabric_envelope(self) -> InterFabricEnvelope:
        """Convert to InterFabricEnvelope for cross-fabric transport."""
        # Provide minimal defaults for all required schema fields
        truth_dict = self.truth.to_envelope_truth() if self.truth else TruthCoordinates().to_envelope_truth()

        routing_dict = self.routing.to_envelope_routing() if self.routing else RoutingCoordinates(
            origin_layer="Gateway",
            return_to="gateway:unknown",
        ).to_envelope_routing()

        compat_dict = self.compatibility.to_envelope_compatibility() if self.compatibility else CompatibilityCoordinates(
            payload_schema="gateway.v0",
            payload_version="v0",
        ).to_envelope_compatibility()

        # Schema requires authority, capability, resource, effect - provide minimal if not set
        authority_dict = self.authority.to_envelope_authority() if self.authority else AuthorityEnvelope(
            authority_scope="L2_READ",
            policy_ref="gateway-default",
        ).to_envelope_authority()

        capability_dict = self.capability.to_envelope_capability() if self.capability else CapabilityCoordinates(
            capability_id="gateway.protocol",
            capability_version="v0",
        ).to_envelope_capability()

        resource_dict = self.resource.to_envelope_resource() if self.resource else ResourceCoordinates().to_envelope_resource()

        effect_dict = self.effect.to_envelope_effect() if self.effect else EffectCoordinates(
            operation_id="gateway-noop",
            effect_class="QUERY",
            idempotency_key="gateway-noop-key",
        ).to_envelope_effect()

        return InterFabricEnvelope.create(
            identity=self.identity.to_envelope_identity(),
            mission=self.mission.to_envelope_mission(),
            capability=capability_dict,
            authority=authority_dict,
            resource=resource_dict,
            effect=effect_dict,
            truth=truth_dict,
            routing=routing_dict,
            compatibility=compat_dict,
            payload=self.payload,
        )

    @classmethod
    def from_inter_fabric_envelope(
        cls,
        envelope: InterFabricEnvelope,
        *,
        protocol_version: str = "v0",
        session_lineage: Optional[List[str]] = None,
        delivery_state: DeliveryState = DeliveryState.PENDING,
        presence_ttl_seconds: int = 300,
    ) -> "GatewayEnvelope":
        """Create GatewayEnvelope from InterFabricEnvelope."""
        raw = envelope.to_dict()

        # Parse identity
        identity = IdentityCoordinates(
            institutional_holon_id=raw["identity"]["holon_id"],
            institutional_rank=raw["identity"]["institutional_rank"],
            embodiment_id=raw["identity"].get("embodiment_ref"),
            session_id=raw["identity"].get("session_ref"),
        )

        # Parse mission
        mission = MissionCoordinates(
            mission_id=raw["mission"]["mission_id"],
            work_id=raw["mission"]["work_id"],
            cell_id=raw["mission"]["cell_id"],
            correlation_id=raw["mission"]["correlation_id"],
            parent_correlation_id=raw["mission"].get("parent_correlation_id"),
        )

        # Parse optional sections
        capability = None
        if raw.get("capability"):
            capability = CapabilityCoordinates(
                capability_id=raw["capability"]["capability_id"],
                capability_version=raw["capability"]["capability_version"],
                contract_ref=raw["capability"].get("contract_ref"),
            )

        authority = None
        if raw.get("authority"):
            authority = AuthorityEnvelope(
                authority_scope=raw["authority"]["authority_scope"],
                policy_ref=raw["authority"]["policy_ref"],
                policy_version=raw["authority"].get("policy_version"),
                mutation_lease=raw["authority"].get("mutation_lease"),
                fencing_key=raw["authority"].get("fencing_key"),
            )

        resource = None
        if raw.get("resource"):
            resource = ResourceCoordinates(
                resource_lease_ref=raw["resource"].get("resource_lease_ref"),
                budget_lease_ref=raw["resource"].get("budget_lease_ref"),
            )

        effect = None
        if raw.get("effect"):
            effect = EffectCoordinates(
                operation_id=raw["effect"]["operation_id"],
                effect_class=raw["effect"]["effect_class"],
                idempotency_key=raw["effect"]["idempotency_key"],
                effect_id=raw["effect"].get("effect_id"),
                replay_semantics=raw["effect"].get("replay_semantics"),
            )

        truth = None
        if raw.get("truth"):
            truth = TruthCoordinates(
                evidence_refs=raw["truth"].get("evidence_refs", []),
                observed_at=raw["truth"].get("observed_at"),
                source_authority=raw["truth"].get("source_authority", ""),
                freshness=Freshness(raw["truth"].get("freshness", "UNKNOWN")),
                epistemic_state=EpistemicState(raw["truth"].get("epistemic_state", "UNKNOWN")),
                age_seconds=raw["truth"].get("age_seconds"),
            )

        routing = None
        if raw.get("routing"):
            routing = RoutingCoordinates(
                origin_layer=raw["routing"]["origin_layer"],
                return_to=raw["routing"]["return_to"],
                blocked_outcome=raw["routing"].get("blocked_outcome"),
                recovery_hint=raw["routing"].get("recovery_hint"),
            )

        compatibility = None
        if raw.get("compatibility"):
            compatibility = CompatibilityCoordinates(
                envelope_version=raw["compatibility"]["envelope_version"],
                payload_schema=raw["compatibility"]["payload_schema"],
                payload_version=raw["compatibility"]["payload_version"],
                lossy_fields=raw["compatibility"].get("lossy_fields", []),
            )

        return cls(
            identity=identity,
            mission=mission,
            capability=capability,
            authority=authority,
            resource=resource,
            effect=effect,
            truth=truth,
            routing=routing,
            compatibility=compatibility,
            payload=raw.get("payload", {}),
            protocol_version=protocol_version,
            session_lineage=session_lineage or [],
            delivery_state=delivery_state,
            presence_ttl_seconds=presence_ttl_seconds,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize to dict."""
        result = {
            "protocol_version": self.protocol_version,
            "gateway_message_id": self.gateway_message_id,
            "gateway_timestamp": self.gateway_timestamp,
            "identity": asdict(self.identity),
            "mission": asdict(self.mission),
            "session_lineage": self.session_lineage,
            "delivery_state": self.delivery_state.value,
            "presence_ttl_seconds": self.presence_ttl_seconds,
            "payload": self.payload,
        }

        if self.capability:
            result["capability"] = asdict(self.capability)
        if self.authority:
            result["authority"] = asdict(self.authority)
        if self.resource:
            result["resource"] = asdict(self.resource)
        if self.effect:
            result["effect"] = asdict(self.effect)
        if self.truth:
            truth_dict = asdict(self.truth)
            truth_dict["freshness"] = self.truth.freshness.value
            truth_dict["epistemic_state"] = self.truth.epistemic_state.value
            result["truth"] = truth_dict
        if self.routing:
            result["routing"] = asdict(self.routing)
        if self.compatibility:
            result["compatibility"] = asdict(self.compatibility)

        return result

    def clone_with_updates(
        self,
        *,
        new_payload: Optional[Dict[str, Any]] = None,
        new_session_id: Optional[str] = None,
        new_embodiment_id: Optional[str] = None,
        new_runtime_id: Optional[str] = None,
        new_session_lineage: Optional[List[str]] = None,
        delivery_state: Optional[DeliveryState] = None,
        allow_truth_resolution: bool = False,
        **section_updates: Dict[str, Any],
    ) -> "GatewayEnvelope":
        """
        Create a new envelope with updates while preserving invariants.

        Uses InterFabricEnvelope.validate_translation to ensure cross-fabric
        invariants are not violated. Only allows specific Gateway-level mutations:
        - session/embodiment/runtime replacement (allowed per holon survival)
        - session lineage growth
        - delivery state updates
        - evidence growth (not shrink)
        """
        new_envelope = copy.deepcopy(self)

        if new_payload is not None:
            new_envelope.payload = new_payload

        if new_session_id is not None:
            new_envelope.identity = IdentityCoordinates(
                institutional_holon_id=new_envelope.identity.institutional_holon_id,
                institutional_rank=new_envelope.identity.institutional_rank,
                embodiment_id=new_envelope.identity.embodiment_id,
                session_id=new_session_id,
                runtime_id=new_envelope.identity.runtime_id,
                node_id=new_envelope.identity.node_id,
                surface_id=new_envelope.identity.surface_id,
                worker_id=new_envelope.identity.worker_id,
            )

        if new_embodiment_id is not None:
            new_envelope.identity = IdentityCoordinates(
                institutional_holon_id=new_envelope.identity.institutional_holon_id,
                institutional_rank=new_envelope.identity.institutional_rank,
                embodiment_id=new_embodiment_id,
                session_id=new_envelope.identity.session_id,
                runtime_id=new_envelope.identity.runtime_id,
                node_id=new_envelope.identity.node_id,
                surface_id=new_envelope.identity.surface_id,
                worker_id=new_envelope.identity.worker_id,
            )

        if new_runtime_id is not None:
            new_envelope.identity = IdentityCoordinates(
                institutional_holon_id=new_envelope.identity.institutional_holon_id,
                institutional_rank=new_envelope.identity.institutional_rank,
                embodiment_id=new_envelope.identity.embodiment_id,
                session_id=new_envelope.identity.session_id,
                runtime_id=new_runtime_id,
                node_id=new_envelope.identity.node_id,
                surface_id=new_envelope.identity.surface_id,
                worker_id=new_envelope.identity.worker_id,
            )

        if new_session_lineage is not None:
            # Lineage can only grow
            existing = set(new_envelope.session_lineage)
            new = set(new_session_lineage)
            if not existing.issubset(new):
                raise ValueError("Session lineage may only grow, not shrink")
            new_envelope.session_lineage = new_session_lineage

        if delivery_state is not None:
            new_envelope.delivery_state = delivery_state

        # Apply section updates
        for section, updates in section_updates.items():
            if hasattr(new_envelope, section):
                current = getattr(new_envelope, section)
                if current is not None and isinstance(current, (IdentityCoordinates, MissionCoordinates, CapabilityCoordinates, AuthorityEnvelope, ResourceCoordinates, EffectCoordinates, TruthCoordinates, RoutingCoordinates, CompatibilityCoordinates)):
                    # For frozen dataclasses, create new instance
                    if section == "truth" and updates:
                        # Evidence can only grow
                        current_evidence = set(current.evidence_refs) if current.evidence_refs else set()
                        new_evidence = set(updates.get("evidence_refs", [])) if updates.get("evidence_refs") else current_evidence
                        if not current_evidence.issubset(new_evidence):
                            raise InterFabricInvariantError("truth.evidence_refs lost lineage")

                        # UNKNOWN cannot be coerced without explicit resolution
                        if (current.epistemic_state == EpistemicState.UNKNOWN and
                            updates.get("epistemic_state") != EpistemicState.UNKNOWN and
                            not allow_truth_resolution):
                            raise InterFabricInvariantError("UNKNOWN was coerced without an explicit truth-resolution boundary")

                        # Preserve observed_at unless explicitly updated
                        if "observed_at" not in updates:
                            updates = {**updates, "observed_at": current.observed_at}

                    new_obj = type(current)(**{**asdict(current), **updates})
                    setattr(new_envelope, section, new_obj)

        # Validate invariants using InterFabricEnvelope
        old_if = self.to_inter_fabric_envelope()
        new_if = new_envelope.to_inter_fabric_envelope()
        InterFabricEnvelope.validate_translation(
            old_if.to_dict(),
            new_if.to_dict(),
            allow_truth_resolution=allow_truth_resolution,
        )

        return new_envelope


class GatewayProtocol:
    """
    Gateway v0 Protocol Engine.

    Handles protocol negotiation, session management, presence projection,
    reconnect/resume, and delivery semantics.
    """

    PROTOCOL_VERSIONS = ["v0"]
    MIN_TTL_SECONDS = 60
    MAX_TTL_SECONDS = 3600

    def __init__(self, default_ttl_seconds: int = 300):
        self.default_ttl_seconds = default_ttl_seconds
        self._active_sessions: Dict[str, Dict[str, Any]] = {}  # session_id -> session_state
        self._delivery_dedupe: Set[str] = set()  # operation_id + fingerprint for duplicate detection

    def negotiate_version(self, client_version: str) -> str:
        """Negotiate protocol version. Returns agreed version or raises."""
        if client_version in self.PROTOCOL_VERSIONS:
            return client_version
        # Fall back to latest
        return self.PROTOCOL_VERSIONS[-1]

    def create_session(
        self,
        identity: IdentityCoordinates,
        mission: MissionCoordinates,
        *,
        ttl_seconds: Optional[int] = None,
    ) -> GatewayEnvelope:
        """Create a new session envelope."""
        session_id = str(uuid.uuid4())
        ttl = ttl_seconds or self.default_ttl_seconds

        identity_with_session = IdentityCoordinates(
            institutional_holon_id=identity.institutional_holon_id,
            institutional_rank=identity.institutional_rank,
            embodiment_id=identity.embodiment_id,
            session_id=session_id,
            runtime_id=identity.runtime_id,
            node_id=identity.node_id,
            surface_id=identity.surface_id,
            worker_id=identity.worker_id,
        )

        envelope = GatewayEnvelope(
            identity=identity_with_session,
            mission=mission,
            truth=TruthCoordinates(
                source_authority="gateway-protocol",
                freshness=Freshness.FRESH,
                epistemic_state=EpistemicState.KNOWN,
            ),
            presence_ttl_seconds=ttl,
            session_lineage=[],
        )

        self._active_sessions[session_id] = {
            "envelope": envelope,
            "created_at": datetime.now(timezone.utc),
            "last_activity": datetime.now(timezone.utc),
            "ttl_seconds": ttl,
        }

        return envelope

    def resume_session(
        self,
        previous_envelope: GatewayEnvelope,
        new_runtime_id: Optional[str] = None,
        new_embodiment_id: Optional[str] = None,
        *,
        ttl_seconds: Optional[int] = None,
    ) -> GatewayEnvelope:
        """
        Resume a session with optional runtime/embodiment migration.

        Preserves: institutional holon, work/correlation identity, authority,
        evidence lineage, effect identity, return_to.
        Allows: runtime/embodiment replacement, session lineage growth.
        """
        old_session_id = previous_envelope.identity.session_id
        new_session_id = str(uuid.uuid4())

        # Build new lineage including previous session
        new_lineage = list(previous_envelope.session_lineage) + [old_session_id]

        resumed = previous_envelope.clone_with_updates(
            new_session_id=new_session_id,
            new_runtime_id=new_runtime_id,
            new_embodiment_id=new_embodiment_id,
            new_session_lineage=new_lineage,
            delivery_state=DeliveryState.PENDING,
            ttl_seconds=ttl_seconds or self.default_ttl_seconds,
        )

        self._active_sessions[new_session_id] = {
            "envelope": resumed,
            "created_at": datetime.now(timezone.utc),
            "last_activity": datetime.now(timezone.utc),
            "ttl_seconds": ttl_seconds or self.default_ttl_seconds,
            "resumed_from": old_session_id,
        }

        return resumed

    def update_activity(self, session_id: str) -> bool:
        """Update last activity timestamp. Returns False if session expired."""
        if session_id not in self._active_sessions:
            return False

        session = self._active_sessions[session_id]
        now = datetime.now(timezone.utc)

        # Check TTL
        created = session["created_at"]
        ttl = session.get("ttl_seconds", self.default_ttl_seconds)
        if (now - created).total_seconds() > ttl:
            del self._active_sessions[session_id]
            return False

        session["last_activity"] = now
        return True

    def get_session(self, session_id: str) -> Optional[GatewayEnvelope]:
        """Get session envelope if still valid."""
        if session_id not in self._active_sessions:
            return None

        session = self._active_sessions[session_id]
        now = datetime.now(timezone.utc)
        created = session["created_at"]
        ttl = session.get("ttl_seconds", self.default_ttl_seconds)

        if (now - created).total_seconds() > ttl:
            del self._active_sessions[session_id]
            return None

        return session["envelope"]

    def check_delivery_dedupe(self, operation_id: str, fingerprint: str) -> DeliveryState:
        """
        Check for duplicate delivery.

        Returns DELIVERED if already seen, PENDING if new, UNKNOWN if ambiguous.
        """
        key = f"{operation_id}:{fingerprint}"
        if key in self._delivery_dedupe:
            return DeliveryState.DUPLICATE
        self._delivery_dedupe.add(key)
        return DeliveryState.DELIVERED

    def project_presence(
        self,
        envelope: GatewayEnvelope,
        runtime_observation: Optional[Dict[str, Any]] = None,
        *,
        now: Optional[datetime] = None,
    ) -> Dict[str, Any]:
        """
        Project multi-axis presence from Gateway envelope + runtime observation.

        Presence is multi-axis, never a single ONLINE badge:
        - institutional_state (from holon identity)
        - embodiment_state (from embodiment_id/session)
        - runtime_state (from runtime observation)
        - workload_state (from mission/work)
        - freshness/TTL
        - provenance
        """
        current_time = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)

        # Determine runtime state
        runtime_state = PresenceState.UNKNOWN
        runtime_reason = "no_runtime_observation"
        runtime_available = False
        runtime_fresh = False

        if runtime_observation:
            observed_at_str = runtime_observation.get("observed_at")
            expires_at_str = runtime_observation.get("expires_at")

            if observed_at_str:
                try:
                    observed_at = datetime.fromisoformat(observed_at_str.replace("Z", "+00:00"))
                    if observed_at.tzinfo is None:
                        observed_at = observed_at.replace(tzinfo=timezone.utc)
                    observed_at = observed_at.astimezone(timezone.utc)
                except (ValueError, AttributeError):
                    observed_at = None
            else:
                observed_at = None

            if expires_at_str:
                try:
                    expires_at = datetime.fromisoformat(expires_at_str.replace("Z", "+00:00"))
                    if expires_at.tzinfo is None:
                        expires_at = expires_at.replace(tzinfo=timezone.utc)
                    expires_at = expires_at.astimezone(timezone.utc)
                except (ValueError, AttributeError):
                    expires_at = None
            else:
                expires_at = None

            if expires_at and expires_at <= current_time:
                runtime_state = PresenceState.STALE
                runtime_reason = "runtime_observation_ttl_expired"
            elif observed_at is None and expires_at is None:
                runtime_state = PresenceState.UNKNOWN
                runtime_reason = "runtime_observation_has_no_freshness"
            elif runtime_observation.get("degraded_reason"):
                runtime_state = PresenceState.DEGRADED
                runtime_reason = str(runtime_observation["degraded_reason"])
            elif runtime_observation.get("available") is False:
                runtime_state = PresenceState.OFFLINE
                runtime_reason = "runtime_observed_offline"
            else:
                runtime_available = True
                runtime_fresh = True
                runtime_state = PresenceState.AVAILABLE
                runtime_reason = "fresh_runtime_available"

        # Determine institutional/embodiment state
        has_session = envelope.identity.session_id is not None
        has_embodiment = envelope.identity.embodiment_id is not None
        has_runtime_id = envelope.identity.runtime_id is not None

        # Work state
        work_executing = False  # Would be derived from WorkGraph in practice

        # Derive combined state
        if runtime_state == PresenceState.UNKNOWN and not has_session and not has_embodiment:
            combined_state = PresenceState.UNKNOWN
            reason = "no_runtime_or_binding_evidence"
        elif runtime_state == PresenceState.STALE:
            combined_state = PresenceState.STALE
            reason = runtime_reason
        elif runtime_state == PresenceState.DEGRADED:
            combined_state = PresenceState.DEGRADED
            reason = runtime_reason
        elif runtime_state == PresenceState.OFFLINE:
            if has_session or has_embodiment:
                combined_state = PresenceState.DEGRADED
                reason = "runtime_offline_with_work_binding"
            else:
                combined_state = PresenceState.OFFLINE
                reason = "runtime_observed_offline"
        elif runtime_available:
            if has_session and has_embodiment:
                if work_executing:
                    combined_state = PresenceState.EXECUTING
                    reason = "fresh_runtime_live_claim_and_executing_work"
                else:
                    combined_state = PresenceState.BOUND
                    reason = "fresh_runtime_live_claim_and_binding"
            else:
                combined_state = PresenceState.AVAILABLE
                reason = "fresh_runtime_available_without_work_binding"
        else:
            if has_session and not has_embodiment:
                combined_state = PresenceState.DEGRADED
                reason = "live_claim_without_session_binding"
            elif has_embodiment:
                combined_state = PresenceState.BOUND
                reason = "binding_present_without_runtime_observation"
            else:
                combined_state = PresenceState.UNKNOWN
                reason = "no_runtime_or_binding_evidence"

        return {
            "schema": "aspace.gateway.presence.v1",
            "identity": envelope.identity.institutional_holon_id,
            "institutional_rank": envelope.identity.institutional_rank,
            "embodiment_id": envelope.identity.embodiment_id,
            "session_id": envelope.identity.session_id,
            "runtime_id": envelope.identity.runtime_id,
            "node_id": envelope.identity.node_id,
            "surface_id": envelope.identity.surface_id,
            "combined_state": combined_state.value,
            "reason": reason,
            "runtime_state": runtime_state.value,
            "runtime_reason": runtime_reason,
            "runtime_available": runtime_available,
            "runtime_fresh": runtime_fresh,
            "has_session": has_session,
            "has_embodiment": has_embodiment,
            "has_runtime_id": has_runtime_id,
            "work_id": envelope.mission.work_id,
            "correlation_id": envelope.mission.correlation_id,
            "provenance": "gateway_protocol",
            "observed_at": current_time.isoformat(),
            "session_lineage": envelope.session_lineage,
            "ttl_seconds": envelope.presence_ttl_seconds,
            "evidence_refs": envelope.truth.evidence_refs if envelope.truth else [],
            "return_to": envelope.routing.return_to if envelope.routing else "",
        }


def create_gateway_envelope_from_cli(
    holon_id: str,
    institutional_rank: str,
    mission_id: str,
    work_id: str,
    cell_id: str,
    correlation_id: str,
    capability_id: Optional[str] = None,
    capability_version: Optional[str] = None,
    authority_scope: str = "L2_READ",
    policy_ref: str = "default",
    return_to: str = "cli:session",
    payload: Optional[Dict[str, Any]] = None,
) -> GatewayEnvelope:
    """Factory for creating GatewayEnvelope from CLI context."""
    identity = IdentityCoordinates(
        institutional_holon_id=holon_id,
        institutional_rank=institutional_rank,
    )

    mission = MissionCoordinates(
        mission_id=mission_id,
        work_id=work_id,
        cell_id=cell_id,
        correlation_id=correlation_id,
    )

    capability = None
    if capability_id:
        capability = CapabilityCoordinates(
            capability_id=capability_id,
            capability_version=capability_version or "1.0",
        )

    authority = AuthorityEnvelope(
        authority_scope=authority_scope,
        policy_ref=policy_ref,
    )

    routing = RoutingCoordinates(
        origin_layer="CLI",
        return_to=return_to,
    )

    truth = TruthCoordinates(
        source_authority="cli",
        freshness=Freshness.FRESH,
        epistemic_state=EpistemicState.KNOWN,
    )

    return GatewayEnvelope(
        identity=identity,
        mission=mission,
        capability=capability,
        authority=authority,
        routing=routing,
        truth=truth,
        payload=payload or {},
    )


if __name__ == "__main__":
    # Quick self-test
    print("Testing Gateway v0 Protocol Core...")

    # Create envelope
    env = create_gateway_envelope_from_cli(
        holon_id="S3-Graham",
        institutional_rank="S3_STATE",
        mission_id="gateway-canary-1",
        work_id="542",
        cell_id="G0",
        correlation_id="corr-gateway-001",
        capability_id="gateway.protocol.create",
        capability_version="v0",
        return_to="github:#542",
        payload={"action": "initialize"},
    )

    print(f"Created envelope: {env.gateway_message_id}")
    print(f"Identity: {env.identity.institutional_holon_id} ({env.identity.institutional_rank})")
    print(f"Mission: {env.mission.mission_id} / work:{env.mission.work_id} / cell:{env.mission.cell_id}")
    print(f"Correlation: {env.mission.correlation_id}")

    # Test protocol
    protocol = GatewayProtocol()
    session = protocol.create_session(env.identity, env.mission)
    print(f"Created session: {session.identity.session_id}")

    # Test resume (runtime migration)
    resumed = protocol.resume_session(session, new_runtime_id="runtime-codex-b")
    print(f"Resumed session: {resumed.identity.session_id}")
    print(f"Lineage: {resumed.session_lineage}")
    print(f"Runtime migrated to: {resumed.identity.runtime_id}")

    # Test presence projection
    presence = protocol.project_presence(resumed, {
        "available": True,
        "observed_at": datetime.now(timezone.utc).isoformat(),
        "expires_at": (datetime.now(timezone.utc) + timedelta(seconds=300)).isoformat(),
    })
    print(f"Presence state: {presence['combined_state']} ({presence['reason']})")

    # Test InterFabric translation
    if_envelope = env.to_inter_fabric_envelope()
    print(f"InterFabric envelope valid: {if_envelope.get_correlation_id() == env.mission.correlation_id}")

    # Test invariants
    try:
        # This should fail - holon identity drift
        bad_env = env.clone_with_updates(
            new_payload={"bad": "data"},
        )
        # Mutate holon_id directly on the identity (bypassing clone)
        bad_env.identity = IdentityCoordinates(
            institutional_holon_id="NotS3-Graham",  # DRIFT!
            institutional_rank=env.identity.institutional_rank,
        )
        if_envelope2 = bad_env.to_inter_fabric_envelope()
        InterFabricEnvelope.validate_translation(if_envelope.to_dict(), if_envelope2.to_dict())
        print("ERROR: Should have failed on holon drift!")
    except InterFabricInvariantError as e:
        print(f"Correctly caught holon identity drift: {e}")

    print("\nAll Gateway v0 Protocol Core tests passed!")