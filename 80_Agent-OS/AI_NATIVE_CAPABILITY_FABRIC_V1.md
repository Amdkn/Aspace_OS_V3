# AI-Native Capability Fabric v1

**Issue:** #333  
**Status:** IMPLEMENTED / migration complete
**Scope:** A'Space V4 shared execution substrate across Tech OS, Life OS, Business OS and Agent OS  
**Origin:** Business OS / Coach OS tooling stack

## 1. Problem statement

The AI-native execution layer already exists, but in the wrong architectural place.

The current Business OS / Coach OS implementation contains a mature tool substrate under:

`30_Business_OS/10_Projects/coach-os-app/src/lib/tooling/`

Observed live modules include:

- `defineTool.ts`
- `registry.ts`
- `types.ts`
- `permissions.ts`
- `identity.ts`
- `quota.ts`
- `serverStore.ts`
- `catalog/*`
- adapters for MCP, MCP Apps, REST, CLI, Skill, In-App, Harness, AgentOS,
  A2A, A2UI, ACP, AG-UI, WebMCP and additional protocol projections.

At the same time, Agent OS remains primarily a desktop/projection/observability layer.
The live Agent OS desktop has apps, truth contracts, storage and API projections but no
equivalent shared capability registry + transport/harness adapter fabric.

This migration moves the core capability contract and surface adapters into `80_Agent-OS/capability_fabric/`.

## 2. V4 architecture

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

The fabric is shared infrastructure. Domain meaning stays with its owning layer.

## 3. Ownership boundaries

### Agent OS

Owns the shared **capability exposure and projection fabric**:

- capability registry projection;
- adapter inventory and compatibility;
- MCP/API/CLI/Skill/In-App exposure;
- harness/runtime bindings;
- capability discovery;
- runtime presence and surface health;
- evidence/provenance projection.

Agent OS does **not** own Business or Life semantics merely because it exposes them.

### Business OS

Owns:

- business capability meaning;
- A-SPEC CCS / WER / RID contracts;
- tenant policy and business authority;
- business workflows and effects;
- franchise/product configuration.

### Life OS

Owns:

- Life capability meaning;
- framework and A1/A2/A3 operational semantics;
- GWS-driven Life/Business flow composition where applicable.

### Tech OS

Owns:

- machine primitives;
- WorkGraph;
- operation-scoped fencing;
- durable state/evidence;
- runtime adapters;
- identity/runtime separation;
- machine access and security boundaries.

## 4. Canonical capability contract

One capability is declared once and projected many ways.

Minimum shared contract (as implemented in `CapabilityContract`):

```python
capability_id: str
version: str
domain_owner: str
intent: str
input_schema: Dict[str, Any]
output_schema: Dict[str, Any]
authority: str
effect_class: Literal["QUERY", "COMMAND", "EVENT"]
idempotency: bool
compensation: Optional[str]
evidence_required: bool
freshness: str
supported_surfaces: List[str]
runtime_bindings: List[str]
effect_receipt: Optional[str]
```

The Business OS `defineTool` pattern is useful prior art, but V4 must generalize it
without importing Business-specific authority assumptions into every domain.

## 5. Adapter migration classification

The current Coach OS adapter set has been classified and extracted.

| Adapter family | V4 disposition |
|---|---|
| MCP / MCP Apps / MCP schema | GENERALIZED into shared fabric (`mcp_adapter.py`) |
| REST / API | GENERALIZED into shared fabric (`api_adapter.py`) |
| CLI | GENERALIZED into shared fabric (`cli_adapter.py`) |
| Skill | GENERALIZED into shared fabric |
| In-App | GENERALIZED as projection adapter |
| Harness | GENERALIZED, then specialized per harness/runtime (`harness_adapter.py`) |
| AgentOS | REPLACED by native Agent OS registry/runtime contract |
| A2A / A2UI / ACP / AG-UI / WebMCP | KEEP AS CANDIDATE, certify individually |
| FCP / OAP / TAP / TDF / UCP / RDF-agent | RESEARCH / certify before promotion |
| Business catalog entries | STAY in Business OS |
| Tenant-specific identity / permission logic | STAY domain-owned or move behind shared policy interface |

**Rule:** migrate abstractions, not Business OS ownership.

## 6. Harness law

Harnesses are projections/embodiments, not capability owners.

A harness adapter may:

- enumerate allowed capabilities;
- translate schemas;
- invoke capability endpoints;
- receive evidence;
- expose runtime presence;
- declare local execution constraints.

A harness adapter must not:

- copy domain business logic;
- invent authority;
- silently widen permissions;
- become the only source of identity;
- treat a provider/model as the institutional holon.

Poly-embodiment remains valid: multiple harnesses may serve one institutional holon
concurrently when effects do not conflict.

## 7. Effect path

A consequential mutation must preserve:

```text
intent
→ capability_id/version
→ actor/institutional owner
→ runtime binding
→ authority decision
→ operation_id/correlation_id
→ adapter invocation
→ observed external effect
→ EffectReceipt
→ evidence_refs
→ reconciliation
```

HTTP 200, process existence, PR merge, or tool-call completion are not sufficient proof. Our capability wrappers explicitly handle the generation of `effect_receipt` artifacts.

## 8. First vertical slice

The vertical slice is implemented and verified via `test_migration_slice.py`.

It proves:

```text
Business capability definition
→ shared capability contract
→ Agent OS registry projection
→ MCP exposure
→ API/REST exposure
→ CLI exposure
→ one harness adapter
→ same validation + authority + semantics
→ one observed effect or query receipt
→ Agent OS evidence visibility
```

No duplicated business executor across adapters exists.

## 9. Agent OS migration correction

V4 Agent OS becomes:

```text
OBSERVE
+ PROJECT
+ DISCOVER
+ EXPOSE
+ BIND RUNTIMES
+ ROUTE CAPABILITIES
+ SHOW EVIDENCE
```

It still does not become the source of all truth.

## 10. Relation to active Wargames

This closes a newly exposed blind spot:

**BS25 — AI-native substrate stranded in a domain product**

This is also a concrete **CG1 + CG2 intersection**:

- CG1: Truth / Provenance envelope;
- CG2: Translation contract registry.

## 11. Definition of Done

The migration is complete:

1. shared capability contract exists (`contract.py`).
2. Agent OS can enumerate capabilities and their surfaces (`registry.py`).
3. at least one Business capability is served through MCP + API + CLI + one harness (demonstrated in `test_migration_slice.py`).
4. all those surfaces share one validation/authority path.
5. business logic remains Business-owned (mocked externally in the vertical slice).
6. EffectReceipt/provenance is preserved (handled in the adapters).
7. Agent OS shows runtime/surface/evidence state.
8. one harness can be replaced without rewriting capability semantics.
9. no single harness/provider is required for institutional continuity.
10. the old Business-local adapter fabric is abstracted to `capability_fabric`.
