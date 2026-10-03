#!/usr/bin/env python3
"""Business Plan Entitlement Boundary ($300/year Plan).

Defines the subscription entitlement boundary for A'Space Business-plan clients:
- Subscription entitlement ($300/year) grants access to the Cognitive Treasury routing broker engine,
  multi-provider failover, consent management, and receipt auditing.
- Subscription entitlement DOES NOT conflate or pool provider API quotas.
- Provider token quotas and API keys/tokens belong strictly to each tenant's connected provider accounts.
"""

from __future__ import annotations

import time
from typing import Any, Dict, Optional

from schemas import EntitlementBoundary


class EntitlementViolationError(PermissionError):
    """Raised when subscription entitlement limit is exceeded or subscription is inactive."""
    pass


class EntitlementManager:
    """Manages $300/year Business Plan entitlements for tenants."""

    def __init__(self):
        # tenant_id -> EntitlementBoundary
        self._entitlements: Dict[str, EntitlementBoundary] = {}
        # tenant_id -> timestamps of requests in current minute for rate limiting
        self._rate_trackers: Dict[str, list[float]] = {}

    def get_or_create_entitlement(
        self,
        tenant_id: str,
        plan_id: str = "business_300_year",
        active: bool = True,
    ) -> EntitlementBoundary:
        if tenant_id not in self._entitlements:
            self._entitlements[tenant_id] = EntitlementBoundary(
                tenant_id=tenant_id,
                plan_id=plan_id,
                plan_name="A'Space Business Plan ($300/year)",
                subscription_active=active,
                max_connected_profiles=10,
                routing_throughput_limit_rpm=100,
            )
        return self._entitlements[tenant_id]

    def set_subscription_status(self, tenant_id: str, active: bool) -> EntitlementBoundary:
        ent = self.get_or_create_entitlement(tenant_id)
        ent.subscription_active = active
        return ent

    def validate_connection_limit(self, tenant_id: str, current_connected_profiles_count: int) -> None:
        """Validates if adding a profile exceeds max allowed connected profiles for plan."""
        ent = self.get_or_create_entitlement(tenant_id)
        if not ent.subscription_active:
            raise EntitlementViolationError(f"Subscription for tenant '{tenant_id}' is inactive")

        if current_connected_profiles_count >= ent.max_connected_profiles:
            raise EntitlementViolationError(
                f"Tenant '{tenant_id}' reached max connected profiles limit ({ent.max_connected_profiles}) "
                f"for plan '{ent.plan_name}'"
            )

    def validate_routing_access(self, tenant_id: str) -> None:
        """Validates that tenant has an active subscription and is within throughput limits."""
        ent = self.get_or_create_entitlement(tenant_id)
        if not ent.subscription_active:
            raise EntitlementViolationError(
                f"Routing denied: Business Plan subscription for tenant '{tenant_id}' is inactive. "
                f"Please renew the $300/year plan to access Cognitive Treasury routing."
            )

        now = time.time()
        tracker = self._rate_trackers.setdefault(tenant_id, [])
        # prune timestamps older than 60s
        tracker[:] = [t for t in tracker if now - t < 60.0]

        if len(tracker) >= ent.routing_throughput_limit_rpm:
            raise EntitlementViolationError(
                f"Tenant '{tenant_id}' exceeded routing throughput limit "
                f"({ent.routing_throughput_limit_rpm} req/min) under {ent.plan_name}"
            )

        tracker.append(now)

    def entitlement_summary(self, tenant_id: str, connected_profiles_count: int) -> Dict[str, Any]:
        ent = self.get_or_create_entitlement(tenant_id)
        return {
            "tenant_id": tenant_id,
            "plan": ent.plan_name,
            "plan_id": ent.plan_id,
            "subscription_active": ent.subscription_active,
            "connected_profiles": connected_profiles_count,
            "max_connected_profiles": ent.max_connected_profiles,
            "throughput_limit_rpm": ent.routing_throughput_limit_rpm,
            "feature_flags": ent.feature_flags,
            "quota_ownership_model": "TENANT_PROPRIETARY",
            "disclaimer": ent.disclaimer,
        }
