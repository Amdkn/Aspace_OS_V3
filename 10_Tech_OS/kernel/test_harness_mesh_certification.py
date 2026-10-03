import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent.parent
SCHEMA = HERE / "schema.sql"

if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
if str(REPO_ROOT / "80_Agent-OS") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "80_Agent-OS"))

from migration import apply_migration
import capability_fabric.harness_certification as h_cert
import capability_fabric.adapters as h_adapters
import capability_fabric.registry as h_reg
import capability_fabric.harness_list as h_list
import capability_fabric.capability_inspect as cap_inspect


class TestHarnessMeshCertificationIntegration(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "uc.db"
        con = sqlite3.connect(self.db)
        con.executescript(SCHEMA.read_text(encoding="utf-8"))
        con.commit()
        con.close()

        apply_migration(str(self.db))

        self.registry = h_reg.CapabilityRegistry()
        h_list.register_harness_list(self.registry)
        cap_inspect.register_capability_inspect(self.registry)

    def tearDown(self):
        self.tmp.cleanup()

    def test_shared_capability_contract_certified_across_3_harnesses(self):
        """Acceptance criteria: at least 3 harnesses PASS same contract."""
        pass_harnesses = ["hermes", "codex", "browser_bridge_chatgpt_web", "claude_code", "antigravity", "jules"]

        for h_id in pass_harnesses:
            adapter = h_adapters.HarnessMeshAdapter(self.registry, h_id)
            res = adapter.invoke_certified(
                capability_id="harness_list",
                payload={},
                actor_id="companion_ryan_build",
                authority_envelope="L2_EXECUTE",
                correlation_id=f"corr-mesh-{h_id}"
            )
            self.assertEqual(res["status"], "SUCCESS")
            self.assertEqual(res["certification"]["status"], "PASS")

            # Store in uc.db session_binding to verify persistence
            con = sqlite3.connect(self.db)
            con.execute(
                "INSERT INTO session_binding(work_id,session_key,harness,capability,status,started_at,institutional_owner,runtime_id) "
                "VALUES(412, ?, ?, 'harness_list', 'active', datetime('now'), 'companion_ryan_build', 'rt-sovereign-node-1')",
                (f"sess-{h_id}", h_id)
            )
            con.commit()
            con.close()

        con = sqlite3.connect(self.db)
        count = con.execute("SELECT COUNT(*) FROM session_binding WHERE work_id=412").fetchone()[0]
        self.assertEqual(count, len(pass_harnesses))
        con.close()

    def test_failover_preserves_actor_work_correlation_authority(self):
        """Acceptance criteria: one failover preserves actor/work/correlation/authority."""
        failover_event = h_cert.failover_harness(
            from_harness="hermes",
            to_harness="codex",
            actor_id="Doctor13",
            work_id=412,
            correlation_id="corr-failover-412",
            authority_envelope="L2_EXECUTE",
            capability_id="harness_list",
            fail_reason="HERMES_TIMEOUT"
        )

        con = sqlite3.connect(self.db)
        con.execute(
            "INSERT INTO work(id,layer,title,status,priority,attempts,institutional_owner,correlation_id) "
            "VALUES(412,'L2','harness.mesh.certification','claimed',1,0,'Doctor13','corr-failover-412')"
        )
        con.execute(
            "INSERT INTO event(work_id,harness,kind,payload) VALUES(412, 'hermes', 'harness_failover', ?)",
            (json.dumps(failover_event),)
        )
        con.commit()

        row = con.execute("SELECT payload FROM event WHERE work_id=412 AND kind='harness_failover'").fetchone()[0]
        payload = json.loads(row)

        self.assertEqual(payload["actor_id"], "Doctor13")
        self.assertEqual(payload["work_id"], 412)
        self.assertEqual(payload["correlation_id"], "corr-failover-412")
        self.assertEqual(payload["authority_envelope"], "L2_EXECUTE")
        self.assertEqual(payload["to_harness"], "codex")

        con.close()

    def test_agent_os_displays_separate_fields(self):
        """Acceptance criteria: Agent OS displays identity, runtime, adapter, capability, budget and evidence separately."""
        view = h_cert.get_harness_mesh_view(
            actor_id="companion_yaz_observe",
            runtime_id="rt-obs-1",
            adapter_type="CertifiedHarnessMeshAdapter",
            harness_id="claude_code",
            capability_id="capability_inspect",
            budget={"quota": "unlimited", "latency_ms": 10, "reliability_score": 1.0, "cost_cents": 0},
            evidence={"observed_effect": "Inspected 2 capabilities", "evidence_refs": ["ref-412"], "provenance": "Agent OS Registry"},
            correlation_id="corr-obs-412"
        )

        self.assertIn("identity", view)
        self.assertIn("runtime", view)
        self.assertIn("adapter", view)
        self.assertIn("capability", view)
        self.assertIn("budget", view)
        self.assertIn("evidence", view)

        self.assertEqual(view["identity"]["actor_id"], "companion_yaz_observe")
        self.assertEqual(view["runtime"]["runtime_id"], "rt-obs-1")
        self.assertEqual(view["adapter"]["harness_id"], "claude_code")
        self.assertEqual(view["capability"]["capability_id"], "capability_inspect")

    def test_unresolved_gaps_are_bounded_child_issues(self):
        """Acceptance criteria: unresolved gaps become bounded child issues, not silent fallback logic."""
        adapter = h_adapters.HarnessMeshAdapter(self.registry, "gemini")
        res = adapter.invoke_certified(
            capability_id="harness_list",
            payload={},
            actor_id="Doctor13",
            correlation_id="corr-gemini-gap"
        )
        self.assertEqual(res["status"], "CERTIFICATION_FAILED")
        self.assertIn("uncertified with a bounded gap", res["error"])


if __name__ == "__main__":
    unittest.main()
