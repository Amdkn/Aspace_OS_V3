import unittest
import sqlite3
import json
import os
import sys

# Ensure local imports work correctly for the tests
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from linear_reconciler import LinearReconciler
from linear_reaper import LinearReaper
import uc

class TestLinearReconcilerAndReaper(unittest.TestCase):
    def setUp(self):
        # Override the uc DB logic for an in-memory testing db
        self.db_path = ":memory:"
        uc.DB = self.db_path
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.c = self.conn.cursor()

        # Initialize the test schema
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "schema.sql"), "r") as f:
            self.c.executescript(f.read())

    def tearDown(self):
        self.conn.close()

    def _create_work(self, title, status="pending"):
        self.c.execute("INSERT INTO work(layer, title, status) VALUES('L0', ?, ?)", (title, status))
        return self.c.lastrowid

    def _create_claim(self, work_id, harness):
        self.c.execute(
            "INSERT INTO claim(work_id, harness, expires_at) VALUES(?, ?, datetime('now', '+1 hour'))",
            (work_id, harness)
        )

    def _add_linear_update(self, work_id, payload):
        self.c.execute(
            "INSERT INTO event(work_id, kind, payload) VALUES(?, 'linear_mcp_update', ?)",
            (work_id, json.dumps(payload))
        )

    def test_reconciler_drifts(self):
        # Setup specific drifts

        # 1. abandoned_in_progress
        w1 = self._create_work("[KER-101] abandoned task", status="claimed")
        self._create_claim(w1, "test_harness")
        self._add_linear_update(w1, {"issue_id": "KER-101", "status": "Todo", "assignee": "test_harness"})

        # 2. ownership_drift
        w2 = self._create_work("[KER-102] stolen task", status="claimed")
        self._create_claim(w2, "test_harness")
        self._add_linear_update(w2, {"issue_id": "KER-102", "status": "In Progress", "assignee": "other_harness"})

        # 3. completed_but_unprojected
        w3 = self._create_work("[KER-103] forgot to update", status="pending")
        self._add_linear_update(w3, {"issue_id": "KER-103", "status": "Done", "assignee": "test_harness"})

        # 4. state_drift
        w4 = self._create_work("[KER-104] closed locally", status="done")
        self._add_linear_update(w4, {"issue_id": "KER-104", "status": "In Progress", "assignee": "test_harness"})

        # 5. Normal (no drift)
        w5 = self._create_work("[KER-105] healthy task", status="claimed")
        self._create_claim(w5, "test_harness")
        self._add_linear_update(w5, {"issue_id": "KER-105", "status": "In Progress", "assignee": "test_harness"})

        reconciler = LinearReconciler(self.c)
        drifts = reconciler.reconcile()

        self.assertEqual(len(drifts["abandoned_in_progress"]), 1)
        self.assertEqual(drifts["abandoned_in_progress"][0]["work_id"], w1)

        self.assertEqual(len(drifts["ownership_drift"]), 1)
        self.assertEqual(drifts["ownership_drift"][0]["work_id"], w2)

        self.assertEqual(len(drifts["completed_but_unprojected"]), 1)
        self.assertEqual(drifts["completed_but_unprojected"][0]["work_id"], w3)

        self.assertEqual(len(drifts["state_drift"]), 1)
        self.assertEqual(drifts["state_drift"][0]["work_id"], w4)

    def test_reaper_fixes_abandoned_and_ownership_drift(self):
        # 1. abandoned_in_progress
        w1 = self._create_work("[KER-201] abandon fix", status="claimed")
        self._create_claim(w1, "test_harness")
        self._add_linear_update(w1, {"issue_id": "KER-201", "status": "Todo", "assignee": "test_harness"})

        # 2. ownership_drift
        w2 = self._create_work("[KER-202] ownership fix", status="claimed")
        self._create_claim(w2, "test_harness")
        self._add_linear_update(w2, {"issue_id": "KER-202", "status": "In Progress", "assignee": "other_harness"})

        reaper = LinearReaper(self.c)
        res = reaper.reap()

        self.assertEqual(res["reaped_count"], 2)

        # Check work items reset to pending
        self.c.execute("SELECT status FROM work WHERE id IN (?, ?)", (w1, w2))
        for row in self.c.fetchall():
            self.assertEqual(row["status"], "pending")

        # Check claims are deleted
        self.c.execute("SELECT count(*) as c FROM claim WHERE work_id IN (?, ?)", (w1, w2))
        self.assertEqual(self.c.fetchone()["c"], 0)

        # Check reap events logged
        self.c.execute("SELECT count(*) as c FROM event WHERE kind='reap' AND work_id IN (?, ?)", (w1, w2))
        self.assertEqual(self.c.fetchone()["c"], 2)

if __name__ == '__main__':
    unittest.main()
