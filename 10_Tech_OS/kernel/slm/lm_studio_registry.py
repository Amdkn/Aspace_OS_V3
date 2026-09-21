import time
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
import urllib.request
import json
import urllib.error

@dataclass
class ModelResourcePolicy:
    context_length: int = 4096
    max_ram_mb: int = 8192
    gpu_layers: int = -1  # -1 means all available

@dataclass
class ModelTTLPolicy:
    ttl_seconds: int = 3600
    last_accessed: float = field(default_factory=time.time)

    def is_expired(self) -> bool:
        return time.time() - self.last_accessed > self.ttl_seconds

    def touch(self):
        self.last_accessed = time.time()

@dataclass
class LoadedModelContext:
    model_id: str
    backend: str = "gguf"
    resource_policy: ModelResourcePolicy = field(default_factory=ModelResourcePolicy)
    ttl_policy: ModelTTLPolicy = field(default_factory=ModelTTLPolicy)

class LMStudioRegistry:
    """Registry to manage LM Studio local serving lifecycle."""

    def __init__(self, api_base_url: str = "http://localhost:1234/v1"):
        self.api_base_url = api_base_url.rstrip("/")
        self.loaded_models: Dict[str, LoadedModelContext] = {}

    def discover_models(self) -> List[Dict[str, Any]]:
        """Discover available GGUF models from LM Studio."""
        try:
            req = urllib.request.Request(f"{self.api_base_url}/models")
            with urllib.request.urlopen(req, timeout=5) as response:
                data = json.loads(response.read().decode())
                return data.get("data", [])
        except (urllib.error.URLError, json.JSONDecodeError):
            return []

    def estimate_resources(self, model_id: str, context_length: int = 4096) -> Dict[str, Any]:
        """Estimate required resources based on model context size and parameters."""
        # A rough estimate for GGUF models. Realistically this requires reading GGUF headers,
        # but for this registry component, we will provide a heuristic.
        base_ram = 2048
        ctx_ram = context_length * 1.5 # approx 1.5MB per token context in 16-bit
        estimated_ram_mb = base_ram + int(ctx_ram / 1024)

        return {
            "model_id": model_id,
            "estimated_ram_mb": min(estimated_ram_mb, 16384),
            "recommended_gpu_layers": -1
        }

    def load_model(self, model_id: str, policy: Optional[ModelResourcePolicy] = None, ttl_seconds: int = 3600) -> bool:
        """Load a model with a specified policy and TTL via LM Studio's API."""
        if policy is None:
            policy = ModelResourcePolicy()

        # Check estimation locally
        est = self.estimate_resources(model_id, policy.context_length)
        if est["estimated_ram_mb"] > policy.max_ram_mb:
            return False

        # Issue HTTP request to load model
        try:
            payload = json.dumps({
                "model": model_id,
                "context_length": policy.context_length,
                "gpu_layers": policy.gpu_layers
            }).encode('utf-8')

            req = urllib.request.Request(
                f"{self.api_base_url}/models/load",
                data=payload,
                headers={'Content-Type': 'application/json'},
                method='POST'
            )
            with urllib.request.urlopen(req, timeout=30) as response:
                if response.getcode() != 200:
                    return False
        except urllib.error.URLError:
            return False

        ttl_policy = ModelTTLPolicy(ttl_seconds=ttl_seconds)
        self.loaded_models[model_id] = LoadedModelContext(
            model_id=model_id,
            resource_policy=policy,
            ttl_policy=ttl_policy
        )
        return True

    def unload_model(self, model_id: str) -> bool:
        """Unload a specific model via LM Studio's API."""
        try:
            req = urllib.request.Request(
                f"{self.api_base_url}/models/unload",
                data=json.dumps({"model": model_id}).encode('utf-8'),
                headers={'Content-Type': 'application/json'},
                method='POST'
            )
            with urllib.request.urlopen(req, timeout=10) as response:
                pass # Doesn't strictly need to check code if it doesn't throw, but it's cleaner
        except urllib.error.URLError:
            # We still might want to remove it locally if it's dead, but let's assume if the API fails
            # it might still be running. For robustness, if it fails to unload on API side, we return False
            return False

        if model_id in self.loaded_models:
            del self.loaded_models[model_id]
        return True

    def touch_model(self, model_id: str) -> bool:
        """Touch a loaded model to extend its TTL."""
        if model_id in self.loaded_models:
            self.loaded_models[model_id].ttl_policy.touch()
            return True
        return False

    def enforce_ttl_policy(self) -> List[str]:
        """Check all models and unload expired ones."""
        expired = []
        for model_id, context in list(self.loaded_models.items()):
            if context.ttl_policy.is_expired():
                if self.unload_model(model_id):
                    expired.append(model_id)
                else:
                    # Could not unload, maybe the server is down? Log warning or handle.
                    pass
        return expired

    def get_health_evidence(self) -> Dict[str, Any]:
        """Provide health evidence of the registry."""
        return {
            "status": "ok",
            "api_base": self.api_base_url,
            "loaded_models_count": len(self.loaded_models),
            "loaded_models": [
                {
                    "id": m.model_id,
                    "ttl_remaining": max(0, int(m.ttl_policy.ttl_seconds - (time.time() - m.ttl_policy.last_accessed)))
                }
                for m in self.loaded_models.values()
            ]
        }
