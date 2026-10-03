import unittest
from anti_amnesia import (
    ConversationIntentCompiler,
    AntiAmnesiaEngine,
    reconstruct_cubefarm_frontier,
)


class TestAntiAmnesia(unittest.TestCase):

    def setUp(self):
        self.compiler = ConversationIntentCompiler(default_source_ref="https://chatgpt.com/c/test-session-123")
        self.engine = AntiAmnesiaEngine(self.compiler)

    def test_verbatim_capture_and_summary(self):
        verbatim = "We must fix the failing CI pipeline for CubeFarm fork integration and push a clean PR."
        record = self.compiler.compile(verbatim)

        self.assertEqual(record.verbatim, verbatim)
        self.assertEqual(record.source_ref, "https://chatgpt.com/c/test-session-123")
        self.assertTrue(record.is_commitment)
        self.assertTrue(record.summary.startswith("We must fix the failing CI pipeline"))

    def test_classify_kind(self):
        self.assertEqual(self.compiler.classify_kind("bug in kernel"), "PROBLEMATIQUE")
        self.assertEqual(self.compiler.classify_kind("We need a new edge function for intent capture"), "BESOIN")
        self.assertEqual(self.compiler.classify_kind("We will build the Living Office spatial projection"), "INTENTION")
        self.assertEqual(self.compiler.classify_kind("We need to fix the bug and we will build the feature"), "MIXED")
        self.assertEqual(self.compiler.classify_kind("hello"), "UNKNOWN")
        self.assertEqual(self.compiler.classify_kind(""), "UNKNOWN")

    def test_commitment_detection(self):
        self.assertTrue(self.compiler.detect_commitment("I will implement feature #405 now"))
        self.assertTrue(self.compiler.detect_commitment("Fix the failing test in kernel"))
        self.assertFalse(self.compiler.detect_commitment("Just pondering about philosophy and coffee"))

    def test_projections_linked_by_single_correlation_id(self):
        verbatim = "We will implement code and PR for cubefarm in GitHub, update Linear governance B1, and log GWS drive task."
        record = self.compiler.compile(verbatim, correlation_id="corr_shared_test_123")

        self.assertEqual(record.correlation_id, "corr_shared_test_123")
        self.assertGreaterEqual(len(record.projections), 3)

        surfaces = {p.surface for p in record.projections}
        self.assertIn("Supabase", surfaces)
        self.assertIn("WorkGraph", surfaces)
        self.assertIn("GitHub", surfaces)
        self.assertIn("Linear", surfaces)
        self.assertIn("GWS", surfaces)

        for proj in record.projections:
            self.assertEqual(proj.correlation_id, "corr_shared_test_123")

    def test_unknown_intent_preserved_durable(self):
        verbatim = "mhm optional thoughts"
        record = self.compiler.compile(verbatim)

        self.assertEqual(record.ipbd_kind, "UNKNOWN")
        self.assertEqual(record.verbatim, verbatim)
        # Even UNKNOWN intent gets Supabase IPBD and WorkGraph projections
        surfaces = {p.surface for p in record.projections}
        self.assertIn("Supabase", surfaces)
        self.assertIn("WorkGraph", surfaces)

    def test_engine_record_and_retrieve(self):
        record1 = self.engine.record_intent("First intent statement requiring fix", correlation_id="corr_1")
        record2 = self.engine.record_intent("Second intent statement for corr_1", correlation_id="corr_1")
        self.engine.record_intent("Third intent for corr_2", correlation_id="corr_2")

        corr_1_records = self.engine.get_by_correlation_id("corr_1")
        self.assertEqual(len(corr_1_records), 2)
        self.assertEqual(corr_1_records[0].intent_id, record1.intent_id)
        self.assertEqual(corr_1_records[1].intent_id, record2.intent_id)

    def test_empty_verbatim_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.compiler.compile("")

        with self.assertRaises(ValueError):
            self.compiler.compile("   \n  ")

    def test_reconstruct_cubefarm_frontier(self):
        frontier = reconstruct_cubefarm_frontier()

        self.assertEqual(frontier["work_id"], 405)
        self.assertEqual(frontier["canary"], "CubeFarm fork chain replay")

        durable = frontier["durable_state"]
        self.assertIn("fork_topology", durable)
        self.assertEqual(durable["fork_topology"]["issue"], "#402")
        self.assertEqual(durable["fork_topology"]["upstream"], "https://github.com/leonvanzyl/cubefarm.git")
        self.assertEqual(durable["fork_topology"]["origin"], "https://github.com/Amdkn/cubefarm.git")

        self.assertIn("living_office", durable)
        self.assertEqual(durable["living_office"]["issue"], "#403")

        self.assertIn("browser_harness_bridge", durable)
        self.assertEqual(durable["browser_harness_bridge"]["issue"], "#404")

        self.assertIn("multi_theme_canary", durable)
        self.assertEqual(durable["multi_theme_canary"]["issue"], "#400")

        self.assertIn("universal_constructor", durable)
        self.assertEqual(durable["universal_constructor"]["issue"], "#388")

        self.assertIn("return_to", durable)
        self.assertIn("#388", durable["return_to"])
        self.assertIn("Ryan", durable["return_to"])

        self.assertIn("next_actionable_step", frontier)


if __name__ == "__main__":
    unittest.main()
