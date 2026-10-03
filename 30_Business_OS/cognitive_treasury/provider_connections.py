"""
Business OS Client-Owned AI Provider Connections & Cognitive Treasury (#419)

Business OS owns commercial subscription entitlement ($300/year plan) and customer experience
for connecting client-owned AI provider accounts to the shared A'Space Cognitive Treasury.

Key Architectural Laws:
1. Commercial subscription entitlement is strictly separated from provider quota ownership.
2. Raw provider secrets are never stored or duplicated in Business OS state; only secret handles
   and redacted fingerprints are preserved.
3. Provider quota capacity is measured dynamically rather than promised as fixed capacity.
4. Provider revocation is strictly isolated: revoking one provider connection never alters
   tenant identity or disrupts remaining active provider connections.
"""

import uuid
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional


class EntitlementError(Exception):
    """Raised when a tenant attempts provider connections without valid plan entitlement."""
    pass


class ProviderConnectionError(Exception):
    """Raised when provider connection authorization or execution fails."""
    pass


class SubscriptionPlan:
    PLAN_300_ANNUAL = "BUSINESS_300_ANNUAL"
    PLAN_FREE = "BUSINESS_FREE"


class ProviderConnectionState:
    ACTIVE = "ACTIVE"
    DEGRADED = "DEGRADED"
    REVOKED = "REVOKED"


class EffectReceipt:
    """Canonical EffectReceipt capturing business state transition proof."""
    def __init__(
        self,
        operation_id: str,
        correlation_id: str,
        causation_id: str,
        capability_id: str,
        capability_version: str,
        source: str,
        target: str,
        idempotency_key: str,
        requested_at: str,
        observed_at: str,
        observed_effect: Dict[str, Any],
        evidence_refs: List[str],
        retry_safe: bool,
        status: str,
        compensation_ref: Optional[str] = None
    ):
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

    def to_dict(self) -> Dict[str, Any]:
        return self.__dict__


class ProviderConnection:
    """Representation of a tenant's authorized connection to an external AI provider."""
    def __init__(
        self,
        tenant_id: str,
        provider_id: str,
        secret_handle: str,
        redacted_fingerprint: str,
        scopes: List[str],
        status: str = ProviderConnectionState.ACTIVE,
        measured_quota: Optional[Dict[str, Any]] = None
    ):
        self.connection_id = f"conn_{uuid.uuid4().hex[:12]}"
        self.tenant_id = tenant_id
        self.provider_id = provider_id
        self.secret_handle = secret_handle
        self.redacted_fingerprint = redacted_fingerprint
        self.scopes = scopes
        self.status = status
        self.authorized_at = datetime.now(timezone.utc).isoformat()
        self.last_health_check = datetime.now(timezone.utc).isoformat()
        self.measured_quota = measured_quota or {
            "quota_type": "VARIABLE_MEASURED",
            "tokens_consumed": 0,
            "tokens_remaining_estimate": 1000000,
            "rate_limit_rpm": 500,
            "last_measured_at": datetime.now(timezone.utc).isoformat()
        }

    def update_measured_quota(self, tokens_used: int):
        self.measured_quota["tokens_consumed"] += tokens_used
        self.measured_quota["tokens_remaining_estimate"] = max(
            0, self.measured_quota["tokens_remaining_estimate"] - tokens_used
        )
        self.measured_quota["last_measured_at"] = datetime.now(timezone.utc).isoformat()

    def to_view_model(self) -> Dict[str, Any]:
        """Expose UX view model without raw credentials."""
        return {
            "connection_id": self.connection_id,
            "tenant_id": self.tenant_id,
            "provider_id": self.provider_id,
            "secret_handle": self.secret_handle,
            "redacted_fingerprint": self.redacted_fingerprint,
            "scopes": self.scopes,
            "status": self.status,
            "authorized_at": self.authorized_at,
            "last_health_check": self.last_health_check,
            "measured_quota": self.measured_quota
        }


class EntitlementManager:
    """Manages $300/year commercial plan subscription entitlements."""
    def __init__(self):
        self._tenant_plans: Dict[str, str] = {}

    def set_tenant_plan(self, tenant_id: str, plan: str):
        self._tenant_plans[tenant_id] = plan

    def get_tenant_plan(self, tenant_id: str) -> str:
        return self._tenant_plans.get(tenant_id, SubscriptionPlan.PLAN_FREE)

    def check_entitlement(self, tenant_id: str):
        plan = self.get_tenant_plan(tenant_id)
        if plan != SubscriptionPlan.PLAN_300_ANNUAL:
            raise EntitlementError(
                f"Tenant '{tenant_id}' under plan '{plan}' lacks entitlement for "
                f"client-owned AI provider connections. Requires '{SubscriptionPlan.PLAN_300_ANNUAL}'."
            )


