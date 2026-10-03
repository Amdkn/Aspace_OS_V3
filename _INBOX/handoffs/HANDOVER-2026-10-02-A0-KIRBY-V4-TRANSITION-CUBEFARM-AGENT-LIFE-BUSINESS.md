# HANDOVER — 2026-10-02 — A0/Kirby — V4 Transition, CubeFarm, Agent OS, Life OS, Business OS

**Status:** CANONICAL SESSION EXIT HANDOVER  
**Reason:** current ChatGPT session reached context saturation; continuing inside it risks omission, compression and amnesia debt.

## 0. Restart rule

The next session MUST NOT reconstruct A'Space from generic AI-agent patterns or a stale conversational session.

Read, in order:
1. this handover;
2. current `AGENTS.md`, `MEMORY.md`, `ASPACE_WORKSPACE_REGISTRY.json`;
3. live GitHub state for #318, #328, #333, #335, #388, #400 and open PRs;
4. the explicit execution frontier below.

Old ChatGPT / Antigravity / Jules conversations are embodiments, not truth. If saturated, stale or zombie, retire them. Durable GitHub / WorkGraph / evidence wins.

---

# 1. V4 constitutional correction

The recurring V1/V2/V3 regression was semantic reduction:

```text
visionary / planner
    ↓
manager
    ↓
worker
    ↓
script / workflow
```

V4 law:

```text
Cognition        → broad
Competence       → cumulative
Responsibility   → primary, not exclusive
Authority        → scoped
Contribution     → transversal
Execution        → may move up/down when reality requires it
```

**Lower rank = narrower jurisdiction, never lower intelligence.**

S1/S2/S3, A1/A2/A3 and B1/B2/B3 are cognitively complete holons inside bounded authority.

Ryan BUILD, Yaz OBSERVE, Graham STATE, River FLOW, Clara DESIGN/FORGE, etc. are first hats / stewardship anchors, not functional prisons.

### Elastic subsidiarity

If the intended lower layer is absent, immature or blocked, a competent peer or upper holon may temporarily absorb the load-bearing work with:
- provenance;
- authority scope;
- effect scope;
- handback/delegation debt;
- return condition.

“Not my job” is a FAIL when a critical hole remains open.

---

# 2. Human Founder ≠ A0

- **A / Amadou** = human Founder.
- **A0 Amadeus / Kirby** = digital-twin / shareholder-level institutional projection.

A0 detachment is an outcome of real autonomy, never a rule that forbids Founder intervention during bootstrap.

---

# 3. Poly-embodiment

Correct model:

```text
                    RYAN
           institutional identity
                    │
       ┌────────────┼───────────────┐
       ▼            ▼               ▼
    Hermes        Codex          Claude
       │            │               │
       ├────── Antigravity ─────────┤
       ├────── Jules / Qwen ────────┤
       └────── future harnesses ─────┘
```

Allowed simultaneously:
- research;
- review;
- simulation;
- separate worktrees;
- non-conflicting implementation.

Forbidden:
- two writers mutating the same protected effect without compatible scoped authority.

Exactly-once/fencing applies to **effect / operation_id / correlation_id / affected resource**, not to actor existence.

Runtime affinity is preference/compatibility, not exclusivity.

---

# 4. Embodied Holon — #318

The durable unit is:

```text
Identity
+ durable home
+ capability profile
+ authority
+ memory/provenance
+ delegation topology
+ runtime affinity
+ compiled mission context
+ continuity ledger
= Embodied Holon
```

Keep separate:
```yaml
institutional_state: ACTIVE|SUSPENDED|ARCHIVED
embodiment_state: READY|DEGRADED|MISSING
runtime_state: ONLINE|OFFLINE|UNSTABLE|UNKNOWN
workload_state: IDLE|QUEUED|WORKING|BLOCKED|REVIEW
```

Never collapse those into one boolean `active`.

Context should be compiled per mission; do not recreate every agent from one giant generic prompt/CLAUDE.md.

---

# 5. V4 target topology

