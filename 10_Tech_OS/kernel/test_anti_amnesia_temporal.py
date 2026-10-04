import json
import unittest

from anti_amnesia import AntiAmnesiaEngine, ConversationIntentCompiler
from temporal_truth.temporal_truth import TemporalCanonGraph


class TestAntiAmnesiaTemporalG7(unittest.TestCase):
    def setUp(self):
        self.graph = TemporalCanonGraph()
        self.compiler = ConversationIntentCompiler(
            default_source_ref="chat://g7-source"
        )
        self.engine = AntiAmnesiaEngine(
            self.compiler,
            temporal_graph=self.graph,
        )

    def test_mixed_intent_is_temporal_before_projection_consumption(self):
        observed_at = "2026-10-03T10:00:00+00:00"
        record = self.engine.record_intent(
            (
                "We will implement code and open a PR for the kernel, "
                "update Linear governance A2, and create a Calendar Drive task in GWS."
            ),
            correlation_id="corr_g7_mixed",
            override_kind="MIXED",
            observed_at=observed_at,
        )

        self.assertIsNotNone(record.temporal_claim_id)
        claim = self.graph.claims[record.temporal_claim_id]
        self.assertEqual(claim["correlation_id"], record.correlation_id)
        self.assertEqual(claim["observed_at"], observed_at)
        self.assertNotEqual(claim["recorded_at"], observed_at)
        self.assertEqual(claim["assertion"]["verbatim"], record.verbatim)
        self.assertEqual(claim["assertion"]["ipbd_kind"], "MIXED")

        surfaces = {projection.surface for projection in record.projections}
        self.assertTrue(
            {"Supabase", "WorkGraph", "GitHub", "Linear", "GWS"}.issubset(
                surfaces
            )
        )
        for projection in record.projections:
            self.assertEqual(projection.correlation_id, "corr_g7_mixed")

        replay = self.graph.replay_history(
            subject=claim["subject"],
            scope="conversation-intent",
            t="2026-10-04T00:00:00+00:00",
            limit=8,
        )
        self.assertEqual(
            [item["claim_id"] for item in replay["claims"]],
            [record.temporal_claim_id],
        )
        self.assertEqual(replay["claims"][0]["source_ref"], "chat://g7-source")

    def test_projection_removal_does_not_delete_temporal_intent(self):
        record = self.engine.record_intent(
            "We will implement code and PR for the kernel.",
            correlation_id="corr_g7_projection_independence",
            observed_at="2026-10-03T11:00:00+00:00",
        )
        record.projections = [
            projection
            for projection in record.projections
            if projection.surface != "GitHub"
        ]

        self.assertNotIn("GitHub", {p.surface for p in record.projections})
        self.assertIn(record.temporal_claim_id, self.graph.claims)
        self.assertEqual(
            self.graph.claims[record.temporal_claim_id]["correlation_id"],
            record.correlation_id,
        )

    def test_unknown_intent_survives_anthology_replay(self):
        record = self.engine.record_intent(
            "mhm optional thoughts",
            correlation_id="corr_g7_unknown",
            override_kind="UNKNOWN",
            observed_at="2026-10-03T12:00:00+00:00",
        )
        claim = self.graph.claims[record.temporal_claim_id]
        self.assertEqual(claim["temporal_state"], "UNKNOWN")

        replay = self.graph.replay_history(
            subject=claim["subject"],
            scope="conversation-intent",
            t="2026-10-04T00:00:00+00:00",
            limit=8,
        )
        self.assertEqual(replay["claims"][0]["temporal_state"], "UNKNOWN")
        self.assertEqual(
            replay["claims"][0]["assertion"]["ipbd_kind"],
            "UNKNOWN",
        )

    def test_context_capsule_references_intent_without_transcript_dump(self):
        record = self.engine.record_intent(
            "We will implement code and PR for the kernel and update Linear governance.",
            correlation_id="corr_g7_capsule",
            observed_at="2026-10-03T13:00:00+00:00",
        )
        capsule = self.engine.compile_context_capsule_for_intent(
            correlation_id=record.correlation_id,
            holon_id="Ryan",
            mission_id="G7-Anti-Amnesia",
            authority_envelope={"scope": "build", "mode": "bounded"},
            return_to={"issue": "#507", "parent": "#448"},
            t="2026-10-04T00:00:00+00:00",
        )

        serialized = json.dumps(capsule, sort_keys=True)
        self.assertIn(record.temporal_claim_id, capsule["anthology_window"])
        self.assertIn("chat://g7-source", capsule["evidence_head"])
        self.assertEqual(
            capsule["source_slice"]["correlation_id"],
            record.correlation_id,
        )
        self.assertNotIn(record.verbatim, serialized)
        self.assertNotIn("next_action", capsule)


if __name__ == "__main__":
    unittest.main()
