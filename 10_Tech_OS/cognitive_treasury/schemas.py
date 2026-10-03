#!/usr/bin/env python3
"""Cognitive Treasury Schemas.

Defines schemas for:
- ProviderAuthProfile
- TenantResourcePool
- ResourceReceipt
- ConsentRecord
- EntitlementBoundary
"""

from __future__ import annotations

import datetime
import json
import uuid
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional

SCHEMA_PROVIDER_AUTH_PROFILE = "aspace.cognitive-treasury.provider-auth-profile.v1"
SCHEMA_TENANT_RESOURCE_POOL = "aspace.cognitive-treasury.tenant-resource-pool.v1"
SCHEMA_RESOURCE_RECEIPT = "aspace.cognitive-treasury.resource-receipt.v1"
SCHEMA_CONSENT_RECORD = "aspace.cognitive-treasury.consent-record.v1"
SCHEMA_ENTITLEMENT_BOUNDARY = "aspace.cognitive-treasury.entitlement-boundary.v1"


def now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


@dataclass
class ProviderAuthProfile:
    tenant_id: str
    provider_id: str  # e.g., 'google', 'openai', 'anthropic'
    provider_account_id: str  # e.g., 'user@gmail.com', 'org_123'
    auth_type: str  # 'oauth2_pkce', 'api_key', 'bearer_token'
    encrypted_credentials: str  # Vault reference or encrypted payload
    scopes: List[str] = field(default_factory=list)
    profile_id: str = field(default_factory=lambda: f"pap-{uuid.uuid4().hex[:12]}")
    status: str = "ACTIVE"  # ACTIVE, REVOKED, EXPIRED, PENDING_AUTH
    connected_at: str = field(default_factory=now_iso)
    updated_at: str = field(default_factory=now_iso)
    metadata: Dict[str, Any] = field(default_factory=dict)
    schema: str = SCHEMA_PROVIDER_AUTH_PROFILE

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> ProviderAuthProfile:
        clean = {k: v for k, v in data.items() if k in cls.__dataclass_fields__}
        return cls(**clean)


@dataclass
class TenantResourcePool:
    tenant_id: str
    pool_id: str = field(default_factory=lambda: f"trp-{uuid.uuid4().hex[:12]}")
    profile_ids: List[str] = field(default_factory=list)
    total_quota_consumed: Dict[str, Any] = field(default_factory=dict)
    updated_at: str = field(default_factory=now_iso)
    schema: str = SCHEMA_TENANT_RESOURCE_POOL

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> TenantResourcePool:
        clean = {k: v for k, v in data.items() if k in cls.__dataclass_fields__}
        return cls(**clean)


@dataclass
class ResourceReceipt:
    tenant_id: str
    provider_id: str
    provider_account_id: str
    model: str
    budget_consumed: Dict[str, Any]  # e.g., {"input_tokens": 100, "output_tokens": 200, "total_tokens": 300}
    latency_ms: int
    result_or_evidence: Dict[str, Any]  # e.g., {"status": "SUCCESS", "digest": "..."}
    remaining_or_unknown_quota: Dict[str, Any]  # e.g., {"remaining": 900000, "unit": "tokens_per_month"}
    correlation_id: str
    receipt_id: str = field(default_factory=lambda: f"rrcpt-{uuid.uuid4().hex[:16]}")
    timestamp: str = field(default_factory=now_iso)
    schema: str = SCHEMA_RESOURCE_RECEIPT

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> ResourceReceipt:
        clean = {k: v for k, v in data.items() if k in cls.__dataclass_fields__}
        return cls(**clean)


@dataclass
class ConsentRecord:
    tenant_id: str
    provider_id: str
    granted_scopes: List[str]
    consent_id: str = field(default_factory=lambda: f"cns-{uuid.uuid4().hex[:12]}")
    granted_at: str = field(default_factory=now_iso)
    revoked_at: Optional[str] = None
    status: str = "ACTIVE"  # ACTIVE, REVOKED
    schema: str = SCHEMA_CONSENT_RECORD

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> ConsentRecord:
        clean = {k: v for k, v in data.items() if k in cls.__dataclass_fields__}
        return cls(**clean)


@dataclass
class EntitlementBoundary:
    tenant_id: str
    plan_id: str = "business_300_year"
    plan_name: str = "A'Space Business Plan ($300/year)"
    subscription_active: bool = True
    max_connected_profiles: int = 10
    routing_throughput_limit_rpm: int = 100
    feature_flags: Dict[str, bool] = field(
        default_factory=lambda: {
            "cognitive_treasury_routing": True,
            "federated_auth_broker": True,
            "custom_routing_policies": True,
            "multi_provider_failover": True,
        }
    )
    disclaimer: str = (
        "Subscription entitlement covers Cognitive Treasury broker access. "
        "Provider API quotas remain strictly owned by the tenant's connected provider accounts."
    )
    schema: str = SCHEMA_ENTITLEMENT_BOUNDARY

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> EntitlementBoundary:
        clean = {k: v for k, v in data.items() if k in cls.__dataclass_fields__}
        return cls(**clean)
