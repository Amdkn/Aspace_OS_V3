from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict

from jsonschema import Draft202012Validator, FormatChecker

SCHEMA_PATH = (
    Path(__file__).resolve().parents[1]
    / "contracts"
    / "INTER_FABRIC_ENVELOPE_V1.schema.json"
)


class InterFabricInvariantError(ValueError):
    pass


def _schema() -> Dict[str, Any]:
    with SCHEMA_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


_VALIDATOR = Draft202012Validator(_schema(), format_checker=FormatChecker())


def validate_envelope(envelope: Dict[str, Any]) -> Dict[str, Any]:
    _VALIDATOR.validate(envelope)
    return envelope


def validate_translation(
    source: Dict[str, Any],
    target: Dict[str, Any],
    *,
    allow_truth_resolution: bool = False,
) -> Dict[str, Any]:
    validate_envelope(source)
    validate_envelope(target)

    if source["mission"]["correlation_id"] != target["mission"]["correlation_id"]:
        raise InterFabricInvariantError("correlation_id changed in transport")

    if source["identity"]["holon_id"] != target["identity"]["holon_id"]:
        raise InterFabricInvariantError("institutional holon identity changed in transport")

    source_scope = set(source["authority"]["authority_scope"])
    target_scope = set(target["authority"]["authority_scope"])
    if not target_scope.issubset(source_scope):
        raise InterFabricInvariantError("authority widened in transport")

    source_cap = source.get("capability")
    target_cap = target.get("capability")
    if source_cap is not None:
        if target_cap is None:
            raise InterFabricInvariantError("capability identity was dropped")
        for field in ("capability_id", "capability_version"):
            if source_cap[field] != target_cap[field]:
                raise InterFabricInvariantError(f"{field} changed in transport")

    source_effect = source.get("effect")
    target_effect = target.get("effect")
    if source_effect and target_effect:
        for field in ("operation_id", "effect_id"):
            value = source_effect.get(field)
            if value is not None and value != target_effect.get(field):
                raise InterFabricInvariantError(f"{field} changed in transport")

    source_evidence = set(source["truth"]["evidence_refs"])
    target_evidence = set(target["truth"]["evidence_refs"])
    if not source_evidence.issubset(target_evidence):
        raise InterFabricInvariantError("evidence lineage was dropped")

    if (
        source["truth"]["epistemic_state"] == "UNKNOWN"
        and target["truth"]["epistemic_state"] != "UNKNOWN"
        and not allow_truth_resolution
    ):
        raise InterFabricInvariantError("UNKNOWN was coerced during transport")

    if source["routing"]["return_to"] != target["routing"]["return_to"]:
        raise InterFabricInvariantError("return_to changed in transport")

    return target


def translated_copy(source: Dict[str, Any], payload_ref: str, payload_type: str) -> Dict[str, Any]:
    target = deepcopy(source)
    target["payload"]["ref"] = payload_ref
    target["compatibility"]["payload_type"] = payload_type
    return validate_translation(source, target)
