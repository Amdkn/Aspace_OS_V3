#!/usr/bin/env python3
"""
lm_studio_registry.py — Local serving registry for GGUF backends via LM Studio.
Handles discovery, resource estimation, loading/unloading, and TTL policy enforcement
using dependency-lite REST API interactions.
"""

import json
import urllib.request
import urllib.error
import time
from typing import List, Dict, Any, Optional

class LMStudioRegistry:
    def __init__(self, base_url: str = "http://127.0.0.1:1234"):
        self.base_url = base_url.rstrip("/")
        self.loaded_models: Dict[str, Dict[str, Any]] = {}
        self.default_ttl = 3600  # 1 hour in seconds

    def _request(self, endpoint: str, method: str = "GET", data: Optional[Dict[str, Any]] = None) -> Any:
        """Helper to perform HTTP requests using urllib."""
        url = f"{self.base_url}{endpoint}"
        req = urllib.request.Request(url, method=method)
        if data is not None:
            req.add_header("Content-Type", "application/json")
            req.data = json.dumps(data).encode("utf-8")

        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                body = response.read().decode("utf-8")
                if body:
                    return json.loads(body)
                return {}
        except urllib.error.URLError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}

    def discover_models(self) -> List[Dict[str, Any]]:
        """Hits /v1/models to discover available models."""
        res = self._request("/v1/models")
        if "error" in res:
            return []
        return res.get("data", [])

    def health_check(self) -> bool:
        """Checks if the LM Studio local server is up and responsive."""
        res = self._request("/v1/models")
        return "error" not in res

    def estimate_resources(self, model_id: str) -> Dict[str, Any]:
        """Provides a basic estimation of RAM/VRAM resources based on model ID heuristics."""
        size_estimate_mb = 4096  # default 4GB
        lower_id = model_id.lower()

        if "7b" in lower_id:
            size_estimate_mb = 6000
        elif "13b" in lower_id:
            size_estimate_mb = 10000
        elif "70b" in lower_id:
            size_estimate_mb = 40000

        return {
            "model_id": model_id,
            "estimated_ram_mb": size_estimate_mb,
            "can_fit": True  # In a real scenario, this would compare with available system RAM
        }

    def load_model(self, model_id: str, context_length: int = 2048, ttl_seconds: Optional[int] = None) -> bool:
        """Loads a model with specified context length and tracks TTL."""
        res = self._request("/v1/models/load", method="POST", data={"model": model_id, "context_length": context_length})

        success = "error" not in res
        if success:
            ttl = ttl_seconds if ttl_seconds is not None else self.default_ttl
            self.loaded_models[model_id] = {
                "loaded_at": time.time(),
                "ttl": ttl,
                "context_length": context_length
            }

        return success

    def unload_model(self, model_id: str) -> bool:
        """Unloads a model to free resources."""
        res = self._request(f"/v1/models/{model_id}/unload", method="POST")
        success = "error" not in res
        if success and model_id in self.loaded_models:
            del self.loaded_models[model_id]
        return success

    def enforce_ttl_policy(self) -> List[str]:
        """Unloads models that have exceeded their Time-To-Live (TTL)."""
        now = time.time()
        unloaded_models = []

        # Use list() to avoid dictionary size changed during iteration
        for model_id, info in list(self.loaded_models.items()):
            if now - info["loaded_at"] > info["ttl"]:
                self.unload_model(model_id)
                unloaded_models.append(model_id)

        return unloaded_models
