import unittest
from unittest.mock import patch, MagicMock
import json
import time

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lm_studio_registry import LMStudioRegistry

class TestLMStudioRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = LMStudioRegistry()

    @patch('urllib.request.urlopen')
    def test_discovery(self, mock_urlopen):
        # Mock successful response
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({"data": [{"id": "model-1"}]}).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response

        res = self.registry.discovery()
        self.assertEqual(res, {"data": [{"id": "model-1"}]})

    @patch('urllib.request.urlopen')
    def test_load(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({"status": "loaded"}).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response

        res = self.registry.load("test-model", context_length=1024, ttl=60)
        self.assertEqual(res, {"status": "loaded"})
        self.assertIn("test-model", self.registry._loaded_models)
        self.assertEqual(self.registry._loaded_models["test-model"]["context_length"], 1024)
        self.assertEqual(self.registry._loaded_models["test-model"]["ttl"], 60)

    @patch('urllib.request.urlopen')
    def test_unload(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({"status": "unloaded"}).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response

        # Pretend model is loaded
        self.registry._loaded_models["test-model"] = {"loaded_at": time.time(), "ttl": 3600, "context_length": 2048}

        res = self.registry.unload("test-model")
        self.assertEqual(res, {"status": "unloaded"})
        self.assertNotIn("test-model", self.registry._loaded_models)

    @patch('urllib.request.urlopen')
    def test_health_healthy(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({"data": []}).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response

        res = self.registry.health()
        self.assertEqual(res["status"], "healthy")

    @patch('urllib.request.urlopen')
    def test_health_unhealthy(self, mock_urlopen):
        import urllib.error
        mock_urlopen.side_effect = urllib.error.URLError("Connection refused")

        res = self.registry.health()
        self.assertEqual(res["status"], "unhealthy")
        self.assertIn("Connection refused", res["evidence"])

    @patch('urllib.request.urlopen')
    def test_enforce_ttl_policy(self, mock_urlopen):
        # Mock unload response
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({"status": "unloaded"}).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response

        current_time = time.time()
        # Model 1 expired
        self.registry._loaded_models["model-1"] = {"loaded_at": current_time - 100, "ttl": 50, "context_length": 2048}
        # Model 2 active
        self.registry._loaded_models["model-2"] = {"loaded_at": current_time, "ttl": 3600, "context_length": 2048}

        unloaded = self.registry.enforce_ttl_policy()
        self.assertIn("model-1", unloaded)
        self.assertNotIn("model-2", unloaded)
        self.assertNotIn("model-1", self.registry._loaded_models)
        self.assertIn("model-2", self.registry._loaded_models)

if __name__ == '__main__':
    unittest.main()
