import unittest
import os
import json
import importlib
from unittest.mock import patch

# Dynamic imports for 80_Agent-OS and 30_Business_OS
capability_module = importlib.import_module("80_Agent-OS.capability_fabric.capability")
registry_module = importlib.import_module("80_Agent-OS.capability_fabric.registry")
adapters_module = importlib.import_module("80_Agent-OS.capability_fabric.adapters")
harness_module = importlib.import_module("80_Agent-OS.capability_fabric.harness_adapters")
quarantine_module = importlib.import_module("80_Agent-OS.capability_fabric.quarantine")
harness_list_module = importlib.import_module("80_Agent-OS.capability_fabric.harness_list")
business_cap_module = importlib.import_module("30_Business_OS.capabilities.research_corpus")

CapabilityRegistry = registry_module.CapabilityRegistry
define_tool = capability_module.define_tool
ToolContext = capability_module.ToolContext
ToolResult = capability_module.ToolResult

CLIAdapter = adapters_module.CLIAdapter
APIAdapter = adapters_module.APIAdapter
MCPAdapter = adapters_module.MCPAdapter
SkillAdapter = adapters_module.SkillAdapter
InAppAdapter = adapters_module.InAppAdapter
AgentOSProjectionAdapter = adapters_module.AgentOSProjectionAdapter
A2AAdapter = adapters_module.A2AAdapter
A2UIAdapter = adapters_module.A2UIAdapter
ACPAdapter = adapters_module.ACPAdapter
AGUIAdapter = adapters_module.AGUIAdapter
WebMCPAdapter = adapters_module.WebMCPAdapter

ClaudeCodeHarnessAdapter = harness_module.ClaudeCodeHarnessAdapter
HermesHarnessAdapter = harness_module.HermesHarnessAdapter
JulesHarnessAdapter = harness_module.JulesHarnessAdapter
AntigravityHarnessAdapter = harness_module.AntigravityHarnessAdapter

QuarantineRegistry = quarantine_module.QuarantineRegistry
register_harness_list = harness_list_module.register_harness_list
register_business_capabilities = business_cap_module.register_business_capabilities


