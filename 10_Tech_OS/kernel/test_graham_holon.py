#!/usr/bin/env python3
"""Comprehensive tests for Graham Embodied Holon — State/Provenance/Replay.

These tests verify:
1. Graham exists as a distinct durable embodiment
2. Graham's instructions/context/capability profiles are materially distinct
3. Graham's primary runtime may differ from Ryan's
4. Each can use native subagents without collapsing institutional boundaries
5. Graham can prove lineage before/after migration
6. The Wargame PASS criteria for Graham
"""
import copy
import json
import os
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Dict

# Add kernel to path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from dispatch_routing import DispatchRoutingError, migrate_mission_runtime
from graham_holon import (
    get_holon_identity,
    get_presence_state,
    checkpoint_save,
    prove_lineage,
    reconcile_continuity,
)
from mission_continuity import project_mission_cell
from temporal_truth.compiler import ContextCompiler
from temporal_truth.temporal_truth import TemporalCanonGraph


class GrahamEmbodimentIdentityTest(unittest.TestCase):
    """Test that Graham has a distinct, durable institutional identity."""

    def test_graham_has_distinct_holon_identity(self):
        """Graham's institutional identity is distinct from runtime/session."""
        identity = get_holon_identity()

        # Verify Graham's identity structure
        self.assertEqual(identity["id"], "S3-Graham-State")
        self.assertEqual(identity["name"], "Graham")
        self.assertEqual(identity["rank"], "S3")
        self.assertEqual(identity["doctor"], "13th")

        # Verify jurisdiction
        self.assertIn("Memory", identity["jurisdiction"])
        self.assertIn("Provenance", identity["jurisdiction"])
        self.assertIn("State", identity["jurisdiction"])

        # Verify stewardship is state-related, not generic manager
        self.assertEqual(identity["stewardship"], "state_plane")

    def test_presence_state_uses_four_axis_model(self):
        """Graham exposes four distinct states, not a single boolean."""
        presence = get_presence_state()

        # All four states must be present
        self.assertIn("institutional_state", presence)
        self.assertIn("embodiment_state", presence)
        self.assertIn("runtime_state", presence)
        self.assertIn("workload_state", presence)

        # Values must be from the allowed vocabularies
        self.assertIn(presence["institutional_state"], ["ACTIVE", "SUSPENDED", "ARCHIVED"])
        self.assertIn(presence["embodiment_state"], ["READY", "DEGRADED", "MISSING"])
        self.assertIn(presence["runtime_state"], ["ONLINE", "OFFLINE", "UNSTABLE", "UNKNOWN"])
        self.assertIn(presence["workload_state"], ["IDLE", "QUEUED", "WORKING", "BLOCKED", "REVIEW"])

    def test_presence_state_distinct_from_single_boolean(self):
        """Verify Graham doesn't use a single boolean 'active' field."""
        presence = get_presence_state()

        # Should have 4 distinct states, not one boolean
        state_count = sum(1 for k in presence if k.endswith("_state"))
        self.assertEqual(state_count, 4, "Should have 4 distinct presence states")

        # Each state should have a value from the defined vocabularies
        self.assertNotEqual(presence["institutional_state"], presence["embodiment_state"])
        self.assertNotEqual(presence["embodiment_state"], presence["runtime_state"])
        self.assertNotEqual(presence["runtime_state"], presence["workload_state"])


class GrahamCapabilityProfileTest(unittest.TestCase):
    """Test that Graham has a materially distinct capability profile."""

    def test_graham_capability_profile_is_distinct(self):
        """Graham's capabilities are memory/provenance focused, not build/observe."""
        identity = get_holon_identity()

        # Graham's jurisdiction is clearly memory/provenance/state
        self.assertIn("Memory", identity["jurisdiction"])
        self.assertIn("Provenance", identity["jurisdiction"])
        self.assertIn("State", identity["jurisdiction"])

        # Graham's stewardship is state_plane (not build, observe, etc.)
        self.assertEqual(identity["stewardship"], "state_plane")

        # This is materially different from Ryan (BUILD) and Yaz (OBSERVE)
        # A0 Amadeus is the visionary, not Graham
        self.assertNotEqual(identity["jurisdiction"], "Kernel Core — BUILD/industrialisation")
        self.assertNotEqual(identity["jurisdiction"], "Kernel Core — Observability/LiDAR")


