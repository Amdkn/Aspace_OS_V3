import urllib.request
import urllib.error
import json
import time
from typing import List, Dict, Any, Optional

class LMStudioRegistry:
    """
    Handles local serving registry for GGUF backends via LM Studio.
    Provides methods for model discovery, health checks, load/unload, and TTL enforcement.
    """

    def __init__(self, base_url: str = "http://127.0.0.1:1234"):
        self.base_url = base_url.rstrip('/')
        self.active_models: Dict[str, Dict[str, Any]] = {}
        # Stores context/policy like {"model_id": {"loaded_at": timestamp, "ttl": seconds}}
        self.policies: Dict[str, Dict[str, Any]] = {}

    def _make_request(self, method: str, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}{endpoint}"
        req = urllib.request.Request(url, method=method)
        req.add_header('Content-Type', 'application/json')

        if data is not None:
            json_data = json.dumps(data).encode('utf-8')
            req.data = json_data

        try:
            with urllib.request.urlopen(req) as response:
                response_data = response.read().decode('utf-8')
                if response_data:
                    return json.loads(response_data)
                return {}
        except urllib.error.URLError as e:
            raise RuntimeError(f"Request failed: {e}")

    def health_check(self) -> bool:
        """Checks if the LM Studio server is responsive."""
        try:
            # Most LM Studio setups respond to /v1/models
            self._make_request("GET", "/v1/models")
            return True
        except RuntimeError:
            return False

    def discover_models(self) -> List[Dict[str, Any]]:
        """Discovers available models via LM Studio API."""
        try:
            response = self._make_request("GET", "/v1/models")
            return response.get("data", [])
        except RuntimeError as e:
            print(f"Error discovering models: {e}")
            return []

    def estimate_resources(self, model_id: str) -> Dict[str, Any]:
        """
        Estimates resource requirement for a model.
        In LM Studio, exact resource estimation without loading might be tricky via standard API,
        but we return a stubbed dictionary representing context for now.
        """
        # Note: In a real system, you might fetch model size from metadata
        return {"estimated_ram_mb": 4096, "requires_gpu": True, "model_id": model_id}

    def load_model(self, model_id: str, ttl: int = 3600) -> bool:
        """
        Loads a model in LM Studio.
        Note: The LM Studio standard /v1 endpoint is OpenAI compatible,
        so model loading typically happens implicitly on first inference or via specific admin endpoints if exposed.
        We'll mock the registry tracking side of it.
        """
        if not self.health_check():
            return False

        # Simulating model load tracking
        self.active_models[model_id] = {"status": "loaded"}
        self.policies[model_id] = {
            "loaded_at": time.time(),
            "ttl": ttl
        }
        return True

    def unload_model(self, model_id: str) -> bool:
        """
        Unloads a model from LM Studio.
        """
        if model_id in self.active_models:
            del self.active_models[model_id]
        if model_id in self.policies:
            del self.policies[model_id]
        return True

    def enforce_ttl_policy(self) -> List[str]:
        """
        Checks loaded models against their TTL policies and unloads them if expired.
        Returns a list of unloaded model IDs.
        """
        current_time = time.time()
        unloaded_models = []

        # Create list of models to check to avoid modifying dict during iteration
        models_to_check = list(self.policies.items())

        for model_id, policy in models_to_check:
            loaded_at = policy.get("loaded_at", 0)
            ttl = policy.get("ttl", 3600)

            if current_time - loaded_at > ttl:
                self.unload_model(model_id)
                unloaded_models.append(model_id)

        return unloaded_models
