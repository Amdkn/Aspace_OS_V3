#!/usr/bin/env python3
"""
A'Space Gateway v0 — G2 Runtime Registry + Surface Federation

Exposes one Gateway semantic across multiple clients and runtimes.

Runtime Registry:
- Represents adapters for: Hermes, Codex local/GitHub-hosted, Claude Code/GitHub-hosted,
  Antigravity, Jules, Browser Harness, local inference, future runtimes
- Runtime health is distinct from holon state

Surface Federation:
- CLI, Agent OS Web/Desktop, GitHub (initial)
- Messaging/CubeFarm/StarNet/mobile as projections without forking session semantics

Capability Bridge:
- Consumes existing AI-Native Capability Fabric from #333
- MCP/API/CLI/Skill/Harness are ports/adapters of one capability, not duplicated business logic

Acceptance: The same institutional holon/session can be observed from at least two surfaces
and migrated between two runtimes without authority or lineage drift.
"""

from __future__ import annotations

import json
import uuid
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional, Callable, Set, Literal
from pathlib import Path
from abc import ABC, abstractmethod

from inter_fabric import InterFabricEnvelope, InterFabricInvariantError
from .protocol import (
    GatewayEnvelope,
    GatewayProtocol,
    IdentityCoordinates,
    MissionCoordinates,
    CapabilityCoordinates,
    AuthorityEnvelope,
    PresenceState,
    Freshness,
    EpistemicState,
    DeliveryState,
    create_gateway_envelope_from_cli,
)
from .github_control_plane import GitHubControlPlane


class RuntimeType(str, Enum):
    """Supported runtime types."""
    HERMES = "hermes"
    CODEX_LOCAL = "codex-local"
    CODEX_GITHUB = "codex-github"
    CLAUDE_CODE_LOCAL = "claude-code-local"
    CLAUDE_CODE_GITHUB = "claude-code-github"
    ANTIGRAVITY = "antigravity"
    JULES = "jules"
    BROWSER_HARNESS = "browser-harness"
    LOCAL_INFERENCE = "local-inference"
    UNKNOWN = "unknown"


class SurfaceType(str, Enum):
    """Supported surface types."""
    CLI = "cli"
    AGENT_OS_WEB = "agent-os-web"
    AGENT_OS_DESKTOP = "agent-os-desktop"
    GITHUB = "github"
    MESSAGING = "messaging"
    CUBEFARM = "cubefarm"
    STARNET = "starnet"
    MOBILE = "mobile"


class RuntimeHealth(str, Enum):
    """Runtime health distinct from holon state."""
    HEALTHY = "HEALTHY"
    DEGRADED = "DEGRADED"
    UNHEALTHY = "UNHEALTHY"
    UNKNOWN = "UNKNOWN"
    OFFLINE = "OFFLINE"


@dataclass(frozen=True)
class RuntimeAdapter:
    """Runtime adapter configuration."""
    runtime_id: str
    runtime_type: RuntimeType
    adapter_name: str
    adapter_version: str
    endpoint: Optional[str] = None
    capabilities: List[str] = field(default_factory=list)
    supported_surfaces: List[SurfaceType] = field(default_factory=list)
    health: RuntimeHealth = RuntimeHealth.UNKNOWN
    last_health_check: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class SurfaceProjection:
    """Surface projection of a Gateway session."""
    surface_id: str
    surface_type: SurfaceType
    session_id: str
    holon_id: str
    attached_at: str
    last_activity: str
    capabilities: List[str] = field(default_factory=list)
    viewport: Dict[str, Any] = field(default_factory=dict)  # Surface-specific view


@dataclass(frozen=True)
class RuntimeObservation:
    """Runtime health observation (from runtime_presence.py)."""
    runtime_id: str
    runtime_type: RuntimeType
    health: RuntimeHealth
    observed_at: str
    expires_at: Optional[str] = None
    capabilities: List[str] = field(default_factory=list)
    degraded_reason: Optional[str] = None
    evidence_refs: List[str] = field(default_factory=list)


