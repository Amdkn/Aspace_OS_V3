#!/usr/bin/env python3
"""Anthropic API Key Provider Adapter.

Supports Anthropic identities via direct API key credentials.
"""

from __future__ import annotations

import time
from typing import Any, Dict, List, Optional

from adapter_contract import ArcadeAdapterContract
from schemas import ProviderAuthProfile


class AnthropicKeyAdapter(ArcadeAdapterContract):
    """Arcade-like Anthropic API Key Adapter."""

    @property
    def provider_id(self) -> str:
        return "anthropic"

    @property
    def auth_type(self) -> str:
        return "api_key"

    def authorize_init(
        self,
        tenant_id: str,
        redirect_uri: Optional[str] = None,
        scopes: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        return {
            "provider_id": self.provider_id,
            "auth_type": self.auth_type,
            "tenant_id": tenant_id,
            "instructions": "Provide your Anthropic API key (starts with 'sk-ant-')",
            "required_fields": ["api_key"],
        }

    def authorize_complete(
        self,
        tenant_id: str,
        auth_input: Dict[str, Any],
    ) -> Dict[str, Any]:
        api_key = auth_input.get("api_key", "").strip()
        if not api_key.startswith("sk-ant-"):
            raise ValueError("Invalid Anthropic API key format")

        account_id = f"anthropic:key:{api_key[-6:]}"

        return {
            "provider_account_id": account_id,
            "credentials": {
                "api_key": api_key,
            },
            "scopes": auth_input.get("scopes") or ["anthropic:messages"],
            "metadata": {"auth_mechanism": "api_key"},
        }

    def validate_credentials(
        self,
        profile: ProviderAuthProfile,
        decrypted_credentials: Dict[str, Any],
    ) -> bool:
        if profile.status != "ACTIVE":
            return False
        key = decrypted_credentials.get("api_key", "")
        return key.startswith("sk-ant-")

    def refresh_credentials(
        self,
        profile: ProviderAuthProfile,
        decrypted_credentials: Dict[str, Any],
    ) -> Dict[str, Any]:
        return decrypted_credentials

    def revoke(
        self,
        profile: ProviderAuthProfile,
        decrypted_credentials: Dict[str, Any],
    ) -> bool:
        decrypted_credentials.clear()
        profile.status = "REVOKED"
        return True

    def execute_routed_call(
        self,
        profile: ProviderAuthProfile,
        decrypted_credentials: Dict[str, Any],
        model: str,
        messages: List[Dict[str, Any]],
        parameters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        if not self.validate_credentials(profile, decrypted_credentials):
            return {
                "status": "UNAUTHORIZED",
                "content": "",
                "tokens_consumed": {"input_tokens": 0, "output_tokens": 0, "total_tokens": 0},
                "latency_ms": 10,
                "remaining_quota": {"remaining": 0, "unit": "usd_credit"},
                "error_detail": "Anthropic profile is inactive or revoked",
            }

        start_time = time.monotonic()
        prompt_str = " ".join(str(m.get("content", "")) for m in messages)
        in_tokens = max(15, len(prompt_str.split()))
        out_tokens = 60
        latency = int((time.monotonic() - start_time) * 1000) + 42

        return {
            "status": "SUCCESS",
            "content": f"[Anthropic {model} response via account {profile.provider_account_id}] Execution complete.",
            "tokens_consumed": {
                "input_tokens": in_tokens,
                "output_tokens": out_tokens,
                "total_tokens": in_tokens + out_tokens,
            },
            "latency_ms": latency,
            "remaining_quota": {
                "remaining_usd": 180.0,
                "unit": "usd_credit",
            },
            "error_detail": None,
        }
