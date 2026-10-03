import json
import os
import tempfile
import unittest
from datetime import datetime, timezone

from cubefarm_triwall import (
    ActorRegistry,
    CubeFarmTriWallProjection,
    build_agent_os_wall,
    build_business_os_wall,
    build_life_os_wall,
)


class TestCubeFarmTriWall(unittest.TestCase):
    def setUp(self):
        self.actor_registry = ActorRegistry()
        self.actor_registry.register_actor(
            actor_id="ryan",
            name="Ryan",
            roles=["S3", "BUILD", "Tech_OS"],
            metadata={"domain": "kernel"},
        )
        self.actor_registry.register_actor(
            actor_id="river",
            name="River",
            roles=["A3", "FLOW", "Life_OS"],
            metadata={"domain": "life"},
        )
        self.actor_registry.register_actor(
            actor_id="clara",
            name="Clara",
            roles=["B3", "DESIGN", "Business_OS"],
            metadata={"domain": "business"},
        )

    def test_agent_os_wall_projection(self):
        now = datetime.now(timezone.utc)
        agent_wall = build_agent_os_wall(
            capabilities=[{"value": "harness.list", "source": "agent_os.registry"}],
            adapters=[{"value": "mcp_adapter", "source": "agent_os.adapters"}],
            harness_bodies=[{"value": {"name": "Hermes", "actor_id": "ryan"}}],
            budgets={"value": {"tokens": 1000000, "currency": "USD", "lease": 50}},
            evidence=[{"value": "proof_123"}],
            workgraph_tasks=[{"value": "claim_task_1"}],
            actor_registry=self.actor_registry,
            observed_at=now,
        )

        self.assertEqual(agent_wall["wall"], "Agent OS")
        self.assertEqual(len(agent_wall["capabilities"]), 1)
        self.assertEqual(agent_wall["capabilities"][0]["truth_state"], "CURRENT")
        self.assertEqual(agent_wall["capabilities"][0]["value"], "harness.list")

        self.assertEqual(len(agent_wall["adapters"]), 1)
        self.assertEqual(agent_wall["adapters"][0]["truth_state"], "CURRENT")

        self.assertEqual(len(agent_wall["harness_bodies"]), 1)
        hb_val = agent_wall["harness_bodies"][0]["value"]
        self.assertEqual(hb_val["name"], "Hermes")
        self.assertIsNotNone(hb_val["actor_ref"])
        self.assertEqual(hb_val["actor_ref"]["name"], "Ryan")

        self.assertEqual(agent_wall["budgets"]["truth_state"], "CURRENT")
        self.assertEqual(agent_wall["budgets"]["value"]["lease"], 50)

    def test_life_os_wall_projection(self):
        now = datetime.now(timezone.utc)
        life_wall = build_life_os_wall(
            holons_a1_a2_a3=[{"value": {"holon_id": "A3_River", "actor_id": "river"}}],
            frameworks={
                "Ikigai": {"value": {"status": "ACTIVE"}, "linear_link": "https://linear.app/aspace/issue/LIFE-1"},
                "12WY": {"value": {"week": 4}, "gws_link": "https://calendar.google.com/event/12wy"},
                "Life Wheel": {"value": {"score": 8.5}},
                "PARA": {"value": {"projects": 12}},
                "GTD": {"value": {"inbox_count": 0}},
                "DEAL": {"value": {"automation_ratio": 0.8}},
            },
            actor_registry=self.actor_registry,
            observed_at=now,
        )

        self.assertEqual(life_wall["wall"], "Life OS")
        self.assertEqual(len(life_wall["holons"]), 1)
        holon_val = life_wall["holons"][0]["value"]
        self.assertEqual(holon_val["holon_id"], "A3_River")
        self.assertEqual(holon_val["actor_ref"]["name"], "River")

        fws = life_wall["frameworks"]
        for required in ["Ikigai", "12WY", "Life Wheel", "PARA", "GTD", "DEAL"]:
            self.assertIn(required, fws)
            self.assertEqual(fws[required]["truth_state"], "CURRENT")
            self.assertIn("linear_link", fws[required]["value"])
            self.assertIn("gws_link", fws[required]["value"])

        self.assertEqual(fws["12WY"]["value"]["gws_link"], "https://calendar.google.com/event/12wy")

    def test_business_os_wall_projection(self):
        now = datetime.now(timezone.utc)
        business_wall = build_business_os_wall(
            holons_b1_b2_b3=[{"value": {"holon_id": "B3_Clara", "actor_id": "clara"}}],
            franchises_products_domains=[{"value": "OMK Services"}],
            engineering_and_ops_state={"value": {"status": "OPERATIONAL", "mrr": 50000}},
            actor_registry=self.actor_registry,
            observed_at=now,
        )

        self.assertEqual(business_wall["wall"], "Business OS")
        self.assertEqual(len(business_wall["holons"]), 1)
        b_holon = business_wall["holons"][0]["value"]
        self.assertEqual(b_holon["actor_ref"]["name"], "Clara")

        self.assertEqual(len(business_wall["franchises_products_domains"]), 1)
        self.assertEqual(business_wall["franchises_products_domains"][0]["value"], "OMK Services")

        ops_state = business_wall["engineering_and_ops_state"]
        self.assertEqual(ops_state["truth_state"], "CURRENT")
        self.assertEqual(ops_state["value"]["status"], "OPERATIONAL")

    def test_actor_identity_unification(self):
        registry = ActorRegistry()
        registry.register_actor(actor_id="actor_omninet", name="OmniActor", roles=["S3"])
        # Registering same actor with additional role across walls
        registry.register_actor(actor_id="actor_omninet", name="OmniActor", roles=["A3"])
        registry.register_actor(actor_id="actor_omninet", name="OmniActor", roles=["B3"])

        actor = registry.get_actor("actor_omninet")
        self.assertIsNotNone(actor)
        self.assertEqual(actor["name"], "OmniActor")
        self.assertEqual(set(actor["roles"]), {"S3", "A3", "B3"})
        self.assertEqual(len(registry.to_dict()), 1)

    def test_canary_persistence_and_restart(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, "cubefarm_triwall_test.json")
            proj = CubeFarmTriWallProjection(storage_filepath=filepath)

            registry = proj.actor_registry
            registry.register_actor("ryan", "Ryan", ["S3", "BUILD"])
            registry.register_actor("river", "River", ["A3", "FLOW"])
            registry.register_actor("clara", "Clara", ["B3", "DESIGN"])

            now = datetime.now(timezone.utc)
            proj.render_triwall(
                agent_data={
                    "capabilities": [{"value": "harness.list"}],
                    "adapters": [{"value": "mcp_adapter"}],
                    "harness_bodies": [{"value": {"name": "Hermes", "actor_id": "ryan"}}],
                },
                life_data={
                    "holons": [{"value": {"holon_id": "A3_River", "actor_id": "river"}}],
                    "frameworks": {"12WY": {"value": {"week": 1}}},
                },
                business_data={
                    "holons": [{"value": {"holon_id": "B3_Clara", "actor_id": "clara"}}],
                    "domains": [{"value": "OMK Desktop"}],
                },
                canary_desk={
                    "desk_id": "desk_ryan_s3",
                    "actor_id": "ryan",
                    "runtimes": ["Hermes", "Codex", "Jules"],
                    "mission": "CubeFarm Canary Test",
                    "return_to": "#403",
                },
                observed_at=now,
            )

            saved_file = proj.save_triwall_state()
            self.assertTrue(os.path.exists(saved_file))

            # Simulate system restart / fresh instance rehydrating state
            proj2 = CubeFarmTriWallProjection(storage_filepath=filepath)
            loaded_data = proj2.load_triwall_state()

            self.assertIsNotNone(proj2.agent_wall)
            self.assertIsNotNone(proj2.life_wall)
            self.assertIsNotNone(proj2.business_wall)
            self.assertIsNotNone(proj2.canary_state)

            canary_desk = proj2.canary_state["agent_desk"]["value"]
            self.assertEqual(canary_desk["desk_id"], "desk_ryan_s3")
            self.assertEqual(canary_desk["actor_id"], "ryan")
            self.assertEqual(canary_desk["actor_ref"]["name"], "Ryan")
            self.assertEqual(canary_desk["return_to"], "#403")

            life_framework = proj2.canary_state["life_framework_projection"]["value"]
            self.assertEqual(life_framework["week"], 1)

            biz_holon = proj2.canary_state["business_hierarchy_projection"]["value"]
            self.assertEqual(biz_holon["holon_id"], "B3_Clara")
            self.assertEqual(biz_holon["actor_ref"]["name"], "Clara")


if __name__ == "__main__":
    unittest.main()
