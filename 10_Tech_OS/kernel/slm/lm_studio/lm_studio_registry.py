import urllib.request
import urllib.error
import json
import re
import datetime
from typing import Dict, Any, List, Optional

class LMStudioRegistry:
    def __init__(self, base_url: str = "http://127.0.0.1:1234", ttl_seconds: int = 3600, max_ram_gb: float = 16.0):
        self.base_url = base_url.rstrip('/')
        self.ttl_seconds = ttl_seconds
        self.max_ram_gb = max_ram_gb
        self.loaded_models: Dict[str, Dict[str, Any]] = {}

    def discover_models(self) -> List[Dict[str, Any]]:
        req = urllib.request.Request(f"{self.base_url}/v1/models")
        try:
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode('utf-8'))
                return data.get("data", [])
        except urllib.error.URLError as e:
            raise RuntimeError(f"Discovery failed: {e}")

    def estimate_resources(self, model_id: str) -> Dict[str, Any]:
        """Estimates model resource requirements by parsing parameter counts and quantization levels."""
        params_b = 7.0
        quant = 4

        param_match = re.search(r'(\d+(?:\.\d+)?)[Bb]', model_id)
        if param_match:
            params_b = float(param_match.group(1))

        quant_match = re.search(r'[Qq](\d+)', model_id)
        if quant_match:
            quant = int(quant_match.group(1))

        estimated_ram_gb = (params_b * quant / 8) + 1.5

        return {
            "parameters_b": params_b,
            "quantization_bits": quant,
            "estimated_ram_gb": estimated_ram_gb
        }

    def can_load_model(self, model_id: str) -> bool:
        """Resource policy: check if loading this model would exceed max RAM."""
        # Calculate current RAM usage
        current_ram_gb = sum(
            self.estimate_resources(m)["estimated_ram_gb"]
            for m in self.loaded_models
        )

        # Calculate estimated RAM for new model
        new_model_ram_gb = self.estimate_resources(model_id)["estimated_ram_gb"]

        return (current_ram_gb + new_model_ram_gb) <= self.max_ram_gb

    def load_model(self, model_id: str) -> bool:
        """Loads a model explicitly and enforces resource policy."""
        if not self.can_load_model(model_id):
            return False

        now = datetime.datetime.now(datetime.timezone.utc)
        self.loaded_models[model_id] = {"loaded_at": now, "last_used": now}

        # Optionally, we could pre-load via API if needed,
        # but tracking it allows us to enforce policy on inference requests.
        return True

    def track_inference(self, model_id: str) -> None:
        """Called implicitly when inference is requested to track model state."""
        now = datetime.datetime.now(datetime.timezone.utc)
        if model_id not in self.loaded_models:
            # Enforce resource policy before implicitly loading
            if self.can_load_model(model_id):
                self.loaded_models[model_id] = {"loaded_at": now, "last_used": now}
        else:
            self.loaded_models[model_id]["last_used"] = now

    def unload_model(self, model_id: str) -> None:
        """Unloads model via POST request to LM Studio."""
        unload_endpoints = [
            f"{self.base_url}/v1/models/{model_id}/unload",
            f"{self.base_url}/v1/internal/model/unload"
        ]

        for endpoint in unload_endpoints:
            req = urllib.request.Request(endpoint, method='POST', data=b"{}")
            req.add_header('Content-Type', 'application/json')
            try:
                with urllib.request.urlopen(req) as response:
                    pass
            except urllib.error.URLError:
                pass

        if model_id in self.loaded_models:
            del self.loaded_models[model_id]

    def enforce_ttl(self) -> None:
        """Enforces TTL policy by unloading models that haven't been used recently."""
        now = datetime.datetime.now(datetime.timezone.utc)
        to_unload = []
        for model_id, state in self.loaded_models.items():
            if (now - state["last_used"]).total_seconds() > self.ttl_seconds:
                to_unload.append(model_id)

        for model_id in to_unload:
            self.unload_model(model_id)

    def health_check(self) -> Dict[str, Any]:
        """Returns health evidence for GGUF backends."""
        try:
            models = self.discover_models()
            return {
                "status": "healthy",
                "evidence": f"Discovered {len(models)} models",
                "loaded_tracked": len(self.loaded_models)
            }
        except Exception as e:
            return {
                "status": "unhealthy",
                "error": str(e)
            }
