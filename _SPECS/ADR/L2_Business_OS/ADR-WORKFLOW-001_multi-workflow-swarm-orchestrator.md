---
id: ADR-WORKFLOW-001
title: Multi-Workflow × Swarm-Orchestrator — Process Canonique 6-Phases pour Création Landing Page de Grande Valeur
status: RATIFIED
ratification:
  by: "A0 Amadeus"
  date_iso: "2026-07-06"
  gate_a0_signed_off: true
  approval_token: "RATIFICATION-BATCH-01-2026-07-06-TIER-0"
  context: "Ratification Tier 0 foundational DDD Landing Pages — 4 ADR bases (ANTI-TEMPLATE + ANTI-PAPERCLIP + SKILLS-CANON + WORKFLOW) ratifiés en bloc suite Phase 5 multi-workflow validée."
date: 2026-07-06
last_updated: 2026-07-06 (Claude Code B1 E-Myth Gatekeeper — distilled from SKILL `multi-workflow` (6 phases canoniques) + SKILL `swarm-orchestrator` (A2 E-Myth patterns) + CLAUDE.md §'🕷️ Doctrine Swarm Orchestration' + ADR-META-001 D1-D8)
deciders: [A0 Amadeus]
proposed_by: Claude Code (B1 E-Myth Gatekeeper, on A0 directive "rédige ADR canonique workflow landing canon multi-workflow × swarm-orchestrator")
domain: L2 Business OS / Workflow Canon / Multi-Workflow / Swarm Orchestration / Landing Page AaaS / B1 E-Myth
tags: [#ADR #workflow #multi-workflow #swarm-orchestrator #landing-page #aaas #orchestration #e-myth #b1-gatekeeper #a2-strategic #a3-subagents #six-phases #anti-paperclip #adr-meta-001]
related: [ADR-NEXUS-LANDING-PERSONAS-001, ADR-ICP-NEXUS-001, ADR-AAAS-PRICING-001, ADR-L2-AAAS-001, ADR-META-001, ADR-META-005, ADR-SOBER-002, PRD-NEXUS-EVOLUTION-IA-001, plan-L2-business-os.md, plan-L1-life-os.md]
supersedes: none
sources_canons: [
  "SKILL `multi-workflow` (chargé en session, canon sibling) — 6 phases canoniques : Research → Ideation → Plan → Execute → Optimize → Review",
  "SKILL `multi-workflow` Phase 1 Research — prompt enhancement + score ≥7 sur 5 critères (goal / expect / scope / constraint) avant de continuer",
  "SKILL `multi-workflow` Phase 2 Ideation — parallèle multi-modèle (Codex backend + Gemini frontend)",
  "SKILL `multi-workflow` Phase 3 Plan — collaborative, ADR sister canon rédigé avant toute exécution",
  "SKILL `multi-workflow` Phase 4 Execute — Claude avec feedback milestones, sub-agents en background",
  "SKILL `multi-workflow` Phase 5 Optimize — multi-model parallel review (Codex security/perf + Gemini a11y/UX)",
  "SKILL `multi-workflow` Phase 6 Review — final eval A0 + checklist self-critique 5 critères",
  "SKILL `swarm-orchestrator` Identity — 'Strategic Orchestration Manager (E-Myth A2)' — Main Agent = A2, jamais A3 technicien",
  "SKILL `swarm-orchestrator` Core Principle — 'Delegate to Background, Never Execute Directly' (verbatim)",
  "SKILL `swarm-orchestrator` Swarm Patterns — Single-Task / Parallel / Chain delegation",
  "SKILL `swarm-orchestrator` When to Delegate — Code / Files / Search / Config / Build / Docs / Multi-step workflows",
  "SKILL `swarm-orchestrator` When NOT to Delegate — Pure questions / Read-only inspection / Summaries / User asks Main Agent to do work directly",
  "CLAUDE.md §'🕷️ Doctrine Swarm Orchestration' — Main Agent (Claude Code A2) ne fait jamais de travail technique direct. Délègue TOUT à des sub-agents en arrière-plan via run_in_background: true. Patterns : sub-agents parallèles / chain delegation / spécialisés.",
  "CLAUDE.md §'Rôles' — A2 = Orchestrateur Stratégique (analyse, délègue, coordonne, présente rapport). A3 = Exécuteurs techniques (reçoivent tâches via Agent tool, exécutent en background, rapportent).",
  "CLAUDE.md §'Doctrines §Mindsets' — A1 Beth (Ikigai, ALIGN→REASON→ACT→OBSERVE→RE-EVALUATE→VERIFY) + A1 Morty (Focus/12WY, FOCUS→REASON→ACT→OBSERVE→RE-EVALUATE→VERIFY→TRACK) + S1 Rick (Sobriété différé Q4 2026/Q1 2027, kernel pivots only)",
  "CLAUDE.md §'Mindsets — Discipline porting layer' — A3 = 35 sub-agents canon, dispatchers via Morty/Beth Dispatch Doctrine",
  "MEMORY.md §'A0 Divinity Arsenal Doctrine 2026-06-20' — A0 = divinité META-OS PASSIF. CC A2 = orchestrateur, NE fait JAMAIS le travail B3 technicien. A1 Beth/Morty + Rick Sobriété différé Q4 2026.",
  "MEMORY.md §'Skill Creator Reflex Phase 2' — Hermes-style self-improvement, agents créent skills end-of-session sans A0 GO (coût false-positive << coût escalation)",
  "ADR-META-001 D1-D8 — D1 Verify-Before-Assert · D2 Research-First · D3 Nuance · D4 No-Contradiction · D5 No-Self-Congratulation · D6 Root-Cause · D7 Cost-Of-Escalation · D8 Cross-Agent",
  "ADR-META-001 D7 cost-of-escalation — A0 escalation ~100× erreur originale. Default NO escalation mid-research.",
  "ADR-META-001 D6 root-cause — 'what's the actual blocker, not the symptom' (verbatim)",
  "ADR-SOBER-002 Anti-Paperclip — pas de promises 2027, pas de chiffres non sourcés, pas de features inventées",
  "PRD-NEXUS-EVOLUTION-IA-001 §6 Rails existants — wargames 05/06/07/08/09 + omk-nexus-landing-page.vercel.app (FR) + omk-nexus-landing-en.vercel.app (EN)",
  "MEMORY.md §'Nexus EN landing DEPLOYED 2026-06-29' — single-file index.html 628 KB · EN ratio 96.8% · dark theme #0A0E16 + #C8A8C8A55C",
  "ADR-NEXUS-LANDING-PERSONAS-001 DRAFT 2026-07-06 — 3 landings distinctes (Marcus / Harrison / David), sister immédiat de ce ADR",
  "ADR-L2-AAAS-001 RATIFIED 2026-06-21 — 3 Variants Solarpunk (Solaris 🎨 Visual · Nexus ⚖️ Data · Orbiter 🏗️ Mobile), 8 B2 × 53 B3 E-Myth matrix"
]
provenance: Née 2026-07-06 d'une directive A0 B1 E-Myth Gatekeeper ('Rédige l'ADR canonique du process multi-workflow × swarm-orchestrator pour création landing canon'). SKILL multi-workflow (canon sibling) lu en D1 — 6 phases. SKILL swarm-orchestrator lu en D1 — 3 patterns (Single-Task / Parallel / Chain) + Core Principle 'Delegate to Background, Never Execute Directly'. CLAUDE.md §'🕷️ Doctrine Swarm Orchestration' ancré. ADR-META-001 D1-D8 + D7 cost-of-escalation gravés. Sister canon ADR-NEXUS-LANDING-PERSONAS-001 (DRAFT même date) — ce workflow est le mode d'emploi opérationnel de la création des 3 landings. Statut DRAFT — ratification A0 attendue post-relecture canon.
---

