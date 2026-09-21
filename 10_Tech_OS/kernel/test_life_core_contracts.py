import json
import os
import sqlite3
import tempfile
import unittest
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
UC_PATH = os.path.join(HERE, "uc.py")

class TestLifeCoreContracts(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test_uc.db")
        self.env = os.environ.copy()
        self.env["ASPACE_DB"] = self.db_path

        # Init DB
        cmd = [sys.executable, UC_PATH, "init"]
        subprocess.run(cmd, env=self.env, check=True, capture_output=True)

        self.conn = sqlite3.connect(self.db_path)
        # Create some work items
        self.conn.execute("INSERT INTO work (id, layer, title, status) VALUES (1, 'L0', 'Kernel Work', 'pending')")
        self.conn.execute("INSERT INTO work (id, layer, title, status) VALUES (2, 'L1', 'Life Work', 'pending')")
        self.conn.commit()

    def tearDown(self):
        self.conn.close()
        self.tmp_dir.cleanup()

    def test_loi_life_core_capability(self):
        # Valid capability
        self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES (2, 'key1', 'Amy', 'Spec', 'active')")
        self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES (2, 'key2', 'Rory', 'Build', 'active')")
        self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES (2, 'key3', 'River', 'Spawn', 'active')")
        self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES (2, 'key4', 'River', 'Knowledge', 'active')")
        self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES (2, 'key5', 'Doctor11', 'Review', 'active')")
        self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES (2, 'key6', 'Doctor11', 'detach', 'active')")

        # Invalid capability
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability"):
            self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES (2, 'key7', 'Amy', 'Build', 'active')")

    def test_loi_life_core_binding_capability_l0(self):
        # Companions cannot bind to L0
        for comp in ['Amy', 'Rory', 'River']:
            with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability"):
                self.conn.execute(f"INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES (1, 'k', '{comp}', 'Spec', 'active')")

        # Doctor11 can bind to L0
        self.conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability, status) VALUES (1, 'k-doc', 'Doctor11', 'Review', 'active')")

if __name__ == "__main__":
    unittest.main()
