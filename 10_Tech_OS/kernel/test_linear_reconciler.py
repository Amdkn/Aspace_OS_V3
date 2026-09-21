import json
import os
import sqlite3
import tempfile
import unittest
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from linear_reconciler import LinearReconciler
from linear_reaper import LinearReaper
import uc

class TestLinearReconciliation(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test_uc.db")

        # Override ASPACE_DB and DB for uc module
        os.environ["ASPACE_DB"] = self.db_path
        uc.DB = self.db_path

        # Init DB schema
        class DummyArgs:
            pass
        uc.cmd_init(DummyArgs())

    def tearDown(self):
        self.tmp_dir.cleanup()

    def _add_work(self, layer, title, status="pending"):
        conn = sqlite3.connect(self.db_path)
        cur = conn.execute("INSERT INTO work(layer, title, status) VALUES(?, ?, ?)", (layer, title, status))
        work_id = cur.lastrowid
        conn.commit()
        conn.close()
        return work_id

    def _add_claim(self, work_id, harness):
        conn = sqlite3.connect(self.db_path)
        conn.execute("INSERT INTO claim(work_id, harness, expires_at) VALUES(?, ?, datetime('now', '+1 hour'))", (work_id, harness))
        conn.commit()
        conn.close()

    def _add_linear_event(self, issue_id, status, assignee=None):
        conn = sqlite3.connect(self.db_path)
        payload = {"issue_id": issue_id, "status": status}
        if assignee:
             payload["assignee"] = assignee
        conn.execute("INSERT INTO event(kind, payload) VALUES('linear_mcp_update', ?)", (json.dumps(payload),))
        conn.commit()
        conn.close()

    def test_abandoned_in_progress(self):
        w1 = self._add_work("L0", "[KER-36] test task", "pending")
        self._add_linear_event("KER-36", "In Progress", "jules")

        reconciler = LinearReconciler(self.db_path)
        report = reconciler.reconcile()

        self.assertEqual(len(report["abandoned_in_progress"]), 1)
        self.assertEqual(report["abandoned_in_progress"][0]["work_id"], w1)

    def test_ownership_drift(self):
        w1 = self._add_work("L0", "[KER-37] test task 2", "claimed")
        self._add_claim(w1, "amy")

        self._add_linear_event("KER-37", "In Progress", "rory")

        reconciler = LinearReconciler(self.db_path)
        report = reconciler.reconcile()

        self.assertEqual(len(report["ownership_drift"]), 1)
        self.assertEqual(report["ownership_drift"][0]["work_id"], w1)

    def test_completed_but_unprojected(self):
        w1 = self._add_work("L0", "[KER-38] test task 3", "claimed")
        self._add_claim(w1, "jules")
        self._add_linear_event("KER-38", "Done")

        reconciler = LinearReconciler(self.db_path)
        report = reconciler.reconcile()

        self.assertEqual(len(report["completed_but_unprojected"]), 1)
        self.assertEqual(report["completed_but_unprojected"][0]["work_id"], w1)

    def test_state_drift(self):
        w1 = self._add_work("L0", "[KER-39] test task 4", "review")
        self._add_linear_event("KER-39", "In Progress", "jules")
        self._add_claim(w1, "jules") # Owner matches, but it's review in DB, In Progress in linear

        # Wait, if Linear is "In Progress" but DB is "review", that's state_drift ?
        # My logic says: if linear_status == "In Progress":
        # if work_status in ("pending", "waiting") or not claim_harness: -> abandoned
        # elif linear_assignee and claim_harness and linear_assignee != claim_harness: -> ownership_drift
        # elif work_status not in ("claimed", "review"): -> state_drift
        # Actually it's fine for it to be in review and in progress.

        # We cannot just set it to 'done' without prediction because of the trigger loi_prediction_prealable
        # Let's just create a new one that doesn't trigger the constraint, or add a prediction first
        conn = sqlite3.connect(self.db_path)
        conn.execute("INSERT INTO prediction(work_id, claim_text, confidence) VALUES(?, 'test', 0.9)", (w1,))
        conn.execute("UPDATE work SET status='done' WHERE id=?", (w1,))
        conn.commit()
        conn.close()

        reconciler = LinearReconciler(self.db_path)
        report = reconciler.reconcile()

        self.assertEqual(len(report["state_drift"]), 1)
        self.assertEqual(report["state_drift"][0]["work_id"], w1)

    def test_reaper(self):
        w1 = self._add_work("L0", "[KER-40] abandoned task", "pending")
        self._add_linear_event("KER-40", "In Progress", "jules")

        w2 = self._add_work("L0", "[KER-41] drifted ownership", "claimed")
        self._add_claim(w2, "amy")
        self._add_linear_event("KER-41", "In Progress", "rory")

        w3 = self._add_work("L0", "[KER-42] good task", "claimed")
        self._add_claim(w3, "jules")
        self._add_linear_event("KER-42", "In Progress", "jules")

        reconciler = LinearReconciler(self.db_path)
        report = reconciler.reconcile()

        reaper = LinearReaper(self.db_path)
        count = reaper.reap(report)
        self.assertEqual(count, 2)

        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        w1_row = conn.execute("SELECT status FROM work WHERE id=?", (w1,)).fetchone()
        self.assertEqual(w1_row["status"], "pending")

        w2_row = conn.execute("SELECT status FROM work WHERE id=?", (w2,)).fetchone()
        self.assertEqual(w2_row["status"], "pending")
        claim2_row = conn.execute("SELECT * FROM claim WHERE work_id=?", (w2,)).fetchone()
        self.assertIsNone(claim2_row)

        w3_row = conn.execute("SELECT status FROM work WHERE id=?", (w3,)).fetchone()
        self.assertEqual(w3_row["status"], "claimed")
        claim3_row = conn.execute("SELECT harness FROM claim WHERE work_id=?", (w3,)).fetchone()
        self.assertEqual(claim3_row["harness"], "jules")
        conn.close()

if __name__ == '__main__':
    unittest.main()
