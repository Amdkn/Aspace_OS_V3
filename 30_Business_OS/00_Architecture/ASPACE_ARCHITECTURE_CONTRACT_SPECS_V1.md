# A'Space Architecture Contract Specifications v1

**Scope:** Business OS / The OMK Services semantic full stack  
**Owner:** Clara / DESIGN-FORGE  
**Date:** 2026-09-30  
**Status:** Proposed canonical contract stack  
**Doctrine:** These specifications complement SDD / PRD / ADR / DDD / TDD. They do not replace them.

## 1. Why A-SPEC exists

Classical documents remain useful:

- SDD: system intent and architecture direction.
- PRD: product requirements and user/business outcomes.
- ADR: architectural decisions and consequences.
- DDD: bounded implementation directives.
- TDD: test design and verification.

They are insufficient by themselves for a multi-repository, multi-surface, agent-operated product because they do not guarantee that product names, domain objects, capabilities, workflows, authority, external effects, deployment and evidence preserve one meaning across repositories and runtimes.

**A-SPEC** is the executable semantic contract layer between product meaning and implementation.

A-SPEC answers:

```
What does this thing mean?
Who owns its state?
Which capability changes it?
Which commands / queries / events exist?
Which state transitions are legal?
Which authority is required?
What external effect proves completion?
How is retry/replay made safe?
Which surfaces project it?
Which repository implements it?
How does the contract migrate without semantic drift?
```

A-SPEC documents are therefore **cross-repository contracts**, not screen specs and not repo-specific task lists.

---

## 2. Product semantics freeze

The current product family must use the following vocabulary until an explicit PSS migration replaces it.

| Concept | Canonical meaning |
|---|---|
| **The OMK Services** | organization / operating company |
| **The OMK Office** | market-facing client-service product: acquisition, catalog, onboarding and client access |
| **OMK Business OS** | authenticated operations engine / back-office |
| **Coach OS** | vertical configuration of Business OS for coaches / consultants / operators |
| **OMK Mobile** | edge/mobile projection of the same Business OS state and capabilities |
| **Business OS Factory** | A'Space internal control plane that compiles tenant/brand/offer/workflow/policy configurations |
| **OMK / ABC / Marina / future operators** | tenant/operator/franchise instances, not separate software architectures |

### Repository roles

Repositories are not products. Every Business repository must have exactly one lifecycle role:

- `CANONICAL`
- `UPSTREAM_COMPONENT`
- `ARCHIVED_LINEAGE`

Current intended mapping:

- `Amdkn/The-OMK-Office-V1-JaaS-Landing-Site-Web` → PUBLIC / The OMK Office front door.
- `omk-services/OMK-DESKTOP-WEB-OS` → CANONICAL operations engine.
- `Amdkn/The-OMK-Mobile-Back-Office` → EDGE projection / upstream component to converge.
- `30_Business_OS/` in Astra → FACTORY control plane.
- historical BusinessOS / Business-Office-3-OS / SaaS Garden / AI Studio repos → lineage or upstream only after explicit extraction.

**Invariant:** surface ≠ product ≠ repository.

---

## 3. A-SPEC registry

### PSS — Product Semantics Specification

**Question:** What is the product, for whom, under which brand, on which surface?

Required contract:

- Organization
- Brand
- Product
- Offer
- Audience
- Tenant
- Workspace
- Role
- Surface
- ProductContext
- repository role / lineage
- positioning promise
- automation maturity exposed to the user

Required outputs:

- canonical glossary;
- ProductContext schema;
- product/surface matrix;
- repo lineage matrix;
- prohibited aliases / superseded names;
- migration map for old names.

A PSS prevents `Coach OS == Business OS == The OMK Office` style semantic collapse.

---

### UDM — Unified Domain Model Specification

**Question:** Which business objects exist, what do they mean, and who owns them?

Minimum objects:

