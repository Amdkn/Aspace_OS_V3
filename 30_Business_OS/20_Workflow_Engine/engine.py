import json
import uuid
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional

class StateMachineError(Exception):
    pass

class EffectReceipt:
    def __init__(self, operation_id: str, correlation_id: str, causation_id: str,
                 capability_id: str, capability_version: str, source: str, target: str,
                 idempotency_key: str, requested_at: str, observed_at: str,
                 observed_effect: Dict[str, Any], evidence_refs: List[str],
                 retry_safe: bool, status: str, compensation_ref: Optional[str] = None):
        self.operation_id = operation_id
        self.correlation_id = correlation_id
        self.causation_id = causation_id
        self.capability_id = capability_id
        self.capability_version = capability_version
        self.source = source
        self.target = target
        self.idempotency_key = idempotency_key
        self.requested_at = requested_at
        self.observed_at = observed_at
        self.observed_effect = observed_effect
        self.evidence_refs = evidence_refs
        self.retry_safe = retry_safe
        self.status = status
        self.compensation_ref = compensation_ref

    def to_dict(self):
        return self.__dict__

class WorkflowEngine:
    def __init__(self):
        self.ledger = {} # idempotency_key -> Receipt
        self.active_journeys = {} # correlation_id -> state

    def start_journey(self, correlation_id: str, initial_state: str = "Lead"):
        if correlation_id in self.active_journeys:
            raise StateMachineError("Journey already exists")
        self.active_journeys[correlation_id] = initial_state

    def process_transition(self, correlation_id: str, trigger: str, source_states: List[str], target_state: str,
                           capability_id: str, idempotency_key: str,
                           execution_fn, retry_safe: bool = False) -> EffectReceipt:

        # Check idempotency first (duplicate webhook/retry)
        if idempotency_key in self.ledger:
            existing = self.ledger[idempotency_key]
            # Return existing receipt instead of double execution
            return existing

        # Check valid state
        current_state = self.active_journeys.get(correlation_id)
        if current_state not in source_states:
            raise StateMachineError(f"Invalid state for transition. Expected one of {source_states}, got {current_state}")

        requested_at = datetime.now(timezone.utc).isoformat()

        try:
            effect_data = execution_fn()
            status = "SUCCEEDED"
            self.active_journeys[correlation_id] = target_state
        except Exception as e:
            effect_data = {"error": str(e)}
            # If it's a simulated external failure, we might not know if it actually worked
            if getattr(e, 'is_unknown', False):
                status = "UNKNOWN"
                self.active_journeys[correlation_id] = "REQUIRES_HUMAN"
            else:
                status = "FAILED"
                # State remains unchanged on failure unless it's UNKNOWN

        observed_at = datetime.now(timezone.utc).isoformat()

        receipt = EffectReceipt(
            operation_id=str(uuid.uuid4()),
            correlation_id=correlation_id,
            causation_id=trigger,
            capability_id=capability_id,
            capability_version="1.0.0",
            source=current_state,
            target=target_state if status == "SUCCEEDED" else ("REQUIRES_HUMAN" if status == "UNKNOWN" else current_state),
            idempotency_key=idempotency_key,
            requested_at=requested_at,
            observed_at=observed_at,
            observed_effect=effect_data,
            evidence_refs=["local_log"],
            retry_safe=retry_safe,
            status=status
        )

        self.ledger[idempotency_key] = receipt
        return receipt
