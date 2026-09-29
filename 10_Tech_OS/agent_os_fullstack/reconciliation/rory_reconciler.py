from datetime import datetime, timezone
import uuid
from ..api.projection_gateway import ReconciliationReceipt, ReconciliationClassification, ReconciliationDecision, RuntimePresenceProjection, OwnershipState, SourceFingerprint

def classify_divergence(
    local_state: dict,
    cloud_projection: dict,
    source_state: SourceFingerprint,
    entity_id: str,
    entity_type: str = "work"
) -> ReconciliationReceipt:
    """
    Classifies contradictions between local WorkGraph execution truth and cloud projections,
    outputting a ReconciliationReceipt.
    """
    receipt = ReconciliationReceipt(
        receipt_id=str(uuid.uuid4()),
        entity_type=entity_type,
        entity_id=entity_id,
        created_at=datetime.now(timezone.utc).isoformat()
    )

    # Source drift
    if source_state and source_state.parent_dirty:
        receipt.classification = ReconciliationClassification.SOURCE_DRIFT
        receipt.decision = ReconciliationDecision.HOLD
        return receipt
    if source_state and any(nested.dirty or nested.observed_head != nested.committed_gitlink for nested in source_state.nested if nested.committed_gitlink):
         receipt.classification = ReconciliationClassification.SOURCE_DRIFT
         receipt.decision = ReconciliationDecision.HOLD
         return receipt

    if not local_state and not cloud_projection:
        receipt.classification = ReconciliationClassification.CONSISTENT
        receipt.decision = ReconciliationDecision.NOOP
        return receipt

    local_updated = local_state.get('updated_at') if local_state else None
    cloud_updated = cloud_projection.get('updated_at') if cloud_projection else None


    if local_state and not cloud_projection:
        receipt.classification = ReconciliationClassification.LOCAL_NEWER
        receipt.decision = ReconciliationDecision.RETRY_SYNC
        return receipt

    if cloud_projection and not local_state:
        # Cloud has data, local does not
        receipt.classification = ReconciliationClassification.CLOUD_NEWER_BUT_NONAUTHORITATIVE
        receipt.decision = ReconciliationDecision.ROUTE_DONNA
        return receipt

    # Convert to timestamps for comparison
    try:
        if local_updated:
            lt = datetime.fromisoformat(local_updated)
            if lt.tzinfo is None: lt = lt.replace(tzinfo=timezone.utc)
        else:
            lt = datetime.min.replace(tzinfo=timezone.utc)

        if cloud_updated:
            ct = datetime.fromisoformat(cloud_updated)
            if ct.tzinfo is None: ct = ct.replace(tzinfo=timezone.utc)
        else:
            ct = datetime.min.replace(tzinfo=timezone.utc)
    except (ValueError, TypeError):
        receipt.classification = ReconciliationClassification.UNKNOWN
        receipt.decision = ReconciliationDecision.ROUTE_DONNA
        return receipt

    if lt > ct:
        receipt.classification = ReconciliationClassification.LOCAL_NEWER
        receipt.decision = ReconciliationDecision.RETRY_SYNC
    elif ct > lt:
        # Cloud newer but non authoritative (e.g. stale row overriding local)
        receipt.classification = ReconciliationClassification.CLOUD_NEWER_BUT_NONAUTHORITATIVE
        receipt.decision = ReconciliationDecision.REFRESH_PROJECTION
    else:
        receipt.classification = ReconciliationClassification.CONSISTENT
        receipt.decision = ReconciliationDecision.NOOP

    # Ownership conflict logic
    local_status = local_state.get('status')
    cloud_status = cloud_projection.get('status')

    # If cloud thinks it's active but local knows it's closed/failed
    if cloud_status in ('active', 'claimed') and local_status not in ('active', 'claimed', 'pending'):
        receipt.classification = ReconciliationClassification.STALE_BINDING
        receipt.decision = ReconciliationDecision.ACCEPT_LOCAL

    return receipt
