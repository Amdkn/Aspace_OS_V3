from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
import datetime

@dataclass
class QuarantinedAdapter:
    adapter_id: str
    protocol_name: str
    owner: str
    reason: str
    quarantined_at: str = field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc).isoformat())
    certified: bool = False

class QuarantineRegistry:
    """
    Acceptance requirement 7:
    Unsupported/experimental adapters are explicitly quarantined rather than silently promoted.
    """
    def __init__(self):
        self._quarantined: Dict[str, QuarantinedAdapter] = {}

    def quarantine(self, adapter_id: str, protocol_name: str, owner: str, reason: str) -> QuarantinedAdapter:
        entry = QuarantinedAdapter(
            adapter_id=adapter_id,
            protocol_name=protocol_name,
            owner=owner,
            reason=reason,
            certified=False
        )
        self._quarantined[adapter_id] = entry
        return entry

    def is_quarantined(self, adapter_id: str) -> bool:
        return adapter_id in self._quarantined and not self._quarantined[adapter_id].certified

    def list_quarantined(self) -> List[QuarantinedAdapter]:
        return list(self._quarantined.values())
