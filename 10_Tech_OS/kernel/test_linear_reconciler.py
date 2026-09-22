import unittest
import sqlite3
import os
import json
from linear_reconciler import LinearReconciler
from linear_reaper import LinearReaper

class TestLinearReconciler(unittest.TestCase):
    def setUp(self):
        self.db_path = "test_uc.db"

        with open("10_Tech_OS/kernel/schema.sql", "r", encoding="utf-8") as f:
            schema = f.read()

        self.conn = sqlite3.connect(self.db_path)
        self.conn.executescript(schema)

        self.cursor = self.conn.cursor()

        # Setup data
        self.cursor.execute("INSERT INTO work(id, title, status, layer) VALUES (1, '[KER-1] Abandoned', 'claimed', 'L0')")
        self.cursor.execute("INSERT INTO claim(work_id, harness, expires_at) VALUES (1, 'Amy', datetime('now', '+1 hour'))")

        self.cursor.execute("INSERT INTO work(id, title, status, layer) VALUES (2, '[KER-2] Ownership Drift', 'claimed', 'L0')")
        self.cursor.execute("INSERT INTO claim(work_id, harness, expires_at) VALUES (2, 'Rory', datetime('now', '+1 hour'))")

        self.cursor.execute("INSERT INTO work(id, title, status, layer) VALUES (3, '[KER-3] Completed unprojected', 'pending', 'L0')")

        self.cursor.execute("INSERT INTO work(id, title, status, layer) VALUES (4, '[KER-4] State drift', 'done', 'L0')")

        payload = {
            "issues": [
                {"id": "KER-1", "status": "Todo", "assignee": "Amy"},
                {"id": "KER-2", "status": "In Progress", "assignee": "Amy"}, # Amy in linear, Rory locally
                {"id": "KER-3", "status": "Done", "assignee": "Rory"},
                {"id": "KER-4", "status": "In Progress", "assignee": "River"}
            ]
        }

        self.cursor.execute("INSERT INTO event(kind, payload) VALUES ('linear_mcp_update', ?)", (json.dumps(payload),))
        self.conn.commit()

    def tearDown(self):
        self.conn.close()
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_reconciler(self):
        reconciler = LinearReconciler(self.db_path)
        report = reconciler.reconcile()

        self.assertEqual(len(report["abandoned_in_progress"]), 1)
        self.assertEqual(report["abandoned_in_progress"][0]["id"], 1)

        self.assertEqual(len(report["ownership_drift"]), 1)
        self.assertEqual(report["ownership_drift"][0]["id"], 2)

        self.assertEqual(len(report["completed_but_unprojected"]), 1)
        self.assertEqual(report["completed_but_unprojected"][0]["id"], 3)

        self.assertEqual(len(report["state_drift"]), 1)
        self.assertEqual(report["state_drift"][0]["id"], 4)

    def test_reaper(self):
        reconciler = LinearReconciler(self.db_path)
        report = reconciler.reconcile()

        reaper = LinearReaper(self.db_path)
        reaped_count = reaper.reap(report)

        self.assertEqual(reaped_count, 2)

        self.cursor.execute("SELECT status FROM work WHERE id = 1")
        self.assertEqual(self.cursor.fetchone()[0], "pending")

        self.cursor.execute("SELECT status FROM work WHERE id = 2")
        self.assertEqual(self.cursor.fetchone()[0], "pending")

        self.cursor.execute("SELECT count(*) FROM claim WHERE work_id IN (1, 2)")
        self.assertEqual(self.cursor.fetchone()[0], 0)

if __name__ == '__main__':
    unittest.main()
