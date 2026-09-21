import unittest
from unittest.mock import patch, MagicMock
import time
import json
import urllib.error

# Append to sys.path to run standalone if needed
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from lm_studio_registry import LMStudioRegistry, ModelResourcePolicy

class TestLMStudioRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = LMStudioRegistry(api_base_url="http://mock-lm-studio:1234/v1")

    @patch('urllib.request.urlopen')
    def test_discover_models_success(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({
            "data": [
                {"id": "qwen2.5-coder"},
                {"id": "llama3.1"}
            ]
        }).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response

        models = self.registry.discover_models()
        self.assertEqual(len(models), 2)
        self.assertEqual(models[0]["id"], "qwen2.5-coder")

    @patch('urllib.request.urlopen')
    def test_discover_models_error(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.URLError("Connection refused")
        models = self.registry.discover_models()
        self.assertEqual(models, [])

    def test_estimate_resources(self):
        est = self.registry.estimate_resources("my-model", 8192)
        self.assertEqual(est["model_id"], "my-model")
        self.assertTrue(est["estimated_ram_mb"] > 2048)

    @patch('urllib.request.urlopen')
    def test_load_and_unload(self, mock_urlopen):
        # Mock successful load response
        mock_load_response = MagicMock()
        mock_load_response.getcode.return_value = 200

        # Mock successful unload response
        mock_unload_response = MagicMock()
        mock_unload_response.getcode.return_value = 200

        # We need side_effect to return different mocks for subsequent calls
        mock_urlopen.side_effect = [
            MagicMock(__enter__=MagicMock(return_value=mock_load_response)),
            MagicMock(__enter__=MagicMock(return_value=mock_unload_response))
        ]

        # Default policy
        success = self.registry.load_model("test-model", ttl_seconds=60)
        self.assertTrue(success)
        self.assertIn("test-model", self.registry.loaded_models)

        # Unload
        success_unload = self.registry.unload_model("test-model")
        self.assertTrue(success_unload)
        self.assertNotIn("test-model", self.registry.loaded_models)

    @patch('urllib.request.urlopen')
    def test_load_api_failure(self, mock_urlopen):
        # Mock failed load response (e.g., 500)
        mock_load_response = MagicMock()
        mock_load_response.getcode.return_value = 500
        mock_urlopen.return_value.__enter__.return_value = mock_load_response

        success = self.registry.load_model("test-model-fail", ttl_seconds=60)
        self.assertFalse(success)
        self.assertNotIn("test-model-fail", self.registry.loaded_models)

    def test_load_reject_resource_limit(self):
        # Strict policy
        strict_policy = ModelResourcePolicy(max_ram_mb=1024) # Very low RAM
        # Should not hit network, so no patch needed
        success = self.registry.load_model("test-model-heavy", policy=strict_policy)
        self.assertFalse(success, "Should reject due to memory limits")

    @patch('urllib.request.urlopen')
    def test_ttl_enforcement(self, mock_urlopen):
        # Mock successful load
        mock_load_response = MagicMock()
        mock_load_response.getcode.return_value = 200

        # Mock successful unload
        mock_unload_response = MagicMock()
        mock_unload_response.getcode.return_value = 200

        mock_urlopen.side_effect = [
            MagicMock(__enter__=MagicMock(return_value=mock_load_response)),
            MagicMock(__enter__=MagicMock(return_value=mock_unload_response))
        ]

        self.registry.load_model("test-ttl", ttl_seconds=1)
        self.assertIn("test-ttl", self.registry.loaded_models)

        # Manually alter the time to simulate expiry
        self.registry.loaded_models["test-ttl"].ttl_policy.last_accessed -= 2

        expired = self.registry.enforce_ttl_policy()
        self.assertIn("test-ttl", expired)
        self.assertNotIn("test-ttl", self.registry.loaded_models)

    @patch('urllib.request.urlopen')
    def test_touch_model(self, mock_urlopen):
        mock_load_response = MagicMock()
        mock_load_response.getcode.return_value = 200
        mock_urlopen.return_value.__enter__.return_value = mock_load_response

        self.registry.load_model("test-touch", ttl_seconds=60)
        original_time = self.registry.loaded_models["test-touch"].ttl_policy.last_accessed

        time.sleep(0.01) # Small delay to ensure timestamp differs
        self.registry.touch_model("test-touch")

        new_time = self.registry.loaded_models["test-touch"].ttl_policy.last_accessed
        self.assertTrue(new_time > original_time)

    @patch('urllib.request.urlopen')
    def test_health_evidence(self, mock_urlopen):
        mock_load_response = MagicMock()
        mock_load_response.getcode.return_value = 200
        mock_urlopen.return_value.__enter__.return_value = mock_load_response

        self.registry.load_model("health-model-1", ttl_seconds=3600)
        evidence = self.registry.get_health_evidence()

        self.assertEqual(evidence["status"], "ok")
        self.assertEqual(evidence["loaded_models_count"], 1)
        self.assertEqual(evidence["loaded_models"][0]["id"], "health-model-1")

if __name__ == '__main__':
    unittest.main()
