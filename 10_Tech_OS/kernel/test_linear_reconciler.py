import unittest
import sqlite3
import json
import os
import tempfile
import sys
import datetime

# Add 10_Tech_OS to path so 'kernel' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kernel.linear_reconciler import LinearReconciler
from kernel.linear_reaper import LinearReaper
from kernel import uc

class TestLinearReconciliation(unittest.TestCase):
    def setUp(self):
        self.db_fd, self.db_path = tempfile.mkstemp()
        os.environ["ASPACE_DB"] = self.db_path
        uc.DB = self.db_path

        # initialize schema
        conn = sqlite3.connect(self.db_path)
        with open("10_Tech_OS/kernel/schema.sql", "r") as f:
            conn.executescript(f.read())
        conn.close()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def test_reconciliation_and_reaping(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Insert test work items
        cursor.execute("INSERT INTO work (id, layer, title, status) VALUES (1, 'L0', '[KER-1] Task 1', 'claimed')")
        cursor.execute("INSERT INTO work (id, layer, title, status) VALUES (2, 'L0', '[KER-2] Task 2', 'claimed')")
        cursor.execute("INSERT INTO work (id, layer, title, status) VALUES (3, 'L0', '[KER-3] Task 3', 'pending')")

        # We must insert prediction first because of the trigger
        cursor.execute("INSERT INTO prediction (id, work_id, claim_text, confidence) VALUES (1, 4, 'test', 0.9)")
        cursor.execute("INSERT INTO work (id, layer, title, status) VALUES (4, 'L0', '[KER-4] Task 4', 'review')") # Insert as review
        cursor.execute("UPDATE work SET status='done' WHERE id=4") # update to done

        # Insert claims
        cursor.execute("INSERT INTO claim (work_id, harness, expires_at) VALUES (1, 'harness_a', datetime('now', '+1 hour'))")
        cursor.execute("INSERT INTO claim (work_id, harness, expires_at) VALUES (2, 'harness_a', datetime('now', '+1 hour'))")

        # Insert Linear MCP event
        event_payload = {
            "issues": [
                {"id": "KER-1", "status": "Todo", "assignee": "harness_a"}, # abandoned_in_progress
                {"id": "KER-2", "status": "In Progress", "assignee": "harness_b"}, # ownership_drift
                {"id": "KER-3", "status": "Done"}, # completed_but_unprojected
                {"id": "KER-4", "status": "In Progress"} # state_drift
            ]
        }
        cursor.execute("INSERT INTO event (work_id, kind, payload) VALUES (NULL, 'linear_mcp_update', ?)", (json.dumps(event_payload),))
        conn.commit()
        conn.close()

        reconciler = LinearReconciler(db_path=self.db_path)
        report = reconciler.reconcile()

        self.assertEqual(len(report["abandoned_in_progress"]), 1)
        self.assertEqual(report["abandoned_in_progress"][0]["work_id"], 1)

        self.assertEqual(len(report["ownership_drift"]), 1)
        self.assertEqual(report["ownership_drift"][0]["work_id"], 2)

        self.assertEqual(len(report["completed_but_unprojected"]), 1)
        self.assertEqual(report["completed_but_unprojected"][0]["work_id"], 3)

        self.assertEqual(len(report["state_drift"]), 1)
        self.assertEqual(report["state_drift"][0]["work_id"], 4)

        # Now reap
        reaper = LinearReaper(db_path=self.db_path)
        reaper.reap(report)

        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Check work 1 is now pending
        row1 = cursor.execute("SELECT status FROM work WHERE id = 1").fetchone()
        self.assertEqual(row1["status"], "pending")
        claim1 = cursor.execute("SELECT * FROM claim WHERE work_id = 1").fetchone()
        self.assertIsNone(claim1)

        # Check work 2 is now pending
        row2 = cursor.execute("SELECT status FROM work WHERE id = 2").fetchone()
        self.assertEqual(row2["status"], "pending")
        claim2 = cursor.execute("SELECT * FROM claim WHERE work_id = 2").fetchone()
        self.assertIsNone(claim2)

        conn.close()

if __name__ == '__main__':
    unittest.main()

    def test_reconciliation_multiple_events(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Insert test work items
        cursor.execute("INSERT INTO work (id, layer, title, status) VALUES (5, 'L0', '[KER-5] Task 5', 'claimed')")
        cursor.execute("INSERT INTO claim (work_id, harness, expires_at) VALUES (5, 'harness_a', datetime('now', '+1 hour'))")

        # Insert first event showing in progress
        event_payload_old = {
            "issues": [
                {"id": "KER-5", "status": "In Progress", "assignee": "harness_a"},
            ]
        }
        cursor.execute("INSERT INTO event (work_id, kind, payload) VALUES (NULL, 'linear_mcp_update', ?)", (json.dumps(event_payload_old),))

        # Insert second event showing Todo
        event_payload_new = {
            "issues": [
                {"id": "KER-5", "status": "Todo", "assignee": "harness_a"},
            ]
        }
        cursor.execute("INSERT INTO event (work_id, kind, payload) VALUES (NULL, 'linear_mcp_update', ?)", (json.dumps(event_payload_new),))

        conn.commit()
        conn.close()

        reconciler = LinearReconciler(db_path=self.db_path)
        report = reconciler.reconcile()

        # because we sort by id ASC, the newest event will overwrite, so the issue will be 'Todo' which triggers abandoned_in_progress
        self.assertTrue(any(i["issue_id"] == "KER-5" for i in report["abandoned_in_progress"]))
