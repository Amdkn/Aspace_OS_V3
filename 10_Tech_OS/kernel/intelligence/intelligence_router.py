import enum
from typing import Dict, Any, Optional
from .needle_adapter import Needle3Adapter

class CapabilityPattern(enum.Enum):
    EXTRACT = "EXTRACT"
    ACT = "ACT"
    EMBED = "EMBED"
    DECIDE = "DECIDE"

class IntelligenceRouter:
    """Native local capability interface."""

    def __init__(self, needle_adapter=None):
        self.needle_adapter = needle_adapter or Needle3Adapter()
        self.patterns = [
            CapabilityPattern.EXTRACT,
            CapabilityPattern.ACT,
            CapabilityPattern.EMBED
        ]

    def add_capability(self, pattern: CapabilityPattern):
        if pattern not in self.patterns:
            self.patterns.append(pattern)

    def remove_capability(self, pattern: CapabilityPattern):
        if pattern in self.patterns:
            self.patterns.remove(pattern)

    def has_capability(self, pattern: CapabilityPattern) -> bool:
        return pattern in self.patterns

    def execute(self, pattern: CapabilityPattern, payload: Dict[str, Any], evidence: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute a pattern using the adapter."""
        if pattern == CapabilityPattern.DECIDE:
            if not evidence:
                raise PermissionError("DECIDE capability requires evidence to justify it. Fail-closed boundary preserved.")
            else:
                return self.needle_adapter.execute(pattern.value, {"payload": payload, "evidence": evidence})

        if not self.has_capability(pattern):
            raise NotImplementedError(f"Pattern {pattern} is not supported.")

        return self.needle_adapter.execute(pattern.value, payload)
