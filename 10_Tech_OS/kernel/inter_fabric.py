import json
import os
import jsonschema
from typing import Dict, Any, Optional

SCHEMA_PATH = os.path.join(
    os.path.dirname(__file__),
    "contracts/INTER_FABRIC_ENVELOPE_V1.schema.json"
)

def _load_schema() -> Dict[str, Any]:
    with open(SCHEMA_PATH, "r") as f:
        return json.load(f)

_schema = _load_schema()

class InterFabricEnvelope:
    """Wrapper class to parse, validate, and serialize inter-fabric envelopes."""
    def __init__(self, raw: Dict[str, Any]):
        self.raw = raw
        self.validate(self.raw)

    @classmethod
    def validate(cls, instance: Dict[str, Any]) -> None:
        """Validate an instance against the schema."""
        jsonschema.validate(instance=instance, schema=_schema)

    @classmethod
    def create(
        cls,
        *,
        identity: Dict[str, Any],
        mission: Dict[str, Any],
        capability: Dict[str, Any],
        authority: Dict[str, Any],
        resource: Dict[str, Any],
        effect: Dict[str, Any],
        truth: Dict[str, Any],
        routing: Dict[str, Any],
        compatibility: Dict[str, Any],
        payload: Dict[str, Any]
    ) -> "InterFabricEnvelope":
        envelope = {
            "identity": identity,
            "mission": mission,
            "capability": capability,
            "authority": authority,
            "resource": resource,
            "effect": effect,
            "truth": truth,
            "routing": routing,
            "compatibility": compatibility,
            "payload": payload
        }
        return cls(envelope)

    def to_dict(self) -> Dict[str, Any]:
        return self.raw

    def get_correlation_id(self) -> str:
        return self.raw["mission"]["correlation_id"]

    def get_epistemic_state(self) -> str:
        return self.raw["truth"]["epistemic_state"]

    def set_epistemic_state(self, state: str) -> None:
        if state not in {"CURRENT", "STALE", "UNKNOWN"}:
            raise ValueError(f"Invalid epistemic state: {state}")
        self.raw["truth"]["epistemic_state"] = state

    def clone_with_payload(self, new_payload: Dict[str, Any], **kwargs) -> "InterFabricEnvelope":
        """Clone the envelope, updating the payload and potentially other fields."""
        import copy
        new_raw = copy.deepcopy(self.raw)
        new_raw["payload"] = new_payload

        for section, updates in kwargs.items():
            if section in new_raw and isinstance(updates, dict):
                new_raw[section].update(updates)

        # Re-validate
        return type(self)(new_raw)
