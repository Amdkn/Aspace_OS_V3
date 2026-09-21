import sys
import os
import sqlite3
import json
import unittest
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from linear_reaper import LinearReaper

class TestLinearReaper(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.temp_dir.name, 'test.db')
        self.conn = sqlite3.connect(self.db_path)
        with open(os.path.join(HERE, 'schema.sql')) as f:
            self.conn.executescript(f.read())

        # Insert a drift scenario
        self.conn.execute("INSERT INTO work (id, layer, title, status) VALUES (2, 'L0', '[KER-2] Test task 2', 'pending')") # abandoned_in_progress
        self.conn.execute("INSERT INTO work (id, layer, title, status) VALUES (3, 'L0', '[KER-3] Test task 3', 'claimed')") # ownership_drift

        self.conn.execute("INSERT INTO claim (work_id, harness, expires_at) VALUES (3, 'jules', '2099-01-01')")

        linear_data = {
            "issues": [
                {"id": "KER-2", "status": "In Progress"},
                {"id": "KER-3", "status": "Todo", "assignee": "rick"},
            ]
        }
        self.conn.execute("INSERT INTO event (kind, payload) VALUES ('linear_mcp_update', ?)", (json.dumps(linear_data),))
        self.conn.commit()

    def tearDown(self):
        self.conn.close()
        self.temp_dir.cleanup()

    def test_reaper(self):
        reaper = LinearReaper(self.db_path)
        res = reaper.reap()

        self.assertTrue(res["ok"])
        self.assertIn(2, res["reaped"])
        self.assertIn(3, res["reaped"])

        # Verify db state
        cur = self.conn.cursor()
        cur.execute("SELECT status FROM work WHERE id = 3")
        self.assertEqual(cur.fetchone()[0], "pending")

        cur.execute("SELECT count(*) FROM claim WHERE work_id = 3")
        self.assertEqual(cur.fetchone()[0], 0)

if __name__ == '__main__':
    unittest.main()
