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


    def test_intent_compilation(self):
        # Create dummy IPBD JSON
        ipbd_path = os.path.join(self.tmp_dir.name, "ipbd.json")
        ipbd_content = {
            "intention": "Préserver la souveraineté Amadeus",
            "problematiques": ["P1"],
            "besoins": ["B1"],
            "desirs": ["D1"]
        }
        with open(ipbd_path, 'w', encoding='utf-8') as f:
            json.dump(ipbd_content, f, ensure_ascii=False)

        # First we need a work_id to attach evidence to
        conn = sqlite3.connect(self.db_path)
        conn.execute("INSERT INTO work(layer, title, status) VALUES('L0', 'test', 'pending')")
        work_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
        conn.commit()
        conn.close()

        # Run intent compilation
        cmd = [
            sys.executable, WORKGRAPH_PATH, "intent",
            "--ipbd", ipbd_path,
            "--source-sha256", "abcd123",
            "--alignment", "L0",
            "--work-id", str(work_id)
        ]
        p = subprocess.run(cmd, env=self.env, capture_output=True, text=True)
        self.assertEqual(p.returncode, 0)

        # Output should be deterministic JSON
        out_data = json.loads(p.stdout)
        self.assertEqual(out_data["intention"], "Préserver la souveraineté Amadeus")
        self.assertEqual(out_data["provenance"]["source_sha256"], "abcd123")
        self.assertEqual(out_data["alignment"], "L0")

        # Verify deterministic structure (sorted keys)
        expected_json = json.dumps(out_data, sort_keys=True, indent=2, ensure_ascii=False)
        self.assertEqual(p.stdout.strip(), expected_json.strip())

        # Verify insertion into database
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        ev = conn.execute("SELECT * FROM event WHERE work_id=? AND kind='evidence'", (work_id,)).fetchone()
        conn.close()

        self.assertIsNotNone(ev)
        ev_payload = json.loads(ev['payload'])
        self.assertEqual(ev_payload["intention"], "Préserver la souveraineté Amadeus")

if __name__ == "__main__":
    unittest.main()
