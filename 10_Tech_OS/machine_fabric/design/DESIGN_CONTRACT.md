# A'Space Machine Fabric — Clara Design Contract v0.1

Mission: #194 · DESIGN cell: #196 · upstream evidence: Bill PR #199

## Decision

Do **not** build Desktop Commander 2.

AMF owns execution truth and durable semantics. DesktopCommanderMCP, Windows-MCP, Playwright, Chrome DevTools, computer-use and remote transports are adapters behind typed capabilities.

Core invariant:

`typed capability -> policy -> operation_id -> precondition -> effect -> durable receipt -> replay/compensation`

A transport disconnect, harness death, browser restart or user-session loss may change availability. It must never change whether a mutation already happened.

## Process boundary

### AMF daemon/service

Runs independently of the signed-in desktop session.

Owns:
- SQLite operation ledger and receipts;
- idempotency/fingerprint conflict detection;
- job claims, leases, retry/backoff and DLQ routing;
- pre-execution policy;
- capability registry and adapter health;
- local MCP Streamable HTTP and stdio compatibility;
- loopback listener;
- private remote transport adapter;
- receipt/provenance export.

The daemon **does not** own interactive desktop authority merely because it is alive.

### AMF user-session worker

Runs only inside an interactive signed-in Windows session.

Owns adapters that require user presence:
- Windows UI Automation / accessibility;
- browser Native Messaging presence;
- clipboard;
- pointer/keyboard;
- interactive process/UI operations.

Worker reconnect performs capability re-registration and lease reconciliation. It does not silently replay mutations.

## Capability surface

Capabilities are narrower than adapters.

Minimum names:
- `machine.fs.read`
- `machine.fs.write`
- `machine.fs.edit`
- `machine.fs.search`
- `machine.process.start`
- `machine.process.interact`
- `machine.process.read`
- `machine.process.stop`
- `machine.ui.inspect`
- `machine.ui.action`
- `browser.tabs.read`
- `browser.dom.read`
- `browser.dom.action`
- `browser.network.inspect`
- `browser.debugger.attach`
- `browser.runtime.evaluate`
- `browser.performance.trace`

Adapters advertise manifests. Policy grants authority to capabilities/actions, not to an adapter wholesale.

## Unified policy hook

Every consequential action reaches the same policy function before effect:

`PolicyRequest(operation_id, capability, action, authority, context) -> ALLOW | DENY | REQUIRE_APPROVAL`

This applies equally to:
- first process start;
- later interactive process input;
- filesystem mutation;
- shell-mediated file access;
- UIA action;
- DOM action;
- Native Messaging request;
- debugger/CDP attach.

An adapter cannot create a second ungoverned path around policy.

### Risk classes

- **read** — no external mutation.
- **reversible_write** — mutation with explicit deterministic compensation.
- **consequential** — mutation with durable receipt and bounded authority.
- **privileged** — debugger/runtime evaluation, authority expansion, public exposure, secret-bearing contexts.

Privileged actions require separate grant; browser DOM authority never implies debugger authority.

## Operation and receipt law

`operation_id` identifies intent across transport/session restarts.

Before effect, daemon records CLAIMED with fingerprint and policy decision.

Replay rules:
1. same operation_id + same fingerprint + SUCCEEDED => return stored receipt, do not execute;
2. same operation_id + different fingerprint => conflict, no effect;
3. RUNNING after crash => reconcile effect/precondition before retry;
4. FAILED => retry only if capability replay class permits;
5. unknown effect state => DLQ/Donna, not blind retry;
6. compensation is a new linked operation with its own receipt.

A success receipt is evidence that the effect was observed, not merely that an adapter returned 200.

## Chrome bridge contract

Architecture:
`daemon <-> user worker <-> Native Messaging host <-> Chrome MV3 extension <-> tab`

Native Messaging is transport/presence, never persistence.

Rules:
- extension messages carry operation_id;
- host-to-extension payloads stay well below the documented 1 MB ceiling; large evidence is referenced by local receipt/artifact ID;
- MV3 service-worker suspension is expected;
- reconnect re-registers presence and resumes from ledger state;
- raw cookies are not exposed by default;
- tabs metadata, DOM read/action, network inspection, debugger attach and performance tracing are separate capability grants;
- `chrome.debugger` is privileged and deny-by-default.

