# HANDOVER — Codex GPT Web fork × Agent OS AI-Native Adapter Migration

**Date:** 2026-10-02  
**Status:** ACTIVE / durable frontier  
**Repo:** `Amdkn/Aspace_OS_V3`

## 0. Founder intent — preserve verbatim meaning

The active intent is twofold and must not be reduced into a generic "tooling cleanup":

1. **Fork and adapt `miuuyy/codex-chatgpt-web`** so the pattern is no longer tied to one provider/browser surface and can serve the heterogeneous A'Space harness mesh.
2. **Transfer the AI-native innovations already built inside Business OS / Coach OS into Agent OS**, especially the reusable adapter/capability substrate, instead of leaving Agent OS as mostly dashboard/observability while Business OS contains the richer execution fabric.

The next session must continue from the durable GitHub objects below. Do not ask the Founder to reconstruct the intent from chat history.

---

## 1. Verified architectural gap

Business OS / Coach OS already contains a reusable AI-native tooling stack under:

`30_Business_OS/10_Projects/coach-os-app/src/lib/tooling/`

Verified components include:

- `defineTool.ts`
- `registry.ts`
- `types.ts`
- identity / permissions / quota / server store
- adapters for:
  - MCP
  - MCP Apps
  - REST/API
  - CLI
  - Skill
  - In-App
  - Harness
  - AgentOS
  - A2A
  - A2UI
  - ACP
  - AG-UI
  - WebMCP
  - additional experimental protocol adapters

Agent OS currently has strong projection/observability/UI/state pieces, but the equivalent shared capability registry + transport + harness-adapter fabric has not been migrated completely.

**Key rule:** migrate the reusable substrate, not Business OS semantic ownership.

---

## 2. Canonical V4 split

```text
Tech OS
  machine primitives / WorkGraph / runtime state / fencing / evidence
       │
       ▼
Agent OS
  shared AI-native Capability Fabric
  registry + MCP/API/CLI/Skill/In-App + harness/runtime adapters
       │
       ├───────────────┐
       ▼               ▼
Life OS           Business OS
domain semantics  domain semantics
flows/effects     products/franchises/effects
```

Harnesses and browser surfaces are projections/embodiments, never institutional identity or business authority.

---

## 3. Durable issue topology

### Existing parents

- **#333** — `[P0][V4][AGENT-OS] Migrate the AI-native Capability Fabric out of Business OS`
- **#335** — first bounded vertical slice: `harness.list`
- **#404** — Cognitive Treasury / Harness Mesh
- **#318** — Embodied Holons

### New issues created from this handover

#### #410 — Browser Harness Bridge / codex-chatgpt-web fork

`[P0][V4][BROWSER-HARNESS-BRIDGE] Fork codex-chatgpt-web and generalize it across A'Space harnesses`

Intent:

```text
miuuyy/codex-chatgpt-web
        ↓ one sovereign A'Space fork
Amdkn-owned fork
        ↓
SurfaceDriver / Browser Harness Bridge core
        ├─ ChatGPT Web
        ├─ Qwen / Qwen Coder
        ├─ Z.ai
        ├─ Kimi
        ├─ MiniMax
        ├─ DeepSeek
        ├─ Gemini / Spark
        ├─ Muse
        └─ future browser-auth surfaces
```

Important correction to the earlier #404 wording:

- **do not fork once per provider**;
- **do fork the upstream once into A'Space ownership**;
- provider differences become SurfaceDriver adapters.

Acceptance begins with ChatGPT Web + one non-OpenAI surface, then expands.

#### #411 — Business OS → Agent OS adapter migration

`[P0][V4][AGENT-OS][ADAPTER-MIGRATION] Transfer Business OS AI-native adapters into the shared Capability Fabric`

Required classification for every module/adapter:

```text
KEEP DOMAIN-SPECIFIC      → Business OS / Life OS remains owner
GENERALIZE PLATFORM       → Agent OS Capability Fabric
RUNTIME/MACHINE PRIMITIVE → Tech OS
UI/PROJECTION             → Agent OS projection
EXPERIMENTAL              → quarantine / research
```

Migration batches:

- M0 — typed capability core / registry / shared types / authority/evidence hooks
- M1 — MCP / REST / CLI / Skill / In-App
- M2 — Harness adapters
- M3 — Agent/protocol adapters
- M4 — Business OS consumes shared substrate and sheds duplicated platform code

