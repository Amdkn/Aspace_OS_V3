import unittest
import json
import os
import shutil
from pathlib import Path
from datetime import datetime, timezone, timedelta
from radar import EmergenceRadar

class TestEmergenceRadar(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path("test_radar_output")
        self.test_dir.mkdir(exist_ok=True)
        self.radar = EmergenceRadar(out_dir=str(self.test_dir))

        # Helper datetimes
        self.now = datetime.now(timezone.utc)
        self.recent_time = (self.now - timedelta(days=5)).isoformat()
        self.old_time = (self.now - timedelta(days=60)).isoformat()

    def tearDown(self):
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_multi_source_ingestion_and_deduplication(self):
        # Create a dummy Discover AI report
        discover_report = {
            "results": [
                {
                    "status": "SUCCESS",
                    "packet": str(self.test_dir / "dummy_packet.json")
                }
            ]
        }

        dummy_packet = {
            "title": "AI Video 1",
            "video_id": "vid123",
            "timestamp": self.old_time,
            "extracted_context": {
                "citations": [
                    {"canonical_id": "arxiv:1234.5678", "status": "RESOLVED"},
                    {"canonical_id": "doi:10.123/456", "status": "RESOLVED"},
                    {"canonical_id": "NEEDS_REVIEW", "status": "NEEDS_REVIEW"}
                ]
            }
        }

        with open(self.test_dir / "dummy_report.json", "w") as f:
            json.dump(discover_report, f)
        with open(self.test_dir / "dummy_packet.json", "w") as f:
            json.dump(dummy_packet, f)

        # Ingest Discover AI
        self.radar.ingest_discover_ai(str(self.test_dir / "dummy_report.json"))

        # Ingest Independent Source citing the SAME arxiv paper
        indep_source = {
            "name": "User Browser History",
            "timestamp": self.recent_time,
            "citations": [
                {"canonical_id": "arxiv:1234.5678", "status": "RESOLVED"}
            ]
        }
        self.radar.ingest_independent_source(indep_source)

        # Run resolution
        self.radar.resolve_identities()

        # Check deduplication
        self.assertIn("arxiv:1234.5678", self.radar.canonical_map)
        self.assertIn("doi:10.123/456", self.radar.canonical_map)
        self.assertNotIn("NEEDS_REVIEW", self.radar.canonical_map)

        arxiv_sources = self.radar.canonical_map["arxiv:1234.5678"]
        self.assertEqual(len(arxiv_sources), 2, "Should have 2 distinct sources for arxiv:1234.5678")

        source_types = [s["type"] for s in arxiv_sources]
        self.assertIn("Discover AI", source_types)
        self.assertIn("independent", source_types)

    def test_temporal_acceleration_and_promotion(self):
        # We need at least one Discover AI (or WATCH S1) and one independent source
        # One older, one recent (to trigger acceleration)
        self.radar.canonical_map = {
            "arxiv:9999.9999": [
                {"type": "Discover AI", "timestamp": self.old_time},
                {"type": "independent", "timestamp": self.recent_time}
            ],
            "arxiv:0000.0000": [
                {"type": "Discover AI", "timestamp": self.old_time}
            ]
        }

        self.radar.check_temporal_acceleration()

        # Check acceleration scores
        self.assertTrue(self.radar.acceleration_scores["arxiv:9999.9999"] > 0)
        self.assertEqual(self.radar.acceleration_scores["arxiv:0000.0000"], 0.0)

        # Build lineages and map capabilities
        self.radar.build_lineages()
        self.radar.map_capabilities()

        # Should have 2 lineages
        self.assertEqual(len(self.radar.lineages), 2)

        # One should be a candidate, one a gap
        self.assertEqual(len(self.radar.promoted_candidates), 1)
        self.assertEqual(len(self.radar.gaps), 1)

        candidate = self.radar.promoted_candidates[0]
        self.assertTrue("arxiv_9999.9999" in candidate.candidate_id)
        self.assertEqual(candidate.architecture["status"], "PROMOTED")

        gap = self.radar.gaps[0]
        self.assertTrue("arxiv_0000.0000" in gap.gap_id)

    def test_report_generation_and_provenance(self):
        self.radar.canonical_map = {
            "arxiv:1111.1111": [
                {"type": "watch_s1", "timestamp": self.recent_time},
                {"type": "independent", "timestamp": self.recent_time}
            ]
        }
        self.radar.check_temporal_acceleration()
        self.radar.build_lineages()
        self.radar.map_capabilities()

        report = self.radar.generate_report()

        # Check provenance
        self.assertEqual(report["provenance"]["routed_to"], "Graham/REMEMBER")

        # Check Clara receives only candidate
        self.assertEqual(len(report["clara_payload"]), 1)
        self.assertEqual(len(report["graham_payload"]["lineages"]), 1)

    def test_architecture_robust_without_discover_ai(self):
        # Even without Discover AI, WATCH S1 + PAPER S1 + Independent should promote
        self.radar.canonical_map = {
            "arxiv:2222.2222": [
                {"type": "watch_s1", "timestamp": self.recent_time},
                {"type": "paper_s1", "timestamp": self.recent_time},
                {"type": "independent", "timestamp": self.recent_time}
            ]
        }
        self.radar.check_temporal_acceleration()
        self.radar.build_lineages()
        self.radar.map_capabilities()

        self.assertEqual(len(self.radar.promoted_candidates), 1)

    def test_pipeline_integration(self):
        # We'll just run it empty to verify it doesn't crash
        report = self.radar.run_pipeline()
        self.assertIn("timestamp", report)
        self.assertEqual(report["lineages_identified"], 0)

if __name__ == "__main__":
    unittest.main()
