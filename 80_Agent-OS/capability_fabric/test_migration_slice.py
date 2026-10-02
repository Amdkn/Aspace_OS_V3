import unittest
import json
from .contract import CapabilityContract
from .registry import CapabilityRegistry
from .mcp_adapter import MCPAdapter
from .api_adapter import RESTAdapter
from .cli_adapter import CLIAdapter
from .harness_adapter import HarnessAdapter

class TestFirstVerticalSlice(unittest.TestCase):
    def setUp(self):
        self.registry = CapabilityRegistry()

        # 1. Define Business Capability Contract (Issue #333 condition 1)
        self.biz_logic_called = False
        self.last_context = None

        def mock_business_logic(inputs, context):
            self.biz_logic_called = True
            self.last_context = context
            return {"status": "success", "tenant": inputs.get("tenant_id"), "result": f"Processed {inputs.get('action')}"}

        self.cap = CapabilityContract(
            capability_id="coach_os.tenant_provision",
            version="1.0.0",
            domain_owner="Business_OS/Coach_OS",
            intent="Provisions a new tenant environment",
            input_schema={
                "type": "object",
                "properties": {
                    "tenant_id": {"type": "string"},
                    "action": {"type": "string"}
                },
                "required": ["tenant_id", "action"]
            },
            output_schema={"type": "object"},
            authority="business_admin",
            effect_class="COMMAND",
            idempotency=True,
            compensation=None,
            evidence_required=True,
            freshness="sync",
            supported_surfaces=["mcp", "api", "cli", "harness"],
            runtime_bindings=["node_v20"],
            effect_receipt="standard",
            executor=mock_business_logic
        )

        # 2. Register projection (condition 2)
        self.registry.register(self.cap)

        self.mcp = MCPAdapter(self.registry)
        self.api = RESTAdapter(self.registry)
        self.cli = CLIAdapter(self.registry)
        self.harness = HarnessAdapter(self.registry, harness_name="test_runner")

    def test_registry_enumeration(self):
        surfaces = self.registry.enumerate_surfaces()
        self.assertIn("mcp", surfaces)
        self.assertIn("api", surfaces)
        self.assertIn("cli", surfaces)
        self.assertIn("harness", surfaces)
        self.assertIn("coach_os.tenant_provision", surfaces["mcp"])

    def test_mcp_exposure(self):
        tools = self.mcp.list_tools()
        self.assertEqual(len(tools), 1)
        self.assertEqual(tools[0]["name"], "coach_os.tenant_provision")

        result = self.mcp.call_tool("coach_os.tenant_provision", {"tenant_id": "t1", "action": "setup"})
        self.assertTrue(self.biz_logic_called)
        self.assertEqual(self.last_context["surface"], "mcp")
        self.assertIn("effect_receipt", result) # condition 6

    def test_api_exposure(self):
        result = self.api.handle_request("/api/capabilities/coach_os.tenant_provision", "POST", {"tenant_id": "t2", "action": "deploy"})
        self.assertEqual(result["status"], 200)
        self.assertTrue(self.biz_logic_called)
        self.assertEqual(self.last_context["surface"], "api")
        self.assertIn("effect_receipt", result)

    def test_harness_exposure(self):
        result = self.harness.execute_capability("coach_os.tenant_provision", {"tenant_id": "t3", "action": "verify"})
        self.assertTrue(self.biz_logic_called)
        self.assertEqual(self.last_context["surface"], "harness")
        self.assertEqual(self.last_context["harness_name"], "test_runner")
        self.assertIn("effect_receipt", result)

if __name__ == "__main__":
    unittest.main()
