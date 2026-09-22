import unittest
import sqlite3
import os
import json
from linear_reconciler import LinearReconciler
from linear_reaper import LinearReaper

class TestLinearReconcilerAndReaper(unittest.TestCase):
    def setUp(self):
        self.db_path = 'test_reconciler.db'
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

        with open('10_Tech_OS/kernel/schema.sql', 'r') as f:
            self.cursor.executescript(f.read())

        # Insert test data
        self.cursor.execute("INSERT INTO work (id, layer, title, status) VALUES (1, 'L0', '[KER-1] Abandoned', 'claimed')")
        self.cursor.execute("INSERT INTO claim (work_id, harness, expires_at) VALUES (1, 'jules', datetime('now', '+1 hour'))")
        self.cursor.execute("INSERT INTO event (work_id, kind, payload) VALUES (1, 'linear_mcp_update', '{\"status\": \"Todo\"}')")

        self.cursor.execute("INSERT INTO work (id, layer, title, status) VALUES (2, 'L0', '[KER-2] Ownership Drift', 'claimed')")
        self.cursor.execute("INSERT INTO claim (work_id, harness, expires_at) VALUES (2, 'jules', datetime('now', '+1 hour'))")
        self.cursor.execute("INSERT INTO event (work_id, kind, payload) VALUES (2, 'linear_mcp_update', '{\"status\": \"In Progress\", \"assignee\": \"rick\"}')")

        self.cursor.execute("INSERT INTO work (id, layer, title, status) VALUES (3, 'L0', '[KER-3] State Drift', 'done')")
        self.cursor.execute("INSERT INTO event (work_id, kind, payload) VALUES (3, 'linear_mcp_update', '{\"status\": \"In Progress\"}')")

        self.cursor.execute("INSERT INTO work (id, layer, title, status) VALUES (4, 'L0', '[KER-4] Completed Unprojected', 'claimed')")
        self.cursor.execute("INSERT INTO claim (work_id, harness, expires_at) VALUES (4, 'jules', datetime('now', '+1 hour'))")
        self.cursor.execute("INSERT INTO event (work_id, kind, payload) VALUES (4, 'linear_mcp_update', '{\"status\": \"Done\"}')")

        self.conn.commit()

    def tearDown(self):
        self.conn.close()
        os.remove(self.db_path)

    def test_reconciler(self):
        reconciler = LinearReconciler(self.cursor)
        drifts = reconciler.reconcile()

        drift_types = {d['drift_type']: d['work_id'] for d in drifts}

        self.assertIn('abandoned_in_progress', drift_types)
        self.assertEqual(drift_types['abandoned_in_progress'], 1)

        self.assertIn('ownership_drift', drift_types)
        self.assertEqual(drift_types['ownership_drift'], 2)

        self.assertIn('state_drift', drift_types)
        self.assertEqual(drift_types['state_drift'], 3)

        self.assertIn('completed_but_unprojected', drift_types)
        self.assertEqual(drift_types['completed_but_unprojected'], 4)

    def test_reaper(self):
        reaper = LinearReaper(self.cursor)
        resolved = reaper.reap()
        self.conn.commit()

        resolved_types = [r['drift_type'] for r in resolved]
        self.assertIn('abandoned_in_progress', resolved_types)
        self.assertIn('ownership_drift', resolved_types)

        # Check if they were actually reset to pending
        self.cursor.execute("SELECT status FROM work WHERE id IN (1, 2)")
        statuses = [row[0] for row in self.cursor.fetchall()]
        self.assertEqual(statuses, ['pending', 'pending'])

        # Check if claims were deleted
        self.cursor.execute("SELECT COUNT(*) FROM claim WHERE work_id IN (1, 2)")
        count = self.cursor.fetchone()[0]
        self.assertEqual(count, 0)

        # Check if events were logged
        self.cursor.execute("SELECT payload FROM event WHERE work_id=1 AND kind='reap'")
        payload = json.loads(self.cursor.fetchone()[0])
        self.assertEqual(payload['reason'], 'abandoned_in_progress')

if __name__ == '__main__':
    unittest.main()
