import sqlite3
import unittest
import os
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCHEMA_PATH = HERE / "schema.sql"

class TestLifeCoreContracts(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test_uc.db")
        self.conn = sqlite3.connect(self.db_path)
        self.conn.execute("PRAGMA foreign_keys = ON;")

        with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
            schema_sql = f.read()
        self.conn.executescript(schema_sql)

        # Setup dummy works
        self.conn.execute("INSERT INTO tape (id, path, sha256) VALUES (1, 't1', 'abc')")
        self.conn.execute("INSERT INTO tape (id, path, sha256) VALUES (2, 't2', 'def')")
        self.conn.execute("INSERT INTO work (id, tape_id, layer, title, status) VALUES (1, 1, 'L1', 'task1', 'pending')")
        self.conn.execute("INSERT INTO work (id, tape_id, layer, title, status) VALUES (2, 2, 'L0', 'task2', 'pending')")
        self.conn.commit()

    def tearDown(self):
        self.conn.close()
        self.tmp_dir.cleanup()

    def test_amy_spec(self):
        # Amy can do Spec on L1
        self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's1', 'Amy', 'Spec')")

        # Amy cannot do Build
        with self.assertRaises(sqlite3.IntegrityError) as ctx:
            self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's2', 'Amy', 'Build')")
        self.assertIn("loi_life_core_binding_capability: Amy is restricted to Spec capability", str(ctx.exception))

        # Amy cannot bind to L0
        with self.assertRaises(sqlite3.IntegrityError) as ctx:
            self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (2, 's3', 'Amy', 'Spec')")
        self.assertIn("loi_life_core_binding_capability: Companions cannot bind to L0 sovereign state", str(ctx.exception))

    def test_rory_build(self):
        # Rory can do Build on L1
        self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's4', 'Rory', 'Build')")

        # Rory cannot do Spec
        with self.assertRaises(sqlite3.IntegrityError) as ctx:
            self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's5', 'Rory', 'Spec')")
        self.assertIn("loi_life_core_binding_capability: Rory is restricted to Build capability", str(ctx.exception))

        # Rory cannot bind to L0
        with self.assertRaises(sqlite3.IntegrityError) as ctx:
            self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (2, 's6', 'Rory', 'Build')")
        self.assertIn("loi_life_core_binding_capability: Companions cannot bind to L0 sovereign state", str(ctx.exception))

    def test_river_spawn_knowledge(self):
        # River can do Spawn and Knowledge on L1
        self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's7', 'River', 'Spawn')")
        self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's8', 'River', 'Knowledge')")

        # River cannot do Spec
        with self.assertRaises(sqlite3.IntegrityError) as ctx:
            self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's9', 'River', 'Spec')")
        self.assertIn("loi_life_core_binding_capability: River is restricted to Spawn/Knowledge capabilities", str(ctx.exception))

        # River cannot bind to L0
        with self.assertRaises(sqlite3.IntegrityError) as ctx:
            self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (2, 's10', 'River', 'Spawn')")
        self.assertIn("loi_life_core_binding_capability: Companions cannot bind to L0 sovereign state", str(ctx.exception))

    def test_doctor11_review_detach(self):
        # Doctor11 can do Review and detach on L1 and L0
        self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's11', 'Doctor11', 'Review')")
        self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's12', 'Doctor11', 'detach')")
        self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (2, 's13', 'Doctor11', 'Review')")
        self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (2, 's14', 'Doctor11', 'detach')")

        # Doctor11 cannot do Spec
        with self.assertRaises(sqlite3.IntegrityError) as ctx:
            self.conn.execute("INSERT INTO session_binding (work_id, session_key, harness, capability) VALUES (1, 's15', 'Doctor11', 'Spec')")
        self.assertIn("loi_life_core_binding_capability: Doctor11 is restricted to Review/detach capabilities", str(ctx.exception))

if __name__ == "__main__":
    unittest.main()
