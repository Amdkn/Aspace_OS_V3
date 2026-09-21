import unittest
from unittest.mock import patch, MagicMock
import json
import urllib.error
import datetime

# Import assuming it's available in the same parent module path or adjust sys.path
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lm_studio_registry import LMStudioRegistry, ModelPolicy

class TestLMStudioRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = LMStudioRegistry(base_url="http://test-url")

    @patch('urllib.request.urlopen')
    def test_discover_success(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({
            "data": [{"id": "model-1", "object": "model"}]
        }).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response

        models = self.registry.discover()
        self.assertEqual(len(models), 1)
        self.assertEqual(models[0]["id"], "model-1")

    @patch('urllib.request.urlopen')
    def test_discover_failure(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.URLError("Network error")
        models = self.registry.discover()
        self.assertEqual(models, [])

    def test_estimate_resources(self):
        resources = self.registry.estimate_resources("model-1", 5.0)
        self.assertAlmostEqual(resources["ram_gb"], 6.0)
        self.assertAlmostEqual(resources["vram_gb"], 4.0)

    @patch('urllib.request.urlopen')
    def test_load_and_unload_model(self, mock_urlopen):
        policy = ModelPolicy(ttl_seconds=3600, context_size=2048)

        # Load success
        success = self.registry.load_model("model-1", policy)
        self.assertTrue(success)
        self.assertIn("model-1", self.registry._active_models)
        self.assertEqual(self.registry._active_models["model-1"]["policy"].context_size, 2048)

        # Unload success
        success = self.registry.unload_model("model-1")
        self.assertTrue(success)
        self.assertNotIn("model-1", self.registry._active_models)

    @patch('urllib.request.urlopen')
    def test_load_and_unload_failure(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.URLError("Network error")
        policy = ModelPolicy(ttl_seconds=3600, context_size=2048)

        # Load fail
        success = self.registry.load_model("model-1", policy)
        self.assertFalse(success)
        self.assertNotIn("model-1", self.registry._active_models)

        # Assuming it's already there (forced)
        self.registry._active_models["model-1"] = {"loaded_at": datetime.datetime.now(), "policy": policy}

        # Unload fail
        success = self.registry.unload_model("model-1")
        self.assertFalse(success)
        self.assertIn("model-1", self.registry._active_models)


    @patch('urllib.request.urlopen')
    def test_enforce_ttl_policy(self, mock_urlopen):
        policy = ModelPolicy(ttl_seconds=3600, context_size=2048)
        self.registry.load_model("model-1", policy)
        self.registry.load_model("model-2", policy)

        # Manipulate loaded_at to simulate expiration for model-1
        expired_time = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(seconds=4000)
        self.registry._active_models["model-1"]["loaded_at"] = expired_time

        unloaded = self.registry.enforce_ttl_policy()

        self.assertIn("model-1", unloaded)
        self.assertNotIn("model-2", unloaded)
        self.assertNotIn("model-1", self.registry._active_models)
        self.assertIn("model-2", self.registry._active_models)

    @patch('urllib.request.urlopen')
    def test_check_health(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({
            "data": [{"id": "model-1", "object": "model"}]
        }).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response

        policy = ModelPolicy(ttl_seconds=3600, context_size=2048)
        self.registry.load_model("model-1", policy)

        health = self.registry.check_health()
        self.assertEqual(health["status"], "ok")
        self.assertIn("model-1", health["evidence"]["active_models_tracked"])
        self.assertEqual(health["evidence"]["discovered_models"][0]["id"], "model-1")

if __name__ == "__main__":
    unittest.main()
