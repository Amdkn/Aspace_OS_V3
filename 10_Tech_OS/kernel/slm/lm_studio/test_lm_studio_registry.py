import unittest
from unittest.mock import patch, MagicMock
import json
import time

# Update the import path to match the module layout if necessary,
# assuming it's available in the PYTHONPATH or relative path.
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lm_studio_registry import LMStudioRegistry

class TestLMStudioRegistry(unittest.TestCase):

    def setUp(self):
        self.registry = LMStudioRegistry()

    @patch('urllib.request.urlopen')
    def test_discover_models_success(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({
            "data": [
                {"id": "model-1"},
                {"id": "model-2"}
            ]
        }).encode('utf-8')
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        models = self.registry.discover_models()
        self.assertEqual(len(models), 2)
        self.assertEqual(models[0]['id'], 'model-1')

    @patch('urllib.request.urlopen')
    def test_discover_models_failure(self, mock_urlopen):
        import urllib.error
        mock_urlopen.side_effect = urllib.error.URLError("Connection refused")

        models = self.registry.discover_models()
        self.assertEqual(models, [])

    def test_estimate_resources(self):
        estimation = self.registry.estimate_resources("any-model")
        self.assertIn('estimated_vram_gb', estimation)
        self.assertIn('fits_in_vram', estimation)
        self.assertTrue(estimation['fits_in_vram'])

    @patch('urllib.request.urlopen')
    def test_load_model_success(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({"status": "success"}).encode('utf-8')
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        res = self.registry.load_model("test-model", context_length=1024, ttl_seconds=60)
        self.assertEqual(res['status'], 'loaded')
        self.assertEqual(res['context_length'], 1024)
        self.assertIn("test-model", self.registry.loaded_models)

    def test_load_model_exceeds_vram(self):
        self.registry.max_vram_gb = 2.0 # Set low to force failure
        with self.assertRaises(ValueError):
            self.registry.load_model("huge-model")

    @patch('urllib.request.urlopen')
    def test_unload_model(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({"status": "success"}).encode('utf-8')
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        self.registry.loaded_models["model-to-unload"] = {"status": "loaded"}
        success = self.registry.unload_model("model-to-unload")
        self.assertTrue(success)
        self.assertNotIn("model-to-unload", self.registry.loaded_models)

    @patch.object(LMStudioRegistry, 'unload_model')
    def test_check_ttl_policy(self, mock_unload):
        now = time.time()
        self.registry.loaded_models = {
            "expired-model": {"loaded_at": now - 3600, "ttl_seconds": 1800, "status": "loaded"},
            "active-model": {"loaded_at": now, "ttl_seconds": 3600, "status": "loaded"}
        }

        self.registry.check_ttl_policy()
        mock_unload.assert_called_once_with("expired-model")

    @patch('urllib.request.urlopen')
    def test_health_healthy(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({"data": [{"id": "m1"}]}).encode('utf-8')
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        health = self.registry.health()
        self.assertEqual(health['status'], 'healthy')
        self.assertEqual(health['available_models_count'], 1)

    @patch('urllib.request.urlopen')
    def test_health_unhealthy(self, mock_urlopen):
        import urllib.error
        mock_urlopen.side_effect = urllib.error.URLError("Down")

        health = self.registry.health()
        self.assertEqual(health['status'], 'unhealthy')
        self.assertEqual(health['backend'], 'lm_studio')

if __name__ == '__main__':
    unittest.main()
