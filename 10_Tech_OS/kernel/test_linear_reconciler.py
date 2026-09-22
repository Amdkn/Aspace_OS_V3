import unittest
import sqlite3
import os
import json
import tempfile
import uc
from linear_reconciler import LinearReconciler
from linear_reaper import LinearReaper

class TestLinearReconciler(unittest.TestCase):
    def setUp(self):
        self.temp_db_fd, self.temp_db_path = tempfile.mkstemp()
        os.close(self.temp_db_fd)

        # Override ASPACE_DB for uc module
        os.environ["ASPACE_DB"] = self.temp_db_path
        uc.DB = self.temp_db_path

        # Init schema
        with open("10_Tech_OS/kernel/schema.sql", encoding="utf-8") as f:
            sql = f.read()

        self.conn = sqlite3.connect(self.temp_db_path)
        self.conn.executescript(sql)

        # Setup linear event
        linear_data = {
            "issues": [
                {"id": "KER-1", "status": "Todo", "assignee": "Yaz"},
                {"id": "KER-2", "status": "In Progress", "assignee": "Rory"},
                {"id": "KER-3", "status": "Done", "assignee": "Amy"},
                {"id": "KER-4", "status": "Todo", "assignee": "Doctor"}
            ]
        }
        self.conn.execute("INSERT INTO event (kind, payload) VALUES (?, ?)",
                          ("linear_mcp_update", json.dumps(linear_data)))

        # Setup work items

        # 1. abandoned_in_progress
        # local claimed, linear Todo
        self.conn.execute("INSERT INTO work (id, layer, title, status) VALUES (?, ?, ?, ?)",
                          (1, "L1", "[KER-1] abandoned", "claimed"))
        self.conn.execute("INSERT INTO claim (work_id, harness, expires_at) VALUES (?, ?, datetime('now', '+1 hour'))",
                          (1, "Yaz_harness"))

        # 2. ownership_drift
        # local claimed by Amy, linear assignee Rory
        self.conn.execute("INSERT INTO work (id, layer, title, status) VALUES (?, ?, ?, ?)",
                          (2, "L1", "[KER-2] ownership drift", "claimed"))
        self.conn.execute("INSERT INTO claim (work_id, harness, expires_at) VALUES (?, ?, datetime('now', '+1 hour'))",
                          (2, "Amy_harness"))

        # 3. completed_but_unprojected
        # local pending, linear Done
        self.conn.execute("INSERT INTO work (id, layer, title, status) VALUES (?, ?, ?, ?)",
                          (3, "L1", "[KER-3] completed but unprojected", "pending"))

        # 4. state_drift
        # local done, linear Todo
        self.conn.execute("INSERT INTO work (id, layer, title, status) VALUES (?, ?, ?, ?)",
                          (4, "L1", "[KER-4] state drift", "done"))

        self.conn.commit()

    def tearDown(self):
        self.conn.close()
        if os.path.exists(self.temp_db_path):
            os.remove(self.temp_db_path)

    def test_reconciler_detection(self):
        reconciler = LinearReconciler(self.conn)
        report = reconciler.reconcile()

        self.assertEqual(len(report["abandoned_in_progress"]), 1)
        self.assertEqual(report["abandoned_in_progress"][0]["work_id"], 1)

        self.assertEqual(len(report["ownership_drift"]), 1)
        self.assertEqual(report["ownership_drift"][0]["work_id"], 2)

        self.assertEqual(len(report["completed_but_unprojected"]), 1)
        self.assertEqual(report["completed_but_unprojected"][0]["work_id"], 3)

        self.assertEqual(len(report["state_drift"]), 1)
        self.assertEqual(report["state_drift"][0]["work_id"], 4)

    def test_reaper_execution(self):
        reconciler = LinearReconciler(self.conn)
        reaper = LinearReaper(reconciler)
        drift_reaped, _ = reaper.reap()

        self.assertEqual(len(drift_reaped), 2)

        # Check if work 1 is reset
        cur = self.conn.execute("SELECT status FROM work WHERE id = 1")
        self.assertEqual(cur.fetchone()[0], "pending")

        # Check if claim 1 is removed
        cur = self.conn.execute("SELECT COUNT(*) FROM claim WHERE work_id = 1")
        self.assertEqual(cur.fetchone()[0], 0)

        # Check if work 2 is reset
        cur = self.conn.execute("SELECT status FROM work WHERE id = 2")
        self.assertEqual(cur.fetchone()[0], "pending")

        # Check if reap events were logged
        cur = self.conn.execute("SELECT COUNT(*) FROM event WHERE kind = 'reap' AND work_id IN (1, 2)")
        self.assertEqual(cur.fetchone()[0], 2)

if __name__ == '__main__':
    unittest.main()
