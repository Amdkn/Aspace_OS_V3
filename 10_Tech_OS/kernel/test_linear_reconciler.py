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

class TestLinearReconciler(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test_uc.db")
        self.env = os.environ.copy()
        self.env["ASPACE_DB"] = self.db_path

        # Initialize the database
        cmd = [sys.executable, UC_PATH, "init"]
        subprocess.run(cmd, env=self.env, check=True, capture_output=True)

        # Import modules under test with the active ASPACE_DB
        import uc
        uc.DB = self.db_path
        from linear_reconciler import LinearReconciler
        from linear_reaper import LinearReaper

        self.reconciler = LinearReconciler(self.db_path)
        self.reaper = LinearReaper(self.db_path)

    def tearDown(self):
        self.tmp_dir.cleanup()

    def _insert_work(self, title: str, status: str) -> int:
        conn = sqlite3.connect(self.db_path)
        cur = conn.execute(
            "INSERT INTO work(layer, title, status) VALUES('L0', ?, ?)",
            (title, status)
        )
        wid = cur.lastrowid
        conn.commit()
        conn.close()
        return wid

    def _insert_claim(self, work_id: int, harness: str):
        conn = sqlite3.connect(self.db_path)
        conn.execute(
            "INSERT INTO claim(work_id, harness, expires_at) VALUES(?, ?, datetime('now', '+1 hour'))",
            (work_id, harness)
        )
        conn.commit()
        conn.close()

    def _insert_linear_event(self, work_id: int, status: str, assignee: str = None):
        conn = sqlite3.connect(self.db_path)
        payload = json.dumps({"status": status, "assignee": assignee})
        conn.execute(
            "INSERT INTO event(work_id, kind, payload) VALUES(?, 'linear_mcp_update', ?)",
            (work_id, payload)
        )
        conn.commit()
        conn.close()

    def test_reconciler_and_reaper(self):
        # 1. abandoned_in_progress
        w1 = self._insert_work("Task 1", "claimed")
        self._insert_claim(w1, "jules_worker")
        self._insert_linear_event(w1, "Todo", assignee="jules_worker")

        # 2. completed_but_unprojected
        w2 = self._insert_work("Task 2", "claimed")
        self._insert_claim(w2, "jules_worker")
        self._insert_linear_event(w2, "Done")

        # 3. state_drift
        w3 = self._insert_work("Task 3", "done")
        self._insert_linear_event(w3, "In Progress", assignee="jules_worker")

        # 4. ownership_drift
        w4 = self._insert_work("Task 4", "claimed")
        self._insert_claim(w4, "jules_worker")
        self._insert_linear_event(w4, "In Progress", assignee="other_worker")

        # 5. normal execution (no drift)
        w5 = self._insert_work("Task 5", "claimed")
        self._insert_claim(w5, "jules_worker")
        self._insert_linear_event(w5, "In Progress", assignee="jules_worker")

        # Reconcile and check
        report = self.reconciler.reconcile()

        abandoned = [i["work_id"] for i in report["abandoned_in_progress"]]
        completed = [i["work_id"] for i in report["completed_but_unprojected"]]
        state_drift = [i["work_id"] for i in report["state_drift"]]
        ownership = [i["work_id"] for i in report["ownership_drift"]]

        self.assertIn(w1, abandoned)
        self.assertIn(w2, completed)
        self.assertIn(w3, state_drift)
        self.assertIn(w4, ownership)

        self.assertNotIn(w5, abandoned)
        self.assertNotIn(w5, ownership)

        # Reap and check
        reap_result = self.reaper.reap()
        reaped_ids = reap_result["reaped_work_ids"]

        self.assertIn(w1, reaped_ids)
        self.assertIn(w4, reaped_ids)
        self.assertNotIn(w2, reaped_ids)
        self.assertNotIn(w3, reaped_ids)
        self.assertNotIn(w5, reaped_ids)

        # Verify DB state
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row

        # w1 and w4 should be pending and have no claim
        row1 = conn.execute("SELECT status FROM work WHERE id = ?", (w1,)).fetchone()
        self.assertEqual(row1["status"], "pending")
        c1 = conn.execute("SELECT * FROM claim WHERE work_id = ?", (w1,)).fetchone()
        self.assertIsNone(c1)

        row4 = conn.execute("SELECT status FROM work WHERE id = ?", (w4,)).fetchone()
        self.assertEqual(row4["status"], "pending")
        c4 = conn.execute("SELECT * FROM claim WHERE work_id = ?", (w4,)).fetchone()
        self.assertIsNone(c4)

        # w5 should still be claimed
        row5 = conn.execute("SELECT status FROM work WHERE id = ?", (w5,)).fetchone()
        self.assertEqual(row5["status"], "claimed")
        c5 = conn.execute("SELECT * FROM claim WHERE work_id = ?", (w5,)).fetchone()
        self.assertIsNotNone(c5)

        conn.close()

if __name__ == "__main__":
    unittest.main()
