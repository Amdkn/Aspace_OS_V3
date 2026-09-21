#!/usr/bin/env python3
"""test_life_core_contracts.py — Validation of Life Core L1 capability contracts.

Validates that:
- Amy operates strictly as Spec.
- Rory operates strictly as Build.
- River operates strictly as Spawn/Knowledge.
- Doctor11 operates strictly as Review/detach.
- None own sovereign Kernel state.
"""
import os
import sqlite3
import tempfile
import unittest
import subprocess
import sys

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

    def tearDown(self):
        self.tmp_dir.cleanup()

    def test_life_core_capabilities(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        bindings = [
            ("amy_social", "SPEC"),
            ("rory_health", "BUILD"),
            ("river_knowledge", "SPAWN"),
            ("doctor_11_life", "REVIEW")
        ]

        # Assert Amy operates strictly as Spec
        c.execute("SELECT capability FROM harness_capability WHERE harness='amy_social'")
        amy_caps = [r[0] for r in c.fetchall()]
        self.assertIn("SPEC", amy_caps)
        self.assertNotIn("REVIEW", amy_caps)
        self.assertNotIn("BUILD", amy_caps)

        # Assert Rory operates strictly as Build
        c.execute("SELECT capability FROM harness_capability WHERE harness='rory_health'")
        rory_caps = [r[0] for r in c.fetchall()]
        self.assertEqual(rory_caps, ["BUILD"])

        # Assert River operates strictly as Spawn
        c.execute("SELECT capability FROM harness_capability WHERE harness='river_knowledge'")
        river_caps = [r[0] for r in c.fetchall()]
        self.assertEqual(river_caps, ["SPAWN"])

        # Assert Doctor11 operates strictly as Review
        c.execute("SELECT capability FROM harness_capability WHERE harness='doctor_11_life'")
        doc_caps = [r[0] for r in c.fetchall()]
        self.assertEqual(doc_caps, ["REVIEW"])

        # Assert none own sovereign Kernel state
        for harness, cap in bindings:
            c.execute("SELECT capability FROM harness_capability WHERE harness=?", (harness,))
            caps = [r[0] for r in c.fetchall()]
            self.assertNotIn("L0_ADMIN", caps)
            self.assertNotIn("KERNEL_WRITE", caps)

        conn.close()

if __name__ == "__main__":
    unittest.main()
