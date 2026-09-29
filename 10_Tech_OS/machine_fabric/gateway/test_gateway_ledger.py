import unittest
import tempfile
import sqlite3
import os
import sys
from pathlib import Path

# Add parent directory to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gateway import UsageLedger

class TestUsageLedger(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.temp_dir.name, "test_ledger.sqlite3")
        self.ledger = UsageLedger(self.db_path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_schema_created(self):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tool_calls'")
            self.assertIsNotNone(cur.fetchone())

    def test_record_call(self):
        self.ledger.record_call("amf_execute", 15.5, "SUCCEEDED", operation_id="test-op-1", capability="machine.fs.read")

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.execute("SELECT * FROM tool_calls WHERE operation_id='test-op-1'")
            row = cur.fetchone()
            self.assertIsNotNone(row)
            self.assertEqual(row['tool_name'], "amf_execute")
            self.assertEqual(row['latency_ms'], 15.5)
            self.assertEqual(row['state'], "SUCCEEDED")
            self.assertEqual(row['is_replay'], 0)
            self.assertEqual(row['effect_new'], 1)

    def test_has_operation(self):
        self.assertFalse(self.ledger.has_operation("op-2"))
        self.ledger.record_call("amf_execute", 10.0, "SUCCEEDED", operation_id="op-2")
        self.assertTrue(self.ledger.has_operation("op-2"))

    def test_record_replay(self):
        # Initial call
        self.ledger.record_call("amf_execute", 10.0, "SUCCEEDED", operation_id="op-replay", effect_new=True)
        # Replay call
        self.ledger.record_call("amf_execute", 5.0, "SUCCEEDED", operation_id="op-replay", is_replay=True, effect_new=False)

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.execute("SELECT * FROM tool_calls WHERE operation_id='op-replay' ORDER BY invocation_id")
            rows = cur.fetchall()
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]['effect_new'], 1)
            self.assertEqual(rows[1]['effect_new'], 0)
            self.assertEqual(rows[1]['is_replay'], 1)

    def test_tool_inventory(self):
        self.ledger.record_call("amf_health", 2.0, "SUCCEEDED", effect_new=False)
        self.ledger.record_call("amf_health", 4.0, "SUCCEEDED", effect_new=False)
        self.ledger.record_call("amf_execute", 10.0, "SUCCEEDED")

        inventory = self.ledger.get_tool_inventory()
        self.assertEqual(len(inventory), 2)

        health_stat = next(i for i in inventory if i['tool'] == 'amf_health')
        self.assertEqual(health_stat['count'], 2)
        self.assertEqual(health_stat['avg_latency'], 3.0)

    def test_bounded_retention(self):
        # Insert 10005 records
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("BEGIN TRANSACTION")
            for i in range(10005):
                conn.execute(
                    "INSERT INTO tool_calls (tool_name, timestamp, latency_ms, state, is_replay, effect_new) VALUES (?, ?, ?, ?, ?, ?)",
                    ("test_tool", "2023-01-01T00:00:00", 1.0, "SUCCEEDED", 0, 1)
                )
            conn.commit()

        # The trigger should limit to 10000
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.execute("SELECT COUNT(*) FROM tool_calls")
            count = cur.fetchone()[0]
            self.assertEqual(count, 10000)

if __name__ == '__main__':
    unittest.main()
