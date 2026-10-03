import unittest
import importlib
import json
import os
from pathlib import Path

reg_module = importlib.import_module("80_Agent-OS.capability_fabric.registry")
CapabilityRegistry = reg_module.CapabilityRegistry

adapters_module = importlib.import_module("80_Agent-OS.capability_fabric.adapters")
CLIAdapter = adapters_module.CLIAdapter
APIAdapter = adapters_module.APIAdapter
MCPAdapter = adapters_module.MCPAdapter

life_module = importlib.import_module("20_Life_OS.life_capabilities")
register_life_capabilities = life_module.register_life_capabilities

class TestLifeCapabilitiesAdapterParity(unittest.TestCase):
    def setUp(self):
        self.registry = CapabilityRegistry()
        register_life_capabilities(self.registry)
        self.cli = CLIAdapter(self.registry)
        self.api = APIAdapter(self.registry)
        self.mcp = MCPAdapter(self.registry)

    def test_multi_surface_gtd_capture_parity(self):
        # 1. Test CLI Adapter
        cli_res = self.cli.invoke("life_gtd_inbox_capture", {"title": "CLI captured task", "category": "CLI"}, "corr-cli-gtd")
        self.assertEqual(cli_res["status"], "SUCCESS")
        self.assertEqual(cli_res["receipt"]["capability_id"], "life_gtd_inbox_capture")
        self.assertEqual(cli_res["receipt"]["correlation_id"], "corr-cli-gtd")
        self.assertEqual(cli_res["data"]["item"]["title"], "CLI captured task")

        # 2. Test API Adapter
        api_res = self.api.invoke("life_gtd_inbox_capture", {"title": "API captured task", "category": "API"}, "corr-api-gtd")
        self.assertEqual(api_res["status"], "SUCCESS")
        self.assertEqual(api_res["receipt"]["capability_id"], "life_gtd_inbox_capture")
        self.assertEqual(api_res["receipt"]["correlation_id"], "corr-api-gtd")
        self.assertEqual(api_res["data"]["item"]["title"], "API captured task")

        # 3. Test MCP Adapter
        mcp_res = self.mcp.invoke("life_gtd_inbox_capture", {"title": "MCP captured task", "category": "MCP"}, "corr-mcp-gtd")
        self.assertEqual(mcp_res["status"], "SUCCESS")
        self.assertEqual(mcp_res["receipt"]["capability_id"], "life_gtd_inbox_capture")
        self.assertEqual(mcp_res["receipt"]["correlation_id"], "corr-mcp-gtd")
        self.assertEqual(mcp_res["data"]["item"]["title"], "MCP captured task")

        # Verify state persistence
        inbox_file = Path("20_Life_OS/25_GTD_Cerritos/01_Inbox_Mariner/inbox_items.json")
        self.assertTrue(inbox_file.exists())
        with open(inbox_file, "r", encoding="utf-8") as f:
            items = json.load(f)
            titles = [i["title"] for i in items]
            self.assertIn("CLI captured task", titles)
            self.assertIn("API captured task", titles)
            self.assertIn("MCP captured task", titles)

    def test_life_wheel_sync_parity(self):
        scores = {"health": 9, "spirituality": 8, "career": 7}
        res = self.cli.invoke("life_wheel_sync", {"scores": scores}, "corr-wheel-cli")
        self.assertEqual(res["status"], "SUCCESS")
        self.assertEqual(res["data"]["scores"], scores)

        wheel_file = Path("20_Life_OS/22_Wheel_Discovery/wheel_state.json")
        self.assertTrue(wheel_file.exists())
        with open(wheel_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertEqual(data["scores"], scores)

if __name__ == "__main__":
    unittest.main()
