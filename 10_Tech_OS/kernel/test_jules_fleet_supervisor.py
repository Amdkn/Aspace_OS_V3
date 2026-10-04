#!/usr/bin/env python3
import json
import pathlib
import tempfile
import unittest
from unittest.mock import patch

import jules_fleet_supervisor as jfs


class TestJulesFleetSupervisor(unittest.TestCase):
    def setUp(self):
        self.p1 = jfs.JulesProfileConfig(
            profile_id="OMK",
            api_key="k1",
            concurrency_cap=3,
            allowed_sources=("sources/github/Amdkn/Aspace_OS_V3",),
        )
        self.p2 = jfs.JulesProfileConfig(
            profile_id="Papa",
            api_key="k2",
            concurrency_cap=3,
            allowed_sources=("sources/github/Amdkn/Aspace_OS_V3",),
        )
        self.s = jfs.JulesFleetSupervisor([self.p1, self.p2], reports_dir=pathlib.Path("/tmp/jules"))

    def test_inventory_uses_supplied_capacity_not_hardcoded_quota(self):
        with patch.object(self.s, "list_sources", return_value=[{"name": "repo"}]), patch.object(
            self.s,
            "list_sessions",
            side_effect=[
                [{"id": "1", "state": "IN_PROGRESS"}, {"id": "2", "state": "COMPLETED"}],
                [{"id": "3", "state": "IN_PROGRESS"}, {"id": "4", "state": "IN_PROGRESS"}],
            ],
        ):
            inv = self.s.inventory()
        self.assertEqual(inv.profiles["OMK"].available_capacity, 2)
        self.assertEqual(inv.profiles["Papa"].available_capacity, 1)
        self.assertEqual(inv.total_active, 3)

    def test_inventory_allows_unknown_provider_capacity(self):
        p = jfs.JulesProfileConfig("x", "k", None, ("sources/github/Amdkn/Aspace_OS_V3",))
        s = jfs.JulesFleetSupervisor([p])
        with patch.object(s, "list_sources", return_value=[]), patch.object(s, "list_sessions", return_value=[]):
            inv = s.inventory()
        self.assertIsNone(inv.profiles["x"].available_capacity)
        self.assertIsNone(inv.total_available)

    def test_exact_duplicate_issue_detection(self):
        sessions = [{"title": "[FLEET] #418 supervisor"}, {"title": "issue #1418 unrelated"}]
        self.assertTrue(self.s.issue_claimed(418, sessions))
        self.assertFalse(self.s.issue_claimed(419, sessions))

    def test_waiting_plan_uses_official_action(self):
        with patch.object(self.s, "_request", return_value={}) as req:
            self.assertTrue(self.s.handle_waiting_state(self.p1, {"id": "abc", "state": "AWAITING_PLAN_APPROVAL"}))
        req.assert_called_once_with(self.p1, "sessions/abc:approvePlan", method="POST", body={})

    def test_feedback_uses_official_send_message_action(self):
        with patch.object(self.s, "_request", return_value={}) as req:
            self.assertTrue(self.s.handle_waiting_state(self.p1, {"id": "abc", "state": "AWAITING_USER_FEEDBACK"}))
        self.assertIn(":sendMessage", req.call_args.args[1])

    def test_create_session_uses_auto_create_pr_and_source_context(self):
        with patch.object(self.s, "_request", return_value={"id": "s1", "state": "QUEUED"}) as req:
            result = self.s.create_session(
                self.p1,
                issue_number=418,
                issue_title="fleet",
                prompt="do it",
                source="sources/github/Amdkn/Aspace_OS_V3",
            )
        self.assertEqual(result["id"], "s1")
        body = req.call_args.kwargs["body"]
        self.assertEqual(body["automationMode"], "AUTO_CREATE_PR")
        self.assertEqual(body["sourceContext"]["githubRepoContext"]["startingBranch"], "main")

    def test_refill_uses_free_slots_without_duplicate_claims(self):
        with patch.object(
            self.s,
            "inventory",
            return_value=jfs.FleetInventory(
                {
                    "OMK": jfs.JulesProfileState("OMK", True, 2, 3, 1, 42),
                    "Papa": jfs.JulesProfileState("Papa", True, 3, 3, 0, 42),
                }
            ),
        ), patch.object(
            self.s,
            "list_sessions",
            return_value=[{"id": "old", "state": "IN_PROGRESS", "title": "#418"}],
        ), patch.object(
            self.s,
            "create_session",
            return_value={"id": "new", "state": "QUEUED", "title": "#419"},
        ) as create:
            launched = self.s.refill(
                [
                    {"issue_number": 418, "title": "duplicate"},
                    {"issue_number": 419, "title": "new"},
                ],
                source="sources/github/Amdkn/Aspace_OS_V3",
                prompt_builder=lambda item: item["title"],
            )
        self.assertEqual(len(launched), 1)
        self.assertEqual(launched[0]["issue_number"], 419)
        self.assertEqual(create.call_count, 1)

    def test_consume_completed_closes_only_after_acceptance(self):
        closed = []
        session = {"id": "s1", "state": "COMPLETED", "pullRequest": {"url": "x"}}
        result = self.s.consume_completed(
            self.p1,
            session,
            work_id="418",
            acceptance=lambda _: True,
            close_work=lambda wid, _: closed.append(wid),
        )
        self.assertTrue(result["accepted"])
        self.assertEqual(closed, ["418"])


    def test_registry_redirects_local_only_repo_to_durable_backing(self):
        with tempfile.TemporaryDirectory() as tmp:
            registry = pathlib.Path(tmp) / "registry.json"
            registry.write_text(
                json.dumps(
                    {
                        "repositories": {
                            "satellites": {
                                "agent_os": {
                                    "repo": "Amdkn/Agent-OS",
                                    "bootstrap": "local_only",
                                    "desktop_snapshot": {
                                        "sync": "pushed_to_Amdkn/Agent-OS-Desktop"
                                    },
                                },
                                "agent_os_desktop": {
                                    "repo": "Amdkn/Agent-OS-Desktop",
                                    "bootstrap": "auto",
                                },
                            }
                        }
                    }
                ),
                encoding="utf-8",
            )
            routes = jfs.load_workspace_source_routes(registry)

        self.assertEqual(
            routes["sources/github/Amdkn/Agent-OS"],
            ("sources/github/Amdkn/Agent-OS-Desktop", None),
        )

        profile = jfs.JulesProfileConfig(
            profile_id="OMK",
            api_key="k",
            concurrency_cap=3,
            allowed_sources=("sources/github/Amdkn/Agent-OS",),
        )
        supervisor = jfs.JulesFleetSupervisor(
            [profile],
            source_routes=routes,
        )
        with patch.object(
            supervisor,
            "_request",
            return_value={"id": "s1", "state": "QUEUED"},
        ) as req:
            supervisor.create_session(
                profile,
                issue_number=1,
                issue_title="Agent OS",
                prompt="execute",
                source="sources/github/Amdkn/Agent-OS",
                starting_branch="main",
            )

        body = req.call_args.kwargs["body"]
        self.assertEqual(
            body["sourceContext"]["source"],
            "sources/github/Amdkn/Agent-OS-Desktop",
        )
        self.assertEqual(
            body["sourceContext"]["githubRepoContext"]["startingBranch"],
            "main",
        )

    def test_source_preflight_blocks_session_creation(self):
        profile = jfs.JulesProfileConfig(
            profile_id="OMK",
            api_key="k",
            concurrency_cap=3,
            allowed_sources=("sources/github/Amdkn/empty",),
        )
        supervisor = jfs.JulesFleetSupervisor(
            [profile],
            source_routes={},
            source_preflight=lambda source, branch: False,
        )
        with patch.object(supervisor, "_request") as req:
            with self.assertRaisesRegex(ValueError, "preflight failed"):
                supervisor.create_session(
                    profile,
                    issue_number=1,
                    issue_title="empty repo",
                    prompt="execute",
                    source="sources/github/Amdkn/empty",
                    starting_branch="main",
                )
        req.assert_not_called()

    def test_refill_uses_per_work_item_source(self):
        profile = jfs.JulesProfileConfig(
            profile_id="OMK",
            api_key="k",
            concurrency_cap=1,
            allowed_sources=(
                "sources/github/Amdkn/Aspace_OS_V3",
                "sources/github/Amdkn/cubefarm",
            ),
        )
        supervisor = jfs.JulesFleetSupervisor(
            [profile],
            source_routes={},
        )
        with patch.object(
            supervisor,
            "inventory",
            return_value=jfs.FleetInventory(
                {"OMK": jfs.JulesProfileState("OMK", True, 0, 1, 1, 2)}
            ),
        ), patch.object(
            supervisor,
            "list_sessions",
            return_value=[],
        ), patch.object(
            supervisor,
            "create_session",
            return_value={"id": "new", "state": "QUEUED"},
        ) as create:
            launched = supervisor.refill(
                [
                    {
                        "issue_number": 421,
                        "title": "CubeFarm",
                        "source": "sources/github/Amdkn/cubefarm",
                    }
                ],
                source="sources/github/Amdkn/Aspace_OS_V3",
                prompt_builder=lambda item: item["title"],
            )

        self.assertEqual(len(launched), 1)
        self.assertEqual(
            create.call_args.kwargs["source"],
            "sources/github/Amdkn/cubefarm",
        )


if __name__ == "__main__":
    unittest.main()
