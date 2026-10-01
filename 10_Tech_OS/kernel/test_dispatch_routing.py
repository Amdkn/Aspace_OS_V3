import json
import sqlite3
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from dispatch_routing import (
    DispatchRoutingError,
    reserve_dispatch,
    route_reconcile_decision,
    select_runtime,
)
from mission_continuity import project_mission_cell


HERE = Path(__file__).resolve().parent
SCHEMA = HERE / "schema.sql"


class DispatchRoutingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "uc.db"
        self.lock = Path(self.tmp.name) / "dispatch.lock"
        con = sqlite3.connect(self.db)
        con.executescript(SCHEMA.read_text(encoding="utf-8"))
        con.execute(
            "INSERT INTO work(layer,title,status,priority,attempts) VALUES('L1','P2 cell','pending',1,0)"
        )
        self.work_id = int(con.execute("SELECT last_insert_rowid()").fetchone()[0])
        con.commit()
        con.close()

    def tearDown(self):
        self.tmp.cleanup()

    def candidate(self):
        return [{
            "runtime_id": "jules-runtime-1",
            "harness": "jules",
            "presence_state": "AVAILABLE",
            "capabilities": {"repo-implementation": "AVAILABLE"},
            "healthy": True,
            "quota_ok": True,
            "priority": 10,
        }]

    def return_route(self):
        return {"mission": "#291", "cell": "#295", "capability": "FLOW"}

    def insert_event(self, kind, payload, harness="test"):
        con = sqlite3.connect(self.db)
        cur = con.execute(
            "INSERT INTO event(work_id,harness,kind,payload) VALUES(?,?,?,?)",
            (self.work_id, harness, kind, json.dumps(payload)),
        )
        con.commit()
        event_id = int(cur.lastrowid)
        con.close()
        return event_id

    def test_runtime_selection_backpressures_when_no_safe_candidate(self):
        result = select_runtime(
            "repo-implementation",
            [{
                "runtime_id": "busy",
                "harness": "jules",
                "presence_state": "EXECUTING",
                "capabilities": {"repo-implementation": "AVAILABLE"},
            }],
        )
        self.assertEqual(result["decision"], "BACKPRESSURE")
        self.assertEqual(result["reason"], "no_safe_runtime")

    def test_backpressure_is_durable_and_visible_in_mission_cell(self):
        result = reserve_dispatch(
            self.db,
            self.work_id,
            required_capability="repo-implementation",
            candidates=[],
            return_route=self.return_route(),
            correlation_id="corr-pressure",
            lock_path=self.lock,
        )
        self.assertEqual(result["decision"], "BACKPRESSURE")
        cell = project_mission_cell(self.db, self.work_id)
        self.assertEqual(cell["next_action"]["action"], "BACKPRESSURE")
        self.assertEqual(cell["next_action"]["required_capability"], "repo-implementation")
        self.assertEqual(cell["correlation_id"], "corr-pressure")

    def test_reserve_claims_once_and_duplicate_dispatch_fails_closed(self):
        first = reserve_dispatch(
            self.db,
            self.work_id,
            required_capability="repo-implementation",
            candidates=self.candidate(),
            return_route=self.return_route(),
            correlation_id="corr-1",
            lock_path=self.lock,
        )
        self.assertEqual(first["decision"], "DISPATCH")
        self.assertEqual(first["envelope"]["correlation_id"], "corr-1")

        with self.assertRaises(DispatchRoutingError):
            reserve_dispatch(
                self.db,
                self.work_id,
                required_capability="repo-implementation",
                candidates=self.candidate(),
                return_route=self.return_route(),
                correlation_id="corr-1",
                lock_path=self.lock,
            )

        con = sqlite3.connect(self.db)
        claims = con.execute("SELECT count(*) FROM claim WHERE work_id=?", (self.work_id,)).fetchone()[0]
        attempts = con.execute(
            "SELECT count(*) FROM event WHERE work_id=? AND kind='fleet_dispatch_attempt'",
            (self.work_id,),
        ).fetchone()[0]
        con.close()
        self.assertEqual(claims, 1)
        self.assertEqual(attempts, 1)

    def test_dependency_creates_backpressure_without_claim(self):
        con = sqlite3.connect(self.db)
        con.execute(
            "INSERT INTO work(layer,title,status,priority,attempts) VALUES('L1','blocker','pending',1,0)"
        )
        blocker = int(con.execute("SELECT last_insert_rowid()").fetchone()[0])
        con.execute(
            "INSERT INTO work_dependency(work_id,depends_on_id,kind) VALUES(?,?, 'requires')",
            (self.work_id, blocker),
        )
        con.commit()
        con.close()

        result = reserve_dispatch(
            self.db,
            self.work_id,
            required_capability="repo-implementation",
            candidates=self.candidate(),
            return_route=self.return_route(),
            correlation_id="corr-dep",
            lock_path=self.lock,
        )
        self.assertEqual(result["decision"], "BACKPRESSURE")
        self.assertEqual(result["backpressure"]["reason"], "dependency_blocked")

        con = sqlite3.connect(self.db)
        self.assertEqual(
            con.execute("SELECT count(*) FROM claim WHERE work_id=?", (self.work_id,)).fetchone()[0],
            0,
        )
        con.close()

    def test_retry_safe_requires_receipt_permission_and_known_effect(self):
        self.insert_event(
            "harness_execution_receipt",
            {
                "correlation_id": "corr-retry",
                "return_route": self.return_route(),
                "effect_state": "UNKNOWN",
                "retry_safe": True,
            },
            "runtime",
        )
        self.insert_event(
            "rory_reconcile_decision",
            {
                "correlation_id": "corr-retry",
                "return_route": self.return_route(),
                "verdict": "RETRY_SAFE",
            },
            "rory-cohere",
        )
        with self.assertRaises(DispatchRoutingError):
            route_reconcile_decision(self.db, self.work_id)

    def test_retry_route_is_idempotent_and_preserves_identity(self):
        self.insert_event(
            "dispatch_envelope",
            {
                "correlation_id": "corr-safe",
                "return_route": self.return_route(),
                "required_capability": "repo-implementation",
            },
            "nardole-dispatch",
        )
        receipt_id = self.insert_event(
            "harness_execution_receipt",
            {
                "correlation_id": "corr-safe",
                "return_route": self.return_route(),
                "effect_state": "FAILED_BEFORE_EFFECT",
                "retry_safe": True,
            },
            "runtime",
        )
        self.insert_event(
            "rory_reconcile_decision",
            {
                "correlation_id": "corr-safe",
                "return_route": self.return_route(),
                "verdict": "RETRY_SAFE",
            },
            "rory-cohere",
        )

        first = route_reconcile_decision(self.db, self.work_id)
        second = route_reconcile_decision(self.db, self.work_id)
        self.assertEqual(first["route_class"], "RETRY")
        self.assertEqual(first["target_capability"], "repo-implementation")
        self.assertEqual(first["correlation_id"], "corr-safe")
        self.assertEqual(first["source_receipt_event_id"], receipt_id)
        self.assertFalse(first["idempotent"])
        self.assertTrue(second["idempotent"])
        self.assertEqual(first["event_id"], second["event_id"])

    def test_recover_unknown_routes_to_donna_not_retry(self):
        self.insert_event(
            "harness_execution_receipt",
            {
                "correlation_id": "corr-unknown",
                "return_route": self.return_route(),
                "effect_state": "UNKNOWN",
                "retry_safe": False,
            },
            "runtime",
        )
        self.insert_event(
            "rory_reconcile_decision",
            {
                "correlation_id": "corr-unknown",
                "return_route": self.return_route(),
                "verdict": "RECOVER_UNKNOWN",
            },
            "rory-cohere",
        )
        routed = route_reconcile_decision(self.db, self.work_id)
        self.assertEqual(routed["route_class"], "RECOVER")
        self.assertEqual(routed["target_capability"], "DONNA")

    def test_complete_materializes_durable_terminal_route(self):
        self.insert_event(
            "harness_execution_receipt",
            {
                "correlation_id": "corr-done",
                "return_route": self.return_route(),
                "effect_state": "SUCCEEDED",
                "retry_safe": False,
            },
            "runtime",
        )
        self.insert_event(
            "rory_reconcile_decision",
            {
                "correlation_id": "corr-done",
                "return_route": self.return_route(),
                "verdict": "COMPLETE",
            },
            "rory-cohere",
        )
        routed = route_reconcile_decision(self.db, self.work_id)
        self.assertEqual(routed["route_class"], "DONE")
        self.assertEqual(routed["correlation_id"], "corr-done")

    def test_reopen_build_routes_to_ryan(self):
        self.insert_event(
            "rory_reconcile_decision",
            {
                "correlation_id": "corr-reopen",
                "return_route": self.return_route(),
                "verdict": "REOPEN_BUILD",
                "reopen_cell": "cell-build",
            },
            "rory-cohere",
        )
        routed = route_reconcile_decision(self.db, self.work_id)
        self.assertEqual(routed["route_class"], "REOPEN")
        self.assertEqual(routed["target_capability"], "RYAN")
        self.assertEqual(routed["reopen_cell"], "cell-build")


    def test_route_reconcile_decision_handles_accept_continue_with_on_success(self):
        self.insert_event(
            "rory_reconcile_decision",
            {
                "correlation_id": "corr-accept",
                "return_route": {"on_success": "rory-cohere"},
                "verdict": "ACCEPT_CONTINUE",
            },
            "rory-cohere",
        )
        routed = route_reconcile_decision(self.db, self.work_id)
        self.assertEqual(routed["route_class"], "NEXT_FLOW")
        self.assertEqual(routed["target_capability"], "rory-cohere")

    def test_reserve_dispatch_consumes_route_continuation(self):
        self.insert_event(
            "continuation_routed",
            {
                "correlation_id": "corr-cont",
                "return_route": self.return_route(),
                "route_class": "REOPEN",
                "target_capability": "RYAN",
                "verdict": "REOPEN_BUILD",
            },
            "nardole-dispatch",
        )

        result = reserve_dispatch(
            self.db,
            self.work_id,
            required_capability="RYAN",
            candidates=[{
                "runtime_id": "ryan-runtime",
                "harness": "ryan",
                "presence_state": "AVAILABLE",
                "capabilities": {"RYAN": "AVAILABLE"},
                "healthy": True,
                "quota_ok": True,
                "priority": 10,
            }],
            return_route=self.return_route(),
            correlation_id="corr-cont-new",
            lock_path=self.lock,
        )
        self.assertEqual(result["decision"], "DISPATCH")
        self.assertEqual(result["envelope"]["required_capability"], "RYAN")
        # reserve_dispatch preserves cell's correlation_id over the newly provided one
        self.assertEqual(result["envelope"]["correlation_id"], "corr-cont")
        self.assertFalse(result["envelope"]["retry"])

    def test_reserve_dispatch_fails_on_route_continuation_mismatch(self):
        self.insert_event(
            "continuation_routed",
            {
                "correlation_id": "corr-cont",
                "return_route": self.return_route(),
                "route_class": "REOPEN",
                "target_capability": "RYAN",
                "verdict": "REOPEN_BUILD",
            },
            "nardole-dispatch",
        )

        with self.assertRaisesRegex(DispatchRoutingError, "does not match durable route RYAN"):
            reserve_dispatch(
                self.db,
                self.work_id,
                required_capability="repo-implementation",
                candidates=self.candidate(),
                return_route=self.return_route(),
                correlation_id="corr-cont",
                lock_path=self.lock,
            )

    def test_unknown_effect_is_never_automatically_retried_via_route_continuation(self):
        self.insert_event(
            "continuation_routed",
            {
                "correlation_id": "corr-unknown",
                "return_route": self.return_route(),
                "route_class": "RECOVER",
                "target_capability": "DONNA",
                "verdict": "RECOVER_UNKNOWN",
            },
            "nardole-dispatch",
        )
        # Verify it routes to DONNA (recovery) and cannot be dispatched as a retry for the original capability
        with self.assertRaisesRegex(DispatchRoutingError, "does not match durable route DONNA"):
            reserve_dispatch(
                self.db,
                self.work_id,
                required_capability="repo-implementation",
                candidates=self.candidate(),
                return_route=self.return_route(),
                correlation_id="corr-unknown",
                lock_path=self.lock,
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
