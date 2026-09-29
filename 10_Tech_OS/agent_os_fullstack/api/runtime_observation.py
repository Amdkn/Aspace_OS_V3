import datetime
from .projection_gateway import RuntimeObservation, RuntimeState

def derive_runtime_state(observation: RuntimeObservation, current_time: datetime.datetime = None) -> RuntimeState:
    """
    Derives the runtime state based on PRESENCE_STATE_MACHINE.json invariants.
    """
    if observation is None:
        return RuntimeState.UNKNOWN

    if current_time is None:
        current_time = datetime.datetime.now(datetime.timezone.utc)

    try:
        observed_time = datetime.datetime.fromisoformat(observation.observed_at)
    except (ValueError, TypeError):
        return RuntimeState.UNKNOWN

    age_seconds = (current_time - observed_time).total_seconds()

    # Rule: Expired evidence cannot sustain LIVE -> STALE
    if age_seconds > observation.ttl_seconds:
        # If it was LIVE/STARTING/WAITING, it's STALE. If it was OFFLINE/FAILED/UNKNOWN, keep it.
        if observation.runtime_state in (RuntimeState.LIVE, RuntimeState.STARTING, RuntimeState.WAITING):
            return RuntimeState.STALE
        return observation.runtime_state

    # Fresh failure evidence
    if observation.failure_reason is not None and observation.failure_reason != "":
        # Note: Provider auth failure is FAILED(provider), not OFFLINE(machine) - we check failure_reason
        return RuntimeState.FAILED

    # Process/provider explicitly offline
    if observation.runtime_state == RuntimeState.OFFLINE:
        return RuntimeState.OFFLINE

    # Process/listener/provider evidence fresh and healthy
    if observation.runtime_state == RuntimeState.LIVE:
        return RuntimeState.LIVE

    if observation.runtime_state == RuntimeState.STARTING:
        return RuntimeState.STARTING

    if observation.runtime_state == RuntimeState.WAITING:
        return RuntimeState.WAITING

    return RuntimeState.UNKNOWN
