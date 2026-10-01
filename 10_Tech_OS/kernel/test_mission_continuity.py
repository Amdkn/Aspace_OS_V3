import json
import sqlite3
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from mission_continuity import MissionContinuityError, project_mission_cell


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
        """
    )
    con.execute(
        "INSERT INTO work(id,layer,title,status,parent_id,attempts) VALUES(1,'L1','Kernel continuity','pending',NULL,0)"
    )
    con.commit()
    return con


class MissionContinuityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "uc.db"
        self.con = init_db(self.db)
        self.now = datetime(2026, 10, 1, 12, 0, tzinfo=timezone.utc)

    def tearDown(self):
        self.con.close()
        self.tmp.cleanup()

    def emit(self, kind, payload, harness="test"):
        self.con.execute(
            "INSERT INTO event(work_id,harness,kind,payload) VALUES(1,?,?,?)",
            (harness, kind, json.dumps(payload)),
        )
        self.con.commit()

    def test_pending_unowned_cell_is_dispatch_ready(self):
        p = project_mission_cell(self.db, 1, now=self.now)
        self.assertEqual(p["next_action"]["action"], "DISPATCH_READY")
        self.assertFalse(p["ownership"]["claim_live"])

    def test_live_claim_and_binding_is_observed_not_redispatched(self):
        expiry = (self.now + timedelta(minutes=30)).isoformat()
        self.con.execute(
            "INSERT INTO claim(work_id,harness,claimed_at,expires_at) VALUES(1,'jules',?,?)",
            (self.now.isoformat(), expiry),
        )
        self.con.execute(
            """INSERT INTO session_binding(
               work_id,session_key,harness,capability,external_ref,status,started_at,ended_at
               ) VALUES(1,'jules-123','jules','repo-implementation','jules-123','active',?,NULL)""",
            (self.now.isoformat(),),
        )
        self.con.commit()

        p = project_mission_cell(self.db, 1, now=self.now)
        self.assertEqual(p["next_action"]["action"], "OBSERVE_BOUND_WORKER")
        self.assertEqual(p["next_action"]["session_key"], "jules-123")

    def test_binding_without_live_claim_requires_reconciliation(self):
        self.con.execute(
            """INSERT INTO session_binding(
               work_id,session_key,harness,capability,external_ref,status,started_at,ended_at
               ) VALUES(1,'stale-1','jules','repo-implementation','stale-1','active',?,NULL)""",
            (self.now.isoformat(),),
        )
        self.con.commit()

        p = project_mission_cell(self.db, 1, now=self.now)
        self.assertEqual(p["next_action"]["action"], "RECONCILE_BINDING")

    def test_receipt_requires_reconcile_before_any_retry(self):
        self.emit(
            "harness_execution_receipt",
            {
                "correlation_id": "corr-1",
                "effect_state": "UNKNOWN",
                "retry_safe": False,
                "return_route": {"on_unknown": "donna-recover"},
            },
        )
        p = project_mission_cell(self.db, 1, now=self.now)
        self.assertEqual(p["correlation_id"], "corr-1")
        self.assertEqual(p["next_action"]["action"], "RECONCILE_RECEIPT")
        self.assertFalse(p["next_action"]["retry_safe"])

    def test_reconcile_decision_routes_before_new_dispatch(self):
        self.emit(
            "harness_execution_receipt",
            {"correlation_id": "corr-2", "effect_state": "NO", "retry_safe": True},
        )
        self.emit(
            "rory_reconcile_decision",
            {
                "correlation_id": "corr-2",
                "verdict": "REOPEN_BUILD",
                "reopen_cell": "build-42",
                "return_route": {"on_build_defect": "ryan-build"},
            },
        )
        p = project_mission_cell(self.db, 1, now=self.now)
        self.assertEqual(p["next_action"]["action"], "ROUTE_RECONCILE_DECISION")
        self.assertEqual(p["next_action"]["verdict"], "REOPEN_BUILD")

    def test_continuation_survives_fresh_process_projection(self):
        route = {
            "mission_id": "kernel-291",
            "cell_id": "p0",
            "on_success": "nardole-dispatch",
            "on_retry": "nardole-dispatch",
            "on_unknown": "donna-recover",
        }
        self.emit(
            "rory_reconcile_decision",
            {"correlation_id": "corr-3", "verdict": "ACCEPT_CONTINUE", "return_route": route},
        )
        self.emit(
            "continuation_routed",
            {
                "correlation_id": "corr-3",
                "route_class": "NEXT_FLOW",
                "target_capability": "river-flow",
                "return_route": route,
            },
        )

        first = project_mission_cell(self.db, 1, now=self.now)
        second = project_mission_cell(self.db, 1, now=self.now)

        self.assertEqual(first["correlation_id"], "corr-3")
        self.assertEqual(first["return_to"], route)
        self.assertEqual(first["next_action"]["action"], "ROUTE_CONTINUATION")
        self.assertEqual(first["next_action"]["target_capability"], "river-flow")
        self.assertEqual(first, second)

    def test_unknown_work_fails_closed(self):
        with self.assertRaises(MissionContinuityError):
            project_mission_cell(self.db, 999, now=self.now)


if __name__ == "__main__":
    unittest.main(verbosity=2)
