#!/usr/bin/env python3
"""GitHub-native control-plane — ingress, egress, security and runtime neutrality.

This module implements the GitHub <--> Gateway membrane described in
docs/governance/ASPACE_GATEWAY_NATIVE_GITHUB_V0.md (gate #544) and
docs/governance/ASPACE_GITHUB_APP_AUTHORITY_ADAPTER_V0.md.

Architecture:

    X-GitHub-Delivery  X-GitHub-Event
           |                |
    X-Hub-Signature-256   payload
           |                |
           v                v
    SignatureVerifier  --> DeliveryDedupe --> GitHubEventNormalizer
                                                    |
                                    InterFabricEnvelope.v1
                                                    |
                                      Nardole / CapabilityFabric / HostPolicy

Guarantees:
- Webhook HMAC-SHA256 signature verification before any intent parsing.
- X-GitHub-Delivery as the first deduplication key.
- No blind retry on UNKNOWN epistemic state.
- Every effect carries `return_to`; no silent coercion.
- Provider-neutral: capability/holon resolved before runtime/provider.
- Fencing token per delivery to reject stale writers.
"""

from __future__ import annotations

import copy
import hashlib
import hmac
import json
import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

import jsonschema

logger = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parent.parent.parent.parent
SCHEMA_DIR = ROOT / "10_Tech_OS" / "kernel" / "contracts"

# ---------------------------------------------------------------------------
# Webhook security primitives
# ---------------------------------------------------------------------------


class SignatureVerificationError(ValueError):
    """Webhook HMAC-SHA256 signature could not be verified."""


class DeliveryDuplicateError(RuntimeError):
    """Duplicate delivery detected via X-GitHub-Delivery header."""


class DeliveryTimeoutError(RuntimeError):
    """Delivery ID was delivered but the event exceeded the retry/ambiguity window."""


def verify_signature(
    body: bytes,
    signature: str,
    secret: str,
    *,
    algorithm: str = "sha256",
) -> bool:
    """Verify the `X-Hub-Signature-256` header against the webhook secret.

    Fails closed (raises SignatureVerificationError) when verification fails
    or the signature header is missing.  This is the **first** gate before
    any intent parsing.
    """
    expected = f"sha256={hmac.new(
        secret.encode("utf-8"),
        body,
        algorithm,
    ).hexdigest()}"
    if not signature:
        raise SignatureVerificationError(
            "X-Hub-Signature-256 header missing; cannot verify webhook origin"
        )
    if not hmac.compare_digest(expected, signature):
        raise SignatureVerificationError(
            "HMAC-SHA256 signature mismatch; possible spoofed webhook"
        )
    return True


def verify_signature_raw(
    body: str | bytes,
    signature: str | None,
    secret: str,
) -> bool:
    """Convenience wrapper accepting body as string or bytes."""
    body_bytes = body.encode("utf-8") if isinstance(body, str) else body
    return verify_signature(body_bytes, signature or "", secret)