First browser canary uses DOM/accessibility semantics. CDP/debugger is not required for the first mutation/replay proof.

## Windows UI/accessibility contract

Prefer semantic selectors and accessibility/UIA trees over coordinates.

A UI action request includes:
- target selector/evidence;
- expected precondition;
- action;
- postcondition;
- operation_id;
- risk class.

Pointer/keyboard fallback is lower confidence and must declare that downgrade in the receipt.

Worker loss changes UI capabilities to UNAVAILABLE while daemon remains DEGRADED.

## Transport topology

### v0 local
Daemon binds only to loopback. Stdio can adapt into the same operation engine.

### v0 private remote canary
Tailscale Serve proxies to the loopback backend. Tailnet ACL/identity is transport identity input, not final capability authority.

### later sovereignty track
Headscale/WireGuard must be separately certified. Do not assume Tailscale Serve headers or application identity semantics transfer unchanged.

No public bind in MVP.

## Truthful health model

Aggregate state:
- **ONLINE**: daemon up and all capabilities required by the requested profile available.
- **DEGRADED**: daemon up but one or more declared capabilities/workers unavailable.
- **OFFLINE**: daemon unavailable.

Examples:
- daemon UP + worker DOWN => DEGRADED;
- daemon UP + Chrome extension suspended => DEGRADED for browser-present profile;
- remote transport DOWN + local loopback UP => local ONLINE / remote OFFLINE, never global OFFLINE.

Health is capability-scoped, not one green lamp.

## Threat / authority model

Primary threats:
- duplicate mutation after reconnect/retry;
- shell escaping path/action authority;
- interactive process bypassing initial process policy;
- browser debugger escalation from ordinary DOM access;
- stale worker reclaiming a job;
- receipt written without verified effect;
- remote identity confused with capability authority;
- adapter compromise expanding scope;
- secret leakage through logs/browser context.

Controls:
- durable operation fingerprint;
- one policy hook across adapters;
- leases + fencing token;
- path canonicalization before shell/action;
- adapter capability manifests;
- deny-by-default privileged capabilities;
- receipt/effect digest + provenance;
- local loopback default;
- private overlay only;
- no raw cookie export.

## Failure / recovery matrix

| Failure | Truthful state | Automatic action | Forbidden |
|---|---|---|---|
| daemon crash before effect | OFFLINE | restart, recover CLAIMED op | assume effect occurred |
| daemon crash after effect before receipt | recovery-required | inspect postcondition/effect evidence | blind re-execute |
| worker dies | DEGRADED | expire lease, await reconnect | claim ONLINE |
| worker reconnects | capability restoring | reconcile fencing token/jobs | double-claim |
| Native Messaging disconnect | browser degraded | reconnect extension/host | invent new operation_id |
| MV3 worker suspension | browser presence degraded | re-handshake | lose durable operation state |
| policy DENY | capability healthy, operation DENIED | persist denial receipt | adapter bypass |
| debugger denied | DOM may remain available | keep privileged capability unavailable | inherit DOM grant |
| remote tunnel reconnect | remote restoring | same daemon ledger/op identity | duplicate mutation |
| unknown partial effect | DEGRADED / DLQ | Donna causal packet | retry by default |
| reversible mutation failed later | DEGRADED | compensation operation if contract exists | erase original receipt |

## Companion contracts

- **Clara** compiles FactoryBlueprint/capability boundaries.
- **Ryan** builds bounded cells only.
- **Yaz** measures duplicate-prevention, latency, policy denials and health transitions.
- **Graham** retains receipts, manifest/policy versions and provenance.
- **Rory** reconciles no-false-online, no-double-claim and authority drift.
- **Nardole** routes jobs/retries/backpressure without becoming execution truth.
- **Amy** presents health/approval/receipt state.
- **Donna** receives unknown-effect DLQ/recovery cases.
- **Rick/Doctor13** arbitrate authority expansion and semantic policy conflicts.

## Ryan gate

Ryan #197 is authorized to begin the bounded M0 cell in `mvp/RYAN_BUILD_PACKET.md`.

The full upstream products are **not** accepted architecture. Only the contracts above are.
