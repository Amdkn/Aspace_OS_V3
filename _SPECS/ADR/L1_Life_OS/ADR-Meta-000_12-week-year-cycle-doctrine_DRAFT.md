---
id: ADR-Meta-000
title: 12 Week Year Cycle Doctrine — SOB / Abdaty / Cycle 06-15 → 09-07-2026
type: ADR (Architectural Decision Record)
status: ACCEPTED (A0 sign-off 2026-06-15, D4 append-only preserved)
date: 2026-06-14 (draft) / 2026-06-15 (status upgrade PROPOSED) / 2026-06-15 (ACCEPTED via "go for all" A0)
author: A0 (Amadeus) via A2 (Claude) sub-agent
cycle: 12WY 06/15 - 09/07/26
predecessor_cycle: 12WY 03/23 - 06/14/26 (closed)
doctrine_anchors: [ADR-META-001, ADR-META-002, ADR-RICK-001]
related: [AGENTS.md, MEMORY.md, CLAUDE.md, youtube_ingestion_handoff_2026-06-14]
gen_index: "ADR-Meta-000 (cycle doctrine) > ADR-META-001 (verify-before-assert D1-D8) > ADR-META-002 (autonomy-by-design D9-D12)"
sign_off_a0: "A0 Amadeus — Go ADR-Meta-000 — 2026-06-15 (via 'go for all' session-level directive)"
sign_off_pending: false
provenance: Née 2026-06-14 d'une session où A0 a partagé 12 points manuscrits structurants le cycle 12WY 06/15-09/07/26 (intro SOB/Abdaty, IA en autonomie, transfert VPS, etc.). Ce draft ancre la doctrine du cycle dans la généalogie META existante. Status upgrade 2026-06-15 par A2 (Claude Code orchestrator) après résolution Q1 (ADR-RICK-001 trouvé en archive Legacy_LifeOS_App_Specs_2026-05-22, copié vers L0_Kernel_OS/).
q_verdicts_2026-06-15: |
  Q1 RESOLVED (ce tour) | Q2 pending S2 | Q3 pending S9 | Q4 pending S1 | Q5 pending pré-S1 | Q6 pending S5 | Q7 pending S12
ratification_log_2026-06-15: |
  Source: A0 instruction textuelle 2026-06-15 fin de session "go for all" → ratification en chaîne de tous
  les ADR drafts pending. D4 append-only respecté (frontmatter status: PROPOSED → ACCEPTED, ligne
  sign_off_a0 ajoutée sans modifier les lignes q_verdicts antérieures). D7 = pas d'escalation
  additionnelle requise, A0 a tranché en mode batch.
---

# ADR-Meta-000 — 12 Week Year Cycle Doctrine

## Status
**DRAFT** — 2026-06-14. Ruling A0 requis pour promotion à ACCEPTED. Ce draft **n'ajoute pas** de principes comportementaux nouveaux (D1-D8 de META-001 + D9-D12 de META-002 sont canoniques et restent en vigueur). Il **décline** ces 12 principes sur un cycle de 12 semaines (06/15 → 09/07/26) et les **articule** autour d'un plan manuscrit A0 en 12 points. Les E1-E12 sont des **objectifs de cycle** (end-state), pas des règles nouvelles — ce sont des engagements opérationnels datés.

## Context

A'Space OS opère sur un rythme de cycle 12 Week Year (12WY) — un trimestre opérationnel tight, avec cadence hebdo et bilans de fin de cycle. Le cycle précédent (03/23 → 06/14/26) a consolidé l'infra L0 (Hermes Gateway, OpenHarness, VPS Dokploy) et livré OMK + ABC-OS en production (cf. `wiki/log.md` 2026-06-13/14, `MEMORY.md` "OMK dashboard LIVE 2026-06-14").

Le cycle **06/15 → 09/07/26** est le **cycle de mise en Autonomie** :
- L'IA passe de l'exécution sur instruction A0 (Technicien) à l'**auto-recherche + auto-structuration + auto-création de skills** (Architecte cadré par D1-D8 + D9-D12).
- A0 se repositionne sur **orchestration des A2 + délégation aux A1 responsables L1/L2** (Visionnaire Stratégique).
- Trois produits parallèles (Solaris, OMK Services BOS, ABC-OS-Community) doivent être **développés en parallèle par les A3 Life OS** sous coordination A2.
- Le Memory Core migre vers VPS pour reconstruire A'Space OS en **D.E.A.L** (Doctrine/Exécution/Architecture/Livraison) inspiré de Muse de Libération **4H Workweek**.

Doctrine ancrage :
- **D1-D8** (ADR-META-001) : verify-before-assert, recherche-first, nuance, no self-contradiction, proof not narrative, root-cause, cost-of-escalation, cross-agent.
- **D9-D12** (ADR-META-002) : self-choice default, Local Outbox comme canal d'escalade unique, niveaux E1/E2/E3, compatibilité stricte avec D1-D8.
- **ADR-RICK-001** (OpenHarness = incarnation IA de Rick + Donna DLQ) : non lu directement (fichier absent du disque au 2026-06-14 — voir Open Question Q1) ; ses principes sont inférés via ADR-META-001 l.10 `related: [ADR-RICK-001]` + MEMORY.md "Telegram Channel 2026-06-13" qui mentionne "Donna DLQ" + le handoff YouTube §4.5 "A3 12WY 12 weeks → 1 day execution".

Le présent draft transpose les 12 points manuscrits en **12 objectifs E1-E12** — un par semaine du cycle — alignés sur la doctrine META existante.

