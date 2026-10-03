"""CubeFarm integration for A'Space OS V3 Kernel.

ADR-0388: CubeFarm is an instrument of Ryan, bounded by FactoryExecution envelopes.
It is NOT a new institutional agent.
"""
import dataclasses
import json
from typing import Optional, Dict, Any, List

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
    remaining_budget: Optional[int] = None

    def to_json(self) -> str:
        return json.dumps(dataclasses.asdict(self))

    @classmethod
    def from_json(cls, data: str) -> "FactoryExecution":
        return cls(**json.loads(data))
