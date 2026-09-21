import unittest
import sqlite3
import tempfile
import os
import json
from linear_reaper import run_reconciliation

class TestLinearReaper(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test_uc.db")

        # Setup schema
        with open(os.path.join(os.path.dirname(__file__), "schema.sql"), "r") as f:
            schema_sql = f.read()

        conn = sqlite3.connect(self.db_path)
        conn.executescript(schema_sql)
        self.conn = conn

    def tearDown(self):
        self.conn.close()
        self.tmp_dir.cleanup()

    def add_work(self, layer, title, status):
        cursor = self.conn.cursor()
        # insert required fields
        cursor.execute("INSERT INTO work(layer, title, status) VALUES(?, ?, ?)", (layer, title, status))
        self.conn.commit()
        return cursor.lastrowid

    def test_abandoned_in_progress(self):
        self.add_work("L0", "Test Task 1", "pending")

        linear_state = [
            {"title": "Test Task 1", "status": "In Progress"}
        ]

        report = run_reconciliation(self.db_path, linear_state)

        self.assertEqual(len(report["abandoned_in_progress"]), 1)
        self.assertEqual(report["abandoned_in_progress"][0]["title"], "Test Task 1")

    def test_completed_but_unprojected(self):
        self.add_work("L0", "Test Task 2", "done")

        linear_state = [
            {"title": "Test Task 2", "status": "In Progress"}
        ]

        report = run_reconciliation(self.db_path, linear_state)

        self.assertEqual(len(report["completed_but_unprojected"]), 1)
        self.assertEqual(report["completed_but_unprojected"][0]["title"], "Test Task 2")

    def test_drift(self):
        self.add_work("L0", "Test Task 3", "claimed")

        linear_state = [
            {"title": "Test Task 3", "status": "Done"}
        ]

        report = run_reconciliation(self.db_path, linear_state)

        self.assertEqual(len(report["drift"]), 1)
        self.assertEqual(report["drift"][0]["title"], "Test Task 3")

    def test_clean_state(self):
        self.add_work("L0", "Test Task 4", "done")
        self.add_work("L0", "Test Task 5", "claimed")
        self.add_work("L0", "Test Task 6", "pending")

        linear_state = [
            {"title": "Test Task 4", "status": "Done"},
            {"title": "Test Task 5", "status": "In Progress"},
            {"title": "Test Task 6", "status": "Todo"}
        ]

        report = run_reconciliation(self.db_path, linear_state)

        self.assertEqual(len(report["abandoned_in_progress"]), 0)
        self.assertEqual(len(report["completed_but_unprojected"]), 0)
        self.assertEqual(len(report["drift"]), 0)

if __name__ == "__main__":
    unittest.main()
