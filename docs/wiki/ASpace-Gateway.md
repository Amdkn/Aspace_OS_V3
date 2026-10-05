# A'Space Gateway

Mission: [#542](https://github.com/Amdkn/Aspace_OS_V3/issues/542)

A'Space Gateway is the **federated membrane** connecting holons, embodiments, runtimes, surfaces and fabrics.

It owns:

- connectivity;
- protocol negotiation;
- presence projection;
- durable session lineage;
- reconnect/resume;
- delivery semantics;
- surface federation.

It does **not** own institutional cognition, business authority, WorkGraph truth, capability semantics or machine-effect truth.

## Gates

- #543 — Protocol Core + identity/presence/session
- #544 — GitHub-native control plane
- #545 — runtime + surface federation
- #546 — sovereign canary

## Existing fabrics reused

- Capability Fabric — #333
- InterFabricEnvelope — #471
- Temporal Truth / Context Compiler — #448
- Embodied Holons — #318
- Reflex Fabric — #484
- RecoveryPort / Donna — #485

## Golden invariant

A runtime may die and a surface may disconnect; the institutional holon, work/correlation identity, authority, evidence lineage and return_to must survive.


## GitHub App authority adapter

GitHub is split into explicit authority planes:

- **App installation token** → repository-native machine authority;
- **App user access token** → user-scoped authority where GitHub exposes it;
- **signed webhooks** → event ingress.

The App is an adapter, not an agent identity. A GitHub event still resolves capability → holon → authority → runtime.

Canonical contract: `docs/governance/ASPACE_GITHUB_APP_AUTHORITY_ADAPTER_V0.md`  
Implementation cell: #555.
