# Discovery Packet — A'Space Machine Fabric (AMF)

Date: 2026-09-28  
Mission: #194 `[MACHINE-FABRIC][S3]`  
Cell: #195 `BILL / DISCOVER`  
Return-to: Clara #196  
Build gate: Ryan #197 remains blocked until Clara emits the accepted MVP boundary.  
Authority: research only; this packet does not select final architecture.

## Executive discovery

The evidence does **not** support building “Desktop Commander 2”.

It supports an A'Space-owned **Machine Fabric** whose durable operation semantics are independent from any one MCP server, browser adapter, desktop-control library or remote tunnel.

The core research invariant is:

`tool request -> typed capability -> policy -> operation identity -> precondition -> effect -> durable receipt -> replay/compensation`

Desktop Commander and other projects are valuable **adapters/upstreams**, not the execution SSOT.

The strongest cross-source decomposition is:

1. Machine Core — filesystem/process/document primitives.
2. Windows Semantic UI — apps/windows/UI Automation/accessibility.
3. Computer-Use Fallback — screenshot/pointer/keyboard/app scripting.
4. Browser Semantic — accessibility/DOM/navigation.
5. Browser Debug — CDP/network/JS/performance.
6. Browser Presence — MV3 side panel/events + Native Messaging.
7. Durable Execution — jobs/idempotency/receipts/replay/leases/DLQ.
8. Policy — one pre-execution gate across all consequential capabilities.
9. Remote Plane — replaceable private transport.
10. Observability/Coherence — health means capability truth, not heartbeat.

---

## 1. Desktop Commander upstream

### 1.1 Local DesktopCommanderMCP

Source: https://github.com/wonderwhy-er/DesktopCommanderMCP  
License: MIT  
Recent inspected commit: `7bad545f4524d6b46ca84369b0015f4ebf151fec` (2026-09-25)

Reusable patterns:
- interactive process sessions;
- start/interact/read/terminate lifecycle;
- output pagination;
- filesystem search/read/write/move/info;
- surgical editing;
- dynamic configuration;
- structured adapters for Excel/PDF/DOCX;
- local tool-call history;
- Docker isolation option.

### Security evidence

Desktop Commander's own `SECURITY.md` states that:
- `allowedDirectories` is a guardrail, not a sandbox;
- terminal execution can escape directory restrictions;
- command blocklists are bypassable through interpreters/substitution/absolute paths;
- OS/container isolation is the real containment boundary.

Current upstream issues strengthen the gap:

- #691: requests a native pre-execution policy hook.
- #552: reports `interact_with_process` can bypass `blockedCommands`.
- #359: requests full-command pattern matching.
- #149: asks for per-project/tool permissions.
- #431: proposes external policy enforcement before machine operations.

Research implication:
**AMF must not inherit path allowlists or blocklists as its primary authorization model.**

A single policy decision point must cover:
- filesystem;
- process and interactive input;
- registry;
- services;
- scheduled tasks;
- browser;
- UI automation;
- network;
- package managers;
- databases;
- WSL/Docker/SSH.

### 1.2 Hosted Remote Desktop Commander

Source: https://github.com/desktop-commander/remote-desktop-commander  
Documentation commit inspected: `b480501dcca59f802ebaf97f2f57b45252d0b720`

The repository license explicitly states:
- the hosted Remote Desktop Commander implementation is proprietary;
- this repo contains docs/manifests, not service source;
- no license to the service implementation is granted;
- the local DesktopCommanderMCP is separately MIT licensed.

Reusable topology:
`AI client -> hosted MCP relay -> paired local device agent -> local execution`.

Do not reproduce the proprietary backend by reverse engineering.

AMF should instead own:
- device identity;
- reachability;
- auth/policy;
- operation ledger;
- replay;
- telemetry;
- fallback transport.

---

## 2. MCP conformance / transport

Signal: DesktopCommanderMCP issue #653  
https://github.com/wonderwhy-er/DesktopCommanderMCP/issues/653

The third-party `@hasmcp/mcp-spec-test` report against revision 2026-07-28 records:
- 10 failed requirements;
- 22 not verified;
- `server/discover` timeout;
- official-SDK handshake/list-tools failure.

The issue itself says this may be cold-start/environment behavior.

Classification: **reproduction target, not verdict**.

Clara/Ryan should require canaries for:
- cold start;
- warm start;
- stdio;
- Streamable HTTP;
- reconnect after daemon restart;
- version negotiation;
- list-tools/capability discovery.

Research invariant:

**MCP session state is transport state, not durable execution state.**

AMF operation/job/lease/receipt continuity must survive MCP reconnects and transport changes.

---

## 3. Windows-native alternatives

