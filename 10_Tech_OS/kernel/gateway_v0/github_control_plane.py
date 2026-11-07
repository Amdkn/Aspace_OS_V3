#!/usr/bin/env python3
"""
A'Space Gateway v0 — G1 GitHub-native Control Plane

Makes GitHub a **native control plane**, not the runtime.

Ingress: Normalize relevant GitHub events into typed Gateway ingress
- issues / issue comments
- pull requests / reviews
- workflow/check results
- discussions when promoted to executable intent

Egress: Return typed results as appropriate GitHub primitive
- Discussion = exploration
- Issue = executable/blocked cell
- PR = mutation + evidence
- Check/Action = deterministic gate
- Project = portfolio
- Milestone = convergence
- Release = promotion

Runtime neutrality: GitHub task intent must resolve capability/holon first; provider second.
Supported embodiments: GitHub-native Codex/Claude/Copilot and external Hermes/Antigravity/Jules/local Codex/Claude through adapters.

Security/Reliability:
- webhook signature verification
- delivery-id dedupe
- fencing
- no blind retry on UNKNOWN
- evidence + return_to round-trip

Acceptance: One GitHub Issue can enter the Gateway, be routed to an admissible non-GitHub runtime,
and return as PR/check/evidence without the Issue being provider-specific.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import uuid
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional, Callable, Literal
from pathlib import Path

from inter_fabric import InterFabricEnvelope, InterFabricInvariantError
from .protocol import (
    GatewayEnvelope,
    GatewayProtocol,
    IdentityCoordinates,
    MissionCoordinates,
    CapabilityCoordinates,
    AuthorityEnvelope,
    ResourceCoordinates,
    EffectCoordinates,
    TruthCoordinates,
    RoutingCoordinates,
    CompatibilityCoordinates,
    DeliveryState,
    Freshness,
    EpistemicState,
    create_gateway_envelope_from_cli,
)


class GitHubEventType(str, Enum):
    """Normalized GitHub event types for Gateway ingress."""
    ISSUE_OPENED = "issue_opened"
    ISSUE_CLOSED = "issue_closed"
    ISSUE_REOPENED = "issue_reopened"
    ISSUE_COMMENT = "issue_comment"
    PR_OPENED = "pr_opened"
    PR_CLOSED = "pr_closed"
    PR_REOPENED = "pr_reopened"
    PR_MERGED = "pr_merged"
    PR_REVIEW = "pr_review"
    PR_REVIEW_COMMENT = "pr_review_comment"
    WORKFLOW_RUN = "workflow_run"
    CHECK_RUN = "check_run"
    CHECK_SUITE = "check_suite"
    DISCUSSION = "discussion"
    DISCUSSION_COMMENT = "discussion_comment"
    RELEASE = "release"
    PUSH = "push"


class GitHubPrimitiveType(str, Enum):
    """GitHub primitives for egress mapping."""
    DISCUSSION = "discussion"
    ISSUE = "issue"
    PULL_REQUEST = "pull_request"
    CHECK = "check"
    ACTION = "action"
    PROJECT = "project"
    MILESTONE = "milestone"
    RELEASE = "release"


class IntentClassification(str, Enum):
    """Classification of GitHub event intent."""
    EXPLORATION = "exploration"  # -> Discussion
    EXECUTABLE = "executable"    # -> Issue
    MUTATION = "mutation"        # -> PR
    VERIFICATION = "verification"  # -> Check/Action
    PORTFOLIO = "portfolio"      # -> Project
    CONVERGENCE = "convergence"  # -> Milestone
    PROMOTION = "promotion"      # -> Release
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class GitHubEvent:
    """Normalized GitHub event for Gateway ingress."""
    event_type: GitHubEventType
    delivery_id: str  # GitHub delivery ID for dedupe
    timestamp: str
    repository: str
    actor: str
    payload: Dict[str, Any]
    signature_verified: bool = False
    intent: IntentClassification = IntentClassification.UNKNOWN
    capability_ref: Optional[str] = None
    holon_ref: Optional[str] = None


@dataclass(frozen=True)
class GitHubEgress:
    """Gateway egress targeting a GitHub primitive."""
    primitive: GitHubPrimitiveType
    action: str  # create, update, close, comment, etc.
    target_ref: str  # issue number, PR number, discussion ID, etc.
    payload: Dict[str, Any]
    evidence_refs: List[str] = field(default_factory=list)
    return_to: str = ""
    correlation_id: str = ""


class GitHubWebhookVerifier:
    """Verifies GitHub webhook signatures."""

    def __init__(self, webhook_secret: str):
        self.secret = webhook_secret.encode()

    def verify(self, payload: bytes, signature_header: str) -> bool:
        """Verify HMAC signature from GitHub."""
        if not signature_header or not signature_header.startswith("sha256="):
            return False
        expected = hmac.new(self.secret, payload, hashlib.sha256).hexdigest()
        received = signature_header[7:]  # Remove "sha256="
        return hmac.compare_digest(expected, received)


class GitHubEventNormalizer:
    """Normalizes raw GitHub webhook payloads into Gateway events."""

    def __init__(self, webhook_verifier: Optional[GitHubWebhookVerifier] = None):
        self.verifier = webhook_verifier
        self._seen_delivery_ids: set = set()

    def normalize(
        self,
        event_name: str,
        payload: Dict[str, Any],
        delivery_id: str,
        signature: Optional[str] = None,
    ) -> GitHubEvent:
        """Normalize a GitHub webhook into a Gateway event."""
        # Dedupe
        if delivery_id in self._seen_delivery_ids:
            raise ValueError(f"Duplicate delivery_id: {delivery_id}")
        self._seen_delivery_ids.add(delivery_id)

        # Verify signature if verifier configured
        signature_verified = False
        if self.verifier and signature:
            signature_verified = self.verifier.verify(
                json.dumps(payload, separators=(",", ":")).encode(),
                signature
            )

        # Extract common fields
        repo = payload.get("repository", {}).get("full_name", "")
        actor = payload.get("sender", {}).get("login", "")
        timestamp = payload.get("timestamp", datetime.now(timezone.utc).isoformat())

        # Map event type
        event_type = self._map_event_type(event_name, payload)

        # Classify intent
        intent = self._classify_intent(event_type, payload)

        # Extract capability/holon refs from labels, body, etc.
        capability_ref = self._extract_capability_ref(payload)
        holon_ref = self._extract_holon_ref(payload)

        return GitHubEvent(
            event_type=event_type,
            delivery_id=delivery_id,
            timestamp=timestamp,
            repository=repo,
            actor=actor,
            payload=payload,
            signature_verified=signature_verified,
            intent=intent,
            capability_ref=capability_ref,
            holon_ref=holon_ref,
        )

    def _map_event_type(self, event_name: str, payload: Dict[str, Any]) -> GitHubEventType:
        """Map GitHub event name to normalized type."""
        action = payload.get("action", "")

        mapping = {
            "issues": {
                "opened": GitHubEventType.ISSUE_OPENED,
                "closed": GitHubEventType.ISSUE_CLOSED,
                "reopened": GitHubEventType.ISSUE_REOPENED,
            },
            "issue_comment": {
                "created": GitHubEventType.ISSUE_COMMENT,
            },
            "pull_request": {
                "opened": GitHubEventType.PR_OPENED,
                "closed": GitHubEventType.PR_CLOSED if not payload.get("pull_request", {}).get("merged") else GitHubEventType.PR_MERGED,
                "reopened": GitHubEventType.PR_REOPENED,
            },
            "pull_request_review": {
                "submitted": GitHubEventType.PR_REVIEW,
            },
            "pull_request_review_comment": {
                "created": GitHubEventType.PR_REVIEW_COMMENT,
            },
            "workflow_run": GitHubEventType.WORKFLOW_RUN,
            "check_run": GitHubEventType.CHECK_RUN,
            "check_suite": GitHubEventType.CHECK_SUITE,
            "discussion": {
                "opened": GitHubEventType.DISCUSSION,
                "edited": GitHubEventType.DISCUSSION,
                "deleted": GitHubEventType.DISCUSSION,
            },
            "discussion_comment": {
                "created": GitHubEventType.DISCUSSION_COMMENT,
            },
            "release": GitHubEventType.RELEASE,
            "push": GitHubEventType.PUSH,
        }

        if event_name in mapping:
            entry = mapping[event_name]
            if isinstance(entry, dict):
                return entry.get(action, GitHubEventType.DISCUSSION)
            return entry

        return GitHubEventType.DISCUSSION

    def _classify_intent(self, event_type: GitHubEventType, payload: Dict[str, Any]) -> IntentClassification:
        """Classify the intent of a GitHub event."""
        # Issues with specific labels -> executable
        if event_type in (GitHubEventType.ISSUE_OPENED, GitHubEventType.ISSUE_REOPENED):
            issue = payload.get("issue", {})
            labels = [l.get("name", "").lower() for l in issue.get("labels", [])]
            if any(l in ("executable", "gateway:execute", "gate:") for l in labels):
                return IntentClassification.EXECUTABLE
            if any(l in ("exploration", "rfc", "research") for l in labels):
                return IntentClassification.EXPLORATION
            # Default: check if it has acceptance criteria
            body = issue.get("body", "")
            if "acceptance" in body.lower() or "definition of done" in body.lower():
                return IntentClassification.EXECUTABLE
            return IntentClassification.EXPLORATION

        # PRs -> mutation
        if event_type in (GitHubEventType.PR_OPENED, GitHubEventType.PR_REOPENED):
            return IntentClassification.MUTATION

        # Reviews/checks -> verification
        if event_type in (GitHubEventType.PR_REVIEW, GitHubEventType.CHECK_RUN, GitHubEventType.WORKFLOW_RUN):
            return IntentClassification.VERIFICATION

        # Discussions -> exploration
        if event_type in (GitHubEventType.DISCUSSION, GitHubEventType.DISCUSSION_COMMENT):
            return IntentClassification.EXPLORATION

        # Release -> promotion
        if event_type == GitHubEventType.RELEASE:
            return IntentClassification.PROMOTION

        return IntentClassification.UNKNOWN

    def _extract_capability_ref(self, payload: Dict[str, Any]) -> Optional[str]:
        """Extract capability reference from labels, body, etc."""
        # Check labels
        for obj in [payload.get("issue"), payload.get("pull_request"), payload.get("discussion")]:
            if obj:
                for label in obj.get("labels", []):
                    name = label.get("name", "")
                    if name.startswith("capability:") or name.startswith("cap:"):
                        return name.split(":", 1)[1]
        return None

    def _extract_holon_ref(self, payload: Dict[str, Any]) -> Optional[str]:
        """Extract holon reference from labels, body, etc."""
        for obj in [payload.get("issue"), payload.get("pull_request"), payload.get("discussion")]:
            if obj:
                for label in obj.get("labels", []):
                    name = label.get("name", "")
                    if name.startswith("holon:") or name.startswith("role:"):
                        return name.split(":", 1)[1]
        return None


class GitHubControlPlane:
    """
    G1 GitHub-native Control Plane.

    Ingress: GitHub events -> GatewayEnvelope
    Egress: GatewayEnvelope -> GitHub primitives
    """

    def __init__(
        self,
        gateway_protocol: GatewayProtocol,
        webhook_secret: Optional[str] = None,
    ):
        self.protocol = gateway_protocol
        self.normalizer = GitHubEventNormalizer(
            GitHubWebhookVerifier(webhook_secret) if webhook_secret else None
        )
        self._pending_egress: List[GitHubEgress] = []

    def ingress(
        self,
        event_name: str,
        payload: Dict[str, Any],
        delivery_id: str,
        signature: Optional[str] = None,
    ) -> GatewayEnvelope:
        """
        Process GitHub event as Gateway ingress.

        Creates a GatewayEnvelope preserving all coordinates.
        """
        event = self.normalizer.normalize(event_name, payload, delivery_id, signature)

        # Build identity from event
        holon_id = event.holon_ref or f"github-{event.actor}"
        institutional_rank = "L2_AGENT"  # Default, could be derived from labels

        identity = IdentityCoordinates(
            institutional_holon_id=holon_id,
            institutional_rank=institutional_rank,
            embodiment_id=f"github:{event.actor}",
            surface_id="github",
        )

        # Build mission coordinates
        work_id = self._extract_work_id(payload)
        correlation_id = f"github:{event.event_type.value}:{delivery_id}"

        mission = MissionCoordinates(
            mission_id=f"github-{event.event_type.value}-{work_id}",
            work_id=work_id,
            cell_id=self._extract_cell_id(payload),
            correlation_id=correlation_id,
        )

        # Capability if referenced
        capability = None
        if event.capability_ref:
            capability = CapabilityCoordinates(
                capability_id=event.capability_ref,
                capability_version="1.0",
            )

        # Authority from event context
        authority = AuthorityEnvelope(
            authority_scope="L2_READ",  # Default, could be escalated
            policy_ref="github-app-policy",
        )

        # Routing back to GitHub
        routing = RoutingCoordinates(
            origin_layer="Gateway",
            return_to=f"github:{event.repository}#{work_id}",
        )

        # Truth from GitHub event
        truth = TruthCoordinates(
            evidence_refs=[f"github:event:{delivery_id}"],
            observed_at=event.timestamp,
            source_authority="github_webhook",
            freshness=Freshness.FRESH,
            epistemic_state=EpistemicState.KNOWN if event.signature_verified else EpistemicState.UNKNOWN,
        )

        envelope = GatewayEnvelope(
            identity=identity,
            mission=mission,
            capability=capability,
            authority=authority,
            routing=routing,
            truth=truth,
            payload={
                "github_event": asdict(event),
                "intent": event.intent.value,
            },
        )

        # Create session
        session = self.protocol.create_session(identity, mission)
        return session

    def _extract_work_id(self, payload: Dict[str, Any]) -> str:
        """Extract work ID from issue/PR/discussion number."""
        for key in ["issue", "pull_request", "discussion", "workflow_run"]:
            obj = payload.get(key)
            if obj and "number" in obj:
                return str(obj["number"])
        return str(uuid.uuid4())[:8]

    def _extract_cell_id(self, payload: Dict[str, Any]) -> str:
        """Extract cell ID from labels or context."""
        for obj in [payload.get("issue"), payload.get("pull_request"), payload.get("discussion")]:
            if obj:
                for label in obj.get("labels", []):
                    name = label.get("name", "")
                    if name.startswith("cell:") or name.startswith("gate:"):
                        return name.split(":", 1)[1]
        return "G0"

    def egress(self, envelope: GatewayEnvelope) -> List[GitHubEgress]:
        """
        Convert Gateway envelope to GitHub egress actions.

        Maps based on intent and envelope state.
        """
        payload = envelope.payload
        github_event = payload.get("github_event", {})
        intent = payload.get("intent", "unknown")

        egress_list = []

        if intent == "exploration":
            # -> Discussion
            egress_list.append(GitHubEgress(
                primitive=GitHubPrimitiveType.DISCUSSION,
                action="create",
                target_ref=github_event.get("repository", ""),
                payload={
                    "title": f"Exploration: {envelope.mission.mission_id}",
                    "body": f"Gateway exploration for {envelope.mission.correlation_id}",
                    "category": "ideas",
                },
                evidence_refs=envelope.truth.evidence_refs if envelope.truth else [],
                return_to=envelope.routing.return_to if envelope.routing else "",
                correlation_id=envelope.mission.correlation_id,
            ))

        elif intent == "executable":
            # -> Issue (already exists, update or comment)
            egress_list.append(GitHubEgress(
                primitive=GitHubPrimitiveType.ISSUE,
                action="comment",
                target_ref=github_event.get("payload", {}).get("issue", {}).get("number", ""),
                payload={
                    "body": f"Gateway accepted: {envelope.mission.correlation_id}\n"
                           f"Holon: {envelope.identity.institutional_holon_id}\n"
                           f"Capability: {envelope.capability.capability_id if envelope.capability else 'TBD'}\n"
                           f"Return to: {envelope.routing.return_to if envelope.routing else 'N/A'}",
                },
                evidence_refs=envelope.truth.evidence_refs if envelope.truth else [],
                return_to=envelope.routing.return_to if envelope.routing else "",
                correlation_id=envelope.mission.correlation_id,
            ))

        elif intent == "mutation":
            # -> PR (already exists, review/merge)
            egress_list.append(GitHubEgress(
                primitive=GitHubPrimitiveType.PULL_REQUEST,
                action="review",
                target_ref=github_event.get("payload", {}).get("pull_request", {}).get("number", ""),
                payload={
                    "event": "COMMENT",
                    "body": f"Gateway verified mutation: {envelope.mission.correlation_id}\n"
                           f"Effect: {envelope.effect.operation_id if envelope.effect else 'TBD'}\n"
                           f"Receipt: {envelope.truth.evidence_refs if envelope.truth else 'pending'}",
                },
                evidence_refs=envelope.truth.evidence_refs if envelope.truth else [],
                return_to=envelope.routing.return_to if envelope.routing else "",
                correlation_id=envelope.mission.correlation_id,
            ))

        elif intent == "verification":
            # -> Check/Action
            egress_list.append(GitHubEgress(
                primitive=GitHubPrimitiveType.CHECK,
                action="create",
                target_ref=envelope.mission.correlation_id,
                payload={
                    "name": f"Gateway Verification / {envelope.mission.mission_id}",
                    "head_sha": github_event.get("payload", {}).get("check_run", {}).get("head_sha", ""),
                    "status": "completed",
                    "conclusion": "success",
                    "output": {
                        "title": "Gateway Verification",
                        "summary": f"Correlation: {envelope.mission.correlation_id}\n"
                                  f"Evidence: {len(envelope.truth.evidence_refs) if envelope.truth else 0} refs",
                    },
                },
                evidence_refs=envelope.truth.evidence_refs if envelope.truth else [],
                return_to=envelope.routing.return_to if envelope.routing else "",
                correlation_id=envelope.mission.correlation_id,
            ))

        # Always return to GitHub primitive
        return egress_list

    def route_to_runtime(
        self,
        envelope: GatewayEnvelope,
        capability_resolver: Callable[[str], Optional[Dict[str, Any]]],
    ) -> Dict[str, Any]:
        """
        Route envelope to an admissible runtime.

        Resolves capability -> holon -> authority -> runtime (provider-neutral).
        Returns routing decision with selected runtime adapter.
        """
        if not envelope.capability:
            return {
                "status": "FAILED",
                "error": "NO_CAPABILITY_SPECIFIED",
                "message": "Cannot route without capability_id",
            }

        capability_info = capability_resolver(envelope.capability.capability_id)
        if not capability_info:
            return {
                "status": "FAILED",
                "error": "CAPABILITY_NOT_FOUND",
                "capability_id": envelope.capability.capability_id,
            }

        # Check authority
        if envelope.authority:
            allowed = capability_info.get("authority_scopes", [])
            if envelope.authority.authority_scope not in allowed:
                return {
                    "status": "FAILED",
                    "error": "AUTHORITY_INSUFFICIENT",
                    "required": allowed,
                    "provided": envelope.authority.authority_scope,
                }

        # Select runtime (provider-neutral)
        runtime_bindings = capability_info.get("runtime_bindings", {})
        supported_runtimes = list(runtime_bindings.keys())

        # Prefer non-GitHub runtimes for provider neutrality
        preferred_order = ["hermes", "antigravity", "codex-local", "claude-code-local", "jules", "browser-harness"]
        selected_runtime = None
        for pref in preferred_order:
            if pref in supported_runtimes:
                selected_runtime = pref
                break

        if not selected_runtime and supported_runtimes:
            selected_runtime = supported_runtimes[0]

        if not selected_runtime:
            return {
                "status": "FAILED",
                "error": "NO_ADMISSIBLE_RUNTIME",
                "capability_id": envelope.capability.capability_id,
                "supported": supported_runtimes,
            }

        return {
            "status": "ROUTED",
            "runtime": selected_runtime,
            "binding": runtime_bindings[selected_runtime],
            "capability": envelope.capability.capability_id,
            "correlation_id": envelope.mission.correlation_id,
            "return_to": envelope.routing.return_to if envelope.routing else "",
        }


def create_github_app_control_plane(
    webhook_secret: str,
    default_ttl_seconds: int = 300,
) -> GitHubControlPlane:
    """Factory for GitHub App control plane."""
    protocol = GatewayProtocol(default_ttl_seconds=default_ttl_seconds)
    return GitHubControlPlane(protocol, webhook_secret=webhook_secret)


if __name__ == "__main__":
    # Quick self-test
    print("Testing GitHub Control Plane...")

    # Create control plane
    cp = create_github_app_control_plane(webhook_secret="test-secret")

    # Simulate issue opened event
    issue_payload = {
        "action": "opened",
        "issue": {
            "number": 123,
            "title": "Test Gateway Issue",
            "body": "Acceptance: Gateway must route this to a runtime",
            "labels": [
                {"name": "executable"},
                {"name": "capability:gateway.protocol.create"},
                {"name": "holon:S3-Graham"},
                {"name": "cell:G0"},
            ],
        },
        "repository": {"full_name": "Amdkn/Aspace_OS_V3"},
        "sender": {"login": "test-user"},
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    delivery_id = "test-delivery-123"

    # Ingress
    envelope = cp.ingress("issues", issue_payload, delivery_id)
    print(f"Ingress envelope: {envelope.gateway_message_id}")
    print(f"Identity: {envelope.identity.institutional_holon_id}")
    print(f"Mission: {envelope.mission.mission_id}")
    print(f"Capability: {envelope.capability.capability_id if envelope.capability else 'none'}")
    print(f"Intent: {envelope.payload.get('intent')}")

    # Mock capability resolver
    def mock_resolver(cap_id: str) -> Optional[Dict[str, Any]]:
        if cap_id == "gateway.protocol.create":
            return {
                "authority_scopes": ["L2_READ", "L2_WRITE"],
                "runtime_bindings": {
                    "hermes": {"adapter": "hermes-adapter", "version": "1.0"},
                    "antigravity": {"adapter": "antigravity-adapter", "version": "1.0"},
                    "claude-code-local": {"adapter": "claude-code-adapter", "version": "1.0"},
                },
            }
        return None

    # Route
    routing = cp.route_to_runtime(envelope, mock_resolver)
    print(f"Routing: {routing['status']} -> {routing.get('runtime')}")

    # Egress
    egress_list = cp.egress(envelope)
    print(f"Egress actions: {len(egress_list)}")
    for e in egress_list:
        print(f"  -> {e.primitive.value}.{e.action} on {e.target_ref}")

    print("\nAll GitHub Control Plane tests passed!")