#!/usr/bin/env python3
"""
test_lm_studio_registry.py — Tests unitaires pour LMStudioRegistry avec mocks d'appels HTTP.
"""

import unittest
from unittest.mock import patch, MagicMock
import json
import time

from slm.lm_studio.lm_studio_registry import LMStudioRegistry

class TestLMStudioRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = LMStudioRegistry(base_url="http://fake-url:1234")

    @patch("urllib.request.urlopen")
    def test_health_check_success(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({"data": []}).encode("utf-8")
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        self.assertTrue(self.registry.health_check())

    @patch("urllib.request.urlopen")
    def test_health_check_failure(self, mock_urlopen):
        import urllib.error
        mock_urlopen.side_effect = urllib.error.URLError("Connection refused")

        self.assertFalse(self.registry.health_check())

    @patch("urllib.request.urlopen")
    def test_discover_models(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({
            "data": [{"id": "model-a"}, {"id": "model-b"}]
        }).encode("utf-8")
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        models = self.registry.discover_models()
        self.assertEqual(len(models), 2)
        self.assertEqual(models[0]["id"], "model-a")
        self.assertEqual(models[1]["id"], "model-b")

    def test_estimate_resources(self):
        # 7b estimation
        res_7b = self.registry.estimate_resources("mistral-7b-v0.1.Q4_K_M")
        self.assertEqual(res_7b["estimated_ram_mb"], 6000)
        self.assertTrue(res_7b["can_fit"])

        # 13b estimation
        res_13b = self.registry.estimate_resources("llama-2-13b-chat.Q5_K_M")
        self.assertEqual(res_13b["estimated_ram_mb"], 10000)

        # 70b estimation
        res_70b = self.registry.estimate_resources("llama-2-70b-chat.Q4_0")
        self.assertEqual(res_70b["estimated_ram_mb"], 40000)

        # default fallback
        res_other = self.registry.estimate_resources("unknown-model")
        self.assertEqual(res_other["estimated_ram_mb"], 4096)

    @patch("urllib.request.urlopen")
    def test_load_and_unload_model(self, mock_urlopen):
        # Mock successful responses
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({}).encode("utf-8")
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        model_id = "test-model-7b"

        # Load
        success = self.registry.load_model(model_id, context_length=4096, ttl_seconds=120)
        self.assertTrue(success)
        self.assertIn(model_id, self.registry.loaded_models)
        self.assertEqual(self.registry.loaded_models[model_id]["ttl"], 120)
        self.assertEqual(self.registry.loaded_models[model_id]["context_length"], 4096)

        # Unload
        success_unload = self.registry.unload_model(model_id)
        self.assertTrue(success_unload)
        self.assertNotIn(model_id, self.registry.loaded_models)

    @patch("urllib.request.urlopen")
    def test_enforce_ttl_policy(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({}).encode("utf-8")
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        # Add models directly to avoid sleeping
        now = time.time()

        # Model 1: loaded 2 hours ago, ttl 1 hour (expired)
        self.registry.loaded_models["model-expired"] = {
            "loaded_at": now - 7200,
            "ttl": 3600,
            "context_length": 2048
        }

        # Model 2: loaded 10 mins ago, ttl 1 hour (active)
        self.registry.loaded_models["model-active"] = {
            "loaded_at": now - 600,
            "ttl": 3600,
            "context_length": 2048
        }

        unloaded = self.registry.enforce_ttl_policy()

        self.assertEqual(len(unloaded), 1)
        self.assertEqual(unloaded[0], "model-expired")
        self.assertNotIn("model-expired", self.registry.loaded_models)
        self.assertIn("model-active", self.registry.loaded_models)


if __name__ == "__main__":
    unittest.main()
