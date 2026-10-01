import json
import sqlite3
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from mission_continuity import project_mission_cell
from mission_watcher import (
    apply_manager_resolution,
    observe_bound_worker,
    reconcile_binding,
    resolve_manager_wake,
)


HERE = Path(__file__).resolve().parent
SCHEMA = HERE / "schema.sql"


class MissionWatcherTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "uc.db"
        con = sqlite3.connect(self.db)
        con.executescript(SCHEMA.read_text(encoding="utf-8"))
        con.execute(
            "INSERT INTO work(layer,title,status,priority,attempts) "
            "VALUES('L1','P3 watcher cell','claimed',1,0)"
        )
        self.work_id = int(con.execute("SELECT last_insert_rowid()").fetchone()[0])
        con.execute(
            "INSERT INTO claim(work_id,harness,claimed_at,expires_at) "
            "VALUES(?, 'jules', datetime('now'), '2099-01-01T00:00:00+00:00')",
            (self.work_id,),
        )
        con.execute(
            """INSERT INTO session_binding(
                 work_id,session_key,harness,capability,external_ref,status,started_at,ended_at
               ) VALUES(?, 'jules-123', 'jules', 'repo-implementation',
                        'jules-123', 'active', datetime('now'), NULL)""",
            (self.work_id,),
        )
        con.execute(
            """INSERT INTO event(work_id,harness,kind,payload)
               VALUES(?, 'nardole-dispatch', 'dispatch_envelope', ?)""",
            (
                self.work_id,
                json.dumps(
                    {
                        "correlation_id": "corr-watch",
                        "return_route": {
                            "mission": "#291",
                            "cell": "#296",
                            "capability": "FLOW",
                        },
                        "required_capability": "repo-implementation",
                    }
                ),
            ),
        )
        con.commit()
        con.close()

    def tearDown(self):
        self.tmp.cleanup()

    def event_count(self, kind):
        con = sqlite3.connect(self.db)
        value = con.execute(
            "SELECT count(*) FROM event WHERE work_id=? AND kind=?",
            (self.work_id, kind),
        ).fetchone()[0]
        con.close()
        return value

    def test_unchanged_in_progress_is_idempotent_and_never_wakes_manager(self):
        observation = {
            "id": "jules-123",
            "state": "IN_PROGRESS",
            "updateTime": "2026-10-01T06:10:00Z",
        }
        first = observe_bound_worker(self.db, self.work_id, observation)
        second = observe_bound_worker(self.db, self.work_id, observation)

        self.assertEqual(first["transition"], "IN_PROGRESS")
        self.assertFalse(first["manager_wake_required"])
        self.assertIsNone(first["wake_event_id"])
        self.assertFalse(first["idempotent"])
        self.assertTrue(second["idempotent"])
        self.assertEqual(self.event_count("worker_transition_observed"), 1)
        self.assertEqual(self.event_count("manager_wake_requested"), 0)

    def test_awaiting_feedback_wakes_once_and_keeps_same_session_resume(self):
        observation = {
            "id": "jules-123",
            "state": "AWAITING_USER_FEEDBACK",
            "updateTime": "2026-10-01T06:11:00Z",
        }
        first = observe_bound_worker(self.db, self.work_id, observation)
        second = observe_bound_worker(self.db, self.work_id, observation)

        self.assertEqual(first["transition"], "AWAITING_USER_FEEDBACK")
        self.assertTrue(first["manager_wake_required"])
        self.assertTrue(first["same_session_resume_safe"])
        self.assertIsNotNone(first["wake_event_id"])
        self.assertTrue(second["idempotent"])
        self.assertEqual(self.event_count("manager_wake_requested"), 1)

    def test_completed_with_pr_becomes_pr_ready(self):
        observation = {
            "id": "jules-123",
            "state": "COMPLETED",
            "updateTime": "2026-10-01T06:12:00Z",
            "outputs": [
                {"pullRequest": {"url": "https://github.com/Amdkn/Aspace_OS_V3/pull/999"}}
            ],
        }
        result = observe_bound_worker(self.db, self.work_id, observation)

        self.assertEqual(result["transition"], "PR_READY")
        self.assertTrue(result["manager_wake_required"])
        self.assertEqual(
            result["pull_requests"],
            ["https://github.com/Amdkn/Aspace_OS_V3/pull/999"],
        )

    def test_completed_without_pr_still_requires_evidence_review(self):
        result = observe_bound_worker(
            self.db,
            self.work_id,
            {
                "id": "jules-123",
                "state": "COMPLETED",
                "updateTime": "2026-10-01T06:13:00Z",
                "outputs": [{"changeSet": {"description": "local patch"}}],
            },
        )
        self.assertEqual(result["transition"], "EVIDENCE_READY")
        self.assertTrue(result["manager_wake_required"])
        self.assertTrue(result["evidence_present"])

    def test_binding_mismatch_is_fenced_unknown_and_wakes(self):
        result = observe_bound_worker(
            self.db,
            self.work_id,
            {
                "id": "replacement-session",
                "state": "IN_PROGRESS",
                "updateTime": "2026-10-01T06:14:00Z",
            },
        )
        self.assertEqual(result["transition"], "UNKNOWN")
        self.assertTrue(result["fenced"])
        self.assertTrue(result["manager_wake_required"])
        self.assertFalse(result["same_session_resume_safe"])

    def test_failed_and_ci_failure_are_useful_wake_transitions(self):
        failed = observe_bound_worker(
            self.db,
            self.work_id,
            {
                "id": "jules-123",
                "state": "FAILED",
                "updateTime": "2026-10-01T06:15:00Z",
            },
        )
        ci = observe_bound_worker(
            self.db,
            self.work_id,
            {
                "id": "jules-123",
                "state": "IN_PROGRESS",
                "ci_state": "failure",
                "updateTime": "2026-10-01T06:16:00Z",
            },
        )
        self.assertEqual(failed["transition"], "FAILED")
        self.assertEqual(ci["transition"], "CI_FAILURE")
        self.assertTrue(ci["same_session_resume_safe"])

    def test_watcher_state_survives_fresh_mission_projection(self):
        observed = observe_bound_worker(
            self.db,
            self.work_id,
            {
                "id": "jules-123",
                "state": "AWAITING_USER_FEEDBACK",
                "updateTime": "2026-10-01T06:17:00Z",
            },
        )

        now = datetime(2026, 10, 1, 6, 17, tzinfo=timezone.utc)
        first = project_mission_cell(self.db, self.work_id, now=now)
        second = project_mission_cell(self.db, self.work_id, now=now)

        self.assertEqual(
            first["continuity"]["worker_transition"]["id"],
            observed["transition_event_id"],
        )
        self.assertEqual(
            first["continuity"]["manager_wake_request"]["id"],
            observed["wake_event_id"],
        )
        self.assertEqual(first, second)

    def test_binding_reconciliation_requires_explicit_claim_release(self):
        with self.assertRaises(Exception):
            reconcile_binding(
                self.db,
                self.work_id,
                session_key="jules-123",
                reason="runtime target does not exist",
            )

        result = reconcile_binding(
            self.db,
            self.work_id,
            session_key="jules-123",
            reason="runtime target does not exist",
            release_claim=True,
        )
        again = reconcile_binding(
            self.db,
            self.work_id,
            session_key="jules-123",
            reason="runtime target does not exist",
            release_claim=True,
        )

        self.assertFalse(result["idempotent"])
        self.assertTrue(result["released_claim"])
        self.assertTrue(again["idempotent"])
        self.assertEqual(self.event_count("binding_reconciled"), 1)

        con = sqlite3.connect(self.db)
        claim_count = con.execute(
            "SELECT count(*) FROM claim WHERE work_id=?", (self.work_id,)
        ).fetchone()[0]
        work_status = con.execute(
            "SELECT status FROM work WHERE id=?", (self.work_id,)
        ).fetchone()[0]
        binding = con.execute(
            "SELECT status,ended_at FROM session_binding WHERE work_id=?",
            (self.work_id,),
        ).fetchone()
        con.close()

        self.assertEqual(claim_count, 0)
        self.assertEqual(work_status, "pending")
        self.assertEqual(binding[0], "failed")
        self.assertIsNotNone(binding[1])
        self.assertEqual(
            project_mission_cell(self.db, self.work_id)["next_action"]["action"],
            "DISPATCH_READY",
        )

    def test_manager_resolution_reconciles_orphan_binding_and_routes_reopen(self):
        observed = observe_bound_worker(
            self.db,
            self.work_id,
            {
                "id": "jules-123",
                "state": "COMPLETED",
                "updateTime": "2026-10-01T06:19:00Z",
                "outputs": [{"changeSet": {"description": "partial build evidence"}}],
            },
        )
        con = sqlite3.connect(self.db)
        con.execute("DELETE FROM claim WHERE work_id=?", (self.work_id,))
        con.commit()
        con.close()

        resolved = resolve_manager_wake(
            self.db,
            self.work_id,
            source_transition_event_id=observed["transition_event_id"],
            outcome="REOPEN_BUILD",
        )
        first = apply_manager_resolution(self.db, self.work_id)
        second = apply_manager_resolution(self.db, self.work_id)

        self.assertEqual(first["source_manager_wake_event_id"], resolved["event_id"])
        self.assertEqual(first["manager_outcome"], "REOPEN_BUILD")
        self.assertEqual(first["route"]["route_class"], "REOPEN")
        self.assertEqual(first["route"]["target_capability"], "RYAN")
        self.assertFalse(first["idempotent"])
        self.assertTrue(second["idempotent"])
        self.assertEqual(self.event_count("binding_reconciled"), 1)
        self.assertEqual(self.event_count("rory_reconcile_decision"), 1)
        self.assertEqual(self.event_count("continuation_routed"), 1)

        con = sqlite3.connect(self.db)
        row = con.execute(
            "SELECT status,ended_at FROM session_binding WHERE work_id=?",
            (self.work_id,),
        ).fetchone()
        con.close()
        self.assertEqual(row[0], "closed")
        self.assertIsNotNone(row[1])

        cell = project_mission_cell(self.db, self.work_id)
        self.assertIsNone(cell["ownership"]["binding"])
        self.assertEqual(cell["next_action"]["action"], "ROUTE_CONTINUATION")
        self.assertEqual(cell["next_action"]["route_class"], "REOPEN")
        self.assertEqual(cell["next_action"]["target_capability"], "RYAN")

    def test_manager_wake_resolution_is_idempotent(self):
        observed = observe_bound_worker(
            self.db,
            self.work_id,
            {
                "id": "jules-123",
                "state": "AWAITING_USER_FEEDBACK",
                "updateTime": "2026-10-01T06:18:00Z",
            },
        )
        first = resolve_manager_wake(
            self.db,
            self.work_id,
            source_transition_event_id=observed["transition_event_id"],
            outcome="MANAGER_REVIEWED",
        )
        second = resolve_manager_wake(
            self.db,
            self.work_id,
            source_transition_event_id=observed["transition_event_id"],
            outcome="MANAGER_REVIEWED",
        )

        self.assertFalse(first["idempotent"])
        self.assertTrue(second["idempotent"])
        self.assertEqual(first["event_id"], second["event_id"])
        self.assertEqual(self.event_count("manager_wake_resolved"), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
