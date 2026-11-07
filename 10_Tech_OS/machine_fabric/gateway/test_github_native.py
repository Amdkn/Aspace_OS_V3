#!/usr/bin/env python3
"""Tests for the GitHub-native control-plane membrane (issue #544).

Covers:
- Webhook HMAC-SHA256 signature verification (#544 security).
- Delivery-ID deduplication (no double-processing same event).
- Ingress normalisation: issues, PRs, checks, discussions, releases.
- InterFabricEnvelope creation with correct invariants (#471).
- Provider-neutral dedup key (dispatch survives runtime swap).
- No-blind-retry guard on UNKNOWN state (#544 reliability).
- Fencing token stale-writer rejection.
- Egress primitive mapping (ingress-event -> GitHub primitive).
"""

import copy
import hashlib
import hmac
import json
import unittest
from datetime import datetime, timezone
from pathlib import Path

# Resolve inter_fabric relative to this module's parent.
_GATEWAY_DIR = Path(__file__).resolve().parent
_KERNEL_DIR = _GATEWAY_DIR.parent.parent  # 10_Tech_OS/kernel

# Ensure inter_fabric is importable.
_import_path = _GATEWAY_DIR.parent  # 10_Tech_OS/machine_fabric
if str(_import_path) not in __import__("sys").path:
    __import__("sys").path.insert(0, str(_import_path))
_kernel_path = _GATEWAY_DIR.parent.parent  # 10_Tech_OS/kernel
if str(_kernel_path) not in __import__("sys").path:
    __import__("sys").path.insert(0, str(_kernel_path))