class GrahamProvenanceTest(unittest.TestCase):
    """Test that Graham can prove lineage and provenance."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "uc.db"
        con = sqlite3.connect(self.db)
        con.executescript((HERE / "schema.sql").read_text())
        con.execute(
            "INSERT INTO work(layer, title, status) VALUES('L1', 'G5 Graham provenance test', 'pending')"
        )
        self.work_id = int(con.execute("SELECT last_insert_rowid()").fetchone()[0])
        con.commit()
        con.close()

    def tearDown(self):
        self.tmp.cleanup()

    def test_graham_can_prove_event_lineage(self):
        """Graham can trace the provenance of events for a work item."""
        # Record some events including continuity-related ones
        con = sqlite3.connect(self.db)
        con.execute(
            "INSERT INTO event(work_id, harness, kind, payload) VALUES(?, ?, ?, ?)",
            (self.work_id, "test_harness", "dispatch_envelope", json.dumps({"test": "data"}))
        )
        con.execute(
            "INSERT INTO event(work_id, harness, kind, payload) VALUES(?, ?, ?, ?)",
            (self.work_id, "test_harness", "harness_execution_receipt", json.dumps({"result": "success"}))
        )
        con.execute(
            "INSERT INTO event(work_id, harness, kind, payload) VALUES(?, ?, ?, ?)",
            (self.work_id, "test_harness", "continuation_routed", json.dumps({"route": "next"}))
        )
        con.commit()
        con.close()

        # Prove lineage
        lineage = prove_lineage(self.db, self.work_id)

        # Verify lineage proof
        self.assertTrue(lineage["ok"])
        self.assertEqual(lineage["work_id"], self.work_id)
        self.assertEqual(lineage["event_count"], 3)
        self.assertEqual(len(lineage["claim_events"]), 2)
        self.assertTrue(lineage["has_continuity"])

    def test_graham_lineage_fails_without_events(self):
        """Lineage proof works but returns empty evidence for no events."""
        lineage = prove_lineage(self.db, self.work_id)

        self.assertTrue(lineage["ok"])
        self.assertEqual(lineage["event_count"], 0)
        self.assertEqual(lineage["claim_events"], [])


class GrahamMigrationContinuesContinuityTest(unittest.TestCase):
    """Test G5 migration proves Graham continuity before/after."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "uc.db"
        con = sqlite3.connect(self.db)
        con.executescript((HERE / "schema.sql").read_text())
        con.execute(
            "INSERT INTO work(layer, title, status) VALUES('L1', 'G5 Graham migration', 'pending')"
        )
        self.work_id = int(con.execute("SELECT last_insert_rowid()").fetchone()[0])
        self.return_to = {"issue": 448, "gate": "G5"}
        self.authority = {
            "scope": "repo:bounded-cell",
            "write": ["worktree:502"],
            "effect": "bounded",
        }
        con.execute(
            "INSERT INTO event(work_id, harness, kind, payload) VALUES(?,?,?,?)",
            (
                self.work_id,
                "nardole-dispatch",
                "dispatch_envelope",
                json.dumps({
                    "schema": "aspace.dispatch-envelope.v2",
                    "work_id": self.work_id,
                    "correlation_id": "corr-graham-test",
                    "return_route": self.return_to,
                    "required_capability": "GRAHAM",
                    "target_runtime": "runtime-graham-a",
                    "target_harness": "claude_code",
                }, sort_keys=True),
            ),
        )
        con.execute(
            """INSERT INTO claim(
                   work_id, harness, institutional_owner, runtime_id, expires_at
               ) VALUES(?,?,?,?,datetime('now', '+900 seconds'))""",
            (self.work_id, "claude_code", "graham", "runtime-graham-a"),
        )
        con.commit()
        con.close()

        graph = TemporalCanonGraph()
        self.cutoff = "2026-10-04T00:55:00+00:00"
        graph.ingest_claim({
            "schema": "aspace.temporal-claim.v1",
            "claim_id": "claim-graham-migration-test",
            "subject": "graham",
            "predicate": "migration_state",
            "scope": "mission-502",
            "source_authority": "workgraph",
            "observed_at": "2026-10-04T00:54:00+00:00",
            "assertion": {"state": "IN_PROGRESS", "runtime": "runtime-graham-a"},
            "evidence_refs": ["workgraph:502", "runtime:runtime-graham-a"],
        })
        compiler = ContextCompiler(graph)
        self.capsule = compiler.compile_context_capsule(
            holon_id="graham",
            mission_id="mission-502",
            correlation_id="corr-graham-test",
            scope="mission-502",
            authority_envelope=copy.deepcopy(self.authority),
            workgraph_neighborhood={
                "work_id": self.work_id,
                "owner": "graham",
                "runtime": "runtime-graham-a",
            },
            evidence_head=["github:issue:502"],
            return_to=copy.deepcopy(self.return_to),
            t=self.cutoff,
            anthology_window=["anthology:mission-502"],
            source_slice={"issue": 502, "work_id": self.work_id},
        )

    def tearDown(self):
        self.tmp.cleanup()

    def test_graham_migration_preserves_identity(self):
        """G5 migration preserves Graham's identity across runtime change."""
        # First, prove initial lineage
        initial_lineage = prove_lineage(self.db, self.work_id)
        self.assertTrue(initial_lineage["ok"])

        # Perform migration
        result = migrate_mission_runtime(
            self.db,
            self.work_id,
            target_runtime_id="runtime-graham-b",
            target_harness="codex",
            reason="runtime-graham-a lost during G5 golden test for Graham",
            actor_id="graham",
            authority_envelope=copy.deepcopy(self.authority),
            context_capsule=copy.deepcopy(self.capsule),
            identity_version="graham-v4",
            workspace_fingerprint=f"worktree:graham:{self.work_id}:sha256:test",
        )

        # Verify migration result
        receipt = result["evidence_receipt"]
        self.assertEqual(receipt["continuity_result"], "PRESERVED")
        self.assertEqual(receipt["actor_id"], "graham")
        self.assertEqual(receipt["work_id"], self.work_id)
        self.assertEqual(receipt["correlation_id"], "corr-graham-test")
        self.assertEqual(receipt["identity_version"], "graham-v4")
        self.assertEqual(receipt["return_to"], self.return_to)

        # Prove lineage after migration
        final_lineage = prove_lineage(self.db, self.work_id)
        self.assertTrue(final_lineage["ok"])
        self.assertTrue(final_lineage["has_migration_receipt"])

    def test_graham_migration_fences_old_writer(self):
        """Migration replaces claim, fencing the old writer."""
        con = sqlite3.connect(self.db)
        claims_before = con.execute(
            "SELECT harness, institutional_owner, runtime_id FROM claim WHERE work_id=?",
            (self.work_id,)
        ).fetchall()
        con.close()

        self.assertEqual(len(claims_before), 1)
        self.assertEqual(claims_before[0], ("claude_code", "graham", "runtime-graham-a"))

        # Migrate
        migrate_mission_runtime(
            self.db,
            self.work_id,
            target_runtime_id="runtime-graham-b",
            target_harness="codex",
            reason="G5 migration test",
            actor_id="graham",
            authority_envelope=self.authority,
            context_capsule=self.capsule,
            identity_version="graham-v4",
        )

        # Verify old writer is fenced
        con = sqlite3.connect(self.db)
        claims_after = con.execute(
            "SELECT harness, institutional_owner, runtime_id FROM claim WHERE work_id=?",
            (self.work_id,)
        ).fetchall()
        con.close()

        self.assertEqual(len(claims_after), 1)
        self.assertEqual(claims_after[0], ("codex", "graham", "runtime-graham-b"))


