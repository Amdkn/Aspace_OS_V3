"""Provider-neutral execution boundary for bounded S3 runtimes.

Issue #560: Jules is a provider behind A'Space authority, never a backlog
scanner or merge authority. This module is intentionally transport-only: it
does not call Jules or any external provider unless an explicit canary gate
and injected provider callable are both supplied.
"""

from __future__ import annotations

import copy
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, Optional

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = Path(__file__).resolve().parent / "contracts" / "PROVIDER_EXECUTION_PACKET_V1.schema.json"
AUTHORITY_PROFILES = ROOT / "github_app_system1" / "authority_profiles.json"

with SCHEMA_PATH.open("r", encoding="utf-8") as handle:
    _SCHEMA = json.load(handle)


class ExecutionEligibilityError(ValueError):
    """Packet is structurally valid but not eligible for provider execution."""


class DuplicateLeaseError(ExecutionEligibilityError):
    """The dedup key already has an active lease."""


class CircuitBreakerOpen(ExecutionEligibilityError):
    """The dedup key is frozen pending an explicit recovery decision."""


@dataclass(frozen=True)
class PreparedProviderCall:
    provider: str
    dedup_key: str
    repo: str
    execution_cell_id: str
    lease_id: str
    payload: Dict[str, Any]


class ExecutionPacketV1:
    """Validated provider-neutral execution packet."""

    def __init__(self, raw: Dict[str, Any]):
        self.raw = copy.deepcopy(raw)
        self.validate(self.raw)
        self.validate_eligibility(self.raw)

    @staticmethod
    def validate(raw: Dict[str, Any]) -> None:
        jsonschema.validate(instance=raw, schema=_SCHEMA)

    @staticmethod
    def canonical_dedup_key(raw: Dict[str, Any]) -> str:
        cap_version = raw["capability_need"]["capability_version"]
        return "|".join(
            (
                raw["repo"],
                raw["execution_cell_id"],
                raw["base_sha"],
                cap_version,
            )
        )

    @classmethod
    def validate_eligibility(cls, raw: Dict[str, Any]) -> None:
        if raw["issue_or_subissue"]["kind"] != "EXECUTION_CELL":
            raise ExecutionEligibilityError(
                "provider execution requires a bounded EXECUTION_CELL"
            )

        expected = cls.canonical_dedup_key(raw)
        if raw["dedup_key"] != expected:
            raise ExecutionEligibilityError("dedup_key does not match canonical identity")

        if raw["authority_profile"] != "S3":
            raise ExecutionEligibilityError("provider authority must remain S3")

        if raw["retry_budget"] != 0:
            raise ExecutionEligibilityError("generic provider retry budget must be zero")

        if raw.get("human_blockers"):
            raise ExecutionEligibilityError("human-only blocker prevents provider execution")

        previous = raw.get("previous_failure")
        if previous and previous["code"] == "FAILED_PRECONDITION":
            if not previous.get("recovery_decision"):
                raise CircuitBreakerOpen(
                    "FAILED_PRECONDITION requires an explicit recovery decision"
                )

        expires_at = datetime.fromisoformat(
            raw["deadline_or_lease"]["expires_at"].replace("Z", "+00:00")
        )
        if expires_at.tzinfo is None:
            expires_at = expires_at.replace(tzinfo=timezone.utc)
        if expires_at <= datetime.now(timezone.utc):
            raise ExecutionEligibilityError("provider lease is expired")

        cls._validate_s3_authority_profile()

    @staticmethod
    def _validate_s3_authority_profile() -> None:
        with AUTHORITY_PROFILES.open("r", encoding="utf-8") as handle:
            doc = json.load(handle)
        profile = doc["profiles"]["s3"]
        permissions = profile.get("permissions", {})
        forbidden = set(doc["defaults"].get("forbidden_without_explicit_exception", []))
        widened = sorted(forbidden.intersection(permissions))
        if widened:
            raise ExecutionEligibilityError(
                f"S3 authority profile contains forbidden permissions: {widened}"
            )

    def to_dict(self) -> Dict[str, Any]:
        return copy.deepcopy(self.raw)

    def with_provider(self, provider: str) -> "ExecutionPacketV1":
        if not provider:
            raise ExecutionEligibilityError("provider name must be non-empty")
        clone = self.to_dict()
        clone["provider"] = provider
        return ExecutionPacketV1(clone)


class JulesExecutionPacket(ExecutionPacketV1):
    """Jules specialization of the provider-neutral packet."""

    def __init__(self, raw: Dict[str, Any]):
        super().__init__(raw)
        if self.raw["provider"] != "jules":
            raise ExecutionEligibilityError("JulesExecutionPacket requires provider=jules")


class ProviderLeaseRegistry:
    """Deterministic in-memory lease/dedup/circuit-breaker state for M0 tests.

    Persistence belongs to the durable coordination layer; this object only
    defines the provider semantics that a durable store must preserve.
    """

    def __init__(self) -> None:
        self._active: Dict[str, str] = {}
        self._frozen: Dict[str, str] = {}

    def admit(self, packet: ExecutionPacketV1) -> str:
        key = packet.raw["dedup_key"]
        if key in self._frozen:
            raise CircuitBreakerOpen(self._frozen[key])
        if key in self._active:
            raise DuplicateLeaseError(f"active lease already owns {key}")
        lease_id = packet.raw["deadline_or_lease"]["lease_id"]
        self._active[key] = lease_id
        return lease_id

    def release(self, packet: ExecutionPacketV1) -> None:
        self._active.pop(packet.raw["dedup_key"], None)

    def record_failure(self, packet: ExecutionPacketV1, code: str) -> None:
        key = packet.raw["dedup_key"]
        self._active.pop(key, None)
        if code == "FAILED_PRECONDITION":
            self._frozen[key] = (
                "FAILED_PRECONDITION circuit breaker open; recovery decision required"
            )

    def recover(self, packet: ExecutionPacketV1, decision: str) -> None:
        if not decision:
            raise ExecutionEligibilityError("recovery decision must be explicit")
        self._frozen.pop(packet.raw["dedup_key"], None)


class JulesProviderAdapter:
    """Prepares Jules calls but cannot execute a provider implicitly."""

    def __init__(
        self,
        provider_call: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]] = None,
    ) -> None:
        self._provider_call = provider_call

    def prepare(self, packet: JulesExecutionPacket) -> PreparedProviderCall:
        return PreparedProviderCall(
            provider="jules",
            dedup_key=packet.raw["dedup_key"],
            repo=packet.raw["repo"],
            execution_cell_id=packet.raw["execution_cell_id"],
            lease_id=packet.raw["deadline_or_lease"]["lease_id"],
            payload=packet.to_dict(),
        )

    def invoke(
        self,
        prepared: PreparedProviderCall,
        *,
        canary_gate: bool = False,
    ) -> Dict[str, Any]:
        if not canary_gate:
            raise ExecutionEligibilityError(
                "provider invocation disabled without explicit canary gate"
            )
        if self._provider_call is None:
            raise ExecutionEligibilityError("no provider transport is configured")
        return self._provider_call(copy.deepcopy(prepared.payload))