### 3.1 CursorTouch / Windows-MCP

Source: https://github.com/CursorTouch/Windows-MCP  
License: MIT  
Inspected commit: `a74df211d8dcb4cdc49f58a5a18d816d79bd6c3b` (2026-09-27)

Relevant patterns:
- native Windows app/window control;
- UI-state inspection;
- keyboard/mouse;
- accessibility-oriented automation;
- browser DOM mode;
- stdio/SSE/Streamable HTTP;
- per-user Scheduled Task installation;
- local logs.

Candidate reuse:
**user-session worker / Windows accessibility adapter**.

Do not promote it as AMF control plane without separate policy/replay semantics.

### 3.2 zavora-ai / computer-use-mcp

Source: https://github.com/zavora-ai/computer-use-mcp  
License: MIT  
Inspected commit: `35de1a26fa846d77bde6af89a43535c1e44980e7` (2026-09-12)

Relevant architecture:
`Server -> Policy -> Session -> Native / Accessibility / Scripts -> Applications`.

Useful patterns:
- accessibility/app scripting first;
- screenshot/pointer/keyboard fallback;
- host-side permissions;
- app/window targeting;
- persistent session/host concepts;
- human-visible run console;
- capability profiles instead of one maximal tool surface.

Its docs explicitly warn that the loopback HTTP endpoint grants desktop control to anything that can reach it and remote exposure needs host-owned authentication.

Candidate reuse:
**computer-use decomposition and UI fallback plane**.

---

## 4. Browser plane

### 4.1 Microsoft Playwright MCP

Source: https://github.com/microsoft/playwright-mcp  
Inspected commit: `e87bb897e15a6f2af402afb0f10b45eced9e1f9b` (2026-09-25)

Relevant patterns:
- accessibility-tree automation;
- deterministic element references;
- persistent browser context;
- CDP endpoint support;
- extension mode for running Chrome/Edge;
- isolated profiles;
- workspace-root restrictions.

Important upstream note:
Playwright documents that origin allow/block lists are **not security boundaries**.

Candidate hierarchy:
`browser semantic/accessibility -> CDP/debug -> vision fallback`.

Also notable: Playwright now recommends CLI+SKILL for some high-throughput coding-agent use cases because it can be more token-efficient than large MCP schemas, while MCP remains useful for persistent state/introspection.

AMF implication:
the Tool SDK should permit both MCP and compact CLI adapters behind the same capability/receipt contract.

### 4.2 Chrome DevTools MCP

Source: https://github.com/ChromeDevTools/chrome-devtools-mcp  
License: Apache-2.0  
Inspected commit: `47c5b3753d9bc6da32e261838a033e6427940cf0` (2026-09-28)

Relevant patterns:
- Chrome inspection/control;
- console/network;
- screenshots;
- performance traces;
- Puppeteer automation;
- attaching to running Chrome.

Risk:
its docs explicitly warn that connected MCP clients may inspect/debug/modify browser data exposed by that Chrome instance.

Usage statistics are enabled by default upstream, with opt-out controls.

Candidate reuse:
**deep browser-debug adapter**, not default browser authority.

Suggested capability split for Clara:
- `browser.tabs.read`
- `browser.dom.read`
- `browser.dom.mutate`
- `browser.navigation`
- `browser.network.inspect`
- `browser.debug.attach`
- `browser.runtime.evaluate`
- `browser.performance.trace`

---

## 5. Chrome Native Messaging + debugger

### 5.1 Native Messaging

Primary source:
https://developer.chrome.com/docs/extensions/develop/concepts/native-messaging

Verified mechanics:
- host communicates through stdin/stdout using framed JSON;
- each host is a separate process;
- `runtime.connectNative()` keeps a host alive while the port exists;
- `runtime.sendNativeMessage()` launches a host per message;
- host -> extension max message size: 1 MB;
- extension -> host max: 64 MiB;
- Windows registration uses HKCU or HKLM NativeMessagingHosts registry keys;
- `allowed_origins` identifies permitted extension IDs and does not accept wildcards;
- stdout must remain protocol-clean; diagnostics go to stderr;
- Windows framing requires binary-safe I/O.

Research candidate:
`MV3 side panel/service worker -> thin Native Messaging bridge -> AMF user worker -> daemon/ledger`.

Do **not** make the extension service-worker lifetime equal AMF lifetime.

Open design questions:
- reconnect after MV3 suspension;
- large evidence transfer/chunking/file refs;
- event batching/backpressure;
- extension upgrade/host version skew.

### 5.2 chrome.debugger

Primary source:
https://developer.chrome.com/docs/extensions/reference/api/debugger

