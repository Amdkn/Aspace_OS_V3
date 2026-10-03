import unittest
from datetime import datetime, timezone
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from temporal_truth.core import TemporalTruth

class TestTemporalTruthCanary(unittest.TestCase):
    def setUp(self):
        self.t = TemporalTruth()

    def test_g1_canon_resurrection(self):
        """
        Encode the known Jules historical sequence as fixture claims:
        0 active -> 15 slots -> 12 IN_PROGRESS -> 12 PR open -> 7 PR open
        """
        sequence = [
            ("t1", "0 active", "2023-01-01T10:00:00Z"),
            ("t2", "15 slots", "2023-01-01T11:00:00Z"),
            ("t3", "12 IN_PROGRESS", "2023-01-01T12:00:00Z"),
            ("t4", "12 PR open", "2023-01-01T13:00:00Z"),
            ("t5", "7 PR open", "2023-01-01T14:00:00Z"),
        ]

        prev_id = None
        for i, (cid, val, ts) in enumerate(sequence):
            claim = {
                "schema": "aspace.temporal-claim.v1",
                "claim_id": cid,
                "source_ref": "runtime-observer",
                "source_authority": "jules",
                "recorded_at": ts,
                "observed_at": ts,
                "scope": "jules-sequence",
                "subject": "jules",
                "predicate": "status",
                "assertion": {"value": val},
                "evidence_refs": [f"ref-{cid}"],
                "temporal_state": "CURRENT",
                "supersedes": [prev_id] if prev_id else []
            }
            self.t.ingest_claim(claim)
            prev_id = cid

        self.assertEqual(len(self.t.claims), 5)
        self.assertIn("t1", self.t.claims)
        self.assertIn("t5", self.t.claims)

        st_t1 = self.t.state_at("jules", "status", "2023-01-01T10:30:00Z", "jules-sequence")
        self.assertEqual(st_t1["status"], "CURRENT")
        self.assertEqual(st_t1["claims"][0]["assertion"]["value"], "0 active")

        st_t3 = self.t.state_at("jules", "status", "2023-01-01T12:30:00Z", "jules-sequence")
        self.assertEqual(st_t3["status"], "CURRENT")
        self.assertEqual(st_t3["claims"][0]["assertion"]["value"], "12 IN_PROGRESS")

        st_t5 = self.t.state_at("jules", "status", "2023-01-01T14:30:00Z", "jules-sequence")
        self.assertEqual(st_t5["status"], "CURRENT")
        self.assertEqual(st_t5["claims"][0]["assertion"]["value"], "7 PR open")

        reinject = {
            "schema": "aspace.temporal-claim.v1",
            "claim_id": "t6",
            "source_ref": "runtime-observer",
            "source_authority": "jules",
            "recorded_at": "2023-01-01T15:00:00Z", # Later
            "observed_at": "2023-01-01T10:00:00Z", # Original
            "scope": "jules-sequence",
            "subject": "jules",
            "predicate": "status",
            "assertion": {"value": "0 active"},
            "evidence_refs": ["ref-t1-reinject"],
            "temporal_state": "HISTORICAL",
            "supersedes": []
        }
        self.t.ingest_claim(reinject)

        st_now = self.t.state_at("jules", "status", "2023-01-01T15:30:00Z", "jules-sequence")

        # Does not make it CURRENT - t5 still wins for the source_authority because its observed_at is later
        self.assertEqual(st_now["status"], "CURRENT")
        self.assertEqual(st_now["claims"][0]["assertion"]["value"], "7 PR open")

    def test_g2_split_brain(self):
        """
        Inputs:
        - GitHub recent mutation evidence;
        - WorkGraph 0 claim;
        - WorkGraph 0 binding;
        - no fresh runtime observation establishing ONLINE/OFFLINE.
        """
        self.t.ingest_claim({
            "schema": "aspace.temporal-claim.v1",
            "claim_id": "gh1",
            "source_ref": "github-webhook",
            "source_authority": "github",
            "recorded_at": "2023-01-01T10:00:00Z",
            "observed_at": "2023-01-01T10:00:00Z",
            "scope": "github",
            "subject": "jules-gh-mutations",
            "predicate": "mutation_state",
            "assertion": {"value": "active"},
            "evidence_refs": ["gh-event-1"],
            "temporal_state": "CURRENT"
        })

        self.t.ingest_claim({
            "schema": "aspace.temporal-claim.v1",
            "claim_id": "wg1",
            "source_ref": "uc.db",
            "source_authority": "kernel",
            "recorded_at": "2023-01-01T10:00:00Z",
            "observed_at": "2023-01-01T10:00:00Z",
            "scope": "workgraph",
            "subject": "jules",
            "predicate": "claim_count",
            "assertion": {"value": 0},
            "evidence_refs": ["db-snap-1"],
            "temporal_state": "CURRENT"
        })

        self.t.ingest_claim({
            "schema": "aspace.temporal-claim.v1",
            "claim_id": "wg2",
            "source_ref": "uc.db",
            "source_authority": "kernel",
            "recorded_at": "2023-01-01T10:00:00Z",
            "observed_at": "2023-01-01T10:00:00Z",
            "scope": "workgraph",
            "subject": "jules",
            "predicate": "binding_count",
            "assertion": {"value": 0},
            "evidence_refs": ["db-snap-1"],
            "temporal_state": "CURRENT"
        })

        st_gh = self.t.state_now("jules-gh-mutations", "mutation_state", "github")
        self.assertEqual(st_gh["status"], "CURRENT")
        self.assertEqual(st_gh["claims"][0]["assertion"]["value"], "active")

        st_wg1 = self.t.state_now("jules", "claim_count", "workgraph")
        self.assertEqual(st_wg1["status"], "CURRENT")
        self.assertEqual(st_wg1["claims"][0]["assertion"]["value"], 0)

        st_rt = self.t.state_now("jules", "status", "runtime")
        self.assertEqual(st_rt["status"], "UNKNOWN")

        snap_gh = self.t.snapshot_physiology("snap-gh", "github", [("jules-gh-mutations", "mutation_state")])
        self.assertEqual(snap_gh["dimensions"][0]["epistemic_state"], "KNOWN")

        snap_wg = self.t.snapshot_physiology("snap-wg", "workgraph", [("jules", "claim_count"), ("jules", "binding_count")])
        self.assertEqual(snap_wg["dimensions"][0]["epistemic_state"], "KNOWN")
        self.assertEqual(snap_wg["dimensions"][1]["epistemic_state"], "KNOWN")

        snap_rt = self.t.snapshot_physiology("snap-rt", "runtime", [("jules", "status")])
        self.assertEqual(snap_rt["dimensions"][0]["epistemic_state"], "UNKNOWN")

if __name__ == '__main__':
    unittest.main()
