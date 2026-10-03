import unittest
from cubefarm_adapter import FactoryExecution, ForkReceipt

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

    def test_fork_receipt_validation_and_serialization(self):
        receipt = ForkReceipt(
            work_id=402,
            upstream_url="https://github.com/leonvanzyl/cubefarm.git",
            origin_url="https://github.com/Amdkn/cubefarm.git",
            baseline_sha="31e7ce01a1dcc1da2b576d1da36718c16b05b8ca",
            local_clone_path="C:/Users/amado/cubefarm",
            integration_branch="aspace/integration-baseline",
            local_state_classification={
                "package-lock.json": "REBUILD",
                "start-demo.bat": "KEEP",
                "start-dev.bat": "KEEP",
                "start.bat": "KEEP"
            },
            upstream_sync_proof={
                "fetch_cmd": "git fetch upstream",
                "rebase_cmd": "git rebase upstream/main",
                "sync_feasible": True
            },
            return_to=["#388", "#400"]
        )

        json_str = receipt.to_json()
        restored = ForkReceipt.from_json(json_str)

        self.assertEqual(restored.work_id, 402)
        self.assertEqual(restored.upstream_url, "https://github.com/leonvanzyl/cubefarm.git")
        self.assertEqual(restored.origin_url, "https://github.com/Amdkn/cubefarm.git")
        self.assertEqual(restored.local_state_classification["package-lock.json"], "REBUILD")
        self.assertEqual(restored.local_state_classification["start.bat"], "KEEP")

    def test_fork_receipt_rejects_main_integration_branch(self):
        receipt = ForkReceipt(
            work_id=402,
            upstream_url="https://github.com/leonvanzyl/cubefarm.git",
            origin_url="https://github.com/Amdkn/cubefarm.git",
            baseline_sha="31e7ce01a1dcc1da2b576d1da36718c16b05b8ca",
            local_clone_path="C:/Users/amado/cubefarm",
            integration_branch="main",
            local_state_classification={"package-lock.json": "REBUILD"},
            upstream_sync_proof={"sync_feasible": True},
            return_to=["#388"]
        )
        with self.assertRaises(ValueError):
            receipt.validate()

    def test_fork_receipt_rejects_invalid_classification(self):
        receipt = ForkReceipt(
            work_id=402,
            upstream_url="https://github.com/leonvanzyl/cubefarm.git",
            origin_url="https://github.com/Amdkn/cubefarm.git",
            baseline_sha="31e7ce01a1dcc1da2b576d1da36718c16b05b8ca",
            local_clone_path="C:/Users/amado/cubefarm",
            integration_branch="aspace/integration-baseline",
            local_state_classification={"package-lock.json": "INVALID_ACTION"},
            upstream_sync_proof={"sync_feasible": True},
            return_to=["#388"]
        )
        with self.assertRaises(ValueError):
            receipt.validate()

if __name__ == '__main__':
    unittest.main()
