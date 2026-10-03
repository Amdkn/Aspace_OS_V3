# HANDOVER — 2026-10-02 — V4 Transition / CubeFarm / Harness Mesh / Anti-Amnesia

## Read this before doing anything

This handover exists because the current ChatGPT session exceeded its useful context horizon and A explicitly requested that the transition intent survive without reconstruction-by-memory.

**Do not redesign A'Space from scratch. Do not collapse this into "manager + dumb workers". Do not treat the latest runtime/session as the agent identity. Do not convert CubeFarm or any harness into the source of truth.**

The next session must resume from the durable GitHub objects referenced below.

---

# 1. Human intent that must not be lost

Amadou / A, human Founder, wants to finish V3 foundations and immediately transition into a lighter A'Space V4 that **integrates Agent OS + Life OS + Business OS**, while preserving Tech OS / Solarpunk Kernel primitives and projecting the whole institution into a living spatial office.

The transition is NOT:
- another rewrite;
- another ontology-only project;
- another dashboard;
- another "one agent = one chat/runtime" system;
- another deterministic-only worker farm;
- another LLM-only paperclip loop.

The transition IS:

```text
A — Human Founder
        ↕
A0 — Amadeus digital twin / shareholder projection
        ↕
Institutional Holons
S1/S2/S3 · A1/A2/A3 · B1/B2/B3
        │
        │ poly-embodiment
        ▼
Hermes / Codex / Claude / Antigravity / Jules /
Qwen / Kimi / Gemini / DeepSeek / other harnesses
        │
        ▼
────────────────────────────────────
           A'SPACE V4
────────────────────────────────────
kernel/
anthology/
embodiments/
capabilities/
evidence/

projections/
  agent/
  life/
  business/
  cubefarm/

adapters/
  github/
  linear/
  gws/
  harness/
  browser/
────────────────────────────────────
```

The system should progressively reduce synchronization/plumbing tax and redirect resources toward:
- Tech OS maintenance target ~20%;
- Life OS execution ~30%;
- Business OS execution ~50%.

These are directional resource targets, not rigid scheduler quotas.

---

# 2. Constitutional correction: hierarchy is not cognitive amputation

Canonical law already encoded by PR #326:

- hierarchy = primary stewardship, accountability, escalation, decision horizon;
- hierarchy != intelligence level;
- first hats such as BUILD / OBSERVE / STATE / FLOW / DESIGN are not job prisons;
- S3/A3/B3 are full reasoning holons, not scripts/workflows;
- upper/peer holons may temporarily absorb load-bearing work when lower layers are absent, immature or blocked;
- borrowed execution must keep provenance and handback/delegation debt;
- Amadou/A human Founder != A0 Amadeus institutional digital projection;
- detachment is an outcome of real autonomy, not a prohibition on Founder intervention.

Canonical motif:

`holon → holon → holon → instruments`

Forbidden regression:

`planner → manager → cognitively reduced worker → script`

---

# 3. Poly-embodiment / multi-harness law

Institutional identity must survive runtime change.

Example:

```text
RYAN / S3
├─ Hermes
├─ Codex
├─ Claude Code
├─ Antigravity
├─ Jules
├─ Qwen
└─ future ADE/browser surfaces
```

Several embodiments MAY coexist.

Allowed:
- multiple cognition paths;
- multiple independent reviews;
- research in parallel;
- separate worktrees;
- non-conflicting implementation.

Forbidden:
- two writers mutating the same protected effect without compatible scoped authority.

Therefore:
- lease/fencing protects effect / operation_id / correlation_id / affected resource;
- lease does NOT mean "only one Ryan may exist";
- runtime affinity is preference/compatibility, not identity.

Anchor: #318.

---

# 4. Agent OS missing migration: AI-native Capability Fabric

This was materially verified during this session.

Business OS / Coach OS already contains the richer AI-native execution substrate under:

`30_Business_OS/10_Projects/coach-os-app/src/lib/tooling/`

Observed components:
- defineTool.ts;
- registry.ts;
- types.ts;
- identity / permissions / quota / serverStore;
- adapters for MCP, MCP Apps, REST/API, CLI, Skill, In-App, Harness, AgentOS, A2A, A2UI, ACP, AG-UI, WebMCP and more.

Agent OS current desktop is still mostly:
- UI/apps;
- storage;
- projection API;
- truth contracts;
- observability.

So V3 migrated Agent OS **desktop/projection**, but not the full **AI-native capability nervous system**.

Canonical target:

