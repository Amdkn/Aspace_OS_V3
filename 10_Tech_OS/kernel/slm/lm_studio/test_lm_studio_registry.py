import unittest
from unittest.mock import patch, MagicMock
import urllib.error
import time
from slm.lm_studio.lm_studio_registry import LMStudioRegistry

class TestLMStudioRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = LMStudioRegistry()

    @patch('urllib.request.urlopen')
    def test_health_check_success(self, mock_urlopen):
        # Mock successful response
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"data": []}'
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        self.assertTrue(self.registry.health_check())

    @patch('urllib.request.urlopen')
    def test_health_check_failure(self, mock_urlopen):
        # Mock failed response
        mock_urlopen.side_effect = urllib.error.URLError("Connection refused")

        self.assertFalse(self.registry.health_check())

    @patch('urllib.request.urlopen')
    def test_discover_models_success(self, mock_urlopen):
        mock_response = MagicMock()
        mock_data = b'{"data": [{"id": "model-1"}, {"id": "model-2"}]}'
        mock_response.read.return_value = mock_data
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        models = self.registry.discover_models()
        self.assertEqual(len(models), 2)
        self.assertEqual(models[0]['id'], 'model-1')
        self.assertEqual(models[1]['id'], 'model-2')

    @patch('urllib.request.urlopen')
    def test_discover_models_failure(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.URLError("Connection refused")
        models = self.registry.discover_models()
        self.assertEqual(models, [])

    def test_estimate_resources(self):
        estimate = self.registry.estimate_resources("test-model")
        self.assertIn("estimated_ram_mb", estimate)
        self.assertEqual(estimate["model_id"], "test-model")

    @patch.object(LMStudioRegistry, 'health_check')
    def test_load_and_unload_model(self, mock_health_check):
        mock_health_check.return_value = True

        # Test load
        success = self.registry.load_model("test-model", ttl=3600)
        self.assertTrue(success)
        self.assertIn("test-model", self.registry.active_models)
        self.assertIn("test-model", self.registry.policies)

        # Test unload
        success = self.registry.unload_model("test-model")
        self.assertTrue(success)
        self.assertNotIn("test-model", self.registry.active_models)
        self.assertNotIn("test-model", self.registry.policies)

    @patch.object(LMStudioRegistry, 'health_check')
    def test_enforce_ttl_policy(self, mock_health_check):
        mock_health_check.return_value = True

        # Load a model with a very short TTL
        self.registry.load_model("short-ttl-model", ttl=0)

        # Load a model with a long TTL
        self.registry.load_model("long-ttl-model", ttl=3600)

        # Add a small delay to ensure the short TTL expires
        time.sleep(0.1)

        unloaded = self.registry.enforce_ttl_policy()

        self.assertIn("short-ttl-model", unloaded)
        self.assertNotIn("long-ttl-model", unloaded)

        # Verify internal state
        self.assertNotIn("short-ttl-model", self.registry.active_models)
        self.assertIn("long-ttl-model", self.registry.active_models)

if __name__ == '__main__':
    unittest.main()
