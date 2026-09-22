import unittest
import sqlite3

class TestLifeCoreContracts(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(":memory:")
        self.db.execute("PRAGMA foreign_keys = ON")
        with open("10_Tech_OS/kernel/schema.sql") as f:
            self.db.executescript(f.read())


        # Insert a tape
        self.db.execute("INSERT INTO tape (id, path, sha256) VALUES (1, 'path/to/tape', 'sha256')")
        # Insert a L1 work
        self.db.execute("INSERT INTO work (id, tape_id, layer, title) VALUES (1, 1, 'L1', 'L1 Work')")
        # Insert a L0 work
        self.db.execute("INSERT INTO work (id, tape_id, layer, title) VALUES (2, 1, 'L0', 'L0 Work')")

    def tearDown(self):
        self.db.close()

    def test_amy_spec(self):
        # Should succeed
        self.db.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 'sess1', 'Amy', 'Spec')")

        # Should fail
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability: Amy is restricted to Spec"):
            self.db.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 'sess2', 'Amy', 'Build')")

    def test_rory_build(self):
        # Should succeed
        self.db.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 'sess1', 'Rory', 'Build')")

        # Should fail
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability: Rory is restricted to Build"):
            self.db.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 'sess2', 'Rory', 'Spec')")

    def test_river_spawn_knowledge(self):
        # Should succeed
        self.db.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 'sess1', 'River', 'Spawn')")
        self.db.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 'sess2', 'River', 'Knowledge')")

        # Should fail
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability: River is restricted to Spawn/Knowledge"):
            self.db.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 'sess3', 'River', 'Build')")

    def test_doctor11_review_detach(self):
        # Should succeed
        self.db.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 'sess1', 'Doctor11', 'Review')")
        self.db.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 'sess2', 'Doctor11', 'detach')")

        # Should fail
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability: Doctor11 is restricted to Review/detach"):
            self.db.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 'sess3', 'Doctor11', 'Spec')")

    def test_l0_sovereign_state(self):
        # Should succeed for Doctor11
        self.db.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (2, 'sess1', 'Doctor11', 'Review')")

        # Should fail for others
        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability: Companions cannot bind to L0 sovereign state"):
            self.db.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (2, 'sess2', 'Amy', 'Spec')")

        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability: Companions cannot bind to L0 sovereign state"):
            self.db.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (2, 'sess3', 'Rory', 'Build')")

        with self.assertRaisesRegex(sqlite3.IntegrityError, "loi_life_core_binding_capability: Companions cannot bind to L0 sovereign state"):
            self.db.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (2, 'sess4', 'River', 'Spawn')")

if __name__ == "__main__":
    unittest.main()