# ADR-WORKFLOW-001 — Multi-Workflow × Swarm-Orchestrator, Process Canonique 6-Phases

## 1. Status

**DRAFT** — 2026-07-06. Produit par Claude Code B1 E-Myth Gatekeeper, sur directive A0 Amadeus. Sister canon de [`ADR-NEXUS-LANDING-PERSONAS-001`](./ADR-NEXUS-LANDING-PERSONAS-001_3-landings-distinctes-icp.md) (DRAFT 2026-07-06 — 3 landings distinctes par persona) et [`ADR-L2-AAAS-001`](./ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md) (RATIFIED 2026-06-21 — 3 Variants Solarpunk). Ancré sur SKILL canoniques `multi-workflow` (6 phases canoniques) et `swarm-orchestrator` (A2 E-Myth Strategic Orchestrator), [`CLAUDE.md`](../../CLAUDE.md) §'🕷️ Doctrine Swarm Orchestration', [`ADR-META-001`](../L0_Tech_OS/ADR-META-001_anti-paresse-verify-before-assert.md) D1-D8 + D7 cost-of-escalation, et [`MEMORY.md`](../../../00_Amadeus/30_MEMORY_CORE/LLM_Wiki/MEMORY.md) §'A0 Divinity Arsenal Doctrine 2026-06-20'.

## 2. Context

### 2.1. D6 racine — aucun process canon pour orchestrer création Landing

Avant ce ADR, **AUCUN process canon formalisé** pour orchestrer la création d'une Landing Page de grande valeur dans le canon A'Space. Le problème D6 vérifié :

