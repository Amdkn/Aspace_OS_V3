import json
from pathlib import Path
from typing import Dict, Any

def load_policy(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def can_allocate(policy: Dict[str, Any], active_counts: Dict[str, int], requested_core: str) -> bool:
    """
    Determines if a new session can be allocated for the requested_core
    based on the current active_counts and the policy constraints.
    """
    max_active = policy.get("max_active", 9)
    core_limits = policy.get("core_limits", {})
    core_reservations = policy.get("core_reservations", {})

    current_total = sum(active_counts.values())

    # 1. Bounded concurrency (global limit)
    if current_total >= max_active:
        return False

    # 2. Budget limits per core
    core_active = active_counts.get(requested_core, 0)
    core_limit = core_limits.get(requested_core, 0)
    if core_active >= core_limit:
        return False

    # 3. Domain reservations to prevent silent capacity theft
    unmet_reservations = 0
    for core, reservation in core_reservations.items():
        if core != requested_core:
            current_active = active_counts.get(core, 0)
            if current_active < reservation:
                unmet_reservations += (reservation - current_active)

    if (max_active - current_total - 1) < unmet_reservations:
        return False

    return True