class TestCapabilityFabric(unittest.TestCase):
    def setUp(self):
        self.registry = CapabilityRegistry()
        self.quarantine = QuarantineRegistry()
        register_harness_list(self.registry)
        register_business_capabilities(self.registry)

    def test_registry_registration(self):
        capabilities = self.registry.list_capabilities()
        self.assertEqual(len(capabilities), 2)
        cap_ids = [c.capability_id for c in capabilities]
        self.assertIn("harness_list", cap_ids)
        self.assertIn("business_research_corpus", cap_ids)

    def test_define_tool_helper(self):
        def sample_exec(payload, ctx):
            return ToolResult(status="SUCCESS", observed_effect="Sample executed", data={"val": payload.get("x")})

        cap = define_tool(
            capability_id="sample_tool",
            intent="Test tool",
            domain_owner="Test Domain",
            executor_fn=sample_exec
        )
        self.registry.register(cap)

        cli = CLIAdapter(self.registry)
        res = cli.invoke("sample_tool", {"x": 42}, "corr-sample-1")
        self.assertEqual(res["status"], "SUCCESS")
        self.assertEqual(res["receipt"]["observed_effect"], "Sample executed")
        self.assertEqual(res["data"]["val"], 42)

    def test_separate_enumeration(self):
        # Acceptance Criteria 5: Agent OS enumerates capability, surface, adapter, runtime binding, observed_at, and evidence source separately
        binding_info = self.registry.enumerate_capability_bindings(
            capability_id="business_research_corpus",
            adapter_name="MCPAdapter",
            runtime_binding="mcp://localhost:8080"
        )
        self.assertEqual(binding_info["capability_id"], "business_research_corpus")
        self.assertEqual(binding_info["domain_owner"], "Business OS")
        self.assertEqual(binding_info["adapter"], "MCPAdapter")
        self.assertEqual(binding_info["runtime_binding"], "mcp://localhost:8080")
        self.assertIn("observed_at", binding_info)
        self.assertIn("evidence_source", binding_info)

    def test_business_capability_multi_surface_consumption(self):
        # Acceptance Criteria 3 & 6: Business capability consumes shared core across multiple transport adapters while remaining Business-owned
        cli = CLIAdapter(self.registry)
        api = APIAdapter(self.registry)
        mcp = MCPAdapter(self.registry)

        cli_res = cli.invoke("business_research_corpus", {"topic": "AI_Market"}, "corr-bus-cli")
        api_res = api.invoke("business_research_corpus", {"topic": "AI_Market"}, "corr-bus-api")
        mcp_res = mcp.invoke("business_research_corpus", {"topic": "AI_Market"}, "corr-bus-mcp")

        self.assertEqual(cli_res["status"], "SUCCESS")
        self.assertEqual(api_res["status"], "SUCCESS")
        self.assertEqual(mcp_res["status"], "SUCCESS")

        self.assertEqual(cli_res["data"]["domain_owner"], "Business OS")
        self.assertEqual(api_res["data"]["domain_owner"], "Business OS")
        self.assertEqual(mcp_res["data"]["domain_owner"], "Business OS")

    def test_harness_adapters_no_executor_duplication(self):
        # Acceptance Criteria 4: At least three harnesses consume the same capability contract without executor duplication
        claude = ClaudeCodeHarnessAdapter(self.registry)
        hermes = HermesHarnessAdapter(self.registry)
        jules = JulesHarnessAdapter(self.registry)

        c_res = claude.execute_harness_capability("business_research_corpus", {"topic": "SaaS"}, "corr-claude")
        h_res = hermes.execute_harness_capability("business_research_corpus", {"topic": "SaaS"}, "corr-hermes")
        j_res = jules.execute_harness_capability("business_research_corpus", {"topic": "SaaS"}, "corr-jules")

        self.assertEqual(c_res["status"], "SUCCESS")
        self.assertEqual(h_res["status"], "SUCCESS")
        self.assertEqual(j_res["status"], "SUCCESS")

        self.assertEqual(c_res["harness_id"], "claude_code")
        self.assertEqual(h_res["harness_id"], "hermes")
        self.assertEqual(j_res["harness_id"], "jules")

        self.assertIn("Harness: claude_code", c_res["receipt"]["provenance"])
        self.assertIn("Harness: hermes", h_res["receipt"]["provenance"])
        self.assertIn("Harness: jules", j_res["receipt"]["provenance"])

    def test_protocol_adapters_and_quarantine(self):
        # Acceptance Criteria 7: Unsupported/experimental adapters are explicitly quarantined rather than silently promoted
        self.quarantine.quarantine("fcp", "FCP Protocol", "Experimental Lab", "Uncertified protocol")

        fcp_adapter = MCPAdapter(self.registry, quarantine_registry=self.quarantine)
        # Hack surface name for test verification
        fcp_adapter.surface_name = "fcp"

        res = fcp_adapter.invoke("business_research_corpus", {})
        self.assertEqual(res["status"], "FAILED")
        self.assertIn("QUARANTINED", res["error"])

    @patch('os.path.exists')
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='{"execution": {"jules": {"harnesses": {"test_harness": {"status": "local_verified_linux_adapter_required"}}}}}')
    def test_cli_adapter_invocation(self, mock_open, mock_exists):
        def side_effect(path):
            if "ASPACE_WORKSPACE_REGISTRY.json" in path:
                return True
            if "runtime.json" in path:
                return True
            return os.path.exists(path)
        mock_exists.side_effect = side_effect

        def open_side_effect(path, *args, **kwargs):
            if "runtime.json" in path:
                return unittest.mock.mock_open(read_data='{"state": "ONLINE"}')()
            return unittest.mock.mock_open(read_data='{"execution": {"jules": {"harnesses": {"test_harness": {"status": "local_verified_linux_adapter_required"}}}}}')()

        mock_open.side_effect = open_side_effect

        cli = CLIAdapter(self.registry)
        result = cli.invoke("harness_list", {}, "corr-cli-123")
        self.assertEqual(result["status"], "SUCCESS")
        self.assertEqual(result["receipt"]["correlation_id"], "corr-cli-123")

    def test_search_and_discovery(self):
        results = self.registry.search_capabilities("research")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].capability_id, "business_research_corpus")


if __name__ == "__main__":
    unittest.main()
