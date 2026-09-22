import os
import sqlite3
import tempfile
import unittest

class TestLifeCoreContracts(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test_uc.db")

        with open("10_Tech_OS/kernel/schema.sql", encoding="utf-8") as f:
            sql = f.read()

        self.conn = sqlite3.connect(self.db_path)
        self.conn.executescript(sql)
        self.conn.execute("PRAGMA foreign_keys = ON")

        self.conn.execute("INSERT INTO tape (id, path, sha256) VALUES (1, 't1', 'abc')")
        self.conn.execute("INSERT INTO work (id, tape_id, layer, title) VALUES (1, 1, 'L0', 'Kernel Task')")
        self.conn.execute("INSERT INTO work (id, tape_id, layer, title) VALUES (2, 1, 'L1', 'Life Task')")
        self.conn.commit()

    def tearDown(self):
        self.conn.close()
        self.tmp_dir.cleanup()

    def test_harness_capability_contracts(self):
        # Valid cases
        self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('Amy', 'Spec')")
        self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('Rory', 'Build')")
        self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('River', 'Spawn')")
        self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('River', 'Knowledge')")
        self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('Doctor11', 'Review')")
        self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('Doctor11', 'detach')")

        # Other identities are unaffected
        self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('Clara', 'Build')")

        # Invalid cases
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability: Amy can only be Spec"):
            self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('Amy', 'Build')")

        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_capability: Rory can only be Build"):
            self.conn.execute("INSERT INTO harness_capability (harness, capability) VALUES ('Rory', 'Spec')")

    def test_session_binding_contracts(self):
        # Valid cases
        self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (2, 's1', 'Amy', 'Spec')")
        self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (2, 's2', 'Rory', 'Build')")

        # Invalid capability bindings
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability: Amy can only bind as Spec"):
            self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (2, 's3', 'Amy', 'Build')")

        # Invalid layer (Sovereign Kernel limitation)
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability: Life Core companions cannot bind to L0 layer work items"):
            self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's4', 'Amy', 'Spec')")

        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability: Life Core companions cannot bind to L0 layer work items"):
            self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's5', 'Rory', 'Build')")

if __name__ == "__main__":
    unittest.main()