class CognitiveTreasuryBroker:
    """
    Shared broker orchestrating client-owned provider authorization,
    capability routing, measured quota accounting, and isolated revocation.
    """
    def __init__(self, entitlement_manager: Optional[EntitlementManager] = None):
        self.entitlement_manager = entitlement_manager or EntitlementManager()
        # Storage: tenant_id -> provider_id -> ProviderConnection
        self._connections: Dict[str, Dict[str, ProviderConnection]] = {}
        # Audit log of receipts per tenant
        self._receipts: Dict[str, List[EffectReceipt]] = {}

    @staticmethod
    def _redact_secret(raw_secret: str) -> str:
        if len(raw_secret) <= 8:
            return "****"
        return f"{raw_secret[:3]}...{raw_secret[-4:]}"

    def authorize_provider(
        self,
        tenant_id: str,
        provider_id: str,
        raw_secret: str,
        scopes: Optional[List[str]] = None
    ) -> ProviderConnection:
        """
        Authorize a client-owned provider connection for a tenant.
        Strictly verifies $300/year plan entitlement before connecting.
        Raw secret is converted into a broker secret_handle; raw secret is NEVER saved in Business OS state.
        """
        self.entitlement_manager.check_entitlement(tenant_id)

        if not raw_secret or not raw_secret.strip():
            raise ProviderConnectionError("Cannot authorize provider without a valid credential.")

        # Create opaque broker secret handle and redacted fingerprint
        secret_handle = f"sec_broker_{tenant_id}_{provider_id}_{uuid.uuid4().hex[:8]}"
        redacted_fp = self._redact_secret(raw_secret)

        conn = ProviderConnection(
            tenant_id=tenant_id,
            provider_id=provider_id,
            secret_handle=secret_handle,
            redacted_fingerprint=redacted_fp,
            scopes=scopes or ["llm.execute", "models.read"],
            status=ProviderConnectionState.ACTIVE
        )

        if tenant_id not in self._connections:
            self._connections[tenant_id] = {}

        self._connections[tenant_id][provider_id] = conn
        return conn

    def get_connection_status(
        self, tenant_id: str, provider_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Return view models showing connection health, consent, and measured quotas."""
        tenant_conns = self._connections.get(tenant_id, {})
        if provider_id:
            conn = tenant_conns.get(provider_id)
            return [conn.to_view_model()] if conn else []
        return [c.to_view_model() for c in tenant_conns.values()]

    def execute_shared_capability(
        self,
        tenant_id: str,
        capability_id: str,
        payload: Dict[str, Any],
        preferred_provider: Optional[str] = None,
        idempotency_key: Optional[str] = None
    ) -> EffectReceipt:
        """
        Execute a capability using the tenant's authorized AI provider connections.
        Measures dynamic quotas rather than assuming static limits.
        Generates a transparent usage/evidence EffectReceipt.
        """
        self.entitlement_manager.check_entitlement(tenant_id)

        tenant_conns = self._connections.get(tenant_id, {})
        active_conns = {
            pid: conn for pid, conn in tenant_conns.items()
            if conn.status == ProviderConnectionState.ACTIVE
        }

        if not active_conns:
            raise ProviderConnectionError(
                f"No active provider connections available for tenant '{tenant_id}'."
            )

        selected_pid = preferred_provider if preferred_provider in active_conns else next(iter(active_conns))
        connection = active_conns[selected_pid]

        requested_at = datetime.now(timezone.utc).isoformat()
        correlation_id = f"corr_{uuid.uuid4().hex[:12]}"
        idemp_key = idempotency_key or f"idemp_{uuid.uuid4().hex[:12]}"

        # Simulate capability execution & variable quota consumption
        simulated_tokens = payload.get("estimated_tokens", 1250)
        connection.update_measured_quota(simulated_tokens)

        observed_at = datetime.now(timezone.utc).isoformat()

        observed_effect = {
            "tenant_id": tenant_id,
            "provider_id": connection.provider_id,
            "secret_handle": connection.secret_handle,
            "capability_id": capability_id,
            "execution_status": "COMPLETED",
            "measured_quota_impact": {
                "tokens_consumed": simulated_tokens,
                "measured_remaining_quota": connection.measured_quota["tokens_remaining_estimate"]
            },
            "output_summary": f"Capability '{capability_id}' executed successfully via provider '{connection.provider_id}'."
        }

        receipt = EffectReceipt(
            operation_id=str(uuid.uuid4()),
            correlation_id=correlation_id,
            causation_id=capability_id,
            capability_id=capability_id,
            capability_version="1.0.0",
            source=f"tenant:{tenant_id}",
            target=f"provider:{connection.provider_id}",
            idempotency_key=idemp_key,
            requested_at=requested_at,
            observed_at=observed_at,
            observed_effect=observed_effect,
            evidence_refs=[f"evidence:{idemp_key}"],
            retry_safe=True,
            status="SUCCEEDED"
        )

        if tenant_id not in self._receipts:
            self._receipts[tenant_id] = []
        self._receipts[tenant_id].append(receipt)

        return receipt

    def revoke_provider(self, tenant_id: str, provider_id: str) -> Dict[str, Any]:
        """
        Revoke authorization for a specific provider connection.
        Crucial requirement: Tenant identity remains intact, and other active providers continue operating normally.
        """
        tenant_conns = self._connections.get(tenant_id, {})
        if provider_id not in tenant_conns:
            raise ProviderConnectionError(
                f"Provider '{provider_id}' not connected for tenant '{tenant_id}'."
            )

        conn = tenant_conns[provider_id]
        conn.status = ProviderConnectionState.REVOKED

        return {
            "tenant_id": tenant_id,
            "provider_id": provider_id,
            "status": ProviderConnectionState.REVOKED,
            "revoked_at": datetime.now(timezone.utc).isoformat(),
            "remaining_active_providers": [
                pid for pid, c in tenant_conns.items()
                if c.status == ProviderConnectionState.ACTIVE
            ]
        }

    def get_receipts(self, tenant_id: str) -> List[Dict[str, Any]]:
        return [r.to_dict() for r in self._receipts.get(tenant_id, [])]