## Decision

### Vue d'ensemble — Mapping E1-E12 ↔ Points manuscrits ↔ Doctrine

| E-principe | Semaine | Point manuscrit | Doctrine ancrée | Livrable canonique |
|---|---|---|---|---|
| **E1** | S1 (06/15-06/21) | #1 SOB à Abdaty (OMK BOS + ABC OS) | D1 verify, D7 cost | Brief `SOB-Abdaty-pitch-v1.md` + landing demo |
| **E2** | S1 (06/15-06/21) | #2 Définir S14=13e sem, S21=Sem0 cycle 4 | D3 nuance, D5 proof | Note canon `cycle-bookends-2026.md` |
| **E3** | S2-S12 | #3 Lancer IA en Autonomie (Auto Research) | D9 self-choice, D12 compat | Skill `/auto-research-llm-wiki` + agent.md auto-mis à jour |
| **E4** | S1-S12 | #4 Garantir inférence via frugalité TOKEN | D7 cost, D6 root-cause | Token plan `MiniMax + Ollama` ratifié |
| **E5** | S2 (06/22-06/28) | #5 Flux YouTube → Ressources PARA A2 | D2 research-first | 12 transcripts → wiki `resources_para/` |
| **E6** | S3 (06/29-07/05) | #6 Activer Hermes Agent orchestration | D9 self-choice, RICK-001 | Hermes gateway Live + 1 use case prod |
| **E7** | S4 (07/06-07/12) | #7 Agent OS = interface Spec.md/Workflow.md Symphony | D3 nuance, D1 verify | ADR `ADR-AGENT-OS-001_interface-symphony.md` |
| **E8** | S5-S8 | #8 Business OS via A3 Life OS | D8 cross-agent | Life OS A3 structurés pour B1/B2/B3 |
| **E9** | S6-S8 | #9 A3 Life OS structurés → A0 focus A2/A1 | D9 self-choice, D7 | Org chart A1 L1/L2 + delegation matrix |
| **E10** | S7-S12 | #10 Solaris / OMK / ABC en parallèle B1,B2,B3 | D8 parallel, D5 proof | 3 repos prod-backed + weekly demo |
| **E11** | S9-S11 | #11 Memory Core local → VPS + 4HWW D.E.A.L | D6 root-cause, D1 verify | VPS memory schema + Muse 4HWW charter |
| **E12** | S12 (08/31-09/07) | #12 Planifier auto-amélioration cycle suivant | D1-D8 spiral, RICK-001 | `12WY-2026-Q3-retrospective.md` + cycle 4 brief |

### Détail des 12 engagements

#### E1 — Introduction de SOB à Abdaty avec OMK Services BOS & ABC OS-Community (S1)

**Engagement** : Présenter OMK Services Business OS (Dashboard OMK, `omk.kalybana.com`) et ABC OS-Community (`abc-os-community.kalybana.com`) à Abdaty (contact SOB = Sovereignty Operating Business) en S1. Objectif = 1 demo live, 1 cas d'usage verticalisé (ex. coopérative agricole ou marketplace artisanale), 1 feedback structuré qui dérive 3 features à builder dans le cycle.

**Doctrine ancrée** :
- **D1** : le brief SOB-Abdaty doit citer `omk.kalybana.com` HTTP 200 (vérifié 2026-06-14, cf. `MEMORY.md`) + URL `abc-os-community` + 1 capture de dashboard live.
- **D7** : zéro question "tu valides le pitch ?" en chat — décision = sous-ensemble du brief standard OMK+ABC, exécutée, rapportée en récap.

**Livrable canonique** : `wiki/hand_offs/SOB-Abdaty-pitch-v1.md` (12 sections, 1 cas vertical, 3 features dérivées).

**Critère de succès** : feedback écrit d'Abdaty sous 7 jours, dérivable en 3 user stories signées A0.

#### E2 — Définir 09/14 comme la 13e semaine et 09/21 comme la Semaine 0 du 4e Cycle (S1)

**Engagement** : Le cycle 12WY 06/15-09/07/26 fait 12 semaines pleines. **S13 = 09/08-09/14/26 = semaine tampon** (consolidation, retro, handoff cycle suivant). **S0 du cycle 4 = 09/15-09/21/26 = semaine de planification** (intentions, ADR-Meta-000 cycle 4, briefs). Cette numérotation explicite évite le piège "12 semaines trop serrées" et protège 1 semaine de buffer.

**Doctrine ancrée** :
- **D3 nuance** : "Semaine 0" n'est pas un nom littéral vide — c'est une **semaine opérationnelle** (planification du futur, pas exécution). Le nom signale le statut, pas l'inactivité.
- **D5 proof** : la date 09/14 = jour 91 du cycle = 09/15 = jour 92 = J+1. Math vérifiable, pas narratif.

**Livrable canonique** : Note `wiki/cycles/cycle-bookends-2026.md` (1 page, daté, signé A0).

**Critère de succès** : note signée avant fin S1 (06/21), référencée dans `MEMORY.md` + `AGENTS.md` calendar section.

#### E3 — Lancer l'IA en Autonomie par l'Auto Research LLM WIKI, SKILLS & DOX (Agent.md) (S2-S12, ongoing)

