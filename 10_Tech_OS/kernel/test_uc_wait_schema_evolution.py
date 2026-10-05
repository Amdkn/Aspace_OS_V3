#!/usr/bin/env python3
import json
import os
import sqlite3
import subprocess
import sys
import tempfile
import time
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
UC_PATH = os.path.join(HERE, "uc.py")
MIGRATION_PATH = os.path.join(HERE, "migration.py")

sys.path.insert(0, HERE)
import migration


LEGACY_SQL = """
PRAGMA foreign_keys=ON;
CREATE TABLE tape (id INTEGER PRIMARY KEY, path TEXT);
CREATE TABLE work (
  id INTEGER PRIMARY KEY,
  tape_id INTEGER,
  layer TEXT NOT NULL CHECK (layer IN ('A0','L0','L1','L2')),
  title TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'pending'
    CHECK (status IN ('pending','claimed','review','done','failed','blocked')),
  priority INTEGER NOT NULL DEFAULT 0,
  parent_id INTEGER,
  attempts INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE TABLE claim (
  work_id INTEGER PRIMARY KEY REFERENCES work(id) ON DELETE CASCADE,
  harness TEXT NOT NULL,
  claimed_at TEXT NOT NULL DEFAULT (datetime('now')),
  expires_at TEXT NOT NULL
);
CREATE TABLE session_binding (
  id INTEGER PRIMARY KEY,
  work_id INTEGER,
  harness TEXT
);
CREATE TABLE work_wait (
  work_id INTEGER PRIMARY KEY REFERENCES work(id) ON DELETE CASCADE,
  condition_text TEXT NOT NULL,
  wake_at TEXT,
  reason TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE TABLE event (
  id INTEGER PRIMARY KEY,
  work_id INTEGER,
  harness TEXT,
  kind TEXT NOT NULL,
  payload TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
"""


class TestUCWaitSchemaEvolution(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = os.path.join(self.tmp.name, "legacy_uc.db")
        c = sqlite3.connect(self.db)
        c.executescript(LEGACY_SQL)
        c.execute(
            "INSERT INTO work(id,layer,title,status,priority) VALUES(1,'L0','legacy wait canary','claimed',95)"
        )
        c.execute(
            "INSERT INTO claim(work_id,harness,expires_at) VALUES(1,'ryan-test',datetime('now','+60 seconds'))"
        )
        c.commit()
        c.close()
        self.env = os.environ.copy()
        self.env["ASPACE_DB"] = self.db

    def tearDown(self):
        self.tmp.cleanup()

    def run_uc(self, *args):
        p = subprocess.run(
            [sys.executable, UC_PATH, *args],
            env=self.env,
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertEqual(p.returncode, 0, msg=p.stderr or p.stdout)
        return json.loads(p.stdout)

    def test_legacy_wait_migrates_and_preserves_sleep_fence(self):
        result = migration.apply_migration(self.db, dry_run=False)
        self.assertTrue(result["ok"])
        self.assertEqual(result["missing_tables"], [])

        c = sqlite3.connect(self.db)
        cols = {
            table: {row[1] for row in c.execute(f"PRAGMA table_info({table})")}
            for table in ("work", "claim", "session_binding", "work_wait")
        }
        self.assertIn("wake_at", cols["work"])
        self.assertIn("institutional_owner", cols["work"])
        self.assertIn("correlation_id", cols["work"])
        self.assertIn("institutional_owner", cols["claim"])
        self.assertIn("runtime_id", cols["claim"])
        self.assertIn("institutional_owner", cols["session_binding"])
        self.assertIn("runtime_id", cols["session_binding"])
        self.assertIn("institutional_owner", cols["work_wait"])
        c.close()

        waited = self.run_uc("wait", "--work", "1", "--seconds", "1")
        self.assertEqual(waited["status"], "pending")

        c = sqlite3.connect(self.db)
        self.assertEqual(c.execute("SELECT status FROM work WHERE id=1").fetchone()[0], "pending")
        self.assertIsNone(c.execute("SELECT * FROM claim WHERE work_id=1").fetchone())
        self.assertIsNotNone(c.execute("SELECT * FROM work_wait WHERE work_id=1").fetchone())
        c.close()

        blocked = self.run_uc("claim", "--harness", "other", "--work", "1")
        self.assertIsNone(blocked["work"])

        time.sleep(2)
        reaped = self.run_uc("reap")
        self.assertIn(1, reaped["woken"])

        c = sqlite3.connect(self.db)
        self.assertIsNone(c.execute("SELECT * FROM work_wait WHERE work_id=1").fetchone())
        self.assertIsNone(c.execute("SELECT wake_at FROM work WHERE id=1").fetchone()[0])
        c.close()

        reclaimed = self.run_uc("claim", "--harness", "other", "--work", "1")
        self.assertEqual(reclaimed["work"]["id"], 1)


    def test_migration_is_idempotent(self):
        first = migration.apply_migration(self.db, dry_run=False)
        second = migration.apply_migration(self.db, dry_run=False)
        self.assertTrue(first["ok"])
        self.assertTrue(second["ok"])
        self.assertEqual(second["applied"], [])
        self.assertEqual(second["errors"], [])
        self.assertEqual(second["missing_tables"], [])

    def test_terminal_work_is_not_resurrected_by_reap(self):
        result = migration.apply_migration(self.db, dry_run=False)
        self.assertTrue(result["ok"])
        self.run_uc("wait", "--work", "1", "--seconds", "1")
        self.run_uc("done", "--work", "1")
        time.sleep(2)
        reaped = self.run_uc("reap")
        self.assertNotIn(1, reaped["woken"])
        c = sqlite3.connect(self.db)
        self.assertEqual(c.execute("SELECT status FROM work WHERE id=1").fetchone()[0], "done")
        self.assertIsNone(c.execute("SELECT * FROM work_wait WHERE work_id=1").fetchone())
        self.assertIsNone(c.execute("SELECT wake_at FROM work WHERE id=1").fetchone()[0])
        c.close()



if __name__ == "__main__":
    unittest.main()
