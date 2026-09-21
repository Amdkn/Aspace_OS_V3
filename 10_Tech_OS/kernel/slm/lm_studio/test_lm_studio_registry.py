import unittest
from unittest.mock import patch, MagicMock
import time
import json
import urllib.request
import urllib.error
import sys
import os

# Add parent directory to path so we can import lm_studio_registry directly
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lm_studio_registry import LMStudioRegistry

class TestLMStudioRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = LMStudioRegistry()

    @patch('lm_studio_registry.urlopen')
    def test_get_available_models(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({"data": [{"id": "model-1"}]}).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response

        models = self.registry.get_available_models()
        self.assertEqual(len(models), 1)
        self.assertEqual(models[0]["id"], "model-1")

    @patch('lm_studio_registry.urlopen')
    def test_load_model(self, mock_urlopen):
        mock_response = MagicMock()
        mock_urlopen.return_value.__enter__.return_value = mock_response

        result = self.registry.load_model("model-1")
        self.assertTrue(result)
        self.assertIn("model-1", self.registry.loaded_models)

    @patch('lm_studio_registry.urlopen')
    def test_unload_model(self, mock_urlopen):
        mock_response = MagicMock()
        mock_urlopen.return_value.__enter__.return_value = mock_response

        self.registry.loaded_models["model-1"] = time.time()
        result = self.registry.unload_model("model-1")

        self.assertTrue(result)
        self.assertNotIn("model-1", self.registry.loaded_models)

    @patch('lm_studio_registry.urlopen')
    def test_enforce_ttl(self, mock_urlopen):
        mock_response = MagicMock()
        mock_urlopen.return_value.__enter__.return_value = mock_response

        self.registry.loaded_models["model-1"] = time.time() - 400 # 400 seconds ago, ttl is 300

        self.registry.enforce_ttl()
        self.assertNotIn("model-1", self.registry.loaded_models)

    @patch('lm_studio_registry.urlopen')
    def test_get_health(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({"data": [{"id": "model-1"}]}).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response

        health = self.registry.get_health()
        self.assertEqual(health["status"], "healthy")
        self.assertEqual(health["available_models"], 1)
        self.assertEqual(health["resource_estimate_gb"], 4)

if __name__ == '__main__':
    unittest.main()
