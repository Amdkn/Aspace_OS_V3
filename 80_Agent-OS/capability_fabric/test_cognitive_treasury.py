import unittest
from .cognitive_treasury import CognitiveTreasury, ResourceProfile, CognitiveTreasuryError
from .browser_bridge import ChatGPTWebAdapter, QwenWebAdapter

class TestCognitiveTreasuryAcceptance(unittest.TestCase):
    def setUp(self):
        self.treasury = CognitiveTreasury()

    def test_acceptance_criterion_1_typed_resource_profile_3_heterogeneous_runtimes(self):
        # 1. One typed ResourceProfile covers at least 3 heterogeneous runtimes/providers.
        p1 = ResourceProfile("p1", "FreeLLMAPI", "freellmapi-default", "gpt-4o", 100000)
        p2 = ResourceProfile("p2", "Anthropic", "claude-code-v1", "claude-3-7-sonnet", 50000)
        p3 = ResourceProfile("p3", "DeepSeek", "deepseek-r1-v1", "deepseek-r1", 80000)

        self.treasury.register_profile(p1)
        self.treasury.register_profile(p2)
        self.treasury.register_profile(p3)

        profiles = self.treasury.list_profiles()
        self.assertEqual(len(profiles), 3)
        self.assertEqual({p.provider_name for p in profiles}, {"FreeLLMAPI", "Anthropic", "DeepSeek"})

    def test_acceptance_criterion_2_surface_driver_2_browser_auth_surfaces(self):
        # 2. One SurfaceDriver contract can represent at least two browser-auth AI surfaces without duplicating core logic.
        chatgpt_driver = ChatGPTWebAdapter()
        qwen_driver = QwenWebAdapter()

        # Both inherit from SurfaceDriver
        s1 = chatgpt_driver.authenticate_session("sess-1", "user-chatgpt", {"token": "abc"})
        s2 = qwen_driver.authenticate_session("sess-2", "user-qwen", {"token": "xyz"})

        self.assertTrue(s1.is_authenticated)
        self.assertTrue(s2.is_authenticated)

        res1 = chatgpt_driver.execute_tool_call("sess-1", "edit_file", {"path": "a.txt"})
        res2 = qwen_driver.execute_tool_call("sess-2", "edit_file", {"path": "b.txt"})

        self.assertEqual(res1["status"], "SUCCESS")
        self.assertEqual(res2["status"], "SUCCESS")
        self.assertEqual(res1["surface"], "chatgpt_web")
        self.assertEqual(res2["surface"], "qwen_web")

    def test_acceptance_criterion_4_token_abundance_metered_no_idle_loop_burn(self):
        # 4. Token abundance is metered as budget/fuel; no heartbeat/idle loop burns it without active mission + lease.
        p = ResourceProfile("p1", "FreeLLMAPI", "freellmapi-default", "gpt-4o", 1000)
        self.treasury.register_profile(p)

        # Rejection on idle loop or missing lease
        with self.assertRaises(CognitiveTreasuryError):
            self.treasury.consume_tokens("p1", 100, has_active_mission=False, has_valid_lease=True)

        with self.assertRaises(CognitiveTreasuryError):
            self.treasury.consume_tokens("p1", 100, has_active_mission=True, has_valid_lease=False)

        with self.assertRaises(CognitiveTreasuryError):
            self.treasury.consume_tokens("p1", 100, has_active_mission=True, has_valid_lease=True, is_idle_loop=True)

        # Successful consumption with active mission + valid lease
        remaining = self.treasury.consume_tokens("p1", 200, has_active_mission=True, has_valid_lease=True)
        self.assertEqual(remaining, 800)

    def test_acceptance_criterion_5_runtime_choice_and_remaining_budget_separate_from_identity(self):
        # 5. Agent OS/CubeFarm can display runtime choice and remaining resource budget separately from identity.
        p = ResourceProfile("p1", "OpenAI", "codex-v1", "gpt-4o", 5000, consumed_tokens=1000)
        self.treasury.register_profile(p)

        proj = self.treasury.get_projection(actor_id="Ryan", profile_id="p1")
        self.assertEqual(proj["identity"]["actor_id"], "Ryan")
        self.assertEqual(proj["runtime_choice"]["provider"], "OpenAI")
        self.assertEqual(proj["resource_budget"]["remaining_budget"], 4000)

    def test_acceptance_criterion_6_action_returns_evidence_receipt(self):
        # 6. Every completed routed action returns an EvidenceReceipt.
        p = ResourceProfile("p1", "FreeLLMAPI", "freellmapi-default", "gpt-4o", 10000)
        self.treasury.register_profile(p)

        receipt = self.treasury.record_action_effect(
            work_id=404,
            correlation_id="corr-404",
            actor_id="Ryan",
            profile_id="p1",
            action="route_model_execution",
            tokens_consumed=500,
            observed_effect="Model routed successfully",
            evidence_refs=["ref-1"],
        )

        self.assertEqual(receipt.work_id, 404)
        self.assertEqual(receipt.actor_id, "Ryan")
        self.assertEqual(receipt.status, "SUCCESS")
        self.assertEqual(receipt.tokens_consumed, 500)
        self.assertEqual(receipt.observed_effect, "Model routed successfully")
        self.assertIn("ref-1", receipt.evidence_refs)

if __name__ == "__main__":
    unittest.main()
