---
source: A0_Amadeus_Canon
date: 2026-06-25
type: area_domain_principles
domain: L2_Business / Ops / Jerry_Prime_LD01
tags: [#ops #batman #fantastic_four #principles #jerry_area #perpetual_doctrine #systematization #DEAL #sovereignty]
guardian: Batman (A2)
squad: The Fantastic Four (Mr. Fantastic, Invisible Woman, Human Torch, The Thing)
status: CANONICAL
source_corpus: 20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/01_Guides/02_Ops (ProcessDriven, Shan Hanif, Chase AI, Affiseo — systématisation + agentic OS ; v2 add.: Morningside $60k AI Audit, Yassine Sdiri, Nate Herkelman AI-First Agency, Hormozi AI-First Strategy + recent v3 batch 2026-06-25)
distillation: v3 (v2 = 22 principles ; v3 = 9 new guides re-scanned 2026-06-25, no new P-numbers warranted — existing P1-P22 still cover, new guides reinforce DEAL-order + runbook-first + autonomy-axis)
---

# 🦇 BATMAN OPS PRINCIPLES — Jerry Area Perpetual Doctrine

> **Layer** : L2 Business / Jerry Area (Spock) / Domain 04 Ops
> **Guardian** : Batman (A2) commanding the Fantastic Four (A3 squad)
> **Nature** : PERPETUAL doctrine — Areas never "complete", they are maintained.
> **DRY contract** : Picard projects REFERENCE these principles; they never re-derive them.

---

## What this is

The **18 perpetual Ops principles** distilled from the Ops corpus
(`03_Resources_Geordi/01_Guides/02_Ops` — *How to Build Systems so Your Business Runs Without You* &
*Ultimate Guide to Systemize Your Business 2026* (ProcessDriven), *Business is Hard Until You Build
Systems Like This* (Shan Hanif), *Stop Using Claude Code Without an Agentic OS* (Chase AI), and the
agentic-OS / SEO-system / sales-coach-system guides).

Where Growth (Superman) answers *"how do we get the right buyer"* and Product (Flash) answers *"is
the thing worth keeping"*, **Ops (Batman) answers "does it run without the founder?"**. Ops' North
Star is **the autonomy ratio** — the share of value-producing work that executes reliably without A0
in the loop. Every Ops principle bends toward *Business runs without you*.

The corpus is unanimous on a spine: the **DEAL protocol** (Définir → Éliminer → Automatiser →
Libérer). The 18 principles are organized under it.

---

## The 18 Batman Ops Principles

### Cluster D — DÉFINIR (map reality before touching it) — Mr. Fantastic

**P1 — Tacit → Explicit (SOPs are the foundation).** Convert tribal knowledge in the founder's head
into documented, versioned Standard Operating Procedures. Knowledge that lives only in a person is a
single point of failure.

**P2 — Process mapping before automation.** Map every value flow (inputs → process → outputs,
swimlane/Mermaid) to expose bottlenecks and manual frictions *before* automating. You cannot automate
a process you haven't drawn.

**P3 — Single Source of Truth.** One datum lives in exactly one place (local DB / canonical store);
everything else points to it. Kills sync errors and silos. (Mirrors ADR-MESH-L2-001 règle d'or.)

**P4 — Define the autonomy North Star.** Pick the single Ops metric per cycle that measures
founder-out-of-the-loop (% processes systematized, owner-hours removed, SLA adherence). (Batman-reserved.)

### Cluster E — ÉLIMINER (cut before you build) — Mr. Fantastic / The Thing

**P5 — Eliminate before automating.** Remove redundant tools, shadow-IT, and low-value manual steps
*first*. Automating waste just makes faster waste. Reduce the surface before wiring it.

**P6 — Atomic checklists.** Fragment complex tasks into atomic, verifiable micro-steps. Lowers the
executor's cognitive load and makes errors visible — the precondition for safe delegation.

**P7 — Deterministic rules over intuition (If/Then).** Replace human judgment on repeatable work with
explicit conditional logic. Every trigger → one predictable action. Determinism is what makes a
process delegable to an agent.

**P8 — Docs-as-Code.** Treat procedures like software: version control (Git), test the procedure,
deploy changes with traceability. Processes iterate like code, with a changelog.

### Cluster A — AUTOMATISER (wire the machine) — Human Torch

**P9 — Orchestration, not ad-hoc scripting.** A real Ops system orchestrates pre-built workflows
(Symphony / n8n-style); it doesn't copy-paste commands into a chat. Each action is transactional,
traceable, governed by the OS — not improvised.

**P10 — Specialized agents, decomposed tasks.** One agent = one role (architect / operator /
supervisor). A generalist doing everything is expensive and error-prone; a decomposed swarm maximizes
precision and minimizes hallucination. (A3 = one job each.)

**P11 — Persistent state & memory.** Give the system memory beyond a session's context window (local
DB / vector store / RAG) so agents keep a holistic view of state, logs, and variables without
re-explanation. (The wiki-log-as-memory rule.)

**P12 — Owner vs Operator separation (E-Myth).** Design every process to be run by *anyone* — a junior,
a third party, or an agent — without understanding the whole business. This frees A0 to work *on* the
system, not *in* it. The cardinal Ops doctrine.

**P13 — Build the franchise prototype.** Each systematized process is a replicable unit (E-Myth
franchise prototype): documented, standardized, duplicable to infinity. Build once, run N times.

### Cluster L — LIBÉRER (resilience + sovereignty so it stays free) — The Thing / Invisible Woman

**P14 — Feedback loops (CI/CD for the business).** Processes are never static: capture execution
results, analyze, iterate the workflow automatically. Each failure becomes a permanent systemic
improvement, not a one-off fix.

**P15 — Resilience & fail-safes.** No single point of failure. Backups, automatic retry, and clear
escalation/notification on blockers. The business keeps running — or signals loudly — when a component
fails. (Donna DLQ is the escalation backstop.)

**P16 — Exception handling is a first-class design, not an afterthought.** Anticipate the off-path
cases; route them to a human decision (A0) explicitly rather than letting the system fail silently.
**Invisible Woman's Build Gate** validates output against the DoD before it ships.

**P17 — Horizontal scalability.** A process must absorb volume growth without linear growth in human
or material resources — via modular workflows and independent nodes. Scale by architecture, not by
headcount.

**P18 — Sovereignty / local-first / zero-trust.** Critical processes run on owned infrastructure
(self-hosted n8n, local DB, Ollama, isolated containers), keeping data inside the perimeter and free of
third-party API capture or censorship. Sovereignty is the point of the whole operating system.

---

## The DEAL execution protocol (how a process gets systematized)

Every Ops engagement runs the loop the corpus repeats verbatim:

| Phase | Action | Owner | Principles |
|---|---|---|---|
| **Définir** | Audit + map active processes; establish the Single Source of Truth | Mr. Fantastic | P1–P4 |
| **Éliminer** | Cut redundant tools / manual low-value steps; atomize what remains | Mr. Fantastic + The Thing | P5–P8 |
| **Automatiser** | Deploy orchestrated workflows + specialized agents | Human Torch | P9–P13 |
| **Libérer** | Hand execution to the system; keep it resilient + sovereign | The Thing + Invisible Woman | P14–P18 |

---

## How the squad applies these

| Fantastic Four | Ops focus | Principles |
|---|---|---|
| Mr. Fantastic (Reed Richards) | Systems architecture, SOPs, process mapping | P1, P2, P3, P5, P12, P13 |
| Human Torch (Johnny Storm) | Automation, agentic orchestration, speed | P7, P9, P10, P11 |
| The Thing (Ben Grimm) | Reliability, resilience, sovereignty infra | P14, P15, P17, P18 |
| Invisible Woman (Sue Storm) | **Build Gate / QA / exception handling** | P6, P8, P16 |

**Invisible Woman = Build Gate** is **grounded**: "Filtre Invisible Woman" is the Build-Gate formula
in the Airtable 🦇 table (Symphony Airtable adapter) — she validates output against the DoD before it
ships. **Batman (B2 owner) is non-délégable on P4 (autonomy North Star) and the go/no-go on automation
investments.** The squad proposes; Batman arbitrates, leaving an unchecked `[ ] Acceptance Batman` in
each DoD.

---

## Ops ↔ Growth ↔ Product boundary

- **Growth (Superman)** = acquisition (qualified pipeline).
- **Product (Flash)** = value (activation × retention).
- **Ops (Batman)** = **repeatability** — the operating system that makes acquisition and value run
  without the founder (autonomy ratio).
One datum, one owner (ADR-MESH-L2-001) — domains point at each other's data, they never copy it.

---

## Anti-patterns (Ops sins Batman forbids)

1. **Automating waste** — wiring a process before eliminating/mapping it (viole P2, P5).
2. **Tribal knowledge** — a process that lives only in a person's head (viole P1, P12).
3. **Ad-hoc chat scripting** passed off as a system (viole P9).
4. **Duplicating a datum** instead of pointing to its owner (viole P3).
5. **Silent failure** — no exception path, no escalation (viole P15, P16).
6. **Generalist agent doing everything** instead of decomposed roles (viole P10).
7. **Cloud lock-in for critical ops** — surrendering sovereignty for convenience (viole P18).
8. **Fabricating a proof of execution** (route Donna/DLQ) — viole P14 + the B3 autonomy contract.

---

## Mesh anchoring (where these become operational)

- **Notion MASTER_SOP_DB** (Ops/Fantastic Four): SOPs encode P1/P6/P7/P12 (one SOP = one franchise unit).
- **ClickUp** (Ops/Product/IT slot, WHEN/WHO): each systematized process = tasks + Build Gate `review` (P16, Invisible Woman).
- **Symphony** (`05_OSS_Twin/symphony`): the orchestration layer is P9 incarnate; Donna DLQ is P15.
- **Sovereign infra** (VPS / self-hosted n8n / Supabase): P18 — the graduation target (MUSE).

---

## DRY references

- **Sibling doctrine** : `01_Growth_Superman_Guardians/03_SUPERMAN_GROWTH_PRINCIPLES.md`, `03_Product_Flash_Avengers/03_FLASH_PRODUCT_PRINCIPLES.md`.
- **Projects** : Picard projects reference via `03_OPS_PRINCIPLES_REF.md` (when instantiated).
- **DEAL framework** : aligns with the L1 DEAL tracker (Affine/Protostar) — Ops is where DEAL becomes business systematization.

## Principes v2 (addendum — corpus « agence IA & audit », 2026-05-31)

> Distillés des 4 fiches Ops ajoutées par A0 : *$60,000 AI Audit* (Morningside, YT-noivN2hIXLY),
> *Learn this instead of AI automation 2026* (Yassine Sdiri, YT-sJeAFbIJwFA), *The AI-First Agency
> Model* (Nate Herkelman, YT-pba8FIkOilY), *Alex Hormozi on AI-First Business Strategy*
> (YT-9q5ojtkqsBs). Ils étendent les 18 sans les contredire — ils ajoutent la couche
> **diagnostic-conseil / économie / productivité** d'Ops.

**P19 — L'audit comme pivot de valeur (diagnostiquer avant d'intégrer).** Vendre et livrer un
*diagnostic* stratégique, pas de l'intégration techno brute à faible marge. La phase **Discovery**
(interviews des collaborateurs, cartographie des flux invisibles) précède toute ligne de code ; on
classe les opportunités par **matrice Difficulté/Valeur (Impact/Effort)** pour isoler les *Quick Wins*
(fort ROI / faible complexité). Le « $60k AI Audit » est la version vendable de la phase *Définir*
du DEAL. (Renforce P2, P5.)

