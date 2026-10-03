from typing import Dict, List, Optional, Any
import datetime
from .capability import CapabilityContract

class CapabilityRegistry:
    def __init__(self):
        self._capabilities: Dict[str, CapabilityContract] = {}

    def register(self, capability: CapabilityContract) -> None:
        self._capabilities[capability.capability_id] = capability

    def get_capability(self, capability_id: str) -> Optional[CapabilityContract]:
        return self._capabilities.get(capability_id)

    def list_capabilities(self, surface_filter: Optional[str] = None, domain_filter: Optional[str] = None) -> List[CapabilityContract]:
        caps = list(self._capabilities.values())
        if surface_filter:
            caps = [cap for cap in caps if surface_filter in cap.supported_surfaces]
        if domain_filter:
            caps = [cap for cap in caps if cap.domain_owner == domain_filter]
        return caps

    def search_capabilities(self, query: str) -> List[CapabilityContract]:
        q = query.lower()
        return [
            cap for cap in self._capabilities.values()
            if q in cap.capability_id.lower() or q in cap.intent.lower() or q in cap.domain_owner.lower()
        ]

    def enumerate_capability_bindings(self, capability_id: str, adapter_name: str, runtime_binding: str) -> Dict[str, Any]:
        """
        Acceptance requirement 5:
        Agent OS enumerates capability, surface, adapter, runtime binding, observed_at and evidence source separately.
        """
        cap = self.get_capability(capability_id)
        if not cap:
            return {"status": "NOT_FOUND", "error": f"Capability {capability_id} not registered."}

        return {
            "capability_id": cap.capability_id,
            "version": cap.version,
            "domain_owner": cap.domain_owner,
            "intent": cap.intent,
            "supported_surfaces": cap.supported_surfaces,
            "adapter": adapter_name,
            "runtime_binding": runtime_binding,
            "observed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "evidence_source": f"Agent OS Capability Fabric / Registry ({cap.domain_owner})"
        }
