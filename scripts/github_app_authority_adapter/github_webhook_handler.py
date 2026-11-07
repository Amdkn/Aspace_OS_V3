#!/usr/bin/env python3
"""
A'Space Gateway GitHub Webhook Handler

This is the Gateway GitHubAdapter that processes incoming GitHub webhook events.
It enforces the authority boundary between installation tokens and user tokens,
verifies webhook signatures, and dispatches events through the AuthorityResolver.

Per ASPACE_GITHUB_APP_AUTHORITY_ADAPTER_V0.md and #555 acceptance criteria.
"""

import json
import hashlib
import hmac
import os
from typing import Optional, Dict, Any, Set
from datetime import datetime, timezone

import sys
import os
from pathlib import Path

# Use absolute imports since this may be run directly
sys.path.insert(0, os.path.dirname(__file__))

from github_authority_resolver import (
    AuthorityResolver,
    GitHubAppContext,
    normalize_event_type,
    verify_hmac_signature,
    create_resolver_from_webhook
)


class GitHubWebhookHandler:
    """
    Handles incoming GitHub webhook events for the A'Space Gateway.

    Responsibilities:
    1. Verify webhook signature (HMAC SHA-256)
    2. Verify delivery ID dedupe
    3. Normalize event type into typed ingress
    4. Resolve authority (installation vs user token)
    5. Dispatch through AuthorityResolver
    6. Return evidence + return_to for the InterFabricEnvelope
    """

    def __init__(self, webhook_secret_path: str = ".gh_app_webhook_secret"):
        self.webhook_secret_path = webhook_secret_path
        self.webhook_secret = self._load_webhook_secret()
        self._delivery_seen: Set[str] = set()
        # In production, this would be persisted across restarts

    def _load_webhook_secret(self) -> str:
        """Load the webhook secret from secure storage."""
        secret_path = Path(self.webhook_secret_path)
        if secret_path.exists():
            return secret_path.read_text(encoding="utf-8").strip()
        # Generate a new one if none exists (for canary)
        import secrets
        new_secret = secrets.token_urlsafe(32)
        secret_path.write_text(new_secret, encoding="utf-8")
        os.chmod(str(secret_path), 0o600)
        return new_secret

    def verify_and_resolve(
        self,
        payload: bytes,
        signature: str,
        headers: Dict[str, str],
        granted_permissions: Set[str]
    ) -> Optional[Dict[str, Any]]:
        """
        Verify a webhook event and resolve the authority decision.

        Returns an evidence package if verification and resolution succeed,
        or None if verification fails.
        """
        # 1. Verify HMAC SHA-256 signature
        sig_valid = verify_hmac_signature(self.webhook_secret, payload, signature)
        if not sig_valid:
            print("FAIL: Webhook signature verification failed")
            return None

        # 2. Verify delivery ID dedupe
        delivery_id = headers.get("X-GitHub-Delivery", "")
        if delivery_id in self._delivery_seen:
            print(f"INFO: Duplicate delivery ID {delivery_id} - idempotently absorbed")
            return {"duplicate": True, "delivery_id": delivery_id}
        self._delivery_seen.add(delivery_id)

        # 3. Normalize event type
        event_type = headers.get("X-GitHub-Event", "")
        normalized = normalize_event_type(event_type)
        print(f"Event: {event_type} -> {normalized}")

        # 4. Parse payload
        try:
            event_data = json.loads(payload)
        except json.JSONDecodeError:
            print("FAIL: Could not parse webhook payload")
            return None

        # 5. Create AuthorityResolver and resolve
        # Extract context from the event
        repo_full_name = event_data.get("repository", {}).get("full_name", "")
        sender_login = event_data.get("sender", {}).get("login", None)

        # We need the delivery_id for the resolver context
        # But the resolver's delivery_seen is separate from ours
        # For now, create a minimal resolver
        try:
            resolver = AuthorityResolver.__new__(AuthorityResolver)
            # Manually set the delivery_seen and other attributes
            resolver._delivery_seen = self._delivery_seen
            resolver.granted_permissions = granted_permissions

            # Build context - simplified
            context = GitHubAppContext(
                delivery_id=delivery_id,
                event_type=normalized,
                repository_full_name=repo_full_name,
                sender_login=sender_login,
                installation_id=None,  # Would be extracted from installation event
                authorizations=granted_permissions
            )
            # Store context on resolver for resolve_authority
            resolver.context = context

            # Resolve authority
            decision = resolver.resolve_authority()

            # Build evidence package
            evidence = {
                "delivery_id": delivery_id,
                "event_type": normalized,
                "signature_valid": True,
                "authority_decision": {
                    "use_installation_token": decision.use_installation_token,
                    "use_user_token": decision.use_user_token,
                    "scope": decision.scope,
                    "reason": decision.reason,
                    "permitted_endpoints": list(decision.permitted_endpoints),
                },
                "received_at": datetime.now(timezone.utc).isoformat(),
                "repository": repo_full_name,
            }

            print(f"Authority resolved: scope={decision.scope}")
            print(f"  Use installation token: {decision.use_installation_token}")
            print(f"  Use user token: {decision.use_user_token}")
            print(f"  Reason: {decision.reason}")

            return evidence

        except Exception as e:
            print(f"FAIL: Authority resolution error: {e}")
            import traceback
            traceback.print_exc()
            return None

    def process_issue_event(
        self,
        payload: dict,
        granted_permissions: Set[str]
    ) -> Optional[Dict[str, Any]]:
        """Process a GitHub Issues webhook event."""
        return self.verify_and_resolve(
            json.dumps(payload).encode(),
            "",  # signature would come from HTTP headers
            {},  # headers would come from HTTP request
            granted_permissions
        )

    def process_pull_request_event(
        self,
        payload: dict,
        granted_permissions: Set[str]
    ) -> Optional[Dict[str, Any]]:
        """Process a GitHub Pull Request webhook event."""
        # For PR events, we need to check if they're in the installed repo
        # or targeting user scope
        event_type = payload.get("action", "")
        return self.verify_and_resolve(
            json.dumps(payload).encode(),
            "",  # signature
            {},  # headers
            granted_permissions
        )

    def generate_return_to(
        self,
        decision: Any,
        correlation_id: str,
        evidence_refs: list
    ) -> Dict[str, Any]:
        """
        Generate the return_to routing for the InterFabricEnvelope.

        Per the InterFabricEnvelope schema, every effect carries return_to
        routing information to ensure proper回流 (return routing).
        """
        return {
            "origin_layer": "github_webhook_handler",
            "return_to": f"github: authority resolution for {correlation_id}",
            "correlation_id": correlation_id,
            "evidence_refs": evidence_refs,
            "authority_scope": decision.scope if hasattr(decision, 'scope') else "unknown",
            "resolution_reason": decision.reason if hasattr(decision, 'reason') else "",
        }