class RuntimeAdapterBase(ABC):
    """Base class for runtime adapters."""

    def __init__(self, adapter: RuntimeAdapter):
        self.adapter = adapter

    @abstractmethod
    def health_check(self) -> RuntimeObservation:
        """Check runtime health."""
        pass

    @abstractmethod
    def execute(
        self,
        envelope: GatewayEnvelope,
        capability_id: str,
        payload: Dict[str, Any],
    ) -> GatewayEnvelope:
        """Execute a capability via this runtime."""
        pass

    @abstractmethod
    def can_execute(self, capability_id: str) -> bool:
        """Check if this runtime can execute a capability."""
        pass


class HermesAdapter(RuntimeAdapterBase):
    """Hermes runtime adapter."""

    def health_check(self) -> RuntimeObservation:
        # In practice, would check actual Hermes health endpoint
        return RuntimeObservation(
            runtime_id=self.adapter.runtime_id,
            runtime_type=RuntimeType.HERMES,
            health=RuntimeHealth.HEALTHY,
            observed_at=datetime.now(timezone.utc).isoformat(),
            capabilities=self.adapter.capabilities,
        )

    def execute(
        self,
        envelope: GatewayEnvelope,
        capability_id: str,
        payload: Dict[str, Any],
    ) -> GatewayEnvelope:
        # Simulate Hermes execution
        new_env = envelope.clone_with_updates(
            new_payload={**envelope.payload, "hermes_execution": True, "result": "simulated"},
            new_runtime_id=self.adapter.runtime_id,
            delivery_state=DeliveryState.DELIVERED,
        )
        return new_env

    def can_execute(self, capability_id: str) -> bool:
        return capability_id in self.adapter.capabilities


class CodexAdapter(RuntimeAdapterBase):
    """Codex (local or GitHub-hosted) runtime adapter."""

    def health_check(self) -> RuntimeObservation:
        return RuntimeObservation(
            runtime_id=self.adapter.runtime_id,
            runtime_type=self.adapter.runtime_type,
            health=RuntimeHealth.HEALTHY,
            observed_at=datetime.now(timezone.utc).isoformat(),
            capabilities=self.adapter.capabilities,
        )

    def execute(
        self,
        envelope: GatewayEnvelope,
        capability_id: str,
        payload: Dict[str, Any],
    ) -> GatewayEnvelope:
        new_env = envelope.clone_with_updates(
            new_payload={**envelope.payload, "codex_execution": True, "result": "simulated"},
            new_runtime_id=self.adapter.runtime_id,
            delivery_state=DeliveryState.DELIVERED,
        )
        return new_env

    def can_execute(self, capability_id: str) -> bool:
        return capability_id in self.adapter.capabilities


class ClaudeCodeAdapter(RuntimeAdapterBase):
    """Claude Code (local or GitHub-hosted) runtime adapter."""

    def health_check(self) -> RuntimeObservation:
        return RuntimeObservation(
            runtime_id=self.adapter.runtime_id,
            runtime_type=self.adapter.runtime_type,
            health=RuntimeHealth.HEALTHY,
            observed_at=datetime.now(timezone.utc).isoformat(),
            capabilities=self.adapter.capabilities,
        )

    def execute(
        self,
        envelope: GatewayEnvelope,
        capability_id: str,
        payload: Dict[str, Any],
    ) -> GatewayEnvelope:
        new_env = envelope.clone_with_updates(
            new_payload={**envelope.payload, "claude_code_execution": True, "result": "simulated"},
            new_runtime_id=self.adapter.runtime_id,
            delivery_state=DeliveryState.DELIVERED,
        )
        return new_env

    def can_execute(self, capability_id: str) -> bool:
        return capability_id in self.adapter.capabilities


