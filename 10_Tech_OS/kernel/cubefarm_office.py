"""CubeFarm Living Office Projection Engine.

Issue #403: Project A'Space Embodied Holons and multi-layer topology into the Living Office.

CubeFarm Office is a projection/runtime surface, NOT an institutional source of truth.

Laws:
1. Identity != runtime != session != repo != desk widget.
2. Multiple cognition/review/research bodies are allowed concurrently.
3. Exclusivity applies only to conflicting mutations/effects.
4. Empty/offline runtime does not delete institutional identity.
5. WorkGraph/Anthology/Agent OS supply truth; CubeFarm renders and acts through bounded adapters.
6. GitHub is an engineering/evidence plane, not the whole cosmology.
7. Ryan/BUILD factory and River/FLOW are complementary.
"""

from __future__ import annotations

import dataclasses
import json
import os
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from truth_projection import project_truth

ALLOWED_HIERARCHIES = {"S1", "S2", "S3", "A1", "A2", "A3", "B1", "B2", "B3"}
ALLOWED_FLOOR_TYPES = {
    "S2 Core",
    "A2 Life framework",
    "B1 business/franchise",
    "B2 domain",
    "MissionCell / temporary war-room",
    "bounded factory floor",
}


@dataclasses.dataclass
class RuntimeBody:
    harness: str
    profile: str
    session: str
    runtime_state: str  # ACTIVE, REVIEWING, BUILDING, RESEARCHING, OFFLINE, etc.
    current_operation: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return dataclasses.asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> RuntimeBody:
        return cls(**data)