- Organization
- Brand
- Product
- Offer
- Audience
- Tenant
- Workspace
- Membership
- Role
- Customer
- Lead
- Booking
- Case
- DocumentRequest
- Payment
- Workflow
- Capability
- Subscription
- Entitlement
- EffectReceipt

Required outputs:

- bounded contexts;
- aggregate boundaries;
- canonical identifiers;
- write authority;
- read projections;
- lifecycle ownership;
- invariants;
- migration/version rules.

A UDM is not a database schema. Databases project the UDM.

---

### CCS — Capability Contract Specification

**Question:** What reusable business capability exists independently of UI, transport or repository?

Examples:

- `customer.intake`
- `case.progress.read`
- `document.request.create`
- `booking.create`
- `billing.collect`
- `task.execute`
- `notification.send`
- `tenant.provision`

Every Capability Contract defines:

- capability_id;
- version;
- intent;
- inputs / outputs;
- preconditions;
- authority / policy;
- deterministic validation;
- side effects;
- idempotency semantics;
- compensation semantics;
- evidence requirements;
- supported projections/adapters.

A capability may be projected through React, HTTP, Mobile, CLI, MCP, Webhook or Cron without becoming seven implementations of business meaning.

### Command / Query / Event rule

Capability services must distinguish:

- **Query** — asks for state and creates no business mutation.
- **Command** — expresses an intended mutation.
- **Event** — records an observed fact that already occurred.

Generic CRUD is not the canonical business contract.

---

### WER — Workflow, Event & Receipt Specification

**Question:** How does business state move, what proves a transition, and how does the system recover?

Every workflow defines:

- state machine;
- allowed transitions;
- triggering command/event;
- authority;
- required evidence;
- human approval gates;
- timeout rules;
- retry safety;
- compensation;
- terminal states.

Example:

```
Lead
→ Diagnostic
→ Qualified
→ Booking
→ Sale
→ Provisioning
→ Delivery
→ Fulfilled
→ Renewal
```

External mutation completion requires an `EffectReceipt`, not merely HTTP 200.

Minimum EffectReceipt:

- operation_id;
- correlation_id;
- causation_id;
- capability_id + version;
- source;
- target;
- idempotency_key;
- requested_at;
- observed_at;
- observed_effect;
- evidence_refs;
- retry_safe;
- compensation_ref;
- status: SUCCEEDED | FAILED | UNKNOWN.

**Invariant:** UNKNOWN ≠ FAILED ≠ retry-safe.

Human-in-the-loop is a first-class workflow state such as `REQUIRES_HUMAN`, with assignment, SLA and receipt.

---

### TPE — Tenant, Policy & Entitlement Specification

**Question:** Who may do what, for which tenant, under which product/package?

Separate explicitly:

- identity;
- organization membership;
- active tenant;
- role;
- scopes;
- capability permissions;
- policy;
- subscription;
- entitlement;
- deployment ownership.

Product packaging such as Cloud / Dedicated / Sovereign is a profile over the same product contracts, not three codebases.

A TPE must define:

- tenant isolation contract;
- RLS expectations;
- entitlement feature matrix;
- plan limits;
- infrastructure ownership;
- approval rules;
- audit obligations.

---

### RID — Runtime, Integration & Deployment Specification

**Question:** Where does the capability execute, through which adapter, and how is it released safely?

External systems are adapters behind capabilities:

- PaymentProvider
- CalendarProvider
- MessagingProvider
- DocumentProvider
- GWSProvider
- GitHubProvider
- AnalyticsProvider

Required DeploymentProfiles include, when relevant:

- public web;
- API runtime;
- background worker;
- webhook receiver;
- scheduled jobs;
- mobile edge;
- shared Supabase;
- dedicated Supabase;
- self-hosted / sovereign;
- secrets and environment promotion.

RID also owns contract compatibility requirements:

