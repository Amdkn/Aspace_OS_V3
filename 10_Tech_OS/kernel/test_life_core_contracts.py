import sqlite3
import unittest
import tempfile
import os

class TestLifeCoreContracts(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test.db")
        self.conn = sqlite3.connect(self.db_path)
        with open("10_Tech_OS/kernel/schema.sql", "r") as f:
            self.conn.executescript(f.read())

        self.conn.execute("INSERT INTO work(id, layer, title, status) VALUES(1, 'L0', 'Kernel Work', 'pending')")
        self.conn.execute("INSERT INTO work(id, layer, title, status) VALUES(2, 'L1', 'Life Work', 'pending')")
        self.conn.commit()

    def tearDown(self):
        self.conn.close()
        self.tmp_dir.cleanup()

    def test_amy_spec(self):
        # Amy can do Spec on L1
        self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(2, 'sk', 'Amy', 'Spec', 'active')")

        # Amy cannot do Build
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability"):
            self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(2, 'sk', 'Amy', 'Build', 'active')")

        # Amy cannot work on L0
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability"):
            self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(1, 'sk', 'Amy', 'Spec', 'active')")

    def test_rory_build(self):
        # Rory can do Build on L1
        self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(2, 'sk', 'Rory', 'Build', 'active')")

        # Rory cannot do Spec
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability"):
            self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(2, 'sk', 'Rory', 'Spec', 'active')")

        # Rory cannot work on L0
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability"):
            self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(1, 'sk', 'Rory', 'Build', 'active')")

    def test_river_spawn_knowledge(self):
        # River can do Spawn and Knowledge on L1
        self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(2, 'sk1', 'River', 'Spawn', 'active')")
        self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(2, 'sk2', 'River', 'Knowledge', 'active')")

        # River cannot do Build
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability"):
            self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(2, 'sk', 'River', 'Build', 'active')")

        # River cannot work on L0
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability"):
            self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(1, 'sk', 'River', 'Spawn', 'active')")

    def test_doctor11_review_detach(self):
        # Doctor11 can do Review and detach on L0 and L1
        self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(1, 'sk1', 'Doctor11', 'Review', 'active')")
        self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(1, 'sk2', 'Doctor11', 'detach', 'active')")
        self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(2, 'sk3', 'Doctor11', 'Review', 'active')")

        # Doctor11 cannot do Spec
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability"):
            self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES(1, 'sk', 'Doctor11', 'Spec', 'active')")

if __name__ == '__main__':
    unittest.main()
