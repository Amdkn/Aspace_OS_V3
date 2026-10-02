from typing import Dict, Any, Optional
import uuid
import json
from .registry import CapabilityRegistry

class AdapterBase:
    def __init__(self, registry: CapabilityRegistry, surface_name: str):
        self.registry = registry
        self.surface_name = surface_name

    def invoke(self, capability_id: str, payload: Dict[str, Any], correlation_id: Optional[str] = None) -> Dict[str, Any]:
        capability = self.registry.get_capability(capability_id)
        if not capability:
            return {"status": "FAILED", "error": f"Capability {capability_id} not found."}

        if self.surface_name not in capability.supported_surfaces:
            return {"status": "FAILED", "error": f"Surface {self.surface_name} not supported by {capability_id}."}

        corr_id = correlation_id or str(uuid.uuid4())

        try:
            receipt = capability.executor(payload, corr_id)
            res = {
                "status": receipt.status,
                "receipt": {
                    "capability_id": receipt.capability_id,
                    "correlation_id": receipt.correlation_id,
                    "observed_effect": receipt.observed_effect,
                    "provenance": receipt.provenance,
                    "observed_at": receipt.observed_at,
                    "evidence_refs": receipt.evidence_refs
                }
            }
            if receipt.data:
                res["data"] = receipt.data
            return res
        except Exception as e:
            return {"status": "UNKNOWN", "error": str(e)}

class CLIAdapter(AdapterBase):
    def __init__(self, registry: CapabilityRegistry):
        super().__init__(registry, "cli")

class APIAdapter(AdapterBase):
    def __init__(self, registry: CapabilityRegistry):
        super().__init__(registry, "api")

class MCPAdapter(AdapterBase):
    def __init__(self, registry: CapabilityRegistry):
        super().__init__(registry, "mcp")