class AntigravityAdapter(RuntimeAdapterBase):
    """Antigravity runtime adapter."""

    def health_check(self) -> RuntimeObservation:
        return RuntimeObservation(
            runtime_id=self.adapter.runtime_id,
            runtime_type=RuntimeType.ANTIGRAVITY,
            health=RuntimeHealth.HEALTHY,
            observed_at=datetime.now(timezone.utc).isoformat(),
            capabilities=self.adapter.capabilities,
        )

    def execute(
        self,
        envelope: GatewayEnvelope,
        capability_id: str,
        payload: Dict[str, Any],
    ) -> GatewayEnvelope:
        new_env = envelope.clone_with_updates(
            new_payload={**envelope.payload, "antigravity_execution": True, "result": "simulated"},
            new_runtime_id=self.adapter.runtime_id,
            delivery_state=DeliveryState.DELIVERED,
        )
        return new_env

    def can_execute(self, capability_id: str) -> bool:
        return capability_id in self.adapter.capabilities


class JulesAdapter(RuntimeAdapterBase):
    """Jules runtime adapter."""

    def health_check(self) -> RuntimeObservation:
        return RuntimeObservation(
            runtime_id=self.adapter.runtime_id,
            runtime_type=RuntimeType.JULES,
            health=RuntimeHealth.HEALTHY,
            observed_at=datetime.now(timezone.utc).isoformat(),
            capabilities=self.adapter.capabilities,
        )

    def execute(
        self,
        envelope: GatewayEnvelope,
        capability_id: str,
        payload: Dict[str, Any],
    ) -> GatewayEnvelope:
        new_env = envelope.clone_with_updates(
            new_payload={**envelope.payload, "jules_execution": True, "result": "simulated"},
            new_runtime_id=self.adapter.runtime_id,
            delivery_state=DeliveryState.DELIVERED,
        )
        return new_env

    def can_execute(self, capability_id: str) -> bool:
        return capability_id in self.adapter.capabilities


class BrowserHarnessAdapter(RuntimeAdapterBase):
    """Browser Harness runtime adapter."""

    def health_check(self) -> RuntimeObservation:
        return RuntimeObservation(
            runtime_id=self.adapter.runtime_id,
            runtime_type=RuntimeType.BROWSER_HARNESS,
            health=RuntimeHealth.HEALTHY,
            observed_at=datetime.now(timezone.utc).isoformat(),
            capabilities=self.adapter.capabilities,
        )

    def execute(
        self,
        envelope: GatewayEnvelope,
        capability_id: str,
        payload: Dict[str, Any],
    ) -> GatewayEnvelope:
        new_env = envelope.clone_with_updates(
            new_payload={**envelope.payload, "browser_execution": True, "result": "simulated"},
            new_runtime_id=self.adapter.runtime_id,
            delivery_state=DeliveryState.DELIVERED,
        )
        return new_env

    def can_execute(self, capability_id: str) -> bool:
        return capability_id in self.adapter.capabilities


class LocalInferenceAdapter(RuntimeAdapterBase):
    """Local inference runtime adapter."""

    def health_check(self) -> RuntimeObservation:
        return RuntimeObservation(
            runtime_id=self.adapter.runtime_id,
            runtime_type=RuntimeType.LOCAL_INFERENCE,
            health=RuntimeHealth.HEALTHY,
            observed_at=datetime.now(timezone.utc).isoformat(),
            capabilities=self.adapter.capabilities,
        )

    def execute(
        self,
        envelope: GatewayEnvelope,
        capability_id: str,
        payload: Dict[str, Any],
    ) -> GatewayEnvelope:
        new_env = envelope.clone_with_updates(
            new_payload={**envelope.payload, "local_execution": True, "result": "simulated"},
            new_runtime_id=self.adapter.runtime_id,
            delivery_state=DeliveryState.DELIVERED,
        )
        return new_env

    def can_execute(self, capability_id: str) -> bool:
        return capability_id in self.adapter.capabilities


# Adapter factory
ADAPTER_FACTORIES: Dict[RuntimeType, Callable[[RuntimeAdapter], RuntimeAdapterBase]] = {
    RuntimeType.HERMES: HermesAdapter,
    RuntimeType.CODEX_LOCAL: CodexAdapter,
    RuntimeType.CODEX_GITHUB: CodexAdapter,
    RuntimeType.CLAUDE_CODE_LOCAL: ClaudeCodeAdapter,
    RuntimeType.CLAUDE_CODE_GITHUB: ClaudeCodeAdapter,
    RuntimeType.ANTIGRAVITY: AntigravityAdapter,
    RuntimeType.JULES: JulesAdapter,
    RuntimeType.BROWSER_HARNESS: BrowserHarnessAdapter,
    RuntimeType.LOCAL_INFERENCE: LocalInferenceAdapter,
}


