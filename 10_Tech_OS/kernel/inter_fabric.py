import copy
import json
import os
from typing import Any, Dict

import jsonschema

SCHEMA_PATH = os.path.join(
    os.path.dirname(__file__),
    "contracts/INTER_FABRIC_ENVELOPE_V1.schema.json",
)


def _load_schema() -> Dict[str, Any]:
    with open(SCHEMA_PATH, "r", encoding="utf-8") as handle:
        return json.load(handle)


_schema = _load_schema()


class InterFabricInvariantError(ValueError):
    """Raised when transport between fabrics mutates a cross-cutting invariant."""


class InterFabricEnvelope:
    """Validated V4 cross-fabric envelope.

    Fabric-specific payload semantics may change. Institutional identity,
    mission lineage, bounded authority, evidence lineage and return routing may not.
    """

    def __init__(self, raw: Dict[str, Any]):
        self.raw = raw
        self.validate(self.raw)

    @classmethod
    def validate(cls, instance: Dict[str, Any]) -> None:
        jsonschema.validate(instance=instance, schema=_schema)

    @classmethod
    def validate_translation(
        cls,
        source: Dict[str, Any],
        target: Dict[str, Any],
        *,
        allow_truth_resolution: bool = False,
    ) -> None:
        """Fail closed when a transport silently changes institutional coordinates."""
        cls.validate(source)
        cls.validate(target)

        for field in ("holon_id", "institutional_rank"):
            if source["identity"].get(field) != target["identity"].get(field):
                raise InterFabricInvariantError(f"identity.{field} changed in transport")

        # Embodiment/session refs are deliberately NOT invariant: a Holon must be
        # able to survive runtime/session replacement without changing identity.
        for field in (
            "mission_id",
            "work_id",
            "cell_id",
            "correlation_id",
            "parent_correlation_id",
        ):
            if source["mission"].get(field) != target["mission"].get(field):
                raise InterFabricInvariantError(f"mission.{field} changed in transport")

        source_capability = source.get("capability")
        target_capability = target.get("capability")
        if source_capability is not None:
            if target_capability is None:
                raise InterFabricInvariantError("capability was dropped in transport")
            for field in ("capability_id", "capability_version", "contract_ref"):
                if source_capability.get(field) != target_capability.get(field):
                    raise InterFabricInvariantError(
                        f"capability.{field} changed in transport"
                    )

        # V1 has no lattice for proving a safe authority narrowing. Exact
        # preservation is therefore the only fail-closed transport rule.
        if source["authority"] != target["authority"]:
            raise InterFabricInvariantError("authority envelope changed in transport")

        source_resource = source.get("resource")
        target_resource = target.get("resource")
        if source_resource is not None:
            if target_resource is None:
                raise InterFabricInvariantError("resource coordinates were dropped")
            for field in ("resource_lease_ref", "budget_lease_ref"):
                value = source_resource.get(field)
                if value is not None and value != target_resource.get(field):
                    raise InterFabricInvariantError(
                        f"resource.{field} changed in transport"
                    )

        source_effect = source.get("effect")
        target_effect = target.get("effect")
        if source_effect is not None:
            if target_effect is None:
                raise InterFabricInvariantError("effect coordinates were dropped")
            for field in (
                "operation_id",
                "effect_id",
                "effect_class",
                "idempotency_key",
                "replay_semantics",
            ):
                value = source_effect.get(field)
                if value is not None and value != target_effect.get(field):
                    raise InterFabricInvariantError(
                        f"effect.{field} changed in transport"
                    )

        for field in ("source_authority", "observed_at", "freshness"):
            if source["truth"].get(field) != target["truth"].get(field):
                raise InterFabricInvariantError(f"truth.{field} changed in transport")

        source_evidence = set(source["truth"].get("evidence_refs", []))
        target_evidence = set(target["truth"].get("evidence_refs", []))
        if not source_evidence.issubset(target_evidence):
            raise InterFabricInvariantError("truth.evidence_refs lost lineage")

        if (
            source["truth"].get("epistemic_state") == "UNKNOWN"
            and target["truth"].get("epistemic_state") != "UNKNOWN"
            and not allow_truth_resolution
        ):
            raise InterFabricInvariantError(
                "UNKNOWN was coerced without an explicit truth-resolution boundary"
            )

        for field in ("origin_layer", "return_to"):
            if source["routing"].get(field) != target["routing"].get(field):
                raise InterFabricInvariantError(f"routing.{field} changed in transport")

        if (
            source["compatibility"].get("envelope_version")
            != target["compatibility"].get("envelope_version")
        ):
            raise InterFabricInvariantError(
                "compatibility.envelope_version changed in transport"
            )

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
    ) -> "InterFabricEnvelope":
        return cls(
            {
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
        )

    def to_dict(self) -> Dict[str, Any]:
        return self.raw

    def get_correlation_id(self) -> str:
        return self.raw["mission"]["correlation_id"]

    def get_epistemic_state(self) -> str:
        return self.raw["truth"]["epistemic_state"]

    def clone_with_payload(
        self,
        new_payload: Dict[str, Any],
        *,
        allow_truth_resolution: bool = False,
        **updates: Dict[str, Any],
    ) -> "InterFabricEnvelope":
        new_raw = copy.deepcopy(self.raw)
        new_raw["payload"] = new_payload
        for section, section_updates in updates.items():
            if section in new_raw and isinstance(section_updates, dict):
                if new_raw[section] is None:
                    new_raw[section] = {}
                new_raw[section].update(section_updates)

        self.validate_translation(
            self.raw,
            new_raw,
            allow_truth_resolution=allow_truth_resolution,
        )
        return type(self)(new_raw)
