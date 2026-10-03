"""CubeFarm Tri-Wall Projections for Agent OS, Life OS, and Business OS.

Issue #416 / #403:
CubeFarm is a projection surface, not the source of truth.
Each wall renders provenance/freshness via project_truth and deep-links to durable sources.
Actors across walls maintain unified identity (actor_id) without duplication.
Canary state persistence allows projections and canary desks to survive refresh/restart.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from truth_projection import project_truth


class ActorRegistry:
    """Unified actor identity registry across Agent, Life, and Business OS walls."""

    def __init__(self) -> None:
        self._actors: Dict[str, Dict[str, Any]] = {}

    def register_actor(
        self,
        actor_id: str,
        name: str,
        roles: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        if actor_id in self._actors:
            actor = self._actors[actor_id]
            if roles:
                existing_roles = set(actor["roles"])
                for r in roles:
                    if r not in existing_roles:
                        actor["roles"].append(r)
            if metadata:
                actor["metadata"].update(metadata)
        else:
            actor = {
                "actor_id": actor_id,
                "name": name,
                "roles": roles or [],
                "metadata": metadata or {},
            }
            self._actors[actor_id] = actor
        return self._actors[actor_id]

    def get_actor(self, actor_id: str) -> Optional[Dict[str, Any]]:
        return self._actors.get(actor_id)

    def to_dict(self) -> Dict[str, Any]:
        return self._actors

    def load_dict(self, data: Dict[str, Any]) -> None:
        self._actors = data


def build_agent_os_wall(
    *,
    capabilities: List[Dict[str, Any]],
    adapters: List[Dict[str, Any]],
    harness_bodies: List[Dict[str, Any]],
    budgets: Dict[str, Any],
    evidence: List[Dict[str, Any]],
    workgraph_tasks: List[Dict[str, Any]],
    actor_registry: ActorRegistry,
    observed_at: Optional[Any] = None,
    freshness_seconds: int = 3600,
) -> Dict[str, Any]:
    now = datetime.now(timezone.utc)
    obs = observed_at or now

    return {
        "wall": "Agent OS",
        "capabilities": [
            project_truth(
                value=cap.get("value"),
                source=cap.get("source", "agent_os.registry"),
                authority=cap.get("authority", "Tech_OS"),
                observed_at=obs,
                evidence_refs=cap.get("evidence_refs", ["github://Amdkn/Aspace_OS_V3#333"]),
                freshness_seconds=freshness_seconds,
            )
            for cap in capabilities
        ],
        "adapters": [
            project_truth(
                value=adp.get("value"),
                source=adp.get("source", "agent_os.adapters"),
                authority=adp.get("authority", "Tech_OS"),
                observed_at=obs,
                evidence_refs=adp.get("evidence_refs", ["github://Amdkn/Aspace_OS_V3#335"]),
                freshness_seconds=freshness_seconds,
            )
            for adp in adapters
        ],
        "harness_bodies": [
            project_truth(
                value={
                    **hb.get("value", {}),
                    "actor_ref": actor_registry.get_actor(hb["value"].get("actor_id"))
                    if "actor_id" in hb.get("value", {})
                    else None,
                },
                source=hb.get("source", "harness.mesh"),
                authority=hb.get("authority", "Tech_OS"),
                observed_at=obs,
                evidence_refs=hb.get("evidence_refs", ["github://Amdkn/Aspace_OS_V3#404"]),
                freshness_seconds=freshness_seconds,
            )
            for hb in harness_bodies
        ],
        "budgets": project_truth(
            value=budgets.get("value", budgets),
            source=budgets.get("source", "cognitive_treasury"),
            authority=budgets.get("authority", "Tech_OS"),
            observed_at=obs,
            evidence_refs=budgets.get("evidence_refs", ["github://Amdkn/Aspace_OS_V3#404"]),
            freshness_seconds=freshness_seconds,
        ),
        "evidence": [
            project_truth(
                value=ev.get("value"),
                source=ev.get("source", "evidence_pack"),
                authority=ev.get("authority", "Tech_OS"),
                observed_at=obs,
                evidence_refs=ev.get("evidence_refs", ["uc.db"]),
                freshness_seconds=freshness_seconds,
            )
            for ev in evidence
        ],
        "workgraph": [
            project_truth(
                value=wg.get("value"),
                source=wg.get("source", "supabase.workgraph"),
                authority=wg.get("authority", "Tech_OS"),
                observed_at=obs,
                evidence_refs=wg.get("evidence_refs", ["workgraph://claim"]),
                freshness_seconds=freshness_seconds,
            )
            for wg in workgraph_tasks
        ],
    }


def build_life_os_wall(
    *,
    holons_a1_a2_a3: List[Dict[str, Any]],
    frameworks: Dict[str, Dict[str, Any]],  # Ikigai, 12WY, Life Wheel, PARA, GTD, DEAL
    actor_registry: ActorRegistry,
    observed_at: Optional[Any] = None,
    freshness_seconds: int = 3600,
) -> Dict[str, Any]:
    now = datetime.now(timezone.utc)
    obs = observed_at or now

    required_fw = ["Ikigai", "12WY", "Life Wheel", "PARA", "GTD", "DEAL"]
    projected_frameworks = {}
    for fw_name in required_fw:
        fw_data = frameworks.get(fw_name, {})
        projected_frameworks[fw_name] = project_truth(
            value={
                **fw_data.get("value", {}),
                "linear_link": fw_data.get("linear_link", f"https://linear.app/aspace/issue/LIFE-{fw_name}"),
                "gws_link": fw_data.get("gws_link", f"https://drive.google.com/aspace/{fw_name}"),
            },
            source=fw_data.get("source", f"life_os.{fw_name.lower().replace(' ', '_')}"),
            authority=fw_data.get("authority", "Life_OS"),
            observed_at=obs,
            evidence_refs=fw_data.get("evidence_refs", [f"github://Amdkn/Life-OS-2026#{fw_name}"]),
            freshness_seconds=freshness_seconds,
        )

    return {
        "wall": "Life OS",
        "holons": [
            project_truth(
                value={
                    **h.get("value", {}),
                    "actor_ref": actor_registry.get_actor(h["value"].get("actor_id"))
                    if "actor_id" in h.get("value", {})
                    else None,
                },
                source=h.get("source", "life_os.holons"),
                authority=h.get("authority", "Life_OS"),
                observed_at=obs,
                evidence_refs=h.get("evidence_refs", ["github://Amdkn/Life-OS-2026"]),
                freshness_seconds=freshness_seconds,
            )
            for h in holons_a1_a2_a3
        ],
        "frameworks": projected_frameworks,
    }


def build_business_os_wall(
    *,
    holons_b1_b2_b3: List[Dict[str, Any]],
    franchises_products_domains: List[Dict[str, Any]],
    engineering_and_ops_state: Dict[str, Any],
    actor_registry: ActorRegistry,
    observed_at: Optional[Any] = None,
    freshness_seconds: int = 3600,
) -> Dict[str, Any]:
    now = datetime.now(timezone.utc)
    obs = observed_at or now

    return {
        "wall": "Business OS",
        "holons": [
            project_truth(
                value={
                    **h.get("value", {}),
                    "actor_ref": actor_registry.get_actor(h["value"].get("actor_id"))
                    if "actor_id" in h.get("value", {})
                    else None,
                },
                source=h.get("source", "business_os.holons"),
                authority=h.get("authority", "Business_OS"),
                observed_at=obs,
                evidence_refs=h.get("evidence_refs", ["github://Amdkn/Aspace_OS_V3#272"]),
                freshness_seconds=freshness_seconds,
            )
            for h in holons_b1_b2_b3
        ],
        "franchises_products_domains": [
            project_truth(
                value=fpd.get("value"),
                source=fpd.get("source", "business_os.domains"),
                authority=fpd.get("authority", "Business_OS"),
                observed_at=obs,
                evidence_refs=fpd.get("evidence_refs", ["github://omk-services/OMK-DESKTOP-WEB-OS"]),
                freshness_seconds=freshness_seconds,
            )
            for fpd in franchises_products_domains
        ],
        "engineering_and_ops_state": project_truth(
            value=engineering_and_ops_state.get("value", engineering_and_ops_state),
            source=engineering_and_ops_state.get("source", "business_os.ops"),
            authority=engineering_and_ops_state.get("authority", "Business_OS"),
            observed_at=obs,
            evidence_refs=engineering_and_ops_state.get("evidence_refs", ["github://Amdkn/Aspace_OS_V3#284"]),
            freshness_seconds=freshness_seconds,
        ),
    }


class CubeFarmTriWallProjection:
    """CubeFarm Tri-Wall projection engine & canary state manager."""

    def __init__(self, storage_filepath: Optional[str] = None) -> None:
        self.storage_filepath = storage_filepath or "10_Tech_OS/kernel/cubefarm_triwall_state.json"
        self.actor_registry = ActorRegistry()
        self.agent_wall: Optional[Dict[str, Any]] = None
        self.life_wall: Optional[Dict[str, Any]] = None
        self.business_wall: Optional[Dict[str, Any]] = None
        self.canary_state: Optional[Dict[str, Any]] = None

    def render_triwall(
        self,
        *,
        agent_data: Dict[str, Any],
        life_data: Dict[str, Any],
        business_data: Dict[str, Any],
        canary_desk: Optional[Dict[str, Any]] = None,
        observed_at: Optional[Any] = None,
    ) -> Dict[str, Any]:
        obs = observed_at or datetime.now(timezone.utc)

        self.agent_wall = build_agent_os_wall(
            capabilities=agent_data.get("capabilities", []),
            adapters=agent_data.get("adapters", []),
            harness_bodies=agent_data.get("harness_bodies", []),
            budgets=agent_data.get("budgets", {}),
            evidence=agent_data.get("evidence", []),
            workgraph_tasks=agent_data.get("workgraph_tasks", []),
            actor_registry=self.actor_registry,
            observed_at=obs,
        )

        self.life_wall = build_life_os_wall(
            holons_a1_a2_a3=life_data.get("holons", []),
            frameworks=life_data.get("frameworks", {}),
            actor_registry=self.actor_registry,
            observed_at=obs,
        )

        self.business_wall = build_business_os_wall(
            holons_b1_b2_b3=business_data.get("holons", []),
            franchises_products_domains=business_data.get("domains", []),
            engineering_and_ops_state=business_data.get("ops_state", {}),
            actor_registry=self.actor_registry,
            observed_at=obs,
        )

        if canary_desk:
            desk_actor = canary_desk.get("actor_id", "Ryan")
            self.canary_state = {
                "agent_desk": project_truth(
                    value={
                        "desk_id": canary_desk.get("desk_id", "desk_ryan_s3"),
                        "actor_id": desk_actor,
                        "actor_ref": self.actor_registry.get_actor(desk_actor),
                        "active_runtimes": canary_desk.get("runtimes", ["Hermes", "Codex", "Jules"]),
                        "current_mission": canary_desk.get("mission", "Issue #416 CubeFarm Tri-Wall"),
                        "return_to": canary_desk.get("return_to", "#403"),
                    },
                    source="cubefarm.desk",
                    authority="Tech_OS",
                    observed_at=obs,
                    evidence_refs=["github://Amdkn/Aspace_OS_V3#416", "github://Amdkn/Aspace_OS_V3#403"],
                    freshness_seconds=86400,
                ),
                "life_framework_projection": self.life_wall["frameworks"].get("12WY"),
                "business_hierarchy_projection": self.business_wall["holons"][0] if self.business_wall["holons"] else None,
            }

        return self.to_dict()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "schema": "aspace.cubefarm-triwall.v1",
            "actors": self.actor_registry.to_dict(),
            "agent_wall": self.agent_wall,
            "life_wall": self.life_wall,
            "business_wall": self.business_wall,
            "canary_state": self.canary_state,
        }

    def save_triwall_state(self, filepath: Optional[str] = None) -> str:
        target = filepath or self.storage_filepath
        dirpath = os.path.dirname(target)
        if dirpath:
            os.makedirs(dirpath, exist_ok=True)
        data = self.to_dict()
        with open(target, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        return target

    def load_triwall_state(self, filepath: Optional[str] = None) -> Dict[str, Any]:
        target = filepath or self.storage_filepath
        with open(target, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.actor_registry.load_dict(data.get("actors", {}))
        self.agent_wall = data.get("agent_wall")
        self.life_wall = data.get("life_wall")
        self.business_wall = data.get("business_wall")
        self.canary_state = data.get("canary_state")
        return data
