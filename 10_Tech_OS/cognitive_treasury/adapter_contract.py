#!/usr/bin/env python3
"""Arcade-style Auth Provider Adapter Contract.

Defines the contract interface for federated authentication adapters
supporting OAuth 2.0 PKCE, API Key, and Bearer Token providers.
"""

from __future__ import annotations

import abc
from typing import Any, Dict, List, Optional

from schemas import ProviderAuthProfile


class ArcadeAdapterContract(abc.ABC):
    """Arcade-like authorization & execution adapter interface."""

    @property
    @abc.abstractmethod
    def provider_id(self) -> str:
        """Returns unique provider identifier (e.g., 'google', 'openai', 'anthropic')."""
        pass

    @property
    @abc.abstractmethod
    def auth_type(self) -> str:
        """Returns authentication type ('oauth2_pkce', 'api_key', 'bearer_token')."""
        pass

    @abc.abstractmethod
    def authorize_init(
        self,
        tenant_id: str,
        redirect_uri: Optional[str] = None,
        scopes: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """Initializes authorization flow.

        For OAuth 2.0 PKCE: generates PKCE verifier/challenge and authorization URL.
        For API Key: returns instructions/fields required from tenant.
        """
        pass

    @abc.abstractmethod
    def authorize_complete(
        self,
        tenant_id: str,
        auth_input: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Completes authorization flow.

        Exchanges auth code + PKCE verifier for tokens OR validates and stores API key.
        Returns:
        {
            "provider_account_id": str,
            "credentials": dict, # raw tokens/keys to be encrypted
            "scopes": list[str],
            "metadata": dict
        }
        """
        pass

    @abc.abstractmethod
    def validate_credentials(
        self,
        profile: ProviderAuthProfile,
        decrypted_credentials: Dict[str, Any],
    ) -> bool:
        """Validates if credentials are currently active and valid."""
        pass

    @abc.abstractmethod
    def refresh_credentials(
        self,
        profile: ProviderAuthProfile,
        decrypted_credentials: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Refreshes expired access tokens if supported; otherwise returns existing credentials."""
        pass

    @abc.abstractmethod
    def revoke(
        self,
        profile: ProviderAuthProfile,
        decrypted_credentials: Dict[str, Any],
    ) -> bool:
        """Revokes token / disconnects credential at the upstream provider if API supports it."""
        pass

    @abc.abstractmethod
    def execute_routed_call(
        self,
        profile: ProviderAuthProfile,
        decrypted_credentials: Dict[str, Any],
        model: str,
        messages: List[Dict[str, Any]],
        parameters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Executes model invocation using tenant-authorized credentials.

        Returns:
        {
            "status": "SUCCESS" | "RATE_LIMITED" | "UNAUTHORIZED" | "ERROR",
            "content": str,
            "tokens_consumed": {"input_tokens": int, "output_tokens": int, "total_tokens": int},
            "latency_ms": int,
            "remaining_quota": dict,
            "error_detail": str | None
        }
        """
        pass
