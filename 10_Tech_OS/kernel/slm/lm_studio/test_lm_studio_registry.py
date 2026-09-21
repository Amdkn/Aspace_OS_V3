import unittest
from unittest.mock import patch, MagicMock
import urllib.error
import json
import time

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lm_studio_registry import LMStudioRegistry

class TestLMStudioRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = LMStudioRegistry()

    @patch('urllib.request.urlopen')
    def test_check_health_healthy(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.read.return_value = b'{"data": []}'
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        health = self.registry.check_health()
        self.assertEqual(health["status"], "healthy")
        self.assertEqual(health["evidence"]["http_status"], 200)

    @patch('urllib.request.urlopen')
    def test_check_health_unhealthy(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.URLError("Connection refused")

        health = self.registry.check_health()
        self.assertEqual(health["status"], "unhealthy")
        self.assertEqual(health["evidence"]["http_status"], 503)

    @patch('urllib.request.urlopen')
    def test_discover(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.read.return_value = b'{"data": [{"id": "model-1"}, {"id": "model-2"}]}'
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        models = self.registry.discover()
        self.assertEqual(len(models), 2)
        self.assertEqual(models[0]["id"], "model-1")
        self.assertEqual(models[1]["id"], "model-2")

    def test_estimate_resources(self):
        # 4096 + (2048/1024) * 256 = 4096 + 512 = 4608
        estimation = self.registry.estimate_resources("model-1", 2048)
        self.assertEqual(estimation["model_id"], "model-1")
        self.assertEqual(estimation["estimated_memory_mb"], 4608.0)
        self.assertTrue(estimation["feasible"])

        # Set policy to make it infeasible
        self.registry.set_policy(max_models=2, max_total_memory_mb=4000, default_ttl_seconds=3600)
        estimation = self.registry.estimate_resources("model-1", 2048)
        self.assertFalse(estimation["feasible"])

    @patch('urllib.request.urlopen')
    def test_load_and_unload(self, mock_urlopen):
        # Mock load response
        mock_load_response = MagicMock()
        mock_load_response.status = 200
        mock_load_response.read.return_value = b'{"success": true}'
        mock_load_response.__enter__.return_value = mock_load_response

        # Mock unload response
        mock_unload_response = MagicMock()
        mock_unload_response.status = 200
        mock_unload_response.read.return_value = b'{"success": true}'
        mock_unload_response.__enter__.return_value = mock_unload_response

        # Use side_effect to return different mocks for load vs unload
        mock_urlopen.side_effect = [mock_load_response, mock_unload_response]

        # Load
        success = self.registry.load("model-1", ttl_seconds=3600)
        self.assertTrue(success)
        self.assertIn("model-1", self.registry._loaded_models)

        # Unload
        success = self.registry.unload("model-1")
        self.assertTrue(success)
        self.assertNotIn("model-1", self.registry._loaded_models)

    @patch('urllib.request.urlopen')
    def test_enforce_ttl_policy(self, mock_urlopen):
        # Mock unload response
        mock_unload_response = MagicMock()
        mock_unload_response.status = 200
        mock_unload_response.read.return_value = b'{"success": true}'
        mock_unload_response.__enter__.return_value = mock_unload_response
        mock_urlopen.return_value = mock_unload_response

        # Manually add expired and unexpired models
        now = time.time()
        self.registry._loaded_models = {
            "model-expired": {"loaded_at": now - 4000, "expires_at": now - 100},
            "model-valid": {"loaded_at": now - 100, "expires_at": now + 3500}
        }

        unloaded = self.registry.enforce_ttl_policy()
        self.assertEqual(len(unloaded), 1)
        self.assertEqual(unloaded[0], "model-expired")
        self.assertNotIn("model-expired", self.registry._loaded_models)
        self.assertIn("model-valid", self.registry._loaded_models)

    @patch('urllib.request.urlopen')
    def test_max_models_policy(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.read.return_value = b'{"success": true}'
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        self.registry.set_policy(max_models=1, max_total_memory_mb=16384, default_ttl_seconds=3600)

        # Load first model should succeed
        success = self.registry.load("model-1")
        self.assertTrue(success)

        # Load second model should fail due to max_models=1
        success = self.registry.load("model-2")
        self.assertFalse(success)

if __name__ == '__main__':
    unittest.main()