```text
Domain Capability
      ↓
Typed Capability Contract
semantic meaning + authority + effect policy
      ↓
AI-Native Capability Registry
      ↓
MCP / API / CLI / Skill / In-App
      ↓
Harness Adapters
      ↓
WorkGraph / operation_id / EffectReceipt / Evidence
      ↓
Agent OS projection
```

Rules:
- MCP is a port, not the foundation;
- Agent OS exposes/projects capabilities but does not steal Business/Life semantic ownership;
- Business OS owns business capabilities;
- Life OS owns Life capabilities/flows;
- Tech OS owns machine primitives, state/evidence, operation-scoped fencing;
- transports/harnesses never become identity or authority.

Anchors:
- #333 — migrate AI-native Capability Fabric out of Business OS;
- #335 — first vertical slice `harness.list`;
- PR #334 / commit df2702a5e389f62f5097d0bcef4c4c0cfcc7262d merged.

---

# 5. CubeFarm is a V4 transition primitive, not a side experiment

A explicitly requires CubeFarm to be part of the V4 transition.

CubeFarm has **two distinct V4 functions**:

## 5.1 Production factory / Universal Constructor

CubeFarm is Ryan's bounded production factory.

Ownership:

```text
A / A0 intent
→ Rick / S1
→ Doctor13 / S2
→ Ryan / S3 BUILD-industrialisation
→ CubeFarm factory instrument
→ coding runtimes / QA / worktrees / browser / GitHub
```

CubeFarm MUST NOT become:
- Ryan's identity;
- A'Space SSOT;
- constitutional authority;
- autonomous paperclip queue;
- replacement for WorkGraph/Anthology.

Anchor: #388.

## 5.2 Living Office / spatial V4 projection

CubeFarm must also become the **Living Office** where Agent OS, Life OS and Business OS are projected on walls, rooms, floors and desks.

A desk represents a durable holon, not a transient runtime.

Example:

```text
RYAN DESK
├ identity: Ryan / S3
├ institutional state
├ embodiment state
├ workload state
├ home
├ missions / WorkIDs
├ effect leases
├ evidence head
├ subagents
└ runtime bodies
    ├ Hermes ACTIVE
    ├ Codex REVIEWING
    ├ Jules BUILDING
    └ Antigravity RESEARCHING
```

Floors/rooms may represent:
- S2 Core;
- A2 Life framework;
- B1 franchise/business;
- B2 domain;
- MissionCell / war room;
- bounded factory floor.

CubeFarm is a **projection/runtime surface**, not the ontology.

Anchor: #403.

## 5.3 Sovereign fork is mandatory

Current verified state from the prior continuation:
- local clone exists at `C:/Users/amado/cubefarm`;
- prior observed HEAD `31e7ce01a1dcc1da2b576d1da36718c16b05b8ca`;
- local CubeFarm was running on `127.0.0.1:4317`;
- remote was still only `origin = https://github.com/leonvanzyl/cubefarm.git`;
- local non-upstream state included modified package-lock + BAT launchers.

Therefore prior work produced a clone/setup, NOT a sovereign fork.

Required topology:

```text
leonvanzyl/cubefarm
      ↓ upstream
Amdkn/cubefarm
      ↓ origin
A'Space integration branches
      ↓
PR / CI / releases
```

Anchor: #402.

## 5.4 First fork canary

After the fork exists, recover the prior UUPM / Business OS **Multi-Theme** system into the A'Space CubeFarm fork.

Do not redesign a new theme engine from memory.

Anchor: #400.

---

# 6. codex-chatgpt-web is also a V4 transition primitive

A explicitly intended `miuuyy/codex-chatgpt-web` to help transport/use A'Space institutional context across browser-auth AI surfaces and coding harnesses.

Do NOT create independent forks for every provider:

```text
codex-qwen-web
codex-kimi-web
codex-zai-web
codex-minimax-web
codex-deepseek-web
...
```

Instead generalize the pattern into:

```text
A'Space Browser Harness Bridge
│
├─ SurfaceDriver<Qwen>
├─ SurfaceDriver<QwenCoder>
├─ SurfaceDriver<ZAI>
├─ SurfaceDriver<Kimi>
├─ SurfaceDriver<MiniMax>
├─ SurfaceDriver<DeepSeek>
├─ SurfaceDriver<Gemini>
└─ future browser AI surfaces
```

Common contract must cover at minimum:
- capabilities;
- authentication_state;
- models;
- context_capacity;
- file_support;
- tool_support;
- scheduling_support;
- persistence;
- send;
- observe;
- extract_artifacts;
- healthcheck;
- detect_drift;
- close_session.

