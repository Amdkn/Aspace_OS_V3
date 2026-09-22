import unittest
import sqlite3
import json
import os
import uuid
from linear_reconciler import LinearReconciler
from linear_reaper import LinearReaper
import datetime

class TestLinearReconciler(unittest.TestCase):
    def setUp(self):
        # Create an in-memory SQLite database for testing
        self.db_path = ':memory:'
        self.c = sqlite3.connect(self.db_path, isolation_level=None)
        self.c.row_factory = sqlite3.Row

        # Initialize schema
        schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
        with open(schema_path, 'r') as f:
            self.c.executescript(f.read())

        # Helper to add work and event
        def add_work(title, status, linear_status, linear_assignee=None, claim_harness=None):
            self.c.execute("INSERT INTO work (layer, title, status) VALUES ('L0', ?, ?)", (title, status))
            wid = self.c.execute("SELECT last_insert_rowid()").fetchone()[0]
            if claim_harness:
                self.c.execute(
                    "INSERT INTO claim (work_id, harness, expires_at) VALUES (?, ?, datetime('now', '+1 hour'))",
                    (wid, claim_harness)
                )

            payload = {"status": linear_status}
            if linear_assignee:
                payload["assignee"] = linear_assignee

            self.c.execute(
                "INSERT INTO event (work_id, kind, payload) VALUES (?, 'linear_mcp_update', ?)",
                (wid, json.dumps(payload))
            )
            return wid

        self.add_work = add_work

    def tearDown(self):
        self.c.close()

    def test_reconciler_no_drift(self):
        wid = self.add_work("[KER-100] In Progress Task", "claimed", "in_progress", linear_assignee="HarnessA", claim_harness="HarnessA")
        reconciler = LinearReconciler(self.c)
        reports = reconciler.reconcile_all()
        self.assertEqual(len(reports), 0)

    def test_abandoned_in_progress(self):
        wid = self.add_work("[KER-101] Abandoned Task", "claimed", "todo", claim_harness="HarnessA")
        reconciler = LinearReconciler(self.c)
        reports = reconciler.reconcile_all()

        self.assertEqual(len(reports), 1)
        self.assertEqual(reports[0]["drift_type"], "abandoned_in_progress")
        self.assertEqual(reports[0]["issue_id"], "KER-101")

        # Check reaper behavior
        reaper = LinearReaper(self.c)
        reaped = reaper.reap_abandoned()
        self.assertIn(wid, reaped)

        # Verify db state
        status = self.c.execute("SELECT status FROM work WHERE id=?", (wid,)).fetchone()[0]
        self.assertEqual(status, "pending")

        claim_count = self.c.execute("SELECT COUNT(*) FROM claim WHERE work_id=?", (wid,)).fetchone()[0]
        self.assertEqual(claim_count, 0)

    def test_ownership_drift(self):
        wid = self.add_work("[KER-102] Stolen Task", "claimed", "in_progress", linear_assignee="HarnessB", claim_harness="HarnessA")
        reconciler = LinearReconciler(self.c)
        reports = reconciler.reconcile_all()

        self.assertEqual(len(reports), 1)
        self.assertEqual(reports[0]["drift_type"], "ownership_drift")
        self.assertEqual(reports[0]["issue_id"], "KER-102")

        # Check reaper behavior
        reaper = LinearReaper(self.c)
        reaped = reaper.reap_abandoned()
        self.assertIn(wid, reaped)

    def test_completed_but_unprojected(self):
        wid = self.add_work("[KER-103] Ghost Done Task", "pending", "done")
        reconciler = LinearReconciler(self.c)
        reports = reconciler.reconcile_all()

        self.assertEqual(len(reports), 1)
        self.assertEqual(reports[0]["drift_type"], "completed_but_unprojected")

        # Should not be reaped by reap_abandoned
        reaper = LinearReaper(self.c)
        reaped = reaper.reap_abandoned()
        self.assertNotIn(wid, reaped)

    def test_state_drift(self):
        wid = self.add_work("[KER-104] Local Done Task", "done", "todo")
        reconciler = LinearReconciler(self.c)
        reports = reconciler.reconcile_all()

        self.assertEqual(len(reports), 1)
        self.assertEqual(reports[0]["drift_type"], "state_drift")

        # Should not be reaped
        reaper = LinearReaper(self.c)
        reaped = reaper.reap_abandoned()
        self.assertNotIn(wid, reaped)

if __name__ == '__main__':
    unittest.main()