Verified:
- `chrome.debugger` is an alternate CDP transport;
- can instrument network, JS, DOM/CSS and targets;
- requires explicit `debugger` permission.

Current Chrome 155 signal:
Chrome published stricter enterprise debugger-policy enforcement on 2026-09-08; Chrome 155 stable is scheduled for 2026-10-06. Managed environments with certain blocked-host/screenshot/DLP policies can reject debugger attachment.

Research implication:
`browser.debug.attach` is a **high-risk capability** and must remain separate from ordinary DOM action.

Do not create a default `dump cookies` or portable-session-token primitive.

---

## 6. Windows UI Automation

Primary sources:
- https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32
- https://learn.microsoft.com/en-us/windows/win32/winauto/ui-automation-specification

Windows UI Automation exposes:
- UI tree structure;
- properties/control types;
- control patterns;
- events;
- out-of-process automation clients.

Recommended research hierarchy:
`UIA semantic element -> control pattern -> app scripting -> coordinates/vision`.

Why:
- deterministic targeting;
- better receipts;
- reduced pointer theft;
- target verification;
- improved accessibility.

Failure cases Clara must model:
- elevated/UAC windows;
- secure desktop;
- locked session;
- multiple interactive sessions;
- provider inconsistency;
- focus stealing/background interaction.

---

## 7. Remote plane

### 7.1 Tailscale Serve — pragmatic private canary

Primary:
https://tailscale.com/docs/features/tailscale-serve

Verified:
- proxies a local service to tailnet devices;
- ACLs apply;
- identity headers are inserted for tailnet traffic;
- spoofed incoming identity headers are stripped;
- docs recommend backend localhost binding when identity headers are trusted;
- Funnel is the public mode and does not provide the same identity headers.

Strong v0 candidate:
`AMF 127.0.0.1:<port> -> Tailscale Serve -> authorized tailnet client`.

Limitation:
still depends on Tailscale's control plane.

### 7.2 Headscale — sovereignty candidate

Source: https://github.com/juanfont/headscale  
License: BSD-3-Clause  
Inspected commit: `99cbba7aff2bd78c62486212f6968c0cca62870c` (2026-09-28)

Headscale describes itself as an open-source self-hosted Tailscale control server.

Candidate use:
self-owned private overlay control plane.

Do **not** assume Tailscale Serve's identity/app-capability behavior is identical under Headscale. Reproduce.

### Other comparison candidates for Clara
- raw WireGuard + Caddy/Envoy/auth;
- SSH reverse transport for constrained cases;
- public relay only as explicit opt-in.

Research rule:
remote transport may change, but the same AMF `operation_id` and receipt semantics must survive it.

---

## 8. Missing primitives classic DC does not make durable

### Durable operation identity
Every consequential mutation should carry:
- `operation_id`
- `idempotency_key`
- capability
- target
- principal
- preconditions
- risk class
- attempt
- lease
- timestamps

### Durable receipt
Receipt should record:
- requested action;
- resolved target;
- precondition result;
- effect;
- evidence;
- replay state;
- undo/compensation reference.

### Restart/replay
After crash:
1. recover unfinished operation;
2. inspect receipt/effect;
3. re-check precondition;
4. classify `already_done | safe_to_retry | needs_human | compensate`;
5. never blindly repeat a mutation.

### Jobs / leases / DLQ
Persist:
- queued/running/waiting/completed/failed;
- lease owner/expiry;
- retry/backoff;
- dependencies;
- cancellation;
- dead-letter;
- last evidence.

### Capability registry
Each adapter should publish:
- capability ID;
- schema;
- read/mutate classification;
- side effects;
- authority/risk;
- target scopes;
- idempotency semantics;
- undo/compensation;
- observability events;
- health probe;
- dependencies.

### Health truth
“Online” must decompose into:
- daemon alive;
- ledger writable;
- policy engine healthy;
- transport reachable;
- user worker attached;
- browser bridge attached;
- target desktop interactive;
- requested capability healthy.

Heartbeat alone is insufficient.

---

## 9. Bill S0 last30days applied to Machine Fabric

Pinned S0 upstream:
`mvanhorn/last30days-skill@084662b501fb0dba95bd55eff0c258d35e0dc499`

Safe profile:
- browser cookies off;
- keyless/free sources;
- no store;
- no publish/webhooks;
- raw JSON.

Machine Fabric scout:
`MCP desktop computer use Chrome browser native messaging remote machine control Windows`

Result:
- exit 0;
- Reddit: 2;
- YouTube: 4;
- grounding: no-results;
- HN/GitHub/web: terminal summary reported zero;
- no warning emitted.

Important quality finding:
the deterministic fallback planner shortened the query and only selected Reddit/YouTube/grounding. Two Reddit results were clearly off-topic.

