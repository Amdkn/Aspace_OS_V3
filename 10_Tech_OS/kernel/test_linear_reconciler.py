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

from linear_reconciler import LinearReconciler
from linear_reaper import LinearReaper

class TestLinearReconciler(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test_uc.db")
        self.env = os.environ.copy()
        self.env["ASPACE_DB"] = self.db_path

        cmd = [sys.executable, UC_PATH, "init"]
        subprocess.run(cmd, env=self.env, check=True, capture_output=True)

        self.reconciler = LinearReconciler(self.db_path)
        self.reaper = LinearReaper(self.db_path)

    def tearDown(self):
        self.tmp_dir.cleanup()

    def create_work(self, title, status):
        conn = sqlite3.connect(self.db_path)
        conn.execute(
            "INSERT INTO work(layer, title, status) VALUES('L0', ?, ?)",
            (title, status)
        )
        work_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
        conn.commit()
        conn.close()
        return work_id

    def add_claim(self, work_id, harness):
        conn = sqlite3.connect(self.db_path)
        conn.execute(
            "INSERT INTO claim(work_id, harness, expires_at) VALUES(?, ?, datetime('now', '+1 hour'))",
            (work_id, harness)
        )
        conn.commit()
        conn.close()

    def add_linear_event(self, issue_id, status, assignee=None):
        payload = {
            "issue_id": issue_id,
            "status": status,
        }
        if assignee:
            payload["assignee"] = assignee

        conn = sqlite3.connect(self.db_path)
        conn.execute(
            "INSERT INTO event(kind, payload) VALUES('linear_mcp_update', ?)",
            (json.dumps(payload),)
        )
        conn.commit()
        conn.close()

    def test_reconciler_and_reaper(self):
        # 1. abandoned_in_progress
        w1 = self.create_work("[KER-1] abandoned", "claimed")
        self.add_claim(w1, "rory_build")
        self.add_linear_event("KER-1", "Todo")

        # 2. ownership_drift
        w2 = self.create_work("[KER-2] ownership drift", "claimed")
        self.add_claim(w2, "rory_build")
        self.add_linear_event("KER-2", "In Progress", "amy_spec")

        # 3. completed_but_unprojected
        w3 = self.create_work("[KER-3] completed unprojected", "review")
        self.add_linear_event("KER-3", "Done")

        # 4. state_drift
        w4 = self.create_work("[KER-4] state drift", "done")
        self.add_linear_event("KER-4", "In Progress")

        # 5. Normal (no drift)
        w5 = self.create_work("[KER-5] normal", "claimed")
        self.add_claim(w5, "rory_build")
        self.add_linear_event("KER-5", "In Progress", "rory_build")

        # Run reconciliation
        report = self.reconciler.reconcile()

        self.assertIn(w1, report["abandoned_in_progress"])
        self.assertIn(w2, report["ownership_drift"])
        self.assertIn(w3, report["completed_but_unprojected"])
        self.assertIn(w4, report["state_drift"])

        self.assertNotIn(w5, report["abandoned_in_progress"])
        self.assertNotIn(w5, report["ownership_drift"])
        self.assertNotIn(w5, report["completed_but_unprojected"])
        self.assertNotIn(w5, report["state_drift"])

        # Run reaper
        self.reaper.reap(report)

        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        works = {r["id"]: r["status"] for r in conn.execute("SELECT id, status FROM work").fetchall()}
        claims = [r["work_id"] for r in conn.execute("SELECT work_id FROM claim").fetchall()]
        conn.close()

        # Reaper should have reset abandoned and ownership_drift works
        self.assertEqual(works[w1], "pending")
        self.assertEqual(works[w2], "pending")
        self.assertNotIn(w1, claims)
        self.assertNotIn(w2, claims)

        # Reaper should not have touched completed_but_unprojected or state_drift yet
        self.assertEqual(works[w3], "review")
        self.assertEqual(works[w4], "done")

        # Reaper should not have touched normal works
        self.assertEqual(works[w5], "claimed")
        self.assertIn(w5, claims)

if __name__ == "__main__":
    unittest.main()
