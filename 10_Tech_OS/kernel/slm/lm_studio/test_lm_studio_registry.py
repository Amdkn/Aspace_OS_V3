import unittest
from unittest.mock import patch, MagicMock
import urllib.error
import time
import sys
from pathlib import Path

# Ensure we can import lm_studio_registry
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from lm_studio_registry import LMStudioRegistry

class TestLMStudioRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = LMStudioRegistry(base_url="http://mock-lm-studio:1234", ttl_seconds=60)

    @patch('urllib.request.urlopen')
    def test_discovery_success(self, mock_urlopen):
        # Mocking the response
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"data": [{"id": "model-1"}, {"id": "model-2"}]}'
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        models = self.registry.discovery()
        self.assertEqual(len(models), 2)
        self.assertEqual(models[0]['id'], "model-1")
        self.assertEqual(models[1]['id'], "model-2")
        mock_urlopen.assert_called_once()

    @patch('urllib.request.urlopen')
    def test_discovery_failure(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.URLError("Mock Connection Refused")

        models = self.registry.discovery()
        self.assertEqual(models, [])
        mock_urlopen.assert_called_once()

    def test_estimate(self):
        estimate = self.registry.estimate("llama-3-8b.gguf")
        self.assertEqual(estimate["model_id"], "llama-3-8b.gguf")
        self.assertIn("estimated_ram_mb", estimate)
        self.assertTrue(estimate["can_fit_in_vram"])

    def test_load_and_unload(self):
        model_id = "test-model-gguf"

        self.registry.load(model_id)
        self.assertIn(model_id, self.registry._model_last_active)

        self.registry.unload(model_id)
        self.assertNotIn(model_id, self.registry._model_last_active)

    def test_ping_model(self):
        model_id = "ping-model"
        self.registry.ping_model(model_id)
        self.assertIn(model_id, self.registry._model_last_active)

        initial_time = self.registry._model_last_active[model_id]
        time.sleep(0.01) # Small delay

        self.registry.ping_model(model_id)
        self.assertGreater(self.registry._model_last_active[model_id], initial_time)

    def test_enforce_ttl(self):
        model_1 = "model-1"
        model_2 = "model-2"

        self.registry.load(model_1)
        self.registry.load(model_2)

        # Manually backdate model-1 beyond TTL (60s)
        self.registry._model_last_active[model_1] = time.time() - 100

        unloaded = self.registry.enforce_ttl()

        self.assertIn(model_1, unloaded)
        self.assertNotIn(model_2, unloaded)

        self.assertNotIn(model_1, self.registry._model_last_active)
        self.assertIn(model_2, self.registry._model_last_active)

    @patch('urllib.request.urlopen')
    def test_health_healthy(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"data": [{"id": "model-1"}]}'
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        self.registry.load("loaded-model-1")

        health = self.registry.health()
        self.assertEqual(health["status"], "healthy")
        self.assertEqual(health["available_models_count"], 1)
        self.assertIn("loaded-model-1", health["loaded_models_tracked"])

    @patch('urllib.request.urlopen')
    def test_health_unhealthy(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.URLError("Mock Connection Refused")

        health = self.registry.health()
        self.assertEqual(health["status"], "unhealthy")
        self.assertEqual(health["available_models_count"], 0)

if __name__ == '__main__':
    unittest.main()
