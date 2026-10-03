"""Test Suite for Browser Harness Bridge and SurfaceDriver Contract.

Validates contract compliance, G2 surface adapters (ChatGPT Web + Qwen Coder),
multi-harness/holon bridge capability invocation, secret fencing, and evidence readback.
"""

import unittest
import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from capability_fabric.registry import CapabilityRegistry
from capability_fabric.adapters import CLIAdapter, APIAdapter
from browser_bridge.adapters import ChatGPTWebAdapter, QwenCoderWebAdapter
from browser_bridge.surface_matrix import list_registered_surfaces, get_surface_spec
from browser_bridge.bridge_capability import register_browser_bridge_capabilities


class TestBrowserHarnessBridge(unittest.TestCase):
    def setUp(self):
        self.gpt_adapter = ChatGPTWebAdapter()
        self.qwen_adapter = QwenCoderWebAdapter()
        self.registry = CapabilityRegistry()
        register_browser_bridge_capabilities(self.registry)

    def test_fork_manifest_exists_and_valid(self):
        manifest_path = os.path.join(os.path.dirname(__file__), "fork_manifest.json")
        self.assertTrue(os.path.exists(manifest_path))
        with open(manifest_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(data["upstream"]["repository"], "miuuyy/codex-chatgpt-web")
        self.assertEqual(data["sovereign_fork"]["repository"], "Amdkn/codex-chatgpt-web")
        self.assertIn("invariants", data)

    def test_surface_matrix_registered_surfaces(self):
        surfaces = list_registered_surfaces()
        self.assertIn("chatgpt_web", surfaces)
        self.assertIn("qwen_coder_web", surfaces)
        self.assertIn("deepseek_web", surfaces)
        self.assertIn("gemini_spark_web", surfaces)
        spec = get_surface_spec("chatgpt_web")
        self.assertEqual(spec["provider"], "OpenAI")

    def test_chatgpt_adapter_lifecycle(self):
        session = self.gpt_adapter.bootstrap_session(
            harness_id="hermes",
            holon_id="ryan",
            auth_credentials={"type": "session_cookie", "secret_token": "SENSITIVE_KEY_DO_NOT_LEAK"},
        )
        self.assertTrue(session.is_authenticated)
        # Verify secrets are isolated and not stored in metadata
        self.assertNotIn("SENSITIVE_KEY_DO_NOT_LEAK", json.dumps(session.metadata))
        self.assertTrue(session.metadata["auth_present"])

        interaction_id = self.gpt_adapter.inject_prompt(session, "Hello ChatGPT")
        chunks = self.gpt_adapter.capture_stream(session, interaction_id)
        self.assertTrue(len(chunks) > 0)
        self.assertTrue(chunks[-1].is_final)

        exec_res = self.gpt_adapter.invoke_capability(
            session=session,
            capability_id="code_interpreter",
            payload={"prompt": "print('test')"},
            correlation_id="corr-gpt-123",
        )
        self.assertEqual(exec_res.status, "SUCCESS")
        self.assertTrue(exec_res.evidence.verified)
        self.assertIn("div.chatgpt-response-complete", exec_res.evidence.readback_observed)

    def test_qwen_coder_adapter_lifecycle(self):
        session = self.qwen_adapter.bootstrap_session(
            harness_id="codex",
            holon_id="clara",
            auth_credentials={"type": "bearer_token", "secret_token": "QWEN_SECRET_KEY"},
        )
        self.assertTrue(session.is_authenticated)
        self.assertNotIn("QWEN_SECRET_KEY", json.dumps(session.metadata))

        exec_res = self.qwen_adapter.invoke_capability(
            session=session,
            capability_id="code_synthesis",
            payload={"prompt": "def fib(n): return n"},
            correlation_id="corr-qwen-456",
        )
        self.assertEqual(exec_res.status, "SUCCESS")
        self.assertTrue(exec_res.evidence.verified)
        self.assertIn("div.qwen-response-complete", exec_res.evidence.readback_observed)

    def test_bridge_capability_multi_harness_invocation(self):
        cli = CLIAdapter(self.registry)

        # Invocation 1: Ryan on Hermes harness calling ChatGPT Web surface
        res1 = cli.invoke(
            "browser_prompt",
            {
                "surface_id": "chatgpt_web",
                "prompt": "Synthesize status",
                "harness_id": "hermes",
                "holon_id": "ryan",
            },
            "corr-multi-1",
        )
        self.assertEqual(res1["status"], "SUCCESS")
        self.assertEqual(res1["data"]["harness_id"], "hermes")
        self.assertEqual(res1["data"]["holon_id"], "ryan")
        self.assertTrue(res1["data"]["verified"])

        # Invocation 2: Clara on Codex harness calling Qwen Coder Web surface using same bridge
        res2 = cli.invoke(
            "browser_capability_exec",
            {
                "surface_id": "qwen_coder_web",
                "capability_id": "code_synthesis",
                "payload": {"prompt": "Write module"},
                "harness_id": "codex",
                "holon_id": "clara",
            },
            "corr-multi-2",
        )
        self.assertEqual(res2["status"], "SUCCESS")
        self.assertEqual(res2["data"]["harness_id"], "codex")
        self.assertEqual(res2["data"]["holon_id"], "clara")
        self.assertTrue(res2["data"]["verified"])


if __name__ == "__main__":
    unittest.main()