Security / continuity rules:
- isolated browser profiles;
- never copy browser secrets into WorkGraph;
- no CAPTCHA/auth bypass;
- fail closed on auth/surface drift;
- browser surface is an embodiment/transport, not institutional identity;
- mission identity, authority, WorkID, correlation and evidence must survive surface replacement.

Anchor: #404.

---

# 7. Cognitive Treasury / resource routing

FreeLLMAPI and abundant models are fuel, not the driver.

Canonical structure:

```text
Institutional Holon
→ MissionContextEnvelope
→ Capability / Resource Governor
   ├ Cognitive Treasury
   ├ Harness/Surface Broker
   ├ Context + Session Broker
   └ Evidence Receipt
→ Hermes / Codex / Claude / Antigravity /
  Jules / Qwen / Kimi / Gemini / DeepSeek / ...
```

No token burn merely to prove tokens exist.

A routing decision may use:
- capability/tool parity;
- provider/model affinity;
- quota/budget;
- latency/reliability;
- privacy/locality;
- context size;
- mission risk;
- authority;
- evidence requirements.

A routing decision must never alter identity/rank/authority/mission ownership.

Anchor: #404.

---

# 8. Anti-amnesia primitive

The session failure itself is now part of the architecture problem.

Canonical pipeline:

```text
conversation / human intent
→ raw capture
→ IPBD classification
→ correlation + provenance
→ GitHub / Linear / GWS / WorkGraph
→ bounded execution
→ evidence / receipts
→ reconciliation / closure
→ durable memory
```

A new chat must be able to reconstruct the exact frontier without A retelling it.

CubeFarm + Browser Harness Bridge + V4 transition chain is the first replay canary.

Anchor: #405.

---

# 9. GitHub / Linear / GWS projection law

GitHub is not the whole institution.

- GitHub = engineering contract, code, PR, CI, release, technical evidence.
- Linear = A1/A2/A3 + B1/B2/B3 governance/outcomes.
- GWS = Life/Business operational effects: Drive, Docs, Sheets, Calendar, Tasks, etc.
- WorkGraph = claim/binding/operation/correlation/continuation/receipt substrate.
- Supabase/IPBD = durable intent/capture provenance where applicable.
- CubeFarm = spatial Living Office + bounded factory projection.
- Agent OS = AI-native capability + runtime/evidence projection plane.

A'Space V4 must unify these surfaces without pretending they are one database or one UI.

---

# 10. Clara → Ryan → River boundary

Do not regress this relationship.

- Clara / DESIGN-FORGE: contracts, architecture, interfaces, holdout scenarios, acceptance and factory design.
- Ryan / BUILD-INDUSTRIALISATION: builds reusable factories/capabilities/adapters/tests/gates/packaging/runtime machinery.
- River / FLOW-OPERATIONS: consumes those factories in real operational flows, sequences effects, handles retries/backpressure/GWS/receipts/outcomes.

Short form:
- Clara designs the engine;
- Ryan builds/industrializes the engine;
- River drives it in real missions.

This is default collaboration topology, not a cognitive caste.

---

# 11. Current closure-swarm state / do not assume fleet continuity is solved

At the last durable recap before this handover:
- Aspace V3 had dropped materially from the earlier backlog;
- 98 Jules sessions had reached COMPLETED in one closure wave;
- the fleet refill had failed once, leaving 0 active despite remaining issues;
- a later refill restored all 15 available Jules slots: 14 IN_PROGRESS + 1 QUEUED, 0 active duplication.

Therefore:
- "Jules can execute" is largely proven;
- "slot freed → automatically select next truthful issue → dispatch → publish PR → CI → merge/acceptance → close → refill" is the real continuity invariant;
- scheduler present != closure runner healthy;
- never declare completion from session status alone.

Do not waste Jules on duplicate sessions. Fill the real platform limit, then refill continuously as slots free.

---

# 12. Current GitHub frontier at handover time

## Amdkn/Aspace_OS_V3 — open issues

- #400 CubeFarm Multi-Theme canary
- #388 CubeFarm Universal Constructor
- #405 Anti-Amnesia continuity
- #404 Cognitive Treasury / Browser Harness Mesh
- #403 CubeFarm Living Office
- #402 Sovereign CubeFarm fork
- #335 harness.list vertical slice
- #333 Agent OS AI-native Capability Fabric
- #328 DC Sovereign auth-browser / recovery
- #318 V4 Embodied Holons
- #317 Anthology across GitHub/Linear/GWS
- #315 S2 Doctors Wargame
- #312 Software Factory + Wargame corpus
- #222 historical multi-source channel harvester
- #283 Foundation Completion
- #197 DC Sovereign build epic
- #219 DC Sovereign v1 cutover
- #290 Business OS tenant isolation canary
- #284 Business OS launch cohort
- #272 The OMK Services objective
- #194 DC Sovereign objective
- #232 Agent OS unified full-stack epic
- #215 production Chrome bridge
- #207 Discovery AI corpus
- #221 Research Atlas / PaperGraph factory