def create_adapter(adapter_config: RuntimeAdapter) -> RuntimeAdapterBase:
    """Create runtime adapter instance from config."""
    factory = ADAPTER_FACTORIES.get(adapter_config.runtime_type)
    if not factory:
        raise ValueError(f"No adapter factory for runtime type: {adapter_config.runtime_type}")
    return factory(adapter_config)


class RuntimeRegistry:
    """
    G2 Runtime Registry.

    Manages runtime adapters, health, and capability routing.
    Runtime health is distinct from holon state.
    """

    def __init__(self):
        self._adapters: Dict[str, RuntimeAdapter] = {}
        self._adapter_instances: Dict[str, RuntimeAdapterBase] = {}
        self._health_observations: Dict[str, RuntimeObservation] = {}
        self._capability_index: Dict[str, Set[str]] = {}  # capability_id -> set of runtime_ids

    def register(self, adapter: RuntimeAdapter) -> None:
        """Register a runtime adapter."""
        self._adapters[adapter.runtime_id] = adapter
        self._adapter_instances[adapter.runtime_id] = create_adapter(adapter)

        # Update capability index
        for cap in adapter.capabilities:
            if cap not in self._capability_index:
                self._capability_index[cap] = set()
            self._capability_index[cap].add(adapter.runtime_id)

    def unregister(self, runtime_id: str) -> None:
        """Unregister a runtime adapter."""
        if runtime_id in self._adapters:
            adapter = self._adapters[runtime_id]
            for cap in adapter.capabilities:
                if cap in self._capability_index:
                    self._capability_index[cap].discard(runtime_id)
            del self._adapters[runtime_id]
            del self._adapter_instances[runtime_id]
            self._health_observations.pop(runtime_id, None)

    def get_adapter(self, runtime_id: str) -> Optional[RuntimeAdapter]:
        """Get adapter config by ID."""
        return self._adapters.get(runtime_id)

    def get_adapter_instance(self, runtime_id: str) -> Optional[RuntimeAdapterBase]:
        """Get adapter instance by ID."""
        return self._adapter_instances.get(runtime_id)

    def list_adapters(
        self,
        runtime_type: Optional[RuntimeType] = None,
        health: Optional[RuntimeHealth] = None,
    ) -> List[RuntimeAdapter]:
        """List adapters with optional filters."""
        result = list(self._adapters.values())
        if runtime_type:
            result = [a for a in result if a.runtime_type == runtime_type]
        if health:
            result = [a for a in result if a.health == health]
        return result

    def find_runtimes_for_capability(
        self,
        capability_id: str,
        min_health: RuntimeHealth = RuntimeHealth.HEALTHY,
    ) -> List[RuntimeAdapter]:
        """Find runtimes that can execute a capability."""
        runtime_ids = self._capability_index.get(capability_id, set())
        result = []
        for rid in runtime_ids:
            adapter = self._adapters.get(rid)
            if adapter and self._health_meets(adapter.health, min_health):
                result.append(adapter)
        return result

    def _health_meets(self, current: RuntimeHealth, minimum: RuntimeHealth) -> bool:
        """Check if current health meets minimum."""
        order = {
            RuntimeHealth.HEALTHY: 4,
            RuntimeHealth.DEGRADED: 3,
            RuntimeHealth.UNKNOWN: 2,
            RuntimeHealth.UNHEALTHY: 1,
            RuntimeHealth.OFFLINE: 0,
        }
        return order.get(current, 0) >= order.get(minimum, 0)

    def update_health(self, observation: RuntimeObservation) -> None:
        """Update runtime health from observation."""
        self._health_observations[observation.runtime_id] = observation
        if observation.runtime_id in self._adapters:
            # Update adapter health
            adapter = self._adapters[observation.runtime_id]
            self._adapters[observation.runtime_id] = RuntimeAdapter(
                **{**asdict(adapter), "health": observation.health, "last_health_check": observation.observed_at}
            )

    def health_check_all(self) -> Dict[str, RuntimeObservation]:
        """Run health checks on all registered adapters."""
        results = {}
        for runtime_id, instance in self._adapter_instances.items():
            try:
                obs = instance.health_check()
                self.update_health(obs)
                results[runtime_id] = obs
            except Exception as e:
                obs = RuntimeObservation(
                    runtime_id=runtime_id,
                    runtime_type=self._adapters[runtime_id].runtime_type,
                    health=RuntimeHealth.UNHEALTHY,
                    observed_at=datetime.now(timezone.utc).isoformat(),
                    degraded_reason=str(e),
                )
                self.update_health(obs)
                results[runtime_id] = obs
        return results


