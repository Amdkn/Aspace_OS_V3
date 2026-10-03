import json
import os
import jsonschema
from typing import Dict, Any

SCHEMA_PATH = os.path.join(
    os.path.dirname(__file__),
    "contracts/RECOVERY_PORT_CONTRACT_V1.schema.json"
)

def _load_schema() -> Dict[str, Any]:
    with open(SCHEMA_PATH, "r") as f:
        return json.load(f)

_schema = _load_schema()

class RecoveryPort:
    """Evaluates local recovery conditions before escalating to Donna DLQ."""

    @classmethod
    def evaluate(cls, request: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluates a recovery request and returns the routing decision."""
        jsonschema.validate(instance=request, schema=_schema)

        evidence = request["local_evidence"]
        budget = request["retry_budget"]

        # 1. Never blindly retry UNKNOWN effect. It must bypass reflexive retry
        #    and escalate or request evidence/reconcile.
        if evidence.get("effect_state") == "UNKNOWN":
            return {
                "decision": "ESCALATE_DONNA",
                "reason": "irreducible UNKNOWN effect requires shared escalation"
            }

        # 2. Transients (local repairable)
        if evidence.get("error_type") == "transient":
            if budget["current_attempt"] < budget["max_attempts"]:
                return {
                    "decision": "RECOVER_LOCAL",
                    "reason": "local transient error within budget"
                }

        # Exhausted budget or irreducible
        return {
            "decision": "ESCALATE_DONNA",
            "reason": "local recovery exhausted or irreducible error"
        }
