# CORPUS 02 — Software Factory + Wargame Evidence Cross-Source Synthesis & Lineage Map

**Corpus ID:** CORPUS-02
**Parent Objective:** #220
**Constitutional Parent:** #311 (Fractal Holon Contract)
**Historical Acquisition Lane:** #222
**Author / Holon:** Bill (S3 Research)
**Date:** 2026-10-03

---

## 1. Executive Summary & Outcome

This synthesis transforms the 9-source research pack (Fable Wargame Kit + 8 video transcripts on AI Software Factories, Dark Factories, AI SDLC, Deterministic Security, Remote Runtimes, and GitHub Swarms) into a **bounded research corpus**.

This corpus proves that:
1. Software factories are **reusable machinery and runtimes**, not the identity or cognitive limit of Companion holons.
2. Companions remain **cognitively complete S3/A3/B3 holons** under #311, capable of independent perception, planning, execution, verification, and escalation.
3. High-risk autonomous execution requires pre-flight **Wargame simulations** (8 pass criteria) and non-bypassable **deterministic security gates**.
4. A0 is successfully removed from the operational loop without creating brittle script-monoliths.

---

## 2. Cross-Source Convergences (At Least 5 Required)

1. **Convergence 1: Multi-Tier Autonomy Bounded by Explicit Jurisdiction (Sources 01, 02, 05, 08)**
   - *Insight:* High-performing AI systems organize execution into explicit autonomy tiers with clear authority boundaries. Read/recon ops run autonomously, while state-mutating actions require policy clearance or test validation.
   - *A'Space Realization:* Tiers map to jurisdiction bounds (S1 file edits, S2 subsystem integration, S3 system orchestration) while preserving full cognitive completeness at every tier.

2. **Convergence 2: Deterministic Verification as the True Gate for Probabilistic Generation (Sources 01, 03, 06, 07)**
   - *Insight:* Probabilistic LLM code output cannot self-certify safety or correctness. Execution pipelines must enforce non-bypassable, deterministic test suites, linter passes, and provenance firewalls.
   - *A'Space Realization:* Implemented via double-entry gates (`gate.py`, `portfolio_firewall.py`, `truth_projection.py`). Code is generated probabilistically, but acceptance is strictly deterministic.

3. **Convergence 3: Asynchronous Headless Execution ("Dark Factory") via Persistent State Machines (Sources 03, 05, 07, 09)**
   - *Insight:* Long-running multi-hour refactors require headless execution where state is persisted asynchronously and execution resumes seamlessly across model or runtime restarts.
   - *A'Space Realization:* Agent OS Harness Runtime (`harness_runtime.py`) and Mission Continuity (`mission_continuity.py`) allow continuous background execution without requiring human (A0) babysitting.

4. **Convergence 4: GitHub-Native Control Plane as Canonical Control & Audit Ledger (Sources 02, 04, 05, 09)**
   - *Insight:* GitHub issues, pull requests, and webhooks provide the ideal transparent, immutable control plane for agent coordination and asynchronous handoffs.
   - *A'Space Realization:* Integrated via `dispatch_routing.py` and `yas_alert_sink.py`, mapping GitHub issues directly to holon mission briefs and PR proofs.

5. **Convergence 5: Simulation-First Risk Discovery via Wargames (Sources 01, 04, 06, 08)**
   - *Insight:* Before running state-mutating missions on production codebases, wargaming the scenario exposes hidden assumptions, failure modes, and required counter-moves.
   - *A'Space Realization:* Embedded via `wargame.py` and `test_wargame_protocol.py` enforcing the 8 Fable Wargame pass criteria prior to high-risk execution.

---

## 3. Contradictions & Limits Identified (At Least 3 Required)