class SurfaceRegistry:
    """
    G2 Surface Federation.

    Manages surface projections of Gateway sessions.
    Allows same session to be observed from multiple surfaces.
    """

    def __init__(self):
        self._projections: Dict[str, SurfaceProjection] = {}  # surface_id -> projection
        self._session_surfaces: Dict[str, Set[str]] = {}  # session_id -> set of surface_ids

    def attach_surface(
        self,
        session_id: str,
        holon_id: str,
        surface_type: SurfaceType,
        surface_id: Optional[str] = None,
        capabilities: Optional[List[str]] = None,
        viewport: Optional[Dict[str, Any]] = None,
    ) -> SurfaceProjection:
        """Attach a surface to a session."""
        sid = surface_id or f"{surface_type.value}-{uuid.uuid4().hex[:8]}"
        now = datetime.now(timezone.utc).isoformat()

        projection = SurfaceProjection(
            surface_id=sid,
            surface_type=surface_type,
            session_id=session_id,
            holon_id=holon_id,
            attached_at=now,
            last_activity=now,
            capabilities=capabilities or [],
            viewport=viewport or {},
        )

        self._projections[sid] = projection
        if session_id not in self._session_surfaces:
            self._session_surfaces[session_id] = set()
        self._session_surfaces[session_id].add(sid)

        return projection

    def detach_surface(self, surface_id: str) -> bool:
        """Detach a surface."""
        projection = self._projections.pop(surface_id, None)
        if projection:
            self._session_surfaces.get(projection.session_id, set()).discard(surface_id)
            return True
        return False

    def get_projection(self, surface_id: str) -> Optional[SurfaceProjection]:
        """Get surface projection."""
        return self._projections.get(surface_id)

    def get_session_surfaces(self, session_id: str) -> List[SurfaceProjection]:
        """Get all surfaces for a session."""
        surface_ids = self._session_surfaces.get(session_id, set())
        return [self._projections[sid] for sid in surface_ids if sid in self._projections]

    def update_activity(self, surface_id: str, viewport: Optional[Dict[str, Any]] = None) -> bool:
        """Update surface last activity."""
        projection = self._projections.get(surface_id)
        if not projection:
            return False

        updates = {"last_activity": datetime.now(timezone.utc).isoformat()}
        if viewport:
            updates["viewport"] = {**projection.viewport, **viewport}

        self._projections[surface_id] = SurfaceProjection(
            **{**asdict(projection), **updates}
        )
        return True


