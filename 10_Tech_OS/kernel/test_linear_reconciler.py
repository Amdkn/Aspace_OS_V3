import json
import os
import sqlite3
import tempfile
import unittest

import uc
from linear_reconciler import LinearReconciler
from linear_reaper import LinearReaper


class TestLinearReconciler(unittest.TestCase):
    def setUp(self):
        self.fd, self.db_path = tempfile.mkstemp()
        uc.DB = self.db_path

        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row

        with open(os.path.join(os.path.dirname(__file__), "schema.sql"), "r") as f:
            self.conn.executescript(f.read())

        self.reconciler = LinearReconciler(self.conn)
        self.reaper = LinearReaper(self.conn)

    def tearDown(self):
        self.conn.close()
        os.close(self.fd)
        os.remove(self.db_path)

    def _create_work(self, title, status="pending", harness=None, linear_status=None, linear_assignee=None):
        self.conn.execute("INSERT INTO work(layer, title, status) VALUES('L0', ?, ?)", (title, status))
        work_id = self.conn.execute("SELECT last_insert_rowid()").fetchone()[0]

        if harness and status == "claimed":
            self.conn.execute(
                "INSERT INTO claim(work_id, harness, expires_at) VALUES(?, ?, datetime('now', '+1 hour'))",
                (work_id, harness)
            )

        if linear_status is not None or linear_assignee is not None:
            payload = {}
            if linear_status:
                payload["status"] = linear_status
            if linear_assignee:
                payload["assignee"] = linear_assignee

            self.conn.execute(
                "INSERT INTO event(work_id, kind, payload) VALUES(?, 'linear_mcp_update', ?)",
                (work_id, json.dumps(payload))
            )

        return work_id

    def test_abandoned_in_progress(self):
        w1 = self._create_work("[KER-36] Active work", status="claimed", harness="agent1", linear_status="In Progress")
        w2 = self._create_work("[KER-37] Abandoned work", status="claimed", harness="agent1", linear_status="Todo")
        w3 = self._create_work("[KER-38] Done work", status="claimed", harness="agent1", linear_status="Done") # Should not be in abandoned

        report = self.reconciler.reconcile()

        abandoned = report["abandoned_in_progress"]
        self.assertEqual(len(abandoned), 1)
        self.assertEqual(abandoned[0]["work_id"], w2)

    def test_ownership_drift(self):
        w1 = self._create_work("[KER-36] Correct owner", status="claimed", harness="agent1", linear_status="In Progress", linear_assignee="agent1")
        w2 = self._create_work("[KER-37] Wrong owner", status="claimed", harness="agent1", linear_status="In Progress", linear_assignee="agent2")

        report = self.reconciler.reconcile()

        ownership_drift = report["ownership_drift"]
        self.assertEqual(len(ownership_drift), 1)
        self.assertEqual(ownership_drift[0]["work_id"], w2)
        self.assertEqual(ownership_drift[0]["linear_assignee"], "agent2")
        self.assertEqual(ownership_drift[0]["local_harness"], "agent1")

    def test_completed_but_unprojected(self):
        w1 = self._create_work("[KER-36] Done local & linear", status="done", linear_status="Done")
        w2 = self._create_work("[KER-37] Done linear, pending local", status="pending", linear_status="Done")

        report = self.reconciler.reconcile()

        completed_unprojected = report["completed_but_unprojected"]
        self.assertEqual(len(completed_unprojected), 1)
        self.assertEqual(completed_unprojected[0]["work_id"], w2)

    def test_state_drift(self):
        w1 = self._create_work("[KER-36] Done local & linear", status="done", linear_status="Done")
        w2 = self._create_work("[KER-37] Done local, not linear", status="done", linear_status="In Progress")

        report = self.reconciler.reconcile()

        state_drift = report["state_drift"]
        self.assertEqual(len(state_drift), 1)
        self.assertEqual(state_drift[0]["work_id"], w2)

    def test_reaper(self):
        # abandoned_in_progress
        w1 = self._create_work("[KER-100] Abandoned", status="claimed", harness="agent1", linear_status="Todo")
        # ownership_drift
        w2 = self._create_work("[KER-101] Wrong owner", status="claimed", harness="agent1", linear_status="In Progress", linear_assignee="agent2")
        # should not be reaped
        w3 = self._create_work("[KER-102] OK", status="claimed", harness="agent1", linear_status="In Progress", linear_assignee="agent1")

        reaped_count = self.reaper.reap()
        self.assertEqual(reaped_count, 2)

        # Verify w1, w2 are pending and claims deleted
        w1_status = self.conn.execute("SELECT status FROM work WHERE id=?", (w1,)).fetchone()[0]
        self.assertEqual(w1_status, "pending")
        w1_claim = self.conn.execute("SELECT * FROM claim WHERE work_id=?", (w1,)).fetchone()
        self.assertIsNone(w1_claim)

        w2_status = self.conn.execute("SELECT status FROM work WHERE id=?", (w2,)).fetchone()[0]
        self.assertEqual(w2_status, "pending")
        w2_claim = self.conn.execute("SELECT * FROM claim WHERE work_id=?", (w2,)).fetchone()
        self.assertIsNone(w2_claim)

        w3_status = self.conn.execute("SELECT status FROM work WHERE id=?", (w3,)).fetchone()[0]
        self.assertEqual(w3_status, "claimed")
        w3_claim = self.conn.execute("SELECT * FROM claim WHERE work_id=?", (w3,)).fetchone()
        self.assertIsNotNone(w3_claim)

        # Verify reap events were logged
        events = self.conn.execute("SELECT payload FROM event WHERE work_id=? AND kind='reap'", (w1,)).fetchall()
        self.assertEqual(len(events), 1)
        payload = json.loads(events[0]["payload"])
        self.assertEqual(payload["reason"], "abandoned_in_progress")

        events = self.conn.execute("SELECT payload FROM event WHERE work_id=? AND kind='reap'", (w2,)).fetchall()
        self.assertEqual(len(events), 1)
        payload = json.loads(events[0]["payload"])
        self.assertEqual(payload["reason"], "ownership_drift")

if __name__ == '__main__':
    unittest.main()