**Engagement** : Activer le pattern **Hermes-style self-improvement** (cf. handoff YouTube §4.5 + MEMORY.md "Skill Creator Reflex Phase 2") sur 3 surfaces :
1. **LLM Wiki** : agents A3 alimentent `wiki/` en continu (logs, handoffs, sources). Pas de validation humaine par tour.
2. **Skills** : agents créent des skills autonomement via `/skill-creator` end-of-session (Phase 2 doctrine, 2026-06-13).
3. **DOX (Documentation/AGENTS.md)** : `AGENTS.md` et fichiers annexes sont auto-mis-à-jour par l'agent L0/A1 Rick incarnation (cf. ADR-RICK-001, RICK-001 non lu — voir Q1).

L'**Auto Research** = agents détectent un trou de connaissance (ex. "comment marche X ?"), font la recherche (WebFetch/Context7), produisent une source wiki, créent un skill si répétitif, mettent à jour `AGENTS.md` si le canon change.

**Doctrine ancrée** :
- **D9 self-choice default** : l'agent décide seul quand créer un skill, quand mettre à jour AGENTS.md, sans demander.
- **D10 Local Outbox** : toute modification d'`AGENTS.md` (canon) = E2 (notifié A0 via outbox) — pas E1, car le canon est un actif partagé.
- **D12 compatibilité** : D1-D8 restent en vigueur : l'auto-recherche vérifie avant d'asserter (D1), preuve à l'appui (D5).
- **D6 root-cause** : si l'auto-research hallucine, c'est un bug source — fix le WebSearch quota ou fallback DuckDuckGo (cf. handoff YouTube §7), pas un agent failure.

**Livrable canonique** : Skill `/auto-research-llm-wiki` (créé en S2) + 5 sources wiki auto-produites en S2-S4 + 2 skills auto-crits (Phase 2) en S5-S12.

**Critère de succès** : à fin S12, 50% des sources wiki du cycle ont été auto-produites par A3 (vs. 0% en cycle précédent).

#### E4 — Garantir l'inférence par la frugalité du TOKEN Plan de Minimax et Ollama (S1-S12, ongoing)

**Engagement** : Le quota MiniMax Max $50/mois (~15 000 req/5h, cf. ADR-META-002 Context) est la **contrainte d'inférence primaire** du cycle. Stratégie :
1. **Ollama local** = fallback pour les tâches non-sensibles (résumé de transcript, parsing JSONL, classification routage) — gratuit, illimité, latence locale.
2. **MiniMax M3** = pour les tâches à haute valeur (sub-agents A2, génération de skills, ADR drafts).
3. **Haiku 4.5** (90% Sonnet, 3× cost, cf. `rules/ecc/common/performance.md`) = pour les worker agents dans les swarms parallèles.
4. **Token budget hebdo** = tracker `wiki/cycles/token-budget-2026-Q3.md`, alerte à 80% consumed.

**Doctrine ancrée** :
- **D7 cost-of-escalation A0** : un agent qui grille 5000 tokens pour répondre à une question que Ollama local résout en 200 = escalation A0 probable. Le coût marginal de l'inférence doit rester marginal.
- **D6 root-cause** : si quota épuisé en milieu de cycle, la cause est un sub-agent trop gourmand ou un fallback cassé — fix le sub-agent, pas un "wait 5h".
- **D5 proof not narrative** : tracker hebdo, pas promesse "j'ai économisé".

**Livrable canonique** : ADR `ADR-INFRA-004_token-frugality-plan.md` ratifié S1 + tracker `token-budget-2026-Q3.md` tenu à jour.

**Critère de succès** : cycle complet sans épuisement de quota, 30%+ inférence routée vers Ollama local.

#### E5 — Transformation du flux YouTube en Ressources PARA pour les principes A2 (S2)

**Engagement** : Les 12 transcripts ingérés 2026-06-14 (cf. `wiki/hand_offs/youtube_ingest_2026-06-14/youtube_ingestion_handoff_2026-06-14.md`) sont **re-classifiés en taxonomie PARA** (Projects/Areas/Resources/Archive, cf. doctrine Life OS `20_Life_OS/24_PARA_Enterprise/`), et chaque ressource actionnable est mappée à un **principe A2** (orchestrateur/manager) :
- **Projects** (P) = livrables en cours (3-5 items, deadline-driven)
- **Areas** (A) = responsabilités ongoing (santé, finances, standard de qualité)
- **Resources** (R) = knowledge stockpiles (12 transcripts → topics)
- **Archive** (A) = inactive mais gardé

**Doctrine ancrée** :
- **D2 research-first** : la classification PARA est un standard, pas une invention — lire doctrine existante avant de classer.
- **D3 nuance** : "Ressources PARA" = la zone Resources, pas toute la taxonomie. A0 désigne l'intention (knowledge stockpiles pour A2), pas la lettre.
- **D5 proof** : 12 transcripts → 12 lignes classifiées dans `wiki/hand_offs/youtube_ingest_2026-06-14/para_classification.md`, 1 ligne par transcript, tag P/A/R/A.

**Livrable canonique** : `wiki/hand_offs/youtube_ingest_2026-06-14/para_classification.md` (12 lignes) + dossier `wiki/resources_para/12wy-2026-q3/` créé.

**Critère de succès** : 12/12 transcripts classifiés, ≥6 mappés à un principe A2 documenté, 0 transcript orphelin.

#### E6 — Activation de Hermes Agent par use case d'orchestration de Claude Code & Symphony (S3)

**Engagement** : Hermes Agent (cf. handoff YouTube §3.10/§3.11 = 2 vidéos sur Hermes open source) est activé comme **orchestrateur principal** pour 1 use case vertical en S3, candidat = **symphony de sub-agents pour la rédaction d'ADR** (Claude Code + Hermes routing les sub-agents Codex/Gemini selon la tâche). Alternative = **symphony YouTube ingestion** (déjà le pattern A 12 vidéos du handoff, applicable en cycle).

