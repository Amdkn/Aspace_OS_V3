from typing import Dict, Any, Optional
import uuid
import json
from .registry import CapabilityRegistry
from .quarantine import QuarantineRegistry

class AdapterBase:
    def __init__(self, registry: CapabilityRegistry, surface_name: str, quarantine_registry: Optional[QuarantineRegistry] = None):
        self.registry = registry
        self.surface_name = surface_name
        self.quarantine_registry = quarantine_registry

    def invoke(self, capability_id: str, payload: Dict[str, Any], correlation_id: Optional[str] = None) -> Dict[str, Any]:
        if self.quarantine_registry and self.quarantine_registry.is_quarantined(self.surface_name):
            return {
                "status": "FAILED",
                "error": f"Surface / protocol '{self.surface_name}' is QUARANTINED and cannot be executed."
            }

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

# --- Batch M1: Core Transport Adapters ---

class CLIAdapter(AdapterBase):
    def __init__(self, registry: CapabilityRegistry, quarantine_registry: Optional[QuarantineRegistry] = None):
        super().__init__(registry, "cli", quarantine_registry)

class APIAdapter(AdapterBase):
    def __init__(self, registry: CapabilityRegistry, quarantine_registry: Optional[QuarantineRegistry] = None):
        super().__init__(registry, "api", quarantine_registry)

class MCPAdapter(AdapterBase):
    def __init__(self, registry: CapabilityRegistry, quarantine_registry: Optional[QuarantineRegistry] = None):
        super().__init__(registry, "mcp", quarantine_registry)

class SkillAdapter(AdapterBase):
    def __init__(self, registry: CapabilityRegistry, quarantine_registry: Optional[QuarantineRegistry] = None):
        super().__init__(registry, "skill", quarantine_registry)

class InAppAdapter(AdapterBase):
    def __init__(self, registry: CapabilityRegistry, quarantine_registry: Optional[QuarantineRegistry] = None):
        super().__init__(registry, "in_app", quarantine_registry)

# --- Batch M3: Agent & Protocol Adapters ---

class AgentOSProjectionAdapter(AdapterBase):
    def __init__(self, registry: CapabilityRegistry, quarantine_registry: Optional[QuarantineRegistry] = None):
        super().__init__(registry, "agent_os_projection", quarantine_registry)

class A2AAdapter(AdapterBase):
    def __init__(self, registry: CapabilityRegistry, quarantine_registry: Optional[QuarantineRegistry] = None):
        super().__init__(registry, "a2a", quarantine_registry)

class A2UIAdapter(AdapterBase):
    def __init__(self, registry: CapabilityRegistry, quarantine_registry: Optional[QuarantineRegistry] = None):
        super().__init__(registry, "a2ui", quarantine_registry)

class ACPAdapter(AdapterBase):
    def __init__(self, registry: CapabilityRegistry, quarantine_registry: Optional[QuarantineRegistry] = None):
        super().__init__(registry, "acp", quarantine_registry)

class AGUIAdapter(AdapterBase):
    def __init__(self, registry: CapabilityRegistry, quarantine_registry: Optional[QuarantineRegistry] = None):
        super().__init__(registry, "ag_ui", quarantine_registry)

class WebMCPAdapter(AdapterBase):
    def __init__(self, registry: CapabilityRegistry, quarantine_registry: Optional[QuarantineRegistry] = None):
        super().__init__(registry, "webmcp", quarantine_registry)
