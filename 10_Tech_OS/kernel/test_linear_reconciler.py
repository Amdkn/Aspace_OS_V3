import json
import os
import sqlite3
import tempfile
import unittest
import subprocess
import sys
import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from linear_reconciler import LinearReconciler
from linear_reaper import LinearReaper
UC_PATH = os.path.join(HERE, "uc.py")

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

    def add_work(self, layer, title, status='pending'):
        conn = sqlite3.connect(self.db_path)
        cur = conn.execute(
            "INSERT INTO work(layer, title, status) VALUES(?, ?, ?)",
            (layer, title, status)
        )
        work_id = cur.lastrowid
        conn.commit()
        conn.close()
        return work_id

    def add_claim(self, work_id, harness, expires_in_seconds):
        conn = sqlite3.connect(self.db_path)
        now = datetime.datetime.now(datetime.timezone.utc)
        expires_at = now + datetime.timedelta(seconds=expires_in_seconds)
        conn.execute(
            "INSERT INTO claim(work_id, harness, expires_at) VALUES(?, ?, ?)",
            (work_id, harness, expires_at.strftime("%Y-%m-%d %H:%M:%S"))
        )
        conn.execute("UPDATE work SET status='claimed' WHERE id=?", (work_id,))
        conn.commit()
        conn.close()

    def add_event_linear_update(self, issues):
        conn = sqlite3.connect(self.db_path)
        payload = {"issues": issues}
        conn.execute(
            "INSERT INTO event(kind, payload) VALUES('linear_mcp_update', ?)",
            (json.dumps(payload),)
        )
        conn.commit()
        conn.close()

    def test_abandoned_in_progress_pending(self):
        work_id = self.add_work("L0", "[KER-100] Task title", "pending")
        self.add_event_linear_update([
            {"id": "KER-100", "status": "In Progress", "assignee": "Alice"}
        ])

        report = self.reconciler.reconcile()
        self.assertEqual(len(report["abandoned_in_progress"]), 1)
        self.assertEqual(report["abandoned_in_progress"][0]["work_id"], work_id)

        self.reaper.reap(report)
        conn = sqlite3.connect(self.db_path)
        status = conn.execute("SELECT status FROM work WHERE id=?", (work_id,)).fetchone()[0]
        self.assertEqual(status, "pending")
        conn.close()

    def test_abandoned_in_progress_expired_claim(self):
        work_id = self.add_work("L0", "[KER-101] Task title", "claimed")
        self.add_claim(work_id, "Alice", -3600) # expired 1 hour ago
        self.add_event_linear_update([
            {"id": "KER-101", "status": "In Progress", "assignee": "Alice"}
        ])

        report = self.reconciler.reconcile()
        self.assertEqual(len(report["abandoned_in_progress"]), 1)
        self.assertEqual(report["abandoned_in_progress"][0]["work_id"], work_id)

        self.reaper.reap(report)
        conn = sqlite3.connect(self.db_path)
        status = conn.execute("SELECT status FROM work WHERE id=?", (work_id,)).fetchone()[0]
        claim_count = conn.execute("SELECT COUNT(*) FROM claim WHERE work_id=?", (work_id,)).fetchone()[0]
        event_count = conn.execute("SELECT COUNT(*) FROM event WHERE kind='linear_reaper_resolution'").fetchone()[0]
        self.assertEqual(status, "pending")
        self.assertEqual(claim_count, 0)
        self.assertEqual(event_count, 1)
        conn.close()

    def test_completed_but_unprojected(self):
        work_id = self.add_work("L0", "[KER-102] Task title", "claimed")
        self.add_claim(work_id, "Alice", 3600)
        self.add_event_linear_update([
            {"id": "KER-102", "status": "Done", "assignee": "Alice"}
        ])

        report = self.reconciler.reconcile()
        self.assertEqual(len(report["completed_but_unprojected"]), 1)
        self.assertEqual(report["completed_but_unprojected"][0]["work_id"], work_id)

        self.reaper.reap(report)
        # Reaper should not touch this
        conn = sqlite3.connect(self.db_path)
        status = conn.execute("SELECT status FROM work WHERE id=?", (work_id,)).fetchone()[0]
        self.assertEqual(status, "claimed")
        conn.close()

    def test_state_drift(self):
        # We need a valid prediction to transition to done
        conn = sqlite3.connect(self.db_path)
        cur = conn.execute(
            "INSERT INTO work(layer, title, status) VALUES('L0', '[KER-103] Task', 'pending')"
        )
        work_id = cur.lastrowid
        conn.execute("INSERT INTO prediction(work_id, claim_text, confidence) VALUES(?, 'pred', 0.9)", (work_id,))
        conn.execute("UPDATE work SET status='review' WHERE id=?", (work_id,))
        conn.execute("UPDATE work SET status='done' WHERE id=?", (work_id,))
        conn.commit()
        conn.close()

        self.add_event_linear_update([
            {"id": "KER-103", "status": "In Progress", "assignee": "Alice"}
        ])

        report = self.reconciler.reconcile()
        self.assertEqual(len(report["state_drift"]), 1)
        self.assertEqual(report["state_drift"][0]["work_id"], work_id)

        self.reaper.reap(report)
        # Reaper should not touch this
        conn = sqlite3.connect(self.db_path)
        status = conn.execute("SELECT status FROM work WHERE id=?", (work_id,)).fetchone()[0]
        self.assertEqual(status, "done")
        conn.close()

    def test_ownership_drift(self):
        work_id = self.add_work("L0", "[KER-104] Task title", "claimed")
        self.add_claim(work_id, "Bob", 3600) # Valid claim by Bob
        self.add_event_linear_update([
            {"id": "KER-104", "status": "In Progress", "assignee": "Alice"} # Assigned to Alice in Linear
        ])

        report = self.reconciler.reconcile()
        self.assertEqual(len(report["ownership_drift"]), 1)
        self.assertEqual(report["ownership_drift"][0]["work_id"], work_id)

        self.reaper.reap(report)
        conn = sqlite3.connect(self.db_path)
        status = conn.execute("SELECT status FROM work WHERE id=?", (work_id,)).fetchone()[0]
        claim_count = conn.execute("SELECT COUNT(*) FROM claim WHERE work_id=?", (work_id,)).fetchone()[0]
        self.assertEqual(status, "pending")
        self.assertEqual(claim_count, 0)
        conn.close()

if __name__ == "__main__":
    unittest.main()
