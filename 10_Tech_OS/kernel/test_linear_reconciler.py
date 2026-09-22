import json
import os
import sqlite3
import tempfile
import unittest
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from linear_reconciler import LinearReconciler
from linear_reaper import LinearReaper

class TestLinearReconciler(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test_uc.db")
        self.env = os.environ.copy()
        self.env["ASPACE_DB"] = self.db_path

        # Initialize DB schema
        conn = sqlite3.connect(self.db_path)
        with open(os.path.join(HERE, "schema.sql"), encoding="utf-8") as f:
            sql = f.read()
        conn.executescript(sql)
        conn.commit()
        conn.close()

    def tearDown(self):
        self.tmp_dir.cleanup()

    def test_reconciler_and_reaper(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        # Insert work items
        # Work 1: abandoned_in_progress
        cur.execute("INSERT INTO work(layer, title, status) VALUES('L0', '[KER-1] abandoned', 'claimed')")
        w1_id = cur.lastrowid
        cur.execute("INSERT INTO claim(work_id, harness, expires_at) VALUES(?, 'harness_1', datetime('now', '+1 hour'))", (w1_id,))

        # Work 2: ownership_drift
        cur.execute("INSERT INTO work(layer, title, status) VALUES('L0', '[KER-2] ownership drift', 'claimed')")
        w2_id = cur.lastrowid
        cur.execute("INSERT INTO claim(work_id, harness, expires_at) VALUES(?, 'harness_1', datetime('now', '+1 hour'))", (w2_id,))

        # Work 3: completed_but_unprojected
        cur.execute("INSERT INTO work(layer, title, status) VALUES('L0', '[KER-3] completed unprojected', 'pending')")
        w3_id = cur.lastrowid

        # Work 4: state_drift
        cur.execute("INSERT INTO work(layer, title, status) VALUES('L0', '[KER-4] state drift', 'done')")
        w4_id = cur.lastrowid

        # Insert linear_mcp_update event
        mcp_payload = {
            "issues": [
                {"id": "KER-1", "status": "Todo", "assignee": "harness_1"},
                {"id": "KER-2", "status": "In Progress", "assignee": "harness_2"},
                {"id": "KER-3", "status": "Done", "assignee": "harness_1"},
                {"id": "KER-4", "status": "In Progress", "assignee": "harness_1"}
            ]
        }
        cur.execute("INSERT INTO event(kind, payload) VALUES('linear_mcp_update', ?)", (json.dumps(mcp_payload),))

        conn.commit()
        conn.close()

        reconciler = LinearReconciler(self.db_path)
        drift_report = reconciler.reconcile()

        # Check drift categories
        reasons = {item["reason"] for item in drift_report}
        self.assertIn("abandoned_in_progress", reasons)
        self.assertIn("ownership_drift", reasons)
        self.assertIn("completed_but_unprojected", reasons)
        self.assertIn("state_drift", reasons)

        # Run reaper
        reaper = LinearReaper(self.db_path)
        reaped_ids = reaper.reap()

        self.assertIn(w1_id, reaped_ids)
        self.assertIn(w2_id, reaped_ids)

        # Verify state after reap
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        cur.execute("SELECT status FROM work WHERE id=?", (w1_id,))
        self.assertEqual(cur.fetchone()[0], "pending")

        cur.execute("SELECT status FROM work WHERE id=?", (w2_id,))
        self.assertEqual(cur.fetchone()[0], "pending")

        cur.execute("SELECT COUNT(*) FROM claim WHERE work_id=?", (w1_id,))
        self.assertEqual(cur.fetchone()[0], 0)

        cur.execute("SELECT payload FROM event WHERE work_id=? AND kind='reap'", (w1_id,))
        event1 = json.loads(cur.fetchone()[0])
        self.assertEqual(event1["reason"], "abandoned_in_progress")

        conn.close()

if __name__ == '__main__':
    unittest.main()