@dataclasses.dataclass
class DeskProjection:
    actor_id: str
    hierarchy: str
    institutional_state: str  # ACTIVE, SUSPENDED, DORMANT, etc.
    embodiment_state: str  # EMBODIED, DISEMBODIED, DORMANT
    workload_state: str  # IDLE, ACTIVE, OVERLOADED
    home: str
    missions: List[str] = dataclasses.field(default_factory=list)
    work_ids: List[Any] = dataclasses.field(default_factory=list)
    effect_leases: List[str] = dataclasses.field(default_factory=list)
    evidence_head: str = ""
    subagents: List[str] = dataclasses.field(default_factory=list)
    runtime_bodies: List[RuntimeBody] = dataclasses.field(default_factory=list)
    return_to: str = ""

    def __post_init__(self) -> None:
        if self.hierarchy not in ALLOWED_HIERARCHIES:
            raise ValueError(f"Invalid hierarchy: {self.hierarchy}. Must be one of {ALLOWED_HIERARCHIES}")

    def add_runtime_body(self, body: RuntimeBody) -> None:
        # Remove existing body with same harness if present
        self.runtime_bodies = [b for b in self.runtime_bodies if b.harness != body.harness]
        self.runtime_bodies.append(body)

    def remove_runtime_body(self, harness: str) -> None:
        self.runtime_bodies = [b for b in self.runtime_bodies if b.harness != harness]

    def switch_runtime_bodies(self, new_bodies: List[RuntimeBody]) -> None:
        """Switch runtime bodies without recreating or renaming the actor/desk identity.

        Law 1: Identity != runtime != session != repo != desk widget.
        Law 4: Empty/offline runtime does not delete institutional identity.
        """
        self.runtime_bodies = list(new_bodies)
        # Institutional state and actor_id remain unchanged!

    def render_projection(
        self,
        observed_at: Optional[Any] = None,
        freshness_seconds: int = 86400,
    ) -> Dict[str, Any]:
        """Render desk projection separating identity, embodiment, runtime, and workload."""
        obs = observed_at or datetime.now(timezone.utc)

        identity_proj = project_truth(
            value={
                "actor_id": self.actor_id,
                "hierarchy": self.hierarchy,
                "institutional_state": self.institutional_state,
                "subagents": list(self.subagents),
            },
            source="workgraph.identity",
            authority="Tech_OS",
            observed_at=obs,
            evidence_refs=[f"github://Amdkn/Aspace_OS_V3#{self.return_to or '403'}"],
            freshness_seconds=freshness_seconds,
        )

        embodiment_proj = project_truth(
            value={
                "embodiment_state": self.embodiment_state,
                "home": self.home,
                "effect_leases": list(self.effect_leases),
                "evidence_head": self.evidence_head,
            },
            source="cubefarm.office.desk",
            authority="Tech_OS",
            observed_at=obs,
            evidence_refs=["anthology://embodiment/holon"],
            freshness_seconds=freshness_seconds,
        )

        runtime_proj = project_truth(
            value={
                "active_count": len(self.runtime_bodies),
                "runtime_bodies": [b.to_dict() for b in self.runtime_bodies],
            },
            source="agent_os.harness_mesh",
            authority="Tech_OS",
            observed_at=obs,
            evidence_refs=["harness://mesh/sessions"],
            freshness_seconds=freshness_seconds,
        )

        workload_proj = project_truth(
            value={
                "workload_state": self.workload_state,
                "missions": list(self.missions),
                "work_ids": list(self.work_ids),
                "return_to": self.return_to,
            },
            source="workgraph.tasks",
            authority="Tech_OS",
            observed_at=obs,
            evidence_refs=[f"workgraph://mission/{m}" for m in self.missions] or ["workgraph://tasks"],
            freshness_seconds=freshness_seconds,
        )

        return {
            "schema": "aspace.desk-projection.v1",
            "identity": identity_proj,
            "embodiment": embodiment_proj,
            "runtime": runtime_proj,
            "workload": workload_proj,
        }

    def to_dict(self) -> Dict[str, Any]:
        return {
            "actor_id": self.actor_id,
            "hierarchy": self.hierarchy,
            "institutional_state": self.institutional_state,
            "embodiment_state": self.embodiment_state,
            "workload_state": self.workload_state,
            "home": self.home,
            "missions": self.missions,
            "work_ids": self.work_ids,
            "effect_leases": self.effect_leases,
            "evidence_head": self.evidence_head,
            "subagents": self.subagents,
            "runtime_bodies": [b.to_dict() for b in self.runtime_bodies],
            "return_to": self.return_to,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> DeskProjection:
        data_copy = dict(data)
        rb_data = data_copy.pop("runtime_bodies", [])
        runtime_bodies = [RuntimeBody.from_dict(b) for b in rb_data]
        return cls(runtime_bodies=runtime_bodies, **data_copy)


@dataclasses.dataclass
class OfficeFloor:
    floor_id: str
    floor_type: str
    title: str
    anthology_refs: List[str] = dataclasses.field(default_factory=list)
    desks: List[DeskProjection] = dataclasses.field(default_factory=list)
    deep_links: Dict[str, str] = dataclasses.field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.floor_type not in ALLOWED_FLOOR_TYPES:
            raise ValueError(f"Invalid floor_type: {self.floor_type}. Must be one of {ALLOWED_FLOOR_TYPES}")

    def render_floor_projection(
        self,
        observed_at: Optional[Any] = None,
        freshness_seconds: int = 86400,
    ) -> Dict[str, Any]:
        obs = observed_at or datetime.now(timezone.utc)

        return {
            "schema": "aspace.office-floor.v1",
            "floor_id": self.floor_id,
            "floor_type": self.floor_type,
            "title": self.title,
            "anthology_refs": [
                project_truth(
                    value=ref,
                    source="anthology.registry",
                    authority="Anthology",
                    observed_at=obs,
                    evidence_refs=[ref],
                    freshness_seconds=freshness_seconds,
                )
                for ref in self.anthology_refs
            ],
            "deep_links": {
                system: project_truth(
                    value=link,
                    source=f"deep_link.{system}",
                    authority="Tech_OS",
                    observed_at=obs,
                    evidence_refs=[link],
                    freshness_seconds=freshness_seconds,
                )
                for system, link in self.deep_links.items()
            },
            "desks": [d.render_projection(observed_at=obs, freshness_seconds=freshness_seconds) for d in self.desks],
        }

    def to_dict(self) -> Dict[str, Any]:
        return {
            "floor_id": self.floor_id,
            "floor_type": self.floor_type,
            "title": self.title,
            "anthology_refs": self.anthology_refs,
            "desks": [d.to_dict() for d in self.desks],
            "deep_links": self.deep_links,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> OfficeFloor:
        data_copy = dict(data)
        desks_data = data_copy.pop("desks", [])
        desks = [DeskProjection.from_dict(d) for d in desks_data]
        return cls(desks=desks, **data_copy)


class CubeFarmOfficeProjection:
    """Living Office Projection manager preserving desk/mission lineage across restarts."""

    def __init__(self, storage_filepath: Optional[str] = None) -> None:
        self.storage_filepath = storage_filepath or "10_Tech_OS/kernel/cubefarm_office_state.json"
        self.floors: Dict[str, OfficeFloor] = {}

    def add_floor(self, floor: OfficeFloor) -> None:
        self.floors[floor.floor_id] = floor

    def get_floor(self, floor_id: str) -> Optional[OfficeFloor]:
        return self.floors.get(floor_id)

    def render_office_projection(
        self,
        observed_at: Optional[Any] = None,
        freshness_seconds: int = 86400,
    ) -> Dict[str, Any]:
        obs = observed_at or datetime.now(timezone.utc)
        return {
            "schema": "aspace.cubefarm-office.v1",
            "is_projection_surface": True,
            "source_of_truth_notice": "CubeFarm Office is a projection/runtime surface, not an institutional source of truth.",
            "floors": [
                f.render_floor_projection(observed_at=obs, freshness_seconds=freshness_seconds)
                for f in self.floors.values()
            ],
        }

    def save_office_state(self, filepath: Optional[str] = None) -> str:
        target = filepath or self.storage_filepath
        dirpath = os.path.dirname(target)
        if dirpath:
            os.makedirs(dirpath, exist_ok=True)
        data = {
            "schema": "aspace.cubefarm-office-state.v1",
            "floors": [f.to_dict() for f in self.floors.values()],
        }
        with open(target, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        return target

    def load_office_state(self, filepath: Optional[str] = None) -> Dict[str, Any]:
        target = filepath or self.storage_filepath
        with open(target, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.floors = {}
        for floor_data in data.get("floors", []):
            floor = OfficeFloor.from_dict(floor_data)
            self.floors[floor.floor_id] = floor
        return data
