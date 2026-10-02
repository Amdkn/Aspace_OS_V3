import json
import sqlite3
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from dispatch_routing import route_capability_need, resolve_ownership_conflict
from mission_watcher import (
    apply_manager_resolution,
    observe_bound_worker,
    reconcile_binding,
    resolve_manager_wake,
    record_contradiction,
    reconcile_contradiction
)

HERE = Path(__file__).resolve().parent
SCHEMA = HERE / "schema.sql"
CONSTITUTION_FILE = HERE / "companion_constitution_v2.json"

if str(HERE) not in __import__("sys").path:
    __import__("sys").path.insert(0, str(HERE))
from migration import apply_migration

class TestWargame314S3Mesh(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "uc.db"
        con = sqlite3.connect(self.db)
        con.executescript(SCHEMA.read_text(encoding="utf-8"))
        con.commit()
        con.close()

        apply_migration(str(self.db))

        with open(CONSTITUTION_FILE, "r") as f:
            self.constitution = json.load(f)

    def tearDown(self):
        self.tmp.cleanup()

    def test_1_parallel_mesh(self):
        con = sqlite3.connect(self.db)
        con.execute(
            "INSERT INTO work(id,layer,title,status,priority,attempts,institutional_owner,correlation_id) "
            "VALUES(314,'L2','adaptive.agent.behavior.routing','claimed',1,0,'companion_bill_research','corr-314')"
        )
        companions = [c['id'] for c in self.constitution['companions']]
        for i, comp_id in enumerate(companions):
            con.execute(
                "INSERT INTO session_binding(work_id,session_key,harness,capability,status,started_at,institutional_owner,runtime_id) "
                "VALUES(314, ?, 'jules', 'project', 'active', datetime('now'), ?, ?)",
                (f"sess-{i}", comp_id, f"rt-{i}")
            )
        con.commit()
        bindings = con.execute("SELECT institutional_owner FROM session_binding WHERE work_id=314").fetchall()
        self.assertEqual(len(bindings), 9)
        con.close()

    def test_2_runtime_replacement(self):
        con = sqlite3.connect(self.db)
        con.execute(
            "INSERT INTO work(id,layer,title,status,priority,attempts,institutional_owner,correlation_id) "
            "VALUES(315,'L2','test.replace','claimed',1,0,'companion_ryan_build','corr-315')"
        )
        con.execute(
            "INSERT INTO session_binding(work_id,session_key,harness,capability,status,started_at,institutional_owner,runtime_id) "
            "VALUES(315, 'sess-315', 'jules', 'project', 'active', datetime('now'), 'companion_ryan_build', 'rt-1')"
        )
        con.commit()
        con.close()

        reconcile_binding(self.db, 315, session_key="sess-315", reason="RUNTIME_CRASH", terminal_status="failed")

        con = sqlite3.connect(self.db)
        con.execute(
            "INSERT INTO session_binding(work_id,session_key,harness,capability,status,started_at,institutional_owner,runtime_id) "
            "VALUES(315, 'sess-315-new', 'jules', 'project', 'active', datetime('now'), 'companion_ryan_build', 'rt-2')"
        )
        con.commit()
        b_count = con.execute("SELECT COUNT(*) FROM session_binding WHERE work_id=315 AND status='active'").fetchone()[0]
        self.assertEqual(b_count, 1)
        con.close()

    def test_3_flow_defect_capability_need(self):
        con = sqlite3.connect(self.db)
        con.execute(
            "INSERT INTO work(id,layer,title,status,priority,attempts,institutional_owner,correlation_id) "
            "VALUES(316,'L2','test.flow','claimed',1,0,'companion_river_workflows','corr-316')"
        )
        con.commit()
        con.close()

        res = route_capability_need(
            self.db,
            316,
            source_harness="companion_river_workflows",
            target_capability="companion_ryan_build",
            evidence={"issue": "Flow failure due to adapter mismatch"}
        )
        self.assertEqual(res["target_capability"], "companion_ryan_build")
        con = sqlite3.connect(self.db)
        self.assertEqual(con.execute("SELECT status FROM work WHERE id=316").fetchone()[0], "pending")
        con.close()

    def test_4_observability_failure(self):
        con = sqlite3.connect(self.db)
        con.execute(
            "INSERT INTO work(id,layer,title,status,priority,attempts,institutional_owner,correlation_id) "
            "VALUES(317,'L2','test.obs','claimed',1,0,'companion_yaz_observe','corr-317')"
        )
        con.execute(
            "INSERT INTO claim(work_id,harness,claimed_at,expires_at,institutional_owner,runtime_id) "
            "VALUES(317, 'jules', datetime('now'), '2099-01-01T00:00:00+00:00', 'companion_yaz_observe', 'rt-1')"
        )
        con.execute(
            "INSERT INTO session_binding(work_id,session_key,harness,capability,status,started_at,institutional_owner,runtime_id) "
            "VALUES(317, 'sess-317', 'jules', 'project', 'active', datetime('now'), 'companion_yaz_observe', 'rt-1')"
        )
        con.execute(
            "INSERT INTO event(work_id,harness,kind,payload) VALUES(317, 'nardole-dispatch', 'dispatch_envelope', ?)",
            (json.dumps({
                "correlation_id": "corr-317",
                "return_route": {"mission": "317", "cell": "test-cell", "capability": "observe"},
                "required_capability": "observe"
            }),)
        )
        con.commit()
        con.close()

        observed = observe_bound_worker(self.db, 317, {"id": "sess-317", "state": "UNKNOWN", "updateTime": "2026-10-02T06:10:00Z"})
        self.assertEqual(observed["transition"], "UNKNOWN")

        resolve_manager_wake(self.db, 317, source_transition_event_id=observed["transition_event_id"], outcome="NO_DURABLE_EFFECT")
        reconcile_binding(self.db, 317, session_key="sess-317", reason="NO_DURABLE_EFFECT", release_claim=True)
        apply_manager_resolution(self.db, 317)

        con = sqlite3.connect(self.db)
        self.assertEqual(con.execute("SELECT status FROM work WHERE id=317").fetchone()[0], "pending")
        con.close()

    def test_5_contradiction_and_reconciliation(self):
        con = sqlite3.connect(self.db)
        con.execute(
            "INSERT INTO work(id,layer,title,status,priority,attempts,institutional_owner,correlation_id) "
            "VALUES(318,'L2','test.contradict','claimed',1,0,'companion_graham_backend','corr-318')"
        )
        con.commit()
        con.close()

        record_contradiction(self.db, 318, source_actor="companion_graham_backend", contradictory_evidence={"diff": "..."})
        reconcile_contradiction(self.db, 318, reconciler_actor="companion_rory_backend", resolution_rule="source_authority", survivor_state={"resolved": True})

        con = sqlite3.connect(self.db)
        events = [e[0] for e in con.execute("SELECT kind FROM event WHERE work_id=318").fetchall()]
        self.assertIn("contradiction_recorded", events)
        self.assertIn("reconciliation_rule", events)
        con.close()

    def test_6_ownership_resolution(self):
        con = sqlite3.connect(self.db)
        con.execute(
            "INSERT INTO work(id,layer,title,status,priority,attempts,institutional_owner,correlation_id) "
            "VALUES(319,'L2','test.owner','claimed',1,0,'companion_nardole_dispatch','corr-319')"
        )
        con.commit()
        con.close()

        resolve_ownership_conflict(self.db, 319, resolver_actor="companion_nardole_dispatch", chosen_owner="companion_clara_design", reason="contract mismatch")
        con = sqlite3.connect(self.db)
        evt = con.execute("SELECT payload FROM event WHERE work_id=319 AND kind='dispatch_routing_resolution'").fetchone()[0]
        self.assertEqual(json.loads(evt)["chosen_owner"], "companion_clara_design")
        con.close()

if __name__ == '__main__':
    unittest.main()
