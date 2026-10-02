import unittest
import os
import json
from unittest.mock import patch
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

    @patch('os.path.exists')
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='{"execution": {"jules": {"harnesses": {"test_harness": {"status": "local_verified_linux_adapter_required"}}}}}')
    def test_cli_adapter_invocation(self, mock_open, mock_exists):
        # We need to ensure os.path.exists returns True for registry, True for runtime
        def side_effect(path):
            if "ASPACE_WORKSPACE_REGISTRY.json" in path:
                return True
            if "runtime.json" in path:
                return True
            return os.path.exists(path)
        mock_exists.side_effect = side_effect

        # Mock multiple open calls
        def open_side_effect(path, *args, **kwargs):
            if "runtime.json" in path:
                return unittest.mock.mock_open(read_data='{"state": "ONLINE"}')()
            return unittest.mock.mock_open(read_data='{"execution": {"jules": {"harnesses": {"test_harness": {"status": "local_verified_linux_adapter_required"}}}}}')()

        mock_open.side_effect = open_side_effect

        cli = CLIAdapter(self.registry)
        result = cli.invoke("harness_list", {}, "corr-cli-123")
        self.assertEqual(result["status"], "SUCCESS")
        self.assertEqual(result["receipt"]["correlation_id"], "corr-cli-123")
        self.assertEqual(result["receipt"]["observed_effect"], "Listed 1 harnesses")
        self.assertIn("data", result)
        self.assertEqual(len(result["data"]["harnesses"]), 1)
        self.assertEqual(result["data"]["harnesses"][0]["id"], "test_harness")
        self.assertEqual(result["data"]["harnesses"][0]["status"], "active")

    @patch('os.path.exists')
    def test_api_adapter_invocation(self, mock_exists):
        def side_effect(path):
            if "ASPACE_WORKSPACE_REGISTRY.json" in path:
                return True
            if "runtime.json" in path:
                return False
            return os.path.exists(path)
        mock_exists.side_effect = side_effect

        def open_side_effect(path, *args, **kwargs):
            return unittest.mock.mock_open(read_data='{"execution": {"jules": {"harnesses": {"test_harness": {"status": "local_verified_linux_adapter_required"}}}}}')()

        with patch('builtins.open', side_effect=open_side_effect):
            api = APIAdapter(self.registry)
            result = api.invoke("harness_list", {"capability": "shell"}, "corr-api-123")
            self.assertEqual(result["status"], "SUCCESS")
            self.assertEqual(result["receipt"]["correlation_id"], "corr-api-123")
            self.assertEqual(result["receipt"]["observed_effect"], "Listed 1 harnesses with filter capability 'shell'")
            self.assertEqual(len(result["data"]["harnesses"]), 1)

    @patch('os.path.exists')
    def test_mcp_adapter_invocation(self, mock_exists):
        def side_effect(path):
            if "ASPACE_WORKSPACE_REGISTRY.json" in path:
                return True
            if "runtime.json" in path:
                return False
            return os.path.exists(path)
        mock_exists.side_effect = side_effect

        def open_side_effect(path, *args, **kwargs):
            return unittest.mock.mock_open(read_data='{"execution": {"jules": {"harnesses": {"test_harness": {"status": "local_verified_linux_adapter_required"}}}}}')()

        with patch('builtins.open', side_effect=open_side_effect):
            mcp = MCPAdapter(self.registry)
            result = mcp.invoke("harness_list", {}, "corr-mcp-123")
            self.assertEqual(result["status"], "SUCCESS")
            self.assertEqual(result["receipt"]["correlation_id"], "corr-mcp-123")
            self.assertEqual(result["receipt"]["observed_effect"], "Listed 1 harnesses")
            self.assertEqual(len(result["data"]["harnesses"]), 1)

    def test_unsupported_surface(self):
        from .adapters import AdapterBase
        unsupported_adapter = AdapterBase(self.registry, "web")
        result = unsupported_adapter.invoke("harness_list", {})
        self.assertEqual(result["status"], "FAILED")
        self.assertIn("not supported", result["error"])

    @patch('os.path.exists')
    def test_negative_stale_declarative_harness(self, mock_exists):
        # Negative test: stale/declarative harness must not appear as live merely because it exists in a registry
        def side_effect(path):
            if "ASPACE_WORKSPACE_REGISTRY.json" in path:
                return True
            if "runtime.json" in path:
                return False  # Runtime offline
            return os.path.exists(path)
        mock_exists.side_effect = side_effect

        mock_registry = {
            "execution": {
                "jules": {
                    "harnesses": {
                        "stale_harness": {
                            "status": "local_verified_linux_adapter_required"
                        }
                    }
                }
            }
        }

        def open_side_effect(path, *args, **kwargs):
            return unittest.mock.mock_open(read_data=json.dumps(mock_registry))()

        with patch('builtins.open', side_effect=open_side_effect):
            from .harness_list import harness_list_executor
            receipt = harness_list_executor({}, "corr-1")

            self.assertEqual(receipt.status, "SUCCESS")
            harnesses = receipt.data["harnesses"]
            self.assertEqual(len(harnesses), 1)
            # Since runtime is offline, the status should remain its declared status, not "active"
            self.assertEqual(harnesses[0]["status"], "local_verified_linux_adapter_required")

if __name__ == "__main__":
    unittest.main()