#### #412 — Harness certification

`[V4][HARNESS-MESH][CERTIFICATION] Certify shared Agent OS adapters across Claude, Codex, Hermes, Antigravity, Jules and browser surfaces`

Initial matrix includes:

- Claude Code
- Codex
- Hermes
- Antigravity
- Jules
- Qwen / Qwen Coder
- Gemini / Spark
- DeepSeek
- Kimi
- MiniMax

Every harness must prove:

- actor identity is supplied externally;
- capability discovery comes from shared Agent OS registry;
- authority is not widened;
- operation/correlation survives;
- effect evidence/readback exists;
- quota/latency/budget remain separate from identity;
- failover does not rewrite mission ownership;
- no harness-specific business executor exists.

---

## 4. Return topology

```text
#335 harness.list slice
       │
#410 Browser Harness Bridge
       │
#411 Adapter Migration
       │
#412 Harness Certification
       │
       ├────────→ #404 Harness Mesh
       └────────→ #333 Agent OS Capability Fabric
                        │
                        └────────→ #323 Wargame / CG1 + CG2 + CG6
```

No child is allowed to declare #333 complete by itself.

---

## 5. Design laws that must survive implementation

### A. One capability, many surfaces

```text
Capability Contract
    ├─ MCP
    ├─ API
    ├─ CLI
    ├─ Skill
    ├─ In-App
    └─ Harness adapter
```

Do not duplicate executor/business logic per transport.

### B. Identity remains independent

```text
Institutional Holon
   ≠ Harness
   ≠ Model
   ≠ Browser session
   ≠ MCP connection
   ≠ Agent OS widget
```

The same Ryan may be embodied in Hermes, Codex, Jules or a browser surface without becoming four Ryans.

### C. Fork substrate, not ontology

The `codex-chatgpt-web` fork is an integration substrate.

It must not become:

- A'Space identity model;
- WorkGraph replacement;
- source of authority;
- durable memory;
- one-provider dependency.

### D. Effect truth

DOM click / HTTP 200 / tool-call completion / PR merge are not enough for consequential effects.

Require authoritative readback or EffectReceipt when claiming an external mutation.

### E. Business OS ownership survives migration

Business capability semantics stay Business-owned even when the adapter/registry layer moves to Agent OS.

---

## 6. Immediate executable frontier

### Frontier A — #410

1. Pin upstream `miuuyy/codex-chatgpt-web` SHA.
2. Create/verify Amdkn-owned fork.
3. Record origin/upstream topology.
4. Inventory browser/auth/session architecture.
5. Extract a minimal SurfaceDriver interface.
6. Prove ChatGPT Web + Qwen/Qwen Coder against that interface.
7. Connect one Agent OS capability through the bridge.

### Frontier B — #411

1. Commit the complete adapter migration matrix.
2. Classify all current Business tooling modules.
3. Promote only the generic capability core first.
4. Keep Business-specific catalog/executors in Business OS.
5. Reuse #335 as first vertical proof instead of opening a new architecture-only branch.

### Frontier C — #412

1. Create a machine-readable certification matrix.
2. Certify Hermes + Codex + one #410 browser surface first.
3. Add Claude/Antigravity/Jules next.
4. Expand browser providers only after the common contract passes.

---

## 7. Anti-amnesia / anti-regression rules

A future session must **not**:

- reinterpret the fork intent as "do not fork";
- create N independent provider forks;
- copy all Business OS adapter files directly into Agent OS without classification;
- turn Agent OS into a second Business OS;
- turn harness/provider sessions into institutional identities;
- declare completion because a dashboard renders the adapter;
- rebuild #333 from scratch;
- replace existing issues with another architecture essay.

If blocked, update the relevant issue with typed evidence and create the smallest child issue needed.

---

## 8. Source of continuity

Durable GitHub frontier:

- #333 — shared Agent OS Capability Fabric
- #335 — first `harness.list` slice
- #404 — Harness Mesh / Cognitive Treasury
- #410 — codex-chatgpt-web sovereign fork + Browser Harness Bridge
- #411 — full Business OS adapter migration
- #412 — cross-harness certification

The next session should begin by reading those issues plus this handover, then continue from the first unmet acceptance criterion rather than reconstructing the architecture from conversation history.
