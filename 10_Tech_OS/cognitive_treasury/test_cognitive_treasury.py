#!/usr/bin/env python3
"""Comprehensive Test Suite for Cognitive Treasury Federated Auth & Token Broker.

Tests deliverables and acceptance criteria of Issue #417:
- Multi-tenant credential isolation & encrypted vault
- 3 heterogeneous providers under one tenant
- Resource Governor routing & provider failover
- Disconnecting/revoking a provider without affecting client identity or sibling providers
- Mandatory ResourceReceipt emission
- $300/year Business Plan entitlement boundary
"""

from __future__ import annotations

import sys
from pathlib import Path

# Add current directory to sys.path for direct imports
sys.path.insert(0, str(Path(__file__).parent))

import pytest

from encrypted_vault import TenantIsolationError, TenantVault
from entitlement_boundary import EntitlementViolationError
from schemas import (
    EntitlementBoundary,
    ProviderAuthProfile,
    ResourceReceipt,
    TenantResourcePool,
)
from treasury_broker import CognitiveTreasuryBroker


def test_tenant_vault_encrypted_isolation():
    """Verifies that secrets are encrypted and cross-tenant access raises TenantIsolationError."""
    vault = TenantVault("test-master-secret")

    tenant_a = "tenant_alpha"
    tenant_b = "tenant_beta"

    creds_a = {"api_key": "sk-proj-alpha-secret-key-12345"}
    encrypted_blob = vault.encrypt_credentials(tenant_a, creds_a)

    # Decrypt with correct tenant_id
    decrypted_a = vault.decrypt_credentials(tenant_a, encrypted_blob)
    assert decrypted_a["api_key"] == "sk-proj-alpha-secret-key-12345"

    # Cross-tenant decryption attempt MUST raise TenantIsolationError
    with pytest.raises(TenantIsolationError) as exc_info:
        vault.decrypt_credentials(tenant_b, encrypted_blob)
    assert "Cross-tenant credential access prohibited" in str(exc_info.value)


def test_heterogeneous_providers_canary():
    """Canary test with 3 heterogeneous providers under ONE tenant (Google OAuth, OpenAI Key, Anthropic Key)."""
    broker = CognitiveTreasuryBroker()
    tenant_id = "tenant_corp_1"

    # 1. Connect Google OAuth profile
    google_init = broker.adapters["google"].authorize_init(tenant_id)
    assert "code_verifier" in google_init
    google_profile = broker.connect_profile(
        tenant_id=tenant_id,
        provider_id="google",
        auth_input={
            "code": "google_auth_code_123",
            "code_verifier": google_init["code_verifier"],
            "provider_account_id": "corp1_admin@gmail.com",
            "scopes": ["https://www.googleapis.com/auth/generative-language"],
        },
    )
    assert google_profile.provider_id == "google"
    assert google_profile.status == "ACTIVE"

    # 2. Connect OpenAI API Key profile
    openai_profile = broker.connect_profile(
        tenant_id=tenant_id,
        provider_id="openai",
        auth_input={"api_key": "sk-proj-openai-key-corp1", "org_id": "org_corp1"},
    )
    assert openai_profile.provider_id == "openai"
    assert openai_profile.status == "ACTIVE"

    # 3. Connect Anthropic API Key profile
    anthropic_profile = broker.connect_profile(
        tenant_id=tenant_id,
        provider_id="anthropic",
        auth_input={"api_key": "sk-ant-api03-anthropic-key-corp1"},
    )
    assert anthropic_profile.provider_id == "anthropic"
    assert anthropic_profile.status == "ACTIVE"

    # Verify tenant resource pool contains all 3 profiles
    pool = broker.get_tenant_resource_pool(tenant_id)
    assert len(pool.profile_ids) == 3
    assert google_profile.profile_id in pool.profile_ids
    assert openai_profile.profile_id in pool.profile_ids
    assert anthropic_profile.profile_id in pool.profile_ids


def test_provider_routing_and_failover():
    """Tests Resource Governor routing preference and failover when primary provider fails."""
    broker = CognitiveTreasuryBroker()
    tenant_id = "tenant_failover_test"

    # Connect Google (primary free choice) and OpenAI
    g_init = broker.adapters["google"].authorize_init(tenant_id)
    google_profile = broker.connect_profile(
        tenant_id=tenant_id,
        provider_id="google",
        auth_input={
            "code": "g_code",
            "code_verifier": g_init["code_verifier"],
            "provider_account_id": "user_failover@gmail.com",
        },
    )

    openai_profile = broker.connect_profile(
        tenant_id=tenant_id,
        provider_id="openai",
        auth_input={"api_key": "sk-proj-openai-key-failover"},
    )

    # First routed call should succeed
    messages = [{"role": "user", "content": "Analyze quarterly budget"}]
    res, receipt = broker.route_request(
        tenant_id=tenant_id,
        model="gemini-pro",
        messages=messages,
        correlation_id="corr-test-001",
    )
    assert res["status"] == "SUCCESS"
    assert receipt.tenant_id == tenant_id
    assert receipt.provider_id in {"google", "openai"}
    assert receipt.correlation_id == "corr-test-001"
    assert receipt.budget_consumed["total_tokens"] > 0

    # Simulate primary provider failure by invalidating Google profile status
    google_profile.status = "EXPIRED"

    # Next call should failover automatically to OpenAI
    res2, receipt2 = broker.route_request(
        tenant_id=tenant_id,
        model="gpt-4o",
        messages=messages,
        correlation_id="corr-test-002",
    )
    assert res2["status"] == "SUCCESS"
    assert receipt2.provider_id == "openai"
    assert receipt2.provider_account_id == openai_profile.provider_account_id


