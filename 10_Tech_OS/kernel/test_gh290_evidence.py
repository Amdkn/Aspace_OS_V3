import json
import unittest
from pathlib import Path

from truth_projection import project_truth


class GH290EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.repo_root = Path(__file__).resolve().parents[2]
        self.evidence_path = self.repo_root / "10_Tech_OS" / "kernel" / "evidence" / "gh290_tenant_provisioning_blocker.json"
        self.handoff_path = self.repo_root / "_INBOX" / "handoffs" / "BLOCKER-290-TENANT-PROVISIONING.md"

    def test_gh290_blocker_file_exists_and_conforms_to_schema(self):
        self.assertTrue(self.evidence_path.exists(), f"Evidence file not found: {self.evidence_path}")
        with open(self.evidence_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertEqual(data.get("schema"), "aspace.typed-blocker.v1")
        self.assertEqual(data.get("issue"), 290)
        self.assertEqual(data.get("blocker_type"), "MissingWriteAccess")
        self.assertEqual(data.get("resource"), "omk-services/OMK-DESKTOP-WEB-OS")
        self.assertIn("handoff_file", data)

    def test_gh290_handoff_file_exists(self):
        self.assertTrue(self.handoff_path.exists(), f"Handoff markdown file not found: {self.handoff_path}")

    def test_truth_projection_with_gh290_blocker_evidence(self):
        with open(self.evidence_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        projection = project_truth(
            value=data,
            source="evidence:gh290_tenant_provisioning_blocker.json",
            authority="kernel:blocker_registry",
            observed_at="2026-10-03T10:00:00Z",
            evidence_refs=[str(self.evidence_path.relative_to(self.repo_root))],
            freshness_seconds=86400,
            confidence=1.0,
            correlation_id=data.get("correlation_id", "gh290-test"),
            work_id=290,
        )

        self.assertEqual(projection["truth_state"], "CURRENT")
        self.assertEqual(projection["confidence_state"], "KNOWN")
        self.assertEqual(projection["value"]["status"], "BLOCKED_BY_PERMISSION")


if __name__ == "__main__":
    unittest.main(verbosity=2)
