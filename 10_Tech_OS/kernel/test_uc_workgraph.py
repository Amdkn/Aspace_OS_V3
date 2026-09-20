#!/usr/bin/env python3
import json
import os
import sqlite3
import tempfile
import unittest
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
UC_PATH = os.path.join(HERE, "uc.py")
WORKGRAPH_PATH = os.path.join(HERE, "uc_workgraph.py")

class TestWorkgraph(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.tmp_dir.name, "test_uc.db")
        self.env = os.environ.copy()
        self.env["ASPACE_DB"] = self.db_path

        cmd = [sys.executable, UC_PATH, "init"]
        subprocess.run(cmd, env=self.env, check=True, capture_output=True)

    def tearDown(self):
        self.tmp_dir.cleanup()

    def add_event(self, harness, payload):
        conn = sqlite3.connect(self.db_path)
        conn.execute(
            "INSERT INTO event(work_id, harness, kind, payload) VALUES(NULL, ?, 'capability', ?)",
            (harness, json.dumps(payload))
        )
        conn.commit()
        conn.close()

    def run_selector(self, caps, min_ev):
        cmd = [sys.executable, WORKGRAPH_PATH]
        for cap in caps:
            cmd.extend(["--require-capability", cap])
        cmd.extend(["--min-evidence-level", str(min_ev)])
        p = subprocess.run(cmd, env=self.env, capture_output=True, text=True)
        self.assertEqual(p.returncode, 0)
        return json.loads(p.stdout)

    def test_selector(self):
        self.add_event("h1", {"capability": "C1", "status": "pass", "evidence_level": 3})
        self.add_event("h2", {"capability": "C1", "status": "pass", "evidence_level": 1})
        self.add_event("h3", {"capability": "C1", "status": "fail", "evidence_level": 5})

        # Test capability C1 with min evidence 1
        res = self.run_selector(["C1"], 1)
        self.assertEqual(res, ["h1", "h2"])

        # Test capability C1 with min evidence 2
        res = self.run_selector(["C1"], 2)
        self.assertEqual(res, ["h1"])

        # Test capability C2
        res = self.run_selector(["C2"], 1)
        self.assertEqual(res, [])

        # Update h2 to fail
        self.add_event("h2", {"capability": "C1", "status": "fail", "evidence_level": 1})
        res = self.run_selector(["C1"], 1)
        self.assertEqual(res, ["h1"])

if __name__ == "__main__":
    unittest.main()
