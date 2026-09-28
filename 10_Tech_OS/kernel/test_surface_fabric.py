#!/usr/bin/env python3
import unittest
from surface_fabric import SurfaceFabric


class TestSharedSurfaceFabric(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fabric = SurfaceFabric()

    def test_stewards_are_defaults_not_access_barriers(self):
        expected = {
            "linear": "Rory",
            "github": "Ryan",
            "agent_os": "Yaz",
            "omarchy": "Yaz",
            "tinybird": "Yaz",
            "supabase": "Graham",
            "herdr": "Amy",
            "gws": "River",
        }
        for surface, steward in expected.items():
            self.assertEqual(self.fabric.surface(surface)["steward"], steward)
            self.assertTrue(self.fabric.surface(surface)["shared"])

    def test_cross_agent_surface_use_is_allowed(self):
        self.assertTrue(self.fabric.can_use("Bill", "github", "issues"))
        self.assertTrue(self.fabric.can_use("Ryan", "linear", "issue_tracking"))
        self.assertTrue(self.fabric.can_use("Rory", "supabase", "rls"))
        self.assertTrue(self.fabric.can_use("River", "herdr", "session_habitat"))
        self.assertTrue(self.fabric.can_use("Amy", "gws", "calendar"))

    def test_capability_not_persona_drives_selection(self):
        result = self.fabric.select("Bill", "issues")
        self.assertEqual(result["candidates"][0]["surface"], "github")
        self.assertFalse(result["candidates"][0]["is_steward"])

        result = self.fabric.select("Rory", "issue_tracking")
        self.assertEqual(result["candidates"][0]["surface"], "linear")
        self.assertTrue(result["candidates"][0]["is_steward"])

    def test_herdr_mounts_multiple_harnesses(self):
        mounted = set(self.fabric.surface("herdr")["mounted_harnesses"])
        self.assertTrue({"antigravity", "codex", "claude_code", "hermes_agent", "deepseek_harness"} <= mounted)

    def test_life_business_composition_is_explicit(self):
        comp = self.fabric.data["composition"]["life_business_nested_delivery"]
        self.assertEqual(comp["life_layers"], ["A1", "A2", "A3"])
        self.assertEqual(comp["business_layers"], ["B1", "B2", "B3"])
        self.assertEqual(comp["planning"], ["PARA", "12WY"])
        self.assertEqual(comp["workflow_surface"], "gws")


if __name__ == "__main__":
    unittest.main()
