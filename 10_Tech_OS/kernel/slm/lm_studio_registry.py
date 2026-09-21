import json
import urllib.request
import urllib.error
from typing import Dict, Any, List, Optional
import datetime

class ModelPolicy:
    def __init__(self, ttl_seconds: int = 3600, context_size: int = 4096):
        self.ttl_seconds = ttl_seconds
        self.context_size = context_size

class LMStudioRegistry:
    def __init__(self, base_url: str = "http://localhost:1234"):
        self.base_url = base_url
        self._active_models: Dict[str, Dict[str, Any]] = {}

    def discover(self) -> List[Dict[str, Any]]:
        """Discover available/loaded models from LM Studio."""
        req = urllib.request.Request(f"{self.base_url}/v1/models", method="GET")
        try:
            with urllib.request.urlopen(req, timeout=5) as response:
                data = json.loads(response.read().decode('utf-8'))
                return data.get("data", [])
        except (urllib.error.URLError, json.JSONDecodeError):
            return []

    def estimate_resources(self, model_id: str, size_gb: float) -> Dict[str, float]:
        """Estimate RAM and VRAM requirements for a GGUF backend."""
        # Simple heuristic for demonstration
        ram_gb = size_gb * 1.2
        vram_gb = size_gb * 0.8  # Assume some offloading
        return {
            "ram_gb": round(ram_gb, 2),
            "vram_gb": round(vram_gb, 2)
        }

    def load_model(self, model_id: str, policy: ModelPolicy) -> bool:
        """Load a model with the specified policy."""
        # Note: Since standard OpenAI compatible APIs don't typically have a dedicated /load endpoint
        # in the same way, we are modelling the interaction conceptually based on the PRD requirements.
        # We will track internal state but we should fail if the backend is not reachable.

        # We ping the models endpoint to ensure the backend is available
        req = urllib.request.Request(f"{self.base_url}/v1/models", method="GET")
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                pass
        except urllib.error.URLError as e:
            # Propagate error or fail if the backend is unavailable
            return False

        # In a real implementation this would call a specific /load endpoint if LM Studio exposes it
        # For now, if the server is up, we track it as active
        self._active_models[model_id] = {
            "loaded_at": datetime.datetime.now(datetime.timezone.utc),
            "policy": policy
        }
        return True

    def unload_model(self, model_id: str) -> bool:
        """Unload a model from LM Studio."""
        # We ping the models endpoint to ensure the backend is available before updating state
        req = urllib.request.Request(f"{self.base_url}/v1/models", method="GET")
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                pass
        except urllib.error.URLError as e:
             # Propagate error or fail if the backend is unavailable
            return False

        # Update local tracking registry
        if model_id in self._active_models:
            del self._active_models[model_id]
        return True

    def enforce_ttl_policy(self) -> List[str]:
        """Enforce TTL policy on all active models and unload if expired."""
        unloaded = []
        now = datetime.datetime.now(datetime.timezone.utc)
        # Iterate over a copy of keys since we are modifying the dict
        for model_id, info in list(self._active_models.items()):
            loaded_at = info["loaded_at"]
            policy = info["policy"]
            elapsed = (now - loaded_at).total_seconds()
            if elapsed > policy.ttl_seconds:
                # Assuming unload_model is successful here, unload
                if self.unload_model(model_id):
                    unloaded.append(model_id)
        return unloaded

    def check_health(self) -> Dict[str, Any]:
        """Return connectivity and active models evidence."""
        req = urllib.request.Request(f"{self.base_url}/v1/models", method="GET")
        try:
            with urllib.request.urlopen(req, timeout=5) as response:
                 data = json.loads(response.read().decode('utf-8'))
                 models = data.get("data", [])
                 status = "ok"
        except (urllib.error.URLError, json.JSONDecodeError):
            models = []
            status = "unavailable"

        return {
            "status": status,
            "evidence": {
                "active_models_tracked": list(self._active_models.keys()),
                "discovered_models": models
            }
        }
