import json
import urllib.request
import urllib.error
import re
from typing import Dict, List, Optional, Any
from datetime import datetime, timezone

class LMStudioRegistry:
    """
    Local Serving Registry for GGUF backends via LM Studio.
    """
    def __init__(self, base_url: str = "http://127.0.0.1:1234"):
        self.base_url = base_url.rstrip("/")
        # Local state to track loaded models and their TTLs
        self.loaded_models: Dict[str, Dict[str, Any]] = {}

    def discover_models(self) -> List[Dict[str, Any]]:
        """
        Discover models via LM Studio /v1/models endpoint.
        """
        url = f"{self.base_url}/v1/models"
        req = urllib.request.Request(url, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode('utf-8'))
                    return data.get("data", [])
                return []
        except (urllib.error.URLError, json.JSONDecodeError):
            return []

    def check_health(self) -> Dict[str, Any]:
        """
        Check health of the LM Studio server.
        """
        url = f"{self.base_url}/v1/models"
        req = urllib.request.Request(url, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=5) as response:
                status = response.status
                return {
                    "status": "healthy" if status == 200 else "unhealthy",
                    "code": status
                }
        except urllib.error.URLError as e:
            return {
                "status": "unreachable",
                "error": str(e)
            }

    def estimate_resources(self, model_id: str) -> Dict[str, Any]:
        """
        Estimate resources needed for the model based on its ID (heuristics).
        """
        models = self.discover_models()
        # Find if it exists
        model_info = next((m for m in models if m.get("id") == model_id), None)

        # Base assumptions
        params_b = 7.0
        bpw = 4.0  # default 4 bits per weight for Q4

        # Extract params from ID (e.g. 7b, 8b, 14b, 8x7b)
        # Check MOE first!
        m_moe = re.search(r'(\d+)x(\d+)b', model_id.lower())
        m_params = re.search(r'(\d+(?:\.\d+)?)b', model_id.lower())

        if m_moe:
            params_b = float(m_moe.group(1)) * float(m_moe.group(2)) * 0.5 # rough MOE active params estimate
        elif m_params:
            params_b = float(m_params.group(1))

        # Extract quant from ID (e.g. q4, q8, fp16)
        match_quant = re.search(r'q(\d+)', model_id.lower())
        if match_quant:
            bpw = float(match_quant.group(1))
        elif 'fp16' in model_id.lower():
            bpw = 16.0
        elif 'fp32' in model_id.lower():
            bpw = 32.0

        # Model size in GB
        model_size_gb = (params_b * 1e9 * bpw) / (8 * 1024**3)

        # KV cache and context overhead (rough estimate: 1.5GB)
        context_gb = 1.5
        estimated_vram = model_size_gb + context_gb

        return {
            "estimated_vram_gb": round(estimated_vram, 2),
            "estimated_ram_gb": round(estimated_vram * 1.5, 2), # System RAM buffer
            "supported": True,
            "found_in_registry": model_info is not None
        }

    def load_model(self, model_id: str, ttl_seconds: int = 3600) -> bool:
        """
        Mark a model as loaded locally. LM Studio loads it implicitly on inference,
        so we track it for TTL purposes here.
        """
        now = datetime.now(timezone.utc)
        self.loaded_models[model_id] = {
            "loaded_at": now,
            "ttl_seconds": ttl_seconds,
            "last_accessed": now
        }
        return True

    def unload_model(self, model_id: str) -> bool:
        """
        Unload a model via LM Studio API and remove from local tracking.
        LM Studio implements /v1/models/unload or we can unload specific models.
        """
        unloaded_from_server = False

        url = f"{self.base_url}/v1/models/unload"
        data = json.dumps({"id": model_id}).encode('utf-8')
        req = urllib.request.Request(url, data=data, method="POST")
        req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    unloaded_from_server = True
        except urllib.error.URLError:
            pass

        if not unloaded_from_server:
            # Fallback
            url = f"{self.base_url}/v1/models/{model_id}/unload"
            req = urllib.request.Request(url, method="POST")
            try:
                with urllib.request.urlopen(req, timeout=5) as response:
                    if response.status == 200:
                        unloaded_from_server = True
            except urllib.error.URLError:
                pass

        # Update local tracking regardless
        if model_id in self.loaded_models:
             del self.loaded_models[model_id]
             return True

        return unloaded_from_server

    def touch_model(self, model_id: str) -> None:
         """Update the last accessed time of a model."""
         if model_id in self.loaded_models:
             self.loaded_models[model_id]["last_accessed"] = datetime.now(timezone.utc)

    def enforce_ttl_policy(self) -> List[str]:
        """
        Enforce TTL policy, unloading models that have expired.
        """
        now = datetime.now(timezone.utc)
        expired_models = []

        for model_id, state in list(self.loaded_models.items()):
            elapsed = (now - state["last_accessed"]).total_seconds()
            if elapsed > state["ttl_seconds"]:
                expired_models.append(model_id)
                self.unload_model(model_id)

        return expired_models
