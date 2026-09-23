import sqlite3
from contextlib import closing
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from concurrent.futures import ThreadPoolExecutor
import fleet_ownership as g
import kernel_fleet_tick as k


class OwnershipTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.db = Path(self.tmp.name) / "uc.db"
        with closing(sqlite3.connect(self.db)) as c, c:
            for name in ("schema.sql", "workgraph_v1.sql"):
                c.executescript((g.HERE / name).read_text(encoding="utf-8"))
            c.execute("INSERT INTO work(id,layer,title) VALUES(1,'L0','[KER-900] test')")

    def sql(self, query, args=()):
        with closing(sqlite3.connect(self.db)) as c, c:
            return c.execute(query, args).fetchall()

    def own(self):
        wid = g.reserve("KER-900", self.db)
        g.bind_session(wid, "123", self.db)
        return wid


    def test_fleet_lock_blocks_parallel_ticks_and_releases(self):
        lock = Path(self.tmp.name) / "fleet.lock"
        with g.dispatch_lock(lock):
            with self.assertRaisesRegex(ValueError, "another fleet"):
                with g.dispatch_lock(lock):
                    self.fail("concurrent dispatcher acquired the lock")
        with g.dispatch_lock(lock):
            pass

    def test_empty_supervisor_does_not_wake(self):
        self.assertFalse(g.supervisor_preflight(self.db)["wake"])

    def test_unknown_and_ambiguous_work_fail_closed(self):
        with self.assertRaises(ValueError):
            g.resolve_work("KER-901", self.db)
        self.sql("INSERT INTO work(layer,title) VALUES('L0','[KER-900] duplicate')")
        with self.assertRaises(ValueError):
            g.resolve_work("KER-900", self.db)

    def test_done_work_never_redispatched(self):
        self.sql("INSERT INTO prediction(work_id,claim_text,confidence) VALUES(1,'test',0.9)")
        self.sql("UPDATE work SET status='review' WHERE id=1")
        self.sql("UPDATE work SET status='done' WHERE id=1")
        with self.assertRaises(ValueError):
            g.reserve("KER-900", self.db)

    def test_dependency_blocks_launch(self):
        self.sql("INSERT INTO work(id,layer,title) VALUES(2,'L0','dependency')")
        self.sql("INSERT INTO work_dependency(work_id,depends_on_id) VALUES(1,2)")
        with self.assertRaises(ValueError):
            g.reserve("KER-900", self.db)

    def test_atomic_claim_only_one_dispatcher(self):
        def claim():
            try:
                return g.reserve("KER-900", self.db)
            except ValueError:
                return None
        with ThreadPoolExecutor(max_workers=2) as pool:
            values = list(pool.map(lambda _: claim(), range(2)))
        self.assertEqual(values.count(1), 1)
        self.assertEqual(self.sql("SELECT COUNT(*) FROM claim")[0][0], 1)

    def test_ambiguous_network_attempt_wakes_and_blocks_retry(self):
        g.reserve("KER-900", self.db)
        self.assertTrue(g.supervisor_preflight(self.db)["wake"])
        self.sql("DELETE FROM claim")
        self.sql("UPDATE work SET status='pending'")
        with self.assertRaisesRegex(ValueError, "requires reconciliation"):
            g.reserve("KER-900", self.db)

    def test_fresh_execution_requires_binding_and_lease(self):
        self.own()
        live = {"id": "123", "state": "IN_PROGRESS"}
        self.assertTrue(g.require_running_owner(1, "123", live, self.db))
        self.sql("UPDATE claim SET expires_at=datetime('now','-1 second')")
        with self.assertRaises(ValueError):
            g.require_running_owner(1, "123", live, self.db)

    def test_wrong_session_and_queued_are_not_execution(self):
        self.own()
        for observed in ({"id": "999", "state": "IN_PROGRESS"},
                         {"id": "123", "state": "QUEUED"},
                         {"id": "123", "state": "COMPLETED"}):
            with self.subTest(observed=observed), self.assertRaises(ValueError):
                g.require_running_owner(1, "123", observed, self.db)

    def test_closed_binding_is_not_execution(self):
        self.own()
        self.sql("UPDATE session_binding SET status='closed',ended_at=datetime('now')")
        with self.assertRaises(ValueError):
            g.require_running_owner(1, "123", {"id":"123","state":"IN_PROGRESS"}, self.db)

    def test_linear_mutation_blocked_without_ownership(self):
        with patch.object(k, "require_running_owner", side_effect=ValueError("no claim")), \
             patch.object(k, "run") as mutate:
            with self.assertRaises(ValueError):
                k.set_progress("KER-900", 1, "123", {"id":"123","state":"IN_PROGRESS"})
            mutate.assert_not_called()

    def test_busy_lane_never_receives_another_work(self):
        issue={"identifier":"KER-900","title":"build runtime","description":""}
        active=[{"id":"123","title":"ASPACE:KERNEL | RYAN | BUILD"}]
        with patch.object(k,"write_prd",return_value=k.ROOT/"brief.md"), \
             patch.object(k,"http_json") as network:
            with self.assertRaisesRegex(ValueError,"occupied"):
                k.create_or_continue_session(issue,"KERNEL_K0","KPRD-001",active)
            network.assert_not_called()


if __name__ == "__main__":
    unittest.main()
