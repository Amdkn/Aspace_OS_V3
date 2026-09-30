import json
import os
import tempfile
import unittest
from unittest.mock import MagicMock, patch

from machine_fabric.gateway.plugin_sdk import GatewayPlugin, MockPluginContext, PluginContext
from machine_fabric.gateway.plugin_discovery import discover_plugins


class DummyPlugin(GatewayPlugin):
    def manifest(self):
        return {"capability_id": "machine.test.dummy", "version": "1.0"}

    def health(self):
        return {"aggregate": "ONLINE"}

    def execute(self, context):
        return {"state": "SUCCEEDED", "evidence": {"result": "success"}}

    def cleanup(self, context):
        if isinstance(context, MockPluginContext):
            context.record_log("cleanup_called")


class TestPluginSDK(unittest.TestCase):

    def test_context_creation(self):
        ctx = PluginContext("op-123", "test_action", {"action": "test"})
        self.assertEqual(ctx.operation_id, "op-123")
        self.assertEqual(ctx.action, "test_action")
        self.assertEqual(ctx.payload, {"action": "test"})

    def test_mock_context_logging(self):
        ctx = MockPluginContext("op-999")
        ctx.record_log("step1")
        self.assertIn("step1", ctx.log)

    def test_plugin_lifecycle(self):
        plugin = DummyPlugin()
        ctx = MockPluginContext("op-xyz", {})

        # Test default inspect
        self.assertTrue(plugin.inspect(ctx.payload))

        # Execute
        plugin.prepare(ctx)
        receipt = plugin.execute(ctx)
        plugin.observe(ctx, receipt)
        final_receipt = plugin.reconcile(ctx, receipt)
        plugin.cleanup(ctx)

        self.assertEqual(final_receipt["state"], "SUCCEEDED")
        self.assertIn("cleanup_called", ctx.log)

    def test_plugin_discovery_valid(self):
        # We test discovery using a temporary directory
        with tempfile.TemporaryDirectory() as tmpdir:
            plugin_code = """
from machine_fabric.gateway.plugin_sdk import GatewayPlugin
class TempPlugin(GatewayPlugin):
    def manifest(self): return {"capability_id": "machine.temp"}
    def health(self): return {"aggregate": "ONLINE"}
    def execute(self, ctx): return {}
"""
            with open(os.path.join(tmpdir, "temp_plugin.py"), "w") as f:
                f.write(plugin_code)

            # Need to modify python path for this test because TempPlugin tries to import GatewayPlugin absolute to PYTHONPATH
            # Which is handled by `PYTHONPATH=$(pwd)/10_Tech_OS python3 -m unittest` properly.
            plugins = discover_plugins(tmpdir)
            self.assertIn("machine.temp", plugins)

    def test_plugin_discovery_disabled(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            with open(os.path.join(tmpdir, "disabled_plugin.py.disabled"), "w") as f:
                f.write("invalid code")

            plugins = discover_plugins(tmpdir)
            self.assertEqual(len(plugins), 0)

    def test_plugin_discovery_isolation(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            with open(os.path.join(tmpdir, "bad_plugin.py"), "w") as f:
                f.write("syntax error here")

            with open(os.path.join(tmpdir, "good_plugin.py"), "w") as f:
                f.write("""
from machine_fabric.gateway.plugin_sdk import GatewayPlugin
class GoodPlugin(GatewayPlugin):
    def manifest(self): return {"capability_id": "machine.good"}
    def health(self): return {}
    def execute(self, ctx): return {}
""")
            # Discovery should catch syntax error and continue
            plugins = discover_plugins(tmpdir)
            self.assertIn("machine.good", plugins)
            self.assertEqual(len(plugins), 1)

if __name__ == '__main__':
    unittest.main()
