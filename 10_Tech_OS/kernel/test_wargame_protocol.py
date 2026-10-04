import sqlite3
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from wargame import WargameProtocolError, is_stale, record_outcome

def init_db(path: Path):
    con = sqlite3.connect(path)
    con.executescript(
        """
        CREATE TABLE work(
          id INTEGER PRIMARY KEY,
          layer TEXT NOT NULL,
          title TEXT NOT NULL,
          status TEXT NOT NULL,
          parent_id INTEGER,
          attempts INTEGER NOT NULL DEFAULT 0,
          created_at TEXT NOT NULL DEFAULT (datetime('now')),
          updated_at TEXT NOT NULL DEFAULT (datetime('now'))
        );
        CREATE TABLE claim(
          work_id INTEGER PRIMARY KEY,
          harness TEXT NOT NULL,
          claimed_at TEXT NOT NULL,
          expires_at TEXT NOT NULL
        );
        CREATE TABLE session_binding(
          id INTEGER PRIMARY KEY,
          work_id INTEGER NOT NULL,
          session_key TEXT NOT NULL UNIQUE,
          harness TEXT NOT NULL,
          capability TEXT,
          external_ref TEXT,
          status TEXT NOT NULL,
          started_at TEXT NOT NULL,
          ended_at TEXT
        );
        CREATE TABLE event(
          id INTEGER PRIMARY KEY,
          work_id INTEGER,
          harness TEXT,
          kind TEXT NOT NULL,
          payload TEXT,
          at TEXT NOT NULL DEFAULT (datetime('now'))
        );
        CREATE TABLE wargame (
          github_issue INTEGER PRIMARY KEY,
          work_id INTEGER REFERENCES work(id) ON DELETE SET NULL,
          state TEXT NOT NULL DEFAULT 'OPEN' CHECK (state IN ('OPEN', 'CLOSED')),
          current_round INTEGER NOT NULL DEFAULT 1,
          hypothesis TEXT,
          falsification_conditions TEXT,
          last_verified_effect TEXT,
          next_gate TEXT,
          owner_level TEXT,
          return_to TEXT,
          stale_after TEXT,
          created_at TEXT NOT NULL DEFAULT (datetime('now')),
          updated_at TEXT NOT NULL DEFAULT (datetime('now'))
        );
        CREATE TABLE wargame_child (
          id INTEGER PRIMARY KEY,
          parent_issue INTEGER NOT NULL REFERENCES wargame(github_issue) ON DELETE CASCADE,
          work_id INTEGER REFERENCES work(id) ON DELETE SET NULL,
          claim_prediction TEXT,
          institutional_owner TEXT,
          capability TEXT,
          runtime_binding TEXT,
          evidence_sink TEXT,
          deterministic_gates TEXT,
          receipt TEXT,
          return_to TEXT,
          status TEXT NOT NULL DEFAULT 'ACTIVE' CHECK (status IN ('ACTIVE', 'CLOSED')),
          created_at TEXT NOT NULL DEFAULT (datetime('now')),
          updated_at TEXT NOT NULL DEFAULT (datetime('now'))
        );
        """
    )
    con.commit()
    return con

