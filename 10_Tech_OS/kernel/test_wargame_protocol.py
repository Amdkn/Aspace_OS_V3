import sqlite3
import tempfile
import unittest
from contextlib import closing
from datetime import datetime, timedelta, timezone
from pathlib import Path

from wargame import WargameProtocolError, is_stale, record_outcome

HERE = Path(__file__).resolve().parent
SCHEMA = HERE / "schema.sql"


class WargameContinuationProtocolTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "uc.db"
        with closing(sqlite3.connect(self.db)) as con:
            con.executescript(SCHEMA.read_text(encoding="utf-8"))

    def tearDown(self):
        self.tmp.cleanup()

    def test_machine_readable_outcomes_advance_round_and_emit_event(self):
        now = datetime(2026, 10, 2, 12, 0, tzinfo=timezone.utc)
        first = record_outcome(self.db, 321, "NEXT_GATE", now=now)
        second = record_outcome(
            self.db, 321, "CHILD_CELL_REQUIRED", now=now + timedelta(minutes=1)
        )

        self.assertEqual(first["round"], 1)
        self.assertEqual(second["round"], 2)
        with closing(sqlite3.connect(self.db)) as con:
            row = con.execute(
                "SELECT current_round, next_gate FROM wargame WHERE github_issue=321"
            ).fetchone()
            self.assertEqual(row, (2, "CHILD_CELL_REQUIRED"))
            events = con.execute(
                "SELECT COUNT(*) FROM event WHERE kind='wargame_outcome'"
            ).fetchone()[0]
            self.assertEqual(events, 2)

    def test_wait_for_user_is_not_a_valid_terminal_outcome(self):
        with self.assertRaises(WargameProtocolError):
            record_outcome(self.db, 321, "WAIT_FOR_USER")

    def test_stale_parent_reopens_only_without_live_claim_or_binding(self):
        now = datetime(2026, 10, 2, 12, 0, tzinfo=timezone.utc)
        stale_after = (now - timedelta(minutes=1)).isoformat()

        with closing(sqlite3.connect(self.db)) as con:
            con.execute(
                """INSERT INTO wargame
                   (github_issue, state, current_round, next_gate, stale_after)
                   VALUES (321, 'OPEN', 1, 'NEXT_GATE', ?)""",
                (stale_after,),
            )
            con.commit()

        self.assertTrue(is_stale(self.db, 321, now=now))

        with closing(sqlite3.connect(self.db)) as con:
            con.execute(
                "INSERT INTO work(id, layer, title, status) VALUES(9001, 'L0', 'child', 'pending')"
            )
            con.execute(
                """INSERT INTO wargame_child(parent_issue, work_id, status)
                   VALUES(321, 9001, 'ACTIVE')"""
            )
            con.execute(
                """INSERT INTO claim(work_id, harness, claimed_at, expires_at)
                   VALUES(9001, 'Jules', ?, ?)""",
                (now.isoformat(), (now + timedelta(minutes=5)).isoformat()),
            )
            con.commit()

        self.assertFalse(is_stale(self.db, 321, now=now))

        with closing(sqlite3.connect(self.db)) as con:
            con.execute(
                "UPDATE claim SET expires_at=? WHERE work_id=9001",
                ((now - timedelta(seconds=1)).isoformat(),),
            )
            con.execute(
                """INSERT INTO session_binding(
                     work_id, session_key, harness, status, started_at
                   ) VALUES(9001, 'session-321', 'Jules', 'active', ?)""",
                (now.isoformat(),),
            )
            con.commit()

        self.assertFalse(is_stale(self.db, 321, now=now))

        with closing(sqlite3.connect(self.db)) as con:
            con.execute(
                "UPDATE session_binding SET status='closed', ended_at=? WHERE work_id=9001",
                (now.isoformat(),),
            )
            con.commit()

        self.assertTrue(is_stale(self.db, 321, now=now))


if __name__ == "__main__":
    unittest.main()
