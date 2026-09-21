import unittest
from unittest.mock import patch, MagicMock
import json
import urllib.error
import datetime
from slm.lm_studio_registry import LMStudioRegistry

class TestLMStudioRegistry(unittest.TestCase):

    def setUp(self):
        self.registry = LMStudioRegistry()

    @patch('urllib.request.urlopen')
    def test_get_health_evidence_healthy(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        result = self.registry.get_health_evidence()
        self.assertEqual(result["status"], "healthy")
        self.assertEqual(result["evidence"], "endpoint reachable")

    @patch('urllib.request.urlopen')
    def test_get_health_evidence_unhealthy(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.status = 500
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        result = self.registry.get_health_evidence()
        self.assertEqual(result["status"], "unhealthy")

    @patch('urllib.request.urlopen')
    def test_discover_models_success(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_data = {
            "data": [
                {"id": "model-1", "object": "model"},
                {"id": "model-2", "object": "model"}
            ]
        }
        mock_response.read.return_value = json.dumps(mock_data).encode('utf-8')
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        models = self.registry.discover_models()
        self.assertEqual(len(models), 2)
        self.assertEqual(models[0]["id"], "model-1")

    @patch('urllib.request.urlopen')
    def test_discover_models_failure(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.URLError("Network error")
        models = self.registry.discover_models()
        self.assertEqual(models, [])

    @patch.object(LMStudioRegistry, 'discover_models')
    def test_estimate_available(self, mock_discover):
        mock_discover.return_value = [{"id": "test-model"}]
        result = self.registry.estimate("test-model")
        self.assertTrue(result["estimable"])
        self.assertEqual(result["model"], "test-model")

    @patch.object(LMStudioRegistry, 'discover_models')
    def test_estimate_not_found(self, mock_discover):
        mock_discover.return_value = [{"id": "other-model"}]
        result = self.registry.estimate("test-model")
        self.assertFalse(result["estimable"])
        self.assertEqual(result["status"], "not_found")

    @patch.object(LMStudioRegistry, 'estimate')
    def test_load_model_success(self, mock_estimate):
        mock_estimate.return_value = {"estimable": True}
        success = self.registry.load_model("test-model", ttl=60)
        self.assertTrue(success)
        self.assertIn("test-model", self.registry.loaded_models)
        self.assertEqual(self.registry.loaded_models["test-model"]["ttl"], 60)

    @patch.object(LMStudioRegistry, 'estimate')
    def test_load_model_failure(self, mock_estimate):
        mock_estimate.return_value = {"estimable": False}
        success = self.registry.load_model("test-model")
        self.assertFalse(success)
        self.assertNotIn("test-model", self.registry.loaded_models)

    def test_unload_model(self):
        self.registry.loaded_models["test-model"] = {"loaded_at": datetime.datetime.now(datetime.timezone.utc), "ttl": 60, "policy": {}}
        success = self.registry.unload_model("test-model")
        self.assertTrue(success)
        self.assertNotIn("test-model", self.registry.loaded_models)

        success_again = self.registry.unload_model("test-model")
        self.assertFalse(success_again)

    def test_enforce_ttl_policy(self):
        now = datetime.datetime.now(datetime.timezone.utc)
        self.registry.loaded_models["model-expired"] = {
            "loaded_at": now - datetime.timedelta(seconds=100),
            "ttl": 60,
            "policy": {}
        }
        self.registry.loaded_models["model-active"] = {
            "loaded_at": now - datetime.timedelta(seconds=10),
            "ttl": 60,
            "policy": {}
        }

        unloaded = self.registry.enforce_ttl_policy()
        self.assertIn("model-expired", unloaded)
        self.assertNotIn("model-active", unloaded)
        self.assertNotIn("model-expired", self.registry.loaded_models)
        self.assertIn("model-active", self.registry.loaded_models)

if __name__ == '__main__':
    unittest.main()
