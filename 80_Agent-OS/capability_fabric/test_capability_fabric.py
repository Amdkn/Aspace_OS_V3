import unittest
from .registry import CapabilityRegistry
from .adapters import CLIAdapter, APIAdapter, MCPAdapter
from .harness_list import register_harness_list

class TestCapabilityFabric(unittest.TestCase):
    def setUp(self):
        self.registry = CapabilityRegistry()
        register_harness_list(self.registry)

    def test_registry_registration(self):
        capabilities = self.registry.list_capabilities()
        self.assertEqual(len(capabilities), 1)
        self.assertEqual(capabilities[0].capability_id, "harness_list")

    def test_cli_adapter_invocation(self):
        cli = CLIAdapter(self.registry)
        result = cli.invoke("harness_list", {"filter": "all"}, "corr-cli-123")
        self.assertEqual(result["status"], "SUCCESS")
        self.assertEqual(result["receipt"]["correlation_id"], "corr-cli-123")
        self.assertEqual(result["receipt"]["observed_effect"], "Listed 4 harnesses with filter 'all'")

    def test_api_adapter_invocation(self):
        api = APIAdapter(self.registry)
        result = api.invoke("harness_list", {"filter": "active"}, "corr-api-123")
        self.assertEqual(result["status"], "SUCCESS")
        self.assertEqual(result["receipt"]["correlation_id"], "corr-api-123")
        self.assertEqual(result["receipt"]["observed_effect"], "Listed 2 harnesses with filter 'active'")

    def test_mcp_adapter_invocation(self):
        mcp = MCPAdapter(self.registry)
        result = mcp.invoke("harness_list", {"filter": "unknown"})
        self.assertEqual(result["status"], "SUCCESS")
        self.assertIsNotNone(result["receipt"]["correlation_id"])
        self.assertEqual(result["receipt"]["observed_effect"], "Listed 4 harnesses with filter 'unknown'")

    def test_unsupported_surface(self):
        from .adapters import AdapterBase
        unsupported_adapter = AdapterBase(self.registry, "web")
        result = unsupported_adapter.invoke("harness_list", {})
        self.assertEqual(result["status"], "FAILED")
        self.assertIn("not supported", result["error"])

if __name__ == "__main__":
    unittest.main()