```text
A — Human Founder
        ↕
A0 — Amadeus
        ↕
Institutional Holons
S1 / S2 / S3
A1 / A2 / A3
B1 / B2 / B3
        │
        │ poly-embodiment
        ▼
Hermes / Codex / Claude / Antigravity
Jules / Qwen / Kimi / Gemini / DeepSeek / ...
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
────────────────────────────────────
```

V4 should be a lighter shared ontology/monorepo with projections, not six disconnected kingdoms synchronized forever.

Strategic resource direction after stabilization:
- L0 Tech OS ≈ 20% maintenance;
- L1 Life OS ≈ 30%;
- L2 Business OS ≈ 50%.

This is a strategic target, not a rigid quota.

---

# 6. Projection law

No SaaS is the universal source of truth.

```text
INTENTION
   ↓
classify by ontology
   ├── reusable technical gap → GitHub
   ├── governance/outcome     → Linear
   ├── scheduled commitment   → Calendar
   ├── next action            → Tasks / Keep
   ├── workspace/resource     → Drive
   ├── operational model      → Sheets
   └── execution continuity   → WorkGraph
          ↓
      AnthologyRef
          ↓
correlation_id / return_to / evidence
```

### GitHub
Engineering S3 surface: repos, Issues, PRs, Discussions, Actions, Releases, worktrees/Codespaces, evidence.

### Linear
Institutional/governance projection for A1/A2/A3 outcomes. Not runtime truth.

### GWS / Life OS mapping
- Ikigai → Docs / Slides
- Life Wheel → Drive / Areas
- PARA → Drive
- 12WY → Calendar / Agenda
- GTD → Tasks / Keep
- DEAL → Sheets

### WorkGraph
Execution continuity, leases/bindings, effect fencing, recovery, return_to. It is a pacemaker substrate, not the brain.

### CubeFarm
Spatial office + bounded production factory projection. Never the Anthology or universal truth store.

---

# 7. CubeFarm V4 — DO NOT LOSE THIS

Current:
- **#388 OPEN** — CubeFarm as Ryan's bounded Universal Constructor.
- **#400 OPEN** — recover UUPM/Business OS Multi-Theme into the A'Space CubeFarm fork.

Canonical ownership:

```text
A / A0 intent
  ↓
Rick / S1 gatekeeper
  ↓
Doctor13 / S2 governor
  ↓
Ryan / S3 BUILD + industrialisation
  ↓
CubeFarm / factory instrument
  ↓
coding runtimes + QA + worktrees + browser + GitHub
```

CubeFarm MUST NOT become:
- Ryan's identity;
- Doctor13's identity;
- A'Space source of truth;
- constitutional authority;
- an unrestricted Paperclip Maximizer.

### Fork topology

```text
leonvanzyl/cubefarm
        │ upstream
        ▼
Amdkn/CubeFarm shadow fork
        │
        ├── thin A'Space UI/runtime patchset
        │     └── #400 Multi-Theme canary
        │
        └── adapters / projections
              ├── WorkGraph
              ├── GitHub
              ├── Linear
              ├── GWS
              └── Harnesses

A'Space Anthology / identity / authority
        ≠
CubeFarm cosmology
```

Decision gate:
- `USE_UPSTREAM + ADAPTER`
- `SHADOW_FORK + THIN_PATCHSET`
- `DEEP_FORK_REQUIRED`

No deep fork by aesthetics.

### #400 Multi-Theme
Required:
1. recover exact prior UUPM/Business OS implementation/config/screenshots;
2. establish Amdkn fork topology;
3. port Multi-Theme as bounded UI/runtime capability;
4. keep CubeFarm cosmology separate from A'Space Anthology;
5. prove ≥2 themes without business-logic duplication;
6. browser evidence + tests + exact commit PR;
7. return to #388.

Do not rewrite Multi-Theme from memory.

---

# 8. CubeFarm as living office

A Ryan desk should render separately:

