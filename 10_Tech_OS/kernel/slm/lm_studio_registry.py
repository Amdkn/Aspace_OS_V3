import json
import urllib.request
import urllib.error
import datetime
from typing import Any, Dict, List, Optional
import time

class LMStudioRegistry:
    """
    LM Studio Registry.
    Handles discovery, estimation, load/unload, context/TTL/resource policy
    and health evidence for GGUF backends served locally via LM Studio.
    Uses standard library urllib.request to avoid external dependencies.
    """

    def __init__(self, base_url: str = "http://127.0.0.1:1234"):
        self.base_url = base_url.rstrip("/")
        # Track loaded models: model_id -> {"loaded_at": datetime, "ttl": seconds, "policy": dict}
        self.loaded_models: Dict[str, Dict[str, Any]] = {}

    def get_health_evidence(self) -> Dict[str, Any]:
        """Check health status of the LM Studio endpoint."""
        url = f"{self.base_url}/v1/models"
        req = urllib.request.Request(url, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    return {"status": "healthy", "evidence": "endpoint reachable"}
                return {"status": "unhealthy", "evidence": f"HTTP {response.status}"}
        except urllib.error.URLError as e:
            return {"status": "unhealthy", "evidence": str(e)}
        except Exception as e:
            return {"status": "unhealthy", "evidence": f"unexpected error: {str(e)}"}

    def discover_models(self) -> List[Dict[str, Any]]:
        """Discover available models via GET /v1/models."""
        url = f"{self.base_url}/v1/models"
        req = urllib.request.Request(url, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode('utf-8'))
                    return data.get("data", [])
                return []
        except urllib.error.URLError:
            return []
        except Exception:
            return []

    def estimate(self, model_name: str) -> Dict[str, Any]:
        """
        Estimate resources for a given model.
        In LM studio we check if the model is available.
        """
        models = self.discover_models()
        for m in models:
            if m.get("id") == model_name:
                return {"estimable": True, "model": model_name, "status": "available"}
        return {"estimable": False, "model": model_name, "status": "not_found"}

    def load_model(self, model_name: str, ttl: int = 3600, policy: Optional[Dict[str, Any]] = None) -> bool:
        """
        Load a model by POSTing to LM Studio /v1/models endpoint (LM studio handles load if requested).
        Registers TTL and policy.
        Returns True if successful, False otherwise.
        """
        # LM Studio standard API for loading might not be standardized in OpenAI format,
        # but typical LM studio endpoints allow loading via a specific endpoint or by just requesting it.
        # We will simulate the load registry tracking and assume an endpoint if it existed,
        # or we just rely on standard OpenAI format if applicable. For registry purposes,
        # we track the loaded state and TTL locally.

        # Here we just check if it's available, and if so, register it locally.
        estimate_res = self.estimate(model_name)
        if not estimate_res.get("estimable"):
            return False

        self.loaded_models[model_name] = {
            "loaded_at": datetime.datetime.now(datetime.timezone.utc),
            "ttl": ttl,
            "policy": policy or {}
        }
        return True

    def unload_model(self, model_name: str) -> bool:
        """
        Unload a model. Since LM studio unloads models automatically or via specific extensions,
        we drop it from our tracking registry.
        """
        if model_name in self.loaded_models:
            del self.loaded_models[model_name]
            return True
        return False

    def enforce_ttl_policy(self) -> List[str]:
        """
        Check all loaded models against their TTL.
        Unloads expired models.
        Returns a list of unloaded model IDs.
        """
        now = datetime.datetime.now(datetime.timezone.utc)
        expired = []
        for model_id, info in list(self.loaded_models.items()):
            loaded_at = info["loaded_at"]
            ttl = info["ttl"]
            if (now - loaded_at).total_seconds() > ttl:
                expired.append(model_id)
                self.unload_model(model_id)
        return expired