| Source canon | Status pré-ADR |
|---|---|
| SKILL canoniques | `multi-workflow` (6 phases canoniques) et `swarm-orchestrator` (A2 patterns) existent comme skills siblings mais **PAS** reliés en process Landing canon |
| CLAUDE.md §'🕷️ Doctrine Swarm Orchestration' | Doctrine Main Agent = A2 orchestrateur, mais **PAS** de mode d'emploi landing spécifique |
| ADR canon | 0/0 ADR `ADR-WORKFLOW-*` dans `_SPECS/ADR/L2_Business_OS/` — gap vérifié par `ls` |
| Rails déployés | `omk-nexus-landing-page.vercel.app` (FR) + `omk-nexus-landing-en.vercel.app` (EN) — LIVE (canon MEMORY.md §'Nexus EN landing DEPLOYED 2026-06-29'), **mais** sans process reproductible |

### 2.2. Le risque D7 — coût d'escalation A0 si pas de process

ADR-META-001 D7 cost-of-escalation est gravé : **« A0 escalation is ~100× the original error »**. Sans process canon, A0 doit trancher à chaque demande Landing (« combien de phases ? », « quel score pour continuer ? », « quand déléguer vs exécuter ? »). **Conséquence D6** : drift procédural + escalation inutile A0. **Solution canon** : fixer le process en ADR, A0 n'a plus qu'à ratifier une seule fois.

### 2.3. La doctrine canonique à respecter (4 piliers)

L'ADR doit encoder **4 piliers** non-négociables du canon A'Space OS V2 :

| Pilier | Source canon | Conséquence workflow Landing |
|---|---|---|
| **A0 = divinité META-OS PASSIF** | MEMORY.md §'A0 Divinity Arsenal Doctrine 2026-06-20' | A0 ratifie milestones, ne touche jamais au B3 technicien |
| **A2 (Claude Code Main Agent) = Orchestrateur Stratégique** | CLAUDE.md §'Rôles' | A2 ne code JAMAIS en main agent, délègue TOUT aux A3 |
| **A3 = 35 sub-agents canon** | CLAUDE.md §'Mindsets — Discipline porting layer' | Dispatchers Beth/Morty, A3 twin runtime |
| **D7 cost-of-escalation** | ADR-META-001 | A0 escalation ~100× erreur, default NO escalation mid-research |

### 2.4. Sister-canon : SKILL multi-workflow × SKILL swarm-orchestrator

Les deux skills canon existent en parallèle (verbatim) :

- **`multi-workflow`** (sibling skill) : **6 phases canoniques** — Research → Ideation → Plan → Execute → Optimize → Review.
- **`swarm-orchestrator`** (sibling skill, `~/.claude/skills/swarm-orchestrator/SKILL.md`) : **A2 E-Myth Strategic Orchestrator** — Single-Task / Parallel / Chain delegation, Core Principle « **Delegate to Background, Never Execute Directly** ».

**D3 nuance critique** : `multi-workflow` ≠ `multi-backend`. `multi-backend` = choisir entre Codex / Hermes / Workflows backend (skill sibling distinct). `multi-workflow` = choisir entre **6 phases canoniques** d'un même livrable Landing. **Pas la même décision**.

## 3. Décision — Process Canonique 6-Phases avec Activation Gates

### 3.1. Périmètre — 6 phases sérialisées, score-gated, A2 orchestrateur

**Décision gravée** : la création d'une Landing Page de grande valeur suit **exactement 6 phases sérialisées**, chacune **gated par un score ≥7/10** sur 5 critères avant de passer à la suivante. **A2 (Main Agent = Claude Code) orchestre, A3 (sub-agents) exécutent en background**. A0 ratifie à 3 gates (Plan / Execute-finish / Review-finish).

```
A0 Intent → A2 Analyse → A2 Scope (AskUserQuestion)
  → Phase 1 Research (A2 + Codex/Gemini sub-agents)
  → Phase 2 Ideation (parallel Codex backend + Gemini frontend)
  → Phase 3 Plan (ADR sister canon rédigé) → ★ Gate A0 #1 ★
  → Phase 4 Execute (A3 sub-agents par Bounded Context, en background)
  → Phase 5 Optimize (parallel Codex + Gemini reviewers) → feedback loop
  → Phase 6 Review (checklist 5 critères + Playwright + D1 receipts) → ★ Gate A0 #2 ★
```

### 3.2. Activation gate — quand basculer en multi-workflow ?

**Décision** : on déclenche `multi-workflow` (vs rester en single-back-and-forth) si et seulement si **au moins 1 de 2 conditions** est vraie :

| # | Condition d'activation | Source |
|---|---|---|
| C1 | ≥ 2 PRD distincts à intégrer dans le livrable Landing | D6 root-cause : multi-PRD = besoin de phases, pas de single-shot |
| C2 | ≥ 3 ADR à créer en sister-canon pour supporter le livrable | D4 no-contradiction : sans ADR sister, dérive de scope |

**Sinon** (single PRD, ≤2 ADR) : rester en single-back-and-forth, pas de multi-workflow. **D3 nuance** : ne JAMAIS sur-orchestrer un livrable simple — YAGNI canon.

### 3.3. Communication pattern — `[Mode: X]` label + score check

**Décision** : à chaque transition de phase, A2 émet un message avec `[Mode: X]` label où X = numéro phase + score sur 5 critères. **Format canon** :

