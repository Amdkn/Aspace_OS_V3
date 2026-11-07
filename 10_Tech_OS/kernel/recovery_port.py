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

CLASSIFICATION_ROUTES = {
    "transient": "local_repair",
    "timeout": "backpressure",
    "adapter_bug": "local_repair",
    "merge_conflict": "local_repair",
    "quota_exhaustion": "backpressure",
    "repeated_recoverable_unknown": "auto_recovery",
    "sans_preuve": "preuve_manquante",
    "aucun_critere": "ruban_sans_critere",
    "execute_en_échec": "critere_execute_en_échec",
    "atteste_en_échec": "critere_atteste_en_échec",
    "sorti_sans_rendre": "harness_disparu",
    "error": "plantage_harness",
    "exception": "plantage_harness",
    "traceback": "plantage_harness",
}

class RecoveryPort:
    """Evaluates local recovery conditions before escalating to Donna DLQ.

    Returns one of five decisions:
      - RECOVER_LOCAL: local transient error within budget
      - WAIT: backpressure / temporal wait required
      - REQUEST_EVIDENCE: insufficient evidence to classify
      - REOPEN_LOCAL: local capability needs reopen/reconfigure
      - ESCALATE_DONNA: local recovery exhausted or irreducible error
    """

    @classmethod
    def evaluate(cls, request: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluates a recovery request and returns the routing decision."""
        jsonschema.validate(instance=request, schema=_schema)

        evidence = request["local_evidence"]
        budget = request["retry_budget"]
        error_type = evidence.get("error_type", "")
        effect_state = evidence.get("effect_state", "")

        # 1. UNKNOWN effect_state always bypasses blind retry -> ESCALATE_DONNA
        #    (it must go through recovery/reconciliation, never a blind RETRY)
        if effect_state == "UNKNOWN":
            return {
                "decision": "ESCALATE_DONNA",
                "reason": "irreducible UNKNOWN effect requires shared escalation",
                "escalation_target": "donna_shared_dlq",
            }

        # 2. Transient local errors: recover within budget
        if error_type in ("transient", "transient_error"):
            if budget["current_attempt"] < budget["max_attempts"]:
                return {
                    "decision": "RECOVER_LOCAL",
                    "reason": "local transient error within budget",
                    "max_attempts": budget["max_attempts"],
                    "current_attempt": budget["current_attempt"] + 1,
                }
            # Budget exhausted -> WAIT (backpressure) before re-evaluate
            return {
                "decision": "WAIT",
                "reason": "transient error budget exhausted, backpressure before retry",
                "wait_reason": "retry_budget_exhausted",
                "next_action": "re-evaluate_after_backpressure",
            }

        # 3. Effect is FAILED but error_type not recognized as transient
        #    -> REQUEST_EVIDENCE to gather more info before deciding
        if effect_state == "FAILED" and error_type not in CLASSIFICATION_ROUTES:
            return {
                "decision": "REQUEST_EVIDENCE",
                "reason": "effect FAILED with unclassified error_type, evidence needed",
                "evidence_requested": error_type,
                "next_steps": ["gather_local_evidence", "reclassify_error"],
            }

        # 4. Classified non-transient error types -> REOPEN_LOCAL capability reconfig
        if error_type in (
            "adapter_bug", "merge_conflict", "quota_exhaustion",
            "repeated_recoverable_unknown",
        ):
            return {
                "decision": "REOPEN_LOCAL",
                "reason": f"local capability needs reopen/reconfigure for {error_type}",
                "reopen_type": error_type,
                "policy_ref": "local_policy_v1",
            }

        # 5. All other classified error types -> escalate to Donna
        if error_type in CLASSIFICATION_ROUTES:
            return {
                "decision": "ESCALATE_DONNA",
                "reason": f"error classified as {error_type}, escalating to Donna DLQ",
                "classification": CLASSIFICATION_ROUTES[error_type],
                "escalation_target": "donna_shared_dlq",
            }

        # 6. Fallback: unknown error type with FAILED effect
        return {
            "decision": "ESCALATE_DONNA",
            "reason": "unrecognized error pattern, default escalation to Donna",
        }
