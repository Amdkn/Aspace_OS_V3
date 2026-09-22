import os
import sys
import unittest
import sqlite3
import tempfile
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
UC_PATH = os.path.join(HERE, "uc.py")

class TestLifeCoreContracts(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test_uc.db")
        self.env = os.environ.copy()
        self.env["ASPACE_DB"] = self.db_path

        cmd = [sys.executable, UC_PATH, "init"]
        subprocess.run(cmd, env=self.env, check=True, capture_output=True)

        self.conn = sqlite3.connect(self.db_path)
        # Create some work items for testing
        self.conn.execute("INSERT INTO work (id, layer, title, status) VALUES (1, 'L1', 'L1 Work', 'pending')")
        self.conn.execute("INSERT INTO work (id, layer, title, status) VALUES (2, 'L0', 'L0 Work', 'pending')")
        self.conn.commit()

    def tearDown(self):
        self.conn.close()
        self.tmp_dir.cleanup()

    def test_amy_spec(self):
        # Valid capability
        self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's1', 'Amy', 'Spec')")
        # Invalid capability
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability"):
            self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's2', 'Amy', 'Build')")

    def test_rory_build(self):
        # Valid capability
        self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's1', 'Rory', 'Build')")
        # Invalid capability
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability"):
            self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's2', 'Rory', 'Spec')")

    def test_river_spawn_knowledge(self):
        # Valid capability Spawn
        self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's1', 'River', 'Spawn')")
        # Valid capability Knowledge
        self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's2', 'River', 'Knowledge')")
        # Invalid capability
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability"):
            self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's3', 'River', 'Spec')")

    def test_doctor11_review_detach(self):
        # Valid capability Review
        self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's1', 'Doctor11', 'Review')")
        # Valid capability detach
        self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's2', 'Doctor11', 'detach')")
        # Invalid capability
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability"):
            self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's3', 'Doctor11', 'Spec')")

    def test_companion_cannot_bind_l0(self):
        # Companion binds to L0 should fail
        for harness, capability in [('Amy', 'Spec'), ('Rory', 'Build'), ('River', 'Spawn'), ('Doctor11', 'Review')]:
            with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability"):
                self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (2, 's1', ?, ?)", (harness, capability))

        # Non-companion binding to L0 should succeed
        self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (2, 's1', 'Rick', 'GodMode')")

if __name__ == "__main__":
    unittest.main()
