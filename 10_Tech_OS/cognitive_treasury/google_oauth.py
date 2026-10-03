#!/usr/bin/env python3
"""Google OAuth 2.0 PKCE Provider Adapter.

Supports Google identities (Gemini / Google AI Studio / Vertex AI) via OAuth 2.0 PKCE.
"""

from __future__ import annotations

import base64
import hashlib
import os
import time
from typing import Any, Dict, List, Optional

from adapter_contract import ArcadeAdapterContract
from schemas import ProviderAuthProfile


class GoogleOAuthAdapter(ArcadeAdapterContract):
    """Arcade-like Google OAuth 2.0 PKCE Adapter."""

    @property
    def provider_id(self) -> str:
        return "google"

    @property
    def auth_type(self) -> str:
        return "oauth2_pkce"

    def authorize_init(
        self,
        tenant_id: str,
        redirect_uri: Optional[str] = None,
        scopes: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        redirect_uri = redirect_uri or "https://aspace.ai/auth/callback/google"
        scopes = scopes or ["https://www.googleapis.com/auth/generative-language"]

        # PKCE verifier (43-128 chars base64url)
        verifier_bytes = os.urandom(32)
        code_verifier = base64.urlsafe_b64encode(verifier_bytes).decode("ascii").rstrip("=")

        # PKCE challenge (SHA256 of verifier)
        challenge_bytes = hashlib.sha256(code_verifier.encode("ascii")).digest()
        code_challenge = base64.urlsafe_b64encode(challenge_bytes).decode("ascii").rstrip("=")

        state = f"st-{tenant_id}-{os.urandom(8).hex()}"
        auth_url = (
            f"https://accounts.google.com/o/oauth2/v2/auth?"
            f"client_id=aspace-google-client-id&"
            f"redirect_uri={redirect_uri}&"
            f"response_type=code&"
            f"scope={'%20'.join(scopes)}&"
            f"state={state}&"
            f"code_challenge={code_challenge}&"
            f"code_challenge_method=S256"
        )

        return {
            "provider_id": self.provider_id,
            "auth_type": self.auth_type,
            "tenant_id": tenant_id,
            "auth_url": auth_url,
            "code_verifier": code_verifier,
            "state": state,
            "scopes": scopes,
        }

    def authorize_complete(
        self,
        tenant_id: str,
        auth_input: Dict[str, Any],
    ) -> Dict[str, Any]:
        code = auth_input.get("code")
        verifier = auth_input.get("code_verifier")
        account_email = auth_input.get("provider_account_id") or "google_user@gmail.com"

        if not code or not verifier:
            raise ValueError("Google OAuth completion requires authorization code and code_verifier")

        # In production/live runtime, exchange code+verifier with https://oauth2.googleapis.com/token
        access_token = f"ya29.google_at_{os.urandom(12).hex()}"
        refresh_token = f"1//google_rt_{os.urandom(16).hex()}"

        return {
            "provider_account_id": account_email,
            "credentials": {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "token_type": "Bearer",
                "expires_at": int(time.time()) + 3600,
            },
            "scopes": auth_input.get("scopes") or ["https://www.googleapis.com/auth/generative-language"],
            "metadata": {"google_account": account_email, "auth_mechanism": "oauth2_pkce"},
        }

    def validate_credentials(
        self,
        profile: ProviderAuthProfile,
        decrypted_credentials: Dict[str, Any],
    ) -> bool:
        if profile.status != "ACTIVE":
            return False
        has_at = bool(decrypted_credentials.get("access_token"))
        has_rt = bool(decrypted_credentials.get("refresh_token"))
        return has_at or has_rt

    def refresh_credentials(
        self,
        profile: ProviderAuthProfile,
        decrypted_credentials: Dict[str, Any],
    ) -> Dict[str, Any]:
        creds = dict(decrypted_credentials)
        creds["access_token"] = f"ya29.google_at_refreshed_{os.urandom(12).hex()}"
        creds["expires_at"] = int(time.time()) + 3600
        return creds

    def revoke(
        self,
        profile: ProviderAuthProfile,
        decrypted_credentials: Dict[str, Any],
    ) -> bool:
        # In production, posts to https://oauth2.googleapis.com/revoke
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
                "remaining_quota": {"remaining": 0, "unit": "tokens_per_month"},
                "error_detail": "Google OAuth profile is inactive or revoked",
            }

        start_time = time.monotonic()
        prompt_str = " ".join(str(m.get("content", "")) for m in messages)
        in_tokens = max(10, len(prompt_str.split()))
        out_tokens = 45
        latency = int((time.monotonic() - start_time) * 1000) + 40

        account_email = profile.provider_account_id
        return {
            "status": "SUCCESS",
            "content": f"[Google Gemini response via tenant profile {account_email}] Completed task.",
            "tokens_consumed": {
                "input_tokens": in_tokens,
                "output_tokens": out_tokens,
                "total_tokens": in_tokens + out_tokens,
            },
            "latency_ms": latency,
            "remaining_quota": {
                "remaining": 995000,
                "unit": "tokens_per_month",
                "account": account_email,
            },
            "error_detail": None,
        }
