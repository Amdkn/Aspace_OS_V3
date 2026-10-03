import unittest
from cubefarm_adapter import (
    FactoryExecution,
    InnovationCandidate,
    MigrationMatrix,
    UUPMThemeAdapter,
    CubeFarmStateProjectionAdapter,
    VALID_CLASSIFICATIONS,
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

    def test_innovation_candidate_validation(self):
        candidate = InnovationCandidate(
            candidate_id="test_cand",
            title="Test Candidate",
            source_issue="#421",
            classification="UI/RUNTIME REUSABLE",
            target_surface="test_surface",
            rationale="Testing",
            portability_notes="Porting notes"
        )
        self.assertEqual(candidate.candidate_id, "test_cand")

        with self.assertRaises(ValueError):
            InnovationCandidate(
                candidate_id="bad_cand",
                title="Bad Candidate",
                source_issue="#421",
                classification="INVALID_CLASSIFICATION",
                target_surface="test_surface",
                rationale="Testing",
                portability_notes="Porting notes"
            )

    def test_migration_matrix(self):
        matrix = MigrationMatrix()
        d = matrix.to_dict()
        self.assertIn("candidates", d)
        self.assertGreaterEqual(len(d["candidates"]), 5)

        reusables = matrix.filter_by_classification("UI/RUNTIME REUSABLE")
        self.assertTrue(any(c.candidate_id == "uupm_multi_theme" for c in reusables))

        quarantined = matrix.filter_by_classification("QUARANTINE")
        self.assertTrue(any(c.candidate_id == "auth_session_ux" for c in quarantined))

    def test_uupm_theme_adapter(self):
        adapter = UUPMThemeAdapter(active_theme="dark_mode_oled")
        tokens = adapter.get_theme_tokens()
        self.assertEqual(tokens["name"], "Dark Mode OLED")

        style = adapter.render_wall_container_style()
        self.assertEqual(style["backgroundColor"], "#000000")

        adapter.set_theme("glassmorphism")
        glass_style = adapter.render_wall_container_style()
        self.assertIn("backdropFilter", glass_style)

        with self.assertRaises(ValueError):
            adapter.set_theme("non_existent_theme")

    def test_cubefarm_state_projection_adapter(self):
        proj_adapter = CubeFarmStateProjectionAdapter(actor_id="Ryan", return_to="#388/#403")
        proj = proj_adapter.project_state(
            wall_id="agent_life_business_wall",
            agent_state={"status": "ACTIVE", "harnesses": ["antigravity"]},
            life_state={"ikigai": "aligned", "cycle": "12WY_Q4"},
            business_state={"domain": "B1", "mrr": 300},
            fabric_surface="agent_os"
        )

        self.assertEqual(proj["wall_id"], "agent_life_business_wall")
        self.assertEqual(proj["actor_id"], "Ryan")
        self.assertEqual(proj["receipt"]["return_to"], "#388/#403")
        self.assertEqual(proj["receipt"]["consumer_role"], "SHARED_CAPABILITY_CONSUMER")

if __name__ == '__main__':
    unittest.main()
