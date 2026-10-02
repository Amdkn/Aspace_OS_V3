from typing import Dict, List
from .capability import CapabilityContract

class CapabilityRegistry:
    def __init__(self):
        self._capabilities: Dict[str, CapabilityContract] = {}

    def register(self, capability: CapabilityContract) -> None:
        self._capabilities[capability.capability_id] = capability

    def get_capability(self, capability_id: str) -> CapabilityContract:
        return self._capabilities.get(capability_id)

    def list_capabilities(self, surface_filter: str = None) -> List[CapabilityContract]:
        if surface_filter:
            return [cap for cap in self._capabilities.values() if surface_filter in cap.supported_surfaces]
        return list(self._capabilities.values())
