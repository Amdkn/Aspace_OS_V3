import sqlite3
import unittest
import os
import tempfile
import sys
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

        # init schema
        cmd = [sys.executable, UC_PATH, "init"]
        subprocess.run(cmd, env=self.env, check=True)

        self.conn = sqlite3.connect(self.db_path)

    def tearDown(self):
        self.conn.close()
        self.tmp_dir.cleanup()

    def test_amy_spec_only(self):
        # Should pass
        self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('Amy', 'Spec')")
        # Should fail
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability"):
            self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('Amy', 'Build')")

    def test_rory_build_only(self):
        self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('Rory', 'Build')")
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability"):
            self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('Rory', 'Spec')")

    def test_river_spawn_knowledge(self):
        self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('River', 'Spawn')")
        self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('River', 'Knowledge')")
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability"):
            self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('River', 'Build')")

    def test_doctor11_review_detach(self):
        self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('Doctor11', 'Review')")
        self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('Doctor11', 'detach')")
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability"):
            self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('Doctor11', 'Spec')")

    def test_no_l0_binding(self):
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability"):
            self.conn.execute("INSERT INTO session_binding (harness, layer) VALUES ('Amy', 'L0')")

        # But L1 should pass
        self.conn.execute("INSERT INTO session_binding (harness, layer) VALUES ('Amy', 'L1')")
        self.conn.execute("INSERT INTO session_binding (harness, layer) VALUES ('Rory', 'L2')")

if __name__ == '__main__':
    unittest.main()
