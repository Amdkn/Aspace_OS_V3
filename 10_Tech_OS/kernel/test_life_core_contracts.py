#!/usr/bin/env python3
"""test_life_core_contracts.py — Suite de tests unitaires pour les contrats Life Core.

Valide la logique de restriction des contrats de capacite par role pour Amy, Rory, River et Doctor11.
Valide egalement l'interdiction de liaison (binding) au layer 'L0' pour les compagnons.
"""
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

        cmd = [sys.executable, UC_PATH, "init"]
        subprocess.run(cmd, env=self.env, check=True, capture_output=True)

        self.conn = sqlite3.connect(self.db_path)
        self.conn.execute("PRAGMA foreign_keys = ON")

        # Insert sample work items to bind to
        self.conn.execute("INSERT INTO work(id, layer, title, status) VALUES (1, 'L0', 'Kernel Root Task', 'pending')")
        self.conn.execute("INSERT INTO work(id, layer, title, status) VALUES (2, 'L1', 'Some L1 Task', 'pending')")
        self.conn.execute("INSERT INTO work(id, layer, title, status) VALUES (3, 'L2', 'Some L2 Task', 'pending')")
        self.conn.commit()

    def tearDown(self):
        self.conn.close()
        self.tmp_dir.cleanup()

    def assertBindingFails(self, work_id, harness, capability, expected_error):
        with self.assertRaisesRegex(sqlite3.IntegrityError, expected_error):
            self.conn.execute(
                "INSERT INTO session_binding (work_id, session_key, harness, capability, status) VALUES (?, 'sess-123', ?, ?, 'active')",
                (work_id, harness, capability)
            )

    def assertBindingSucceeds(self, work_id, harness, capability):
        cur = self.conn.execute(
            "INSERT INTO session_binding (work_id, session_key, harness, capability, status) VALUES (?, 'sess-123', ?, ?, 'active')",
            (work_id, harness, capability)
        )
        self.assertEqual(cur.rowcount, 1)

    def test_amy_spec_contract(self):
        # Amy MUST be Spec
        self.assertBindingSucceeds(2, 'Amy', 'Spec')
        self.assertBindingFails(2, 'Amy', 'Build', 'Amy is restricted to Spec')
        self.assertBindingFails(2, 'Amy', 'Review', 'Amy is restricted to Spec')

    def test_rory_build_contract(self):
        # Rory MUST be Build
        self.assertBindingSucceeds(2, 'Rory', 'Build')
        self.assertBindingFails(2, 'Rory', 'Spec', 'Rory is restricted to Build')
        self.assertBindingFails(2, 'Rory', 'Review', 'Rory is restricted to Build')

    def test_river_spawn_knowledge_contract(self):
        # River MUST be Spawn or Knowledge
        self.assertBindingSucceeds(2, 'River', 'Spawn')
        self.assertBindingSucceeds(3, 'River', 'Knowledge')
        self.assertBindingFails(2, 'River', 'Build', 'River is restricted to Spawn or Knowledge')
        self.assertBindingFails(2, 'River', 'Review', 'River is restricted to Spawn or Knowledge')

    def test_doctor11_review_detach_contract(self):
        # Doctor11 MUST be Review or detach
        self.assertBindingSucceeds(2, 'Doctor11', 'Review')
        self.assertBindingSucceeds(3, 'Doctor11', 'detach')
        self.assertBindingFails(2, 'Doctor11', 'Spec', 'Doctor11 is restricted to Review or detach')
        self.assertBindingFails(2, 'Doctor11', 'Build', 'Doctor11 is restricted to Review or detach')

    def test_l0_layer_restriction(self):
        # Companions cannot bind to L0
        self.assertBindingFails(1, 'Amy', 'Spec', 'Companions cannot bind to L0 layer')
        self.assertBindingFails(1, 'Rory', 'Build', 'Companions cannot bind to L0 layer')
        self.assertBindingFails(1, 'River', 'Spawn', 'Companions cannot bind to L0 layer')

        # Doctor11 CAN bind to L0 (exempted companion/manager)
        self.assertBindingSucceeds(1, 'Doctor11', 'Review')

    def test_other_harnesses_unrestricted(self):
        # Other harnesses shouldn't be affected by this specific trigger
        self.assertBindingSucceeds(1, 'Rick', 'Root')
        self.assertBindingSucceeds(2, 'Clara', 'Spec')

if __name__ == '__main__':
    unittest.main()