1. **Contradiction 1: "Worker Compression" vs. Holonic Autonomy (Sources 03, 05 vs. Constitutional Invariant #311)**
   - *Industry Flaw:* Standard software factory literature frequently equates agents to "dumb workers" or single-step script runners managed by a central prompt.
   - *Resolution:* In A'Space OS V3, S3/A3/B3 holons (Ryan, River, Clara, etc.) are cognitively complete. Factories and scripts are *instruments* they invoke, never their institutional identity.

2. **Contradiction 2: Eager Full-Text Context Ingestion vs. Modular Context Isolation (Sources 02, 04 vs. Graphify / Research Atlas)**
   - *Industry Flaw:* Naive factory implementations try to shove the entire codebase into huge prompt windows, causing high token costs, hallucination, and rate limit exhaustion.
   - *Resolution:* Graphify (Source 08) and Research Atlas enforce 1-degree targeted context retrieval and knowledge graph indexing (`paper_microscope.py`, `discovery.py`).

3. **Contradiction 3: Pure Automated Flow vs. Necessary Human-in-the-Loop (HITL) Policy Gates (Sources 03, 07 vs. Wargame LEDGER / OMK-C)**
   - *Industry Flaw:* "Dark Factory" hype claims 100% human removal for all ops, ignoring destructive external actions (e.g. Supabase dashboard re-provisioning, billing changes).
   - *Resolution:* As proven in the Fable Wargame LEDGER (OMK-C trace), destructive UI/external cloud moves are explicitly flagged as `A0 HITL pending` while safe local moves execute autonomously.

---

## 4. Factory / Flow Boundary: Explicit Modeling (Clara ↔ Ryan ↔ River)

To prevent domain collision and maintain clear stewardship:

```
+-----------------------------------------------------------------------------------+
|                                CLARA (S3 Design / Forge)                          |
|  - Owns intent distillation, architectural specs, contracts, & acceptance criteria|
|  - Validates PRs against architectural invariants                                |
+-----------------------------------------------------------------------------------+
                                         |
                                         v  (Architectural Acceptance)
+-----------------------------------------------------------------------------------+
|                                RYAN (S3 Build / Industrialization)                |
|  - Industrializes factory machinery, harnesses, adapters, and build pipelines     |
|  - Packages Dark Factory automation & deterministic gate scripts                  |
+-----------------------------------------------------------------------------------+
                                         |
                                         v  (Capability / Factory Machinery)
+-----------------------------------------------------------------------------------+
|                                RIVER (S3 Flow / Operations)                       |
|  - Consumes industrialized factories to execute live business/code flows           |
|  - Manages mission dispatch, queue flow, effect sequencing, & execution velocity |
+-----------------------------------------------------------------------------------+
                                         |
                                         v  (Telemetry & Evidence)
+-----------------------------------------------------------------------------------+
|                         YAZ / GRAHAM / RORY / DOCTOR13                            |
|  - Yaz: Audits drift & metrics | Graham: Persists knowledge | Rory: UI view       |
+-----------------------------------------------------------------------------------+
```

- **Clara (Design):** Defines *what* success looks like (contracts, schemas, Wargame criteria).
- **Ryan (Build):** Builds *how* the factory executes (harnesses, container runners, gate scripts).
- **River (Flow):** Drives *when* and *which* work items flow through the factory to achieve live effects.

---

## 5. Explicit Anti-Simplification Rules

In strict compliance with #311 and the issue requirements:
- **Ryan ≠ builder worker:** Ryan is an S3 holon who owns industrialization strategy and build execution authority.
- **Yaz ≠ monitoring agent:** Yaz is an S3 holon who exercises analytical judgment over telemetry, drift, and systemic health.
- **Graham ≠ memory database:** Graham is an S3 holon who curates institutional knowledge, ontology, and cognitive treasury.
- **River ≠ workflow automation:** River is an S3 holon who manages operational flow, sequencing, and effect stewardship.

Each Companion possesses full perception, planning, execution, verification, and escalation capabilities.

---

## 6. Lineage Map

`SourcePattern -> RuntimePrimitive -> HolonImpact -> CandidateCapability -> ValidationNeed`

| Source Pattern | Runtime Primitive | Holon Impact | Candidate Capability | Validation Need |
| :--- | :--- | :--- | :--- | :--- |
| **01: Fable Wargames** | `wargame.py` simulation harness | Bill / River pre-flight scenario evaluation | `capability_wargame_simulation` | Pass 8/8 criteria in `SUCCESS.md` |
| **02: Autonomy Config** | Bounded jurisdiction gates | Clara / Ryan clear scope definition | `capability_jurisdiction_guard` | `test_mission_continuity.py` |
| **03: Dark Factory** | Headless background pipeline (`dark_factory.py`) | Ryan build execution, River queue consumption | `capability_dark_factory_build` | `test_p4_canary.py` lights-out run |
| **04: AI SDLC** | Workgraph state transitions (`uc_workgraph.py`) | Clara -> Ryan -> River -> Yaz multi-holon flow | `capability_holonic_sdlc` | `test_uc_workgraph.py` |
| **05: Factory Revolution** | Machine fabric adapters (`harness_runner.py`) | Ryan factory industrialization | `capability_factory_fabric` | `run_v0_local_acceptance.py` |
| **06: Security Gates** | Double-entry deterministic gates (`gate.py`, `portfolio_firewall.py`) | Clara security spec enforcement | `capability_deterministic_gate` | `test_truth_projection.py` |
| **07: Remote Harness** | Containerized session runner (`harness_runtime.py`) | Ryan remote execution, Graham state reconcile | `capability_remote_harness` | `test_harness_runtime.py` |
| **08: Simple Factory** | Modular script instruments (`uc.py`, `harness.py`) | Ryan instrument crafting | `capability_modular_instrument` | `test_uc_workgraph.py` |
| **09: GitHub Swarm** | Issue/PR dispatch router (`dispatch_routing.py`) | Nardole dispatch, River flow tracking | `capability_github_control_plane` | `test_dispatch_routing.py` |

---

## 7. Provenance References

- `20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/Wargames/Fable_Wargame_Kit/fable_wargame_kit_source.zip`
- `30_Business_OS/09_Blueprints/agentic-os/transcriptions/01-self-improving.txt`
- `30_Business_OS/09_Blueprints/agentic-os/transcriptions/02-graphify.txt`
- `30_Business_OS/09_Blueprints/agentic-os/transcriptions/03-fable5-agentic-os.txt`
- `30_Business_OS/09_Blueprints/agentic-os/transcriptions/04-second-brain-fable5.txt`
- `30_Business_OS/09_Blueprints/agentic-os/transcriptions/05-cinq-couches.txt`
- `30_Business_OS/09_Blueprints/agentic-os/transcriptions/06-runs-my-business.txt`
- `30_Business_OS/09_Blueprints/agentic-os/transcriptions/07-remplace-openclaw.txt`
- `30_Business_OS/00_Architecture/CONSTITUTION/FRACTAL_HOLON_CONTRACT.md`