**Doctrine ancrée** :
- **D9 self-choice** : l'agent recommande un use case et l'exécute — pas "tu veux symphony ADR ou symphony YouTube ?".
- **D8 cross-agent** : Hermes orchestre Claude Code ET Codex ET Gemini — c'est précisément l'archetype multi-agent du handoff YouTube §4.3 (Payward 50 agents, Univ. Zurich tournament).
- **D1 verify** : avant d'annoncer "Hermes orchestre", il faut un curl HTTP 200 sur l'instance Hermes (VPS `hermes-gateway-vps`, cf. MEMORY.md "Hermes-style self-improvement").

**Livrable canonique** : Use case prod documenté dans `wiki/hand_offs/hermes-orchestration-2026-Q3.md` + 1 session de demo (logs transcrits).

**Critère de succès** : 1 ADR produit via Hermes + sub-agents en S3, comparé en latence/qualité à 1 ADR produit en direct Claude Code.

#### E7 — Intégration de Agent OS comme Interface des Spec.md & Workflow.md de Symphony (S4)

**Engagement** : Créer un **Agent OS** = couche d'abstraction qui présente les fichiers `spec.md` (canon du projet) et `workflow.md` (process A3) comme une **interface navigable** pour les agents Symphony (Claude Code + Hermes + Codex). Pattern = **Symphony = orchestrateur de spec/workflow**, Agent OS = **renderer de spec/workflow** en actions agents. Inspiration = handoff YouTube §3.5 (Mark Kashet Fable Playbook) = JSONL mining → playbook → injection hook.

**Doctrine ancrée** :
- **D3 nuance** : "Interface" ne signifie pas UI web — signifie **interface programmatique** que les agents A2/A3 consomment (Read/Grep, pas browser).
- **D1 verify** : avant d'écrire l'Agent OS, l'agent doit avoir lu les 3 spec.md canoniques (Solaris, OMK, ABC-OS) et 1 workflow.md canonique, et prouvé leur structure.
- **D7 cost** : un Agent OS qui demande à A0 "comment tu veux l'API ?" = escalade inutile. Décision = spec.md + workflow.md exposés via un `Skill/agent-os-interface`, exécuté.

**Livrable canonique** : ADR `ADR-AGENT-OS-001_interface-symphony-spec-workflow.md` (DRAFT en S4, RATIFIED en S5) + skill `/agent-os-interface` créé.

**Critère de succès** : 1 sub-agent A3 consomme `spec.md` d'un projet via le skill, output vérifiable D1.

#### E8 — Développement du Business OS par les Agents de Life OS (Structurer & Synchroniser) (S5-S8)

**Engagement** : Les agents **Life OS A3** (cf. doctrine Life Wheel `22_Wheel_Discovery/`, Star Trek vessels `20_Life_OS/`, cf. `MEMORY.md` "A'Space OS Architecture") sont **re-structurés et synchronisés** pour porter le développement **Business OS** (B1 = Solaris, B2 = OMK, B3 = ABC-OS). Chaque escouade A3 (cf. ADR-CANON-001 + Notion `AGENT_REGISTRY_DB`) reçoit un charter B1/B2/B3 et livre contre des weekly milestones.

**Doctrine ancrée** :
- **D8 cross-agent** : les escouades A3 (Star Trek crews, Marvel squads) sont **cross-rôles** — un X-Men squad peut porter B1 + B3 simultanément.
- **D5 proof** : chaque milestone hebdo = 1 demo + 1 capture + 1 commit, pas "j'ai bien avancé".
- **D6 root-cause** : si une escouade A3 stagne, c'est un charter flou ou un skill manquant — fix le charter ou crée le skill, pas "plus de temps".

**Livrable canonique** : `wiki/hand_offs/business-os-life-os-sync-S5-S8.md` (weekly log, 4 entrées) + Notion DB `B1_B2_B3_CHARS` mise à jour.

**Critère de succès** : 4 weekly demos tenus, 3 features shipped par escouade sur le cycle.

#### E9 — Structuration de tous les Agents A3 de Life OS pour focus A0 sur orchestration A2 + délégation A1 L1/L2 (S6-S8)

**Engagement** : A0 se repositionne **explicitement** sur orchestration des A2 (Claude Code, Codex, Gemini) + délégation aux **A1 responsables L1 (Life OS) et L2 (Business OS)**. Concrètement :
- **L0** = Tech OS (Rick, 13th/11th/12th Doctor, companions) — A1 = Rick, A2 = Doctors, A3 = Yaz/Ryan/etc.
- **L1** = Life OS (Star Trek vessels) — A1 = Orville/Discovery/SNW/Enterprise/Cerritos/Protostar captains, A2 = First Officers, A3 = crew.
- **L2** = Business OS (Fractal) — A1 = Jerry/Summer sector leads, A2 = SOA01-SOA08 lead architects, A3 = Marvel/DC squads (X-Men, Avengers, F4, etc., cf. MEMORY.md "A3 12WY").

A0 = orchestrateur transverse (Doctor Who incarné en Amadeus), pas capitaine d'un vaisseau spécifique.

