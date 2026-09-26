import json
from pathlib import Path
from typing import Dict, Optional

class CapacityPolicy:
    """
    Capacity policy enforcing bounded concurrency, domain reservations,
    and preventing silent capacity theft.
    """
    def __init__(self, data: dict):
        self.max_active = data.get("max_active", 10)
        self.max_dispatch_per_tick = data.get("max_dispatch_per_tick", 3)
        self.reservations: Dict[str, int] = data.get("reservations", {
            "KERNEL": 2, "LIFE": 3, "BUSINESS": 5
        })
        self.cost_ceiling_usd = data.get("cost_ceiling_usd", 100.0)

    @classmethod
    def load(cls, path: str | Path) -> 'CapacityPolicy':
        p = Path(path)
        if not p.exists():
            return cls({})
        with open(p, "r", encoding="utf-8") as f:
            return cls(json.load(f))

    def remaining_capacity(self, active_count: int) -> int:
        """Returns global capacity remaining before ceiling."""
        return max(0, self.max_active - active_count)

    def can_dispatch(self, core: str, current_counts: Dict[str, int], active_count: int) -> bool:
        """
        Evaluate if a new work item for `core` can be dispatched.
        Prevents silent capacity theft by ensuring we do not consume
        capacity that is reserved for other domains.
        """
        if active_count >= self.max_active:
            return False

        # Calculate unmet reservations for all OTHER cores
        unmet_others = 0
        for c, res in self.reservations.items():
            if c != core:
                unmet_others += max(0, res - current_counts.get(c, 0))

        # Check if taking 1 unit of capacity would leave enough room
        # for all unmet reservations of other domains.
        remaining = self.max_active - active_count
        if remaining - 1 < unmet_others:
            return False

        return True

    def overload_signal(self, active_count: int) -> bool:
        """Backpressure signal when we are at or above global concurrency bound."""
        return active_count >= self.max_active
