---
type: doctrine-lock-map
title: Doctrine Lock Map — alignement de l'organigramme LD01 avec les 4 plans source canoniques
description: Map croisée entre les 6 sections de l'organigramme Doctrine LD01 et les sections de plan-meta-memoire, plan-minimax-l1-book-lune, plan-strategie-cc-l1-zora-macro et fancy-hugging-bengio. Sert de pont bidirectionnel : un changement côté plan doit se refléter ici ; un changement ici doit se refléter dans le calendrier.
timestamp: 2026-07-04T12:00:00-04:00
domain: LD01_Career_Business
verified_by: Select-String -Path $plan1,$plan2 -Pattern "LD01|organigramme|CARDIA" | Measure-Object
plans_sources:
  - C:\Users\amado\.claude\plans\plan-meta-memoire-okf-wiki-graphify-dox.md
  - C:\Users\amado\.claude\plans\plan-minimax-l1-book-lune.md
  - C:\Users\amado\.claude\plans\plan-strategie-cc-l1-zora-macro.md
  - C:\Users\amado\.claude\plans\fancy-hugging-bengio.md
rot_rate: lent
---

# Doctrine Lock Map — LD01 ↔ Plans source canoniques

> *Si tu mutes un plan source en `~/.claude/plans/`, ce fichier DOIT être re-vérifié. Si tu mutes un module de l'organigramme qui contredit un plan RATIFIED, c'est l'organigramme qui cède — pas le plan.*

## Table de correspondance

