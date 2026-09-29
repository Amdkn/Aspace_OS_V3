from typing import Optional, Dict
from datetime import datetime, timezone
from .projection_gateway import OwnershipState

def derive_ownership_state(
    claim: Optional[Dict],
    lease: Optional[Dict],
    session_binding: Optional[Dict],
    current_time: Optional[datetime] = None
) -> OwnershipState:
    """
    Derives ownership state from uc.db evidence according to PRESENCE_STATE_MACHINE.json

    Inputs are expected to be dictionaries representing the rows from uc.db.
    """
    if current_time is None:
        current_time = datetime.now(timezone.utc)

    def is_fresh(entry: Optional[Dict], expiry_key: str = 'expires_at') -> bool:
        if not entry or expiry_key not in entry or not entry[expiry_key]:
            return False
        try:
            expiry = datetime.fromisoformat(entry[expiry_key])
            # Handle naive datetime from sqlite by assuming UTC if no tzinfo
            if expiry.tzinfo is None:
                expiry = expiry.replace(tzinfo=timezone.utc)
            return expiry > current_time
        except (ValueError, TypeError):
            return False

    has_fresh_claim = is_fresh(claim, 'expires_at')
    has_fresh_lease = is_fresh(lease, 'expires_at')
    has_active_binding = session_binding and session_binding.get('status') == 'active'

    if not claim and not lease and not session_binding:
        return OwnershipState.NONE

    # Check for contradictions first
    # Example: multiple active owners or contradictory lease/binding
    # For now, we define conflict as having a binding without a claim/lease
    # when one is expected, or if fields mismatch (e.g. work_id mismatch)
    if has_active_binding:
        binding_work_id = session_binding.get('work_id')
        claim_work_id = claim.get('work_id') if claim else None
        lease_work_id = lease.get('work_id') if lease else None

        # If binding exists but points to different work than claim/lease, it's a conflict
        if claim_work_id and binding_work_id != claim_work_id:
            return OwnershipState.CONFLICT
        if lease_work_id and binding_work_id != lease_work_id:
            return OwnershipState.CONFLICT

        # Fresh session binding + lease/claim are coherent
        if has_fresh_claim or has_fresh_lease:
            return OwnershipState.BOUND

    # Fresh lease exists
    if has_fresh_lease:
        return OwnershipState.LEASED

    # Fresh claim exists
    if has_fresh_claim:
        return OwnershipState.CLAIMED

    # Default fallback when db is missing or state is unclear
    return OwnershipState.UNKNOWN
