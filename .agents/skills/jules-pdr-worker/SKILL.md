---
name: jules-pdr-worker
description: Delegate code-heavy bounded PDRs to Jules, then independently verify and integrate the result.
---
# Jules PDR Worker
Use Jules only with explicit repo boundary and acceptance.
One Jules session = one bounded PDR. Prefer configured Jules MCP when available.
Jules output is a proposal, never automatic promotion. Integrator verifies diff/tests/security; Yaz independently observes where required; Graham records evidence.
Failure returns to the Doctor as evidence, never to A0 as technician work.