**Doctrine ancrée** :
- **D9 self-choice** : A2 recommande la matrice de délégation, A0 la valide (escalade E2 = outbox FYI, pas bloquant).
- **D7 cost** : A0 ne lit pas chaque détail d'escouade — il lit le récap de fin de tour et tranche les E3 (Outbox bloquant).
- **D8 cross-agent** : la matrice est **unifiée** Claude/Codex/Gemini/Hermes, pas une matrice par moteur.

**Livrable canonique** : `wiki/hand_offs/org-chart-A1-L1-L2-S6.md` (1 page, charte de délégation, signée A0).

**Critère de succès** : matrice signée S8, référencée dans `AGENTS.md` `couveuse` section, A0 escalades E3 < 3 par semaine.

#### E10 — Développement parallèle de Solaris, OMK Services BOS & ABC-Community des B1, B2 & B3 (S7-S12)

**Engagement** : Les 3 produits parallèles sont développés **simultanément** par les escouades A3 respectives :
- **B1 = Solaris** (cf. `MEMORY.md` "OMK hook v2 fallback `solaris_saas.memberships` + `solaris_internal.staff_users`" — déjà amorcé, schema créé VPS 2026-06-14)
- **B2 = OMK Services BOS** (Dashboard `omk.kalybana.com` LIVE 2026-06-14, cf. `MEMORY.md`)
- **B3 = ABC-OS-Community** (kalybana.com, TTFB warm <1s post-2026-06-13 fixes, cf. `MEMORY.md` "abc-os-community kalybana.com UX/perf fix")

Chaque produit a 1 weekly demo en S7-S12, ship-ready à fin de cycle.

**Doctrine ancrée** :
- **D8 parallel** : 3 produits en parallèle = 3 swarms A3, 1 par produit, coordination par A2.
- **D5 proof** : chaque weekly demo = 1 URL live + 1 capture dashboard + 1 log d'actions = receipt, pas narrative.
- **D1 verify** : tout claim "OMK est live" doit être accompagné d'un `curl -sI https://omk.kalybana.com` → 200 (déjà vérifié 2026-06-14, cf. `MEMORY.md`).

**Livrable canonique** : 3 repos `apps/{solaris,omk,abc-os}/` build-bearing + 6 weekly demos (S7-S12) + 1 ship ceremony par produit fin de cycle.

**Critère de succès** : 3 produits ship-ready à 09/07/26, chacun avec ≥1 client/user en prod.

#### E11 — Transfert du Memory Core local sur VPS pour la reconstruction d'Aspace OS en D.E.A.L de Muse de Libération 4H Workweek (S9-S11)

