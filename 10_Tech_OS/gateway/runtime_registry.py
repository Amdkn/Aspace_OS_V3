"""Provider-neutral runtime registry for A'Space Gateway G2.

Runtime availability is observational state. It never implies institutional
holon activity, work ownership, or execution authority.
"""

from __future__ import annotations

import copy
from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List, Optional


@dataclass(frozen=True)
class RuntimeDescriptor:
    runtime_id: str
    adapter_id: str
    adapter_version: str
    upstream_repo: str
    upstream_sha: str
    intrinsic_scale: str
    projected_scales: List[str]
    capabilities: List[str]
    forbidden_organs: List[str] = field(default_factory=list)
    evidence_refs: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class RuntimeObservation:
    runtime_id: str
    runtime_state: str
    observed_at: str
    evidence_refs: List[str] = field(default_factory=list)
    degraded_reason: Optional[str] = None


class RuntimeRegistry:
    """Descriptor + observation registry with no dispatch authority."""

    VALID_STATES = {"UNKNOWN", "OFFLINE", "STARTING", "LIVE", "WAITING", "STALE", "FAILED"}

    def __init__(self) -> None:
        self._descriptors: Dict[str, RuntimeDescriptor] = {}
        self._observations: Dict[str, RuntimeObservation] = {}

    def register(self, descriptor: RuntimeDescriptor) -> None:
        if not descriptor.runtime_id:
            raise ValueError("runtime_id is required")
        if descriptor.runtime_id in self._descriptors:
            raise ValueError(f"runtime already registered: {descriptor.runtime_id}")
        self._descriptors[descriptor.runtime_id] = descriptor

    def observe(self, observation: RuntimeObservation) -> None:
        if observation.runtime_id not in self._descriptors:
            raise ValueError(f"unknown runtime: {observation.runtime_id}")
        if observation.runtime_state not in self.VALID_STATES:
            raise ValueError(f"invalid runtime state: {observation.runtime_state}")
        if not observation.evidence_refs:
            raise ValueError("runtime observation requires evidence")
        self._observations[observation.runtime_id] = observation

    def get(self, runtime_id: str) -> Optional[RuntimeDescriptor]:
        return self._descriptors.get(runtime_id)

    def list(self, capability: Optional[str] = None) -> List[RuntimeDescriptor]:
        values: Iterable[RuntimeDescriptor] = self._descriptors.values()
        if capability:
            values = (item for item in values if capability in item.capabilities)
        return list(values)

    def projection(self, runtime_id: str) -> Dict[str, Any]:
        descriptor = self._descriptors.get(runtime_id)
        if descriptor is None:
            return {"status": "NOT_FOUND", "runtime_id": runtime_id}
        observation = self._observations.get(runtime_id)
        return {
            "runtime_id": descriptor.runtime_id,
            "adapter_id": descriptor.adapter_id,
            "adapter_version": descriptor.adapter_version,
            "upstream_repo": descriptor.upstream_repo,
            "upstream_sha": descriptor.upstream_sha,
            "intrinsic_scale": descriptor.intrinsic_scale,
            "projected_scales": list(descriptor.projected_scales),
            "capabilities": list(descriptor.capabilities),
            "runtime_state": observation.runtime_state if observation else "UNKNOWN",
            "observed_at": observation.observed_at if observation else None,
            "evidence_refs": list(observation.evidence_refs) if observation else list(descriptor.evidence_refs),
            "degraded_reason": observation.degraded_reason if observation else None,
            # Deliberately absent: institutional_state / workload_state / ownership.
        }
