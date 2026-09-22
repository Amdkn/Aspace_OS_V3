import json
import os
import sqlite3
import tempfile
import unittest

from linear_reconciler import LinearReconciler
from linear_reaper import LinearReaper

class TestLinearReconciler(unittest.TestCase):
    def setUp(self):
        self.fd, self.db_path = tempfile.mkstemp()

        os.environ['ASPACE_DB'] = self.db_path
        import uc
        uc.DB = self.db_path

        self.conn = sqlite3.connect(self.db_path, isolation_level=None)
        self.c = self.conn.cursor()
        self._init_db()

    def tearDown(self):
        self.conn.close()
        os.close(self.fd)
        os.remove(self.db_path)

    def _init_db(self):
        self.c.executescript("""
            CREATE TABLE tape (
                id INTEGER PRIMARY KEY, path TEXT UNIQUE, sha256 TEXT, created_at TEXT
            );
            CREATE TABLE work (
                id INTEGER PRIMARY KEY,
                tape_id INTEGER REFERENCES tape(id),
                layer TEXT NOT NULL,
                title TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'pending',
                wake_at TEXT,
                priority INTEGER NOT NULL DEFAULT 0,
                parent_id INTEGER,
                attempts INTEGER NOT NULL DEFAULT 0,
                created_at TEXT,
                updated_at TEXT
            );
            CREATE TABLE claim (
                work_id INTEGER PRIMARY KEY REFERENCES work(id) ON DELETE CASCADE,
                harness TEXT NOT NULL,
                claimed_at TEXT,
                expires_at TEXT NOT NULL
            );
            CREATE TABLE prediction (
                id INTEGER PRIMARY KEY,
                work_id INTEGER NOT NULL REFERENCES work(id) ON DELETE CASCADE,
                claim_text TEXT NOT NULL,
                confidence REAL NOT NULL,
                predicted_at TEXT,
                outcome INTEGER,
                scored_at TEXT
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

    def _insert_work(self, layer, title, status):
        self.c.execute("INSERT INTO work (layer, title, status) VALUES (?, ?, ?)", (layer, title, status))
        return self.c.lastrowid

    def _insert_claim(self, work_id, harness):
        self.c.execute("INSERT INTO claim (work_id, harness, expires_at) VALUES (?, ?, '2099-01-01')", (work_id, harness))

    def _insert_linear_event(self, issue_id, status, assignee):
        payload = json.dumps({"issue_id": issue_id, "status": status, "assignee": assignee})
        self.c.execute("INSERT INTO event (kind, payload) VALUES ('linear_mcp_update', ?)", (payload,))

    def test_abandoned_in_progress(self):
        w_id = self._insert_work('L0', '[KER-1] Test task', 'claimed')
        self._insert_claim(w_id, 'amy')
        self._insert_linear_event('KER-1', 'todo', 'amy')

        rec = LinearReconciler(self.db_path)
        report = rec.reconcile()

        self.assertIn(w_id, report['abandoned_in_progress'])
        self.assertEqual(len(report['abandoned_in_progress']), 1)

    def test_ownership_drift(self):
        w_id = self._insert_work('L0', '[KER-2] Another task', 'claimed')
        self._insert_claim(w_id, 'amy')
        self._insert_linear_event('KER-2', 'in progress', 'rory')

        rec = LinearReconciler(self.db_path)
        report = rec.reconcile()

        self.assertIn(w_id, report['ownership_drift'])
        self.assertEqual(len(report['ownership_drift']), 1)

    def test_completed_but_unprojected(self):
        w_id = self._insert_work('L0', '[KER-3] Done task', 'claimed')
        self._insert_claim(w_id, 'amy')
        self._insert_linear_event('KER-3', 'done', 'amy')

        rec = LinearReconciler(self.db_path)
        report = rec.reconcile()

        self.assertIn(w_id, report['completed_but_unprojected'])
        self.assertEqual(len(report['completed_but_unprojected']), 1)

    def test_state_drift(self):
        w_id = self._insert_work('L0', '[KER-4] Drift task', 'done')
        self._insert_linear_event('KER-4', 'in progress', 'amy')

        rec = LinearReconciler(self.db_path)
        report = rec.reconcile()

        self.assertIn(w_id, report['state_drift'])
        self.assertEqual(len(report['state_drift']), 1)

    def test_reaper_resets_abandoned(self):
        w_id = self._insert_work('L0', '[KER-5] Abandoned task', 'claimed')
        self._insert_claim(w_id, 'amy')
        self._insert_linear_event('KER-5', 'todo', 'amy')

        rec = LinearReconciler(self.db_path)
        report = rec.reconcile()

        reaper = LinearReaper(self.db_path)
        reaped_count = reaper.reap(report)
        self.assertEqual(reaped_count, 1)

        self.c.execute("SELECT status FROM work WHERE id = ?", (w_id,))
        status = self.c.fetchone()[0]
        self.assertEqual(status, 'pending')

        self.c.execute("SELECT count(*) FROM claim WHERE work_id = ?", (w_id,))
        claim_count = self.c.fetchone()[0]
        self.assertEqual(claim_count, 0)

    def test_reaper_resets_ownership_drift(self):
        w_id = self._insert_work('L0', '[KER-6] Ownership drift task', 'claimed')
        self._insert_claim(w_id, 'amy')
        self._insert_linear_event('KER-6', 'in progress', 'rory')

        rec = LinearReconciler(self.db_path)
        report = rec.reconcile()

        reaper = LinearReaper(self.db_path)
        reaped_count = reaper.reap(report)
        self.assertEqual(reaped_count, 1)

        self.c.execute("SELECT status FROM work WHERE id = ?", (w_id,))
        status = self.c.fetchone()[0]
        self.assertEqual(status, 'pending')

        self.c.execute("SELECT count(*) FROM claim WHERE work_id = ?", (w_id,))
        claim_count = self.c.fetchone()[0]
        self.assertEqual(claim_count, 0)

if __name__ == '__main__':
    unittest.main()
