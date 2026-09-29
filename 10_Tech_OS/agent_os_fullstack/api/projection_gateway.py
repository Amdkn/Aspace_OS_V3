from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum

class RuntimeState(str, Enum):
    UNKNOWN = "UNKNOWN"
    OFFLINE = "OFFLINE"
    STARTING = "STARTING"
    LIVE = "LIVE"
    WAITING = "WAITING"
    STALE = "STALE"
    FAILED = "FAILED"

class OwnershipState(str, Enum):
    NONE = "NONE"
    CLAIMED = "CLAIMED"
    LEASED = "LEASED"
    BOUND = "BOUND"
    CONFLICT = "CONFLICT"
    UNKNOWN = "UNKNOWN"

class SyncState(str, Enum):
    SYNCED = "SYNCED"
    LOCAL_AHEAD = "LOCAL_AHEAD"
    CLOUD_AHEAD = "CLOUD_AHEAD"
    DEGRADED = "DEGRADED"
    CONFLICT = "CONFLICT"
    UNKNOWN = "UNKNOWN"

class SourceState(str, Enum):
    CURRENT = "CURRENT"
    SOURCE_STALE = "SOURCE_STALE"
    DIRTY = "DIRTY"
    UNKNOWN = "UNKNOWN"

class ReconciliationClassification(str, Enum):
    LOCAL_NEWER = "LOCAL_NEWER"
    CLOUD_NEWER_BUT_NONAUTHORITATIVE = "CLOUD_NEWER_BUT_NONAUTHORITATIVE"
    OWNERSHIP_CONFLICT = "OWNERSHIP_CONFLICT"
    STALE_BINDING = "STALE_BINDING"
    SOURCE_DRIFT = "SOURCE_DRIFT"
    MISSING_RUNTIME_EVIDENCE = "MISSING_RUNTIME_EVIDENCE"
    DUPLICATE_EVENT = "DUPLICATE_EVENT"
    UNKNOWN = "UNKNOWN"
    CONSISTENT = "CONSISTENT"

class ReconciliationDecision(str, Enum):
    ACCEPT_LOCAL = "ACCEPT_LOCAL"
    ACCEPT_CLOUD_PROJECTION = "ACCEPT_CLOUD_PROJECTION"
    REFRESH_PROJECTION = "REFRESH_PROJECTION"
    RETRY_SYNC = "RETRY_SYNC"
    HOLD = "HOLD"
    ROUTE_DONNA = "ROUTE_DONNA"
    REOPEN_BUILD = "REOPEN_BUILD"
    REOPEN_DESIGN = "REOPEN_DESIGN"
    NOOP = "NOOP"

@dataclass
class Provenance:
    source_plane: str
    observed_at: str
    evidence_refs: List[str] = field(default_factory=list)
    expires_at: Optional[str] = None
    ttl_seconds: Optional[int] = None
    reason: Optional[str] = None

@dataclass
class RuntimeObservation:
    schema: str = "aspace.runtime-observation.v1"
    observation_id: str = ""
    identity: str = ""
    entity_kind: str = ""
    runtime_state: RuntimeState = RuntimeState.UNKNOWN
    observed_at: str = ""
    ttl_seconds: int = 60
    evidence_refs: List[str] = field(default_factory=list)
    provider: Optional[str] = None
    harness: Optional[str] = None
    process_ref: Optional[str] = None
    listener: Optional[str] = None
    session_ref: Optional[str] = None
    heartbeat_at: Optional[str] = None
    failure_reason: Optional[str] = None

@dataclass
class RuntimePresenceProjection:
    schema: str = "aspace.runtime-presence-projection.v1"
    identity: str = ""
    entity_kind: str = ""
    runtime_state: RuntimeState = RuntimeState.UNKNOWN
    ownership_state: OwnershipState = OwnershipState.NONE
    sync_state: SyncState = SyncState.UNKNOWN
    source_state: SourceState = SourceState.UNKNOWN
    provenance: List[Provenance] = field(default_factory=list)
    declared_capabilities: List[str] = field(default_factory=list)
    runtime_reason: Optional[str] = None
    work_id: Optional[str] = None
    claim_id: Optional[str] = None
    lease_id: Optional[str] = None
    session_binding_id: Optional[str] = None
    provider: Optional[str] = None
    harness: Optional[str] = None
    execution_id: Optional[str] = None

@dataclass
class NestedSourceFingerprint:
    path: str
    observed_head: str
    dirty: bool
    repo: Optional[str] = None
    branch: Optional[str] = None
    committed_gitlink: Optional[str] = None
    worktree: Optional[str] = None
    active_pr: Optional[str] = None

@dataclass
class SourceFingerprint:
    schema: str = "aspace.source-fingerprint.v1"
    world_id: str = ""
    parent_repo: str = ""
    parent_head: str = ""
    parent_dirty: bool = False
    observed_at: str = ""
    nested: List[NestedSourceFingerprint] = field(default_factory=list)
    parent_branch: Optional[str] = None

@dataclass
class ReconciliationReceipt:
    schema: str = "aspace.reconciliation-receipt.v1"
    receipt_id: str = ""
    entity_type: str = ""
    entity_id: str = ""
    classification: ReconciliationClassification = ReconciliationClassification.UNKNOWN
    decision: ReconciliationDecision = ReconciliationDecision.NOOP
    created_at: str = ""
    evidence_refs: List[str] = field(default_factory=list)
    work_id: Optional[str] = None
    correlation_id: Optional[str] = None

@dataclass
class SyncHealthProjection:
    schema: str = "aspace.sync-health-projection.v1"
    local_runtime: str = "UNKNOWN"
    workgraph: str = "UNKNOWN"
    supabase: str = "UNKNOWN"
    git: str = "UNKNOWN"
    projection_gateway: str = "OFFLINE"
    overall: str = "UNKNOWN"
    observed_at: str = ""
    reasons: List[str] = field(default_factory=list)
