# Discovery Packet 09: GitHub-Native Swarm Software Factory

## SourceClaim
GitHub issues, pull requests, and webhooks serve as the native control plane and coordination ledger for distributed AI agent swarms.

## Supporting evidence
- `10_Tech_OS/kernel/dispatch_routing.py` & `mission_continuity.py` (GitHub-native mission routing and continuity in A'Space).
- `10_Tech_OS/kernel/webhooks/yas_alert_sink.py` (Webhook event handling and swarm notification).

## Contradictions / limits
- GitHub issue API rate limits and notification noise require local caching and structured event filtering to avoid swarm thrashing.

## A'Space adaptation candidate
- Use GitHub issues/PRs as the primary external audit trail and handoff mechanism, synchronized with local blackboard states (`aspace_machine_blackboard_v1`).

## Anti-pattern / risk
- Hardcoding agent logic into monolithic GitHub Actions workflows rather than keeping decision logic inside S3 holons.

## Impacted holons
- **Nardole (S3 Dispatch):** Dispatches GitHub issue tasks to appropriate holons.
- **River (S3 Flow):** Tracks PR lifecycle and automated merge flows.
- **Yaz (S3 Observe):** Monitors GitHub event webhooks and execution logs.

## Candidate contract/ADR
- `ADR-312-GITHUB-CONTROL-PLANE`: Establishes GitHub issues and webhooks as the canonical external coordination surface.

## Required test/canary
- `10_Tech_OS/kernel/test_dispatch_routing.py` verifying GitHub-native mission parsing and dispatch.

## Confidence
High (0.94)

## Provenance refs
- `10_Tech_OS/kernel/dispatch_routing.py`
- `10_Tech_OS/kernel/mission_continuity.py`
- `10_Tech_OS/kernel/webhooks/yas_alert_sink.py`
