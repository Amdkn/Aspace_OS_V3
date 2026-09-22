import urllib.request
import urllib.error
import json
import time
from typing import Dict, Any

class LMStudioRegistry:
    """LM Studio local serving registry for GGUF backends.

    Provides capabilities for model discovery, estimation, load/unload,
    health checks, and TTL/resource policy enforcement.
    """
    def __init__(self, base_url="http://127.0.0.1:1234"):
        self.base_url = base_url.rstrip("/")
        # In-memory tracking for TTL policy enforcement
        self._loaded_models = {}

    def _request(self, endpoint, method="GET", data=None) -> Dict[str, Any]:
        url = f"{self.base_url}{endpoint}"
        req = urllib.request.Request(url, method=method)
        if data is not None:
            req.data = json.dumps(data).encode("utf-8")
            req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req) as response:
                response_data = response.read().decode("utf-8")
                return json.loads(response_data) if response_data else {}
        except urllib.error.URLError as e:
            return {"error": str(e)}
        except json.JSONDecodeError:
            return {"error": "Invalid JSON response"}

    def discovery(self):
        """Discovers available models via /v1/models"""
        return self._request("/v1/models")

    def estimate(self, model_id):
        """Estimates resource requirements for a model."""
        # Simulated or generic endpoint for estimation
        return self._request(f"/api/v0/models/{model_id}/estimate")

    def load(self, model_id, context_length=2048, ttl=3600):
        """Loads a model with context/TTL/resource policy."""
        data = {
            "model": model_id,
            "context_length": context_length,
            "ttl": ttl
        }
        res = self._request("/api/v0/models/load", method="POST", data=data)
        if "error" not in res:
            self._loaded_models[model_id] = {
                "loaded_at": time.time(),
                "ttl": ttl,
                "context_length": context_length
            }
        return res

    def unload(self, model_id):
        """Unloads a model to free resources."""
        data = {"model": model_id}
        res = self._request("/api/v0/models/unload", method="POST", data=data)
        if "error" not in res and model_id in self._loaded_models:
            del self._loaded_models[model_id]
        return res

    def health(self):
        """Health check and evidence for the LM Studio instance."""
        res = self._request("/v1/models")
        if "error" in res:
            return {"status": "unhealthy", "evidence": res["error"]}
        return {"status": "healthy", "evidence": "LM Studio is responding"}

    def enforce_ttl_policy(self):
        """Checks loaded models and unloads those that exceeded their TTL."""
        current_time = time.time()
        unloaded = []
        # Create a list of keys to avoid modifying dict during iteration
        for model_id, info in list(self._loaded_models.items()):
            if current_time - info["loaded_at"] > info["ttl"]:
                self.unload(model_id)
                unloaded.append(model_id)
        return unloaded