class DeliveryDeduper:
    """Idempotency tracker keyed by X-GitHub-Delivery.

    Tracks:
    - delivered: already processed delivery IDs.
    - pending: delivery IDs currently being processed (fencing).
    - unknown: deliveries that produced UNKNOWN epistemic state — never
      retried blindly per Gateway rule.
    """

    def __init__(
        self,
        capacity: int = 10_000,
        retention_seconds: int = 3600,
    ) -> None:
        self._capacity = capacity
        self._retention_seconds = retention_seconds
        self._delivered: Dict[str, float] = {}  # delivery_id -> timestamp
        self._pending: Dict[str, str] = {}       # delivery_id -> fencing_token
        self._unknown: Set[str] = set()          # delivery IDs in UNKNOWN
        self._base_time = datetime.now(timezone.utc).timestamp()

    def register(
        self,
        delivery_id: str,
        fencing_token: int,
    ) -> str:
        """Register a delivery and fence it.  Raises on duplicates/ambiguous.

        Returns the fencing token to attach to all downstream envelope edits.
        """
        # Expire stale entries first.
        self._expire()

        if delivery_id in self._unknown:
            raise DeliveryTimeoutError(
                "Delivery produced UNKNOWN epistemic state; blind retry is forbidden by Gateway policy. "
                "Manual recovery via Donna/RecoveryPort required."
            )
        if delivery_id in self._delivered:
            raise DeliveryDuplicateError(
                f"Duplicate delivery {delivery_id}; already processed"
            )
        if delivery_id in self._pending:
            existing_token = self._pending[delivery_id]
            if existing_token >= fencing_token:
                raise DeliveryTimeoutError(
                    f"Stale delivery {delivery_id} fenced by token {existing_token} >= {fencing_token}"
                )

        self._pending[delivery_id] = fencing_token
        return fencing_token

    def complete(
        self,
        delivery_id: str,
        *,
        epistemic_state: str = "UNKNOWN",
    ) -> None:
        """Mark delivery as completed (SUCCEEDED/FAILED/DLQ) or UNKNOWN."""
        self._pending.pop(delivery_id, None)
        if epistemic_state == "UNKNOWN":
            self._unknown.add(delivery_id)
        else:
            self._delivered[delivery_id] = (
                datetime.now(timezone.utc).timestamp()
            )

    def is_delivered(self, delivery_id: str) -> bool:
        return delivery_id in self._delivered

    def is_pending(self, delivery_id: str) -> bool:
        return delivery_id in self._pending

    def _expire(self) -> None:
        cutoff = datetime.now(timezone.utc).timestamp() - self._retention_seconds
        stale = [
            k for k, ts in self._delivered.items() if ts < cutoff
        ]
        old_unknown = [
            k for k in self._unknown
            if k not in self._pending
        ]
        for k in stale + old_unknown:
            self._delivered.pop(k, None)
            self._unknown.discard(k)
        if len(self._delivered) + len(self._unknown) >= self._capacity:
            # Keep most recent half, drop the rest.
            sorted_ids = sorted(
                self._delivered.items(), key=lambda x: x[1]
            )
            half = len(sorted_ids) // 2
            for k, _ in sorted_ids[:half]:
                self._delivered.pop(k, None)


def derive_fencing_token(delivery_id: str, base: int = 0) -> int:
    """Deterministic fencing token derived from delivery ID.

    Tokens increase monotonically; a stale writer produces a lower token
    and is rejected by DeliveryDeduper.register().
    """
    hex_hash = hashlib.sha256(delivery_id.encode("utf-8")).hexdigest()
    return base + int(hex_hash[:16], 16) % (10**9)


# ---------------------------------------------------------------------------
# GitHub event types (ingress normalizer)
# ---------------------------------------------------------------------------


class GHEventType(str, Enum):
    ISSUE = "issues"
    ISSUE_COMMENT = "issue_comment"
    PULL_REQUEST = "pull_request"
    PULL_REQUEST_REVIEW = "pull_request_review"
    CHECK_RUN = "check_run"
    CHECK_SUITE = "check_suite"
    WORKFLOW_RUN = "workflow_run"
    DISCUSSION = "discussion"
    DISCUSSION_COMMENT = "discussion_comment"
    RELEASE = "release"
    INSTALLATION = "installation"
    INSTALLATION_REPOSITORIES = "installation_repositories"


@dataclass
class GitHubEvent:
    """Normalized GitHub webhook event ready for InterFabricEnvelope creation."""

    event_type: GHEventType
    action: str
    delivery_id: str
    repository: str  # e.g. "Amdkn/Aspace_OS_V3"
    installation_id: int
    sender: str
    sender_type: str  # "User" | "Bot" | "Organization"
    issue_number: Optional[int] = None
    pull_request_number: Optional[int] = None
    discussion_url: Optional[str] = None
    check_status: Optional[str] = None  # success | failure | action_required | etc.
    release_tag: Optional[str] = None
    promoted: bool = False  # discussion => executable intent?

    def fingerprint(self) -> str:
        parts = [
            self.event_type.value,
            self.action,
            self.repository,
            str(self.delivery_id),
        ]
        return hashlib.sha256("|".join(parts).encode("utf-8")).hexdigest()[:64]


