#!/usr/bin/env python3
"""Cognitive Treasury Token Broker.

Coordinates federated authorization, tenant-scoped encrypted credential storage,
Resource Governor routing, entitlement boundary checks, consent tracking,
audit logging, and mandatory ResourceReceipt emission.

Law: Pass criterion requires that a provider profile can be disconnected/revoked
without changing client identity or breaking other connected profiles.
"""

from __future__ import annotations

import datetime
import uuid
from typing import Any, Dict, List, Optional

from adapter_contract import ArcadeAdapterContract
from anthropic_key import AnthropicKeyAdapter
from encrypted_vault import TenantIsolationError, TenantVault
from entitlement_boundary import EntitlementManager
from freellmapi_adapter import FreeLLMAPIAdapter
from google_oauth import GoogleOAuthAdapter
from openai_key import OpenAIKeyAdapter
from resource_governor import ResourceGovernor
from schemas import (
    ConsentRecord,
    EntitlementBoundary,
    ProviderAuthProfile,
    ResourceReceipt,
    TenantResourcePool,
)


class CognitiveTreasuryBroker:
    """Middle authorization and routing broker for A'Space Cognitive Treasury."""

    def __init__(self, master_secret: str = "aspace-cognitive-treasury-master-key-2026"):
        self.vault = TenantVault(master_secret)
        self.entitlement_mgr = EntitlementManager()
        self.governor = ResourceGovernor(self.vault)

        # Register standard Arcade-like auth adapters
        self.adapters: Dict[str, ArcadeAdapterContract] = {
            "google": GoogleOAuthAdapter(),
            "openai": OpenAIKeyAdapter(),
            "anthropic": AnthropicKeyAdapter(),
            "freellmapi": FreeLLMAPIAdapter(self.vault),
        }

        # Durable state in memory (or sqlite)
        # tenant_id -> list of ProviderAuthProfile
        self._profiles: Dict[str, List[ProviderAuthProfile]] = {}
        # consent_id -> ConsentRecord
        self._consents: Dict[str, ConsentRecord] = {}
        # receipt_id -> ResourceReceipt
        self._receipts: Dict[str, ResourceReceipt] = {}
        # audit log
        self._audit_log: List[Dict[str, Any]] = []

    def _log_audit(self, tenant_id: str, event_type: str, details: Dict[str, Any]) -> None:
        self._audit_log.append({
            "audit_id": f"aud-{uuid.uuid4().hex[:12]}",
            "tenant_id": tenant_id,
            "event_type": event_type,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "details": details,
        })

    def get_audit_log(self, tenant_id: str) -> List[Dict[str, Any]]:
        return [entry for entry in self._audit_log if entry["tenant_id"] == tenant_id]

    def register_adapter(self, adapter: ArcadeAdapterContract) -> None:
        self.adapters[adapter.provider_id] = adapter

    def connect_profile(
        self,
        tenant_id: str,
        provider_id: str,
        auth_input: Dict[str, Any],
        granted_scopes: Optional[List[str]] = None,
    ) -> ProviderAuthProfile:
        """Connects a new provider account credential to tenant pool."""
        self.entitlement_mgr.validate_routing_access(tenant_id)

        adapter = self.adapters.get(provider_id)
        if not adapter:
            raise ValueError(f"Unsupported auth provider_id: '{provider_id}'")

        connected_count = len(self.get_tenant_profiles(tenant_id, active_only=True))
        self.entitlement_mgr.validate_connection_limit(tenant_id, connected_count)

        # Complete authorization flow
        auth_result = adapter.authorize_complete(tenant_id, auth_input)
        raw_creds = auth_result["credentials"]
        provider_account_id = auth_result["provider_account_id"]
        scopes = granted_scopes or auth_result.get("scopes") or []

        # Encrypt raw credentials with tenant-derived key
        encrypted_creds = self.vault.encrypt_credentials(tenant_id, raw_creds)

        profile = ProviderAuthProfile(
            tenant_id=tenant_id,
            provider_id=provider_id,
            provider_account_id=provider_account_id,
            auth_type=adapter.auth_type,
            encrypted_credentials=encrypted_creds,
            scopes=scopes,
            status="ACTIVE",
            metadata=auth_result.get("metadata") or {},
        )

        # Record explicit consent
        consent = ConsentRecord(
            tenant_id=tenant_id,
            provider_id=provider_id,
            granted_scopes=scopes,
            status="ACTIVE",
        )
        self._consents[consent.consent_id] = consent

        self._profiles.setdefault(tenant_id, []).append(profile)
        self._log_audit(
            tenant_id,
            "PROFILE_CONNECTED",
            {
                "profile_id": profile.profile_id,
                "provider_id": provider_id,
                "provider_account_id": provider_account_id,
                "scopes": scopes,
            },
        )
        return profile

    def get_tenant_profiles(self, tenant_id: str, active_only: bool = True) -> List[ProviderAuthProfile]:
        profiles = self._profiles.get(tenant_id, [])
        if active_only:
            return [p for p in profiles if p.status == "ACTIVE"]
        return list(profiles)

    def revoke_profile(self, tenant_id: str, profile_id: str) -> bool:
        """Revokes/disconnects a specific provider profile under a tenant without affecting client identity or other profiles."""
        tenant_profiles = self._profiles.get(tenant_id, [])
        target = next((p for p in tenant_profiles if p.profile_id == profile_id), None)

        if not target:
            raise ValueError(f"Profile '{profile_id}' not found under tenant '{tenant_id}'")

        adapter = self.adapters.get(target.provider_id)
        if adapter:
            try:
                decrypted = self.vault.decrypt_credentials(tenant_id, target.encrypted_credentials)
                adapter.revoke(target, decrypted)
            except Exception:
                pass

        target.status = "REVOKED"
        target.updated_at = datetime.datetime.now(datetime.timezone.utc).isoformat()

        # Update associated consent records
        for consent in self._consents.values():
            if consent.tenant_id == tenant_id and consent.provider_id == target.provider_id:
                consent.status = "REVOKED"
                consent.revoked_at = target.updated_at

        self._log_audit(
            tenant_id,
            "PROFILE_REVOKED",
            {
                "profile_id": profile_id,
                "provider_id": target.provider_id,
                "provider_account_id": target.provider_account_id,
            },
        )
        return True

    def get_tenant_resource_pool(self, tenant_id: str) -> TenantResourcePool:
        active_profiles = self.get_tenant_profiles(tenant_id, active_only=True)
        return TenantResourcePool(
            tenant_id=tenant_id,
            profile_ids=[p.profile_id for p in active_profiles],
        )

    def route_request(
        self,
        tenant_id: str,
        model: str,
        messages: List[Dict[str, Any]],
        correlation_id: Optional[str] = None,
        parameters: Optional[Dict[str, Any]] = None,
        privacy_requirement: str = "standard",
    ) -> Tuple[Dict[str, Any], ResourceReceipt]:
        """Routes execution request across tenant's active provider profiles and emits a mandatory ResourceReceipt."""
        # 1. Enforce subscription entitlement boundary
        self.entitlement_mgr.validate_routing_access(tenant_id)

        correlation_id = correlation_id or f"corr-{uuid.uuid4().hex[:12]}"
        active_profiles = self.get_tenant_profiles(tenant_id, active_only=True)

        # 2. Delegate to ResourceGovernor
        result = self.governor.route_and_execute(
            tenant_id=tenant_id,
            candidate_profiles=active_profiles,
            adapters=self.adapters,
            model=model,
            messages=messages,
            parameters=parameters,
            privacy_requirement=privacy_requirement,
        )

        selected_profile: Optional[ProviderAuthProfile] = result.get("selected_profile")
        provider_id = selected_profile.provider_id if selected_profile else "none"
        provider_account_id = selected_profile.provider_account_id if selected_profile else "none"

        # 3. Emit mandatory ResourceReceipt
        receipt = ResourceReceipt(
            tenant_id=tenant_id,
            provider_id=provider_id,
            provider_account_id=provider_account_id,
            model=model,
            budget_consumed=result.get("tokens_consumed", {"total_tokens": 0}),
            latency_ms=result.get("latency_ms", 0),
            result_or_evidence={
                "status": result.get("status"),
                "has_content": bool(result.get("content")),
                "failover_count": len(result.get("failover_attempts", [])),
                "error_detail": result.get("error_detail"),
            },
            remaining_or_unknown_quota=result.get("remaining_quota", {}),
            correlation_id=correlation_id,
        )

        self._receipts[receipt.receipt_id] = receipt
        self._log_audit(
            tenant_id,
            "REQUEST_ROUTED",
            {
                "receipt_id": receipt.receipt_id,
                "correlation_id": correlation_id,
                "provider_id": provider_id,
                "model": model,
                "status": result.get("status"),
            },
        )

        return result, receipt

    def get_receipt(self, receipt_id: str) -> Optional[ResourceReceipt]:
        return self._receipts.get(receipt_id)

    def list_tenant_receipts(self, tenant_id: str) -> List[ResourceReceipt]:
        return [r for r in self._receipts.values() if r.tenant_id == tenant_id]
