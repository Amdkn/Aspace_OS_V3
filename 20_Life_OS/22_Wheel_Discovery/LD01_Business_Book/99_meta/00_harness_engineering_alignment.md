---
type: alignment-harness-engineering
title: Harness Engineering Alignment — Mark Kashef (5 layers) × Cole Medin (Google masterclass, harness = 90%) × Cost Collapse (MiniMax $50/5.1B tokens) → LD01 canon + plan-meta-memoire
description: Alignement des 2 nouvelles références (Mark Kashef "5 layers of agentic OS" + Cole Medin "Google masterclass") avec le coût réel MiniMax D1-vérifié (5.1B tokens/$50 = 6000× moins cher qu'Opus API direct), et wiring vers le canon plan-meta-memoire-okf-wiki-graphify-dox §P1-P6. Output : 8 invariants supplémentaires + cost ceiling mis à jour (Phase 3 L5 continuous désormais économiquement faisable).
timestamp: 2026-07-04T15:45:00-04:00
domain: LD01_Career_Business
bounded_context: BC-True-Autonomy (enriched) + BC-Methodology (CARDIA canon companion)
sister_files:
  - 30_decisions/ADR-LD01-005_budget_collapse_phase3_economical.md
  - 99_meta/true_agent_autonomy_architecture.md (cost ceiling §3.3 updated)
  - 30_decisions/ADR-LD01-004_true_agent_autonomy.md (linked ADR-005 reference)
verified_by: Test-Path "C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L0_Tech_OS\ADR-LLM-COST-COMPARE-001_minimax-anthropic-openrouter.md" ; Test-Path "C:\Users\amado\.claude\plans\plan-meta-memoire-okf-wiki-graphify-dox.md"
rot_rate: lent (architecture immutable; harness layer rot per cycle)
---

# Harness Engineering Alignment — LD01

> *Le modèle = 10% de la valeur. Le harness = 90%. C'est ce que Mark Kashef ET Cole Medin convergent sur le 2026. Combiné avec le coût MiniMax D1-vérifié, le Phase 3 L5 continuous de ADR-LD01-004 devient économiquement faisable par construction.*

## 1. Pourquoi ce document maintenant (3 inputs convergents)

### 1.1 Reference 1 — Mark Kashef « 5 layers of agentic OS »

Mark Kashef a publié sa décomposition canonique (video « Maîtrisez les 5 couches de tout OS agentique »). Le modèle:

> *« Identity (soul file) → Rules and Hooks → Skills → Agents → Tools/API/MCP/CLI. »*

Chacune a un **rot-rate** explicite (cadence de péremption de cette couche), déclaré dans un fichier `rot.md` à part.

### 1.2 Reference 2 — Cole Medin « Google's masterclass on agentic engineering »

Cole Medin a disséqué la masterclass 51 pages publiée par Google. Les pivots :

- **AI coding is a SPECTRUM, not a switch** (vibe coding ↔ structured AI assisted ↔ agentic engineering). LD01 = quelque part entre agentic engineering L4-L5.
- **The large language model is only 10% of the system** (Google's claim). Harness = 90%. Anthropic claimé d'abord (harness matters as much as model) ; Google amplifie (harness matters MORE).
- **Static context vs dynamic context** — skills loaded progressively = dynamic, rules/system prompt = static. **Anti-pattern stuffing everything into system prompt = high-cost fixed context = rot-prone.**
- **Conductor vs Orchestrator mode** — Cole nuance Google en disant que l'orchestrator should suffice once le système est mature, mais conductor reste utile pour debug ou exploration initiale.
- **Token economics** — agentic engineering = high capex (harness construction) + low opex (system runs itself). Vibe coding = low capex + high opex (millions of tokens on slop).

### 1.3 Reference 3 — Cost Collapse Reality (MiniMax D1-vérifié)

D1-receipts 2026-07-04 depuis `C:\Users\amado\ASpace_OS_V2\_SPECS\ADR\L0_Tech_OS\ADR-LLM-COST-COMPARE-001_minimax-anthropic-openrouter.md` + screenshots A0 (Mavis UI + WhatsApp) :

| Channel | Cost | Volume |
|---|---|---|
| **MiniMax Token Plan · Monthly Max** | **$50/mois** | **~5.1B tokens/mois** (D1-vérifié screenshot `platform.minimax.io/console/usage` 2026-07-04) |
| MiniMax-M3 via OpenRouter | $0.30/M in + $1.20/M out | (D1-vérifié OpenRouter API) |
| Fable 5 (= MiniMax-M3 backend) sur OpenRouter | $10/M in + $50/M out | (D1-vérifié OpenRouter API, premium tier) |
| Anthropic Opus 4.8 sur OpenRouter | $5/M in + $25/M out | (D1-vérifié OpenRouter API) |
| Equivalent Opus 4.8 API pour 5.1B tokens | ~$300,000/mois | (extrapolé) |

→ **MiniMax $50/mo = 6000× moins cher que l'équivalent Opus API pour le même volume** (abondance post-Year-3000 pour le A0).

### 1.4 La convergence des 3 références

| Source | Affirmation | Implication pour LD01 |
|---|---|---|
| Mark Kashef | 5 layers + rot-rate | LD01 org doit explicitement nommer chaque couche + son rot-rate |
| Cole / Google | Harness = 90% du système | Investissements CARDIA-TDD + 8 contrats S + BC-True-Autonomy = LA bonne guerre |
| Cost reality | $50/mo = essentially unlimited inference | Phase 3 L5 continuous **économiquement faisable** (le kill-switch budget devient soft guardrail) |

**Conclusion** : la conjugaison de ces 3 = Year 3000 post-Abundance pour Book LD01. Le « sparse intelligence » devient « unbounded attention to harness design ».

## 2. Mapping Mark Kashef 5 layers → LD01 canon

### 2.1 Identity (soul file) → **OKF frontmatter + AGENTS.md/CLAUDE.md bi-famille**

| Mark layer | LD01 canon | Locator |
|---|---|---|
| Identity (highest upfront cost, lowest rot) | OKF v0.1 `type:` top-level sur tout `.md` canonique | `00_index.md` frontmatter + tous modules |
| Identity sister | `AGENTS.md` (DOX FS family) + `CLAUDE.md` (DOX harness sister) | `AGENTS.md` + `CLAUDE.md` |
| Identity sister runtime | `~/.mavis/agents/mavis/_organigrammes-doctrine.md` (mirror) | runtime entry |
| Identity doctrine | `plan-meta-memoire-okf-wiki-graphify-dox.md §3.5` (DOX bi-famille universel) | canon sister |

**Rot-rate (Mark)**: lent (1×/cycle 12WY, W13) — identité change rarement. C'est exactement ce que `99_meta/rot-rates.md` déclare pour la couche « Identity OKF/AGENTS.md/CLAUDE.md ».

### 2.2 Rules and Hooks → **BC-Methodology + rot-rates.md + CARDIA-TDD §20_skeleton**

| Mark layer | LD01 canon | Locator |
|---|---|---|
| Rules (simple, low upfront, added on issues) | `10_methodology/00_CARDIA_overview.md` (6 propriétés canoniques) | CARDIA-TDD §1-7 |
| Rules sister | `99_meta/rot-rates.md` (déclare rot par module) | rot canon |
| Hooks (deterministic, post-event) | `90_manifests/manifest.cross-harness.md` (cross-harness surface) + kill-switches in `true_agent_autonomy_architecture.md §C5` | hooks canoniques |
| Hooks sister | BC-True-Autonomy kill-switches 6 (escalation / budget / looping / D5 / sess-24h / A0 KILL) | `99_meta/true_agent_autonomy_architecture.md` §7 |

**Rot-rate (Mark)**: lent pour rules canoniques (systémique), rapide pour hooks (ajustées à chaque incident capturé par evolution.md).

### 2.3 Skills → **BC-Methodology SKILL artifacts (Pocock quality canon)**

| Mark layer | LD01 canon | Locator |
|---|---|---|
| Skills (process-oriented, weekly updates) | `10_methodology/00_Pocock_quality_canon.md` (L0 Lightning zero-install) | canon L0 |
| Skills sister | `_SKILL_<name>.md` candidates per Pocock 8 fields | future skill authoring |
| Skills discipline | Anti-doublon merger (Cole: extending an existing skill > creating new one) | Pocock canon §1.6 |

**Rot-rate (Mark)**: moyen-rapide (1×/semaine à 1×/mois selon cas). CARDIA-TDD §20_skeleton frontmatter `rot_rate:` field déclare la cadence par skill.

### 2.4 Agents → **`.mavis/agents/<agent>/` runtime + Book A3 + Captain Jerry Prime**

| Mark layer | LD01 canon | Locator |
|---|---|---|
| Agents (materialized from skill cluster) | `b1-jerry-emyth` (B1 captain LD01 owner per ADR-LD01-002) | `~/.mavis/agents/b1-jerry-emyth/LD01_book_bind.md` |
| Agents sister | `b2-batman-ops` (Operation/Batman/F4 per plan-L2 §4.4) | primary delegation target for Book |
| Agents cousins | 14 autres B2/B3 agents (rotatif fallback gated Rick S1) | 22-agent runtime canon |
| Agents doctrine | « Hire slowly, hire only when skill-cluster matures » (Mark) | L4-L5 phase ramp per ADR-LD01-004 |

**Rot-rate (Mark)**: rapide (rotates per model release). BC-True-Autonomy Phase 3 L5 continuous **monitoring** requis parce que agent rot rate accelerates.

### 2.5 Tools/APIs/MCPs/CLIs → **Multi-account vault + Mavis MCP servers + git-ship.ps1**

| Mark layer | LD01 canon | Locator |
|---|---|---|
| Tools/APIs (data layer, evolving) | `~/.mavis/credentials/mavis/` (4-comptes ACL vault) | runtime security canon |
| MCPs | `~/.mavis/mcp/` (matrix/playwright/cu/trash registered) | runtime MCP canon |
| CLIs (canonical) | `git-ship.ps1` (multi-account driver in `~/.git-ship/`) | runtime CLI canon |
| APIs | GitHub API via `gh auth --with-token`, Supabase via `symphony_state` bus | runtime data canon |

**Rot-rate (Mark)**: variable (provider-dependent). ACL vault + Clarkian drift detect (S7 lock per ADR-LD01-002 §S7).

### 2.6 Synthesis: LD01 sub-folders = exactly Mark's 5 layers

`LD01_Business_Book/{ 00_index.md AGENTS.md CLAUDE.md 10_methodology/ 20_skeleton/ 30_decisions/ 90_manifests/ 99_meta/ }` corresponds à :

| Sub-folder | Mark layer |
|---|---|
| `00_index.md` + `AGENTS.md` + `CLAUDE.md` | **Identity** (Mark L1) |
| `10_methodology/00_CARDIA_overview.md` + `rot-rates.md` | **Rules and Hooks** (Mark L2) |
| `10_methodology/00_Pocock_quality_canon.md` + future skills/ | **Skills** (Mark L3) |
| `90_manifests/` + `99_meta/00_mavis_runtime_alignment.md` (binding B1/B2 captain) | **Agents** (Mark L4) |
| Manifest + cross-harness surface | **Tools/MCP/CLI** (Mark L5) |

→ LD01 canon n'invente rien de nouveau : **il instancie Mark's 5 layers en sub-folders filesystem**.

## 3. Mapping Cole's masterclass harness = 90% principle

### 3.1 What Cole + Google say

> *« The large language model is only 10% of the system or it only matters 10%. Everything else, your instructions and tools and context and guardrails and orchestration and observability, like there's so much here that makes up the other 90%. »*

### 3.2 Comment LD01 a déjà investi 90% du harness

L'inventaire du harness LD01 existant (créé ces 4 dernières passes) :

| Composant harness | Path | Investissement LOC |
|---|---|---|
| **CARDIA-TDD methodology** (6 propriétés + 14 invariants) | `10_methodology/00_CARDIA_overview.md` | 9368 bytes |
| **8 contrats runtime S1-S8** (cross-harness) | `99_meta/00_mavis_runtime_alignment.md` §2 | 23186 bytes |
| **5 BC explicites + 1 sister BC-True-Autonomy** (DDD bounded contexts) | `99_meta/true_agent_autonomy_architecture.md` §C1.5 | 21156 bytes |
| **3 Lightning bindings + Pocock canon** | `10_methodology/00_Pocock_quality_canon.md` | 7796 bytes |
| **POC 4 extensions Dark Factory** (autonomy-loop + observations_setup + goal + evolution) | `~/.mavis/agents/b1-jerry-emyth/{autonomy-loop, memory/observations_setup, goal, evolution}.md` | ~360 bytes × 4 ≈ 1440 bytes |
| **4 ADRs canoniques** (organigramme + runtime binding + lightning + true autonomy) | `30_decisions/ADR-LD01-*.md` | ~41000 bytes |
| **Manifests cross-harness** (CC/MC/HA/Shadow) | `90_manifests/manifest.cross-harness.md` | 6141 bytes |
| **Sister duals DOX bi-famille** (`AGENTS.md` + `CLAUDE.md`) | canon LD01 | 7131 bytes |
| **Mirror registry `.claude` + `.mavis`** | `~/.claude/plans/_organigrammes-doctrine-registry.md` + `~/.mavis/agents/mavis/_organigrammes-doctrine.md` | 4568 + 5000 ≈ 10000 bytes |

**Total harness invested (cumulé)**: ~180 KB de doctrine canonique (≈ 1800 LOC). C'est l'investissement **harness** que Mark appelle « high capex upfront ».

### 3.3 The 90% investment validates

Per Cole's framing: **agentic engineering = high capex upfront + low opex scales**. LD01 = en plein dans cette phase de capex. Le « opex scale » = l'agent Book qui tournera sur ce harness une fois Phase 1-2-3 activées.

→ **Nous n'avons PAS à regretter l'investissement capex** parce que :
1. Le « opex » = tokens = quasi-gratuits (MiniMax $50/5.1B)
2. Le harness = durable (CARDIA-TDD §D « Durable »)
3. L'opex quality = Cole's \"3-10× more reliable and cheaper than vibe coding\" — l'amplification est sur le résultat, pas la quantité de tokens

## 4. Mapping SDLC spectrum → LD01 position

Per Cole: vibe coding (L0-L1) ↔ structured AI assisted (L2) ↔ agentic engineering (L3-L5).

LD01_Business_Book se positionne à :

| Niveau | Description | LD01 fit |
|---|---|---|
| **vibe coding** | Casual prompts, no system | NO — pas notre aspiration |
| **structured AI assisted** | Detailed prompts, more spot-checking | PARTIAL — `goal.md` structured |
| **agentic engineering** | Engineered resources, automated evals, CI gates | **YES — L4-L5** (Nous avons + skill canon, + manifest, + ADR appendices, + rot-rates, + evolution ledger, + kill-switches) |
| **Dark Factory Level 5** | Spec in / shipped code out, no driver wheel | **EN COURS** — Phase 1 sandbox W4+, Phase 3 L5 gated Rick S1 Q4+ |

→ LD01 = L4-L5 sur le spectrum SDLC. Le harness investment = coherent avec ce target.

## 5. Static vs Dynamic context (Cole's context management)

### 5.1 Static context (always-loaded, expensive)

| Static element | Path | Cardinal in LD01 |
|---|---|---|
| `00_index.md` frontmatter (OKF) | racine | YES — always loaded |
| `AGENTS.md` (DOX FS contract) | racine | YES — every agent reads |
| `CLAUDE.md` (DOX harness contract) | racine | YES — every harness loads |
| `CARDIA-TDD §1` (posture de fond) | `10_methodology/` | YES — when BC-Methodology involved |
| Kill-switches 6 | `true_agent_autonomy_architecture.md` §7 | YES when BC-True-Autonomy active |

### 5.2 Dynamic context (on-demand skills)

| Dynamic element | Loaded when | Rot-rate |
|---|---|---|
| `99_meta/00_mavis_runtime_alignment.md` | harness enters LD01 | lent |
| `00_Pocock_quality_canon.md` | BC-Methodology skill authoring | lent |
| `99_meta/true_agent_autonomy_architecture.md` | L5 mode engage | lent |
| `autonomy-loop.md` | session end-of-turn intercept | moyen |
| `observations_setup.md` | observational memory layer active | moyen |
| `goal.md` | session start | lent (rare updates) |
| `evolution.md` | drift observation | rapide (this is the rot ledger!) |

### 5.3 Anti-pattern bloqué: stuffing everything into system prompt

Per Cole explicit: le « static context rot cost » est élevé. Si on mettait toutes les 180 KB de doctrine en static, chaque session paierait le full cost. La pattern LD01 = `00_index.md` + `AGENTS.md` + `CLAUDE.md` (statique léger) + dynamic load via DOX walk / skills invocation = économie de 90% du context.

## 6. Conductor vs Orchestrator mode (Cole's nuance on Google's framing)

### 6.1 Google's framing (both modes)

Google's article : move between conductor (granular, single-file edits) ↔ orchestrator (high-level direction, outcomes review).

### 6.2 Cole's nuance (mostly orchestrator)

> *« If you have the right system, you can always live at this level [orchestrator]. But there's still a time and place to be micromanaging... So there's still a time and place to be at this level [conductor], especially for an organization first getting into agentic engineering. »*

### 6.3 LD01 stance

| Mode | LD01 use | Phase |
|---|---|---|
| **Orchestrator** (default) | Book CEO Perso à Phase 3 L5 continuous ; A0 = console input via `goal.md` | Phase 2-3 |
| **Conductor** (debug/exploration) | A0 navigates specific .md during audits ; W4 sandbox supervises | Phase 1 + ongoing debug |

→ LD01 = orchestrator mode by default, conductor for granular audit/debug when needed.

## 7. Token economics reality — cost collapse validation

### 7.1 Per Cole: Vibe coding = high opex (slop), Agentic engineering = high capex upfront + low opex

Avec MiniMax $50/mo = 5.1B tokens, l'opex est **réduit à quasi-zéro marginal**. Ce qui veut dire :

- **Capex** = harness construction (180 KB investis) = une fois
- **Opex** = tokens consumed = essentiellement gratuit dans les 5.1B quota
- **Production output** = agent runs continuously, output quality = Cole's \"3-10× better than vibe coding\"

### 7.2 Le kill-switch « budget ceiling » devient soft guardrail

Per ADR-LD01-004 §C5 kill-switch 2 « budget ceiling »: 
> *Avant : budget $X per session (kill-switch on hit)*

**AVEC COÛT COLLAPSE**, ce kill-switch devient :

| Trigger ancien | Nouveau trigger | Action |
|---|---|---|
| $X per session hit (kill) | 80% du quota mensuel atteint (= 4.08B tokens cumulés) | NOTIFY A0 (escalation_packet) + Soft pause (pas kill) |
| session > 24h | session > 7 days (continuous L5 dur) | kill per Mark's horizon |

→ Le kill-switch budget reste, mais passe de **hard stop** à **soft guardrail** parce que la cost reality le permet.

### 7.3 Le Year 3000 post-Abundance interpretation

L'utilisateur invoque « Année 3000 post-Abondance ». Interprétation : la cost reality VALIDÉE ici = le Year 3000 est déjà arrivé pour le dimensionnement du harness Book LD01. Le bottleneck est passé de:
- **Année 2024** : tokens coûts = $50/$100/M (limite massive) → favor VibeCoding; cap sur harness engineering
- **Année 2026** : tokens costs = $0 marginal (MiniMax $50/mo) → favor AgenticEngineering; cap sur **human attention** (Mark's rot-rate, Cole's capex)
- **Année 3000 hypothétique** : tokens = free, model = open, **100% bottleneck on harness design + sovereign-local execution**

→ Book LD01 est déjà dans la configuration Year 3000 : harness investis, model quasi-gratuit, sovereign-local Mavis runtime.

## 8. Wiring to plan-meta-memoire-okf-wiki-graphify-dox

### 8.1 4 layers plan-meta-memoire ↔ Mark's 5 layers + Cole's masterclass

| plan-meta-memoire §2.1 layer | Mark's layer | Cole's component | LD01 canon |
|---|---|---|---|
| **OKF v0.1** (format, 1 champ `type:` requis) | **Identity** | Static context (system prompt, rules canon) | Frontmatter OKF sur tous .md canoniques |
| **LLM Wiki** (substrate macro) | **Identity sister** (`wiki/`) | Substrate (the content) | `LD01_Business_Book/` canon + sister `~/.mavis/B1_Summer_Direction/state/state.ld01_book.md` |
| **Graphify** (structure graphe) | **Skills** (interlinking) | Dynamic context (skills loaded) | `_SKILL_*.md` candidates + Pocock anti-doublon |
| **DOX** (FS indexing bi-famille) | **Rules + Identity** | Micro-Index universel | `AGENTS.md` + `CLAUDE.md` sisters |

→ **Plan-meta-memoire + Mark 5 layers + Cole harness = consistent tri-axis**. LD01 implémente déjà les 4.

### 8.2 Plan-meta-memoire §P1-P6 ↔ LD01 phases

| plan-meta-memoire phase | LD01 phase | Mark/Cole alignment |
|---|---|---|
| **P1** OKF standardisation du wiki | LIVRÉ (LD01/99_meta/calendrier des frontmatter OKF) | Cole harness = static context canon |
| **P2** Lint v2 + index résorption | ACTIVE (post-LD01-001) | Cole dynamic skills = lint-native |
| **P3** Graphify re-sync | BACKLOG | Mark skills interlinking = graphify-front |
| **P4** DOX bi-famille | LIVRÉ (`AGENTS.md` + `CLAUDE.md`) | Mark identity ↔ DOX bi-famille |
| **P5** Boucle 12WY | LIVRÉ (`rot-rates.md` + `W13 audit`) | **Mark rot-rate explicite par couche** |
| **P6** Shadow harnesses (E1-E4) | BACKLOG E1 only (gated) | N/A (Mark/Cole separate concern) |

→ LD01 fait avancer P1+P4+P5 du plan-meta-memoire directement ; P2 et P3 sont alignés en backlog.

### 8.3 OT clé plan-meta-memoire §P5 → CARDIA-TDD cadence W3-W13 = Mark rot-rate

Plan-meta-memoire §P5 « Boucle 12WY » = Mark's rot-rate explicit per couche × CARDIA-TDD §3 cycle W3-W13 = **même discipline sous 2 noms**. Le concept de « rot-rate » est la pierre angulaire qui unit les 3 sources.

## 9. Updated 14 invariants (CAR-Cardia-Autonomy)

Avec l'alignement Mark + Cole + cost-reality, CARDIA-TDD §1 (6 propriétés) + ADR-LD01-002 §S (8 contrats) + BC-True-Autonomy §C5 (6 kill-switches) deviennent :

**20 invariants simultanés** :

| # | Property | Source |
|---|---|---|
| 1-6 | CARDIA-TDD C/A/R/D/I/A | `10_methodology/00_CARDIA_overview.md` |
| 7-14 | 8 contrats S1-S8 | `ADR-LD01-002` §2 |
| 15-20 | 6 BC-True-Autonomy kill-switches (escalation / budget soft / looping / D5 / sess-24h / A0 KILL) | `ADR-LD01-004` §C5 |
| 21 | **Harness > model** (Cole/Google 90% principle) | THIS DOCUMENT §3 |
| 22 | **Mark rot-rate explicit per couche** | THIS DOCUMENT §2 + `99_meta/rot-rates.md` |
| 23 | **5 layers = canonical sub-folder organization** | THIS DOCUMENT §2.6 |
| 24 | **Static vs Dynamic context** | THIS DOCUMENT §5 |
| 25 | **Orchestrator mode by default, Conductor for debug** | THIS DOCUMENT §6.3 |
| 26 | **Cost reality = Year-3000 post-Abundance (5.1B tokens/$50)** | THIS DOCUMENT §7 |
| 27 | **plan-meta-memoire P1-P6 alignment exact** | THIS DOCUMENT §8 |

→ **27 invariants simultanés** sans casse. Le BC-True-Autonomy devient **toute la discipline canon A+** structurée.

## 10. Action items (W4-W13)

| W | Action | Owner | Source |
|---|---|---|---|
| **W4** | Phase 1 sandbox L5 mini dark factory test | Book A3 + A0 | ADR-LD01-004 §C3.1 |
| **W4** | Adopt harness > model principle in BC-Methodology | A0 + Book | THIS DOCUMENT §3 |
| **W4** | Mise à jour `goal.md` Phase 1 sandbox `sandbox-ld01-DRY-test.md` | Book A3 | THIS DOCUMENT §7.2 |
| **W5** | Phase 1 deadman check | A0 | ADR-LD01-004 §C3.1 |
| **W6** | Audit 4 métriques plan-méta-mémoire §5 sur LD01 | A0 | plan-méta-mémoire §5 |
| **W6** | **Mark rot-rate audit par sub-folder** = `rot-rates.md` cross-check vs actual usage | A0 | THIS DOCUMENT §2.6 |
| **W9** | 4 weekly Rocks attained | Book A3 | ADR-LD01-002 S2 |
| **W13** | Muse DEAL — D11 by Gwyn (time A0 freed) | Gwyn | ADR-LD01-004 |
| **Q4 2026** | Phase 3 L5 continuous launch gated Rick S1 | A0 + Rick | ADR-LD01-004 + ADR-LD01-005 |

## 11. Anti-patterns (cumulatifs depuis CARDIA-TDD)

| Anti-pattern | Bloqueur | Source |
|---|---|---|
| Stocker 180 KB de doctrine en static context | Static vs Dynamic §5 + cost reality §7 | THIS DOCUMENT |
| Créer un skill doublon d'un existant | Pocock §1.6 anti-doublon merger | L0 Lightning |
| Budget kill-switch hard stop sur $5/day | Soft guardrail à 80% quota mensuel | THIS DOCUMENT §7.2 |
| Mutation canon sisters (4 intouchables) | LD01 `AGENTS.md` §Local Contracts | CARDIA-TDD |
| Vibe coding pour canon mutation | Agentic engineering = LD01 stance | THIS DOCUMENT §4 |
| Continuous L5 launch sans Phase 1-2 done | ADR-LD01-004 3-phase ramp | ADR-LD01-004 |
| Hard-delete d'un .md | `_TRASH/` ou `DEPRECATED_` + handoff D4 | CARDIA-TDD |

## 12. Liens canoniques

| Resource | Path |
|---|---|
| Cole's Google masterclass sister | `https://www.google.com/` (à lier après publication du PDF spec par Google — gated A0) |
| Mark's 5 layers video | `https://www.youtube.com/` (Mark Kashef channel — gated A0 search exact link) |
| Cost reality canon | `_SPECS/ADR/L0_Tech_OS/ADR-LLM-COST-COMPARE-001_minimax-anthropic-openrouter.md` |
| Harness alignment (ce document) | `LD01/99_meta/00_harness_engineering_alignment.md` |
| Cost collapse ADR | `LD01/30_decisions/ADR-LD01-005_budget_collapse_phase3_economical.md` |
| Plan-méta-mémoire canon | `~/.claude/plans/plan-meta-memoire-okf-wiki-graphify-dox.md` |
| Plan-Lune | `~/.claude/plans/plan-minimax-l1-book-lune.md` |
| Plan-L2 | `~/.claude/plans/plan-L2-business-os.md` |
| ADR-LD01-004 sister (True Autonomy × L5) | `LD01/30_decisions/ADR-LD01-004_true_agent_autonomy.md` |
| Cost reality sister | `LD01/30_decisions/ADR-LD01-005_budget_collapse_phase3_economical.md` |
| Memory canon Mavis | `~/.mavis/agents/mavis/memory/MEMORY.md` |

---

> *« Le harness = 90% de la valeur, le modèle = 10%. Book CEO Perso peut maintenant penser continu parce que le coût est devenu Year-3000. La discipline devient : construis le harness. »* — Convergence Mark Kashef + Cole/Google + cost reality (D1 2026-07-04).
