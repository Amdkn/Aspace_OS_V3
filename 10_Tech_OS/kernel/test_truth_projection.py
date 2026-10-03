import unittest
from datetime import datetime, timedelta, timezone

from truth_projection import project_truth


class TruthProjectionTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 10, 2, 12, 0, tzinfo=timezone.utc)

    def current(self, **overrides):
        data = {
            "value": {"state": "AVAILABLE"},
            "source": "runtime-presence",
            "authority": "workgraph+runtime_presence",
            "observed_at": self.now.isoformat(),
            "evidence_refs": ["runtime:receipt:1"],
            "freshness_seconds": 60,
            "confidence": 0.9,
            "now": self.now,
            "correlation_id": "corr-1",
            "work_id": 42,
        }
        data.update(overrides)
        return project_truth(**data)

    def test_complete_provenance_is_current(self):
        p = self.current()
        self.assertEqual(p["truth_state"], "CURRENT")
        self.assertEqual(p["confidence_state"], "KNOWN")
        self.assertEqual(p["evidence_refs"], ["runtime:receipt:1"])

    def test_no_evidence_never_becomes_current(self):
        p = self.current(evidence_refs=[])
        self.assertEqual(p["truth_state"], "UNKNOWN")
        self.assertIn("evidence_refs", p["reason"])

    def test_missing_freshness_is_unknown(self):
        p = self.current(freshness_seconds=None, expires_at=None)
        self.assertEqual(p["truth_state"], "UNKNOWN")
        self.assertIn("freshness", p["reason"])

    def test_expired_evidence_is_stale_not_failed(self):
        p = self.current(
            observed_at=(self.now - timedelta(minutes=2)).isoformat(),
            freshness_seconds=30,
        )
        self.assertEqual(p["truth_state"], "STALE")
        self.assertEqual(p["reason"], "evidence_freshness_expired")

    def test_unknown_confidence_is_preserved(self):
        p = self.current(confidence=None)
        self.assertEqual(p["truth_state"], "CURRENT")
        self.assertIsNone(p["confidence"])
        self.assertEqual(p["confidence_state"], "UNKNOWN")

    def test_invalid_confidence_does_not_fabricate_certainty(self):
        p = self.current(confidence=2.0)
        self.assertIsNone(p["confidence"])
        self.assertEqual(p["confidence_state"], "UNKNOWN")


if __name__ == "__main__":
    unittest.main(verbosity=2)