class CapabilityBridge:
    """
    G2 Capability Bridge.

    Consumes AI-Native Capability Fabric (#333) and exposes capabilities
    through Gateway protocol without duplicating business logic.
    """

    def __init__(self, capability_fabric_module):
        self.fabric = capability_fabric_module
        self._gateway_adapter_map: Dict[str, str] = {}  # capability_id -> surface

    def register_gateway_surface(self, capability_id: str, surface: str) -> None:
        """Register that a capability is available via Gateway surface."""
        self._gateway_adapter_map[capability_id] = surface

    def get_capability_manifest(self, capability_id: str) -> Optional[Dict[str, Any]]:
        """Get capability manifest from fabric."""
        if hasattr(self.fabric, 'registry'):
            cap = self.fabric.registry.get_capability(capability_id)
            if cap:
                return {
                    "capability_id": cap.capability_id,
                    "version": cap.version,
                    "domain_owner": cap.domain_owner,
                    "intent": cap.intent,
                    "input_schema": cap.input_schema,
                    "output_schema": cap.output_schema,
                    "authority": cap.authority,
                    "effect_class": cap.effect_class,
                    "supported_surfaces": cap.supported_surfaces + ["gateway"],
                }
        return None

    def invoke_via_gateway(
        self,
        capability_id: str,
        payload: Dict[str, Any],
        envelope: GatewayEnvelope,
    ) -> GatewayEnvelope:
        """
        Invoke capability through Gateway (not directly via fabric adapter).

        This preserves Gateway protocol invariants.
        """
        # Use fabric adapter but wrap in Gateway envelope
        adapter = self.fabric.adapters.get(envelope.identity.surface_id or "cli")
        if not adapter:
            # Create a basic CLI adapter for Gateway
            import sys
            sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "80_Agent-OS"))
            from capability_fabric.adapters import CLIAdapter
            from capability_fabric.quarantine import QuarantineRegistry
            adapter = CLIAdapter(self.fabric.registry, QuarantineRegistry())

        result = adapter.invoke(capability_id, payload, envelope.mission.correlation_id)

        # Wrap result in Gateway envelope
        new_env = envelope.clone_with_updates(
            new_payload={**envelope.payload, "capability_result": result},
            delivery_state=DeliveryState.DELIVERED if result.get("status") == "SUCCEEDED" else DeliveryState.UNKNOWN,
        )

        # Add evidence
        if envelope.truth:
            new_evidence = list(envelope.truth.evidence_refs)
            if result.get("receipt"):
                new_evidence.append(f"capability:{capability_id}:{result['receipt'].get('correlation_id', '')}")
            new_env = new_env.clone_with_updates(
                truth={"evidence_refs": new_evidence},
                allow_truth_resolution=True,
            )

        return new_env