Therefore Bill S0 promotion needs one additional contract:
**for specialized technical missions Bill must generate an explicit `--plan`; deterministic fallback is not accepted as evidence selection authority.**

No scout result enters S1 merely because engagement is high.

---

## 10. Evidence-backed candidate boundaries for Clara

These are **design inputs**, not final architecture.

### Candidate invariant A — Fabric, not fork
Reuse upstream adapters selectively; AMF owns durable operation semantics.

### Candidate invariant B — daemon vs interactive worker
A machine service/daemon owns:
- ledger;
- policy;
- jobs;
- receipts;
- remote transport;
- health.

A user-session worker owns:
- desktop/UI;
- browser Native Messaging;
- clipboard;
- interactive-only capabilities.

### Candidate invariant C — one policy gate
All consequential capabilities pass a shared pre-execution policy contract.

### Candidate invariant D — semantic before pixels
Desktop:
`UIA/accessibility -> scripting -> coordinates/vision`.

Browser:
`DOM/accessibility -> extension APIs -> CDP/debug -> vision`.

### Candidate invariant E — localhost first
Core MCP/HTTP endpoint binds loopback by default.
Remote adapters own external exposure.

### Candidate invariant F — transport-independent operations
Operation identity/receipts survive:
- stdio;
- local HTTP;
- Tailscale;
- Headscale/WireGuard;
- reconnect/client retry.

### Candidate invariant G — no credential portability by default
Act inside browser/session context; do not export raw cookies/tokens as normal tools.

---

## 11. CapabilityNeeds emitted to Clara

1. **Execution Core Contract**
   - daemon/worker boundary;
   - durable operation schema;
   - idempotency/replay;
   - receipts;
   - leases/retry/DLQ.

2. **Policy Contract**
   - uniform pre-execution input;
   - allow/deny/approval;
   - fail-closed behavior for high-risk classes;
   - policy engine health semantics.

3. **Capability Manifest**
   - typed tool/adaptor metadata;
   - side effects;
   - risk;
   - observability;
   - rollback.

4. **Browser Bridge Contract**
   - MV3 extension;
   - Native Messaging framing/reconnect;
   - DOM vs debugger authority;
   - event backpressure;
   - secret-handling invariant.

5. **Windows Worker Contract**
   - UIA/accessibility;
   - user-session binding;
   - elevation/secure-desktop failure semantics;
   - fallback ordering.

6. **Transport Contract**
   - localhost core;
   - Tailscale Serve canary;
   - sovereignty path Headscale/WireGuard;
   - identity propagation;
   - reconnect without duplicate mutation.

7. **Health/Observability Contract**
   - Yaz metrics;
   - Rory truthful availability;
   - Amy human-visible approvals/receipts/undo;
   - Graham evidence/provenance;
   - Nardole routing/leases/backpressure.

---

## 12. Required canaries before Ryan build acceptance

Clara should translate these into the MVP boundary:

1. **restart after mutation -> replay -> zero duplicate mutation**
2. daemon alive while user worker dies -> truthful degraded capability state
3. worker reconnect -> no duplicate job claim
4. policy denial blocks both initial process execution and interactive process input
5. out-of-scope filesystem action denied even when attempted indirectly through shell
6. Native Messaging reconnect after extension/service-worker restart
7. deterministic DOM action -> receipt
8. debugger capability denied unless separately authorized
9. remote transport reconnect preserves operation identity
10. Tailscale private transport canary
11. Headscale/sovereign transport evaluated separately; do not block v0 if not required
12. MCP cold/warm conformance test against selected SDK revision
13. capability health differs from heartbeat
14. undo/compensation demonstrated for at least one reversible mutation

---

## 13. Bill verdict

**Research is sufficient for Clara to start #196.**

What Bill recommends *for evaluation*:
- use DesktopCommanderMCP as a source of core machine UX patterns;
- use Windows-MCP + Windows UIA as semantic Windows references;
- use computer-use-mcp as fallback/session/policy reference;
- use Playwright as default browser-semantic reference;
- use Chrome DevTools / `chrome.debugger` as separately authorized deep-debug adapter;
- use Native Messaging for browser presence ↔ local worker;
- use Tailscale Serve for the first private remote canary;
- preserve Headscale/WireGuard as sovereignty path;
- make A'Space's ledger/policy/receipts/replay layer the durable center.

What Bill explicitly does **not** decide:
- implementation language;
- database library;
- Windows service framework;
- exact MCP SDK;
- exact extension UX;
- final permission levels;
- final remote provider;
- final MVP file layout.

Those belong to Clara #196.

**Return-to: #194 -> Clara #196.**
