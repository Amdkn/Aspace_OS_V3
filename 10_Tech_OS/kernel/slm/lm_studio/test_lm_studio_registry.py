import unittest
from unittest.mock import patch, MagicMock
import json
import urllib.error

# Import the registry class
from slm.lm_studio_registry import LMStudioRegistry

class TestLMStudioRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = LMStudioRegistry()

    @patch('urllib.request.urlopen')
    def test_health_check_ok(self, mock_urlopen):
        # Mock successful response
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({"data": []}).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response

        self.assertTrue(self.registry.health_check())

    @patch('urllib.request.urlopen')
    def test_health_check_fail(self, mock_urlopen):
        # Mock failed response
        mock_urlopen.side_effect = urllib.error.URLError("Connection refused")

        self.assertFalse(self.registry.health_check())

    @patch('urllib.request.urlopen')
    def test_discover_models(self, mock_urlopen):
        # Mock models response
        mock_response = MagicMock()
        mock_data = {
            "data": [
                {"id": "model-1", "object": "model"},
                {"id": "model-2", "object": "model"}
            ]
        }
        mock_response.read.return_value = json.dumps(mock_data).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response

        models = self.registry.discover_models()
        self.assertEqual(len(models), 2)
        self.assertEqual(models[0]['id'], "model-1")

    @patch('urllib.request.urlopen')
    def test_load_model_success(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({"status": "success"}).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response

        res = self.registry.load_model("model-1", 2048, 3600)
        self.assertEqual(res, {"status": "success"})

        # Verify request details
        req = mock_urlopen.call_args[0][0]
        self.assertEqual(req.method, "POST")
        payload = json.loads(req.data.decode('utf-8'))
        self.assertEqual(payload["model"], "model-1")
        self.assertEqual(payload["context_length"], 2048)
        self.assertEqual(payload["ttl"], 3600)

    @patch('urllib.request.urlopen')
    def test_unload_model(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({"status": "unloaded"}).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response

        res = self.registry.unload_model("model-1")
        self.assertEqual(res, {"status": "unloaded"})

        # Verify request details
        req = mock_urlopen.call_args[0][0]
        self.assertEqual(req.method, "POST")
        payload = json.loads(req.data.decode('utf-8'))
        self.assertEqual(payload["model"], "model-1")

    def test_estimate_resources(self):
        res = self.registry.estimate_resources("model-1")
        self.assertIn("ram_required_mb", res)
        self.assertIn("vram_required_mb", res)

if __name__ == '__main__':
    unittest.main()
