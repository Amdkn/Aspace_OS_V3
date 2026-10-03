import unittest
from cubefarm_adapter import FactoryExecution

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

if __name__ == '__main__':
    unittest.main()