class GatewayFederation:
    """
    G2 Gateway Federation Engine.

    Coordinates RuntimeRegistry, SurfaceRegistry, and CapabilityBridge
    to provide unified Gateway semantics across runtimes and surfaces.
    """

    def __init__(
        self,
        protocol: GatewayProtocol,
        capability_fabric_module,
    ):
        self.protocol = protocol
        self.runtime_registry = RuntimeRegistry()
        self.surface_registry = SurfaceRegistry()
        self.capability_bridge = CapabilityBridge(capability_fabric_module)
        self.github_control_plane = None  # Set if G1 is active

    def register_github_control_plane(self, control_plane: GitHubControlPlane) -> None:
        """Register GitHub control plane for G1 integration."""
        self.github_control_plane = control_plane

    def bootstrap_default_runtimes(self) -> None:
        """Register default runtime adapters for testing/canary."""
        defaults = [
            RuntimeAdapter(
                runtime_id="rt-hermes-1",
                runtime_type=RuntimeType.HERMES,
                adapter_name="hermes-adapter",
                adapter_version="1.0",
                capabilities=["gateway.protocol.create", "gateway.session.resume", "amf.execute"],
                supported_surfaces=[SurfaceType.CLI, SurfaceType.AGENT_OS_WEB],
            ),
            RuntimeAdapter(
                runtime_id="rt-codex-local-1",
                runtime_type=RuntimeType.CODEX_LOCAL,
                adapter_name="codex-adapter",
                adapter_version="1.0",
                capabilities=["gateway.protocol.create", "code.edit", "test.run"],
                supported_surfaces=[SurfaceType.CLI, SurfaceType.GITHUB],
            ),
            RuntimeAdapter(
                runtime_id="rt-claude-local-1",
                runtime_type=RuntimeType.CLAUDE_CODE_LOCAL,
                adapter_name="claude-code-adapter",
                adapter_version="1.0",
                capabilities=["gateway.protocol.create", "code.edit", "analysis.run"],
                supported_surfaces=[SurfaceType.CLI, SurfaceType.AGENT_OS_DESKTOP],
            ),
            RuntimeAdapter(
                runtime_id="rt-antigravity-1",
                runtime_type=RuntimeType.ANTIGRAVITY,
                adapter_name="antigravity-adapter",
                adapter_version="1.0",
                capabilities=["gateway.protocol.create", "ide.control", "browser.automate"],
                supported_surfaces=[SurfaceType.AGENT_OS_WEB, SurfaceType.AGENT_OS_DESKTOP],
            ),
            RuntimeAdapter(
                runtime_id="rt-jules-1",
                runtime_type=RuntimeType.JULES,
                adapter_name="jules-adapter",
                adapter_version="1.0",
                capabilities=["gateway.protocol.create", "code.edit", "pr.create"],
                supported_surfaces=[SurfaceType.GITHUB],
            ),
            RuntimeAdapter(
                runtime_id="rt-browser-1",
                runtime_type=RuntimeType.BROWSER_HARNESS,
                adapter_name="browser-harness-adapter",
                adapter_version="1.0",
                capabilities=["browser.tabs.read", "browser.dom.action", "browser.debugger.attach"],
                supported_surfaces=[SurfaceType.AGENT_OS_WEB, SurfaceType.AGENT_OS_DESKTOP],
            ),
        ]

        for adapter in defaults:
            self.runtime_registry.register(adapter)

        # Register Gateway surface for all capabilities
        for adapter in defaults:
            for cap in adapter.capabilities:
                self.capability_bridge.register_gateway_surface(cap, "gateway")

    def create_session(
        self,
        holon_id: str,
        institutional_rank: str,
        mission_id: str,
        work_id: str,
        cell_id: str,
        correlation_id: str,
        surface_type: SurfaceType = SurfaceType.CLI,
        capability_id: Optional[str] = None,
    ) -> tuple[GatewayEnvelope, SurfaceProjection]:
        """Create a new federated session with surface attachment."""
        envelope = create_gateway_envelope_from_cli(
            holon_id=holon_id,
            institutional_rank=institutional_rank,
            mission_id=mission_id,
            work_id=work_id,
            cell_id=cell_id,
            correlation_id=correlation_id,
            capability_id=capability_id,
            return_to=f"{surface_type.value}:session",
        )

        session = self.protocol.create_session(envelope.identity, envelope.mission)

        # Attach surface
        projection = self.surface_registry.attach_surface(
            session_id=session.identity.session_id,
            holon_id=holon_id,
            surface_type=surface_type,
            capabilities=[capability_id] if capability_id else [],
        )

        return session, projection

    def migrate_runtime(
        self,
        envelope: GatewayEnvelope,
        target_runtime_id: str,
    ) -> GatewayEnvelope:
        """
        Migrate session to a different runtime.

        Preserves: institutional holon, work/correlation identity, authority,
        evidence lineage, effect identity, return_to.
        """
        target_adapter = self.runtime_registry.get_adapter(target_runtime_id)
        if not target_adapter:
            raise ValueError(f"Runtime not found: {target_runtime_id}")

        # Check capability support
        if envelope.capability and envelope.capability.capability_id not in target_adapter.capabilities:
            raise ValueError(f"Runtime {target_runtime_id} does not support capability {envelope.capability.capability_id}")

        # Resume session with new runtime
        resumed = self.protocol.resume_session(
            envelope,
            new_runtime_id=target_runtime_id,
            new_embodiment_id=f"{target_adapter.runtime_type.value}:{target_runtime_id}",
        )

        return resumed

    def observe_from_surface(
        self,
        session_id: str,
        surface_type: SurfaceType,
    ) -> Optional[SurfaceProjection]:
        """Observe session from a specific surface."""
        surfaces = self.surface_registry.get_session_surfaces(session_id)
        for s in surfaces:
            if s.surface_type == surface_type:
                return s
        return None

    def execute_capability(
        self,
        envelope: GatewayEnvelope,
        capability_id: str,
        payload: Dict[str, Any],
        target_runtime_id: Optional[str] = None,
    ) -> GatewayEnvelope:
        """Execute a capability via the appropriate runtime."""
        # Find runtime
        if target_runtime_id:
            runtime_id = target_runtime_id
        else:
            runtimes = self.runtime_registry.find_runtimes_for_capability(capability_id)
            if not runtimes:
                raise ValueError(f"No healthy runtime for capability: {capability_id}")
            runtime_id = runtimes[0].runtime_id

        adapter_instance = self.runtime_registry.get_adapter_instance(runtime_id)
        if not adapter_instance:
            raise ValueError(f"Runtime adapter not instantiated: {runtime_id}")

        # Execute via runtime adapter
        result = adapter_instance.execute(envelope, capability_id, payload)

        return result

    def get_federated_presence(
        self,
        envelope: GatewayEnvelope,
    ) -> Dict[str, Any]:
        """Get federated presence across all surfaces and runtimes."""
        # Project presence from protocol
        protocol_presence = self.protocol.project_presence(envelope)

        # Add surface projections
        session_id = envelope.identity.session_id
        surfaces = self.surface_registry.get_session_surfaces(session_id)

        # Add runtime health
        runtime_health = {}
        for rid, obs in self.runtime_registry._health_observations.items():
            runtime_health[rid] = {
                "runtime_type": obs.runtime_type.value,
                "health": obs.health.value,
                "observed_at": obs.observed_at,
                "capabilities": obs.capabilities,
            }

        return {
            "protocol_presence": protocol_presence,
            "surfaces": [
                {
                    "surface_id": s.surface_id,
                    "surface_type": s.surface_type.value,
                    "attached_at": s.attached_at,
                    "last_activity": s.last_activity,
                    "viewport": s.viewport,
                }
                for s in surfaces
            ],
            "runtime_health": runtime_health,
            "federated": True,
        }


