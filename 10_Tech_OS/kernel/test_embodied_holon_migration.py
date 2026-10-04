import copy
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

from dispatch_routing import DispatchRoutingError, migrate_mission_runtime
from temporal_truth.compiler import ContextCompiler
from temporal_truth.temporal_truth import TemporalCanonGraph


HERE = Path(__file__).resolve().parent
SCHEMA = HERE / "schema.sql"


class EmbodiedHolonMigrationCanary(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "uc.db"
        con = sqlite3.connect(self.db)
        con.executescript(SCHEMA.read_text(encoding="utf-8"))
        con.execute(
            "INSERT INTO work(layer,title,status,priority,attempts) "
            "VALUES('L1','G5 Ryan runtime migration','pending',1,0)"
        )
        self.work_id = int(con.execute("SELECT last_insert_rowid()").fetchone()[0])
        self.return_to = {"issue": 448, "gate": "G6"}
        self.authority = {
            "scope": "repo:bounded-cell",
            "write": ["worktree:502"],
            "effect": "bounded",
        }
        con.execute(
            "INSERT INTO event(work_id,harness,kind,payload) VALUES(?,?,?,?)",
            (
                self.work_id,
                "nardole-dispatch",
                "dispatch_envelope",
                json.dumps(
                    {
                        "schema": "aspace.dispatch-envelope.v2",
                        "work_id": self.work_id,
                        "correlation_id": "corr-502",
                        "return_route": self.return_to,
                        "required_capability": "RYAN",
                        "target_runtime": "runtime-a",
                        "target_harness": "claude_code",
                    },
                    sort_keys=True,
                ),
            ),
        )
        con.execute(
            """INSERT INTO claim(
                   work_id,harness,institutional_owner,runtime_id,expires_at
               ) VALUES(?,?,?,?,datetime('now', '+900 seconds'))""",
            (self.work_id, "claude_code", "ryan", "runtime-a"),
        )
        con.commit()
        con.close()

        graph = TemporalCanonGraph()
        self.cutoff = "2026-10-04T00:55:00+00:00"
        graph.ingest_claim(
            {
                "schema": "aspace.temporal-claim.v1",
                "claim_id": "claim-g5-runtime-a",
                "subject": "ryan",
                "predicate": "mission_state",
                "scope": "mission-502",
                "source_authority": "workgraph",
                "observed_at": "2026-10-04T00:54:00+00:00",
                "assertion": {"state": "IN_PROGRESS", "runtime": "runtime-a"},
                "evidence_refs": ["workgraph:502", "runtime:runtime-a"],
            }
        )
        compiler = ContextCompiler(graph)
        self.capsule = compiler.compile_context_capsule(
            holon_id="ryan",
            mission_id="mission-502",
            correlation_id="corr-502",
            scope="mission-502",
            authority_envelope=copy.deepcopy(self.authority),
            workgraph_neighborhood={
                "work_id": self.work_id,
                "owner": "ryan",
                "runtime": "runtime-a",
            },
            evidence_head=["github:issue:502"],
            return_to=copy.deepcopy(self.return_to),
            t=self.cutoff,
            anthology_window=["anthology:mission-502"],
            source_slice={"issue": 502, "work_id": self.work_id},
        )

    def tearDown(self):
        self.tmp.cleanup()

    def migrate(self, capsule=None, authority=None):
        return migrate_mission_runtime(
            self.db,
            self.work_id,
            target_runtime_id="runtime-b",
            target_harness="codex",
            reason="runtime-a lost during G5 canary",
            actor_id="ryan",
            authority_envelope=copy.deepcopy(
                self.authority if authority is None else authority
            ),
            context_capsule=copy.deepcopy(
                self.capsule if capsule is None else capsule
            ),
            identity_version="ryan-v4",
            workspace_fingerprint="worktree:502:sha256:test",
        )

    def test_g5_preserves_holon_continuity_and_fences_old_writer(self):
        self.assertNotIn("next_action", self.capsule)
        result = self.migrate()
        receipt = result["evidence_receipt"]

        self.assertEqual(receipt["continuity_result"], "PRESERVED")
        self.assertEqual(receipt["actor_id"], "ryan")
        self.assertEqual(receipt["work_id"], self.work_id)
        self.assertEqual(receipt["mission_id"], "mission-502")
        self.assertEqual(receipt["correlation_id"], "corr-502")
        self.assertEqual(receipt["identity_version"], "ryan-v4")
        self.assertEqual(receipt["from_harness"], "claude_code")
        self.assertEqual(receipt["from_runtime"], "runtime-a")
        self.assertEqual(receipt["to_harness"], "codex")
        self.assertEqual(receipt["to_runtime"], "runtime-b")
        self.assertEqual(receipt["return_to"], self.return_to)
        self.assertEqual(receipt["workspace_fingerprint"], "worktree:502:sha256:test")
        self.assertTrue(receipt["context_hash"])
        self.assertTrue(receipt["authority_hash"])
        self.assertIn("claim-g5-runtime-a", self.capsule["canon_slice"])
        self.assertIn("github:issue:502", receipt["evidence_head"])

        con = sqlite3.connect(self.db)
        claims = con.execute(
            "SELECT harness,institutional_owner,runtime_id FROM claim WHERE work_id=?",
            (self.work_id,),
        ).fetchall()
        event = con.execute(
            "SELECT payload FROM event WHERE work_id=? "
            "AND kind='embodiment_migration_receipt' ORDER BY id DESC LIMIT 1",
            (self.work_id,),
        ).fetchone()
        con.close()

        self.assertEqual(len(claims), 1)
        self.assertEqual(claims[0], ("codex", "ryan", "runtime-b"))
        durable = json.loads(event[0])
        self.assertEqual(durable["receipt_id"], receipt["receipt_id"])
        self.assertEqual(durable["context_hash"], receipt["context_hash"])
        self.assertEqual(durable["return_to"], self.return_to)

    def test_correlation_drift_fails_closed_without_replacing_writer(self):
        capsule = copy.deepcopy(self.capsule)
        capsule["correlation_id"] = "corr-drift"
        with self.assertRaisesRegex(DispatchRoutingError, "correlation_id mismatch"):
            self.migrate(capsule=capsule)
        self._assert_writer_still_runtime_a()

    def test_authority_widening_fails_closed_without_replacing_writer(self):
        wider = copy.deepcopy(self.authority)
        wider["write"].append("filesystem:C:/")
        with self.assertRaisesRegex(DispatchRoutingError, "authority envelope mismatch"):
            self.migrate(authority=wider)
        self._assert_writer_still_runtime_a()

    def test_identity_drift_and_imperative_capsule_fail_closed(self):
        capsule = copy.deepcopy(self.capsule)
        capsule["holon_id"] = "not-ryan"
        with self.assertRaisesRegex(DispatchRoutingError, "holon identity mismatch"):
            self.migrate(capsule=capsule)

        capsule = copy.deepcopy(self.capsule)
        capsule["next_action"] = "continue implementation"
        with self.assertRaisesRegex(DispatchRoutingError, "must not prescribe next_action"):
            self.migrate(capsule=capsule)

        self._assert_writer_still_runtime_a()

    def _assert_writer_still_runtime_a(self):
        con = sqlite3.connect(self.db)
        row = con.execute(
            "SELECT harness,institutional_owner,runtime_id FROM claim WHERE work_id=?",
            (self.work_id,),
        ).fetchone()
        con.close()
        self.assertEqual(row, ("claude_code", "ryan", "runtime-a"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
