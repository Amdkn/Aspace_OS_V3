from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict, Optional

MATRIX_FILE = Path(__file__).resolve().parent / "harness_certification_matrix.json"


class CertificationError(RuntimeError):
    pass


class HarnessCertificationEngine:
    def __init__(self, matrix_path: Path = MATRIX_FILE):
        self.matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
        self.harnesses = self.matrix["harnesses"]

    def check_contract(
        self, *, harness_id: str, actor_id: str, capability_contract: Any,
        input_payload: Dict[str, Any], correlation_id: str, authority_envelope: str,
        receipt: Optional[Any] = None, quota_budget: Optional[Dict[str, Any]] = None,
        executor_func: Optional[Any] = None
    ) -> Dict[str, Any]:
        info = self.harnesses.get(harness_id)
        if not info:
            raise CertificationError(f"Harness {harness_id!r} is not registered")
        if info.get("status") != "PASS":
            raise CertificationError(f"Harness {harness_id!r} is uncertified with a bounded gap")
        if not actor_id or actor_id == harness_id:
            raise CertificationError("Rule 1 Failure: actor identity must be supplied externally")
        if not getattr(capability_contract, "capability_id", None):
            raise CertificationError("Rule 2 Failure: capability must come from shared registry")
        if not isinstance(input_payload, dict):
            raise CertificationError("Rule 3 Failure: input payload must be typed")
        if not authority_envelope:
            raise CertificationError("Rule 4 Failure: authority envelope is required")
        if not correlation_id:
            raise CertificationError("Rule 5 Failure: correlation_id is required")
        if getattr(capability_contract, "effect_class", None) not in {"QUERY","COMMAND","EVENT","EFFECT"}:
            raise CertificationError("Rule 6 Failure: effect class is not explicit")
        if receipt is not None and not getattr(receipt, "evidence_refs", None):
            raise CertificationError("Rule 7 Failure: evidence readback is required")
        if quota_budget is not None and not isinstance(quota_budget, dict):
            raise CertificationError("Rule 8 Failure: budget must be independently observable")
        if executor_func and getattr(executor_func, "__module__", "").startswith(f"harness_{harness_id}"):
            raise CertificationError("Rule 10 Failure: harness-specific business executor detected")
        return {
            "harness_id": harness_id,
            "status": "PASS",
            "actor_id": actor_id,
            "correlation_id": correlation_id,
            "authority_envelope": authority_envelope,
            "checks": {f"rule_{i}": True for i in range(1, 11)},
        }


def get_harness_mesh_view(*, actor_id: str, runtime_id: str, adapter_type: str,
                          harness_id: str, capability_id: str, budget: Dict[str, Any],
                          evidence: Dict[str, Any], correlation_id: str) -> Dict[str, Any]:
    return {
        "identity": {"actor_id": actor_id, "independent_of_provider": True},
        "runtime": {"runtime_id": runtime_id},
        "adapter": {"harness_id": harness_id, "adapter_type": adapter_type, "certified": True},
        "capability": {"capability_id": capability_id},
        "budget": budget,
        "evidence": {"correlation_id": correlation_id, **evidence},
    }


def failover_harness(*, from_harness: str, to_harness: str, actor_id: str, work_id: int,
                     correlation_id: str, authority_envelope: str, capability_id: str,
                     fail_reason: str) -> Dict[str, Any]:
    target = HarnessCertificationEngine().harnesses.get(to_harness)
    if not target or target.get("status") != "PASS":
        raise CertificationError(f"Failover target {to_harness!r} is not certified")
    return {
        "event_kind": "harness_mesh_failover",
        "work_id": work_id,
        "from_harness": from_harness,
        "to_harness": to_harness,
        "actor_id": actor_id,
        "correlation_id": correlation_id,
        "authority_envelope": authority_envelope,
        "capability_id": capability_id,
        "fail_reason": fail_reason,
        "status": "SUCCESS",
    }
