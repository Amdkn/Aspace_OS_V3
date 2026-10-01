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

class KernelP4CanaryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "uc.db"
        con = sqlite3.connect(self.db)
        con.executescript(SCHEMA.read_text(encoding="utf-8"))
        con.commit()
        con.close()

    def tearDown(self):
        self.tmp.cleanup()

    def test_p4_continuity_steps_1_to_12(self):
        con = sqlite3.connect(self.db)

        # Step 1: Create work
        con.execute(
            "INSERT INTO work(id,layer,title,status,priority,attempts) "
            "VALUES(193,'L2','Mission #297','claimed',1,0)"
        )
        # Step 2: Claim
        con.execute(
            "INSERT INTO claim(work_id,harness,claimed_at,expires_at) "
            "VALUES(193, 'jules', datetime('now'), '2099-01-01T00:00:00+00:00')"
        )
        # Step 3: Session binding
        con.execute(
            """INSERT INTO session_binding(
                 work_id,session_key,harness,capability,external_ref,status,started_at,ended_at
               ) VALUES(193, 'jules-4237535969551815147', 'jules', 'recovery',
                        'gh297-kernel-p4-20261001', 'active', datetime('now'), NULL)"""
        )
        # Step 4: Dispatch envelope
        con.execute(
            """INSERT INTO event(work_id,harness,kind,payload)
               VALUES(193, 'nardole-dispatch', 'dispatch_envelope', ?)""",
            (
                json.dumps(
                    {
                        "correlation_id": "gh297-kernel-p4-20261001",
                        "return_route": {
                            "mission": "#297",
                            "cell": "kernel-continuity-p4-canary",
                            "capability": "recovery",
                        },
                        "required_capability": "recovery",
                    }
                ),
            ),
        )
        con.commit()
        con.close()

        # Step 5: Observe worker -> UNKNOWN
        observation = {
            "id": "jules-4237535969551815147",
            "state": "UNKNOWN",
            "updateTime": "2026-10-01T06:10:00Z",
        }
        observed = observe_bound_worker(self.db, 193, observation)
        self.assertEqual(observed["transition"], "UNKNOWN")
        self.assertTrue(observed["manager_wake_required"])

        # Step 6: Verify manager wake requested event
        con = sqlite3.connect(self.db)
        wake_event = con.execute("SELECT payload FROM event WHERE work_id=193 AND kind='manager_wake_requested'").fetchone()
        self.assertIsNotNone(wake_event)

        # Step 7: Resolve manager wake with NO_DURABLE_EFFECT
        resolved = resolve_manager_wake(
            self.db,
            193,
            source_transition_event_id=observed["transition_event_id"],
            outcome="NO_DURABLE_EFFECT",
        )
        self.assertEqual(resolved["outcome"], "NO_DURABLE_EFFECT")

        # Step 8: Apply manager resolution (reopens BUILD and routes continuation)
        reconcile_binding(self.db, 193, session_key="jules-4237535969551815147", reason="NO_DURABLE_EFFECT", release_claim=True)
        first_apply = apply_manager_resolution(self.db, 193)
        self.assertEqual(first_apply["manager_outcome"], "NO_DURABLE_EFFECT")

        # Re-check events
        # Step 9: Reconcile decision
        reconcile_decision_event = con.execute("SELECT payload FROM event WHERE work_id=193 AND kind='rory_reconcile_decision'").fetchone()
        self.assertIsNotNone(reconcile_decision_event)

        # Step 10: Continuation routed
        route_event = con.execute("SELECT payload FROM event WHERE work_id=193 AND kind='continuation_routed'").fetchone()
        self.assertIsNotNone(route_event)

        # Step 11: Verify work is pending again
        work_status = con.execute("SELECT status FROM work WHERE id=193").fetchone()[0]
        self.assertEqual(work_status, "pending")

        # Step 12: Verify binding is closed/failed
        binding_status = con.execute("SELECT status FROM session_binding WHERE work_id=193").fetchone()[0]
        self.assertEqual(binding_status, "failed")
        con.close()

if __name__ == "__main__":
    unittest.main()