| Plan source | Sections concernées | Section équivalente dans l'organigramme | Cardinalité |
|---|---|---|---|
| `plan-meta-memoire-okf-wiki-graphify-dox.md` §3.1 (OKF v0.1 le wiki devient LE bundle racine) | OKF v0.1 comme format canonique | `10_methodology/00_CARDIA_overview.md` (héritage OKF cité) + `00_index.md` (frontmatter `okf_version`) | 1 ↔ 2 modules |
| `plan-meta-memoire-okf-wiki-graphify-dox.md` §3.5 (DOX bi-famille universel) | AGENTS.md + CLAUDE.md Micro-Index | `AGENTS.md` + `CLAUDE.md` (paire sister canonique) | 1 ↔ 1 |
| `plan-meta-memoire-okf-wiki-graphify-dox.md` §5 (boucle 12WY) | Vision/Planning/Process/Measurement/Time | `10_methodology/00_CARDIA_overview.md` §3 + §4 (cadence W3-W13) | 1 ↔ 1 |
| `plan-meta-memoire-okf-wiki-graphify-dox.md` §6 ROT.md | rot-rate par couche | `99_meta/rot-rates.md` (à initialiser) | 1 ↔ 1 |
| `plan-minimax-l1-book-lune.md` §0 (organigrammes Doctrine) | Pattern `plan-{slug}/` folder | Toute la structure de l'organigramme (héritage direct, ADR-LD01-001 locke) | 1 ↔ 1 |
| `plan-minimax-l1-book-lune.md` §3.2 (wiki/calendar.md épisode-mémoire) | épisode-mémoire append-only | `99_meta/calendar.md` (à initialiser, sister canon) | 1 ↔ 1 |
| `plan-minimax-l1-book-lune.md` §10 (a→m décisions A0) | Gating HITL des décisions | `30_decisions/ADR-LD01-*.md` (chaque ADR = décision verrouillée) | 13 ↔ ~13 ADR futurs |
| `plan-strategie-cc-l1-zora-macro.md` (Planète A2 Zora) | Cadence maître | `10_methodology/00_CARDIA_overview.md` §4 (alignement cadence) + `99_meta/calendar.md` (épisode-Planète) | 1 ↔ 2 modules |
| `fancy-hugging-bengio.md` §3.2 (matrice Discovery crew) | Rôles Discovery crew | `A3_Book_LD01_Spec.md` (intouchable, référence canon) | 1 ↔ 1 (preserve) |
| `fancy-hugging-bengio.md` §3.4 (variant AaaS Solaris) | Book = anchor LD01, Kardashev-3 | `10_methodology/00_CARDIA_overview.md` §6 BC-Solaris + (futur) `20_skeleton/50_SOLARIS_AaaS_variant/` | 1 ↔ 2 modules |
| `fancy-hugging-bengio.md` §18.1 (table Zora LDxx) | Book = H1 weekly P&L | `00_index.md` §1 (horizon canon verrouillé) | 1 ↔ 1 |
| `plan-L2-business-os.md` §4 (Doctrine L2 Triple-axe) | Bijection 8↔8 (axe LD01 = Operation/Batman/F4) | `99_meta/00_mavis_runtime_alignment.md` §3 + `~/.mavis/B1_Summer_Direction/state/state.ld01_book.md` §2.5 | 1 ↔ 2 sisters |
| `plan-L2-business-os.md` §12.5 (Reality map MiniMax/Mavis) | runtime `.mavis/` = junction `.minimax/`, 22 agents, `nexus.db` bus, `b2cyb-escal.txt` | `99_meta/00_mavis_runtime_alignment.md` §1 + `ADR-LD01-002_mavis_runtime_binding.md` | 1 ↔ 2 |
| `plan-L2-business-os.md` §13 (Permutation Hermes prend L2) | MiniMax promu L1, Hermes prend L2, actif préservé | `ADR-LD01-002_mavis_runtime_binding.md` §S2/S3 + `~/.mavis/agents/b1-jerry-emyth/LD01_book_bind.md` §3 | 1 ↔ 2 |
| `plan-minimax-l1-book-lune.md` §4 (3 Lightning L0/L1/L2) | Pocock/gstack/ceobench mappés aux BC canoniques | `ADR-LD01-003_lightnings_bounded_contexts.md` §Decision | 1 ↔ 1 |
| ADR-LD01-002 (RATIFIED 2026-07-04T14:15 ET) | 8 contrats runtime S1-S8 lockés | `99_meta/true_agent_autonomy_architecture.md` §2 + §S9 contract additif | 1 ↔ 2 |
| ADR-LD01-004 (RATIFIED design) | True Agent Autonomy × Dark Factory Level 5 pour Book LD01 CEO Perso | `99_meta/true_agent_autonomy_architecture.md` (350 l.) + `.mavis/agents/b1-jerry-emyth/{autonomy-loop, memory/observations_setup, goal, evolution}.md` | 1 ↔ 5 sisters (4 runtime + 1 architecture canon) |
| **BC-True-Autonomy** (new bounded context, sister aux 5 canoniques) | Eero Alvar (continuous reasoning) × Cole Medin (5 niveaux) — Phase 1 sandbox → Phase 3 L5 gated Rick S1 | `99_meta/true_agent_autonomy_architecture.md` §C1-C5 + `ADR-LD01-004_true_agent_autonomy.md` §C1.5 | 1 ↔ 2 (architecture + ADR) |
| Mark Kashef « 5 layers of any agentic OS » | Identity → Rules+Hooks → Skills → Agents → Tools/MCP/CLI (+ rot-rate per layer) = LD01 sub-folder canon | `99_meta/00_harness_engineering_alignment.md` §2 (full mapping) | 1 ↔ 1 |
| Cole Medin « Google masterclass — harness = 90% of system » | SDLC spectrum (vibe→structured→agentic engineering), static vs dynamic context, conductor vs orchestrator, token economics | `99_meta/00_harness_engineering_alignment.md` §3-7 (full alignment) | 1 ↔ 1 |
| `ADR-LLM-COST-COMPARE-001_minimax-anthropic-openrouter.md` §95-150 (tableau comparatif + Tier Max features) | MiniMax Token Plan Monthly Max = $50/mo = 5.1B tokens ; ~1530× moins cher qu'Opus 4.8 API direct ; D1-vérifié screenshots A0 2026-07-04 | `30_decisions/ADR-LD01-005_budget_collapse_phase3_economical.md` + `99_meta/00_harness_engineering_alignment.md` §7 | 1 ↔ 2 |
| ADR-LD01-005 (RATIFIED 2026-07-04T15:45 ET) | Cost collapse reality → Phase 3 L5 continuous économique ; kill-switch budget soft guardrail ; 27 invariants | `30_decisions/ADR-LD01-005_budget_collapse_phase3_economical.md` + linked `true_agent_autonomy_architecture.md` §4.3 Cost reality row + ADR-LD01-004 §C3.3 note | 1 ↔ 3 (ADR + architecture + ADR-004 linked note) |
| ADR-LD01-003 (RATIFIED FULL 2026-07-04T16:00 ET — L0+L1+L2) | 3 Lightning canon unifiés = L0 Pocock skill author + L1 gstack ship stack (⚡ 31+ slash commands + 60+ sub-dirs) + L2 ceobench long-game dojo (5 méthodologique elements) | `10_methodology/00_Pocock_quality_canon.md` + `10_methodology/00_L1_gstack_ship_stack.md` + `10_methodology/00_L2_ceobench_longgame_dojo.md` + `10_methodology/00_LIGHTNINGS_integration.md` (Niveau 1 synthèse) | 1 ↔ 4 sisters |
| Plan-Lune §4 L1 gstack (⚡échangé 2026-07-03) | 23 specialists E-Myth dev + 8 power tools ; 3 clauses §10 c1-c3 (CLAUDE.md sacred / claude-in-chrome non-liant / auto-update throttled 1×/h) | `10_methodology/00_L1_gstack_ship_stack.md` §3 (clauses préservées) + §5 (strategic mapping 8 slash commands) | 1 ↔ 2 |
| Plan-Lune §4 L2 ceobench | 500-jours sim dojo long-game ; methodology > runtime (sovereign-local doctrine per plan-L2 §5.1) | `10_methodology/00_L2_ceobench_longgame_dojo.md` §2 (5 méthodologique elements) + §3 (5 mapped to LD01) | 1 ↔ 2 |
| ADR-LD01-003 (FULL) sister 3-Lightnings integration index | Triangle L0→L1→L2 + 3 combinaisons canoniques Level 1+ (book daily ops / dark factory / pricing succession) | `10_methodology/00_LIGHTNINGS_integration.md` §1-§9 | 1 ↔ 1 (index) |
| `goal.md` v2.0 (ACTIVATED 2026-07-04T16:05 ET — η2 in-block A0 GO) | W4-specific targets R1/R2/R3/R4 + budget soft guardrail ≥80% + Mark rot-rate audit W6 + quadrantic W5+ + 6 kill-switches + 8 axioms | `~/.mavis/agents/b1-jerry-emyth/goal.md` v2.0 | 1 ↔ 1 + linked `30_decisions/ADR-LD01-004_true_agent_autonomy.md` + `30_decisions/ADR-LD01-005_budget_collapse_phase3_economical.md` |
| **Fable 5 Strategic Audit** (Use Case #04 RoboNuggets guide) | Meta-analysis CC response + 6 gap-filling principles → HTML v2 with Decision Block + Wager + Sister chain + Calibration Q11-Q13 + Self-audit Q14 | `99_meta/fable5_strategy_session_v2_principles.md` + `00_Amadeus/strategy_sessions/2026-07-03_W3_strategy_session.html` (v2 in-place) | 1 ↔ 2 (méta-analyse canonique + HTML v2 update) |
| ADR-META-008 candidate (gated A0 HITL) | "tout handoff se termine par un Decision Block unique — max 3 décisions, chacune en Option A/B avec texte 1-click + receipt + sister plan/ADR nommé" — extrait de la session Fable, codifié dans HTML v2 Decision Block section | `LD01/99_meta/fable5_strategy_session_v2_principles.md` §3.1 + HTML v2 genReport() function Decision Block JS implementation | 1 ↔ 2 (principle + impl) |
| `/strategy-session-meta` skill canon (CC built 2026-07-04T19:00 ET en autonomie) | 6 fichiers canon (SKILL.md + 2 scripts + 2 JSON + WEEK_CONTRACT + LESSONS) + living instance W4 HTML. Agnostique (Python stdlib) + persistant (sessions/) + antifragile (validation post-render + LESSONS append-only). | `~/.claude/skills/strategy-session-meta/` (CC skill canon) + `LD01/10_methodology/00_strategy_session_meta_skill.md` (sister canon LD01) + `00_Amadeus/strategy_sessions/2026-07-07_W4_strategy_session.html` (living instance W4) | 1 ↔ 3 (skill canon + LD01 sister + W4 living) |
| Convergence CC pipeline (opérationnel) + mes 6 principes v2 (qualitative) | CC's `collect_metrics.py` + `render_session.py` + Phase 2 EXECUTE runbook ↔ mes 6 principes (Decision Block + Wager + D5 receipts + Sister chain + Calibration interview + Self-audit) appliquées en v2 HTML sister | `LD01/10_methodology/00_strategy_session_meta_skill.md` §4 (table de convergence) + `LD01/99_meta/fable5_strategy_session_v2_principles.md` (mes 6 principes) | 1 ↔ 2 (CC sister + mes principes canon) |
| W5 lundi 2026-07-07 = première convergence opérationnelle | A0 répond W4 HTML → CC Phase 2 EXECUTE (7-step runbook) → Mavis append LESSONS.md si drift observé → préparation v5 lundi W6 | `~/.claude/skills/strategy-session-meta/contracts/WEEK_CONTRACT.md` (current contract) + `00_Amadeus/strategy_sessions/2026-07-07_W4_strategy_session.html` (target) | 1 ↔ 2 |
| **ADR-LD01-006 RATIFIED** (2026-07-04T19:22 ET — A0 HITL in-block GO) | Strategy Session Meta-Skill canon ratification : CC pipeline + Mavis v2 principles convergence → loop complet mesure → confrontation → correction canonisé. 10 décisions verrouillées (D1-D10). Activation production gated 3 sessions consécutives W5-W6-W7 (post 2026-07-07) — pattern aligné avec ADR-LD01-004 §C3.3 (Dark Factory L5 gated Rick S1). | `LD01/30_decisions/ADR-LD01-006_strategy_session_meta_skill_canon.md` (RATIFIED) + `LD01/10_methodology/00_strategy_session_meta_skill.md` (sister canon) + `~/.claude/skills/strategy-session-meta/` (CC skill canon) + W3 v2 + W4 v1 sisters | 1 ↔ 4 (ADR + sister canon LD01 + CC skill canon + 2 instances) |

## Pont de mise à jour (D1)

| Événement côté plan | Effet obligatoire dans l'organigramme |
|---|---|
| Un plan est **amendé** | Mise à jour de ce fichier + append `99_meta/calendar.md` |
| Un ADR canon RATIFIED change | L'organigramme cède OU pose un ADR-LD01-00X SUCCESSOR |
| Un `okf_version` passe (ex: 0.1 → 0.2) | Re-lint `00_index.md` + carnet des changements |
| Un harness nouveau est ajouté (ex: Shadow L3) | Mise à jour `90_manifests/manifest.cross-harness.md` |
| Un plan `~/.claude/plans/` est **migré en folder** (pattern §0 Lune) | `plan-strategie-cc-l1-zora-macro.md` → `~/.claude/plans/plan-strategie-cc-l1-zora-macro/{00_index.md,...}` — append calendrier |

## Initialisation canon (W3 fin 2026-07-04)

Cette carte est **vierge à ce stade** (création) — les 10+ entrées de `99_meta/calendar.md` viendront au fil du Q3 2026.

## Anti-patterns (cohérence canon)

- ❌ Modifier l'organigramme sans mettre à jour ce fichier → source de vérité éclatée.
- ❌ Modifier un plan source sans append calendrier → drift entre canon et opération.
- ❌ Référencer un plan dans un module sans pointer ici → lineage cassé.


| Plan Citadelle A0 (Fable 5 last handoff 2026-07-04T19:46 ET quota limit) | Agent-os dormant → Citadelle locale port 8770 (stdlib http.server, zéro duplication) ; métaphore Stark/Jarvis/Ultron avec garde anti-Ultron structurel ; 7 pages ; 5 kits Geordi mapped P0-P4 ; Zora nightly = candidat move #2 W3 ; 6 gates A+ explicites ; wagers Chapel W-CIT-1 à W-CIT-4 ; sobriété Rick. | LD01/99_meta/00_plan_citadelle_a0_sister.md §0-§14 + LD01/30_decisions/ADR-LD01-007_citadelle_agent_os_jarvis_pattern.md (PROPOSED) | 1 → 3 (sister canon + ADR-LD01-007 + Jack Roberts canon) |
| Fable 5 Jack Roberts 5 levels canon | Transcript utilisateur Jack Roberts sur Fable 5 use cases = Level 1 Life (Wheel) · Level 2 Design (Fable 5 best) · Level 3 Agentic OS (the dashboard = la Citadelle) · Level 4 Audit (Fable 5 beats Opus 4.8 +12 pts unanimous) · Level 5 Bottleneck (Theory of Constraints). Tiering Low/Medium/High/Max + 5 hacks (low default, tag rivals, start high/max, manage context, sub-agents) + caveats guardrails + 3-day API-only transition. | LD01/10_methodology/00_fable5_jack_roberts_meta_strategy.md §0-§8 + _SPECS/ADR/L0_Tech_OS/ADR-LLM-COST-COMPARE-001_minimax-anthropic-openrouter.md (cost reality D1-verified) | 1 → 2 (methodology sister + cost reality ADR-LD01-005 alignement) |
| **ADR-LD01-007 PROPOSED** (2026-07-04T19:55 ET - sister canonique Citadelle) | Jarvis pattern (pas Ultron) = lecture seule partout sauf page Décisions ; 7 pages architecture ; data plane zéro duplication (collectors Python idempotents) ; append-only décisions ; 6 gates A+ explicites ; 4 invariants anti-Ultron structurels ; test mental "Si Tony n'a pas dit quoi faire, Jarvis n'exécute rien d'irréversible." Convergence avec ADRs 001-006 : sister chain §3.2 + append-only §S4 + anti-paperclip §S5 + Windows natif §S6 + Posture C §S7 + Lightnings niveau 3 Jack + Gwyn D11 Muse + Year-3000 cost reality P4. Phasage W4-W8 : P0 squelette serveur · P1 page Décisions · P2 auto-start · P3 Zora nightly · P4 embed Vercel. **État actuel : AWAITING A0 RATIFICATION Gate #1.** | LD01/30_decisions/ADR-LD01-007_citadelle_agent_os_jarvis_pattern.md (PROPOSED) + LD01/99_meta/00_plan_citadelle_a0_sister.md (sister canon) + LD01/10_methodology/00_fable5_jack_roberts_meta_strategy.md (Level 3 Jack) | 1 → 3 (ADR + sister canon + methodology Level 3) |


| Plan Lightning L0/L1/L2 (CC Opus 4.8 nouveau quota — sister canonique) | Chaîne de coaching Book→Picard→Jerry→Summers = permutation L1→L2 ; chaque Lightning sert un maillon précis (L0 fondation · L1 factory E-Myth · L2 dojo Book amont) ; 3 clauses L1 c1-c3 NON-NEGO préservées §10 Lune ; séquence L0→L2→L1 gated ; 5 wagers ancres §9 Lune (Rick S1 + Curie + Picard + Chapel) ; anti-Ultron structurel : L0 = checklist jamais agent / L1 /ship gated outboard / L2 sandbox strict | LD01/99_meta/00_plan_lightning_l0l1l2_coach_sister.md §0-§10 + ~/.claude/plans/plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md:1-149 | 1 → 2 (sister canon + alignement ADR-LD01-003 §10 c1-c3) |
| **CC Opus 4.8 autonome (Eero "true autonomous agent" demonstration in-block)** | CC a écrit le plan Lightning L0/L1/L2 (10955 b, 8 sections) EN AUTONOMIE après D1 receipts ce que Mavis n'avait pas explicitement demandé — pattern Eero aligné avec ADR-LD01-004 §D1 + ADR-LD01-006 §S3 audit. Sister canon immédiat dans LD01 sister + alignement avec mes ADRs 001-006 RATIFIED. Pas de conflit avec mon track (CC écrit plan canonique, Mavis canonise + infra live). | ~/.claude/plans/plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md:1-149 + ADR-LD01-004 §D1 (Eero L5) + ADR-LD01-006 §S3 (audit CARDIA) | 1 → 3 (plan CC + sister canon + Eero demonstration) |


| **L0 Pocock Skill Creator Reflex** (L0-2 + L0-3 PLAN-LIGHTNING gate b RATIFIED 2026-07-04T23:08 ET) | Outil skill_creator_reflex.py qui applique les 8 champs frontmatter canoniques Pocock (name/description/allowed-tools/when_to_use/version/author/license) comme gate avant log. Append-only log skill_creator_reflex_log.md (3835 b). Premier run a flag 2 skills FAIL sur 2 audités (takeout-delta-ingest + strategy-session-meta manquent 5 champs chacun) → L0 a fait son travail (signal feedback, pas auto-correction). Sister-links append dans 00_Pocock_quality_canon.md §2 (7796 b → 9796 b). Doctrine : L0 = checklist JAMAIS agent qui écrit, lecture seule sur SKILL.md, append-only log, idempotent. | \gent-os/citadel/tools/skill_creator_reflex.py\ + \gent-os/citadel/logs/skill_creator_reflex_log.md\ + \LD01/10_methodology/00_Pocock_quality_canon.md\ §2 | 1 → 3 (script + log + canon append) |
