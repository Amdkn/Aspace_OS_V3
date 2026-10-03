import unittest
import os
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
AGENT_OS_ROOT = HERE.parent
if str(AGENT_OS_ROOT) not in sys.path:
    sys.path.insert(0, str(AGENT_OS_ROOT))

try:
    from .registry import CapabilityRegistry
    from .adapters import HarnessMeshAdapter, BrowserBridgeAdapter, CLIAdapter, APIAdapter, MCPAdapter
    from .harness_list import register_harness_list
    from .capability_inspect import register_capability_inspect
    from .harness_certification import HarnessCertificationEngine, CertificationError, failover_harness, get_harness_mesh_view
except ImportError:
    from capability_fabric.registry import CapabilityRegistry
    from capability_fabric.adapters import HarnessMeshAdapter, BrowserBridgeAdapter, CLIAdapter, APIAdapter, MCPAdapter
    from capability_fabric.harness_list import register_harness_list
    from capability_fabric.capability_inspect import register_capability_inspect
    from capability_fabric.harness_certification import HarnessCertificationEngine, CertificationError, failover_harness, get_harness_mesh_view

class TestHarnessCertification(unittest.TestCase):
    def setUp(self):
        self.registry = CapabilityRegistry()
        register_harness_list(self.registry)
        register_capability_inspect(self.registry)
        self.engine = HarnessCertificationEngine()

    def test_matrix_loaded_and_valid(self):
        harnesses = self.engine.harnesses
        self.assertIn("hermes", harnesses)
        self.assertIn("codex", harnesses)
        self.assertIn("browser_bridge_chatgpt_web", harnesses)
        self.assertIn("claude_code", harnesses)
        self.assertIn("antigravity", harnesses)
        self.assertIn("jules", harnesses)
        self.assertIn("qwen", harnesses)

        # Ensure required PASS harnesses in First Wave
        for h_id in ["hermes", "codex", "browser_bridge_chatgpt_web", "claude_code", "antigravity", "jules"]:
            self.assertEqual(harnesses[h_id]["status"], "PASS")

        # Ensure bounded gaps
        for h_id in ["qwen", "gemini", "deepseek", "kimi", "minimax"]:
            self.assertEqual(harnesses[h_id]["status"], "RECON_BOUNDED_GAP")

    def test_certified_first_wave_harnesses(self):
        certified_harnesses = ["hermes", "codex", "browser_bridge_chatgpt_web", "claude_code", "antigravity", "jules"]
        for h_id in certified_harnesses:
            adapter = HarnessMeshAdapter(self.registry, h_id)
            res = adapter.invoke_certified(
                capability_id="harness_list",
                payload={},
                actor_id="Doctor13",
                authority_envelope="L2_EXECUTE",
                correlation_id=f"corr-{h_id}-1"
            )
            self.assertEqual(res["status"], "SUCCESS")
            self.assertEqual(res["certification"]["status"], "PASS")
            self.assertEqual(res["mesh_view"]["identity"]["actor_id"], "Doctor13")
            self.assertTrue(res["mesh_view"]["identity"]["independent_of_provider"])
            self.assertIn("budget", res["mesh_view"])
            self.assertIn("evidence", res["mesh_view"])

    def test_second_shared_capability_capability_inspect(self):
        adapter = HarnessMeshAdapter(self.registry, "hermes")
        res = adapter.invoke_certified(
            capability_id="capability_inspect",
            payload={"surface": "harness"},
            actor_id="companion_ryan_build",
            authority_envelope="L2_READ",
            correlation_id="corr-inspect-1"
        )
        self.assertEqual(res["status"], "SUCCESS")
        self.assertEqual(res["receipt"]["capability_id"], "capability_inspect")
        self.assertTrue(len(res["data"]["capabilities"]) >= 2)

    def test_rule_1_actor_id_external_requirement(self):
        adapter = HarnessMeshAdapter(self.registry, "hermes")
        res = adapter.invoke_certified(
            capability_id="harness_list",
            payload={},
            actor_id="hermes",
            correlation_id="corr-rule1-fail"
        )
        self.assertEqual(res["status"], "CERTIFICATION_FAILED")
        self.assertIn("Rule 1 Failure", res["error"])

    def test_bounded_gap_rejection_no_silent_fallback(self):
        adapter = HarnessMeshAdapter(self.registry, "qwen")
        res = adapter.invoke_certified(
            capability_id="harness_list",
            payload={},
            actor_id="Doctor13",
            correlation_id="corr-qwen-fail"
        )
        self.assertEqual(res["status"], "CERTIFICATION_FAILED")
        self.assertIn("uncertified with a bounded gap", res["error"])

    def test_failover_preserves_invariants(self):
        failover_res = failover_harness(
            from_harness="hermes",
            to_harness="codex",
            actor_id="Doctor13",
            work_id=412,
            correlation_id="corr-failover-412",
            authority_envelope="L2_EXECUTE",
            capability_id="harness_list",
            fail_reason="HERMES_TIMEOUT"
        )
        self.assertEqual(failover_res["status"], "SUCCESS")
        self.assertEqual(failover_res["actor_id"], "Doctor13")
        self.assertEqual(failover_res["work_id"], 412)
        self.assertEqual(failover_res["correlation_id"], "corr-failover-412")
        self.assertEqual(failover_res["authority_envelope"], "L2_EXECUTE")
        self.assertTrue(failover_res["preserved_invariants"]["actor_id_unchanged"])
        self.assertTrue(failover_res["preserved_invariants"]["work_id_unchanged"])

    def test_agent_os_mesh_view_display_separation(self):
        view = get_harness_mesh_view(
            actor_id="companion_ryan_build",
            runtime_id="rt-sovereign-node-1",
            adapter_type="HarnessMeshAdapter",
            harness_id="codex",
            capability_id="capability_inspect",
            budget={"quota": "50_calls", "latency_ms": 12, "reliability_score": 0.99},
            evidence={"observed_effect": "Inspected 2 capabilities", "evidence_refs": ["ref-1"], "provenance": "Agent OS Registry"},
            correlation_id="corr-view-1"
        )
        self.assertEqual(view["identity"]["actor_id"], "companion_ryan_build")
        self.assertEqual(view["runtime"]["runtime_id"], "rt-sovereign-node-1")
        self.assertEqual(view["adapter"]["harness_id"], "codex")
        self.assertEqual(view["capability"]["capability_id"], "capability_inspect")
        self.assertEqual(view["budget"]["latency_ms"], 12)
        self.assertEqual(view["evidence"]["observed_effect"], "Inspected 2 capabilities")

if __name__ == "__main__":
    unittest.main()
