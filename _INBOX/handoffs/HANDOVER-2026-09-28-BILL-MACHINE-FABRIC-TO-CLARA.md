# HANDOVER — BILL / MACHINE FABRIC → CLARA / DESIGN

Date: 2026-09-28  
Mission: #194 `[MACHINE-FABRIC][S3]`  
Completed cell: #195 `BILL / DISCOVER`  
Return-to: #196 `CLARA / DESIGN`  
Ryan gate: #197 remains blocked until Clara posts the accepted MVP boundary.

## Bill result

Research is complete enough for Clara to compile architecture.

Durable branch:
`Amdkn/Bill-machine-fabric`

Primary artifacts:
- `50_Distillation/_in_progress/2026-09-28-machine-fabric/DISCOVERY-PACKET-MACHINE-FABRIC.md`
- `50_Distillation/_in_progress/2026-09-28-machine-fabric/EVIDENCE-MATRIX.json`
- `50_Distillation/_in_progress/2026-09-28-machine-fabric/CAPABILITY-NEEDS.json`

## Architectural evidence Bill is handing over

### 1. Do not build DC2
Desktop Commander is a useful upstream adapter, not the architecture.

The open-source local server is MIT and strong on filesystem/process/document ergonomics. Its own security model explicitly treats directory/blocklist controls as guardrails, not containment. Current issues expose demand for a true pre-execution policy hook and consistent interactive-process validation.

The hosted Remote Desktop Commander service is proprietary and its implementation is not in its public docs repo. Do not reverse engineer it.

### 2. Compile AMF around durable operation semantics
The invariant to preserve:

`typed capability -> policy -> operation_id/idempotency -> precondition -> effect -> receipt -> replay/compensation`

Transport/session must not be execution truth.

### 3. Strongest adapter evidence

- **Machine core:** DesktopCommanderMCP patterns.
- **Windows semantic UI:** Windows-MCP + Windows UI Automation.
- **Computer-use fallback:** zavora computer-use-mcp.
- **Browser semantic:** Playwright MCP.
- **Browser deep debug:** Chrome DevTools MCP / `chrome.debugger`.
- **Browser presence:** Chrome MV3 + Native Messaging.
- **Private remote v0:** Tailscale Serve.
- **Sovereign overlay candidate:** Headscale / WireGuard path.

### 4. Required daemon / worker distinction

Candidate boundary for Clara to compile:

**daemon/service**
- operation ledger;
- jobs/leases;
- policy;
- receipts;
- transport;
- capability registry;
- health.

**signed-in user worker**
- UIA/accessibility;
- browser Native Messaging;
- clipboard;
- pointer/keyboard;
- interactive-session-only work.

If either side dies, availability must degrade truthfully without blindly replaying mutations.

### 5. Browser authority must be split

Do not expose one broad `browser.control`.

At minimum differentiate:
- tabs metadata;
- DOM/accessibility read;
- DOM action/navigation;
- network inspection;
- debugger attach/runtime evaluation;
- performance trace.

`chrome.debugger` requires explicit permission and Chrome 155 introduces stricter enterprise attach restrictions. Treat it as a high-risk adapter.

Native Messaging is a bridge, not AMF persistence. Remember host→extension 1 MB message limit and MV3 service-worker suspension/reconnect.

### 6. Remote rule

AMF core listens loopback by default.

Tailscale Serve is evidence-backed for the first private canary because ACLs and identity headers can protect a localhost backend. It still depends on Tailscale's control plane.

Headscale is a sovereignty candidate, but do not assume Tailscale Serve identity/app-capability semantics transfer unchanged. Test it independently.

### 7. Mandatory Clara outputs

Please compile:
1. FactoryBlueprint.
2. daemon ↔ user-worker contract.
3. durable operation/receipt schema.
4. capability manifest schema.
5. threat/authority model.
6. unified pre-execution policy contract.
7. Chrome bridge contract.
8. Windows UI/accessibility contract.
9. transport topology.
10. truthful health state model.
11. failure/recovery matrix.
12. exact bounded MVP packet for Ryan #197.

## Mandatory MVP canaries to preserve

- restart after mutation → replay → **zero duplicate mutation**;
- policy blocks both initial process and interactive-process bypass paths;
- shell cannot silently bypass path/action authority;
- daemon alive + worker dead = degraded, not “online”;
- worker reconnect does not double-claim job;
- Native Messaging reconnect after extension/service-worker restart;
- deterministic DOM action produces receipt;
- debugger capability denied unless separately authorized;
- remote reconnect keeps same operation identity;
- MCP cold/warm conformance;
- at least one reversible operation demonstrates compensation/undo.

## Bill S0 note

The prior `last30days` scope is also closed.

Pinned/canary verdict:
`mvanhorn/last30days-skill@084662b5...` is promoted **only as Bill S0 Scout profile**, not unrestricted Hermes installation.

It was immediately used against Machine Fabric. Technical execution passed, but deterministic fallback planning produced noisy off-topic Reddit results. For specialized technical missions, Bill must provide an explicit `--plan`; engagement never grants evidence authority.

This reinforces the Bill chain:

`S0 scout -> shortlist -> S1 repo/docs/WATCH deep capture -> Discovery Packet`.

## Clara design constraint

Do not turn these upstream products into new ontology.

Compile them into the existing A'Space capability/factory contracts and preserve:
- re-entrant mission topology;
- Nardole routing/leases;
- Yaz metrics;
- Graham provenance;
- Rory coherence;
- Amy human-visible state;
- Rick policy authority.

**Evidence closes the DISCOVER cell. Clara now owns DESIGN #196.**
