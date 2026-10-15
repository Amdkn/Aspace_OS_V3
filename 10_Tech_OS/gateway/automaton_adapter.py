"""Bounded Conway Automaton adapter for Gateway G2 (#545).

This is a contract adapter, not an Automaton installation. It maps an already
authorized A'Space ExecutionPacket + InterFabricEnvelope into the public
Automaton coding-harness semantics pinned at the audited upstream snapshot.
It deliberately excludes Automaton wallet, heartbeat, replication,
self-modification, provisioning and sovereign identity semantics.
"""

from __future__ import annotations

import copy
from dataclasses import asdict, dataclass
from typing import Any, Dict, List

from runtime_registry import RuntimeDescriptor

AUTOMATON_REPO = "Conway-Research/automaton"
AUTOMATON_SHA = "d8f816881fd24b6f5e3d616e59edec387a447667"
AUTOMATON_HARNESS = "coding"
AUTOMATON_ADAPTER_VERSION = "0.1.0"

PATCH_TOOLS = ["read_file", "list_dir", "patch_file", "write_file", "task_done"]
FORBIDDEN_ORGANS = [
    "wallet",
    "survival",
    "heartbeat",
    "replication",
    "self_modification",
    "provisioning",
    "domain_management",
    "on_chain_identity",
]
TARGET_MODES = {"LOCAL_ONLY", "REMOTE_ONLY"}


class AutomatonAdapterError(ValueError):
    """Fail-closed contract violation at the Automaton boundary."""


@dataclass(frozen=True)
class AutomatonBudget:
    max_turns: int
    max_cost_cents: int
    timeout_ms: int


@dataclass(frozen=True)
class AutomatonPatchRequest:
    runtime_id: str
    upstream_repo: str
    upstream_sha: str
    harness_id: str
    target_mode: str
    fallback_policy: str
    repo: str
    base_sha: str
    allowed_paths: List[str]
    mission_id: str
    work_id: Any
    execution_cell_id: str
    correlation_id: str
    return_to: str
    authority_profile: str
    policy_ref: str
    mutation_lease: str
    fencing_key: str
    operation_id: str
    idempotency_key: str
    budget: AutomatonBudget
    tool_allowlist: List[str]
    task: Dict[str, Any]


def automaton_descriptor() -> RuntimeDescriptor:
    return RuntimeDescriptor(
        runtime_id="automaton-public-pinned",
        adapter_id="gateway.automaton.coding",
        adapter_version=AUTOMATON_ADAPTER_VERSION,
        upstream_repo=AUTOMATON_REPO,
        upstream_sha=AUTOMATON_SHA,
        intrinsic_scale="M0",
        projected_scales=["M1", "M2"],
        capabilities=["code.patch"],
        forbidden_organs=list(FORBIDDEN_ORGANS),
        evidence_refs=[
            f"github:{AUTOMATON_REPO}@{AUTOMATON_SHA}",
            "docs:AUTOMATON_GATEWAY_M0_M1_M2_PROPOSAL.md",
        ],
    )