- API schema compatibility;
- DB migration compatibility;
- webhook replay;
- duplicate payment handling;
- mobile reconnect;
- adapter timeout;
- failed provisioning;
- rollback;
- deployment health.

---

### FCS — Franchise Configuration Specification

**Question:** How does Business OS Factory compile a new operator without forking the product?

Canonical configuration bundle:

```
TenantProfile
+ BrandProfile
+ OfferCatalog
+ WorkflowProfile
+ SOPBundle
+ PolicyBundle
+ EntitlementProfile
+ DeploymentProfile
→ Operable Product Instance
```

OMK, Coach, ABC, Marina and future operators should be configurations over the same engine wherever technically possible.

FCS acceptance requires that a new instance can be produced without copying business logic into a new repository.

---

## 4. Common A-SPEC envelope

Every A-SPEC issue/document must contain:

```yaml
spec_id:
spec_type:
version:
status: DRAFT | ACCEPTED | IMPLEMENTING | VERIFIED | SUPERSEDED
owner:
origin_objective:
consumers:
repositories:
product_surfaces:
bounded_contexts:
capabilities:
authority:
state_owners:
evidence_required:
migration_from:
supersedes:
```

Every spec must explicitly state:

1. canonical terminology;
2. invariants;
3. authority boundaries;
4. inputs / outputs;
5. state ownership;
6. commands / queries / events;
7. effects and receipts;
8. failure / UNKNOWN behavior;
9. migration and versioning;
10. implementation consumers;
11. contract tests;
12. release evidence.

A spec is not `VERIFIED` because a document exists. It is VERIFIED only when consuming implementations prove the contract.

---

## 5. GitHub operating model

GitHub is part of the architecture, not merely the code host.

- **Discussion** = divergent exploration / signal.
- **Objective Issue** = accepted business outcome.
- **A-SPEC Issue** = versioned architecture contract.
- **Implementation Issue** = bounded mutation consuming an accepted spec.
- **PR** = mutation + tests + evidence.
- **Worktree** = isolated execution environment.
- **Gate** = evidence checkpoint inside the same mission.
- **WorkGraph** = machine coordination / execution identity.

**Gate ≠ future project.**

A spec issue must remain linked to all consuming implementation issues/PRs until its release acceptance is proven.

---

## 6. GitHub Project definition

Target Project:

**The OMK Services — Semantic Full Stack & Launch**

Recommended fields:

- Object Type: Objective | A-SPEC | Build Cell | Release Gate | Incident
- A-SPEC: PSS | UDM | CCS | WER | TPE | RID | FCS
- Product Surface: Public | Operations | Edge | Factory | Cross-cutting
- Product: OMK Office | Business OS | Coach OS | Mobile | Factory
- Repo Role: Canonical | Upstream | Archived Lineage | Cross-repo
- Owner Capability: DESIGN | BUILD | FLOW | INTERFACE | STATE | COHERE | DISPATCH | OBSERVE
- Gate: Semantic | Contract | Build | Integration | Evidence | Release
- State: Proposed | Accepted | Building | Verifying | Waiting | Done
- Release: Launch Cohort | General SaaS | Future

Views:

1. **Architecture Contracts** — grouped by A-SPEC.
2. **Product Surfaces** — grouped by Public / Operations / Edge / Factory.
3. **Launch Cohort** — only objects necessary for first real customer.
4. **Repo Convergence** — Canonical / Upstream / Archive.
5. **Evidence Gates** — verification state and blockers.

---

## 7. Release criterion

The Semantic Full Stack is not complete when all specs are written.

The first release is proven when one real economic journey is traceable end-to-end:

```
lead
→ diagnostic
→ booking
→ sale or explicit human-assisted sale
→ customer
→ workspace
→ case/service delivery
→ external effects
→ EffectReceipts
→ fulfillment
→ evidence-backed client state
```

Every displayed operational state must be explainable by:

```
value
source
observed_at
authority
evidence
freshness
```

**No provenance → no green state.**
