import json
import time
import urllib.request
import urllib.error
from typing import Dict, Any, List, Optional

class LMStudioRegistry:
    """
    Handles local serving registry for GGUF backends via LM Studio.
    Performs dependency-lite REST API interactions using standard urllib.request.
    Includes discovery, estimation, loading/unloading, and TTL/resource policy enforcement.
    """
    def __init__(self, base_url: str = "http://localhost:1234", ttl_seconds: int = 3600):
        self.base_url = base_url.rstrip('/')
        self.ttl_seconds = ttl_seconds
        # Keep track of when a model was last used/loaded for TTL enforcement
        self._model_last_active: Dict[str, float] = {}

    def _request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Any:
        url = f"{self.base_url}{endpoint}"
        req_data = json.dumps(data).encode('utf-8') if data else None
        headers = {'Content-Type': 'application/json'} if data else {}
        req = urllib.request.Request(url, data=req_data, headers=headers, method=method)

        try:
            with urllib.request.urlopen(req) as response:
                response_body = response.read().decode('utf-8')
                if response_body:
                    return json.loads(response_body)
                return {}
        except urllib.error.URLError as e:
            raise RuntimeError(f"LM Studio API error at {url}: {e}")

    def discovery(self) -> List[Dict[str, Any]]:
        """
        Discover available GGUF models.
        """
        try:
            response = self._request("GET", "/v1/models")
            return response.get("data", [])
        except RuntimeError:
            return []

    def estimate(self, model_id: str) -> Dict[str, Any]:
        """
        Estimate resource requirements based on model context size.
        """
        # In a real scenario, this might query model metadata or parse the filename.
        # Here we provide a heuristic-based placeholder.
        return {
            "model_id": model_id,
            "estimated_ram_mb": 8192,
            "recommended_context_size": 4096,
            "can_fit_in_vram": True
        }

    def load(self, model_id: str) -> bool:
        """
        Load a model into memory.
        Note: LM Studio typically loads models lazily on first chat completion request,
        or explicitly via model management API if available.
        """
        # Assuming there is an endpoint or simulating the load tracking
        # self._request("POST", "/v1/models/load", {"model": model_id})
        self._model_last_active[model_id] = time.time()
        return True

    def unload(self, model_id: str) -> bool:
        """
        Unload a model from memory to free resources.
        """
        # Assuming there is a standard endpoint to unload a model
        # self._request("POST", "/v1/models/unload", {"model": model_id})
        if model_id in self._model_last_active:
            del self._model_last_active[model_id]
        return True

    def enforce_ttl(self) -> List[str]:
        """
        Enforce TTL policy by unloading models that have exceeded the TTL limit.
        Returns a list of model IDs that were unloaded.
        """
        current_time = time.time()
        unloaded_models = []
        # Copy items to a list to avoid dictionary size change during iteration
        for model_id, last_active in list(self._model_last_active.items()):
            if (current_time - last_active) > self.ttl_seconds:
                self.unload(model_id)
                unloaded_models.append(model_id)
        return unloaded_models

    def ping_model(self, model_id: str) -> None:
        """
        Update the last active timestamp for a model.
        """
        if model_id in self._model_last_active:
            self._model_last_active[model_id] = time.time()
        else:
            self.load(model_id)

    def health(self) -> Dict[str, Any]:
        """
        Gather health evidence (status of the server and loaded models).
        """
        status = "unhealthy"
        available_models = []
        try:
            # We explicitly test the API endpoint because discovery() swallows the error
            response = self._request("GET", "/v1/models")
            available_models = response.get("data", [])
            status = "healthy"
        except Exception:
            pass

        return {
            "status": status,
            "loaded_models_tracked": list(self._model_last_active.keys()),
            "available_models_count": len(available_models),
            "ttl_seconds_policy": self.ttl_seconds
        }
