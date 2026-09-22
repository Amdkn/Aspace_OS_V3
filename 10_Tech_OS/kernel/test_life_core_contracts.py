import unittest
import sqlite3
import os
import tempfile

class TestLifeCoreContracts(unittest.TestCase):
    def setUp(self):
        self.fd, self.db_path = tempfile.mkstemp(suffix=".db")
        os.close(self.fd)

        self.conn = sqlite3.connect(self.db_path)
        self.conn.execute("PRAGMA foreign_keys = ON;")

        with open("10_Tech_OS/kernel/schema.sql", "r") as f:
            self.conn.executescript(f.read())

        self.conn.execute("INSERT INTO tape (path, sha256) VALUES ('dummy_tape', '123')")
        self.conn.execute("INSERT INTO work (id, tape_id, layer, title, status) VALUES (1, 1, 'L0', 'Kernel Work', 'pending')")
        self.conn.execute("INSERT INTO work (id, tape_id, layer, title, status) VALUES (2, 1, 'L1', 'Life Work', 'pending')")

    def tearDown(self):
        self.conn.close()
        os.remove(self.db_path)

    def test_harness_capability_amy(self):
        # Should allow Spec
        self.conn.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('Amy', 'Spec', 'HIGH', 'active')")

        # Should reject Build
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability"):
            self.conn.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('Amy', 'Build', 'HIGH', 'active')")

    def test_harness_capability_rory(self):
        self.conn.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('Rory', 'Build', 'HIGH', 'active')")
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability"):
            self.conn.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('Rory', 'Spec', 'HIGH', 'active')")

    def test_harness_capability_river(self):
        self.conn.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('River', 'Spawn', 'HIGH', 'active')")
        self.conn.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('River', 'Knowledge', 'HIGH', 'active')")
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability"):
            self.conn.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('River', 'Build', 'HIGH', 'active')")

    def test_harness_capability_doctor11(self):
        self.conn.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('Doctor11', 'Review', 'HIGH', 'active')")
        self.conn.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('Doctor11', 'detach', 'HIGH', 'active')")
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability"):
            self.conn.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES ('Doctor11', 'Build', 'HIGH', 'active')")

    def test_l0_binding_restriction(self):
        # Cannot bind to L0
        for companion in ['Amy', 'Rory', 'River', 'Doctor11']:
            with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability"):
                self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES (1, 'key1', ?, 'Spec', 'active')", (companion,))

        # Can bind to L1
        self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES (2, 'key2', 'Amy', 'Spec', 'active')")

if __name__ == '__main__':
    unittest.main()