class AutomatonPatchAdapter:
    """Compile-only M1/M2 adapter for Automaton's public CodingHarness."""

    runtime_id = "automaton-public-pinned"

    @staticmethod
    def compile(
        packet: Dict[str, Any],
        envelope: Dict[str, Any],
        *,
        target_mode: str,
        budget: AutomatonBudget,
    ) -> AutomatonPatchRequest:
        if packet.get("provider") != "automaton":
            raise AutomatonAdapterError("ExecutionPacket provider must be automaton")
        if packet.get("authority_profile") != "S3":
            raise AutomatonAdapterError("Automaton adapter accepts bounded S3 authority only")
        if packet.get("provider_mode") != "CHANGESET_ONLY":
            raise AutomatonAdapterError("Automaton adapter is ChangeSet-only")
        if packet.get("retry_budget") != 0:
            raise AutomatonAdapterError("generic retries are forbidden")
        if packet.get("issue_or_subissue", {}).get("kind") != "EXECUTION_CELL":
            raise AutomatonAdapterError("only bounded execution cells may reach a runtime")
        if target_mode not in TARGET_MODES:
            raise AutomatonAdapterError("target must be explicit; AUTO/fallback targets are forbidden")
        if budget.max_turns <= 0 or budget.max_cost_cents < 0 or budget.timeout_ms <= 0:
            raise AutomatonAdapterError("A'Space budget must be explicit and bounded")

        mission = envelope.get("mission") or {}
        authority = envelope.get("authority") or {}
        effect = envelope.get("effect") or {}
        routing = envelope.get("routing") or {}
        capability = envelope.get("capability") or {}

        if mission.get("mission_id") != packet.get("mission_id"):
            raise AutomatonAdapterError("mission_id drift")
        if mission.get("work_id") != packet.get("work_id"):
            raise AutomatonAdapterError("work_id drift")
        if mission.get("cell_id") != packet.get("execution_cell_id"):
            raise AutomatonAdapterError("cell_id drift")
        if routing.get("return_to") != packet.get("return_to"):
            raise AutomatonAdapterError("return_to drift")

        if capability.get("capability_id") != "code.patch":
            raise AutomatonAdapterError("initial Automaton slice exposes only code.patch")
        if not authority.get("mutation_lease"):
            raise AutomatonAdapterError("mutation lease is required")
        if not authority.get("fencing_key"):
            raise AutomatonAdapterError("fencing key is required")
        if not authority.get("policy_ref"):
            raise AutomatonAdapterError("policy_ref is required")
        if not effect.get("operation_id") or not effect.get("idempotency_key"):
            raise AutomatonAdapterError("effect identity is required")
        if packet.get("effect_class") not in {"REVERSIBLE_MUTATION", "GOVERNED_MUTATION"}:
            raise AutomatonAdapterError("code.patch requires a governed reversible mutation")

        allowed_paths = packet.get("allowed_paths") or []
        if not allowed_paths:
            raise AutomatonAdapterError("allowed_paths cannot be empty")

        task = {
            "title": f"A'Space bounded patch cell {packet['execution_cell_id']}",
            "description": (
                "Produce a bounded code patch only inside allowed_paths. "
                "Do not provision infrastructure, modify identity, use wallets, "
                "replicate, self-modify the runtime, or change execution target."
            ),
            "id": str(packet["execution_cell_id"]),
            "goalId": str(packet["mission_id"]),
            "agentRole": "executor",
            "dependencies": [],
            "metadata": {
                "aspace_work_id": packet["work_id"],
                "aspace_correlation_id": mission.get("correlation_id"),
                "base_sha": packet["base_sha"],
                "allowed_paths": list(allowed_paths),
            },
        }

        return AutomatonPatchRequest(
            runtime_id=AutomatonPatchAdapter.runtime_id,
            upstream_repo=AUTOMATON_REPO,
            upstream_sha=AUTOMATON_SHA,
            harness_id=AUTOMATON_HARNESS,
            target_mode=target_mode,
            fallback_policy="DENY",
            repo=packet["repo"],
            base_sha=packet["base_sha"],
            allowed_paths=list(allowed_paths),
            mission_id=packet["mission_id"],
            work_id=packet["work_id"],
            execution_cell_id=packet["execution_cell_id"],
            correlation_id=mission["correlation_id"],
            return_to=packet["return_to"],
            authority_profile="S3",
            policy_ref=authority["policy_ref"],
            mutation_lease=authority["mutation_lease"],
            fencing_key=authority["fencing_key"],
            operation_id=effect["operation_id"],
            idempotency_key=effect["idempotency_key"],
            budget=budget,
            tool_allowlist=list(PATCH_TOOLS),
            task=task,
        )

    @staticmethod
    def normalize_result(
        request: AutomatonPatchRequest,
        provider_result: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Provider success never equals A'Space acceptance."""
        state = provider_result.get("state")
        if state in {"TIMEOUT", "DISCONNECTED", "TARGET_UNCERTAIN"}:
            return {
                "runtime_id": request.runtime_id,
                "operation_id": request.operation_id,
                "effect_state": "UNKNOWN",
                "provider_state": state,
                "acceptance_state": "PENDING_RECONCILIATION",
                "retry_safe": False,
                "return_to": request.return_to,
                "evidence": copy.deepcopy(provider_result.get("evidence", [])),
            }

        success = bool(provider_result.get("success"))
        return {
            "runtime_id": request.runtime_id,
            "operation_id": request.operation_id,
            "effect_state": "PROVIDER_REPORTED" if success else "FAILED",
            "provider_state": "REPORTED_SUCCESS" if success else "REPORTED_FAILURE",
            "acceptance_state": "PENDING_VERIFICATION" if success else "REVIEW_FAILURE",
            "retry_safe": False,
            "return_to": request.return_to,
            "artifacts": copy.deepcopy(provider_result.get("artifacts", [])),
            "evidence": copy.deepcopy(provider_result.get("evidence", [])),
            "cost_cents": provider_result.get("costCents"),
            "duration_ms": provider_result.get("duration"),
        }


def request_to_dict(request: AutomatonPatchRequest) -> Dict[str, Any]:
    return asdict(request)
