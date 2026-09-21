import sqlite3
import unittest
import os
import tempfile
import sys
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
UC_PATH = os.path.join(HERE, "uc.py")

class TestLifeCoreContracts(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test_uc.db")
        self.env = os.environ.copy()
        self.env["ASPACE_DB"] = self.db_path

        cmd = [sys.executable, UC_PATH, "init"]
        subprocess.run(cmd, env=self.env, check=True, capture_output=True)

    def tearDown(self):
        self.tmp_dir.cleanup()

    def test_life_core_capability_contracts(self):
        conn = sqlite3.connect(self.db_path)
        # Create a work item in L1 (not L0)
        conn.execute("INSERT INTO work (id, layer, title) VALUES (1, 'L1', 'Test L1')")

        # Amy = Spec
        conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability, status) VALUES (1, 'k', 'Amy', 'Spec', 'active')")
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability"):
            conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability, status) VALUES (1, 'k', 'Amy', 'Build', 'active')")

        # Rory = Build
        conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability, status) VALUES (1, 'k', 'Rory', 'Build', 'active')")
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability"):
            conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability, status) VALUES (1, 'k', 'Rory', 'Spec', 'active')")

        # River = Spawn/Knowledge
        conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability, status) VALUES (1, 'k', 'River', 'Spawn', 'active')")
        conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability, status) VALUES (1, 'k', 'River', 'Knowledge', 'active')")
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability"):
            conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability, status) VALUES (1, 'k', 'River', 'Build', 'active')")

        # Doctor11 = Review/detach
        conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability, status) VALUES (1, 'k', 'Doctor11', 'Review', 'active')")
        conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability, status) VALUES (1, 'k', 'Doctor11', 'detach', 'active')")
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability"):
            conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability, status) VALUES (1, 'k', 'Doctor11', 'Spec', 'active')")

        conn.close()

    def test_life_core_binding_capability_l0_restriction(self):
        conn = sqlite3.connect(self.db_path)
        # Create a work item in L0
        conn.execute("INSERT INTO work (id, layer, title) VALUES (2, 'L0', 'Test L0')")

        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability"):
            conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability, status) VALUES (2, 'k', 'Amy', 'Spec', 'active')")

        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability"):
            conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability, status) VALUES (2, 'k', 'Rory', 'Build', 'active')")

        # Another harness can bind to L0
        conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability, status) VALUES (2, 'k', 'Rick', 'Spec', 'active')")

        conn.close()

if __name__ == "__main__":
    unittest.main()
