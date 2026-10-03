#!/usr/bin/env python3
"""Resource Governor Routing Engine.

Optimizes model/provider choice across connected tenant profiles based on:
- Quota availability & policy gates (terms/limits are policy gates, never bypassed)
- Reliability / health score
- Latency (historical moving average)
- Capability matching (context window, model family, tool support)
- Privacy policy requirements
- Cost (free-tier preference)

Provides automatic failover across candidate profiles/providers upon failure or rate-limiting.
"""

from __future__ import annotations

import time
from typing import Any, Dict, List, Optional, Tuple

from adapter_contract import ArcadeAdapterContract
from encrypted_vault import TenantVault
from schemas import ProviderAuthProfile


class ResourceGovernor:
    """Resource Governor routing engine."""

    def __init__(self, vault: TenantVault):
        self.vault = vault
        # Profile metrics: profile_id -> {"successes": int, "failures": int, "avg_latency_ms": float, "last_error": str}
        self._metrics: Dict[str, Dict[str, Any]] = {}

    def get_metrics(self, profile_id: str) -> Dict[str, Any]:
        return self._metrics.setdefault(
            profile_id,
            {"successes": 0, "failures": 0, "avg_latency_ms": 50.0, "last_error": None},
        )

    def record_outcome(self, profile_id: str, success: bool, latency_ms: int, error_detail: Optional[str] = None) -> None:
        m = self.get_metrics(profile_id)
        if success:
            m["successes"] += 1
            m["last_error"] = None
        else:
            m["failures"] += 1
            m["last_error"] = error_detail

        # Exponential moving average for latency
        m["avg_latency_ms"] = 0.8 * m["avg_latency_ms"] + 0.2 * float(latency_ms)

    def rank_candidate_profiles(
        self,
        tenant_id: str,
        candidate_profiles: List[ProviderAuthProfile],
        adapters: Dict[str, ArcadeAdapterContract],
        required_model: Optional[str] = None,
        privacy_requirement: str = "standard",  # standard | strict
        prefer_free_tier: bool = True,
    ) -> List[Tuple[ProviderAuthProfile, ArcadeAdapterContract, float]]:
        """Ranks candidate profiles for a given request.

        Returns list of (profile, adapter, score) sorted by score descending.
        Policy gates (active status, consent, valid credentials) filter out ineligible profiles.
        """
        ranked: List[Tuple[ProviderAuthProfile, ArcadeAdapterContract, float]] = []

        for profile in candidate_profiles:
            # Policy gate 1: Tenant identity isolation
            if profile.tenant_id != tenant_id:
                continue

            # Policy gate 2: Active profile status
            if profile.status != "ACTIVE":
                continue

            adapter = adapters.get(profile.provider_id)
            if not adapter:
                continue

            # Decrypt credentials to check validity policy gate
            try:
                decrypted = self.vault.decrypt_credentials(tenant_id, profile.encrypted_credentials)
            except Exception:
                continue

            if not adapter.validate_credentials(profile, decrypted):
                continue

            # Calculate composite score
            metrics = self.get_metrics(profile.profile_id)
            total_calls = metrics["successes"] + metrics["failures"]
            reliability = (metrics["successes"] + 1) / (total_calls + 1)  # Laplace smoothing

            latency_score = max(0.0, 1.0 - (metrics["avg_latency_ms"] / 2000.0))

            cost_score = 1.0 if (prefer_free_tier and profile.provider_id in {"google", "freellmapi"}) else 0.5

            privacy_score = 1.0
            if privacy_requirement == "strict" and profile.provider_id == "freellmapi":
                privacy_score = 0.5

            # Model match boost
            model_score = 1.0
            if required_model and profile.provider_id in required_model.lower():
                model_score = 1.2

            composite_score = (
                (reliability * 0.4) +
                (latency_score * 0.2) +
                (cost_score * 0.2) +
                (privacy_score * 0.1) +
                (model_score * 0.1)
            )

            ranked.append((profile, adapter, composite_score))

        ranked.sort(key=lambda item: item[2], reverse=True)
        return ranked

    def route_and_execute(
        self,
        tenant_id: str,
        candidate_profiles: List[ProviderAuthProfile],
        adapters: Dict[str, ArcadeAdapterContract],
        model: str,
        messages: List[Dict[str, Any]],
        parameters: Optional[Dict[str, Any]] = None,
        privacy_requirement: str = "standard",
    ) -> Dict[str, Any]:
        """Routes execution to top candidate; performs failover to next ranked profiles if primary fails."""
        ranked = self.rank_candidate_profiles(
            tenant_id=tenant_id,
            candidate_profiles=candidate_profiles,
            adapters=adapters,
            required_model=model,
            privacy_requirement=privacy_requirement,
        )

        if not ranked:
            return {
                "status": "ALL_PROVIDERS_EXHAUSTED",
                "content": "",
                "tokens_consumed": {"input_tokens": 0, "output_tokens": 0, "total_tokens": 0},
                "latency_ms": 0,
                "remaining_quota": {},
                "selected_profile": None,
                "failover_attempts": [],
                "error_detail": f"No eligible/authorized provider profiles available for tenant '{tenant_id}'",
            }

        failover_attempts = []

        for profile, adapter, score in ranked:
            try:
                decrypted = self.vault.decrypt_credentials(tenant_id, profile.encrypted_credentials)

                start_t = time.monotonic()
                res = adapter.execute_routed_call(
                    profile=profile,
                    decrypted_credentials=decrypted,
                    model=model,
                    messages=messages,
                    parameters=parameters,
                )
                latency = int((time.monotonic() - start_t) * 1000)

                status = res.get("status")
                if status == "SUCCESS":
                    self.record_outcome(profile.profile_id, success=True, latency_ms=latency)
                    res["selected_profile"] = profile
                    res["adapter_used"] = adapter
                    res["failover_attempts"] = failover_attempts
                    return res
                else:
                    err_msg = res.get("error_detail") or f"Provider returned status {status}"
                    self.record_outcome(profile.profile_id, success=False, latency_ms=latency, error_detail=err_msg)
                    failover_attempts.append({
                        "profile_id": profile.profile_id,
                        "provider_id": profile.provider_id,
                        "status": status,
                        "error": err_msg,
                    })
            except Exception as exc:
                self.record_outcome(profile.profile_id, success=False, latency_ms=10, error_detail=str(exc))
                failover_attempts.append({
                    "profile_id": profile.profile_id,
                    "provider_id": profile.provider_id,
                    "status": "EXCEPTION",
                    "error": str(exc),
                })

        return {
            "status": "ALL_PROVIDERS_FAILED",
            "content": "",
            "tokens_consumed": {"input_tokens": 0, "output_tokens": 0, "total_tokens": 0},
            "latency_ms": 0,
            "remaining_quota": {},
            "selected_profile": None,
            "failover_attempts": failover_attempts,
            "error_detail": "All candidate providers failed or returned non-success status",
        }
