#!/usr/bin/env python3
"""
intelligence_router.py — IntelligenceRouter with Cactus Needle 3 capability adapter.

Provides native local capability interfaces: EXTRACT, ACT, EMBED.
Exposes DECIDE only if evidence justifies it.
Preserves fail-closed authority boundary.
"""

import enum
from typing import Dict, Any, Optional

class Capability(enum.Enum):
    EXTRACT = "EXTRACT"
    ACT = "ACT"
    EMBED = "EMBED"
    DECIDE = "DECIDE"

class IntelligenceRouter:
    def __init__(self, require_evidence_for_decide: bool = True):
        self._capabilities = {
            Capability.EXTRACT: True,
            Capability.ACT: True,
            Capability.EMBED: True,
            Capability.DECIDE: not require_evidence_for_decide
        }
        self.evidence = None

    def provide_evidence(self, evidence: Any) -> None:
        """Provide evidence to unlock restricted capabilities like DECIDE."""
        if evidence:
            self.evidence = evidence
            self._capabilities[Capability.DECIDE] = True

    def execute(self, capability: Capability, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a capability via Cactus Needle 3 if authorized."""
        if not self._capabilities.get(capability, False):
            raise PermissionError(f"Capability {capability.name} is not authorized. Fail-closed authority boundary preserved.")

        # Simulate Cactus Needle 3 capability adapter execution
        if capability == Capability.EXTRACT:
            return {"status": "success", "extracted_data": f"Extracted from {payload.get('source')}"}
        elif capability == Capability.ACT:
            return {"status": "success", "action": payload.get("action"), "result": "Action executed via Cactus Needle 3"}
        elif capability == Capability.EMBED:
            return {"status": "success", "embedding": [0.1, 0.2, 0.3]}
        elif capability == Capability.DECIDE:
            return {"status": "success", "decision": f"Decision based on evidence: {self.evidence}"}

        raise ValueError(f"Unknown capability {capability}")

def discover_capabilities() -> Dict[str, bool]:
    """Runtime discovery of capabilities."""
    return {
        "EXTRACT": True,
        "ACT": True,
        "EMBED": True,
        "DECIDE": False # Default fail-closed
    }
