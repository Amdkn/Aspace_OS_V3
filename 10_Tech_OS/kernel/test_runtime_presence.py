import json
import sqlite3
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from runtime_presence import project_agent_presence


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
        "INSERT INTO work(id,layer,title,status,parent_id,attempts) VALUES(1,'L1','Presence cell','pending',NULL,0)"
    )
    con.commit()
    return con


class RuntimePresenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = Path(self.tmp.name) / "uc.db"
        self.con = init_db(self.db)
        self.now = datetime(2026, 10, 1, 12, 0, tzinfo=timezone.utc)

    def tearDown(self):
        self.con.close()
        self.tmp.cleanup()

    def observe(self, *, active=True, expires_delta=30, degraded=None):
        return {
            "schema": "aspace.runtime-observation.v1",
            "identity": "jules-1",
            "provenance": "test-runtime",
            "observed_at": self.now.isoformat(),
            "expires_at": (self.now + timedelta(seconds=expires_delta)).isoformat(),
            "available": active,
            "degraded_reason": degraded,
            "evidence_refs": ["runtime:test"],
            "fencing_lease_identity": "fence:7",
            "capabilities": {"repo-implementation": "AVAILABLE"},
        }

    def bind(self, *, live_claim=True, session_key="jules-1"):
        if live_claim:
            self.con.execute(
                "INSERT OR REPLACE INTO claim(work_id,harness,claimed_at,expires_at) VALUES(1,'jules',?,?)",
                (
                    self.now.isoformat(),
                    (self.now + timedelta(minutes=10)).isoformat(),
                ),
            )
        self.con.execute(
            """INSERT INTO session_binding(
               work_id,session_key,harness,capability,external_ref,status,started_at,ended_at
               ) VALUES(1,?,'jules','repo-implementation',?,'active',?,NULL)""",
            (session_key, session_key, self.now.isoformat()),
        )
        self.con.commit()

    def test_fresh_runtime_without_binding_is_available(self):
        p = project_agent_presence(self.db, 1, self.observe(), now=self.now)
        self.assertEqual(p["state"], "AVAILABLE")
        self.assertEqual(p["fencing_lease_identity"], "fence:7")

    def test_live_claim_and_binding_is_bound(self):
        self.bind()
        p = project_agent_presence(self.db, 1, self.observe(), now=self.now)
        self.assertEqual(p["state"], "BOUND")

    def test_running_work_with_live_claim_binding_is_executing(self):
        self.bind()
        self.con.execute("UPDATE work SET status='in_progress' WHERE id=1")
        self.con.commit()
        p = project_agent_presence(self.db, 1, self.observe(), now=self.now)
        self.assertEqual(p["state"], "EXECUTING")

    def test_expired_runtime_is_stale(self):
        self.bind()
        p = project_agent_presence(
            self.db,
            1,
            self.observe(expires_delta=-1),
            now=self.now,
        )
        self.assertEqual(p["state"], "STALE")

    def test_offline_runtime_with_live_binding_is_degraded(self):
        self.bind()
        p = project_agent_presence(
            self.db,
            1,
            self.observe(active=False),
            now=self.now,
        )
        self.assertEqual(p["state"], "DEGRADED")
        self.assertEqual(p["reason"], "runtime_offline_with_work_binding")

    def test_binding_without_claim_is_degraded(self):
        self.bind(live_claim=False)
        p = project_agent_presence(self.db, 1, self.observe(), now=self.now)
        self.assertEqual(p["state"], "DEGRADED")
        self.assertEqual(p["reason"], "binding_without_live_claim")

    def test_no_runtime_and_no_binding_is_unknown(self):
        p = project_agent_presence(self.db, 1, None, now=self.now)
        self.assertEqual(p["state"], "UNKNOWN")

    def test_multiple_active_bindings_fail_degraded(self):
        self.bind(session_key="jules-1")
        self.con.execute(
            """INSERT INTO session_binding(
               work_id,session_key,harness,capability,external_ref,status,started_at,ended_at
               ) VALUES(1,'agy-2','antigravity','manager-review','agy-2','active',?,NULL)""",
            (self.now.isoformat(),),
        )
        self.con.commit()
        p = project_agent_presence(self.db, 1, self.observe(), now=self.now)
        self.assertEqual(p["state"], "DEGRADED")
        self.assertEqual(p["reason"], "multiple_active_bindings")

    def test_agent_os_camel_case_presence_is_accepted(self):
        p = project_agent_presence(
            self.db,
            1,
            {
                "identity": "worker-9",
                "provenance": "agent-os",
                "observedAt": int(self.now.timestamp() * 1000),
                "expiresAt": int((self.now + timedelta(seconds=5)).timestamp() * 1000),
                "ttlSeconds": 5,
                "active": True,
                "evidenceRefs": ["agent-os:presence"],
                "fencingLeaseIdentity": "fence:9",
                "capabilities": {"browser.dom.action": "AVAILABLE"},
            },
            now=self.now,
        )
        self.assertEqual(p["state"], "AVAILABLE")
        self.assertEqual(p["identity"], "worker-9")
        self.assertIn("agent-os:presence", p["evidence_refs"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
