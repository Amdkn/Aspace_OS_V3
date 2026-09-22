import unittest
import sqlite3
import tempfile
import os
import json
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from linear_reconciler import LinearReconciler
from linear_reaper import LinearReaper
import uc

class TestLinearReconciler(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test_uc.db")

        # Initialize schema
        with open(os.path.join(HERE, "schema.sql"), "r", encoding="utf-8") as f:
            schema = f.read()
        conn = sqlite3.connect(self.db_path)
        conn.executescript(schema)
        conn.close()

    def tearDown(self):
        self.tmp_dir.cleanup()

    def _insert_linear_update(self, payload):
        conn = sqlite3.connect(self.db_path)
        conn.execute(
            "INSERT INTO event(work_id, kind, payload) VALUES(NULL, 'linear_mcp_update', ?)",
            (json.dumps(payload),)
        )
        conn.commit()
        conn.close()

    def _insert_work(self, title, status='pending', harness=None):
        conn = sqlite3.connect(self.db_path)
        cur = conn.execute(
            "INSERT INTO work(layer, title, status) VALUES('L0', ?, ?)",
            (title, status)
        )
        work_id = cur.lastrowid
        if harness and status == 'claimed':
            conn.execute(
                "INSERT INTO claim(work_id, harness, expires_at) VALUES(?, ?, datetime('now', '+1 hour'))",
                (work_id, harness)
            )
        conn.commit()
        conn.close()
        return work_id

    def test_reconciler_scenarios(self):
        # 1. abandoned_in_progress
        w1 = self._insert_work("[KER-101] Fix bug", "claimed", "Yaz")
        # 2. ownership_drift
        w2 = self._insert_work("[KER-102] Implement feature", "claimed", "Graham")
        # 3. completed_but_unprojected
        w3 = self._insert_work("[KER-103] Documentation", "pending")
        # 4. state_drift
        w4 = self._insert_work("[KER-104] Testing", "done")

        # Insert Linear update
        self._insert_linear_update({
            "issues": [
                {"id": "KER-101", "status": "Todo", "assignee": "Yaz"}, # Linear not active, local claimed
                {"id": "KER-102", "status": "In Progress", "assignee": "Ryan"}, # Linear in progress by Ryan, local claimed by Graham
                {"id": "KER-103", "status": "Done", "assignee": "Yaz"}, # Linear Done, local pending
                {"id": "KER-104", "status": "In Progress", "assignee": "Yaz"}, # Linear in progress, local Done
            ]
        })

        reconciler = LinearReconciler(self.db_path)
        report = reconciler.generate_report()

        self.assertEqual(len(report["abandoned_in_progress"]), 1)
        self.assertEqual(report["abandoned_in_progress"][0]["issue_id"], "KER-101")

        self.assertEqual(len(report["ownership_drift"]), 1)
        self.assertEqual(report["ownership_drift"][0]["issue_id"], "KER-102")

        self.assertEqual(len(report["completed_but_unprojected"]), 1)
        self.assertEqual(report["completed_but_unprojected"][0]["issue_id"], "KER-103")

        self.assertEqual(len(report["state_drift"]), 1)
        self.assertEqual(report["state_drift"][0]["issue_id"], "KER-104")

    def test_reaper(self):
        w1 = self._insert_work("[KER-201] Abandoned task", "claimed", "Yaz")
        w2 = self._insert_work("[KER-202] Drift task", "claimed", "Graham")

        self._insert_linear_update({
            "issues": [
                {"id": "KER-201", "status": "Todo", "assignee": "Yaz"},
                {"id": "KER-202", "status": "In Progress", "assignee": "Ryan"},
            ]
        })

        reaper = LinearReaper(self.db_path)
        reaped_count = reaper.reap()
        self.assertEqual(reaped_count, 2)

        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        w1_status = conn.execute("SELECT status FROM work WHERE id=?", (w1,)).fetchone()["status"]
        w2_status = conn.execute("SELECT status FROM work WHERE id=?", (w2,)).fetchone()["status"]

        self.assertEqual(w1_status, "pending")
        self.assertEqual(w2_status, "pending")

        # Check claims deleted
        claim1 = conn.execute("SELECT * FROM claim WHERE work_id=?", (w1,)).fetchone()
        self.assertIsNone(claim1)

        # Check reap events
        events = conn.execute("SELECT * FROM event WHERE kind='reap'").fetchall()
        self.assertEqual(len(events), 2)
        conn.close()

    def test_uc_reap_integration(self):
        env = os.environ.copy()
        env["ASPACE_DB"] = self.db_path

        w1 = self._insert_work("[KER-301] Abandoned via uc", "claimed", "Yaz")
        self._insert_linear_update({
            "issues": [
                {"id": "KER-301", "status": "Todo", "assignee": "Yaz"}
            ]
        })

        cmd = [sys.executable, os.path.join(HERE, "uc.py"), "reap"]
        p = subprocess.run(cmd, env=env, capture_output=True, text=True)
        self.assertEqual(p.returncode, 0)

        conn = sqlite3.connect(self.db_path)
        w1_status = conn.execute("SELECT status FROM work WHERE id=?", (w1,)).fetchone()[0]
        conn.close()
        self.assertEqual(w1_status, "pending")

if __name__ == '__main__':
    unittest.main()
