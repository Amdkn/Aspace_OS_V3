#!/usr/bin/env python3
"""test_life_core_contracts.py — Unit tests for Life Core capability contracts.

Validates the enforcement of specific capability bindings via the
loi_life_core_binding_capability SQLite trigger. Tests constraints for
Amy, Rory, River, and Doctor11, as well as Sovereign L0 limits.
"""
import os
import sqlite3
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA_PATH = os.path.join(HERE, "schema.sql")


class TestLifeCoreContracts(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test_uc.db")

        self.conn = sqlite3.connect(self.db_path)
        with open(SCHEMA_PATH, encoding="utf-8") as f:
            self.conn.executescript(f.read())

        self._insert_harness_capabilities()

    def tearDown(self):
        self.conn.close()
        self.tmp_dir.cleanup()

    def _insert_harness_capabilities(self):
        caps = [
            ("h_spec", "Spec"),
            ("h_build", "Build"),
            ("h_spawn", "Spawn"),
            ("h_knowledge", "Knowledge"),
            ("h_review", "Review"),
            ("h_detach", "detach"),
            ("h_other", "Other")
        ]
        self.conn.executemany("INSERT INTO harness_capability (harness, cap_name) VALUES (?, ?)", caps)
        self.conn.commit()

    def test_amy_spec_contract(self):
        # Valid: Amy with Spec capability
        self.conn.execute("INSERT INTO session_binding (companion, layer, harness) VALUES ('Amy', 'L1', 'h_spec')")

        # Invalid: Amy with non-Spec capability
        with self.assertRaisesRegex(sqlite3.IntegrityError, "Amy is restricted to Spec"):
            self.conn.execute("INSERT INTO session_binding (companion, layer, harness) VALUES ('Amy', 'L1', 'h_build')")

    def test_rory_build_contract(self):
        # Valid: Rory with Build capability
        self.conn.execute("INSERT INTO session_binding (companion, layer, harness) VALUES ('Rory', 'L1', 'h_build')")

        # Invalid: Rory with non-Build capability
        with self.assertRaisesRegex(sqlite3.IntegrityError, "Rory is restricted to Build"):
            self.conn.execute("INSERT INTO session_binding (companion, layer, harness) VALUES ('Rory', 'L1', 'h_spec')")

    def test_river_spawn_knowledge_contract(self):
        # Valid: River with Spawn capability
        self.conn.execute("INSERT INTO session_binding (companion, layer, harness) VALUES ('River', 'L1', 'h_spawn')")

        # Valid: River with Knowledge capability
        self.conn.execute("INSERT INTO session_binding (companion, layer, harness) VALUES ('River', 'L1', 'h_knowledge')")

        # Invalid: River with non-Spawn/Knowledge capability
        with self.assertRaisesRegex(sqlite3.IntegrityError, "River is restricted to Spawn/Knowledge"):
            self.conn.execute("INSERT INTO session_binding (companion, layer, harness) VALUES ('River', 'L1', 'h_build')")

    def test_doctor11_review_detach_contract(self):
        # Valid: Doctor11 with Review capability
        self.conn.execute("INSERT INTO session_binding (companion, layer, harness) VALUES ('Doctor11', 'L1', 'h_review')")

        # Valid: Doctor11 with detach capability
        self.conn.execute("INSERT INTO session_binding (companion, layer, harness) VALUES ('Doctor11', 'L1', 'h_detach')")

        # Invalid: Doctor11 with non-Review/detach capability
        with self.assertRaisesRegex(sqlite3.IntegrityError, "Doctor11 is restricted to Review/detach"):
            self.conn.execute("INSERT INTO session_binding (companion, layer, harness) VALUES ('Doctor11', 'L1', 'h_build')")

    def test_l0_sovereign_kernel_limitation(self):
        # Valid: Doctor11 binding to L0
        self.conn.execute("INSERT INTO session_binding (companion, layer, harness) VALUES ('Doctor11', 'L0', 'h_review')")

        # Invalid: Anyone else binding to L0 (e.g. Amy)
        with self.assertRaisesRegex(sqlite3.IntegrityError, "Only Doctor11 can bind to L0"):
            self.conn.execute("INSERT INTO session_binding (companion, layer, harness) VALUES ('Amy', 'L0', 'h_spec')")


if __name__ == "__main__":
    unittest.main()
