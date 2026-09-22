import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime, timezone, timedelta
import json
import urllib.error
import urllib.request
# Fix the import path to be safe whether tested from kernel root or module root
import sys
import os
try:
    from slm.lm_studio.lm_studio_registry import LMStudioRegistry
except ImportError:
    from lm_studio_registry import LMStudioRegistry

class TestLMStudioRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = LMStudioRegistry()

    @patch('urllib.request.urlopen')
    def test_discover_models_success(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_data = {
            "data": [
                {"id": "meta-llama-3-8b-instruct-q4_k_m", "object": "model"},
                {"id": "model-2", "object": "model"}
            ]
        }
        mock_response.read.return_value = json.dumps(mock_data).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response

        models = self.registry.discover_models()
        self.assertEqual(len(models), 2)
        self.assertEqual(models[0]["id"], "meta-llama-3-8b-instruct-q4_k_m")

    @patch('urllib.request.urlopen')
    def test_discover_models_failure(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.URLError("Connection refused")
        models = self.registry.discover_models()
        self.assertEqual(models, [])

    @patch('urllib.request.urlopen')
    def test_check_health_healthy(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_urlopen.return_value.__enter__.return_value = mock_response

        health = self.registry.check_health()
        self.assertEqual(health["status"], "healthy")
        self.assertEqual(health["code"], 200)

    @patch('urllib.request.urlopen')
    def test_check_health_unreachable(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.URLError("Connection refused")
        health = self.registry.check_health()
        self.assertEqual(health["status"], "unreachable")
        self.assertIn("Connection refused", health["error"])

    @patch('urllib.request.urlopen')
    def test_estimate_resources_found(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_data = {
            "data": [
                {"id": "meta-llama-3-8.5b-instruct-q4"}
            ]
        }
        mock_response.read.return_value = json.dumps(mock_data).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response

        estimation = self.registry.estimate_resources("meta-llama-3-8.5b-instruct-q4")
        self.assertIn("estimated_vram_gb", estimation)
        self.assertTrue(estimation["supported"])
        self.assertTrue(estimation["found_in_registry"])
        self.assertGreater(estimation["estimated_vram_gb"], 4.0)

    @patch('urllib.request.urlopen')
    def test_estimate_resources_moe(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.URLError("Connection refused")

        estimation = self.registry.estimate_resources("mixtral-8x7b-instruct-v0.1-q4_k_m")
        self.assertTrue(estimation["supported"])
        self.assertFalse(estimation["found_in_registry"])
        # 8 * 7 = 56, * 0.5 = 28B active params. 28B * 4 bits = 112Gb = 14GB + 1.5 context = 15.5 VRAM roughly.
        self.assertGreater(estimation["estimated_vram_gb"], 14.0)

    @patch('urllib.request.urlopen')
    def test_load_and_unload_model(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_urlopen.return_value.__enter__.return_value = mock_response

        self.registry.load_model("test-model", ttl_seconds=3600)
        self.assertIn("test-model", self.registry.loaded_models)
        self.registry.unload_model("test-model")
        self.assertNotIn("test-model", self.registry.loaded_models)

        mock_urlopen.assert_called()

    @patch('urllib.request.urlopen')
    def test_enforce_ttl_policy(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_urlopen.return_value.__enter__.return_value = mock_response

        self.registry.load_model("model-1", ttl_seconds=10)
        self.registry.load_model("model-2", ttl_seconds=3600)

        past_time = datetime.now(timezone.utc) - timedelta(seconds=20)
        self.registry.loaded_models["model-1"]["last_accessed"] = past_time

        expired = self.registry.enforce_ttl_policy()
        self.assertIn("model-1", expired)
        self.assertNotIn("model-2", expired)
        self.assertNotIn("model-1", self.registry.loaded_models)
        self.assertIn("model-2", self.registry.loaded_models)

if __name__ == '__main__':
    unittest.main()
