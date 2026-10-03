"""Cognitive Treasury & ResourceProfile for A'Space OS V3.

Manages heterogeneous compute/model resource profiles (FreeLLMAPI, Claude, Codex, DeepSeek, Qwen, etc.),
meters token fuel against active missions with valid leases, and keeps identity distinct from
runtime choice and resource budget.
"""
from __future__ import annotations

import datetime
import uuid
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional


@dataclass
class ResourceProfile:
    profile_id: str
    provider_name: str  # e.g., FreeLLMAPI, OpenAI, Anthropic, DeepSeek, Qwen, Z.ai
    runtime_id: str     # e.g., freellmapi-default, claude-code-v1, codex-chatgpt-web, deepseek-r1
    model_name: str     # e.g., gpt-4o, claude-3-7-sonnet, deepseek-r1, qwen-2.5-coder
    total_token_budget: int
    consumed_tokens: int = 0
    quota_status: str = "OK"  # "OK", "EXHAUSTED", "BACKPRESSURE"
    cost_per_1k_tokens: float = 0.0
    latency_ms: float = 0.0
    reliability_score: float = 1.0
    supported_capabilities: List[str] = field(default_factory=list)

    @property
    def remaining_budget(self) -> int:
        return max(0, self.total_token_budget - self.consumed_tokens)


@dataclass
class EvidenceReceipt:
    receipt_id: str
    work_id: Optional[int]
    correlation_id: str
    actor_id: str
    runtime_id: str
    provider_name: str
    action: str
    status: str
    tokens_consumed: int
    observed_effect: str
    observed_at: str = field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc).isoformat())
    evidence_refs: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


class CognitiveTreasuryError(Exception):
    pass


class CognitiveTreasury:
    def __init__(self):
        self._profiles: Dict[str, ResourceProfile] = {}

    def register_profile(self, profile: ResourceProfile) -> None:
        self._profiles[profile.profile_id] = profile

    def get_profile(self, profile_id: str) -> Optional[ResourceProfile]:
        return self._profiles.get(profile_id)

    def list_profiles(self) -> List[ResourceProfile]:
        return list(self._profiles.values())

    def consume_tokens(
        self,
        profile_id: str,
        token_count: int,
        *,
        has_active_mission: bool,
        has_valid_lease: bool,
        is_idle_loop: bool = False,
    ) -> int:
        """Meter token fuel. Rejects consumption from heartbeat/idle loops without active mission + lease."""
        if is_idle_loop or not has_active_mission or not has_valid_lease:
            raise CognitiveTreasuryError(
                "Token burn rejected: requires active mission + valid lease (heartbeat/idle loop burning is prohibited)."
            )

        profile = self.get_profile(profile_id)
        if not profile:
            raise CognitiveTreasuryError(f"ResourceProfile '{profile_id}' not found.")

        if profile.remaining_budget < token_count:
            profile.quota_status = "EXHAUSTED"
            raise CognitiveTreasuryError(
                f"Quota exhausted for profile '{profile_id}': required {token_count}, remaining {profile.remaining_budget}."
            )

        profile.consumed_tokens += token_count
        if profile.remaining_budget == 0:
            profile.quota_status = "EXHAUSTED"

        return profile.remaining_budget

    def record_action_effect(
        self,
        *,
        work_id: Optional[int],
        correlation_id: str,
        actor_id: str,
        profile_id: str,
        action: str,
        tokens_consumed: int,
        observed_effect: str,
        status: str = "SUCCESS",
        has_active_mission: bool = True,
        has_valid_lease: bool = True,
        evidence_refs: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> EvidenceReceipt:
        """Execute action, consume metered tokens, and return an EvidenceReceipt."""
        self.consume_tokens(
            profile_id,
            tokens_consumed,
            has_active_mission=has_active_mission,
            has_valid_lease=has_valid_lease,
            is_idle_loop=False,
        )

        profile = self.get_profile(profile_id)
        runtime_id = profile.runtime_id if profile else "unknown"
        provider_name = profile.provider_name if profile else "unknown"

        receipt = EvidenceReceipt(
            receipt_id=f"rec-{uuid.uuid4().hex[:8]}",
            work_id=work_id,
            correlation_id=correlation_id,
            actor_id=actor_id,
            runtime_id=runtime_id,
            provider_name=provider_name,
            action=action,
            status=status,
            tokens_consumed=tokens_consumed,
            observed_effect=observed_effect,
            evidence_refs=evidence_refs or [],
            metadata=metadata or {},
        )
        return receipt

    def get_projection(self, actor_id: str, profile_id: str) -> Dict[str, Any]:
        """Display runtime choice and remaining resource budget separately from identity."""
        profile = self.get_profile(profile_id)
        if not profile:
            raise CognitiveTreasuryError(f"Profile '{profile_id}' not found")

        return {
            "identity": {
                "actor_id": actor_id,
                "institutional_role": "Holon / Agent",
            },
            "runtime_choice": {
                "profile_id": profile.profile_id,
                "runtime_id": profile.runtime_id,
                "provider": profile.provider_name,
                "model": profile.model_name,
            },
            "resource_budget": {
                "total_token_budget": profile.total_token_budget,
                "consumed_tokens": profile.consumed_tokens,
                "remaining_budget": profile.remaining_budget,
                "quota_status": profile.quota_status,
            },
        }
