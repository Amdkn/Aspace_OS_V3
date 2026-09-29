from typing import List, Dict, Any, Optional
import uuid
from datetime import datetime, timezone

class SyncReceipt:
    def __init__(self, event_id: str, success: bool, reason: str = ""):
        self.event_id = event_id
        self.success = success
        self.reason = reason
        self.synced_at = datetime.now(timezone.utc).isoformat()

class SupabaseSyncAdapter:
    """
    Interface/mock for outbox synchronization from local uc.db to Supabase aspace.
    """
    def __init__(self, supabase_client=None):
        # In a real implementation, this would hold the service-role Supabase client
        self.client = supabase_client
        self.outbox: List[Dict[str, Any]] = []

    def queue_event(self, event_type: str, payload: Dict[str, Any], correlation_id: Optional[str] = None) -> str:
        """
        Queues a local change into the outbox for synchronization.
        """
        event_id = str(uuid.uuid4())
        self.outbox.append({
            "event_id": event_id,
            "event_type": event_type,
            "payload": payload,
            "correlation_id": correlation_id,
            "queued_at": datetime.now(timezone.utc).isoformat()
        })
        return event_id

    def flush_outbox(self) -> List[SyncReceipt]:
        """
        Attempts to synchronize all queued events to Supabase.
        Returns a receipt for each attempted event.
        """
        receipts = []
        # Mock flushing
        for event in list(self.outbox):
            # In real impl, would send to Supabase and check response
            # Ensuring idempotency by using event_id as key
            success = True
            reason = "MOCK_SUCCESS"

            receipt = SyncReceipt(event["event_id"], success, reason)
            receipts.append(receipt)

            if success:
                self.outbox.remove(event)

        return receipts