## Other active repos

### Life OS
Open:
- #105 Fractal Holon / Clara→Ryan Factory→River Flow
- #90 Terra state convergence
- #88 Terra M4 mission
- #98 Terra program
- #93 Terra flow / GWS / release

### Agent OS
Open:
- #1 hierarchy != identity != stewardship != runtime

### Business-Office-3-OS
Open:
- #2 B1/B2/B3 autonomous holons

### Mobile
Open:
- #29 extract Edge capabilities into canonical Business OS then freeze lineage

### Canonical Business OS repo
`omk-services/OMK-DESKTOP-WEB-OS`
- current product PR must be handled in that repo, not simulated by a V3 handoff.

---

# 13. Immediate resume order for the next session

Do NOT begin with another architecture essay.

## Lane A — preserve this handover
1. Read this file.
2. Read #405, #402, #403, #404, #333, #335, #388, #318, #317.
3. Verify no newer durable receipt supersedes any frontier below.

## Lane B — V4 transition primitives
1. Finish #402 sovereign CubeFarm fork.
2. Then #400 Multi-Theme canary on the real fork.
3. Continue #403 Living Office projection.
4. Treat codex-chatgpt-web through #404 as a Browser Harness Bridge proof pattern, not per-provider fork proliferation.
5. Continue #333/#335 Capability Fabric migration so Agent OS becomes the shared AI-native execution/projection layer.
6. Project Agent OS + Life OS + Business OS into CubeFarm only after source ownership remains clear.

## Lane C — closure before V4 cutover
Continue the Jules closure swarm until the foundation chains are truly closed by acceptance/evidence, not merely by COMPLETED sessions or merged PRs.

## Lane D — anti-amnesia
Use #405 to prove that a fresh session can reconstruct this exact plan without access to this old chat history.

---

# 14. Hard anti-regression rules

FAIL if the next session:
- forgets CubeFarm;
- forgets codex-chatgpt-web / Browser Harness Bridge;
- treats CubeFarm only as a code factory and forgets Living Office projection;
- treats CubeFarm as A'Space SSOT;
- makes Agent OS just another dashboard;
- leaves the Business OS AI-native adapter fabric stranded in Coach OS;
- copies every adapter blindly without classification;
- forks codex-chatgpt-web once per provider;
- reduces S3/A3/B3 to dumb workers;
- treats first-hat role labels as capability prohibitions;
- binds identity to one harness/session;
- makes one global writer lease equal one global actor;
- confuses A human Founder with A0 digital twin;
- lets scheduler/heartbeat become the brain;
- declares Jules fleet healthy merely because Scheduled Task is Ready;
- declares an issue done without acceptance/evidence;
- creates a new V4 monorepo before the transition primitives and closure state are durably understood.

---

# 15. Definition of transition readiness for creating the V4 project

A may create the new V4 project when the following are sufficiently true:

1. V3 foundation frontier is materially closed or each remaining blocker is typed and non-ambiguous.
2. CubeFarm has a sovereign Amdkn fork with upstream sync preserved.
3. CubeFarm is accepted as BOTH bounded factory + Living Office projection.
4. Browser Harness Bridge / SurfaceDriver direction is durable and not provider-forked.
5. Agent OS Capability Fabric has at least one real shared vertical slice.
6. Agent OS / Life OS / Business OS source ownership and projections are explicit.
7. Embodied Holon identity survives runtime replacement.
8. GitHub / Linear / GWS / WorkGraph / IPBD projection contracts are explicit.
9. Anti-amnesia replay succeeds from durable state.
10. The new V4 repo/project can be started as a **compression/unification migration**, not as another clean-room rewrite.

---

# 16. One-sentence continuity

**V4 is the compression of A'Space into durable institutional holons + shared capability/evidence substrate, with Agent/Life/Business projected into a CubeFarm Living Office, CubeFarm also serving as Ryan's bounded factory, and codex-chatgpt-web generalized into a replaceable Browser Harness Bridge — all without collapsing identity, authority, semantics or truth into any one runtime, UI, protocol or repository.**
