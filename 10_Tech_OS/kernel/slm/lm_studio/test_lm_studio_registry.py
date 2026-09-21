import unittest
from unittest.mock import patch, MagicMock
import json
import time

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lm_studio_registry import LMStudioRegistry

class TestLMStudioRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = LMStudioRegistry(base_url="http://localhost:1234")

    @patch('urllib.request.urlopen')
    def test_health_ok(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": [{"id": "model1"}, {"id": "model2"}]}).encode("utf-8")
        mock_urlopen.return_value.__enter__.return_value = mock_response

        health = self.registry.health()
        self.assertEqual(health["status"], "ok")
        self.assertEqual(health["evidence"], "API responding")
        self.assertEqual(health["models_count"], 2)

    @patch('urllib.request.urlopen')
    def test_health_error_http(self, mock_urlopen):
        import urllib.error
        mock_urlopen.side_effect = urllib.error.HTTPError(url="", code=500, msg="Internal Server Error", hdrs={}, fp=None)

        health = self.registry.health()
        self.assertEqual(health["status"], "error")
        self.assertEqual(health["evidence"], "HTTP 500")

    @patch('urllib.request.urlopen')
    def test_health_error_exception(self, mock_urlopen):
        mock_urlopen.side_effect = Exception("Connection refused")

        health = self.registry.health()
        self.assertEqual(health["status"], "error")
        self.assertEqual(health["evidence"], "Connection refused")

    @patch('urllib.request.urlopen')
    def test_discover_models_ok(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": [{"id": "model1"}, {"id": "model2"}]}).encode("utf-8")
        mock_urlopen.return_value.__enter__.return_value = mock_response

        models = self.registry.discover_models()
        self.assertEqual(len(models), 2)
        self.assertEqual(models[0]["id"], "model1")

    @patch('urllib.request.urlopen')
    def test_discover_models_error_http(self, mock_urlopen):
        import urllib.error
        mock_urlopen.side_effect = urllib.error.HTTPError(url="", code=404, msg="Not Found", hdrs={}, fp=None)

        models = self.registry.discover_models()
        self.assertEqual(models, [])

    @patch('urllib.request.urlopen')
    def test_discover_models_error_exception(self, mock_urlopen):
        mock_urlopen.side_effect = Exception("Connection refused")

        models = self.registry.discover_models()
        self.assertEqual(models, [])

    def test_estimate_resources(self):
        est = self.registry.estimate_resources("my-gguf-model")
        self.assertEqual(est["model_id"], "my-gguf-model")
        self.assertTrue(est["estimated_ram_mb"] > 0)
        self.assertTrue("estimated_vram_mb" in est)

    def test_load_and_unload_model(self):
        self.assertTrue(self.registry.load_model("model1", ttl=60))
        self.assertIn("model1", self.registry.loaded_models)
        self.assertEqual(self.registry.loaded_models["model1"]["ttl"], 60)

        self.assertTrue(self.registry.unload_model("model1"))
        self.assertNotIn("model1", self.registry.loaded_models)

        # Unloading already unloaded model
        self.assertFalse(self.registry.unload_model("model1"))

    def test_enforce_ttl(self):
        # Load a model that expires immediately
        self.registry.loaded_models["model1"] = {
            "loaded_at": time.time() - 100,
            "ttl": 10
        }
        # Load a model that doesn't expire
        self.registry.loaded_models["model2"] = {
            "loaded_at": time.time(),
            "ttl": 3600
        }
        # Load a model with no TTL
        self.registry.loaded_models["model3"] = {
            "loaded_at": time.time() - 1000,
            "ttl": None
        }

        expired = self.registry.enforce_ttl()
        self.assertEqual(expired, ["model1"])
        self.assertNotIn("model1", self.registry.loaded_models)
        self.assertIn("model2", self.registry.loaded_models)
        self.assertIn("model3", self.registry.loaded_models)

if __name__ == '__main__':
    unittest.main()