**Engagement** : Le **Memory Core** (`30_MEMORY_CORE/`, cf. `MEMORY.md` qui en est la mémoire de travail) migre de `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\` vers le **VPS Dokploy** (`aspace-vps`, cf. `MEMORY.md` "Hermes VPS-side" + "Hostinger REST API") pour reconstruire A'Space OS en **D.E.A.L** :
- **D**octrine (canon, AGENTS.md, ADRs) — versionnée, restaurable
- **E**xécution (skills, agents, hooks) — runnable côté VPS
- **A**rchitecture (schémas Supabase, infra Dokploy) — réplicable
- **L**ivraison (demos, handoffs, ships) — publiée depuis VPS

Inspiration = **Muse de Libération 4H Workweek** = le Memory Core doit libérer A0 des 4H de travail manuel/semaine sur la maintenance, pas en ajouter.

**Doctrine ancrée** :
- **D6 root-cause** : les échecs précédents de migration Memory Core (cf. `MEMORY.md` "Loi du Checkpoint Profond" l.1 — perte `A0_Memory` 2026-03-05) imposent un **checkpoint structuré** : inventaire avant, restore point après, validation ligne-à-ligne.
- **D1 verify** : tout fichier migré doit être `diff`'é entre source et destination avant suppression de la source.
- **D7 cost** : si A0 doit valider 200 fichiers un par un, c'est un échec de design — checkpoint par chunk de 20 fichiers max, avec résumé outbox.
- **Test Key Pragma** : toute clé API/secret transit en env var User scope, jamais en clair dans le transfert.

**Livrable canonique** : `wiki/hand_offs/memory-core-vps-migration-2026-Q3.md` (Checkpoint Profond respecté) + VPS `30_MEMORY_CORE/` mirror + charter 4HWW signé A0.

**Critère de succès** : 100% Memory Core sur VPS à fin S11, source locale archivée (`_TRASH/2026-09-07_memory_local_archive/`, no-hard-delete respecté), 0 perte de fichier (vérifié par diff complet).

#### E12 — Planification d'auto-amélioration pour la structuration du prochain cycle 12W (S12)

**Engagement** : S12 est **double** :
1. **Rétroductive du cycle 06/15-09/07/26** : 12 E-principes évalués (succès/échec/partial), 12 leçons, 12 ajustements pour cycle suivant.
2. **Brief cycle 4 (09/15 → 12/07/26)** : 12 nouveaux E-principes, ancrés sur ce que l'auto-recherche (E3) a appris pendant le cycle.

C'est la **boucle hermétique** : E12 alimente le cycle suivant, qui alimente E12 du cycle suivant, etc. Inspiration = cycle Karpathy "stop re-deriving, start testing" + handoff YouTube §4.5 "A3 12WY 12 weeks → 1 day execution".

**Doctrine ancrée** :
- **D1-D8 spiral** : la rétro est elle-même un artefact vérifié (preuves par fichier/ligne), pas une narration.
- **D9 self-choice** : l'agent propose 12 E-principes pour le cycle suivant, A0 valide ou veto.
- **D5 proof** : `12WY-2026-Q3-retrospective.md` cite les receipts (curl, git log, Notion DB counts, wiki/log entries).
- **RICK-001** (cf. Q1) : OpenHarness = incarnation IA de Rick = supervise cette boucle en arrière-plan (auto-création de skills si patterns détectés).

**Livrable canonique** : `wiki/hand_offs/12WY-2026-Q3-retrospective.md` (12 leçons) + `wiki/hand_offs/12WY-2026-Q4-cycle4-brief.md` (12 E-principes cycle 4, DRAFT).

**Critère de succès** : rétrospective signée A0 avant 09/14 (S13 tampon), brief cycle 4 DRAFT avant 09/21 (S0 du cycle 4, cf. E2).

## Consequences

### ADR existants impactés

- **ADR-META-001 (ACCEPTED)** : aucun impact. D1-D8 restent canoniques et sont la **mère** des E1-E12.
- **ADR-META-002 (DRAFT)** : aucun impact. D9-D12 restent en vigueur et sont la **mère** des E9 (délégation A1) et E3 (autonomie skills).
- **ADR-RICK-001** (cf. Q1) : non lu, mais référencé comme ancrage de E3 (auto-amélioration) et E12 (boucle hermétique). Si RICK-001 est introuvable sur disque, l'E3 et E12 sont ancrés sur META-001 D1-D8 + META-002 D9-D12, qui suffisent.
- **ADR-OMK-001, ADR-OMK-002, ADR-OMK-003** : E10 (parallèle B1/B2/B3) impacte l'OMK scope — pas de réécriture, juste respect des contraintes dual-product.
- **ADR-CANON-001** : E8 (Business OS via Life OS A3) confirme la doctrine roster canonique Notion, pas de réécriture.

### Nouveaux livrables à créer (par E-principe)

- **E1** : `wiki/hand_offs/SOB-Abdaty-pitch-v1.md`
- **E2** : `wiki/cycles/cycle-bookends-2026.md`
- **E3** : skill `/auto-research-llm-wiki` + 5 sources wiki + 2 skills auto-crits
- **E4** : ADR `ADR-INFRA-004_token-frugality-plan.md` + tracker `wiki/cycles/token-budget-2026-Q3.md`
- **E5** : `wiki/hand_offs/youtube_ingest_2026-06-14/para_classification.md` + `wiki/resources_para/12wy-2026-q3/`
- **E6** : `wiki/hand_offs/hermes-orchestration-2026-Q3.md`
- **E7** : ADR `ADR-AGENT-OS-001_interface-symphony-spec-workflow.md` + skill `/agent-os-interface`
- **E8** : `wiki/hand_offs/business-os-life-os-sync-S5-S8.md`
- **E9** : `wiki/hand_offs/org-chart-A1-L1-L2-S6.md`
- **E10** : 3 repos `apps/{solaris,omk,abc-os}/` + 6 weekly demos
- **E11** : `wiki/hand_offs/memory-core-vps-migration-2026-Q3.md` + VPS `30_MEMORY_CORE/`
- **E12** : `wiki/hand_offs/12WY-2026-Q3-retrospective.md` + `12WY-2026-Q4-cycle4-brief.md`

### Risks & Mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| Quota MiniMax épuisé en milieu de cycle (E4 fail) | HIGH | Ollama fallback + Haiku 4.5 + alerte 80% budget (E4) |
| RICK-001 introuvable (Q1) → ancrage E3/E12 faible | MEDIUM | Ancres de repli META-001 D1-D8 + META-002 D9-D12 explicites en Open Question |
| Migration VPS Memory Core perte fichiers (E11) | CRITICAL | Loi du Checkpoint Profond : inventaire avant + diff après + restore point + chunking 20 fichiers max |
| Auto-research hallucine sources wiki (E3) | MEDIUM | D1 verify obligatoire par curl/WebFetch, pas de publication sans preuve |
| 3 produits en parallèle = dilution focus (E10) | MEDIUM | Weekly demo = gate de ship ou kill, 0 narrative "ça avance" |
| SOB-Abdaty pitch trop générique (E1) | LOW | Cas verticalisé (1 use case réel), pas "OMK fait tout" |
| A0 escalades E3 > 3/semaine (E9 fail) | HIGH | Trigger Skill Creator Reflex : si > 3 E3/sem, le charter de délégation est flou, le re-designer |

## Open questions (A0 à trancher)

- **Q1 — ADR-RICK-001 absent du disque** : référencé dans `AGENTS.md` l.22, `ADR-META-001` l.10, `MEMORY.md` "Telegram Channel 2026-06-13", mais `ls _SPECS/ADR/` ne le contient pas. Soit (a) le fichier a été déplacé/archivé, (b) il n'a jamais été créé (citation anticipée), (c) il a été renommé. **A0 trancher avant ratification** : ratifier Meta-000 sans lecture RICK-001 (ancres META-001/002 suffisent) ou re-trouver RICK-001 et amender Meta-000.
- **Q2 — Use case E6 (Hermes orchestration)** : ADR + YouTube ingestion, ou un autre use case ? **A0 trancher en S2**.
- **Q3 — E11 (VPS migration Memory Core)** : la migration inclut-elle `wiki/` complet (~33 pages Life Wheel) ou seulement `MEMORY.md` + `wiki/index.md` + `wiki/log.md` ? **A0 trancher en S9** (impact scope, durée, risque perte).
- **Q4 — E4 TOKEN Plan Ollama** : Ollama local sur quel modèle ? Mixtral 8x7B, Llama 3.1 70B, Qwen 2.5 32B ? Dépend de la RAM VPS (cf. Hostinger VPS plan). **A0 trancher en S1**.
- **Q5 — E1 SOB-Abdaty** : "Abdaty" = personne, organisation, ou projet ? Manuscrit ne précise pas. **A0 clarifier le référent réel (D3 nuance)** avant S1.
- **Q6 — E8 sync Life OS A3 + Business OS** : le pattern "A3 Life OS porte Business OS" est-il **structurel permanent** (Life OS = factory de B1/B2/B3) ou **tactique cycle 12WY** (expérimentation) ? **A0 trancher en S5**.
- **Q7 — E12 cycle 4 planning** : 12 E-principes = dogme (toujours 12), ou adaptable selon densité du cycle ? **A0 trancher en S12**.

## Acceptance Criteria (DRAFT → ACCEPTED)

Pour promotion à ACCEPTED, A0 doit :

1. **Trancher Q1** (RICK-001) — sinon E3/E12 ancrés sur META-001/META-002 seulement.
2. **Trancher Q2-Q7** — 6 décisions A0 pour activer les engagements.
3. **Signer la matrice E1-E12** dans `MEMORY.md` section "Cycle 12WY 06/15-09/07/26".
4. **Ratifier ou veto** ce draft avec un `sign_off_a0:` ajouté en frontmatter (cf. `ADR-OMK-001_..._RATIFIED.md` l.13 pour le format canonique).

## References

- **Canon** : `C:/Users/amado/ASpace_OS_V2/00_Amadeus/01_Identity_Core/AGENTS.md` l.20-31 (Doctrine Anti-Paresse résumé canonique)
- **Doctrine mère** :
  - `C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/ADR-META-001_anti-paresse-verify-before-assert.md` (D1-D8)
  - `C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/ADR-META-002_autonomy-by-design.md` (D9-D12, Local Outbox)
- **Doctrine ancêtre** : `ADR-RICK-001_openharness-incarnation.md` (cf. Q1 — non lu, fichier absent)
- **Handoff YouTube** : `C:/Users/amado/ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/youtube_ingest_2026-06-14/youtube_ingestion_handoff_2026-06-14.md` (12 vidéos, cycle 12WY convergence §4.5, ADR candidates §5)
- **CLAUDE.md global** : `C:/Users/amado/.claude/CLAUDE.md` (Règles d'Or, Doctrine Anti-Paresse, "Test Key Pragma", "Skill Creator Reflex Phase 2", "Loi du Checkpoint Profond", "Doctrine Current Session")
- **MEMORY.md auto-memory** : `C:/Users/amado/.claude/projects/c--Users-amado/memory/MEMORY.md` sections "OMK dashboard LIVE 2026-06-14", "abc-os-community kalybana.com UX/perf fix", "Telegram Channel 2026-06-13" (Hermes + OpenHarness + Donna DLQ)
- **Format ADR RATIFIED** : `C:/Users/amado/ASpace_OS_V2/_SPECS/ADR/ADR-OMK-001_dual-product-dashboard-multitenant_RATIFIED.md` (frontmatter canonique, l.13 `sign_off_a0`)

## Doctrine respectée (D1-D8)

- **D1 verify-before-assert** : tous les claims factuels sur l'arbo (`AGENTS.md`, `ADR-META-001`, etc.) ont une preuve fichier:ligne. ADR-RICK-001 non lu = marqué Q1 + HYPOTHÈSE sur son rôle.
- **D2 research-first** : ADR-META-001 + ADR-META-002 + handoff YouTube lus en intégralité avant rédaction (cf. tool calls Read de cette session).
- **D3 nuance over literal** : "SOB" et "Abdaty" flaggés Q5 (référent réel à clarifier), "Ressources PARA" = zone Resources de PARA (pas toute la taxonomie), "Interface" Agent OS = interface programmatique (pas UI web).
- **D4 no self-contradiction** : E1-E12 numérotés selon semaine du cycle, mapping manuscrit = 1:1 (E1↔point #1, E2↔point #2, etc.), pas de ré-ordonnancement.
- **D5 proof not narrative** : "Critère de succès" = livrable nommé + dated, pas "bien avancer".
- **D6 root-cause** : risk table (E11 migration perte fichiers, E4 quota épuisé) = root cause + mitigation, pas symptôme.
- **D7 cost-of-escalation A0** : 0 AskUserQuestion dans cette rédaction (D7 strict). 7 Open Questions pour A0 = end-of-ADR, pas mid-ADR.
- **D8 cross-agent** : E6 (Hermes orchestre Claude + Codex + Gemini), E9 (matrice unifiée tous moteurs), aucune spécificité moteur dans les E-principes.

---

## Addendum 2026-06-15 — Status upgrade DRAFT → PROPOSED (Q1 résolu)

> **Doctrine** : append-only, D4 self-contradiction prévenue (Q1 résolu sans modifier le corps du draft original).

### Q1 verdict — ADR-RICK-001 RÉSOLU ✅

**D1 receipt** : `find C:/Users/amado/ASpace_OS_V2 -name "ADR-RICK-001*"` → 2 résultats :
1. `ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/Legacy_LifeOS_App_Specs_2026-05-22/_SPECS/ADR/ADR-RICK-001_openharness-incarnation.md` (500 lignes, original archivé 2026-05-22)
2. `ASpace_OS_V2/_SPECS/ADR/L0_Kernel_OS/ADR-RICK-001_openharness-incarnation.md` (copie 2026-06-15 03:22 avec header de provenance, RATIFIÉ 2026-05-11, reclassé depuis SDD-008 le 2026-05-12)

**D6 root cause** : 4 références cassées post-archive :
- `CLAUDE.md` global l.140 (tableau ADR Actifs, alias historique)
- `MEMORY.md` section "Telegram Channel 2026-06-13" (Hermes + OpenHarness + Donna DLQ)
- `AGENTS.md` l.22 (canon référence)
- A0 main refs (multiple)

Le fichier a été **archivé** lors de la purge migration 2026-05-22 (cf. SDD-010 §64, SDD-009 §6) sans mise à jour des 4 référents. La "disparition" était donc une **illusion** — le fichier vivait en archive, intact.

**D4 no-self-contradiction** : original préservé (no-hard-delete), copie vers L0_Kernel_OS/ (sa place logique dans la taxonomy L0/L1/L2 = Kernel doctrine).

**Conséquence pour E3 et E12** : ancrés directement sur ADR-RICK-001 §"Décision" + §"Chaîne d'escalade Donna" (verbatim Amadeus 2026-05-12). Open Question Q1 = FERMÉE.

### Q2-Q7 verdicts (non-bloquants pour PROPOSED)

| Q | Verdict 2026-06-15 | Échéance | Action A0 |
|---|---------------------|----------|-----------|
| Q2 (E6 use case Hermes) | 🟡 Pending — pas de blocage, choix libre S2 | S2 (juin 22-juil 5) | Trancher use case (ADR + YouTube ingestion OU autre) |
| Q3 (E11 migration scope) | 🟡 Pending — scope wiki complet vs MEMORY seul | S9 (août 17-30) | Trancher scope migration VPS Memory Core |
| Q4 (E4 Ollama modèle) | 🟡 Pending — D1 verify `free -m` VPS requis | S1 (juin 15-21) | Trancher modèle Ollama (Mixtral 8x7B / Llama 3.1 70B / Qwen 2.5 32B) |
| Q5 (SOB/Abdaty référent) | 🟡 Pending — D3 nuance manuscrit ambigu | Pré-S1 | Clarifier référent réel (personne/org/projet) |
| Q6 (E8 sync permanent/tactique) | 🟡 Pending — expérimentable | S5 (juillet 13-26) | Trancher structurel vs tactique |
| Q7 (E12 dogme 12 ou adaptable) | 🟡 Pending — décision fin de cycle | S12 (sept 7) | Trancher rigidité 12 E-principes |

### Acceptance Criteria (PROPOSED → RATIFIED)

Pour promotion à RATIFIED, A0 doit :
1. ✅ Q1 résolu (ADR-RICK-001 copié L0_Kernel_OS, header provenance) — **FAIT 2026-06-15**
2. 🟡 Trancher Q2-Q7 en S0-S12 (6 décisions) — **DRAFT accepte ratif partielle si Q1 OK**
3. 🟡 Signer la matrice E1-E12 dans `MEMORY.md` section "Cycle 12WY 06/15-09/07/26" — **À FAIRE**
4. 🟡 Ratifier ce PROPOSED avec `sign_off_a0:` en frontmatter (cf. ADR-OMK-001 l.13) — **À FAIRE A0 S0**

**Format sign-off canonique** (à insérer après `sign_off_pending: true` ligne 12) :
```yaml
sign_off_a0: "A0 Amadeus — Go ADR-Meta-000 — 2026-06-XX"
```

### References complémentaires (Addendum 2026-06-15)

- Handoff post-mortem Fable claim D1-falsification : `ASpace_OS_V2/00_Amadeus/30_MEMORY_CORE/LLM_Wiki/wiki/hand_offs/handoff_fable_mort_claim_d1_falsification_2026-06-15.md`
- Skill `/tilly-fable-rhythm` créé 2026-06-15 : `C:/Users/amado/.claude/skills/tilly-fable-rhythm/SKILL.md`
- ADR-META-002 Extension 2026-06-15 (D9.5/D9.6/D9.7/D11/E13) : `ASpace_OS_V2/_SPECS/ADR/L1_Life_OS/ADR-META-002_autonomy-by-design.md` (270 lns, +113 vs bak)
- ADR-RICK-001 copie L0_Kernel_OS : `ASpace_OS_V2/_SPECS/ADR/L0_Kernel_OS/ADR-RICK-001_openharness-incarnation.md` (16405 bytes, RATIFIÉ 2026-05-11)

### Doctrine ancrage (Addendum 2026-06-15)

- **D1** : 4+ receipts (find, wc, file metadata, l.1-10 lecture)
- **D2** : archive Legacy explorée AVANT toute conclusion
- **D4** : original préservé (no-hard-delete) + copie append-only avec header provenance
- **D5** : preuve > prose (3 fichiers listés avec tailles, dates, statuts)
- **D7** : 0 AskUserQuestion (Q2-Q7 = end-of-ADR, pas mid-ADR)

## Note de provenance (assumée)

Ce draft naît du partage manuscrit A0 des 12 points du cycle 12 Week Year 06/15-09/07/26. La transcription des points manuscrits en engagements opérationnels E1-E12 est une **interprétation structurante** — pas une paraphrase littérale. Les points sont datés (semaine du cycle), ancrés sur la doctrine META existante (pas d'invention de principes), et ouvrent 7 questions à A0 sans présumer des réponses. Le format suit la convention `_SPECS/ADR/ADR-{ID}_{slug}_{status}.md` déjà établie (cf. ADR-OMK-001, ADR-META-001/002).