from github_native import (
    DeliveryDeduper,
    DeliveryDuplicateError,
    DeliveryTimeoutError,
    GitHubEgressAdapter,
    GitHubEvent,
    GitHubIngressNormalizer,
    GHEventType,
    GHPrimitive,
    GHResult,
    ProviderResolver,
    SignatureVerificationError,
    UnknownStateGuard,
    derive_fencing_token,
    derive_provider_neutral_dedup_key,
    github_ingress_to_egress,
    verify_signature,
    verify_signature_raw,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_signature(payload: dict, secret: str) -> str:
    body = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode()
    return hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()


def _sample_issue_event(action: str = "opened") -> dict:
    return {
        "action": action,
        "repository": {
            "owner": {"login": "Amdkn"},
            "name": "Aspace_OS_V3",
        },
        "installation": {"id": 42},
        "sender": {"login": "S3-rider", "type": "User"},
        "issue": {
            "number": 544,
            "title": "[P0][GATEWAY] GitHub-native control plane",
            "body": "Make GitHub a native control plane",
        },
        "hook": {"type": "issues"},
    }


def _sample_pr_event(action: str = "opened") -> dict:
    return {
        "action": action,
        "repository": {"owner": {"login": "Amdkn"}, "name": "Aspace_OS_V3"},
        "installation": {"id": 42},
        "sender": {"login": "S3-ryan", "type": "User"},
        "number": 123,
        "pull_request": {"number": 123},
        "hook": {"type": "pull_request"},
    }


def _sample_check_run_event(status: str = "completed") -> dict:
    return {
        "action": status,
        "repository": {"owner": {"login": "Amdkn"}, "name": "Aspace_OS_V3"},
        "installation": {"id": 42},
        "sender": {"login": "GitHubActions", "type": "Bot"},
        "check_run": {
            "name": "CI / tests",
            "status": status,
            "conclusion": "success" if status == "completed" else None,
        },
        "hook": {"type": "check_run"},
    }


def _sample_discussion_event(action: str = "created", promoted: bool = False) -> dict:
    return {
        "action": action,
        "repository": {"owner": {"login": "Amdkn"}, "name": "Aspace_OS_V3"},
        "installation": {"id": 42},
        "sender": {"login": "clara", "type": "User"},
        "discussion": {"url": "https://github.com/Amdkn/Aspace_OS_V3/discussions/550", "_aspace_promoted": promoted},
        "hook": {"type": "discussion"},
    }


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestSignatureVerification(unittest.TestCase):
    def test_correct_signature_passes(self):
        payload = {"test": True}
        secret = "my-secret"
        body = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode()
        sig = hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()
        self.assertTrue(verify_signature(body, f"sha256={sig}", secret))

    def test_wrong_signature_raises(self):
        body = b"{'payload': 'tampered'}"
        self.assertRaises(
            SignatureVerificationError,
            verify_signature,
            body,
            "sha256-fakedfakedfakedfakedfakedfakedfakedfakedfakedfaked",
            "secret",
        )

    def test_missing_signature_raises(self):
        body = b"{}"
        self.assertRaises(
            SignatureVerificationError, verify_signature, body, "", "secret"
        )

    def test_verify_signature_raw_string(self):
        payload = {"a": 1}
        secret = "s"
        body_str = json.dumps(payload, separators=(",", ":"), sort_keys=True)
        sig = hmac.new(secret.encode(), body_str.encode(), hashlib.sha256).hexdigest()
        self.assertTrue(
            verify_signature_raw(body_str, f"sha256={sig}", secret)
        )


class TestDeliveryDeduper(unittest.TestCase):
    def test_first_delivery_accepted(self):
        deduper = DeliveryDeduper()
        token = deduper.register("del-1", 1)
        self.assertIsInstance(token, int)

    def test_duplicate_raises(self):
        deduper = DeliveryDeduper()
        deduper.register("del-1", 1)
        with self.assertRaises(DeliveryDuplicateError):
            deduper.register("del-1", 2)

    def test_iss_delivered_flag(self):
        deduper = DeliveryDeduper()
        self.assertFalse(deduper.is_delivered("del-1"))
        deduper.register("del-1", 1)
        deduper.complete("del-1", epistemic_state="SUCCEEDED")
        self.assertTrue(deduper.is_delivered("del-1"))

    def test_non_unknown_delivery_not_frozen(self):
        deduper = DeliveryDeduper()
        deduper.register("del-1", 1)
        deduper.complete("del-1", epistemic_state="SUCCEEDED")
        # SUCCEEDED deliveries are recorded, not frozen.
        self.assertIn("del-1", deduper._delivered)
        # Duplicate still raises.
        with self.assertRaises(DeliveryDuplicateError):
            deduper.register("del-1", 2)

    def test_stale_fencing_token_rejected(self):
        deduper = DeliveryDeduper()
        deduper.register("del-1", 100)
        # Lower token from stale writer should fail.
        with self.assertRaises(DeliveryTimeoutError):
            deduper.register("del-1", 50)
        # Higher token from new writer should succeed.
        self.assertEqual(deduper.register("del-1", 200), 200)

    def test_unknown_delivery_raises_on_retry(self):
        deduper = DeliveryDeduper()
        deduper.register("del-1", 1)
        deduper.complete("del-1", epistemic_state="UNKNOWN")
        with self.assertRaises(DeliveryTimeoutError):
            deduper.register("del-1", 2)


class TestFencingToken(unittest.TestCase):
    def test_deterministic(self):
        t1 = derive_fencing_token("same-id")
        t2 = derive_fencing_token("same-id")
        self.assertEqual(t1, t2)

    def test_different_ids_different_tokens(self):
        self.assertNotEqual(
            derive_fencing_token("id-a"),
            derive_fencing_token("id-b"),
        )


class TestGitHubIngressNormalizer(unittest.TestCase):
    def test_normalize_issue_event(self):
        payload = _sample_issue_event("opened")
        secret = "s"
        sig = f"sha256={_make_signature(payload, secret)}"
        n = GitHubIngressNormalizer()
        event = n.normalize(payload, "del-1", secret_sha=sig, webhook_secret=secret)

        self.assertEqual(event.event_type, GHEventType.ISSUE)
        self.assertEqual(event.action, "opened")
        self.assertEqual(event.delivery_id, "del-1")
        self.assertEqual(event.repository, "Amdkn/Aspace_OS_V3")
        self.assertEqual(event.installation_id, 42)
        self.assertEqual(event.sender, "S3-rider")
        self.assertEqual(event.sender_type, "User")
        self.assertEqual(event.issue_number, 544)
        self.assertEqual(event.pull_request_number, None)

    def test_normalize_pr_event(self):
        payload = _sample_pr_event("synchronize")
        sig = f"sha256={_make_signature(payload, 's')}"
        n = GitHubIngressNormalizer()
        event = n.normalize(payload, "d2", secret_sha=sig, webhook_secret="s")
        self.assertEqual(event.event_type, GHEventType.PULL_REQUEST)
        self.assertEqual(event.pull_request_number, 123)

    def test_normalize_check_run_event(self):
        payload = _sample_check_run_event("completed")
        sig = f"sha256={_make_signature(payload, 's')}"
        n = GitHubIngressNormalizer()
        event = n.normalize(payload, "d3", secret_sha=sig, webhook_secret="s")
        self.assertEqual(event.event_type, GHEventType.CHECK_RUN)
        self.assertEqual(event.check_status, "completed")

    def test_normalize_discussion_event(self):
        payload = _sample_discussion_event(promoted=True)
        sig = f"sha256={_make_signature(payload, 's')}"
        n = GitHubIngressNormalizer()
        event = n.normalize(payload, "d4", secret_sha=sig, webhook_secret="s")
        self.assertEqual(event.event_type, GHEventType.DISCUSSION)
        self.assertTrue(event.promoted)
        self.assertIsNotNone(event.discussion_url)

    def test_event_to_ingress_dict_validates_schema(self):
        n = GitHubIngressNormalizer()
        payload = _sample_issue_event()
        sig = f"sha256={_make_signature(payload, 's')}"
        event = n.normalize(payload, "d-schema", secret_sha=sig, webhook_secret="s")
        ingress = n.event_to_ingress_dict(event)
        self.assertIn("fingerprint", ingress)
        self.assertIn("normalized_at", ingress)
        self.assertEqual(ingress["event_type"], "issues")

    def test_signature_check_on_normalize(self):
        payload = _sample_issue_event()
        # Wrong signature should raise.
        n = GitHubIngressNormalizer()
        with self.assertRaises(SignatureVerificationError):
            n.normalize(payload, "d-bad", secret_sha="sha256-wrong", webhook_secret="s")


class TestGitHubEgressAdapter(unittest.TestCase):
    def setUp(self):
        self.egress = GitHubEgressAdapter()

    def _event(self, event_type: GHEventType):
        return GitHubEvent(
            event_type=event_type,
            action="opened",
            delivery_id="d0",
            repository="Amdkn/Aspace_OS_V3",
            installation_id=42,
            sender="S3-test",
            sender_type="User",
            issue_number=544,
        )

    def test_issue_maps_to_issue(self):
        r = self.egress.build_result(self._event(GHEventType.ISSUE), holon_id="Test")
        self.assertEqual(r.primitive, GHPrimitive.ISSUE)

    def test_pr_maps_to_pr(self):
        r = self.egress.build_result(self._event(GHEventType.PULL_REQUEST), holon_id="Test")
        self.assertEqual(r.primitive, GHPrimitive.PULL_REQUEST)

    def test_check_runs_map_to_check(self):
        r = self.egress.build_result(
            self._event(GHEventType.CHECK_RUN), holon_id="Test"
        )
        self.assertEqual(r.primitive, GHPrimitive.CHECK)

    def test_discussion_maps_to_discussion(self):
        r = self.egress.build_result(
            self._event(GHEventType.DISCUSSION), holon_id="Test"
        )
        self.assertEqual(r.primitive, GHPrimitive.DISCUSSION)

    def test_installation_maps_to_issue(self):
        r = self.egress.build_result(
            self._event(GHEventType.INSTALLATION), holon_id="Test"
        )
        self.assertEqual(r.primitive, GHPrimitive.ISSUE)

    def test_check_suite_and_workflow_run_map_to_check(self):
        for et in (GHEventType.CHECK_SUITE, GHEventType.WORKFLOW_RUN):
            r = self.egress.build_result(self._event(et), holon_id="Test")
            self.assertEqual(r.primitive, GHPrimitive.CHECK)

    def test_release_maps_to_release(self):
        r = self.egress.build_result(self._event(GHEventType.RELEASE), holon_id="Test")
        self.assertEqual(r.primitive, GHPrimitive.RELEASE)


class TestProviderNeutralDedup(unittest.TestCase):
    def test_dedup_key_does_not_depend_on_provider(self):
        from unittest.mock import MagicMock
        r1 = {
            "holon_id": "Ryan",
            "capability_id": "code.build",
            "capability_version": "1.0.0",
            "repository": "Amdkn/Aspace_OS_V3",
            "event_id": "d1",
            "return_to": "github:#544",
            "evidence_refs": ["e1"],
            "authoriser": "A0",
        }
        req1 = MagicMock()
        for k, v in r1.items():
            setattr(req1, k, v)
        key1 = derive_provider_neutral_dedup_key(req1)

        req2 = MagicMock()
        for k, v in r1.items():
            setattr(req2, k, v)
        req2.provider = "jules"
        key2 = derive_provider_neutral_dedup_key(req2)
        # Dedup key should be identical regardless of provider.
        self.assertEqual(key1, key2)


class TestUnknownStateGuard(unittest.TestCase):
    def test_unknown_frozens(self):
        guard = UnknownStateGuard()
        guard.record_unknown("d1", "runtime returned UNKNOWN")
        self.assertTrue(guard.is_frozen("d1"))

    def test_blank_recovery_rejected(self):
        guard = UnknownStateGuard()
        guard.record_unknown("d1", "reason")
        self.assertFalse(guard.resolve("d1", ""))

    def test_explicit_recovery_unfrozes(self):
        guard = UnknownStateGuard()
        guard.record_unknown("d1", "reason")
        self.assertTrue(guard.resolve("d1", "RETRY_WITH_HERMES"))
        self.assertFalse(guard.is_frozen("d1"))


class TestProviderResolver(unittest.TestCase):
    def test_resolve_returns_candidates(self):
        resolver = ProviderResolver()
        resolver.register_capability("code.build", [
            {"id": "hermes", "health": "available"},
            {"id": "codex", "health": "available"},
        ])
        candidates = resolver.resolve("code.build")
        self.assertEqual(candidates, ["hermes", "codex"])

    def test_unknown_capability_returns_empty(self):
        resolver = ProviderResolver()
        self.assertEqual(resolver.resolve("unknown.capability"), [])

    def test_dispatch_has_provider_neutral_dedup_key(self):
        resolver = ProviderResolver()
        event = GitHubEvent(
            event_type=GHEventType.ISSUE,
            action="opened",
            delivery_id="d-unique",
            repository="Amdkn/Aspace_OS_V3",
            installation_id=42,
            sender="S3-test",
            sender_type="User",
            issue_number=544,
        )
        dispatch = resolver.build_dispatch(
            event=event,
            holon_id="TestHolon",
            capability_id="code.build",
            return_to="github:#544",
            evidence_refs=["e1"],
            authoriser="A0",
        )
        self.assertEqual(dispatch.dedup_key, derive_provider_neutral_dedup_key(dispatch))


class TestEndToEnd(unittest.TestCase):
    """Acceptance test for #544: a GitHub Issue enters the Gateway."""

    def test_issue_ingressed_routed_returned(self):
        payload = _sample_issue_event("opened")
        secret = "canary-test-secret"
        sig = f"sha256={_make_signature(payload, secret)}"

        result = github_ingress_to_egress(
            raw_payload=payload,
            delivery_id="end-to-end-1",
            signature=sig,
            webhook_secret=secret,
            institution_id="Amdkn",
            holon_id="Buzz",
            return_to="github:Amdkn/Aspace_OS_V3",
            evidence_refs=["precondition:#542"],
        )

        # Egress primitive should be Issue for an Issue ingress.
        self.assertEqual(result.primitive, GHPrimitive.ISSUE)
        # Target should be the issue number.
        self.assertEqual(result.target_id, 544)
        # Owner should be the holon that produced it.
        self.assertEqual(result.owner, "Buzz")


if __name__ == "__main__":
    import sys
    sys.path.insert(0, '10_Tech_OS/machine_fabric/gateway')
    unittest.main(verbosity=2)