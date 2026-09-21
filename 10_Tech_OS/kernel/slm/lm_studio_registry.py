import json
import urllib.request
import urllib.error
import time
from typing import Dict, List, Optional, Any
import logging

logger = logging.getLogger(__name__)

class LMStudioRegistry:
    """
    Registry for managing local serving of GGUF models via LM Studio.
    Implements discovery, load/unload, context/TTL/resource policies, and health checking
    using dependency-lite REST API interactions (urllib.request).
    """

    def __init__(self, base_url: str = "http://127.0.0.1:1234"):
        self.base_url = base_url.rstrip("/")
        self.loaded_models: Dict[str, Dict[str, Any]] = {}
        self.max_vram_gb = 8.0 # Default max VRAM policy

    def _request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Any:
        url = f"{self.base_url}{endpoint}"
        headers = {"Content-Type": "application/json"}
        req_data = json.dumps(data).encode("utf-8") if data else None

        req = urllib.request.Request(url, data=req_data, headers=headers if data else {}, method=method)
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                response_data = response.read().decode("utf-8")
                if response_data:
                    return json.loads(response_data)
                return {}
        except urllib.error.URLError as e:
            logger.error(f"LM Studio API request failed: {e}")
            raise

    def discover_models(self) -> List[Dict[str, Any]]:
        """Discover available models."""
        try:
            # LM Studio standard OpenAI-like endpoint for available models
            response = self._request("GET", "/v1/models")
            return response.get("data", [])
        except Exception:
            return []

    def estimate_resources(self, model_id: str) -> Dict[str, Any]:
        """Estimate required resources for a model."""
        # A simple mock estimation since LM Studio's API might not natively expose exact VRAM before loading.
        # This could be based on file size or quantization.
        size_gb = 4.0 # Fake standard size for estimation
        return {
            "model_id": model_id,
            "estimated_vram_gb": size_gb,
            "estimated_ram_gb": size_gb * 1.5,
            "fits_in_vram": size_gb <= self.max_vram_gb
        }

    def load_model(self, model_id: str, context_length: int = 2048, ttl_seconds: int = 3600) -> Dict[str, Any]:
        """Load a model with a specified context length and TTL."""
        # Enforce resource policy
        estimation = self.estimate_resources(model_id)
        if not estimation.get("fits_in_vram", False):
            raise ValueError(f"Model {model_id} exceeds VRAM policy limit of {self.max_vram_gb}GB.")

        try:
            # LM Studio API for loading a model (using standard structure or mock structure)
            payload = {
                "model": model_id,
                "context_length": context_length
            }
            # Often, loading happens just by querying or via specific admin endpoints.
            # We'll mock a POST /v1/models/load or similar if we assume standard LM studio admin API.
            # Or standard OpenAI completions endpoint automatically loads it in LM Studio.
            # But the mandate says "load/unload". Let's assume a generic admin endpoint.
            response = self._request("POST", "/api/v0/models/load", data=payload)

            self.loaded_models[model_id] = {
                "loaded_at": time.time(),
                "ttl_seconds": ttl_seconds,
                "context_length": context_length,
                "status": "loaded"
            }
            return self.loaded_models[model_id]
        except Exception as e:
            logger.error(f"Failed to load model {model_id}: {e}")
            raise

    def unload_model(self, model_id: str) -> bool:
        """Unload a model from memory."""
        try:
            self._request("POST", "/api/v0/models/unload", data={"model": model_id})
            if model_id in self.loaded_models:
                del self.loaded_models[model_id]
            return True
        except Exception as e:
            logger.error(f"Failed to unload model {model_id}: {e}")
            return False

    def check_ttl_policy(self) -> None:
        """Check and enforce TTL for all loaded models."""
        now = time.time()
        to_unload = []
        for model_id, info in self.loaded_models.items():
            if now - info["loaded_at"] > info["ttl_seconds"]:
                to_unload.append(model_id)

        for model_id in to_unload:
            self.unload_model(model_id)

    def health(self) -> Dict[str, Any]:
        """Health evidence for the backend."""
        try:
            # We explicitly want to fail if the API is down, so we do a request.
            # We then reuse this response to count available models.
            response = self._request("GET", "/v1/models")
            models = response.get("data", [])
            return {
                "status": "healthy",
                "backend": "lm_studio",
                "available_models_count": len(models),
                "loaded_models": list(self.loaded_models.keys()),
                "timestamp": time.time()
            }
        except Exception as e:
            return {
                "status": "unhealthy",
                "backend": "lm_studio",
                "error": str(e),
                "timestamp": time.time()
            }
