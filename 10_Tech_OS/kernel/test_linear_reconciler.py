#!/usr/bin/env python3
import json
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
RECONCILER_PATH = os.path.join(HERE, "linear_reconciler.py")

class TestLinearReconciler(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test_uc.db")
        self.env = os.environ.copy()
        self.env["ASPACE_DB"] = self.db_path

        cmd = [sys.executable, UC_PATH, "init"]
        subprocess.run(cmd, env=self.env, check=True, capture_output=True)

    def tearDown(self):
        self.tmp_dir.cleanup()

    def add_work(self, layer, title, status, harness=None):
        conn = sqlite3.connect(self.db_path)
        cur = conn.execute("INSERT INTO work (layer, title, status) VALUES (?, ?, ?)", (layer, title, status))
        work_id = cur.lastrowid

        if harness and status == "claimed":
            conn.execute("INSERT INTO claim (work_id, harness, expires_at) VALUES (?, ?, datetime('now', '+1 hour'))", (work_id, harness))

        conn.commit()
        conn.close()
        return work_id

    def add_linear_mcp_event(self, issues):
        payload = {"issues": issues}
        conn = sqlite3.connect(self.db_path)
        conn.execute("INSERT INTO event (kind, payload) VALUES ('linear_mcp_update', ?)", (json.dumps(payload),))
        conn.commit()
        conn.close()

    def run_reconciler(self):
        cmd = [sys.executable, RECONCILER_PATH, "--db", self.db_path]
        p = subprocess.run(cmd, env=self.env, capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, f"Error: {p.stderr}")
        return json.loads(p.stdout)

    def test_abandoned_in_progress(self):
        self.add_work("L0", "[KER-1] abandoned", "pending")
        self.add_linear_mcp_event([{"id": "KER-1", "status": "In Progress"}])

        res = self.run_reconciler()
        self.assertIn("KER-1", res["abandoned_in_progress"])
        self.assertEqual(len(res["abandoned_in_progress"]), 1)

    def test_completed_but_unprojected(self):
        self.add_work("L0", "[KER-2] completed unprojected", "done")
        self.add_linear_mcp_event([{"id": "KER-2", "status": "In Progress"}])

        res = self.run_reconciler()
        self.assertIn("KER-2", res["completed_but_unprojected"])
        self.assertEqual(len(res["completed_but_unprojected"]), 1)

    def test_state_drift(self):
        self.add_work("L0", "[KER-3] drift", "claimed", harness="jules")
        self.add_linear_mcp_event([{"id": "KER-3", "status": "Done"}])

        res = self.run_reconciler()
        self.assertIn("KER-3", res["state_drift"])
        self.assertEqual(len(res["state_drift"]), 1)

    def test_ownership_drift(self):
        self.add_work("L0", "[KER-4] owner drift", "claimed", harness="jules")
        self.add_linear_mcp_event([{"id": "KER-4", "status": "In Progress", "assignee": "amy"}])

        res = self.run_reconciler()
        self.assertIn("KER-4", res["ownership_drift"])
        self.assertEqual(len(res["ownership_drift"]), 1)

    def test_no_drift(self):
        self.add_work("L0", "[KER-5] perfectly aligned", "claimed", harness="jules")
        self.add_linear_mcp_event([{"id": "KER-5", "status": "In Progress", "assignee": "jules"}])

        res = self.run_reconciler()
        self.assertEqual(len(res["abandoned_in_progress"]), 0)
        self.assertEqual(len(res["completed_but_unprojected"]), 0)
        self.assertEqual(len(res["state_drift"]), 0)
        self.assertEqual(len(res["ownership_drift"]), 0)

if __name__ == "__main__":
    unittest.main()
