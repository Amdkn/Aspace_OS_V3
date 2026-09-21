#!/usr/bin/env python3
"""
test_linear_reconciler.py — Tests for Linear<->WorkGraph reconciliation
"""

import json
import os
import sqlite3
import tempfile
import unittest
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
UC_PATH = os.path.join(HERE, "uc.py")
RECONCILER_PATH = os.path.join(HERE, "linear_reconciler.py")

class TestLinearReconciler(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test_uc.db")
        self.env = os.environ.copy()
        self.env["ASPACE_DB"] = self.db_path

        # Initialize the database
        cmd = [sys.executable, UC_PATH, "init"]
        subprocess.run(cmd, env=self.env, check=True, capture_output=True)

        self.conn = sqlite3.connect(self.db_path, isolation_level=None)
        self.conn.row_factory = sqlite3.Row

    def tearDown(self):
        self.conn.close()
        self.tmp_dir.cleanup()

    def run_reconciler(self):
        cmd = [sys.executable, RECONCILER_PATH]
        p = subprocess.run(cmd, env=self.env, capture_output=True, text=True)
        return p

    def add_work(self, title, status):
        cursor = self.conn.execute(
            "INSERT INTO work(layer, title, status) VALUES('L0', ?, ?)",
            (title, status)
        )
        return cursor.lastrowid

    def add_claim(self, work_id, harness, expired=False):
        expires_at = "datetime('now', '-1 hour')" if expired else "datetime('now', '+1 hour')"
        self.conn.execute(
            f"INSERT INTO claim(work_id, harness, expires_at) VALUES(?, ?, {expires_at})",
            (work_id, harness)
        )

    def add_linear_mcp_event(self, issues):
        payload = {"issues": issues}
        self.conn.execute(
            "INSERT INTO event(kind, payload) VALUES('linear_mcp_update', ?)",
            (json.dumps(payload),)
        )

    def test_no_drift(self):
        w1 = self.add_work("[KER-10] Normal task", "pending")
        w2 = self.add_work("[KER-20] Claimed task", "claimed")
        self.add_claim(w2, "harness_1")

        self.add_linear_mcp_event([
            {"id": "KER-10", "status": "Todo", "assignee": "None"},
            {"id": "KER-20", "status": "In Progress", "assignee": "harness_1"},
        ])

        p = self.run_reconciler()
        self.assertEqual(p.returncode, 0)

        events = self.conn.execute("SELECT * FROM event WHERE kind='reconciliation_drift'").fetchall()
        self.assertEqual(len(events), 0)

    def test_abandoned_in_progress(self):
        w1 = self.add_work("[KER-30] Pending but Linear says In Progress", "pending")
        w2 = self.add_work("[KER-40] Claimed but expired", "claimed")
        self.add_claim(w2, "harness_1", expired=True)

        self.add_linear_mcp_event([
            {"id": "KER-30", "status": "In Progress"},
            {"id": "KER-40", "status": "In Progress"}
        ])

        p = self.run_reconciler()
        self.assertEqual(p.returncode, 0)

        events = self.conn.execute("SELECT payload FROM event WHERE kind='reconciliation_drift'").fetchall()
        self.assertEqual(len(events), 2)

        drifts = [json.loads(e["payload"]) for e in events]
        types = [d["type"] for d in drifts]

        self.assertIn("abandoned_in_progress", types)
        # Should be two abandoned_in_progress
        self.assertEqual(types.count("abandoned_in_progress"), 2)

    def test_completed_but_unprojected(self):
        w1 = self.add_work("[KER-50] Done here but not there", "done")

        self.add_linear_mcp_event([
            {"id": "KER-50", "status": "In Progress"}
        ])

        p = self.run_reconciler()
        self.assertEqual(p.returncode, 0)

        events = self.conn.execute("SELECT payload FROM event WHERE kind='reconciliation_drift'").fetchall()
        self.assertEqual(len(events), 1)

        payload = json.loads(events[0]["payload"])
        self.assertEqual(payload["type"], "completed_but_unprojected")
        self.assertEqual(payload["details"]["issue_id"], "KER-50")

    def test_state_drift(self):
        w1 = self.add_work("[KER-60] Not done here", "pending")

        self.add_linear_mcp_event([
            {"id": "KER-60", "status": "Done"}
        ])

        p = self.run_reconciler()
        self.assertEqual(p.returncode, 0)

        events = self.conn.execute("SELECT payload FROM event WHERE kind='reconciliation_drift'").fetchall()
        self.assertEqual(len(events), 1)

        payload = json.loads(events[0]["payload"])
        self.assertEqual(payload["type"], "state_drift")
        self.assertEqual(payload["details"]["issue_id"], "KER-60")

    def test_ownership_drift(self):
        w1 = self.add_work("[KER-70] Mismatched assignee", "claimed")
        self.add_claim(w1, "harness_1")

        self.add_linear_mcp_event([
            {"id": "KER-70", "status": "In Progress", "assignee": "harness_2"}
        ])

        p = self.run_reconciler()
        self.assertEqual(p.returncode, 0)

        events = self.conn.execute("SELECT payload FROM event WHERE kind='reconciliation_drift'").fetchall()
        self.assertEqual(len(events), 1)

        payload = json.loads(events[0]["payload"])
        self.assertEqual(payload["type"], "ownership_drift")
        self.assertEqual(payload["details"]["issue_id"], "KER-70")

if __name__ == "__main__":
    unittest.main()