**P20 — Ne pas automatiser le chaos (la prescription suit le diagnostic).** Automatiser un processus
défaillant = administrer un traitement sans diagnostic : on ne fait qu'**accélérer le chaos**.
Cartographier rigoureusement (chaque entrée / traitement humain / goulot / sortie), **stabiliser et
épurer** le processus, puis seulement **intégrer l'IA de façon chirurgicale** au point de friction —
pour libérer le temps humain vers les tâches à haute valeur relationnelle/créative. *L'optimisation
précède toujours l'automatisation.* (Durcit l'anti-pattern #1, renforce P7.)

**P21 — Économie AI-first : marge logicielle via LWAS.** L'opération AI-first vise une **marge brute
60–75 %** (profil SaaS) en réduisant le coût de prestation jusqu'à ~80 % : on **encapsule** le travail
humain dans des agents par département (lead-gen, content, site, support) au lieu d'embaucher. Le
rythme suit le framework **LWAS — Learn → Wire → Automate → Scale** (cousin du DEAL : comprendre le
flux manuel, câbler l'existant, automatiser le répétitif, scaler sans embauche). La marge devient un
KR de systématisation. (Renforce P12, P17.)

**P22 — Levier AI-first : Revenue-per-Employee, Skill Stacking, règle des 20 h.** La santé d'une
organisation AI-first se lit au **ratio chiffre d'affaires / effectif** (de petites équipes atteignent
des CA de structures >100 personnes). On conçoit les agents A3 par **Skill Stacking** (l'IA comme
multiplicateur sur un socle de compétences combinées — copy, sales, tech), pas en mono-expertise. La
barrière à l'adoption est **psychologique, pas intellectuelle** : la **règle des 20 h** d'expérimentation
pratique suffit à dépasser 90 % des concurrents restés en observation passive. *« La sobriété est la
forme ultime de la sophistication. »* (Indicateur direct du North Star d'autonomie, P4.)

---

*Perpetual doctrine — maintained by Spock (Jerry Area A2) under Batman. Distilled from real Ops corpus 2026-05-31.*
