import sys
import os
import sqlite3
import json
import unittest
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
from linear_reconciler import LinearReconciler

class TestLinearReconciler(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.temp_dir.name, 'test.db')
        self.conn = sqlite3.connect(self.db_path)
        with open(os.path.join(HERE, 'schema.sql')) as f:
            self.conn.executescript(f.read())

        # Add some work items
        self.conn.execute("INSERT INTO work (id, layer, title, status) VALUES (1, 'L0', '[KER-1] Test task 1', 'pending')")
        self.conn.execute("INSERT INTO work (id, layer, title, status) VALUES (2, 'L0', '[KER-2] Test task 2', 'pending')")
        self.conn.execute("INSERT INTO work (id, layer, title, status) VALUES (3, 'L0', '[KER-3] Test task 3', 'claimed')")
        self.conn.execute("INSERT INTO work (id, layer, title, status) VALUES (4, 'L0', '[KER-4] Test task 4', 'pending')")

        self.conn.execute("INSERT INTO prediction (work_id, claim_text, confidence) VALUES (4, 'test', 0.9)")
        self.conn.execute("UPDATE work SET status='review' WHERE id=4")
        self.conn.execute("UPDATE work SET status='done' WHERE id=4")

        self.conn.execute("INSERT INTO claim (work_id, harness, expires_at) VALUES (3, 'jules', '2099-01-01')")
        self.conn.commit()

    def tearDown(self):
        self.conn.close()
        self.temp_dir.cleanup()

    def test_reconcile(self):
        linear_data = {
            "issues": [
                {"id": "KER-1", "status": "Done"},
                {"id": "KER-2", "status": "In Progress"},
                {"id": "KER-3", "status": "Todo", "assignee": "rick"},
                {"id": "KER-4", "status": "Todo"}
            ]
        }
        self.conn.execute("INSERT INTO event (kind, payload) VALUES ('linear_mcp_update', ?)", (json.dumps(linear_data),))
        self.conn.commit()

        reconciler = LinearReconciler(self.db_path)
        report = reconciler.reconcile()

        self.assertTrue(any(i['issue_id'] == 'KER-1' for i in report['completed_but_unprojected']))
        self.assertTrue(any(i['issue_id'] == 'KER-2' for i in report['abandoned_in_progress']))
        self.assertTrue(any(i['issue_id'] == 'KER-4' for i in report['state_drift']))
        self.assertTrue(any(i['issue_id'] == 'KER-3' for i in report['ownership_drift']))

if __name__ == '__main__':
    unittest.main()
