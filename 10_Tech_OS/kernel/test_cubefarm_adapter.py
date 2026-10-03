import unittest
from cubefarm_adapter import (
    FactoryExecution,
    CubeFarmThemeConfig,
    CUBEFARM_FORK_TOPOLOGY,
    UUPM_THEME_CATALOGUE,
)

class TestCubeFarmAdapter(unittest.TestCase):
    def test_factory_execution_serialization(self):
        exec = FactoryExecution(
            actor_id="Ryan",
            doctor="Doctor13",
            work_id=388,
            mission_id="mission_123",
            issue_ref="Amdkn/Aspace_OS_V3#388",
            operation_id="op_1",
            correlation_id="corr_1",
            authority_envelope={"sandbox": True},
            affected_resources=["10_Tech_OS/kernel/cubefarm_adapter.py"],
            allowed_repos=["Amdkn/Aspace_OS_V3"],
            allowed_effects=["PR_CREATE"],
            forbidden_effects=["MAIN_MUTATION"],
            budget_lease=1000,
            session_limit=1,
            runtime_choice="CubeFarm",
            qa_policy="independent_worktree",
            evidence_head="sha_123",
            return_to="Doctor13",
            fencing_token="fence_1"
        )

        json_data = exec.to_json()
        loaded = FactoryExecution.from_json(json_data)

        self.assertEqual(loaded.actor_id, "Ryan")
        self.assertEqual(loaded.work_id, 388)
        self.assertEqual(loaded.authority_envelope["sandbox"], True)
        self.assertEqual(loaded.allowed_repos, ["Amdkn/Aspace_OS_V3"])

    def test_fork_topology_constraints(self):
        self.assertEqual(CUBEFARM_FORK_TOPOLOGY["upstream_repo"], "leonvanzyl/cubefarm")
        self.assertEqual(CUBEFARM_FORK_TOPOLOGY["fork_repo"], "Amdkn/cubefarm")
        self.assertTrue(CUBEFARM_FORK_TOPOLOGY["upstream_syncable"])
        self.assertFalse(CUBEFARM_FORK_TOPOLOGY["direct_upstream_main_customization"])
        self.assertTrue(CUBEFARM_FORK_TOPOLOGY["theme_capability_bounded"])

    def test_multi_theme_switching_and_bounds(self):
        # 1. Test Theme 'dark-oled'
        theme_dark = CubeFarmThemeConfig(active_theme_id="dark-oled")
        self.assertTrue(theme_dark.validate_bounds())
        tokens_dark = theme_dark.get_effective_tokens()
        self.assertEqual(tokens_dark["bg_surface"], "#000000")
        self.assertEqual(tokens_dark["accent_color"], "#38bdf8")

        # 2. Test Theme 'warm-paper'
        theme_warm = CubeFarmThemeConfig(active_theme_id="warm-paper")
        self.assertTrue(theme_warm.validate_bounds())
        tokens_warm = theme_warm.get_effective_tokens()
        self.assertEqual(tokens_warm["bg_surface"], "#fbf9f5")
        self.assertEqual(tokens_warm["accent_color"], "#ea580c")

        # Prove two distinct theme profiles without business logic duplication
        self.assertNotEqual(tokens_dark["bg_surface"], tokens_warm["bg_surface"])
        self.assertNotEqual(tokens_dark["accent_color"], tokens_warm["accent_color"])

    def test_factory_execution_with_multi_theme(self):
        exec = FactoryExecution(
            actor_id="Ryan",
            doctor="Doctor13",
            work_id=400,
            mission_id="mission_400",
            issue_ref="Amdkn/Aspace_OS_V3#400",
            operation_id="op_400",
            correlation_id="corr_400",
            authority_envelope={"sandbox": True},
            affected_resources=["10_Tech_OS/kernel/cubefarm_adapter.py"],
            allowed_repos=["Amdkn/cubefarm"],
            allowed_effects=["PR_CREATE"],
            forbidden_effects=["UPSTREAM_MAIN_DIRECT_COMMIT"],
            budget_lease=1000,
            session_limit=1,
            runtime_choice="CubeFarm",
            qa_policy="independent_worktree",
            evidence_head="sha_400",
            return_to="#388",
            fencing_token="fence_400",
            theme_config=CubeFarmThemeConfig(active_theme_id="cyberpunk")
        )

        json_data = exec.to_json()
        loaded = FactoryExecution.from_json(json_data)

        self.assertIsNotNone(loaded.theme_config)
        self.assertEqual(loaded.theme_config.active_theme_id, "cyberpunk")
        tokens = loaded.theme_config.get_effective_tokens()
        self.assertEqual(tokens["text_color"], "#00ffcc")
        self.assertTrue(loaded.theme_config.validate_bounds())

if __name__ == '__main__':
    unittest.main()