def test_token_revocation_pass_criterion():
    """PASS Criterion Test:

    A provider profile can be disconnected/revoked without changing the client identity
    or breaking other connected providers under that tenant.
    """
    broker = CognitiveTreasuryBroker()
    tenant_id = "tenant_revocation_test"

    # Connect Google, OpenAI, Anthropic
    g_init = broker.adapters["google"].authorize_init(tenant_id)
    p_google = broker.connect_profile(
        tenant_id=tenant_id,
        provider_id="google",
        auth_input={"code": "c", "code_verifier": g_init["code_verifier"], "provider_account_id": "rev_g@gmail.com"},
    )
    p_openai = broker.connect_profile(
        tenant_id=tenant_id,
        provider_id="openai",
        auth_input={"api_key": "sk-proj-revocation-openai"},
    )
    p_anthropic = broker.connect_profile(
        tenant_id=tenant_id,
        provider_id="anthropic",
        auth_input={"api_key": "sk-ant-api03-revocation-anthropic"},
    )

    # Revoke OpenAI profile
    assert broker.revoke_profile(tenant_id, p_openai.profile_id) is True
    assert p_openai.status == "REVOKED"

    # Client identity (tenant_id) remains valid
    active_profiles = broker.get_tenant_profiles(tenant_id, active_only=True)
    assert len(active_profiles) == 2
    active_provider_ids = {p.provider_id for p in active_profiles}
    assert active_provider_ids == {"google", "anthropic"}
    assert "openai" not in active_provider_ids

    # Routing requests continues to work seamlessly with remaining connected providers
    messages = [{"role": "user", "content": "Execute remaining capacity request"}]
    res, receipt = broker.route_request(
        tenant_id=tenant_id,
        model="claude-3-5-sonnet",
        messages=messages,
    )
    assert res["status"] == "SUCCESS"
    assert receipt.provider_id in {"google", "anthropic"}


def test_freellmapi_adapter_uses_authorized_profile():
    """Verifies that FreeLLMAPI adapter uses tenant-authorized provider profiles rather than anonymous global fuel."""
    broker = CognitiveTreasuryBroker()
    tenant_id = "tenant_freellmapi_test"

    # Connect Google profile first
    g_init = broker.adapters["google"].authorize_init(tenant_id)
    p_google = broker.connect_profile(
        tenant_id=tenant_id,
        provider_id="google",
        auth_input={"code": "c", "code_verifier": g_init["code_verifier"], "provider_account_id": "freellm_owner@gmail.com"},
    )

    # Bind FreeLLMAPI adapter using tenant-authorized profile
    p_freellm = broker.connect_profile(
        tenant_id=tenant_id,
        provider_id="freellmapi",
        auth_input={"underlying_profile_id": p_google.profile_id},
    )

    assert p_freellm.provider_id == "freellmapi"
    assert p_freellm.status == "ACTIVE"

    res, receipt = broker.route_request(
        tenant_id=tenant_id,
        model="freellmapi-fast",
        messages=[{"role": "user", "content": "routed prompt"}],
    )
    assert res["status"] == "SUCCESS"
    assert receipt.provider_id in {"google", "freellmapi"}


def test_business_plan_entitlement_boundary():
    """Verifies $300/year plan billing/entitlement boundary logic."""
    broker = CognitiveTreasuryBroker()
    tenant_id = "tenant_entitlement_test"

    summary = broker.entitlement_mgr.entitlement_summary(tenant_id, connected_profiles_count=0)
    assert summary["plan_id"] == "business_300_year"
    assert summary["quota_ownership_model"] == "TENANT_PROPRIETARY"

    # Disable subscription
    broker.entitlement_mgr.set_subscription_status(tenant_id, active=False)

    # Routing attempt should be denied due to inactive subscription
    with pytest.raises(EntitlementViolationError) as exc_info:
        broker.route_request(tenant_id, "model", [{"role": "user", "content": "hi"}])
    assert "subscription for tenant 'tenant_entitlement_test' is inactive" in str(exc_info.value)
