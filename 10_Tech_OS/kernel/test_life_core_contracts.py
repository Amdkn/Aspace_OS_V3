import sqlite3
import tempfile
import unittest
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

class TestLifeCoreContracts(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test_contracts.db")
        self.conn = sqlite3.connect(self.db_path)
        self.conn.execute("PRAGMA foreign_keys = ON")

        schema_path = os.path.join(HERE, "schema.sql")
        with open(schema_path, "r", encoding="utf-8") as f:
            self.conn.executescript(f.read())

        # Create some test work items
        self.conn.execute("INSERT INTO work (id, layer, title, status) VALUES (1, 'L0', 'Kernel Task', 'pending')")
        self.conn.execute("INSERT INTO work (id, layer, title, status) VALUES (2, 'L1', 'Life Task', 'pending')")
        self.conn.commit()

    def tearDown(self):
        self.conn.close()
        self.tmp_dir.cleanup()

    def test_amy_capability(self):
        # Spec is allowed
        self.conn.execute("INSERT INTO harness_capability (harness, capability, evidence_level, status) VALUES ('Amy', 'Spec', 'CANARY', 'pass')")
        # Build is forbidden
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability: Amy is strictly Spec"):
            self.conn.execute("INSERT INTO harness_capability (harness, capability, evidence_level, status) VALUES ('Amy', 'Build', 'CANARY', 'pass')")

    def test_rory_capability(self):
        # Build is allowed
        self.conn.execute("INSERT INTO harness_capability (harness, capability, evidence_level, status) VALUES ('Rory', 'Build', 'CANARY', 'pass')")
        # Spec is forbidden
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability: Rory is strictly Build"):
            self.conn.execute("INSERT INTO harness_capability (harness, capability, evidence_level, status) VALUES ('Rory', 'Spec', 'CANARY', 'pass')")

    def test_river_capability(self):
        # Spawn is allowed
        self.conn.execute("INSERT INTO harness_capability (harness, capability, evidence_level, status) VALUES ('River', 'Spawn', 'CANARY', 'pass')")
        # Knowledge is allowed
        self.conn.execute("INSERT INTO harness_capability (harness, capability, evidence_level, status) VALUES ('River', 'Knowledge', 'CANARY', 'pass')")
        # Spec is forbidden
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability: River is strictly Spawn/Knowledge"):
            self.conn.execute("INSERT INTO harness_capability (harness, capability, evidence_level, status) VALUES ('River', 'Spec', 'CANARY', 'pass')")

    def test_doctor11_capability(self):
        # Review is allowed
        self.conn.execute("INSERT INTO harness_capability (harness, capability, evidence_level, status) VALUES ('Doctor11', 'Review', 'CANARY', 'pass')")
        # detach is allowed
        self.conn.execute("INSERT INTO harness_capability (harness, capability, evidence_level, status) VALUES ('Doctor11', 'detach', 'CANARY', 'pass')")
        # Spec is forbidden
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability: Doctor11 is strictly Review/detach"):
            self.conn.execute("INSERT INTO harness_capability (harness, capability, evidence_level, status) VALUES ('Doctor11', 'Spec', 'CANARY', 'pass')")

    def test_sovereign_l0_binding(self):
        # Companions cannot bind to L0
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability: Companions cannot own sovereign Kernel state \\(L0\\)"):
            self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's1', 'Amy', 'Spec')")

        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability: Companions cannot own sovereign Kernel state \\(L0\\)"):
            self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's2', 'Rory', 'Build')")

        # But they can bind to L1
        self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (2, 's3', 'Amy', 'Spec')")
        self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (2, 's4', 'Rory', 'Build')")

    def test_binding_capabilities(self):
        # Correct capabilities on L1 are allowed
        self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (2, 's1', 'Amy', 'Spec')")
        self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (2, 's2', 'River', 'Knowledge')")

        # Incorrect capabilities block binding
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability: Amy must bind as Spec"):
            self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (2, 's3', 'Amy', 'Build')")

        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability: Doctor11 must bind as Review/detach"):
            self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (2, 's4', 'Doctor11', 'Spec')")

if __name__ == '__main__':
    unittest.main()
