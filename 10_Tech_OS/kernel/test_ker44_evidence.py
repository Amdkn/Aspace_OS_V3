from contextlib import closing
import hashlib
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path
from topology_validator import load_constitution, validate_constitution, ROLES, HERE
from dao_jing import project, encode, MAX_BYTES

class ConstitutionTests(unittest.TestCase):
    def setUp(self):
        self.doc = load_constitution()

    def test_complete_canonical_contract(self):
        validate_constitution(self.doc)
        self.assertEqual(len(self.doc["projection_roles"]), 13)
        self.assertEqual(self.doc, json.loads((HERE/"companion_constitution_v2.json").read_text(encoding="utf8")))

    def test_duplicate_positions_rejected(self):
        self.doc["companions"][1]["position"] = 1
        with self.assertRaisesRegex(ValueError, "Positions"):
            validate_constitution(self.doc)

    def test_boolean_position_rejected(self):
        self.doc["companions"][0]["position"] = True
        with self.assertRaisesRegex(ValueError, "Positions"):
            validate_constitution(self.doc)

    def test_forbidden_grant_rejected(self):
        self.doc["companions"][0]["authority"].append("promote_own_work")
        with self.assertRaisesRegex(ValueError, "forbidden authority grant"):
            validate_constitution(self.doc)

    def test_removed_authority_guard_rejected(self):
        self.doc["companions"][0]["forbidden_authority"] = []
        with self.assertRaisesRegex(ValueError, "protection missing"):
            validate_constitution(self.doc)

    def test_open_loop_rejected(self):
        self.doc["topology"]["horizontal"].pop()
        with self.assertRaisesRegex(ValueError, "loop must close"):
            validate_constitution(self.doc)

    def test_broken_handoff_rejected(self):
        self.doc["companions"][-1]["handoffs"]["next"] = "Ryan"
        with self.assertRaisesRegex(ValueError, "broken handoff"):
            validate_constitution(self.doc)

    def test_harness_identity_rejected(self):
        self.doc["companions"][0]["effectors"].append("ryan")
        with self.assertRaisesRegex(ValueError, "harness cannot"):
            validate_constitution(self.doc)

    def test_home_exclusivity_rejected(self):
        self.doc["companions"][0]["home_exclusive"] = True
        with self.assertRaisesRegex(ValueError, "cross-core"):
            validate_constitution(self.doc)

    def test_duplicate_identity_and_tier_rejected(self):
        self.doc["companions"][1]["id"] = self.doc["companions"][0]["id"]
        self.doc["companions"][1]["organization_tier"] = "Doctor S2"
        with self.assertRaises(ValueError):
            validate_constitution(self.doc)

class ProjectionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.db = Path(self.tmp.name)/"world.db"
        with closing(sqlite3.connect(self.db)) as c, c:
            c.executescript("""
            CREATE TABLE work(id INTEGER PRIMARY KEY, layer TEXT,title TEXT,status TEXT,updated_at TEXT);
            CREATE TABLE claim(work_id INTEGER,harness TEXT,expires_at TEXT);
            CREATE TABLE session_binding(id INTEGER PRIMARY KEY,work_id INTEGER,harness TEXT,status TEXT,ended_at TEXT);
            CREATE TABLE artifact(id INTEGER PRIMARY KEY,work_id INTEGER,kind TEXT,sha256 TEXT);
            CREATE TABLE gate_decision(id INTEGER PRIMARY KEY,work_id INTEGER,gate TEXT,verdict TEXT);
            INSERT INTO work VALUES(1,'L0','Kernel','claimed','2026-09-23 10:00:00');
            INSERT INTO work VALUES(2,'L1','Life','pending','2026-09-23 10:00:00');
            INSERT INTO work VALUES(3,'L2','Business','done','2026-09-23 10:00:00');
            INSERT INTO claim VALUES(1,'hermes','2026-09-23 09:00:00');
            INSERT INTO session_binding VALUES(1,1,'hermes','active',NULL);
            """)
        self.now = "2026-09-23T11:00:00+00:00"

    def projection(self, role="Rick", work_id=None):
        return project(self.db,role,work_id,as_of=self.now)

    def test_all_thirteen_roles_reproducible_and_readonly(self):
        before = self.db.read_bytes()
        for role in ROLES:
            a = self.projection(role)
            self.assertEqual(a,self.projection(role))
            self.assertEqual(a["authority"],"read_only")
            self.assertLessEqual(len(encode(a)),MAX_BYTES)
        self.assertEqual(before,self.db.read_bytes())

    def test_state_change_changes_projection(self):
        before = self.projection()
        with closing(sqlite3.connect(self.db)) as c, c:
            c.execute("UPDATE work SET title='New persistent fact' WHERE id=2")
        after = self.projection()
        self.assertNotEqual(before["snapshot_sha256"],after["snapshot_sha256"])
        self.assertIn("New persistent fact",encode(after).decode())

    def test_doctor_home_scope_and_explicit_cross_core_focus(self):
        self.assertEqual([x["work_id"] for x in self.projection("Doctor11")["items"]],[2])
        self.assertEqual(self.projection("Doctor11",1)["items"][0]["work_id"],1)

    def test_drift_is_observed_not_repaired(self):
        item = self.projection(work_id=1)["items"][0]
        self.assertIn("expired_or_missing_claim",item["drift"])
        self.assertIn("orphan_binding",item["drift"])
        self.assertEqual(item["status"],"claimed")
        self.assertFalse(item["ownership"]["executing"])

    def test_binding_and_claim_are_not_execution_proof(self):
        with closing(sqlite3.connect(self.db)) as c, c:
            c.execute("UPDATE claim SET expires_at='2026-09-24 10:00:00'")
        item = self.projection(work_id=1)["items"][0]
        self.assertTrue(item["ownership"]["matching_binding"])
        self.assertFalse(item["ownership"]["executing"])

    def test_done_requires_evidence_and_gate(self):
        item = self.projection(work_id=3)["items"][0]
        self.assertIn("done_without_artifact",item["drift"])
        self.assertIn("done_without_passing_latest_gate",item["drift"])
        with closing(sqlite3.connect(self.db)) as c, c:
            c.execute("INSERT INTO artifact VALUES(1,3,'review','abc')")
            c.execute("INSERT INTO gate_decision VALUES(1,3,'ACCEPTANCE','pass')")
        self.assertEqual(self.projection(work_id=3)["items"][0]["drift"],[])

    def test_cardinality_unicode_and_byte_bounds(self):
        with closing(sqlite3.connect(self.db)) as c, c:
            for i in range(4,35):
                c.execute("INSERT INTO work VALUES(?,'L0',?,'pending','2026-09-23')",(i,"界"*2000))
        data = self.projection()
        self.assertLessEqual(len(data["items"]),8)
        self.assertLessEqual(len(encode(data)),8192)
        self.assertEqual(len(data["items"])+data["omitted_count"],34)

    def test_delivered_hash_verifiable_after_byte_truncation(self):
        with closing(sqlite3.connect(self.db)) as c, c:
            for i in range(4,40):
                c.execute("INSERT INTO work VALUES(?,'L0',?,'pending','2026-09-23')",(i,"界"*120))
                for j in range(3):
                    c.execute("INSERT INTO artifact VALUES(?,?,?,?)",(i*10+j,i,"evidence"*100,"a"*64))
        result = self.projection()
        self.assertLess(len(result["items"]),8)
        actual = hashlib.sha256(encode({key:value for key,value in result.items() if key != "snapshot_sha256"})).hexdigest()
        self.assertEqual(result["snapshot_sha256"],actual)
        self.assertLessEqual(len(encode(result)),8192)
        self.assertEqual(len(result["items"])+result["omitted_count"],39)

    def test_unknown_role_work_and_missing_db_fail(self):
        for role,wid in [("impostor",None),("Rick",999),("Rick",-1),("Rick",True)]:
            with self.assertRaises(ValueError):
                self.projection(role,wid)
        missing=Path(self.tmp.name)/"missing.db"
        with self.assertRaises(sqlite3.Error):
            project(missing,"Rick")
        self.assertFalse(missing.exists())

if __name__ == "__main__":
    unittest.main()
