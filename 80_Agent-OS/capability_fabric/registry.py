from typing import Dict, List, Optional
from .contract import CapabilityContract

class CapabilityRegistry:
    def __init__(self):
        self._capabilities: Dict[str, CapabilityContract] = {}

    def register(self, contract: CapabilityContract):
        if contract.capability_id in self._capabilities:
            raise ValueError(f"Capability {contract.capability_id} is already registered.")
        self._capabilities[contract.capability_id] = contract

    def get(self, capability_id: str) -> Optional[CapabilityContract]:
        return self._capabilities.get(capability_id)

    def list_capabilities(self) -> List[CapabilityContract]:
        return list(self._capabilities.values())

    def enumerate_surfaces(self) -> Dict[str, List[str]]:
        surfaces = {}
        for cap in self.list_capabilities():
            for surface in cap.supported_surfaces:
                if surface not in surfaces:
                    surfaces[surface] = []
                surfaces[surface].append(cap.capability_id)
        return surfaces
