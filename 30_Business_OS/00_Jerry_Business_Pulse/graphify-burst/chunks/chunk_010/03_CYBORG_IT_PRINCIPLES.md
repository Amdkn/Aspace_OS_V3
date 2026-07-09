---
source: A0_Amadeus_Canon
date: 2026-05-31
type: area_domain_principles
domain: L2_Business / IT / Jerry_Prime_LD01
tags: [#it #cyborg #kang_dynasty #principles #jerry_area #perpetual_doctrine #sovereign_ai #agentic_engineering #local_first]
guardian: Cyborg (A2)
squad: The Kang Dynasty (Kang Prime, Iron Lad, Scarlet Centurion, Immortus, Victor Timely, Rama-Tut)
status: CANONICAL
source_corpus: 03_IT (Geordi Guides — Cole Medin, Mark Kashef, cocadmin, AI Stack Engineer, GithubAwesome) + B3 Kang Dynasty squad canon + control room
distillation: v1 (corpus IT distillé → 18 principes ; backlog 322 fiches indexées dans IT_CHANNELS_BULK_AUDIT.md)
---

# 🤖 CYBORG IT PRINCIPLES — Jerry Area Perpetual Doctrine

> **Layer** : L2 Business / Jerry Area (Spock) / Domain 05 IT
> **Guardian** : Cyborg (A2) commanding the Kang Dynasty (A3 squad)
> **Nature** : PERPETUAL doctrine — Areas never "complete", they are maintained.
> **DRY contract** : Picard projects REFERENCE these principles; they never re-derive them.

---

## What this is

The **18 perpetual IT principles** distilled from the real IT corpus
(`03_Resources_Geordi/01_Guides/03_IT` — Cole Medin's agent-harness / local-AI-stack /
local-AI-agents guides, Mark Kashef's self-improving Claude Code systems, cocadmin's
network/infra formations, AI Stack Engineer) **plus the Kang Dynasty squad canon** (the
infra/VPS/Dokploy/DNS reality A'Space actually runs on). Picard projects apply them; the
project-specific HOW lives there.

Where Growth gets the buyer, Sales converts, Product delivers value, and Ops makes it
repeatable, **IT (Cyborg) builds and defends the machine that all of them run on**. IT's
North Star is **operational integrity**: system latency, zero critical security incidents,
and data integrity (KR-5a 0 critical / <3 medium incidents per quarter, KR-5b weekly backup
verified quarterly, KR-5c tech debt <20% of engineering capacity).

The corpus is unanimous on one stance: **sovereign, local-first, agentic engineering** — own
the stack, run it locally, let supervised agents build it, never rent dependency from GAFAM.

> ⚠️ Corpus quality note: a subset of the 322 IT fiches are degenerate template boilerplate
> (sentences with the literal word "Code"/"Engineer" substituted into a generic frame). Those
> were **not** used as sources. The principles below trace only to the substantive fiches.

---

## The 18 Cyborg IT Principles

### Cluster A — Agentic Engineering (the build engine) — Kang Prime / Victor Timely

**P1 — Multi-level agent orchestration (A2 supervises, A3 executes).** A supervisor delegates
cognitive sub-tasks (code analysis, test generation, refactor) to technician agents. This is
A'Space's own A0–A3 hierarchy: it minimizes behavioural drift and token over-consumption while
maximizing functional conformance. (Cole Medin — agent harnesses.)

**P2 — One agent, one role (decomposed tasks).** Decompose a problem into specialized agents
(refactor / test / docs) coordinated by a central orchestrator that validates intermediate
outputs before integration. Generalist-does-everything is expensive and error-prone.

**P3 — Test-Driven Agent Development (TDAD).** An agent writes its own integration tests before
touching business code — forcing it to make boundary conditions and error cases explicit, and
guaranteeing structural non-regression. (The IT-side mirror of Ops P14.)

**P4 — Cognitive resilience: error-injection auto-correction.** When a compiler/linter throws,
the supervision framework injects the error + the modification history back into the agent's
prompt, driving an autonomous iterative correction loop instead of a synchronous human bottleneck.

**P5 — Self-improving feedback loop.** Plan → execute → evaluate → correct, continuously. Failures
become training data; quality is gated by objective automated metrics (linting, coverage,
benchmarks) wired into the auto-correction prompt. (Mark Kashef — self-improving systems.)

**P6 — Adaptive prompt engineering.** The system generates and optimizes its own system/user
prompts as the project evolves, rather than using static prompts — it learns to ask Claude Code
more effectively under the constraints it actually hits.

### Cluster B — Context & Memory — Immortus

**P7 — Context-window management is core engineering.** Feed agents only the relevant fragments
via semantic sliding windows, AST (Abstract Syntax Tree) dependency-graph extraction, and
compression. The art is relevance at the right moment, not stuffing the window.

**P8 — Persistent state & long-term memory.** Maintain a persistent representation of project
state (dependencies, prior architectural patterns, historical errors) in a local vector store so
the model keeps global coherence beyond a single context window.

**P9 — Local RAG, grounded answers only.** Retrieval-Augmented Generation over a self-hosted
vector DB (ChromaDB/Qdrant) ensures agents answer from the private corpus, never leaking or
inventing from external data. (Mirrors People/Beast brand-book RAG and the Symphony context_pack.)

### Cluster C — Sovereign Local Stack (anti-GAFAM) — Kang Prime / Scarlet Centurion

**P10 — Local inference first.** Run quantized models (GGUF/GPTQ — Llama/Mistral) locally via
Ollama: near-zero latency, zero recurring API cost, absolute confidentiality. The workstation
becomes an autonomous compute node.

**P11 — Sovereign tooling over SaaS.** Prefer self-hosted equivalents — Open WebUI over ChatGPT,
n8n over Zapier/Make, Qdrant over Pinecone. No telemetry, no lock-in, runs offline.

**P12 — MCP as the standardized local connector.** Expose local data (SQLite/Postgres/FileSystem)
to LLMs via Model Context Protocol servers, so the Digital Twin's data is reachable without
leaving the perimeter or touching a proprietary remote API.

**P13 — Data sovereignty / anti-GAFAM.** IP, secrets, and sensitive data never transit a
third-party cloud under foreign jurisdiction. Prefer an internal failure point you control over a
rented external dependency you don't. (The bedrock A'Space stance.)

### Cluster D — Infrastructure & Security (Kang Dynasty's specialty) — Scarlet Centurion / Rama-Tut / Victor Timely

**P14 — Infrastructure as Code.** Provision the network/VPS/topology with Terraform/Ansible,
idempotent and versioned — the Digital Twin is defined by code, not by clicking a cloud console.
Enables disaster redeploy. (Real stack: Hostinger VPS + Dokploy.)

**P15 — Containerization & reproducibility.** Package services in Docker/Docker Compose (Dokploy
orchestration) pinning exact versions of models, libraries, dependencies — portable and scalable
from local box to edge cluster.

**P16 — Network isolation & defense-in-depth.** Apply VPC logic locally: segment public/private
subnets, distinguish stateful firewalls (Security Groups) from stateless ones (NACLs), use private
service endpoints, and tunnel with WireGuard/Tailscale. Critical workloads never face the public net.

**P17 — Sandboxed, atomic, immutable changes.** Agents operate in a sandbox; source files stay
immutable via shadow-copy / ephemeral volumes. Each proposed change passes syntactic validation +
unit tests before an **atomic** merge to main. Access via ephemeral tokens only. (Build Gate:
zero leaked secret in logs — Yaz Watchdog scan.)

**P18 — Observability & traceability.** Document agent decisions as ADRs + standardized Markdown
activity logs; run health monitoring (Uptime Kuma + PM2 endpoints, ADR-INFRA-001). An unauditable
system is an ungoverned one. (Build Gates: VPS provisioning <5 min payment-to-active; Solaris
uptime >99.5% monthly.)

---

## How the squad applies these (Kang Dynasty — canon Notion)

| Kang Dynasty member | IT focus | Principles |
|---|---|---|
| Kang Prime | Lead infra — VPS / DNS / Dokploy architecture | P1, P10, P12, P14 |
| Iron Lad | Fast provisioning, bootstrap scripts (Hostinger API) | P14, P15 |
| Scarlet Centurion | Network security, firewall, SSL/TLS | P13, P16, P17 |
| Immortus | Long-term capacity planning, scaling, memory | P7, P8 |
| Victor Timely | CI/CD discipline, time-boxed deployments | P3, P5, P18 |
| Rama-Tut | Backup & disaster recovery | P15, P18 (KR-5b) |

**Cyborg (B2 owner) owns IT architecture decisions outright — Jerry does NOT make them** (per the
control room). The squad executes; Cyborg arbitrates architecture and leaves an unchecked
`[ ] Acceptance Cyborg` in each DoD. Escalate to Jerry if monthly uptime <99% or infra MTTR >1h.

---

## IT ↔ neighbours boundary

- **Ops (Batman)** = repeatable *business* processes (SOPs, the operating system). **IT (Cyborg)**
  = the *technical* substrate those processes run on (infra, security, AI systems, data). Ops says
  "what the process is"; IT says "the machine is up, secure, and sovereign."
- IT serves every domain (Sales' Stripe, Finance's Airtable, Growth's RAG) but **owns none of
  their data** — one datum, one owner (ADR-MESH-L2-001). IT provides the secure substrate; it points.

---

## Anti-patterns (IT sins Cyborg forbids)

1. **Manual SSH on prod VPS** without a traced ClickUp ticket (Kang canon).
2. **Deploy without CI/CD** (no direct `scp`) — violates P14/P18.
3. **Changing DNS without propagation check** post-change.
4. **Renting GAFAM dependency** for sensitive workloads when a sovereign local option exists — P13.
5. **Stuffing the context window** instead of relevance-managing it — P7.
6. **Leaking a secret into logs** — P17 (Build Gate failure).
7. **Generalist agent doing everything** instead of decomposed roles — P2.
8. **Fabricating a proof of execution** (route Donna/DLQ) — P5 + the B3 autonomy contract.

---

## Mesh anchoring (where these become operational)

- **Sovereign infra**: Hostinger VPS + Dokploy + Hostinger DNS API + Supabase (managed Postgres);
  CI/CD GitHub Actions → Dokploy webhook; monitoring Uptime Kuma + PM2 (ADR-INFRA-001).
- **SOPs** (Kang canon): SOP-L2-IT-001 Provision VPS Nexus · -002 Deploy Solaris via Dokploy ·
  -003 Rotate Hostinger API keys (quarterly) · -004 VPS backup snapshot (weekly).
- **Symphony / Shadow L0**: the multi-agent orchestration (P1) and self-correction (P4/P5) are the
  heartbeat mesh; Donna DLQ is the escalation backstop.
- **Local AI stack**: Ollama + Open WebUI + n8n + Qdrant + MCP — the sovereign substrate (P10-P12).

---

## Extension plan / backlog

`IT_CHANNELS_BULK_AUDIT.md` indexes **364 IT-classified videos** across 10 channels (Cole Medin,
Mark Kashef, cocadmin, AI Stack Engineer, GithubAwesome, World of AI, RoboNuggets, Julian Goldie,
Manu AGI, Itssssss Jack — the last two largely noise). Only a sample is distilled into v1. v2 should
mine: Cole Medin's full agentic-engineering set, cocadmin's Linux/Docker/networking depth, and the
GithubAwesome self-hosted-tooling ecosystem. Bump `distillation:` to v2 then.

---

## DRY references

- **Sibling doctrine** : `04_Ops_Batman_Fantastic4/03_BATMAN_OPS_PRINCIPLES.md` (closest neighbour), `01_Growth…`, `03_Product…`.
- **Domain identity / KRs** : `00_B2_DOMAIN_CONTROL_ROOM.md` + `README.md` (KR-5a..c).
- **Squad canon** : `B3_Squad_KangDynasty/00_B3_SQUAD_CANON.md` (roster + stack + SOPs + gates).
- **Infra ADR** : ADR-INFRA-001 (monitoring), and the Symphony specs in `00_Amadeus/05_OSS_Twin/symphony`.

## Sources distilled

- Cole Medin — *Anthropic masterclass on agent harnesses* → P1, P2, P3, P4, P7, P17, P18.
- Cole Medin — *The ONLY AI Tech Stack You Need in 2026* → P10, P11, P12, P9.
- Cole Medin — *Ultimate Guide to Local AI and AI Agents* → P9, P10, P13, P15.
- Mark Kashef — *How to Build Self-Improving Systems in Claude Code* → P5, P6, P8.
- cocadmin — *Formation complète Réseau AWS (VPC)* → P14, P16.
- Kang Dynasty squad canon + control room → squad table, stack, SOPs, gates, KR-5a..c.

*Perpetual doctrine — maintained by Spock (Jerry Area A2) under Cyborg. Distilled from real IT corpus + Kang canon, 2026-05-31.*
