import json
import urllib.request
import urllib.error
import time

class LMStudioRegistry:
    def __init__(self, base_url="http://127.0.0.1:1234"):
        self.base_url = base_url

    def _make_request(self, method, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        req = urllib.request.Request(url, method=method)
        if payload is not None:
            data = json.dumps(payload).encode('utf-8')
            req.add_header('Content-Type', 'application/json')
            req.data = data

        try:
            with urllib.request.urlopen(req, timeout=5) as response:
                response_data = response.read().decode('utf-8')
                if response_data:
                    return json.loads(response_data)
                return {}
        except urllib.error.URLError as e:
            raise Exception(f"LM Studio API request failed: {e}")

    def health_check(self):
        try:
            self._make_request('GET', '/v1/models')
            return True
        except Exception:
            return False

    def discover_models(self):
        try:
            response = self._make_request('GET', '/v1/models')
            return response.get('data', [])
        except Exception:
            return []

    def estimate_resources(self, model_id):
        # A mock implementation for estimating resources
        return {"ram_required_mb": 4096, "vram_required_mb": 8192}

    def load_model(self, model_id, context_length, ttl_seconds):
        payload = {
            "model": model_id,
            "context_length": context_length,
            "ttl": ttl_seconds
        }
        # Assuming an endpoint for loading the model, LM Studio might just load it automatically,
        # but the prompt requires us to implement load/unload and TTL/resource policy enforcement.
        return self._make_request('POST', '/v1/models/load', payload=payload)

    def unload_model(self, model_id):
        return self._make_request('POST', '/v1/models/unload', payload={"model": model_id})
