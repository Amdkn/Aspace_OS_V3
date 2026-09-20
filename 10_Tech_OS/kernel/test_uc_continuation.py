#!/usr/bin/env python3
"""test_uc_continuation.py — Suite de tests unitaires pour les invariants de continuation du noyau L0.

Valide claim/lease/heartbeat/reap/fencing invariants in uc.py / uc.db.
Test continuation invariants against restart, stale lease, orphan recovery,
waiting and duplicate ownership scenarios.
"""
import json
import os
import sqlite3
import tempfile
import unittest
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
UC_PATH = os.path.join(HERE, "uc.py")

class TestUCContinuation(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test_uc.db")
        self.env = os.environ.copy()
        self.env["ASPACE_DB"] = self.db_path
        self.run_cmd(UC_PATH, "init")

    def tearDown(self):
        self.tmp_dir.cleanup()

    def run_cmd(self, script_path, *args):
        cmd = [sys.executable, script_path] + list(args)
        p = subprocess.run(cmd, capture_output=True, text=True, env=self.env, timeout=10)
        return p

    def test_continuation_invariants(self):
        # 1. Submit work
        p = self.run_cmd(UC_PATH, "submit", "--layer", "L0", "--title", "Restart Task L0")
        self.assertEqual(p.returncode, 0)
        res = json.loads(p.stdout)
        self.assertTrue(res.get("ok"))
        work_id = res["work_id"]

        # 2. Claim work
        p = self.run_cmd(UC_PATH, "claim", "--harness", "test_harness", "--work", str(work_id), "--lease", "1")
        self.assertEqual(p.returncode, 0)
        res = json.loads(p.stdout)
        self.assertTrue(res.get("ok"))
        self.assertEqual(res["work"]["id"], work_id)

        # 3. Duplicate ownership attempt
        p = self.run_cmd(UC_PATH, "claim", "--harness", "other_harness", "--work", str(work_id), "--lease", "1")
        self.assertEqual(p.returncode, 0)
        res = json.loads(p.stdout)
        self.assertTrue(res.get("ok"))
        self.assertIsNone(res.get("work")) # Should not be claimable because it's already claimed

        time.sleep(2) # Let lease expire

        # 4. Reap orphan lease (stale lease recovery)
        p = self.run_cmd(UC_PATH, "reap")
        self.assertEqual(p.returncode, 0)
        res = json.loads(p.stdout)
        self.assertTrue(res.get("ok"))
        self.assertIn(work_id, res["reclames"])

        # 5. Re-claim by another harness
        p = self.run_cmd(UC_PATH, "claim", "--harness", "other_harness", "--work", str(work_id))
        self.assertEqual(p.returncode, 0)
        res = json.loads(p.stdout)
        self.assertTrue(res.get("ok"))
        self.assertEqual(res["work"]["id"], work_id)

        # 6. Beat heartbeat
        p = self.run_cmd(UC_PATH, "beat", "--work", str(work_id), "--harness", "other_harness")
        self.assertEqual(p.returncode, 0)
        res = json.loads(p.stdout)
        self.assertTrue(res.get("ok"))

        # Predict
        p = self.run_cmd(UC_PATH, "predict", "--work", str(work_id), "--claim", "Finish task", "--confidence", "0.9")
        self.assertEqual(p.returncode, 0)

        # Review
        p = self.run_cmd(UC_PATH, "review", "--work", str(work_id))
        self.assertEqual(p.returncode, 0)

        # 7. Check terminal fencing
        # Rick closed as duplicate
        conn = sqlite3.connect(self.db_path)
        conn.execute("INSERT INTO event(work_id, harness, kind, payload) VALUES(?, ?, 'arbitrage', ?)",
                     (work_id, "test_harness", json.dumps({"terminal": True, "reason": "duplicate"})))
        conn.execute("UPDATE work SET status='failed' WHERE id=?", (work_id,))
        conn.commit()
        conn.close()

        # 8. Try claim fenced work
        p = self.run_cmd(UC_PATH, "claim", "--harness", "test_harness", "--work", str(work_id))
        self.assertEqual(p.returncode, 0)
        res = json.loads(p.stdout)
        self.assertTrue(res.get("ok"))
        self.assertIsNone(res.get("work"))
        self.assertIn("refus", res)

    def test_wait_wake_invariant(self):
        # 1. Submit work
        p = self.run_cmd(UC_PATH, "submit", "--layer", "L0", "--title", "Wait Task L0")
        self.assertEqual(p.returncode, 0)
        res = json.loads(p.stdout)
        self.assertTrue(res.get("ok"))
        work_id = res["work_id"]

        # 2. Claim work
        p = self.run_cmd(UC_PATH, "claim", "--harness", "test_harness", "--work", str(work_id))
        self.assertEqual(p.returncode, 0)

        # 3. Put to wait
        p = self.run_cmd(UC_PATH, "wait", "--work", str(work_id), "--seconds", "1")
        self.assertEqual(p.returncode, 0)
        res = json.loads(p.stdout)
        self.assertTrue(res.get("ok"))

        # 4. Try claim (should fail because it's waiting)
        p = self.run_cmd(UC_PATH, "claim", "--harness", "test_harness", "--work", str(work_id))
        self.assertEqual(p.returncode, 0)
        res = json.loads(p.stdout)
        self.assertTrue(res.get("ok"))
        self.assertIsNone(res.get("work"))

        time.sleep(2) # Let wake_at expire

        # 5. Reap should wake it
        p = self.run_cmd(UC_PATH, "reap")
        self.assertEqual(p.returncode, 0)
        res = json.loads(p.stdout)
        self.assertTrue(res.get("ok"))
        self.assertIn(work_id, res.get("woken", []))

        # 6. Re-claim should succeed
        p = self.run_cmd(UC_PATH, "claim", "--harness", "test_harness", "--work", str(work_id))
        self.assertEqual(p.returncode, 0)
        res = json.loads(p.stdout)
        self.assertTrue(res.get("ok"))
        self.assertEqual(res["work"]["id"], work_id)

if __name__ == "__main__":
    unittest.main()