class TestWargameProtocol(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "uc.db"
        self.con = init_db(self.db)
        self.now = datetime(2026, 10, 2, 12, 0, tzinfo=timezone.utc)

    def tearDown(self):
        self.con.close()
        self.tmp.cleanup()

    def test_record_outcome_valid(self):
        res = record_outcome(self.db, 321, "NEXT_GATE", now=self.now)
        self.assertEqual(res["outcome"], "NEXT_GATE")
        self.assertEqual(res["round"], 1)

        res = record_outcome(self.db, 321, "CHILD_CELL_REQUIRED", now=self.now)
        self.assertEqual(res["outcome"], "CHILD_CELL_REQUIRED")
        self.assertEqual(res["round"], 2)

        cur = self.con.execute("SELECT * FROM wargame WHERE github_issue=321")
        row = cur.fetchone()
        self.assertIsNotNone(row)
        self.assertEqual(row[7], "CHILD_CELL_REQUIRED") # next_gate
        self.assertEqual(row[3], 2) # current_round

    def test_record_outcome_invalid(self):
        with self.assertRaises(WargameProtocolError):
            record_outcome(self.db, 321, "WAIT_FOR_USER", now=self.now)
            
    def test_is_stale_false_when_not_open(self):
        self.con.execute(
            "INSERT INTO wargame (github_issue, state, next_gate) VALUES (1, 'CLOSED', 'NEXT_GATE')"
        )
        self.con.commit()
        self.assertFalse(is_stale(self.db, 1, now=self.now))

    def test_is_stale_false_when_no_stale_after(self):
        self.con.execute(
            "INSERT INTO wargame (github_issue, state, next_gate) VALUES (1, 'OPEN', 'NEXT_GATE')"
        )
        self.con.commit()
        self.assertFalse(is_stale(self.db, 1, now=self.now))

    def test_is_stale_false_when_not_past_stale_after(self):
        future = (self.now + timedelta(days=1)).isoformat()
        self.con.execute(
            "INSERT INTO wargame (github_issue, state, next_gate, stale_after) VALUES (1, 'OPEN', 'NEXT_GATE', ?)",
            (future,)
        )
        self.con.commit()
        self.assertFalse(is_stale(self.db, 1, now=self.now))

    def test_is_stale_true_when_past_stale_after_and_no_children(self):
        past = (self.now - timedelta(days=1)).isoformat()
        self.con.execute(
            "INSERT INTO wargame (github_issue, state, next_gate, stale_after) VALUES (1, 'OPEN', 'NEXT_GATE', ?)",
            (past,)
        )
        self.con.commit()
        self.assertTrue(is_stale(self.db, 1, now=self.now))

    def test_is_stale_false_when_active_child_has_live_claim(self):
        past = (self.now - timedelta(days=1)).isoformat()
        self.con.execute(
            "INSERT INTO wargame (github_issue, state, next_gate, stale_after) VALUES (1, 'OPEN', 'NEXT_GATE', ?)",
            (past,)
        )
        self.con.execute(
            "INSERT INTO work (id, layer, title, status) VALUES (10, 'L1', 'test', 'pending')"
        )
        self.con.execute(
            "INSERT INTO wargame_child (parent_issue, work_id, status) VALUES (1, 10, 'ACTIVE')"
        )
        
        future = (self.now + timedelta(minutes=30)).isoformat()
        self.con.execute(
            "INSERT INTO claim (work_id, harness, claimed_at, expires_at) VALUES (10, 'ryan', ?, ?)",
            (self.now.isoformat(), future)
        )
        self.con.commit()

        self.assertFalse(is_stale(self.db, 1, now=self.now))

    def test_is_stale_true_when_active_child_claim_expired(self):
        past_stale = (self.now - timedelta(days=1)).isoformat()
        self.con.execute(
            "INSERT INTO wargame (github_issue, state, next_gate, stale_after) VALUES (1, 'OPEN', 'NEXT_GATE', ?)",
            (past_stale,)
        )
        self.con.execute(
            "INSERT INTO work (id, layer, title, status) VALUES (10, 'L1', 'test', 'pending')"
        )
        self.con.execute(
            "INSERT INTO wargame_child (parent_issue, work_id, status) VALUES (1, 10, 'ACTIVE')"
        )
        
        past_claim = (self.now - timedelta(minutes=30)).isoformat()
        self.con.execute(
            "INSERT INTO claim (work_id, harness, claimed_at, expires_at) VALUES (10, 'ryan', ?, ?)",
            ((self.now - timedelta(hours=1)).isoformat(), past_claim)
        )
        self.con.commit()

        self.assertTrue(is_stale(self.db, 1, now=self.now))
        
    def test_is_stale_false_when_active_child_has_active_binding(self):
        past = (self.now - timedelta(days=1)).isoformat()
        self.con.execute(
            "INSERT INTO wargame (github_issue, state, next_gate, stale_after) VALUES (1, 'OPEN', 'NEXT_GATE', ?)",
            (past,)
        )
        self.con.execute(
            "INSERT INTO work (id, layer, title, status) VALUES (10, 'L1', 'test', 'pending')"
        )
        self.con.execute(
            "INSERT INTO wargame_child (parent_issue, work_id, status) VALUES (1, 10, 'ACTIVE')"
        )
        self.con.execute(
            "INSERT INTO session_binding (work_id, session_key, harness, status, started_at) VALUES (10, 'k', 'ryan', 'active', ?)",
            (self.now.isoformat(),)
        )
        self.con.commit()

        self.assertFalse(is_stale(self.db, 1, now=self.now))

if __name__ == "__main__":
    unittest.main()