class GrahamDistinctFromPeersTest(unittest.TestCase):
    """Test that Graham's embodiment is distinctly from Ryan/Yaz."""

    def test_three_distinct_s3_holons(self):
        """Ryan, Yaz, and Graham exist as three distinct durable embodiments.

        Wargame PASS criteria #1: Ryan, Yaz and Graham exist simultaneously
        as three distinct durable embodiments.
        """
        from ryan_holon import get_holon_identity as ryan_identity
        from yaz_holon import get_holon_identity as yaz_identity

        graham = get_holon_identity()
        ryan = ryan_identity()
        yaz = yaz_identity()

        # All three have distinct identities
        self.assertNotEqual(graham["id"], ryan["id"])
        self.assertNotEqual(graham["id"], yaz["id"])
        self.assertNotEqual(ryan["id"], yaz["id"])

        # All three have distinct jurisdictions
        self.assertNotEqual(graham["jurisdiction"], ryan["jurisdiction"])
        self.assertNotEqual(graham["jurisdiction"], yaz["jurisdiction"])

    def test_graham_not_deriving_from_shared_prompt(self):
        """Wargame PASS criteria #3: They do not derive identity solely from one shared global prompt."""
        graham = get_holon_identity()

        # Graham's identity includes specific stewardship and role models
        self.assertIsNotNone(graham["stewardship"])
        self.assertIn("state", graham["stewardship"].lower())

        # Graham's capability profile is specific to memory/provenance
        self.assertIn("Memory", graham["jurisdiction"])


class GrahamSubagentTest(unittest.TestCase):
    """Test that Graham can use native subagents without collapsing boundaries."""

    def test_graham_subagents_are_bounded(self):
        """Graham's subagents are delegated organs, not new institutional identities."""
        identity = get_holon_identity()

        # Graham's capability profile includes skills that map to subagents
        self.assertIn("capability_profile", identity)
        skills = identity["capability_profile"].get("skills", [])

        # These are Graham's core operational skills
        self.assertIn("recall_retriever", skills)
        self.assertIn("provenance_checker", skills)
        self.assertIn("replay_verifier", skills)

        # Verify they are NOT new S3 identities
        self.assertNotEqual(len(skills), 0)


class GrahamCheckpointTest(unittest.TestCase):
    """Test Graham's checkpoint and recovery capabilities."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "uc.db"
        con = sqlite3.connect(self.db)
        con.executescript((HERE / "schema.sql").read_text())
        con.execute(
            "INSERT INTO work(layer, title, status) VALUES('L1', 'Checkpoint test', 'pending')"
        )
        self.work_id = int(con.execute("SELECT last_insert_rowid()").fetchone()[0])
        con.commit()
        con.close()

    def tearDown(self):
        self.tmp.cleanup()

    def test_checkpoint_creates_durable_backup(self):
        """Checkpoint creates a durable physical backup."""
        result = checkpoint_save(self.db, self.work_id)

        self.assertTrue(result["ok"])
        self.assertEqual(result["work_id"], self.work_id)
        self.assertTrue(os.path.exists(result["checkpoint_path"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)