def test_webhook_handler():
    """Test the webhook handler with a sample issue event."""
    print("=" * 60)
    print("Testing GitHub Webhook Handler")
    print("=" * 60)

    handler = GitHubWebhookHandler()

    # Simulate an issue opened event
    test_payload = {
        "action": "opened",
        "issue": {
            "number": 555,
            "title": "[P0][GATEWAY] Authority adapter canary test",
            "body": "Testing the GitHub App authority adapter per issue #555",
        },
        "repository": {
            "id": 168081230,
            "name": "Aspace_OS_V3",
            "full_name": "Amdkn/Aspace_OS_V3",
            "owner": {"login": "Amdkn", "id": 12345},
        },
        "sender": {"login": "test-user", "id": 67890},
    }

    test_body = json.dumps(test_payload).encode()

    # Generate expected signature
    secret = handler.webhook_secret
    sig = f"sha256={hmac.new(
        secret.encode('utf-8'),
        test_body,
        hashlib.sha256
    ).hexdigest()}"

    test_headers = {
        "X-Hub-Signature-256": sig,
        "X-GitHub-Delivery": f"test-delivery-{int(__import__('time').time())}",
        "X-GitHub-Event": "issues",
    }

    print("\n--- Processing issue opened event ---")
    evidence = handler.verify_and_resolve(
        test_body,
        sig,
        test_headers,
        {"issues", "contents", "pull_requests"}  # Gateway default permissions
    )

    if evidence:
        print(f"\n✓ Event processed successfully")
        print(f"  Delivery ID: {evidence['delivery_id']}")
        print(f"  Event type: {evidence['event_type']}")
        decision = evidence['authority_decision']
        print(f"  Authority scope: {decision['scope']}")
        print(f"  Use installation token: {decision['use_installation_token']}")
        print(f"  Permitted endpoints: {decision['permitted_endpoints']}")

        # Generate return_to
        return_to = handler.generate_return_to(
            decision,
            evidence['delivery_id'],
            evidence['event_type']
        )
        print(f"  Return_to: {return_to['return_to']}")
    else:
        print("\n✗ Event processing failed")


if __name__ == "__main__":
    test_webhook_handler()