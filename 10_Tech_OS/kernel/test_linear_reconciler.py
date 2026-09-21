import unittest
import sqlite3
import os
import json
from linear_reconciler import LinearReconciler, ReconcilerReport
from linear_reaper import LinearReaper
import tempfile

class TestLinearReconciler(unittest.TestCase):
    def setUp(self):
        self.temp_db = tempfile.NamedTemporaryFile(delete=False)
        self.db_path = self.temp_db.name
        self.temp_db.close()

        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row

        # Setup schema
        with open("10_Tech_OS/kernel/schema.sql", "r") as f:
            self.conn.executescript(f.read())

        self.reconciler = LinearReconciler(self.db_path)
        self.reaper = LinearReaper(self.db_path)

    def tearDown(self):
        self.conn.close()
        os.unlink(self.db_path)

    def seed_data(self):
        # Work items
        self.conn.execute("INSERT INTO work (id, layer, title, status) VALUES (1, 'L0', '[KER-1] Test task 1', 'claimed')")
        self.conn.execute("INSERT INTO work (id, layer, title, status) VALUES (2, 'L0', '[KER-2] Test task 2', 'claimed')")
        self.conn.execute("INSERT INTO work (id, layer, title, status) VALUES (3, 'L0', '[KER-3] Test task 3', 'claimed')")
        # For done state, need a prediction first due to trigger
        self.conn.execute("INSERT INTO work (id, layer, title, status) VALUES (4, 'L0', '[KER-4] Test task 4', 'review')")
        self.conn.execute("INSERT INTO prediction (work_id, claim_text, confidence) VALUES (4, 'test', 0.9)")
        self.conn.execute("UPDATE work SET status = 'done' WHERE id = 4")

        # Claims
        self.conn.execute("INSERT INTO claim (work_id, harness, expires_at) VALUES (1, 'jules-worker', '2030-01-01')")
        self.conn.execute("INSERT INTO claim (work_id, harness, expires_at) VALUES (2, 'jules-worker', '2030-01-01')")
        self.conn.execute("INSERT INTO claim (work_id, harness, expires_at) VALUES (3, 'jules-worker', '2030-01-01')")

        # Events
        # KER-1: Abandoned in progress (linear unassigned, workgraph claimed)
        payload1 = json.dumps({"issue_id": "KER-1", "status": "In Progress", "assignee": None})
        self.conn.execute("INSERT INTO event (work_id, kind, payload) VALUES (1, 'linear_mcp_update', ?)", (payload1,))

        # KER-2: Completed but unprojected (linear done, workgraph claimed)
        payload2 = json.dumps({"issue_id": "KER-2", "status": "Done", "assignee": "jules"})
        self.conn.execute("INSERT INTO event (work_id, kind, payload) VALUES (2, 'linear_mcp_update', ?)", (payload2,))

        # KER-3: Ownership drift (linear assignee is bob, workgraph is jules-worker)
        payload3 = json.dumps({"issue_id": "KER-3", "status": "In Progress", "assignee": "bob"})
        self.conn.execute("INSERT INTO event (work_id, kind, payload) VALUES (3, 'linear_mcp_update', ?)", (payload3,))

        # KER-4: State drift (workgraph is done, linear is not)
        payload4 = json.dumps({"issue_id": "KER-4", "status": "In Progress", "assignee": "jules"})
        self.conn.execute("INSERT INTO event (work_id, kind, payload) VALUES (4, 'linear_mcp_update', ?)", (payload4,))

        self.conn.commit()

    def test_reconciler(self):
        self.seed_data()

        report = self.reconciler.reconcile()

        self.assertEqual(len(report.abandoned_in_progress), 1)
        self.assertEqual(report.abandoned_in_progress[0]["issue_id"], "KER-1")

        self.assertEqual(len(report.completed_but_unprojected), 1)
        self.assertEqual(report.completed_but_unprojected[0]["issue_id"], "KER-2")

        # state_drift will have KER-2 and KER-4
        self.assertEqual(len(report.state_drift), 2)
        state_drift_ids = [s["issue_id"] for s in report.state_drift]
        self.assertIn("KER-2", state_drift_ids)
        self.assertIn("KER-4", state_drift_ids)

        # ownership_drift will have KER-1 (abandoned in linear but claimed in WG) and KER-3 (mismatched assignee)
        self.assertEqual(len(report.ownership_drift), 2)
        ownership_drift_ids = [s["issue_id"] for s in report.ownership_drift]
        self.assertIn("KER-1", ownership_drift_ids)
        self.assertIn("KER-3", ownership_drift_ids)

    def test_reaper(self):
        self.seed_data()

        report = self.reconciler.reconcile()

        # Should reap KER-1 and KER-3
        results = self.reaper.reap(report)

        self.assertEqual(results["reaped_abandoned"], 1)
        self.assertEqual(results["reaped_ownership_drift"], 2)

        # Check DB state
        w1 = self.conn.execute("SELECT status FROM work WHERE id = 1").fetchone()
        self.assertEqual(w1["status"], "pending")

        c1 = self.conn.execute("SELECT COUNT(*) as c FROM claim WHERE work_id = 1").fetchone()
        self.assertEqual(c1["c"], 0)

        w3 = self.conn.execute("SELECT status FROM work WHERE id = 3").fetchone()
        self.assertEqual(w3["status"], "pending")

        c3 = self.conn.execute("SELECT COUNT(*) as c FROM claim WHERE work_id = 3").fetchone()
        self.assertEqual(c3["c"], 0)

        # Event should be logged
        e1 = self.conn.execute("SELECT COUNT(*) as c FROM event WHERE work_id = 1 AND kind = 'system'").fetchone()
        self.assertEqual(e1["c"], 1)

if __name__ == '__main__':
    unittest.main()
