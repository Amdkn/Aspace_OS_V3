"""
Unit and Canary Tests for Business OS Client-Owned AI Provider Connections & Cognitive Treasury (#419)
"""

import unittest
import pytest
from provider_connections import (
    EntitlementManager,
    CognitiveTreasuryBroker,
    SubscriptionPlan,
    ProviderConnectionState,
    EntitlementError,
    ProviderConnectionError
)


class TestProviderConnectionsAndEntitlement(unittest.TestCase):

    def setUp(self):
        self.entitlement_mgr = EntitlementManager()
        self.broker = CognitiveTreasuryBroker(entitlement_manager=self.entitlement_mgr)
        self.tenant_id = "tenant_acme_corp"

    def test_entitlement_enforcement(self):
        """Verify that tenants without the $300/year plan are blocked from connecting providers."""
        # By default tenant is under PLAN_FREE
        self.assertEqual(
            self.entitlement_mgr.get_tenant_plan(self.tenant_id),
            SubscriptionPlan.PLAN_FREE
        )

        # Attempting provider authorization should fail with EntitlementError
        with self.assertRaises(EntitlementError) as ctx:
            self.broker.authorize_provider(
                tenant_id=self.tenant_id,
                provider_id="openai",
                raw_secret="sk-proj-secret-key-12345"
            )
        self.assertIn("BUSINESS_300_ANNUAL", str(ctx.exception))

        # Upgrade tenant to $300/year plan
        self.entitlement_mgr.set_tenant_plan(self.tenant_id, SubscriptionPlan.PLAN_300_ANNUAL)

        # Authorization now succeeds
        conn = self.broker.authorize_provider(
            tenant_id=self.tenant_id,
            provider_id="openai",
            raw_secret="sk-proj-secret-key-12345"
        )
        self.assertEqual(conn.tenant_id, self.tenant_id)
        self.assertEqual(conn.provider_id, "openai")
        self.assertEqual(conn.status, ProviderConnectionState.ACTIVE)

    def test_no_raw_secret_duplication(self):
        """Verify that raw provider secrets are never stored in Business OS state/view models."""
        self.entitlement_mgr.set_tenant_plan(self.tenant_id, SubscriptionPlan.PLAN_300_ANNUAL)
        raw_secret = "sk-proj-super-secret-key-9999"

        conn = self.broker.authorize_provider(
            tenant_id=self.tenant_id,
            provider_id="anthropic",
            raw_secret=raw_secret
        )

        view_model = conn.to_view_model()

        # Check raw secret is not stored
        self.assertNotIn("raw_secret", view_model)
        self.assertNotIn(raw_secret, str(view_model))
        self.assertEqual(view_model["redacted_fingerprint"], "sk-...9999")
        self.assertTrue(view_model["secret_handle"].startswith("sec_broker_"))

    def test_canary_multi_provider_shared_capability_and_isolated_revocation(self):
        """
        Canary Requirement (#419):
        1 tenant connects multiple providers,
        runs 1 shared capability,
        receives a usage/evidence receipt with measured quotas,
        then revokes 1 provider without changing tenant identity or breaking the others.
        """
        self.entitlement_mgr.set_tenant_plan(self.tenant_id, SubscriptionPlan.PLAN_300_ANNUAL)

        # 1. Connect multiple providers (OpenAI, Anthropic, Google Gemini)
        conn_openai = self.broker.authorize_provider(
            tenant_id=self.tenant_id,
            provider_id="openai",
            raw_secret="sk-openai-key-000001"
        )
        conn_anthropic = self.broker.authorize_provider(
            tenant_id=self.tenant_id,
            provider_id="anthropic",
            raw_secret="sk-ant-key-000002"
        )
        conn_gemini = self.broker.authorize_provider(
            tenant_id=self.tenant_id,
            provider_id="google_gemini",
            raw_secret="ai-gemini-key-000003"
        )

        # Verify initial connections view model
        status_list = self.broker.get_connection_status(self.tenant_id)
        self.assertEqual(len(status_list), 3)

        # 2. Run one shared capability
        receipt = self.broker.execute_shared_capability(
            tenant_id=self.tenant_id,
            capability_id="llm.generate.summary",
            payload={"prompt": "Summarize fiscal Q3 results", "estimated_tokens": 2500},
            preferred_provider="anthropic"
        )

        # Verify usage/evidence receipt
        self.assertEqual(receipt.status, "SUCCEEDED")
        self.assertEqual(receipt.capability_id, "llm.generate.summary")
        self.assertEqual(receipt.observed_effect["provider_id"], "anthropic")
        self.assertEqual(
            receipt.observed_effect["measured_quota_impact"]["tokens_consumed"], 2500
        )
        self.assertEqual(
            receipt.observed_effect["measured_quota_impact"]["measured_remaining_quota"],
            997500
        )

        # Verify receipt is in treasury audit ledger
        tenant_receipts = self.broker.get_receipts(self.tenant_id)
        self.assertEqual(len(tenant_receipts), 1)
        self.assertEqual(tenant_receipts[0]["operation_id"], receipt.operation_id)

        # 3. Revoke one provider (e.g., Anthropic)
        revoke_res = self.broker.revoke_provider(
            tenant_id=self.tenant_id,
            provider_id="anthropic"
        )

        self.assertEqual(revoke_res["status"], ProviderConnectionState.REVOKED)
        self.assertNotIn("anthropic", revoke_res["remaining_active_providers"])
        self.assertIn("openai", revoke_res["remaining_active_providers"])
        self.assertIn("google_gemini", revoke_res["remaining_active_providers"])

        # 4. Assert tenant identity is unchanged and remaining active providers function
        status_after_revoke = self.broker.get_connection_status(self.tenant_id)
        self.assertEqual(len(status_after_revoke), 3) # total connections still 3 (1 revoked, 2 active)
        revoked_conn = [c for c in status_after_revoke if c["provider_id"] == "anthropic"][0]
        self.assertEqual(revoked_conn["status"], ProviderConnectionState.REVOKED)

        # Execute capability again; should automatically route to another active provider (e.g. openai or gemini)
        receipt2 = self.broker.execute_shared_capability(
            tenant_id=self.tenant_id,
            capability_id="llm.generate.summary",
            payload={"prompt": "Analyze market trends", "estimated_tokens": 1000},
            preferred_provider="openai"
        )

        self.assertEqual(receipt2.status, "SUCCEEDED")
        self.assertEqual(receipt2.observed_effect["provider_id"], "openai")
        self.assertEqual(receipt2.observed_effect["tenant_id"], self.tenant_id) # Tenant identity unchanged


if __name__ == "__main__":
    unittest.main()