```text
Identity: Ryan
Institution: S3 / Doctor13
Home: durable workspace
Institutional state: ACTIVE
Embodiment: READY

Hermes       ACTIVE
Codex        REVIEWING
Jules        BUILDING
Antigravity  SUPERVISING / RESEARCH
Qwen         IDLE

missions
effects
operation leases
session lineage
subagents
budget lease
evidence head
fallbacks
```

If Codex is replaced by Claude, Ryan's desk remains Ryan's desk.

CubeFarm may project Agent OS, Life OS and Business OS onto rooms/walls/desks without becoming their source of truth.

---

# 9. Agent OS — missing AI-native migration

Current:
- **#333 OPEN** — migrate AI-native Capability Fabric out of Business OS.
- **#335 OPEN** — first vertical slice: `harness.list`.

Business OS / Coach OS already contains:

```text
30_Business_OS/10_Projects/coach-os-app/src/lib/tooling/
├── defineTool.ts
├── registry.ts
├── types.ts
├── identity.ts
├── permissions.ts
├── quota.ts
├── serverStore.ts
└── adapters/
    ├── mcp.ts
    ├── mcp-apps.ts
    ├── rest.ts
    ├── cli.ts
    ├── skill.ts
    ├── in-app.ts
    ├── harness.ts
    ├── agentos.ts
    ├── a2a.ts
    ├── a2ui.ts
    ├── acp.ts
    ├── agui.ts
    ├── webmcp.ts
    └── ... ~24 adapters
```

Agent OS was migrated mainly as UI/observability/projection, not as this AI-native nervous system.

### V4 Capability Fabric

```text
Institutional Holon / Domain Capability
                │
                ▼
      Capability Contract
 schema + authority + effect policy
                │
                ▼
    AI-Native Capability Registry
                │
     ┌──────────┼───────────┐
     ▼          ▼           ▼
   MCP/API     CLI/Skill    In-App
     │                       │
     └──────────┬────────────┘
                ▼
        Harness Adapters
 Claude / Codex / Hermes / Antigravity /
 Jules / Qwen / DeepSeek / Kimi / future ADEs
                │
                ▼
      WorkGraph / EffectReceipt / Evidence
```

### Ownership
- Agent OS owns shared exposure/projection fabric.
- Business OS owns business semantics/capabilities.
- Life OS owns Life semantics/capabilities/flows.
- Tech OS owns machine primitives, WorkGraph, policy, state/evidence, runtime security.

### Key rule
```text
MCP ≠ foundation
MCP = one port
Capability Contract = foundation
```

If MCP or a provider disappears, A'Space should continue.

### #335 vertical slice
```text
shared harness.list capability contract
→ Agent OS capability registry
→ MCP
→ API/REST
→ CLI
→ one real harness adapter
→ same schema/result semantics
→ provenance / observed_at / evidence visible in Agent OS
```

Do NOT migrate all adapters blindly. Classify KEEP / GENERALIZE / BUSINESS-SPECIFIC / DEPRECATE-RESEARCH.

---

# 10. Factory / design / flow boundaries

Useful default topology:
- Bill → RESEARCH / Discovery Packets.
- Clara → DESIGN/FORGE contracts and factory blueprints.
- Ryan → BUILD/industrialisation reusable capability/factory.
- River → FLOW/operations composing factories into effects.
- Yaz → OBSERVE behavior/cost/drift/zombies.
- Graham → STATE/provenance/replay.
- Nardole → DISPATCH/dependencies/return_to/backpressure.
- Amy → INTERFACE / typed exposure.
- Rory → PERSISTENCE / Linear-Life reconciliation.

These are stewardship anchors, not caste restrictions.

Critical:
```text
Ryan BUILD factories
≠
River FLOW using factories
```

---

# 11. Wargames must execute

#323 Blind Spots is CLOSED after RECON, but its outputs remain canonical.

Added in this session:
- BS21 ROLE RIGIDITY
- BS22 SINGLE-HARNESS CAGE
- BS23 BOOTSTRAP ABSTENTION
- BS24 FOUNDER/A0 CONFLATION
- BS25 AI-NATIVE SUBSTRATE STRANDED IN A DOMAIN PRODUCT

