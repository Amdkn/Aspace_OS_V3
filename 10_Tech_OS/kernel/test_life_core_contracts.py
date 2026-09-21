import os
import sqlite3
import tempfile
import unittest

class TestLifeCoreContracts(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test.db")
        self.conn = sqlite3.connect(self.db_path)
        self.c = self.conn.cursor()
        with open("10_Tech_OS/kernel/schema.sql", "r") as f:
            self.c.executescript(f.read())

        # Add a tape and work for testing
        self.c.execute("INSERT INTO tape(path, sha256) VALUES('dummy.txt', '123')")
        self.tape_id = self.c.lastrowid
        self.c.execute("INSERT INTO work(tape_id, layer, title) VALUES(?, 'L1', 'Test Work')", (self.tape_id,))
        self.work_l1 = self.c.lastrowid
        self.c.execute("INSERT INTO work(tape_id, layer, title) VALUES(?, 'L0', 'Kernel Work')", (self.tape_id,))
        self.work_l0 = self.c.lastrowid

    def tearDown(self):
        self.conn.close()
        self.tmp_dir.cleanup()

    def test_amy_spec(self):
        self.c.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(?, 's1', 'Amy', 'Spec', 'active')", (self.work_l1,))
        self.assertEqual(self.c.rowcount, 1)

    def test_amy_build_fails(self):
        with self.assertRaises(sqlite3.IntegrityError) as context:
            self.c.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(?, 's2', 'Amy', 'Build', 'active')", (self.work_l1,))
        self.assertIn("loi_life_core_binding_capability", str(context.exception))

    def test_l0_restriction(self):
        with self.assertRaises(sqlite3.IntegrityError) as context:
            self.c.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(?, 's3', 'Amy', 'Spec', 'active')", (self.work_l0,))
        self.assertIn("loi_life_core_binding_capability", str(context.exception))

    def test_river_spawn_knowledge(self):
        self.c.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(?, 's4', 'River', 'Spawn', 'active')", (self.work_l1,))
        self.c.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(?, 's5', 'River', 'Knowledge', 'active')", (self.work_l1,))
        self.c.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(?, 's6', 'River', 'Spawn/Knowledge', 'active')", (self.work_l1,))

    def test_river_build_fails(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.c.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(?, 's7', 'River', 'Build', 'active')", (self.work_l1,))

    def test_doctor11_review_detach(self):
        self.c.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(?, 's8', 'Doctor11', 'Review', 'active')", (self.work_l1,))
        self.c.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(?, 's9', 'Doctor11', 'detach', 'active')", (self.work_l1,))
        self.c.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(?, 's10', 'Doctor11', 'Review/detach', 'active')", (self.work_l1,))

    def test_rory_build(self):
        self.c.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(?, 's11', 'Rory', 'Build', 'active')", (self.work_l1,))

    def test_harness_capability_amy(self):
        self.c.execute("INSERT INTO harness_capability(harness, capability) VALUES('Amy', 'Spec')")
        with self.assertRaises(sqlite3.IntegrityError):
            self.c.execute("INSERT INTO harness_capability(harness, capability) VALUES('Amy', 'Build')")

if __name__ == '__main__':
    unittest.main()
