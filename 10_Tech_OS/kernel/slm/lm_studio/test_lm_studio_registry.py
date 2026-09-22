import unittest
from unittest.mock import patch, MagicMock
import urllib.error
import datetime
import sys
import os

# Add the parent directory to sys.path to allow imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from lm_studio_registry import LMStudioRegistry

class TestLMStudioRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = LMStudioRegistry(ttl_seconds=3600, max_ram_gb=16.0)

    @patch('urllib.request.urlopen')
    def test_discover_models_success(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"data": [{"id": "llama-2-7b-chat.Q4_K_M.gguf"}]}'
        mock_urlopen.return_value.__enter__.return_value = mock_response

        models = self.registry.discover_models()
        self.assertEqual(len(models), 1)
        self.assertEqual(models[0]['id'], "llama-2-7b-chat.Q4_K_M.gguf")

    @patch('urllib.request.urlopen')
    def test_discover_models_failure(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.URLError("Connection refused")
        with self.assertRaises(RuntimeError):
            self.registry.discover_models()

    def test_estimate_resources(self):
        est1 = self.registry.estimate_resources("llama-2-7b-chat.Q4_K_M.gguf")
        self.assertEqual(est1["parameters_b"], 7.0)
        self.assertEqual(est1["quantization_bits"], 4)
        self.assertEqual(est1["estimated_ram_gb"], 5.0)

        est2 = self.registry.estimate_resources("mixtral-8x7b-v0.1.Q8_0.gguf")
        self.assertEqual(est2["parameters_b"], 7.0)
        self.assertEqual(est2["quantization_bits"], 8)
        self.assertEqual(est2["estimated_ram_gb"], 8.5)

    def test_can_load_model(self):
        # 1. 5GB + 2. 8.5GB = 13.5GB <= 16.0GB
        self.registry.loaded_models["llama-2-7b-chat.Q4_K_M.gguf"] = {}
        self.assertTrue(self.registry.can_load_model("mixtral-8x7b-v0.1.Q8_0.gguf"))

        # 1. 5GB + 2. 8.5GB + 3. 5GB = 18.5GB > 16.0GB
        self.registry.loaded_models["mixtral-8x7b-v0.1.Q8_0.gguf"] = {}
        self.assertFalse(self.registry.can_load_model("llama-3-8b.Q4_K_M.gguf"))

    def test_load_model(self):
        self.assertTrue(self.registry.load_model("llama-2-7b-chat.Q4_K_M.gguf"))
        self.assertIn("llama-2-7b-chat.Q4_K_M.gguf", self.registry.loaded_models)

        # Should fail due to resource policy
        self.registry.loaded_models["mixtral-8x7b-v0.1.Q8_0.gguf"] = {}
        self.registry.loaded_models["llama-3-8b.Q4_K_M.gguf"] = {}
        self.assertFalse(self.registry.load_model("another-model-7b.Q4_0.gguf"))

    def test_track_inference(self):
        self.registry.track_inference("test-7b.Q4.gguf")
        self.assertIn("test-7b.Q4.gguf", self.registry.loaded_models)

        first_used = self.registry.loaded_models["test-7b.Q4.gguf"]["last_used"]
        self.registry.track_inference("test-7b.Q4.gguf")
        second_used = self.registry.loaded_models["test-7b.Q4.gguf"]["last_used"]

        self.assertGreaterEqual(second_used, first_used)

        # Test resource policy enforcement on implicit load
        self.registry.loaded_models["mixtral-8x7b-v0.1.Q8_0.gguf"] = {}
        self.registry.loaded_models["llama-3-8b.Q4_K_M.gguf"] = {}
        self.registry.track_inference("another-model-7b.Q4_0.gguf")
        self.assertNotIn("another-model-7b.Q4_0.gguf", self.registry.loaded_models)

    @patch('urllib.request.urlopen')
    def test_unload_model(self, mock_urlopen):
        self.registry.loaded_models["test_model"] = {
            "loaded_at": datetime.datetime.now(datetime.timezone.utc),
            "last_used": datetime.datetime.now(datetime.timezone.utc)
        }

        self.registry.unload_model("test_model")

        self.assertNotIn("test_model", self.registry.loaded_models)
        self.assertEqual(mock_urlopen.call_count, 2)

    @patch.object(LMStudioRegistry, 'unload_model')
    def test_enforce_ttl(self, mock_unload_model):
        now = datetime.datetime.now(datetime.timezone.utc)

        self.registry.loaded_models["active_model"] = {
            "loaded_at": now,
            "last_used": now
        }

        past = now - datetime.timedelta(seconds=4000)
        self.registry.loaded_models["expired_model"] = {
            "loaded_at": past,
            "last_used": past
        }

        self.registry.enforce_ttl()

        mock_unload_model.assert_called_once_with("expired_model")

    @patch.object(LMStudioRegistry, 'discover_models')
    def test_health_check(self, mock_discover):
        mock_discover.return_value = [{"id": "model1"}]
        health = self.registry.health_check()
        self.assertEqual(health["status"], "healthy")
        self.assertIn("Discovered 1 models", health["evidence"])

        mock_discover.side_effect = Exception("API down")
        health = self.registry.health_check()
        self.assertEqual(health["status"], "unhealthy")
        self.assertIn("API down", health["error"])

if __name__ == '__main__':
    unittest.main()
