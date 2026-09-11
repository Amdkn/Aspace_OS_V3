#!/usr/bin/env python3
"""test_l0_kernel.py — Suite de tests unitaires pour le Kernel L0 (uc.py, dlq.py, gate.py).

Valide la Loi L0 : Auto-réplication, gestion du cycle de vie des travaux,
triage Donna DLQ et validation déterministe des portes SSSF.
"""
import json
import os
import sqlite3
import tempfile
import unittest
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
UC_PATH = os.path.join(HERE, "uc.py")
DLQ_PATH = os.path.join(HERE, "dlq.py")
GATE_PATH = os.path.join(HERE, "gate.py")

class TestL0Kernel(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test_uc.db")
        self.env = os.environ.copy()
        self.env["ASPACE_DB"] = self.db_path

    def tearDown(self):
        self.tmp_dir.cleanup()

    def run_cmd(self, script_path, *args):
        cmd = [sys.executable, script_path] + list(args)
        p = subprocess.run(cmd, capture_output=True, text=True, env=self.env, timeout=30)
        return p

    def test_01_uc_init_and_workflow(self):
        # 1. Init DB
        p = self.run_cmd(UC_PATH, "init")
        self.assertEqual(p.returncode, 0, f"Error init: {p.stderr}")
        data = json.loads(p.stdout)
        self.assertTrue(data.get("ok"))

        # 2. Submit work
        p = self.run_cmd(UC_PATH, "submit", "--layer", "L0", "--title", "Test Task L0")
        self.assertEqual(p.returncode, 0)
        res = json.loads(p.stdout)
        self.assertTrue(res.get("ok"))
        work_id = res["work_id"]

        # 3. Claim work
        p = self.run_cmd(UC_PATH, "claim", "--harness", "test_harness", "--work", str(work_id))
        self.assertEqual(p.returncode, 0)
        res = json.loads(p.stdout)
        self.assertTrue(res.get("ok"))
        self.assertEqual(res["work"]["id"], work_id)

        # 4. Predict work (Loi de prédiction préalable)
        p = self.run_cmd(UC_PATH, "predict", "--work", str(work_id), "--claim", "Succès attendu du test L0", "--confidence", "0.9")
        self.assertEqual(p.returncode, 0)
        res = json.loads(p.stdout)
        self.assertTrue(res.get("ok"))

        # 5. Attest criterion
        p = self.run_cmd(UC_PATH, "attest", "--work", str(work_id), "--criterion", "1", "--ok", "1", "--harness", "test_harness")
        self.assertEqual(p.returncode, 0)
        res = json.loads(p.stdout)
        self.assertTrue(res.get("ok"))

        # 6. Move to review (Loi de détachement)
        p = self.run_cmd(UC_PATH, "review", "--work", str(work_id))
        self.assertEqual(p.returncode, 0)
        res = json.loads(p.stdout)
        self.assertTrue(res.get("ok"))

        # 7. Mark done
        p = self.run_cmd(UC_PATH, "done", "--work", str(work_id))
        self.assertEqual(p.returncode, 0)
        res = json.loads(p.stdout)
        self.assertTrue(res.get("ok"))

    def test_02_dlq_escalation_and_arbitrage(self):
        # 1. Init DB
        self.run_cmd(UC_PATH, "init")

        # 2. Submit and fail work 3 times
        p = self.run_cmd(UC_PATH, "submit", "--layer", "L0", "--title", "Failing Task")
        work_id = json.loads(p.stdout)["work_id"]

        conn = sqlite3.connect(self.db_path)
        conn.execute("UPDATE work SET attempts=3, status='failed' WHERE id=?", (work_id,))
        conn.execute("INSERT INTO event(work_id, harness, kind, payload) VALUES(?, ?, 'failed', ?)",
                     (work_id, "test_harness", json.dumps({"reason": "sans preuve"})))
        conn.commit()
        conn.close()

        # 3. Run Donna DLQ
        p = self.run_cmd(DLQ_PATH, "run", "--seuil", "3")
        self.assertEqual(p.returncode, 0)
        res = json.loads(p.stdout)
        self.assertEqual(len(res["escalades"]), 1)
        self.assertEqual(res["escalades"][0]["work_id"], work_id)

        # 4. Rapport
        p = self.run_cmd(DLQ_PATH, "rapport")
        self.assertEqual(p.returncode, 0)
        res = json.loads(p.stdout)
        self.assertEqual(len(res["bureau_de_rick"]), 1)

        # 5. Cloture terminale Rick
        p = self.run_cmd(DLQ_PATH, "cloturer", "--work", str(work_id), "--motif", "Doublon - Cloture Rick L0")
        self.assertEqual(p.returncode, 0)
        res = json.loads(p.stdout)
        self.assertTrue(res.get("ok"))

        # Check terminal status
        conn = sqlite3.connect(self.db_path)
        row = conn.execute("SELECT status FROM work WHERE id=?", (work_id,)).fetchone()
        self.assertEqual(row[0], "failed")
        conn.close()

if __name__ == "__main__":
    unittest.main()
