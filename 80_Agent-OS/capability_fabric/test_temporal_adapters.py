import importlib
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

temporal_adapters = importlib.import_module("80_Agent-OS.capability_fabric.temporal_adapters")
registry_mod = importlib.import_module("80_Agent-OS.capability_fabric.registry")
adapters_mod = importlib.import_module("80_Agent-OS.capability_fabric.adapters")
temporal_truth = importlib.import_module("10_Tech_OS.kernel.temporal_truth.temporal_truth")
compiler_mod = importlib.import_module("10_Tech_OS.kernel.temporal_truth.compiler")


class TestTemporalAdapters(unittest.TestCase):
    def setUp(self):
        self.graph = temporal_truth.TemporalCanonGraph()
        self.cutoff = "2026-10-04T01:00:00+00:00"
        self.graph.ingest_claim(
            {
                "schema": "aspace.temporal-claim.v1",
                "claim_id": "claim-g6",
                "subject": "ryan",
                "predicate": "runtime_state",
                "scope": "mission-504",
                "source_authority": "yaz",
                "observed_at": "2026-10-04T00:59:00+00:00",
                "assertion": "UNKNOWN",
                "evidence_refs": ["runtime:observation:504"],
            }
        )
        self.compiler = compiler_mod.ContextCompiler(self.graph)
        self.registry = registry_mod.CapabilityRegistry()
        temporal_adapters.register_temporal_capabilities(
            self.registry, self.graph, self.compiler
        )

    def test_all_g6_capabilities_are_registered_as_graham_queries(self):
        expected = {
            "canon.resolve",
            "canon.state_at",
            "context.compile",
            "physiology.snapshot",
            "anthology.replay",
        }
        actual = {c.capability_id for c in self.registry.list_capabilities()}
        self.assertTrue(expected.issubset(actual))
        for capability_id in expected:
            cap = self.registry.get_capability(capability_id)
            self.assertEqual(cap.domain_owner, "Graham / Temporal Truth")
            self.assertEqual(cap.effect_class, "QUERY")
            self.assertEqual(set(cap.supported_surfaces), {"cli", "api", "mcp", "harness"})

    def test_canon_state_at_has_same_semantics_across_cli_api_mcp(self):
        payload = {
            "subject": "ryan",
            "predicate": "runtime_state",
            "scope": "mission-504",
            "t": self.cutoff,
        }
        results = []
        for adapter_cls in (
            adapters_mod.CLIAdapter,
            adapters_mod.APIAdapter,
            adapters_mod.MCPAdapter,
        ):
            result = adapter_cls(self.registry).invoke(
                "canon.state_at", payload, "corr-g6"
            )
            self.assertEqual(result["status"], "SUCCESS")
            self.assertEqual(result["receipt"]["correlation_id"], "corr-g6")
            self.assertIn("runtime:observation:504", result["receipt"]["evidence_refs"])
            results.append(result["data"])
        self.assertEqual(results[0], results[1])
        self.assertEqual(results[1], results[2])
        self.assertEqual(results[0]["states"][0]["assertion"], "UNKNOWN")

    def test_context_compile_preserves_unknown_and_has_no_imperative(self):
        payload = {
            "holon_id": "ryan",
            "mission_id": "mission-504",
            "scope": "mission-504",
            "authority_envelope": {"scope": "read-only"},
            "workgraph_neighborhood": {"work_id": 504},
            "evidence_head": ["github:issue:504"],
            "return_to": {"issue": 448, "gate": "G7"},
            "t": self.cutoff,
            "anthology_window": ["anthology:g6"],
            "source_slice": {"issue": 504},
        }
        result = adapters_mod.MCPAdapter(self.registry).invoke(
            "context.compile", payload, "corr-g6-context"
        )
        self.assertEqual(result["status"], "SUCCESS")
        self.assertEqual(result["receipt"]["correlation_id"], "corr-g6-context")
        self.assertEqual(result["data"]["correlation_id"], "corr-g6-context")
        self.assertNotIn("next_action", result["data"])
        self.assertNotIn("prompt", result["data"])
        self.assertIn("claim-g6", result["data"]["canon_slice"])

    def test_anthology_replay_is_bounded_and_source_linked(self):
        result = adapters_mod.APIAdapter(self.registry).invoke(
            "anthology.replay",
            {
                "subject": "ryan",
                "scope": "mission-504",
                "t": self.cutoff,
                "limit": 1,
            },
            "corr-g6-replay",
        )
        self.assertEqual(result["status"], "SUCCESS")
        replay = result["data"]
        self.assertEqual(replay["limit"], 1)
        self.assertEqual(len(replay["claims"]), 1)
        self.assertEqual(replay["claims"][0]["claim_id"], "claim-g6")
        self.assertIn("runtime:observation:504", result["receipt"]["evidence_refs"])

        failed = adapters_mod.APIAdapter(self.registry).invoke(
            "anthology.replay",
            {"limit": 129},
            "corr-g6-replay-bad",
        )
        self.assertEqual(failed["status"], "UNKNOWN")
        self.assertIn("limit", failed["error"])

    def test_physiology_snapshot_preserves_unknown_dimension(self):
        result = adapters_mod.CLIAdapter(self.registry).invoke(
            "physiology.snapshot",
            {
                "subject": "ryan",
                "scope": "mission-504",
                "requested_predicates": ["runtime_state"],
                "t": self.cutoff,
            },
            "corr-g6-phys",
        )
        self.assertEqual(result["status"], "SUCCESS")
        dims = result["data"]["dimensions"]
        self.assertEqual(len(dims), 1)
        self.assertEqual(dims[0]["value"], "UNKNOWN")
        self.assertEqual(dims[0]["source_authority"], "yaz")


if __name__ == "__main__":
    unittest.main(verbosity=2)