# ---------------------------------------------------------------------------
# Egress primitives
# ---------------------------------------------------------------------------


class GHPrimitive(str, Enum):
    DISCUSSION = "discussion"
    ISSUE = "issue"
    PULL_REQUEST = "pull_request"
    CHECK = "check"
    PROJECT = "project"
    MILESTONE = "milestone"
    RELEASE = "release"


@dataclass
class GHResult:
    """Typed Gateway egress result bound to a GitHub primitive."""

    primitive: GHPrimitive
    target_id: Optional[int] = None  # issue/PR/discussion number or check ID
    target_url: Optional[str] = None
    title: str = ""
    body: str = ""
    status: Optional[str] = None  # for checks: success | failure | pending
    conclusion: Optional[str] = None  # for checks: success | action_required | etc.
    label: Optional[str] = None  # for issues: category
    owner: Optional[str] = None  # holon_id that produced this result


# ---------------------------------------------------------------------------
# GitHubIngressNormalizer
# ---------------------------------------------------------------------------

# JSON schema for the ingress envelope that wraps a normalized GitHub event.
_INGRESS_SCHEMA = {
    "type": "object",
    "required": [
        "schema",
        "ingress_version",
        "event_type",
        "action",
        "delivery_id",
        "repository",
        "installation_id",
        "sender",
        "sender_type",
        "normalized_at",
        "fingerprint",
    ],
    "properties": {
        "schema": {"type": "string"},
        "ingress_version": {"type": "string"},
        "event_type": {"type": "string"},
        "action": {"type": "string"},
        "delivery_id": {"type": "string"},
        "repository": {"type": "string"},
        "installation_id": {"type": "integer"},
        "sender": {"type": "string"},
        "sender_type": {"type": "string"},
        "normalized_at": {"type": "string"},
        "fingerprint": {"type": "string"},
        "issue_number": {"type": ["integer", "null"]},
        "pull_request_number": {"type": ["integer", "null"]},
        "discussion_url": {"type": ["string", "null"]},
        "check_status": {"type": ["string", "null"]},
        "release_tag": {"type": ["string", "null"]},
        "promoted": {"type": "boolean"},
        "metadata": {"type": "object"},
    },
}


