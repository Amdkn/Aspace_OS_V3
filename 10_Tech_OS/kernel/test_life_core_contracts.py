import unittest, os, json, sqlite3, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
UC_PATH = os.path.join(HERE, "uc.py")

class TestLifeCoreContracts(unittest.TestCase):
    def setUp(self):
        # Use a unique DB for each test to avoid locking
        self.tmp_db = os.path.join(HERE, f"test_uc_contracts_{self.id().split('.')[-1]}.db")
        self.env = os.environ.copy()
        self.env["ASPACE_DB"] = self.tmp_db
        if os.path.exists(self.tmp_db):
            os.remove(self.tmp_db)
        subprocess.run([sys.executable, UC_PATH, "init"], env=self.env, check=True, capture_output=True)

    def tearDown(self):
        if os.path.exists(self.tmp_db):
            os.remove(self.tmp_db)

    def test_harness_capability_contracts(self):
        conn = sqlite3.connect(self.tmp_db)
        # Should pass
        conn.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES('amy', 'Spec', 'NATIVE', 'pass')")
        conn.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES('rory', 'Build', 'NATIVE', 'pass')")
        conn.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES('river', 'Spawn', 'NATIVE', 'pass')")
        conn.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES('river', 'Knowledge', 'NATIVE', 'pass')")
        conn.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES('doctor11', 'Review', 'NATIVE', 'pass')")
        conn.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES('doctor11', 'detach', 'NATIVE', 'pass')")

        # Should fail
        with self.assertRaises(sqlite3.IntegrityError) as context:
            conn.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES('amy', 'Build', 'NATIVE', 'pass')")
        self.assertIn("Contract violation", str(context.exception))

        with self.assertRaises(sqlite3.IntegrityError):
            conn.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES('rory', 'Review', 'NATIVE', 'pass')")

        with self.assertRaises(sqlite3.IntegrityError):
            conn.execute("INSERT INTO harness_capability(harness, capability, evidence_level, status) VALUES('river', 'Spec', 'NATIVE', 'pass')")
        conn.close()

    def test_session_binding_contracts(self):
        conn = sqlite3.connect(self.tmp_db)
        conn.execute("INSERT INTO work(layer, title) VALUES('L1', 'test L1')")
        work_id_l1 = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

        conn.execute("INSERT INTO work(layer, title) VALUES('L0', 'test L0')")
        work_id_l0 = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

        # Valid bindings
        conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability) VALUES(?, 's1', 'amy', 'Spec')", (work_id_l1,))
        conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability) VALUES(?, 's2', 'rory', 'Build')", (work_id_l1,))

        # Invalid capability bindings
        with self.assertRaises(sqlite3.IntegrityError):
            conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability) VALUES(?, 's3', 'amy', 'Build')", (work_id_l1,))

        # Kernel sovereignty violation
        with self.assertRaises(sqlite3.IntegrityError) as context:
            conn.execute("INSERT INTO session_binding(work_id, session_key, harness, capability) VALUES(?, 's4', 'amy', 'Spec')", (work_id_l0,))
        self.assertIn("Kernel state", str(context.exception))
        conn.close()

if __name__ == '__main__':
    unittest.main()