Wargames must produce bounded experiments and vertical slices, not dormant documents.

#321/#322 are CLOSED, but continuation law remains:
```text
stale event
→ wake responsible holon/topology
→ re-evaluate reality
→ continue / split / merge / research / build / suspend / reroute / stop
```

Scheduler = pacemaker, not brain.

---

# 12. DC / machine fabric

**#328 OPEN**.

Canonical direction:
- A'Space Sovereign DC = primary machine gateway;
- hosted Desktop Commander = explicit fallback only;
- no automatic browser opening during autonomous recovery;
- `AUTH_REQUIRED` is state/evidence, not permission to create a browser loop.

Do not reintroduce hosted DC as V4's control SPOF.

---

# 13. Multi-harness abundance

The user has many models/providers/harnesses and large free token capacity. The problem is not scarcity.

The missing integration pattern is:

```text
capability semantics
→ shared registry
→ adapters
→ harness compatibility
→ operation-scoped authority
→ evidence
→ replaceable runtime
```

No provider/harness becomes the institutional identity.

---

# 14. Historical failure lessons

### Multica
- apparent multi-agent fleet collapsed onto shared runtime/prompt fate;
- shared generic context compressed distinct identities;
- runtime lifecycle confused with institutional presence.

### Buzz / Paperclip
- execution organ must remain inside authority + WorkGraph + evidence + fencing.

### Antigravity
- scheduled/zombie conversations can persist without valid mission/lease;
- long contexts can keep executing after durable truth moved elsewhere.

### Codex / Claude / Hermes / Jules
- useful embodiments, never identity.

---

# 15. Jules closure swarm

The user explicitly authorized aggressive Jules parallelism rather than protecting quota at the expense of closure.

Historical snapshots in this session:

Snapshot A:
- 22 A'Space V3 issues open;
- 98 Jules COMPLETED;
- 2 FAILED;
- 0 IN_PROGRESS;
- refill loop failed after completion.

Snapshot B after refill:
- 14 IN_PROGRESS;
- 1 QUEUED;
- 15/15 slots occupied;
- 0 active duplication;
- wave included #194 #197 #206 #207 #215 #219 #220 #221 #222 #232 #272 #283 #284 #290 #311.

These are snapshots, not current truth. Always re-check live state.

Required supervision is hybrid:
1. deterministic local inventory/refill/state loop;
2. Antigravity LLM supervisor for stalls, user-input waits, bad assumptions and replanning;
3. ChatGPT hourly outer safety net.

Do not reduce this to deterministic-only worker logic or LLM-only babysitting.

---

# 16. Live GitHub frontier at handover creation

Fresh check:

OPEN:
- #318 Embodied Holons
- #328 DC Sovereign
- #333 AI-native Capability Fabric
- #335 harness.list vertical slice
- #388 CubeFarm bounded Universal Constructor
- #400 CubeFarm Multi-Theme canary

CLOSED but canonical:
- #321 prompt-independent continuation
- #322 owner/runtime separation substrate
- #323 Blind Spots Wargame
- #324 Orca/Hermes environment divergence

Open PRs visible:
- #372 Fix Discovery Corpus GWS Architecture Regression & Generate Closure Evidence
- #339 [P0][V4][AGENT-OS] Migrate the AI-native Capability Fabric out of Business OS
- #332 [WARGAME][TB09] TruthProjection envelope for machine→human state

Resolve/supersede conflicts; do not blind-merge stale branches.

---

# 17. Cross-repo completion intent

The user's explicit target is not “progress”. It is to clear the V3/Agent/Life/Business backlog enough to create V4 without dragging ambiguous foundation debt forward.

Before V4 creation gate:
```text
A'Space V3 backlog      → closed or explicitly carried forward
Agent OS                → Capability Fabric migration anchored
Life OS                 → projection/operational gaps bounded
Business OS             → canonical repos clean; no handoff pretending to be implementation
CubeFarm                 → fork decision + first canary
DC/machine fabric        → sovereign path not a critical SPOF
Jules closure swarm      → refill + publish + CI + merge + close loop proven
```