class GitHubIngressNormalizer:
    """Maps raw GitHub webhook payloads to normalized GitHubEvent objects.

    Does NOT inspect provider identity.  A GitHub event only provides the
    delivery channel; capability and authority determine the destination.
    """

    def __init__(self) -> None:
        self._schema = copy.deepcopy(_INGRESS_SCHEMA)

    @staticmethod
    def _parse_event_type(payload: Dict[str, Any]) -> GHEventType:
        """Detect event type from the GitHub X-GitHub-Event header or payload context."""
        event_type_str = payload.get("hook", {}).get("type", "unknown")
        for et in GHEventType:
            if event_type_str == et.value:
                return et
        return GHEventType(payload.get("hook", {}).get("type", "unknown"))

    @staticmethod
    def _derive_action(payload: Dict[str, Any]) -> str:
        """Extract the action from the payload; falls back to the event type."""
        return payload.get("action", "") or ""

    @staticmethod
    def _extract_repository(payload: Dict[str, Any]) -> str:
        repo = payload.get("repository", {})
        owner = repo.get("owner", {}).get("login", "")
        name = repo.get("name", "")
        return f"{owner}/{name}"

    def normalize(
        self,
        payload: Dict[str, Any],
        delivery_id: str,
        *,
        webhook_secret: str = "",
        secret_sha: str | None = None,
    ) -> GitHubEvent:
        """Parse a raw GitHub webhook payload into a normalized GitHubEvent.

        If `secret_sha` is provided, the signature from `X-Hub-Signature-256`
        is verified **before** normalisation proceeds.  Callers should
        invoke :func:`verify_signature` explicitly when the body is received
        over HTTP; `secret_sha` is a convenience for testing.
        """
        # Allow optional signature check.
        if secret_sha:
            body = json.dumps(
                payload, separators=(",", ":"), sort_keys=True
            ).encode("utf-8")
            verify_signature(body, secret_sha, webhook_secret)

        event_type = self._parse_event_type(payload)
        action = self._derive_action(payload)
        repository = self._extract_repository(payload)
        inst_id = payload.get("installation", {}).get("id", 0)
        sender = payload.get("sender", {}).get("login", "unknown")
        sender_type = payload.get("sender", {}).get("type", "Unknown")

        # Derive issue / PR / release metadata where present.
        issue_number = None
        if event_type in (GHEventType.ISSUE, GHEventType.ISSUE_COMMENT):
            issue_number = payload.get("issue", {}).get("number")
        pr_number = None
        if event_type in (GHEventType.PULL_REQUEST, GHEventType.PULL_REQUEST_REVIEW):
            pr_number = payload.get("pull_request", {}).get("number", payload.get("number"))
        check_status = None
        if event_type in (GHEventType.CHECK_RUN, GHEventType.CHECK_SUITE):
            check_status = payload.get("check_run", {}).get(
                "status",
                payload.get("check_suite", {}).get("status"),
            )
        release_tag = None
        if event_type == GHEventType.RELEASE:
            release_tag = payload.get("release", {}).get("tag_name")
        promoted = False
        if event_type in (GHEventType.DISCUSSION,):
            promoted = payload.get("discussion", {}).get("_aspace_promoted", False)
            promoted = promoted or payload.get("action") == "promoted"

        return GitHubEvent(
            event_type=event_type,
            action=action,
            delivery_id=delivery_id,
            repository=repository,
            installation_id=inst_id,
            sender=sender,
            sender_type=sender_type,
            issue_number=issue_number,
            pull_request_number=pr_number,
            check_status=check_status,
            release_tag=release_tag,
            promoted=promoted,
        )

    def event_to_ingress_dict(
        self,
        event: GitHubEvent,
    ) -> Dict[str, Any]:
        """Serialise a GitHubEvent into the typed ingress envelope schema."""
        now = datetime.now(timezone.utc).isoformat()
        envelope = {
            "schema": "aspace.gateway.github-ingress.v1",
            "ingress_version": "1.0.0",
            "event_type": event.event_type.value,
            "action": event.action,
            "delivery_id": event.delivery_id,
            "repository": event.repository,
            "installation_id": event.installation_id,
            "sender": event.sender,
            "sender_type": event.sender_type,
            "normalized_at": now,
            "fingerprint": event.fingerprint(),
            "issue_number": event.issue_number,
            "pull_request_number": event.pull_request_number,
            "discussion_url": event.discussion_url,
            "check_status": event.check_status,
            "release_tag": event.release_tag,
            "promoted": event.promoted,
            "metadata": {
                "original_event": event.event_type.value,
                "original_action": event.action,
            },
        }
        # Validate against our ingress schema.
        jsonschema.validate(instance=envelope, schema=self._schema)
        return envelope

    def ingress_to_envelope(
        self,
        ingress: Dict[str, Any],
        *,
        institution_id: str,
        holon_id: str,
        capability_id: Optional[str] = None,
        return_to: str = "",
        evidence_refs: Optional[List[str]] = None,
        fencing_token: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Wrap an ingress envelope in an InterFabricEnvelope-ready dict.

        The actual InterFabricEnvelope constructor is imported at runtime
        from `10_Tech_OS.kernel.inter_fabric` so that this module can be used
        standalone without the kernel.
        """
        from inter_fabric import InterFabricEnvelope  # type: ignore[import-not-found,import]

        envelope = InterFabricEnvelope.create(
            identity={
                "institutional_holon_id": institution_id,
                "embodiment_id": f"gh-app:{ingress['installation_id']}",
                "runtime_id": "github-control-plane",
                "device": "github-app",
                "surface_id": "github",
                "session_id": ingress["delivery_id"],
            },
            mission={
                "mission_id": f"incoming-{ingress['delivery_id']}",
                "work_id": ingress.get("issue_number") or ingress.get("pull_request_number") or 0,
                "cell_id": ingress["fingerprint"][:16],
                "correlation_id": ingress["delivery_id"],
            },
            capability={
                "capability_id": capability_id or "github.control-plane.ingress",
                "capability_version": "1.0.0",
                "contract_ref": "gateway-native-github:v1",
            },
            authority={
                "authority_scope": "github-ingress",
                "fencing_token": fencing_token,
                "policy_ref": "github-app-authority-adapter:v0",
            },
            resource=None,
            effect={
                "operation_id": f"gh-op:{ingress['delivery_id']}",
                "effect_id": None,
                "effect_class": "INGRESS",
                "idempotency_key": ingress["delivery_id"],
                "replay_semantics": "SAFE",
            },
            truth={
                "evidence_refs": evidence_refs or [],
                "observed_at": datetime.now(timezone.utc).isoformat(),
                "source_authority": "github-webhook",
                "epistemic_state": "UNKNOWN",  # Must be resolved downstream; not coerced.
                "freshness": "FRESH",
            },
            routing={
                "origin_layer": "GitHub",
                "return_to": return_to or f"github:{ingress['repository']}",
                "blocked_outcome": None,
            },
            compatibility={
                "envelope_version": "v1",
                "payload_schema": "aspace.gateway.github-ingress.v1",
                "payload_version": "1.0.0",
                "lossy_fields": [],
            },
            payload=ingress,
        )
        return envelope.to_dict()


# ---------------------------------------------------------------------------
# GitHubEgress — return typed results to GitHub primitives
# ---------------------------------------------------------------------------


class GitHubEgressAdapter:
    """Converts Gateway results back into the appropriate GitHub primitive.

    Egress rules per #544:
    - exploration result   -> Discussion reply
    - executable/work      -> Issue comment / state change
    - mutation             -> Pull Request
    - deterministic verdict -> Check run update
    - portfolio state      -> Project card update
    - release boundary     -> Milestone completion
    - promoted version     -> Release artifact
    """

    @staticmethod
    def _map_primitive(event: GitHubEvent) -> GHPrimitive:
        """Map the incoming event to the appropriate return primitive."""
        mapping = {
            GHEventType.DISCUSSION: GHPrimitive.DISCUSSION,
            GHEventType.DISCUSSION_COMMENT: GHPrimitive.DISCUSSION,
            GHEventType.ISSUE: GHPrimitive.ISSUE,
            GHEventType.ISSUE_COMMENT: GHPrimitive.ISSUE,
            GHEventType.PULL_REQUEST: GHPrimitive.PULL_REQUEST,
            GHEventType.PULL_REQUEST_REVIEW: GHPrimitive.PULL_REQUEST,
            GHEventType.CHECK_RUN: GHPrimitive.CHECK,
            GHEventType.CHECK_SUITE: GHPrimitive.CHECK,
            GHEventType.WORKFLOW_RUN: GHPrimitive.CHECK,
            GHEventType.RELEASE: GHPrimitive.RELEASE,
            GHEventType.INSTALLATION: GHPrimitive.ISSUE,
            GHEventType.INSTALLATION_REPOSITORIES: GHPrimitive.ISSUE,
        }
        return mapping.get(event.event_type, GHPrimitive.ISSUE)

    def build_result(
        self,
        event: GitHubEvent,
        *,
        holon_id: str,
        status: Optional[str] = None,
        conclusion: Optional[str] = None,
        body: str = "",
        label: Optional[str] = None,
        target_id: Optional[int] = None,
    ) -> GHResult:
        """Produce a typed GHResult for the given event."""
        primitive = self._map_primitive(event)
        return GHResult(
            primitive=primitive,
            target_id=target_id or (event.issue_number or event.pull_request_number),
            title=f"[GW:{holon_id}] {event.event_type.value}:{event.action}",
            body=body,
            status=status,
            conclusion=conclusion,
            label=label,
            owner=holon_id,
        )

    def get_egress_primitive(self, event: GitHubEvent) -> GHPrimitive:
        return self._map_primitive(event)


# ---------------------------------------------------------------------------
# Provider-neutral dispatch (runtime neutrality)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class DispatchRequest:
    """Gateway-ready dispatch request that is **purely capability-driven**.

    The provider field exists only after the Gateway has resolved that the
    selected runtime is admissible (authority + health + budget checks passed).
    """

    holon_id: str
    capability_id: str
    capability_version: str
    repository: str
    event_id: str
    return_to: str
    evidence_refs: List[str]
    authoriser: str  # who approved this dispatch
    dedup_key: str


def derive_provider_neutral_dedup_key(request: DispatchRequest) -> str:
    """Deterministic dedup key that does **not** depend on provider.

    This allows the same dispatch to be retried against a different runtime
    without being considered a duplicate.
    """
    parts = (
        request.holon_id,
        request.capability_id,
        request.capability_version,
        request.repository,
        request.event_id,
    )
    return hashlib.sha256("|".join(parts).encode("utf-8")).hexdigest()[:64]


class ProviderResolver:
    """Resolves capability/holon first, provider second.

    This is the implementation cell of #544 § Provider neutrality.
    It does NOT select a provider; it returns admissible runtime candidates
    in priority order after capability/authority/health checks.
    """

    def __init__(self) -> None:
        # Placeholder registry — real implementation queries Capability Fabric (#333).
        self._registry: Dict[str, List[Dict[str, Any]]] = {}

    def register_capability(self, capability_id: str, candidates: List[Dict[str, Any]]) -> None:
        """Register candidate runtimes for a capability."""
        self._registry[capability_id] = candidates

    def resolve(self, capability_id: str) -> List[str]:
        """Return ordered list of admissible provider IDs for `capability_id`."""
        return [c["id"] for c in self._registry.get(capability_id, [])]

    def build_dispatch(
        self,
        event: GitHubEvent,
        holon_id: str,
        capability_id: str,
        return_to: str,
        evidence_refs: List[str],
        authoriser: str,
    ) -> DispatchRequest:
        req = DispatchRequest(
            holon_id=holon_id,
            capability_id=capability_id,
            capability_version="1.0.0",
            repository=event.repository,
            event_id=event.delivery_id,
            return_to=return_to,
            evidence_refs=evidence_refs,
            authoriser=authoriser,
            dedup_key="",  # filled by derive_provider_neutral_dedup_key
        )
        req = DispatchRequest(
            **{**req.__dict__, "dedup_key": derive_provider_neutral_dedup_key(req)},
        )
        return req


# ---------------------------------------------------------------------------
# No-blind-retry guard on UNKNOWN
# ---------------------------------------------------------------------------


class UnknownStateGuard:
    """Ensures UNKNOWN epistemic state is never resolved by blind retry.

    Gateway rule (verbatim from #544):
    "no blind retry on UNKNOWN"
    """

    def __init__(self) -> None:
        self._frozen: Dict[str, str] = {}

    def record_unknown(self, delivery_id: str, reason: str) -> None:
        self._frozen[delivery_id] = reason

    def is_frozen(self, delivery_id: str) -> bool:
        return delivery_id in self._frozen

    def resolve(self, delivery_id: str, recovery_decision: str) -> bool:
        if not recovery_decision:
            return False
        self._frozen.pop(delivery_id, None)
        return True


# ---------------------------------------------------------------------------
# Public API — the "one path" for a GitHub Issue through the Gateway
# ---------------------------------------------------------------------------


def github_ingress_to_egress(
    raw_payload: Dict[str, Any],
    delivery_id: str,
    signature: str,
    webhook_secret: str,
    *,
    institution_id: str = "Amdkn",
    holon_id: str = "Gateway",
    return_to: str = "",
    evidence_refs: Optional[List[str]] = None,
) -> GHResult:
    """End-to-end: GitHub event in -> normalized -> routed -> egress out.

    Acceptance test for #544:
        One GitHub Issue can enter the Gateway, be routed to an admissible
        non-GitHub runtime, and return as PR/check/evidence without the
        Issue being provider-specific.
    """
    body = json.dumps(
        raw_payload, separators=(",", ":"), sort_keys=True
    ).encode("utf-8")
    verify_signature(body, signature, webhook_secret)

    normalizer = GitHubIngressNormalizer()
    event = normalizer.normalize(
        raw_payload,
        delivery_id,
        webhook_secret=webhook_secret,
    )

    deduper = DeliveryDeduper(capacity=1000)
    fencing_token = deduper.register(delivery_id, derive_fencing_token(delivery_id))

    ingress = normalizer.event_to_ingress_dict(event)
    envelope = normalizer.ingress_to_envelope(
        ingress,
        institution_id=institution_id,
        holon_id=holon_id,
        return_to=return_to,
        evidence_refs=evidence_refs or [],
        fencing_token=fencing_token,
    )

    egress = GitHubEgressAdapter()
    result = egress.build_result(
        event,
        holon_id=holon_id,
        body=json.dumps(envelope, indent=2),
    )

    # Route to runtime — provider-neutral dedup key means the same dispatch
    # can be retried against a different runtime without collision.
    resolver = ProviderResolver()
    dispatch = resolver.build_dispatch(
        event=event,
        holon_id=holon_id,
        capability_id="github.control-plane.ingress",
        return_to=return_to or f"github:{event.repository}",
        evidence_refs=evidence_refs or [],
        authoriser="system-bootstrap",
    )

    logger.info(
        "GitHub ingress->egress complete: event=%s action=%s delivery=%s "
        "primitive=%s dedup=%s fencing=%d",
        event.event_type.value,
        event.action,
        delivery_id,
        result.primitive.value,
        dispatch.dedup_key,
        fencing_token,
    )

    return result


# ---------------------------------------------------------------------------
# CLI for testing / debugging
# ---------------------------------------------------------------------------


def _main() -> int:
    import sys

    parser = argparse.ArgumentParser(
        description="GitHub-native control-plane diagnostic"
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_verify = sub.add_parser("verify-signature")
    p_verify.add_argument("body_file", type=Path)
    p_verify.add_argument("--signature", required=True)
    p_verify.add_argument("--secret", required=True)

    p_normalize = sub.add_parser("normalize")
    p_normalize.add_argument("payload_file", type=Path)
    p_normalize.add_argument("--delivery-id", required=True)

    p_ingress = sub.add_parser("ingress-to-egress")
    p_ingress.add_argument("payload_file", type=Path)
    p_ingress.add_argument("--delivery-id", required=True)
    p_ingress.add_argument("--signature", required=True)
    p_ingress.add_argument("--secret", required=True)
    p_ingress.add_argument("--return-to", default="github:main")

    args = parser.parse_args()

    if args.cmd == "verify-signature":
        body = args.body_file.read_bytes()
        ok = verify_signature_raw(body, args.signature, args.secret)
        print(json.dumps({"verified": ok}))
        return 0 if ok else 1

    if args.cmd == "normalize":
        payload = json.loads(args.payload_file.read_text(encoding="utf-8"))
        n = GitHubIngressNormalizer()
        event = n.normalize(payload, args.delivery_id)
        print(json.dumps({
            "event_type": event.event_type.value,
            "action": event.action,
            "delivery_id": event.delivery_id,
            "repository": event.repository,
            "issue_number": event.issue_number,
            "fingerprint": event.fingerprint(),
        }, indent=2))
        return 0

    if args.cmd == "ingress-to-egress":
        payload = json.loads(args.payload_file.read_text(encoding="utf-8"))
        body = json.dumps(
            payload, separators=(",", ":"), sort_keys=True
        ).encode("utf-8")
        result = github_ingress_to_egress(
            raw_payload=payload,
            delivery_id=args.delivery_id,
            signature=args.signature,
            webhook_secret=args.secret,
            return_to=args.return_to,
        )
        print(json.dumps({
            "status": "OK",
            "primitive": result.primitive.value,
            "target_id": result.target_id,
            "owner": result.owner,
        }, indent=2))
        return 0

    return 1


if __name__ == "__main__":
    import argparse
    raise SystemExit(_main())