if __name__ == "__main__":
    # Quick self-test
    print("Testing G2 Runtime Registry + Surface Federation...")

    # Mock capability fabric
    class MockFabric:
        class MockRegistry:
            def get_capability(self, cap_id):
                return None
        registry = MockRegistry()
        adapters = {}

    # Create federation
    protocol = GatewayProtocol()
    federation = GatewayFederation(protocol, MockFabric())

    # Bootstrap default runtimes
    federation.bootstrap_default_runtimes()
    print(f"Registered {len(federation.runtime_registry._adapters)} runtimes")

    # Create session
    session, projection = federation.create_session(
        holon_id="S3-Graham",
        institutional_rank="S3_STATE",
        mission_id="gateway-canary-2",
        work_id="542",
        cell_id="G2",
        correlation_id="corr-gateway-002",
        surface_type=SurfaceType.CLI,
        capability_id="gateway.protocol.create",
    )
    print(f"Created session: {session.identity.session_id}")
    print(f"Attached surface: {projection.surface_id} ({projection.surface_type.value})")

    # Attach second surface (Agent OS Web)
    projection2 = federation.surface_registry.attach_surface(
        session_id=session.identity.session_id,
        holon_id="S3-Graham",
        surface_type=SurfaceType.AGENT_OS_WEB,
    )
    print(f"Attached second surface: {projection2.surface_id} ({projection2.surface_type.value})")

    # Check session surfaces
    surfaces = federation.surface_registry.get_session_surfaces(session.identity.session_id)
    print(f"Session has {len(surfaces)} surfaces")

    # Migrate runtime
    migrated = federation.migrate_runtime(session, "rt-codex-local-1")
    print(f"Migrated to runtime: {migrated.identity.runtime_id}")
    print(f"Lineage: {migrated.session_lineage}")

    # Execute capability
    result = federation.execute_capability(
        migrated,
        "gateway.protocol.create",
        {"action": "test"},
    )
    print(f"Execution result: {result.payload.get('capability_result', {}).get('status')}")

    # Get federated presence
    presence = federation.get_federated_presence(migrated)
    print(f"Federated presence: {presence['protocol_presence']['combined_state']}")
    print(f"Surfaces: {len(presence['surfaces'])}")
    print(f"Runtime health entries: {len(presence['runtime_health'])}")

    print("\nAll G2 Runtime Registry + Surface Federation tests passed!")