Not every historical satellite must be perfect if remaining debt is explicit, bounded and intentionally carried forward.

---

# 18. Economic test

```text
Architecture Debt
Compute Debt
Coordination Debt
Complexity Debt
        │
        ▼
acceptable only if it creates
        │
        ▼
Verified Recurring Flow
Life outcomes
Business outcomes
Cashflow
Attention liberated
Automation reused
```

If the architecture consumes the Founder without recurring flow, it is economically insolvent.

V4 must reduce A's babysitting tax.

---

# 19. ESOP / Open Democracy intent

```text
structured accountability
≠ superiority of persons
≠ narrow job caste
≠ prohibition on contribution
```

Authority can be scoped while intelligence/contribution remain broad.

---

# 20. Resource pressure

The A'Space SSD was shown near saturation (~76.6 GB free of 930 GB at that snapshot).

Factor disk pressure into:
- CubeFarm worktrees;
- Jules concurrency;
- clones;
- caches;
- model/runtime logs;
- Orca/Antigravity artifacts.

Do not create massive duplicate worktrees blindly.

---

# 21. Immediate next execution order

1. **Fresh truth** — inspect current open PRs/issues across canonical repos + current Jules fleet + zombie sessions.
2. **Consume closures** — merge/reject/supersede near-complete PRs with acceptance evidence.
3. **Prove refill** — completed Jules slot automatically launches next eligible issue without duplicate conflicting writers.
4. **Continue #333/#335** — one real `harness.list` shared-capability slice before broad adapter migration.
5. **Continue #388/#400** — establish/verify Amdkn CubeFarm shadow fork and recover exact UUPM Multi-Theme.
6. **Project Life/Business** — Agent OS exposes shared capabilities without stealing domain semantics; correlate GitHub ↔ Linear ↔ GWS ↔ WorkGraph.
7. **V4 creation gate** — create the new V4 structure only when critical V3 foundation debt is either closed or explicitly carried forward.

---

# 22. What the next session must NOT do

Do NOT:
- reconstruct the cosmology from zero;
- reduce S3/A3/B3 to scripts/workflows;
- forbid Doctors/Rick from technical work during bootstrap;
- enforce one runtime per identity;
- make CubeFarm the truth store;
- make GitHub the universal intention store;
- make Linear runtime truth;
- make GWS CLI equal Life semantics;
- copy all Business adapters blindly into Agent OS;
- rewrite UUPM Multi-Theme from memory;
- treat PR merge as capability completion without evidence;
- trust process ONLINE as institutional presence;
- reopen closed Wargames just to write more docs;
- ask A to babysit the next step when durable frontier is known.

---

# 23. Next-chat bootstrap

> Resume A'Space from `HANDOVER-2026-10-02-A0-KIRBY-V4-TRANSITION-CUBEFARM-AGENT-LIFE-BUSINESS.md`. Do not redesign the hierarchy or reconstruct context from memory. Read live GitHub state for #318, #328, #333, #335, #388, #400 and current open PRs, then inspect the Jules/Closure-Swarm frontier. Preserve the V4 laws: jurisdiction ≠ intelligence; first hat ≠ functional prison; A ≠ A0; identity ≠ runtime; poly-embodiment allowed; effect-scoped fencing; CubeFarm = bounded factory/spatial projection; Agent OS = shared AI-native Capability Fabric/projection plane; Life/Business keep semantic ownership; GitHub/Linear/GWS/WorkGraph are complementary projections. Continue from the first unresolved execution gate and produce real evidence/PR/closure before new architecture prose.

---

# 24. North star

```text
Anthology / identities / authority
        +
Embodied Holons
        +
AI-Native Capability Fabric
        +
WorkGraph continuity / effect fencing
        +
GitHub / Linear / GWS projections
        +
CubeFarm spatial office + bounded factory
        +
Life OS / Business OS semantics
        +
replaceable poly-harness runtimes
```

The system succeeds only when structure decreases A's babysitting tax instead of increasing it.
