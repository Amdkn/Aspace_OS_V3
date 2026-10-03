#!/usr/bin/env python3
import json
import pathlib
import unittest
from unittest.mock import patch, MagicMock

import jules_fleet_supervisor as jfs


class TestJulesFleetSupervisor(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = pathlib.Path("/tmp/jules_supervisor_tests")
        self.tmp_dir.mkdir(parents=True, exist_ok=True)
        self.p1 = jfs.JulesProfileConfig(profile_id="p1", credentials="tok1", max_capacity=2)
        self.p2 = jfs.JulesProfileConfig(profile_id="p2", credentials="tok2", max_capacity=3)
        self.supervisor = jfs.JulesFleetSupervisor(profiles=[self.p1, self.p2], reports_dir=self.tmp_dir)

    def test_inventory_check(self):
        mock_sessions = {
            "sessions": [
                {"id": "s1", "title": "KER-19", "state": "IN_PROGRESS"},
                {"id": "s2", "title": "KER-20", "state": "COMPLETED"},
            ]
        }
        with patch.object(self.supervisor, "_http_request") as mock_req:
            def side_effect(profile, path, **kwargs):
                if path == "/health":
                    return {"ok": True}
                if path == "/sessions":
                    return mock_sessions
                return {}

            mock_req.side_effect = side_effect
            inventory = self.supervisor.check_inventory()
            self.assertEqual(inventory.total_active_sessions, 2)  # 1 active per profile (2 total)
            self.assertEqual(inventory.total_available_capacity, 3)  # (2-1) + (3-1) = 3
            self.assertTrue(inventory.profiles["p1"].healthy)
            self.assertTrue(inventory.profiles["p2"].healthy)

    def test_prevent_duplicate_claims(self):
        active_sessions = [
            {"id": "s1", "title": "ASPACE:KERNEL | KER-19", "prompt": "Fix bug in KER-19"},
            {"id": "s2", "title": "ASPACE:LIFE | LPRD-01", "prompt": "Update life ritual"},
        ]
        self.assertTrue(self.supervisor.prevent_duplicate_claims(active_sessions, "KER-19"))
        self.assertFalse(self.supervisor.prevent_duplicate_claims(active_sessions, "KER-20"))

    def test_enforce_mutation_lease(self):
        with patch("jules_fleet_supervisor.reserve") as mock_reserve, \
             patch("jules_fleet_supervisor.bind_session") as mock_bind:
            mock_reserve.return_value = None
            mock_bind.return_value = None

            # First lease succeeds
            self.assertTrue(self.supervisor.enforce_mutation_lease("388", "sess_100"))
            self.assertEqual(self.supervisor.active_leases["388"], "sess_100")

            # Same session holds lease
            self.assertTrue(self.supervisor.enforce_mutation_lease("388", "sess_100"))

            # Different session rejected
            self.assertFalse(self.supervisor.enforce_mutation_lease("388", "sess_200"))

    def test_handle_waiting_states_approval(self):
        session = {"id": "s1", "state": "AWAITING_PLAN_APPROVAL", "requirePlanApproval": True}
        with patch.object(self.supervisor, "_http_request") as mock_req:
            mock_req.return_value = {"ok": True}
            handled = self.supervisor.handle_waiting_states(self.p1, session)
            self.assertTrue(handled)
            mock_req.assert_called_with(self.p1, "/sessions/s1/approve", method="POST", body={})

    def test_handle_waiting_states_feedback(self):
        session = {"id": "s2", "state": "ACTIVE"}
        mock_activities = {
            "activities": [
                {"type": "AWAITING_USER_INPUT"}
            ]
        }
        with patch.object(self.supervisor, "_http_request") as mock_req:
            def side_effect(profile, path, **kwargs):
                if path == "/sessions/s2/activities":
                    return mock_activities
                return {"ok": True}

            mock_req.side_effect = side_effect
            handled = self.supervisor.handle_waiting_states(self.p1, session)
            self.assertTrue(handled)

    def test_apply_retry_bounds(self):
        self.assertTrue(self.supervisor.apply_retry_bounds("work_418"))
        self.assertTrue(self.supervisor.apply_retry_bounds("work_418"))
        self.assertTrue(self.supervisor.apply_retry_bounds("work_418"))
        # 4th retry exceeds MAX_RETRIES_PER_WORK_ID (3)
        self.assertFalse(self.supervisor.apply_retry_bounds("work_418"))

    def test_consume_pr_and_close_work(self):
        session = {
            "id": "s3",
            "state": "COMPLETED",
            "pullRequest": {"url": "https://github.com/Amdkn/Aspace_OS_V3/pull/419"},
        }
        self.supervisor.active_leases["418"] = "s3"
        closure = self.supervisor.consume_pr_and_close_work(self.p1, session, "418")
        self.assertTrue(closure["closed"])
        self.assertTrue(closure["evidence_consumed"])
        self.assertNotIn("418", self.supervisor.active_leases)

    def test_export_fleet_state(self):
        inventory = jfs.FleetInventory()
        active_sessions = [{"id": "s1", "title": "KER-19", "state": "IN_PROGRESS"}]
        closures = [{"work_id": "388", "closed": True}]

        fleet_state = self.supervisor.export_fleet_state(inventory, active_sessions, closures)
        self.assertEqual(fleet_state["schema"], "aspace.jules.fleet_state.v1")
        self.assertEqual(fleet_state["active_sessions_count"], 1)
        self.assertEqual(fleet_state["closed_work_count"], 1)

        written_file = self.tmp_dir / "jules_fleet_state.json"
        self.assertTrue(written_file.exists())
        data = json.loads(written_file.read_text(encoding="utf-8"))
        self.assertEqual(data["cubefarm_integration"]["supervisor_role"], "RYAN")


if __name__ == "__main__":
    unittest.main()