```
[Mode: Phase X — <name>]
Score: <0-10>/10
Critères: goal=<X>/10 · expect=<X>/10 · scope=<X>/10 · constraint=<X>/10 · leverage=<X>/10
Verdict: <CONTINUE | FORCE-STOP>
Si CONTINUE → Phase X+1
Si FORCE-STOP (score <7) → diagnostic D6 root-cause, retour Phase X ou escalation A0
```

**D7 cost-of-escalation appliqué** : si FORCE-STOP, A2 NE escalade PAS immédiatement A0. Il diagnostique D6 root-cause (verbatim ADR-META-001 D6 : « what's the actual blocker, not the symptom »), tente 1 retry, puis seulement si 2e FORCE-STOP consécutif → escalation A0.

### 3.4. Sister-canon par phase — outils réels qui implémentent

| Phase | Skill canon sister | Output canon |
|---|---|---|
| 1 Research | `context7-mcp` + `multi-routines-12wy` + lecture canon (`MEMORY.md`, `wiki/index.md`) | Score ≥7/10 sur 5 critères |
| 2 Ideation | `multi-backend` (Codex + Gemini parallèles) + `wargame` skill | Vision DDD (3-5 Bounded Contexts) |
| 3 Plan | `openspec-propose` + `ratify-adr` | ADR sister canon (DRAFT → Gate A0 #1) |
| 4 Execute | `swarm-orchestrator` (run_in_background: true) + `canon-batch-spawn` | Code/deploy per Bounded Context |
| 5 Optimize | `code-reviewer` + `security-reviewer` + `a11y-architect` + `performance-optimizer` | Feedback loops, ≤3 itérations |
| 6 Review | `e2e-runner` + `playwright` + checklist `ADR-LANDING-QA-001` | Screenshots + D1 receipts final → Gate A0 #2 |

## 4. Doctrine — Anti-Patterns Interdits + Score Gate

### 4.1. Anti-patterns interdits (D6 root-cause)

| # | Anti-pattern | Conséquence | Source canon |
|---|---|---|---|
| A1 | A2 (Main Agent) code directement | Viole CLAUDE.md §'🕷️ Doctrine Swarm Orchestration' | SKILL `swarm-orchestrator` Core Principle verbatim |
| A2 | Sauter une phase (ex. passer Ideation → Execute) | Perte canon, drift D4 no-contradiction | SKILL `multi-workflow` 6 phases sérialisées |
| A3 | Continuer quand score <7 | Viole Phase 1 Research gate | SKILL `multi-workflow` Phase 1 |
| A4 | A3 sub-agent bloque A2 synchrone | Viole SKILL `swarm-orchestrator` « Never Execute Directly » | SKILL `swarm-orchestrator` When NOT to Delegate |
| A5 | Confondre `multi-backend` (choisir LLM backend) et `multi-workflow` (6 phases) | D3 nuance violation | D3 nuance §2.4 |
| A6 | Auto-scope sans AskUserQuestion | Viole D8 cross-agent (A0 doit valider scope) | SKILL `swarm-orchestrator` When to Delegate |
| A7 | Escalation A0 mid-research sans 2 FORCE-STOP consécutifs | Viole D7 cost-of-escalation | ADR-META-001 D7 |
| A8 | Multi-workflow pour single PRD simple | YAGNI violation, sur-orchestration | D3 nuance §3.2 |

### 4.2. Score gate — 5 critères canon (≥7/10 pour continuer)

| Critère | Description | Source |
|---|---|---|
| **goal** | L'objectif Landing est-il aligné Ikigai A0 (sister canon `ADR-ICP-NEXUS-001` ou équivalent) ? | SKILL `multi-workflow` Phase 1 + A1 Beth ALIGN gate |
| **expect** | Le résultat attendu est-il mesurable et vérifiable (D1 receipts possibles) ? | SKILL `multi-workflow` Phase 1 + D1 Verify-Before-Assert |
| **scope** | Le scope est-il borné par A0 (AskUserQuestion) ou dérive-t-il ? | SKILL `multi-workflow` Phase 1 + D8 Cross-Agent |
| **constraint** | Les contraintes (budget tokens, time-to-ship, stack) sont-elles canon et respectées ? | SKILL `multi-workflow` Phase 1 + ADR-SOBER-002 Anti-Paperclip |
| **leverage** | Le livrable a-t-il un leverage H1/H3/H10/H30/H90 mesurable ? | SKILL `multi-workflow` Phase 1 + A1 Orville Ikigai horizons |

**Score < 7/10** sur l'un des 5 critères = **FORCE-STOP**. Score global = moyenne des 5. Si moyenne < 7 → diagnostic D6 root-cause + retry ou escalation A0.

### 4.3. Activation gates A0 — exactement 3, à moments fixes

| Gate # | Moment | Livrable attendu | Décision A0 |
|---|---|---|---|
| **Gate A0 #1** | Fin Phase 3 Plan | ADR sister canon DRAFT | GO/NO-GO/HOLD |
| **Gate A0 #2** | Fin Phase 4 Execute | Code deploy staging + screenshots | GO/NO-GO/HOLD |
| **Gate A0 #3** | Fin Phase 6 Review | Checklist QA + D1 receipts + rapport final | RATIFY/REJECT/REVISE |

**D7 cost-of-escalation appliqué** : A2 ne demande PAS confirmation A0 entre Gate #1 et Gate #2. Phases 4-5 = autonomie A2/A3 sub-agents.

## 5. Architecture — Les 6 Phases en Détail

### 5.1. Phase 1 — Research (A2 + Codex/Gemini sub-agents)

**Goal canon** : extraire le canon depuis PRD source + sœur ADRs + wiki canon, scorer ≥7/10 sur 5 critères.

**Pattern SKILL multi-workflow (verbatim)** : « **Phase 1 Research — prompt enhancement + score ≥7 sur 5 critères (goal / expect / scope / constraint) avant de continuer** ».

**Outils réels** :
1. A2 lit PRD source (ex. `PRD-NEXUS-EVOLUTION-IA-001`)
2. A2 spawn Codex sub-agent pour extraire canon data (pricing canon, modules, ICP) — `swarm-orchestrator` Pattern « Single-Task Delegation »
3. A2 spawn Gemini sub-agent pour extraire canon UI/aesthetic (références visuelles, anti-template policy) — `swarm-orchestrator` Pattern « Parallel Delegation »
4. A2 synthétise en **Brief Canon** (max 2 pages)
5. A2 score sur 5 critères (§4.2) — si ≥7/10 → Phase 2

**Anti-pattern A4 interdit** : A2 ne lit JAMAIS synchrone en attendant Codex/Gemini. `run_in_background: true` mandatory.

### 5.2. Phase 2 — Ideation (Codex backend // Gemini frontend)

**Goal canon** : générer une **Vision DDD** (Domain-Driven Design) avec 3-5 Bounded Contexts, synthèse backend (Codex) + frontend (Gemini).

**Pattern SKILL multi-workflow (verbatim)** : « **Phase 2 Ideation — parallèle multi-modèle (Codex backend + Gemini frontend) → synthèse Vision DDD** ».

**Outils réels** :
1. A2 dispatch Codex sub-agent pour **architecture backend** (data structures, API surface, deployment topology) — `swarm-orchestrator` Pattern « Parallel Delegation »
2. A2 dispatch Gemini sub-agent pour **UI/UX aesthetic direction** (style intent, palette, typography, motion) — parallèlement
3. A2 synthétise en **Vision DDD** (1 page) : nom landing + 3-5 BC + aesthetic direction +1 phrase
4. Score check rapide (≥6/10 sur goal/leverage) → Phase 3

**D3 nuance** : pas de score strict Phase 2 (c'est de la divergence créative, pas une gate canon). Mais si goal/leverage <6 → diagnostic D6 root-cause.

### 5.3. Phase 3 — Plan (ADR sister canon rédigé) → Gate A0 #1

**Goal canon** : rédiger **l'ADR sister canon** (DRAFT) qui fige la décision Landing. Sister canon de `ADR-NEXUS-LANDING-PERSONAS-001` (DRAFT 2026-07-06) pour le cas OMK Nexus.

**Pattern SKILL multi-workflow (verbatim)** : « **Phase 3 Plan — collaborative, ADR sister canon rédigé avant toute exécution** ».

**Outils réels** :
1. A2 rédige ADR sister canon DRAFT en suivant frontmatter canon (voir template §7.1)
2. A2 spawn `code-reviewer` sub-agent pour review cohérence D4 no-contradiction
3. A2 présente **ADR DRAFT + Vision DDD** à A0 → **Gate A0 #1** (GO/NO-GO/HOLD)
4. Si GO → Phase 4. Si NO-GO → diagnostic, retry Phase 1-3 ou abandon canon.

**Template prompt A2 → A0 (verbatim, à utiliser)** :

```markdown
[Mode: Phase 3 — Plan → Gate A0 #1]
ADR sister canon rédigé : [path-to-adr-sister-draft.md]
Vision DDD : [3-5 BC + aesthetic direction +1 phrase]
Score Phase 1-3 cumulés : goal=<X>/10 · expect=<X>/10 · scope=<X>/10 · constraint=<X>/10 · leverage=<X>/10
Verdict score : <PASS ≥7/10 | FORCE-STOP <7/10>

★ GATE A0 #1 ★
Décision attendue : GO (Phase 4) · NO-GO (retry) · HOLD (pause canon)
Si GO, livraison attendue : code deploy staging + screenshots live avant Gate A0 #2.
```

### 5.4. Phase 4 — Execute (A3 sub-agents en background, par Bounded Context)

**Goal canon** : implémenter la Landing, **un A3 sub-agent par Bounded Context du DDD**, en parallèle background.

**Pattern SKILL multi-workflow (verbatim)** : « **Phase 4 Execute — Claude avec feedback milestones, sub-agents en background** ». **Pattern SKILL swarm-orchestrator** : « **Parallel Delegation — User Intent → Main Agent analyzes → Spawn N sub-agents in parallel → Wait + Monitor → Coordinate → Report** » (verbatim).

**Outils réels** :
1. A2 dispatch **N sub-agents A3** (1 par BC) via `swarm-orchestrator` avec `run_in_background: true`
2. A2 dispatch sub-agent DevOps pour setup Vercel project (canon `vercel-deploy-from-github`)
3. A2 monitor sans bloquer (lit `list_pages` MCP Vercel)
4. Chaque A3 sub-agent rapporte à A2 (commits, screenshots staging)
5. Quand tous BC terminés → A2 dispatch `e2e-runner` pour test staging

**D4 no-contradiction** : aucun A3 ne touche au canon (CLAUDE.md, MEMORY.md, wiki/) sans gate A0 explicite. **D6 root-cause** : si un BC échoue, A2 isole le BC fautif, ne rollback pas les autres.

### 5.5. Phase 5 — Optimize (multi-model reviewers, feedback loops)

**Goal canon** : reviewers multi-modèle parallèles (Codex security/perf + Gemini a11y/UX) avec feedback loops max 3 itérations.

**Pattern SKILL multi-workflow (verbatim)** : « **Phase 5 Optimize — multi-model parallel review (Codex security/perf + Gemini a11y/UX) → feedback loops** ».

**Outils réels** :
1. A2 dispatch Codex sub-agent pour **security review + perf audit** (Playwright Lighthouse + `lighthouse_audit`)
2. A2 dispatch Gemini sub-agent pour **a11y review + UX critique** (`a11y-architect` + UX pattern check)
3. A2 collecte feedback → génère **Patch List** (≤10 items prioritaires)
4. A2 dispatch `code-reviewer` sub-agent pour appliquer Patch List sur la landing
5. Si score Optimize <7/10 → retry (max 3 itérations) avant Phase 6

**D7 cost-of-escalation** : si 3 itérations Phase 5 sans score ≥7 → diagnostic D6 root-cause + escalate A0 (autorisé ici, D7 = NO escalation mid-research, Phase 5 = fin recherche).

### 5.6. Phase 6 — Review (checklist 5 critères + Playwright + D1 receipts) → Gate A0 #2

**Goal canon** : validation finale A0 via checklist 5 critères (déjà `ADR-LANDING-QA-001` sister) + screenshots Playwright live + D1 receipts.

**Pattern SKILL multi-workflow (verbatim)** : « **Phase 6 Review — final eval A0 + checklist self-critique 5 critères** ».

**Outils réels** :
1. A2 dispatch `playwright` sub-agent pour screenshots 4 breakpoints (320, 768, 1024, 1440) — canon `ecc/web/testing.md`
2. A2 dispatch `lighthouse_audit` pour score Performance/A11y/Best Practices/SEO — canon `ecc/web/performance.md` targets (LCP <2.5s, INP <200ms, CLS <0.1)
3. A2 génère **Rapport Final** : checklist 5 critères + screenshots + D1 receipts (URLs live, hash commits, scores Lighthouse)
4. A2 présente à A0 → **Gate A0 #2** (RATIFY/REJECT/REVISE)
5. Si RATIFY → handoff canon (wiki/hand_offs/) + MEMORY.md update (D4 append-only)
6. Si REJECT → retour Phase 1 ou Phase 4 selon feedback
7. Si REVISE → A0 indique patch ciblé, A2 patch + re-Phase 6

## 6. Verification — D1 Receipts Mandatory

### 6.1. D1 receipts obligatoires à chaque Gate A0

| Gate | D1 receipts à fournir |
|---|---|
| Gate A0 #1 (Phase 3) | (1) ADR sister canon DRAFT path + SHA · (2) Vision DDD 1-page · (3) Score 5 critères |
| Gate A0 #2 (Phase 6) | (1) URL landing live · (2) Screenshot 4 breakpoints (Playwright) · (3) Score Lighthouse (Perf/A11y/BP/SEO) · (4) Hash commits GitHub · (5) Wiki handoff path + SHA · (6) MEMORY.md update path |

### 6.2. D2 Research-First gates

**Avant chaque phase**, A2 vérifie :
- Phase 1 : PRD source existe + sister ADRs citées (canon wiki/index.md)
- Phase 2 : aesthetic direction référencée (canon `ecc/web/design-quality.md` Anti-Template Policy)
- Phase 3 : ADR format canonique (frontmatter YAML complet, 9 sections numérotées)
- Phase 4 : sub-agents A3 canon existent dans le roster (`~/.claude/agents/`)
- Phase 5 : reviewers canon disponibles (`code-reviewer`, `security-reviewer`, `a11y-architect`)
- Phase 6 : checklist `ADR-LANDING-QA-001` existe ou est rédigée en sister canon

### 6.3. D8 Cross-Agent — sister-canon linkage obligatoire

Ce ADR doit citer verbatim :
- SKILL `multi-workflow` 6 phases
- SKILL `swarm-orchestrator` Core Principle + 3 patterns
- CLAUDE.md §'🕷️ Doctrine Swarm Orchestration' + §'Rôles'
- ADR-META-001 D1-D8 (particulièrement D7 cost-of-escalation)
- ADR-NEXUS-LANDING-PERSONAS-001 (sister immédiat) si scope = OMK Nexus
- ADR-ICP-NEXUS-001 + ADR-AAAS-PRICING-001 (canon pricing/ICP)

## 7. Risks + Rollback

### 7.1. Risques identifiés (D6 root-cause)

| # | Risque | Probabilité | Mitigation canon |
|---|---|---|---|
| R1 | A0 escalation inutile mid-research | Haute sans ADR | D7 cost-of-escalation + 3 gates fixes |
| R2 | Drift procédural (passer des phases) | Moyenne | Score gate ≥7 obligatoire + `[Mode: X]` label |
| R3 | Sur-orchestration (multi-workflow pour single PRD) | Moyenne | YAGNI gate (§3.2 conditions C1/C2) |
| R4 | A3 sub-agent bloque A2 synchrone | Moyenne | `run_in_background: true` mandatory + monitor async |
| R5 | Landing livrée mais ICP mal ciblé (anti-paperclip) | Faible avec ADR sister | `ADR-NEXUS-LANDING-PERSONAS-001` sister gate A0 #1 |
| R6 | Code BC incohérent entre A3 sub-agents | Moyenne | Sister ADR fige Vision DDD en Phase 3 |

### 7.2. Rollback strategy

| Situation | Action rollback | Source canon |
|---|---|---|
| Score <7 sur 2 phases consécutives | Retour Phase 1 + diagnostic D6 root-cause | ADR-META-001 D6 |
| Gate A0 #1 = NO-GO | ADR sister archivé `_TRASH_<date>/`, retour Phase 1 ou abandon | D4 no-contradiction append-only |
| Gate A0 #2 = REJECT | Code BC rollbacké Git (commit revert), retour Phase 4 ou Phase 1 selon feedback | D4 no-hard-delete (`_TRASH_<date>/`) |
| Phase 5 = 3 itérations sans score ≥7 | Escalation A0 (autorisé Phase 5, fin recherche) | ADR-META-001 D7 |
| Landing live mais post-launch drift détecté | Nouvelle ADR sister `ADR-WORKFLOW-002_*` postmortem + Phase 1 nouvelle | D4 append-only |

### 7.3. Migration strategy — passer d'un single-shot landing à ce process

Si une Landing est en cours de création hors ce process :
1. **Pause** création actuelle
2. **Audit D6** : la livraison actuelle respecte-t-elle Phase 3 Plan (ADR sister) + Phase 6 Review (checklist QA) ?
3. **Si non** : rédiger ADR sister canon DRAFT rétroactivement (Phase 3 rattrapage) → Gate A0 #1 retroactif
4. **Si oui** : continuer Phase 4-5-6 sur le process canon
5. **Wiki log** : noter la migration dans `wiki/log.md` (D4 append-only)

## 8. Statut C — Démonstration sur le Cas Pilote OMK Nexus (3 Landings)

### 8.1. Application immédiate — 3 Landings OMK Nexus

**Cas pilote** : `ADR-NEXUS-LANDING-PERSONAS-001` (DRAFT 2026-07-06) demande 3 landings distinctes (Marcus / Harrison / David). Application de ce workflow :

| Landing | Statut workflow 6-phases | Prochaine action |
|---|---|---|
| **L1 Marcus Vance** | Phase 1-2 DONE (PRD lu + Vision DDD), Phase 3 Plan = ce ADR + ADR Personas DRAFT | Gate A0 #1 sur ADR Personas + Plan L1 |
| **L2 Harrison Vance / Clara Sterling** | Phase 1-2 DONE, Phase 3 Plan = ce ADR + ADR Personas DRAFT | Gate A0 #1 sur ADR Personas + Plan L2 (focus prioritaire A+) |
| **L3 David Kross** | Phase 1-2 DONE, Phase 3 Plan = ce ADR + ADR Personas DRAFT | Gate A0 #1 sur ADR Personas + Plan L3 |

### 8.2. Sister-canon linké

| Canon | Path | Status |
|---|---|---|
| ADR-NEXUS-LANDING-PERSONAS-001 (sister immédiat, 3 landings distinctes) | `_SPECS/ADR/L2_Business_OS/ADR-NEXUS-LANDING-PERSONAS-001_3-landings-distinctes-icp.md` | DRAFT 2026-07-06 |
| ADR-ICP-NEXUS-001 (5 piliers ICP canon) | `_SPECS/ADR/L2_Business_OS/ADR-ICP-NEXUS-001_icp-nexus-structuration.md` | RATIFIED 2026-06-24 |
| ADR-AAAS-PRICING-001 (5 tiers USD post-accuponcture) | `_SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-001_aaas-pricing-canon.md` | RATIFIED+AMENDED 2026-06-24 |
| ADR-L2-AAAS-001 (3 Variants Solarpunk) | `_SPECS/ADR/L2_Business_OS/ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md` | RATIFIED 2026-06-21 |
| ADR-META-001 (D1-D8) | `_SPECS/ADR/L0_Tech_OS/ADR-META-001_anti-paresse-verify-before-assert.md` | RATIFIED |
| ADR-META-005 (Hooks automation) | `_SPECS/ADR/L1_Life_OS/ADR-META-005_hooks-automation.md` | RATIFIED 2026-06-21 |
| ADR-SOBER-002 (Anti-Paperclip) | `_SPECS/ADR/L1_Life_OS/ADR-SOBER-002_anti-paperclip.md` | RATIFIED |

## 9. Decision Summary

**Décision gravée** : la création d'une Landing Page de grande valeur dans le canon A'Space OS V2 suit **exactement 6 phases sérialisées** (`multi-workflow` canon) orchestrées par A2 (Main Agent = Claude Code) avec sub-agents A3 en background (`swarm-orchestrator` canon).

**Conditions d'activation** : ≥2 PRD distincts OU ≥3 ADR sister à créer. Sinon single-back-and-forth (YAGNI).

**3 gates A0 fixes** : Plan (Phase 3) / Execute-finish (Phase 4) / Review-finish (Phase 6). Entre gates : autonomie A2/A3.

**Score gate ≥7/10** sur 5 critères (goal/expect/scope/constraint/leverage) à chaque transition de phase. FORCE-STOP si <7 → diagnostic D6 root-cause + retry ou escalation A0 (D7).

**D7 cost-of-escalation appliqué** : pas d'escalation A0 mid-research. Escalation seulement après 2 FORCE-STOP consécutifs OU en fin Phase 5 (3 itérations sans score).

**Sister-canon linké** : SKILL `multi-workflow` + SKILL `swarm-orchestrator` + CLAUDE.md §'🕷️ Doctrine Swarm Orchestration' + ADR-META-001 D1-D8 + ADR-NEXUS-LANDING-PERSONAS-001 (sister immédiat).

**Cas pilote** : 3 landings OMK Nexus (Marcus / Harrison / David) doivent suivre ce workflow après ratification Gate A0 #1 sur ce ADR + ADR Personas.

**Anti-patterns interdits** (8 listés §4.1) : A2 code directement / saute phase / score <7 continue / A3 synchrone / confus multi-backend vs multi-workflow / auto-scope / escalation mid-research / sur-orchestration single PRD.

**Aucune invention procédurale** : tous les patterns viennent verbatim de SKILL canoniques ou CLAUDE.md. **Rollback** : `_TRASH_<date>/` append-only (D4 no-hard-delete).

**Statut** : **DRAFT** — ratification A0 attendue post-relecture canon (Gate A0 #1 sur ce ADR + sister ADR Personas).

---

> **Annexe — Rappel canonique SKILL swarm-orchestrator (verbatim, source sibling skill)**
>
> - **Identity** : « **swarm-orchestrator** — Strategic Orchestration Manager (E-Myth A2) »
> - **Core Principle** : « **Delegate to Background, Never Execute Directly.** »
> - **Swarm Patterns** : Single-Task Delegation / Parallel Delegation / Chain Delegation
> - **When to Delegate** : « Code writing, editing, refactoring · File operations · Search operations · Configuration changes · Build/compilation tasks · Documentation generation · Multi-step workflows with dependencies »
> - **When NOT to Delegate** : « Pure questions (no technical execution required) · Read-only file inspection for context · Summary/reporting of existing information · When user explicitly asks Main Agent to do the work directly »

> **Annexe — Rappel canonique SKILL multi-workflow (verbatim, source sibling skill)**
>
> - **6 phases canoniques** : Research → Ideation → Plan → Execute → Optimize → Review
> - **Phase 1 Research** : « prompt enhancement + score ≥7 sur 5 critères (goal / expect / scope / constraint) avant de continuer »
> - **Phase 2 Ideation** : « parallèle multi-modèle (Codex backend + Gemini frontend) → synthèse Vision DDD »
> - **Phase 3 Plan** : « collaborative, ADR sister canon rédigé avant toute exécution »
> - **Phase 4 Execute** : « Claude avec feedback milestones, sub-agents en background »
> - **Phase 5 Optimize** : « multi-model parallel review (Codex security/perf + Gemini a11y/UX) → feedback loops »
> - **Phase 6 Review** : « final eval A0 + checklist self-critique 5 critères »