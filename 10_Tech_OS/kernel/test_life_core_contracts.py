import unittest
import sqlite3
import os

class TestLifeCoreContracts(unittest.TestCase):
    def setUp(self):
        self.db_path = ":memory:"
        self.conn = sqlite3.connect(self.db_path)
        with open("10_Tech_OS/kernel/schema.sql", "r") as f:
            self.conn.executescript(f.read())

    def tearDown(self):
        self.conn.close()

    def test_amy_capability_allowed(self):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('Amy', 'Spec', 'CANARY', 'pass')")
        self.assertEqual(cur.rowcount, 1)

    def test_amy_capability_denied(self):
        cur = self.conn.cursor()
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability: Amy is restricted to Spec"):
            cur.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('Amy', 'Build', 'CANARY', 'pass')")

    def test_rory_capability_allowed(self):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('Rory', 'Build', 'CANARY', 'pass')")
        self.assertEqual(cur.rowcount, 1)

    def test_rory_capability_denied(self):
        cur = self.conn.cursor()
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability: Rory is restricted to Build"):
            cur.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('Rory', 'Spec', 'CANARY', 'pass')")

    def test_river_capability_allowed(self):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('River', 'Spawn', 'CANARY', 'pass')")
        cur.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('River', 'Knowledge', 'CANARY', 'pass')")

    def test_river_capability_denied(self):
        cur = self.conn.cursor()
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability: River is restricted to Spawn/Knowledge"):
            cur.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('River', 'Build', 'CANARY', 'pass')")

    def test_doctor11_capability_allowed(self):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('Doctor11', 'Review', 'CANARY', 'pass')")
        cur.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('Doctor11', 'detach', 'CANARY', 'pass')")

    def test_doctor11_capability_denied(self):
        cur = self.conn.cursor()
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability: Doctor11 is restricted to Review/detach"):
            cur.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('Doctor11', 'Build', 'CANARY', 'pass')")

    def test_companion_binding_denied_l0(self):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO tape (path, sha256) VALUES ('dummy/path', 'dummy_hash')")
        cur.execute("INSERT INTO work (id, layer, title) VALUES (1, 'L0', 'Test L0 Work')")
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability: Companions cannot bind to L0 layer"):
            cur.execute("INSERT INTO session_binding (work_id, session_key, harness, status) VALUES (1, 'sess123', 'Amy', 'active')")

    def test_companion_binding_allowed_l1(self):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO tape (path, sha256) VALUES ('dummy/path', 'dummy_hash')")
        cur.execute("INSERT INTO work (id, layer, title) VALUES (1, 'L1', 'Test L1 Work')")
        cur.execute("INSERT INTO session_binding (work_id, session_key, harness, status) VALUES (1, 'sess123', 'Amy', 'active')")
        self.assertEqual(cur.rowcount, 1)

if __name__ == '__main__':
    unittest.main()
