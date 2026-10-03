#!/usr/bin/env python3
"""OpenAI API Key Provider Adapter.

Supports OpenAI identities via direct API key / project key credentials.
"""

from __future__ import annotations

import time
from typing import Any, Dict, List, Optional

from adapter_contract import ArcadeAdapterContract
from schemas import ProviderAuthProfile


class OpenAIKeyAdapter(ArcadeAdapterContract):
    """Arcade-like OpenAI API Key Adapter."""

    @property
    def provider_id(self) -> str:
        return "openai"

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
            "instructions": "Provide your OpenAI API key (starts with 'sk-')",
            "required_fields": ["api_key"],
            "optional_fields": ["org_id", "project_id"],
        }

    def authorize_complete(
        self,
        tenant_id: str,
        auth_input: Dict[str, Any],
    ) -> Dict[str, Any]:
        api_key = auth_input.get("api_key", "").strip()
        if not api_key.startswith("sk-") and not api_key.startswith("sk-proj-"):
            raise ValueError("Invalid OpenAI API key format")

        org_id = auth_input.get("org_id") or "org_default"
        account_id = f"openai:{org_id}:{api_key[-6:]}"

        return {
            "provider_account_id": account_id,
            "credentials": {
                "api_key": api_key,
                "org_id": org_id,
                "project_id": auth_input.get("project_id"),
            },
            "scopes": auth_input.get("scopes") or ["openai:chat:completion", "openai:embeddings"],
            "metadata": {"org_id": org_id, "auth_mechanism": "api_key"},
        }

    def validate_credentials(
        self,
        profile: ProviderAuthProfile,
        decrypted_credentials: Dict[str, Any],
    ) -> bool:
        if profile.status != "ACTIVE":
            return False
        key = decrypted_credentials.get("api_key", "")
        return key.startswith("sk-") or key.startswith("sk-proj-")

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
                "error_detail": "OpenAI profile is inactive or revoked",
            }

        start_time = time.monotonic()
        prompt_str = " ".join(str(m.get("content", "")) for m in messages)
        in_tokens = max(12, len(prompt_str.split()))
        out_tokens = 50
        latency = int((time.monotonic() - start_time) * 1000) + 35

        return {
            "status": "SUCCESS",
            "content": f"[OpenAI {model} response via account {profile.provider_account_id}] Execution complete.",
            "tokens_consumed": {
                "input_tokens": in_tokens,
                "output_tokens": out_tokens,
                "total_tokens": in_tokens + out_tokens,
            },
            "latency_ms": latency,
            "remaining_quota": {
                "remaining_usd": 250.0,
                "unit": "usd_credit",
                "org_id": decrypted_credentials.get("org_id"),
            },
            "error_detail": None,
        }
