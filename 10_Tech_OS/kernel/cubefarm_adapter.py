"""CubeFarm integration for A'Space OS V3 Kernel.

ADR-0388: CubeFarm is an instrument of Ryan, bounded by FactoryExecution envelopes.
It is NOT a new institutional agent.

Issue #402: Sovereign Amdkn fork topology & ForkReceipt validation contract.
"""
import dataclasses
import json
from typing import Optional, Dict, Any, List

ALLOWED_CLASSIFICATIONS = {"KEEP", "REBUILD", "DROP"}

@dataclasses.dataclass
class FactoryExecution:
    actor_id: str
    doctor: str
    work_id: Optional[int]
    mission_id: Optional[str]
    issue_ref: Optional[str]
    operation_id: str
    correlation_id: str
    authority_envelope: Dict[str, Any]
    affected_resources: List[str]
    allowed_repos: List[str]
    allowed_effects: List[str]
    forbidden_effects: List[str]
    budget_lease: int
    session_limit: int
    runtime_choice: str
    qa_policy: str
    evidence_head: str
    return_to: str
    fencing_token: str

    def to_json(self) -> str:
        return json.dumps(dataclasses.asdict(self))

    @classmethod
    def from_json(cls, data: str) -> "FactoryExecution":
        return cls(**json.loads(data))


@dataclasses.dataclass
class ForkReceipt:
    work_id: int
    upstream_url: str
    origin_url: str
    baseline_sha: str
    local_clone_path: str
    integration_branch: str
    local_state_classification: Dict[str, str]
    upstream_sync_proof: Dict[str, Any]
    return_to: List[str]

    def validate(self) -> None:
        if "leonvanzyl/cubefarm" not in self.upstream_url:
            raise ValueError(f"Invalid upstream_url: {self.upstream_url}")
        if "Amdkn/cubefarm" not in self.origin_url:
            raise ValueError(f"Invalid origin_url: {self.origin_url}")
        if len(self.baseline_sha) != 40:
            raise ValueError(f"Invalid baseline_sha: {self.baseline_sha}")
        if self.integration_branch in {"main", "master"}:
            raise ValueError(f"Customizing upstream {self.integration_branch} directly is forbidden. Use a named integration branch.")
        for file_path, action in self.local_state_classification.items():
            if action not in ALLOWED_CLASSIFICATIONS:
                raise ValueError(f"Invalid classification for {file_path}: {action}. Must be one of {ALLOWED_CLASSIFICATIONS}")

    def to_json(self) -> str:
        self.validate()
        return json.dumps(dataclasses.asdict(self), indent=2)

    @classmethod
    def from_json(cls, data: str) -> "ForkReceipt":
        obj = cls(**json.loads(data))
        obj.validate()
        return obj
