# Discovery Packet 06: Security in AI Coding / Deterministic Gates

## SourceClaim
Autonomous AI execution must be bounded by immutable deterministic security gates, sandboxes, and verification test suites to prevent hallucinated or malicious state mutations.

## Supporting evidence
- `10_Tech_OS/kernel/gate.py` & `portfolio_firewall.py` (A'Space deterministic security gates and portfolio firewall).
- `10_Tech_OS/kernel/truth_projection.py` enforcing provenance and freshness state verification.

## Contradictions / limits
- Deterministic gates can cause false positives or deadlocks if safety policies are too rigid for novel wargame scenarios.

## A'Space adaptation candidate
- Implement double-entry deterministic verification: automated test/lint passes + portfolio/provenance firewall checks before state merge.

## Anti-pattern / risk
- Relying on probabilistic AI self-reflection for safety checks instead of hard, non-bypassable deterministic code gates.

## Impacted holons
- **Clara (S3 Design):** Defines security policy specs.
- **Yaz (S3 Observe):** Monitors gate compliance and security incidents.
- **Ryan (S3 Build):** Integrates gate checks into CI/build pipelines.

## Candidate contract/ADR
- `ADR-312-DETERMINISTIC-SAFETY-GATES`: Mandates non-probabilistic hard gates for all production state mutations.

## Required test/canary
- `10_Tech_OS/kernel/test_truth_projection.py` & `10_Tech_OS/kernel/test_l0_kernel.py` validating security gate enforcement.

## Confidence
High (0.96)

## Provenance refs
- `10_Tech_OS/kernel/gate.py`
- `10_Tech_OS/kernel/portfolio_firewall.py`
- `10_Tech_OS/kernel/truth_projection.py`
