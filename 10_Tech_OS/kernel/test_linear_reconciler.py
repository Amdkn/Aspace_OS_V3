import unittest
import os
import sqlite3
import json
import tempfile
import sys

from linear_reconciler import LinearReconciler
from linear_reaper import LinearReaper

class TestLinearReconciliation(unittest.TestCase):
    def setUp(self):
        # Create a temporary database file
        self.db_fd, self.db_path = tempfile.mkstemp(suffix=".db")

        # Override ASPACE_DB for the system
        os.environ["ASPACE_DB"] = self.db_path

        self.conn = sqlite3.connect(self.db_path)
        self._init_db()

    def tearDown(self):
        self.conn.close()
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def _init_db(self):
        # Basic schema needed for tests
        self.conn.executescript("""
            CREATE TABLE tape (
              id INTEGER PRIMARY KEY,
              path TEXT NOT NULL UNIQUE,
              sha256 TEXT NOT NULL,
              created_at TEXT NOT NULL DEFAULT (datetime('now'))
            );
            CREATE TABLE work (
              id INTEGER PRIMARY KEY,
              tape_id INTEGER REFERENCES tape(id),
              layer TEXT NOT NULL,
              title TEXT NOT NULL,
              status TEXT NOT NULL DEFAULT 'pending'
            );
            CREATE TABLE claim (
              work_id INTEGER PRIMARY KEY REFERENCES work(id) ON DELETE CASCADE,
              harness TEXT NOT NULL,
              claimed_at TEXT NOT NULL DEFAULT (datetime('now')),
              expires_at TEXT NOT NULL
            );
            CREATE TABLE event (
              id INTEGER PRIMARY KEY,
              work_id INTEGER REFERENCES work(id) ON DELETE CASCADE,
              harness TEXT,
              kind TEXT NOT NULL,
              payload TEXT,
              at TEXT NOT NULL DEFAULT (datetime('now'))
            );
        """)

    def _insert_linear_event(self, issues):
        payload = json.dumps({"issues": issues})
        self.conn.execute("INSERT INTO event(kind, payload) VALUES('linear_mcp_update', ?)", (payload,))
        self.conn.commit()

    def test_abandoned_in_progress(self):
        # Local claimed, Linear is not in progress
        self.conn.execute("INSERT INTO work(id, layer, title, status) VALUES(1, 'L0', '[KER-100] Task A', 'claimed')")
        self.conn.execute("INSERT INTO claim(work_id, harness, expires_at) VALUES(1, 'jules', '2099-01-01')")
        self.conn.commit()

        self._insert_linear_event([
            {"id": "KER-100", "status": "Todo", "assignee": "jules"}
        ])

        reconciler = LinearReconciler(self.db_path)
        report = reconciler.reconcile()

        self.assertIn(1, report["abandoned_in_progress"])
        self.assertEqual(len(report["abandoned_in_progress"]), 1)
        self.assertEqual(len(report["completed_but_unprojected"]), 0)
        self.assertEqual(len(report["state_drift"]), 0)
        self.assertEqual(len(report["ownership_drift"]), 0)

    def test_completed_but_unprojected(self):
        # Linear done, Local not done
        self.conn.execute("INSERT INTO work(id, layer, title, status) VALUES(2, 'L0', '[KER-101] Task B', 'claimed')")
        self.conn.execute("INSERT INTO claim(work_id, harness, expires_at) VALUES(2, 'jules', '2099-01-01')")
        self.conn.commit()

        self._insert_linear_event([
            {"id": "KER-101", "status": "Done", "assignee": "jules"}
        ])

        reconciler = LinearReconciler(self.db_path)
        report = reconciler.reconcile()

        self.assertIn(2, report["completed_but_unprojected"])

    def test_state_drift(self):
        # Local done, Linear not done
        self.conn.execute("INSERT INTO work(id, layer, title, status) VALUES(3, 'L0', '[KER-102] Task C', 'done')")
        self.conn.commit()

        self._insert_linear_event([
            {"id": "KER-102", "status": "In Progress", "assignee": "jules"}
        ])

        reconciler = LinearReconciler(self.db_path)
        report = reconciler.reconcile()

        self.assertIn(3, report["state_drift"])

    def test_ownership_drift(self):
        # Local claimed, Linear in progress, assignee mismatch
        self.conn.execute("INSERT INTO work(id, layer, title, status) VALUES(4, 'L0', '[KER-103] Task D', 'claimed')")
        self.conn.execute("INSERT INTO claim(work_id, harness, expires_at) VALUES(4, 'rick', '2099-01-01')")
        self.conn.commit()

        self._insert_linear_event([
            {"id": "KER-103", "status": "In Progress", "assignee": "jules"}
        ])

        reconciler = LinearReconciler(self.db_path)
        report = reconciler.reconcile()

        self.assertIn(4, report["ownership_drift"])

    def test_linear_reaper(self):
        # Setup conditions for abandoned_in_progress and ownership_drift
        self.conn.execute("INSERT INTO work(id, layer, title, status) VALUES(10, 'L0', '[KER-200] Abnd', 'claimed')")
        self.conn.execute("INSERT INTO claim(work_id, harness, expires_at) VALUES(10, 'jules', '2099-01-01')")

        self.conn.execute("INSERT INTO work(id, layer, title, status) VALUES(11, 'L0', '[KER-201] OwnDrift', 'claimed')")
        self.conn.execute("INSERT INTO claim(work_id, harness, expires_at) VALUES(11, 'rick', '2099-01-01')")

        self.conn.commit()

        self._insert_linear_event([
            {"id": "KER-200", "status": "Todo", "assignee": "jules"},
            {"id": "KER-201", "status": "In Progress", "assignee": "jules"}
        ])

        reaper = LinearReaper(self.db_path)
        result = reaper.reap()

        self.assertEqual(result["reset_count"], 2)
        self.assertIn(10, result["reset_items"])
        self.assertIn(11, result["reset_items"])

        # Check DB state
        c = self.conn.cursor()

        work_10 = c.execute("SELECT status FROM work WHERE id=10").fetchone()
        self.assertEqual(work_10[0], "pending")
        claim_10 = c.execute("SELECT * FROM claim WHERE work_id=10").fetchone()
        self.assertIsNone(claim_10)

        work_11 = c.execute("SELECT status FROM work WHERE id=11").fetchone()
        self.assertEqual(work_11[0], "pending")
        claim_11 = c.execute("SELECT * FROM claim WHERE work_id=11").fetchone()
        self.assertIsNone(claim_11)

if __name__ == "__main__":
    unittest.main()
