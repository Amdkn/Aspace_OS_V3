import json
import urllib.request
import urllib.error
import urllib.parse
from typing import Dict, Any, List, Optional
import time
import logging

logger = logging.getLogger(__name__)

class LMStudioRegistry:
    def __init__(self, base_url: str = "http://localhost:1234"):
        self.base_url = base_url.rstrip("/")
        # format: {model_id: {"loaded_at": timestamp, "ttl": seconds_or_None}}
        self.loaded_models: Dict[str, Dict[str, Any]] = {}

    def health(self) -> Dict[str, Any]:
        """
        Check health of LM studio API by querying /v1/models endpoint.
        Returns health evidence dict.
        """
        try:
            req = urllib.request.Request(f"{self.base_url}/v1/models", method="GET")
            with urllib.request.urlopen(req, timeout=5) as response:
                data = json.loads(response.read().decode("utf-8"))
                return {"status": "ok", "evidence": "API responding", "models_count": len(data.get("data", []))}
        except urllib.error.HTTPError as e:
            return {"status": "error", "evidence": f"HTTP {e.code}"}
        except Exception as e:
            return {"status": "error", "evidence": str(e)}

    def discover_models(self) -> List[Dict[str, Any]]:
        """
        Discover available models via /v1/models.
        """
        try:
            req = urllib.request.Request(f"{self.base_url}/v1/models", method="GET")
            with urllib.request.urlopen(req, timeout=5) as response:
                data = json.loads(response.read().decode("utf-8"))
                return data.get("data", [])
        except urllib.error.HTTPError as e:
            logger.error(f"Failed to discover models: HTTP {e.code}")
            return []
        except Exception as e:
            logger.error(f"Failed to discover models: {e}")
            return []

    def estimate_resources(self, model_id: str) -> Dict[str, Any]:
        """
        Estimate resources for a given model (mock implementation for GGUF).
        """
        # In reality, this might query an endpoint or parse GGUF metadata.
        # For now, providing a mock estimation logic.
        return {
            "model_id": model_id,
            "estimated_ram_mb": 4096, # mock value
            "estimated_vram_mb": 0,
        }

    def load_model(self, model_id: str, ttl: Optional[int] = None, config: Optional[Dict[str, Any]] = None) -> bool:
        """
        Load a model. Simulates load by posting to some endpoint or just tracking internally.
        LM Studio automatically loads models upon inference, but typically doesn't have an explicit load endpoint.
        However, newer versions might support model loading/unloading endpoints.
        We'll track it internally.
        """
        # Actually LM Studio API doesn't have a standard /v1/load endpoint,
        # but we simulate or track it as per PRD for resource management.

        # Let's say we just track it.
        try:
            # We assume it succeeds.
            self.loaded_models[model_id] = {
                "loaded_at": time.time(),
                "ttl": ttl,
                "config": config or {}
            }
            return True
        except Exception as e:
            logger.error(f"Failed to load model {model_id}: {e}")
            return False

    def unload_model(self, model_id: str) -> bool:
        """
        Unload a model.
        In LM Studio API, usually there's no explicit unload endpoint in standard OpenAI API,
        but for local registry lifecycle, we remove it from tracking.
        If LM Studio provides a custom endpoint like DELETE /v1/models/{model_id} we would call it.
        """
        try:
            # Try calling a custom endpoint if it exists
            # We'll just track it internally for now.
            if model_id in self.loaded_models:
                del self.loaded_models[model_id]
                return True
            return False
        except Exception as e:
            logger.error(f"Failed to unload model {model_id}: {e}")
            return False

    def enforce_ttl(self) -> List[str]:
        """
        Check TTLs and unload expired models.
        Returns list of unloaded model_ids.
        """
        now = time.time()
        expired = []
        for model_id, data in list(self.loaded_models.items()):
            ttl = data.get("ttl")
            loaded_at = data.get("loaded_at", now)
            if ttl is not None and (now - loaded_at) > ttl:
                expired.append(model_id)

        for model_id in expired:
            self.unload_model(model_id)

        return expired
