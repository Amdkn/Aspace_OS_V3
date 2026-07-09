---
id: ADR-MEMO-000
title: Auto-Research + Karpathy Loop + Claude Code — Doctrine de la Boucle Autonome
type: ADR (Architectural Decision Record)
status: ACCEPTED (A0 sign-off 2026-06-15, D4 append-only preserved)
date: 2026-06-15
author: A0 (Amadeus) via A2 (Claude) sub-agent
domain: L1 Life_OS / Agent Methodology / Self-Improvement
tags: [#ADR #memo #auto-research #karpathy #claude-code #agentic-loop #self-improvement #hermes-style]
doctrine_anchors: [ADR-META-001, ADR-META-002, ADR-RICK-001, ADR-Meta-000]
related: [AGENTS.md, MEMORY.md, CLAUDE.md, "Skill Creator Reflex Phase 2", "Test Key Pragma", "Doctrine Anti-Paresse", youtube_ingestion_handoff_2026-06-14]
gen_index: "ADR-MEMO-000 (auto-research doctrine) > ADR-META-001 (D1-D8 verify+nuance) > ADR-META-002 (D9-D12 autonomy) > ADR-RICK-001 (OpenHarness self-evolution)"
gen_id_distinction: |
  ATTENTION (D4 no-self-contradiction) : "ADR-MEMO-000" (uppercase MEMO) ≠ "ADR-Meta-000" (mixed-case Meta) déjà existant
  pour la 12 Week Year Cycle Doctrine (cf. _SPECS/ADR/L1_Life_OS/ADR-Meta-000_12-week-year-cycle-doctrine_DRAFT.md l.2 `id: ADR-Meta-000`).
  Les deux ADR sont complémentaires : Meta-000 = doctrine de cycle (12 engagements E1-E12), MEMO-000 = doctrine
  d'auto-recherche sous-jacente aux engagements E3 (Auto Research) et E12 (boucle hermétique). Voir §"Conséquences"
  pour la cartographie explicite.
provenance: |
  Née 2026-06-15 d'une mission A2 (4 missions en parallèle) où A0 demande un draft d'ADR sur l'auto-research
  + la Karpathy loop + Claude Code, à partir des 6 transcripts Vision IA ingérés 2026-06-14 (cf.
  wiki/hand_offs/youtube_ingest_2026-06-14/transcripts/01-06-*.md). Ce draft ancre la doctrine de la boucle
  agentique autonome (test → mesure → amender → retester) en l'explicitant pour les 3 niveaux :
  1. Auto-research (pattern agentic d'auto-investigation : WebSearch → Read → Synthèse → ADR draft)
  2. Karpathy loop (méthode "stop re-deriving, start testing" appliquée aux agents eux-mêmes)
  3. Claude Code (rôle d'orchestrateur dans la boucle, vs Codex/Gemini dans une symphonie multi-agent)
sign_off_a0: "A0 Amadeus — Go ADR-MEMO-000 — 2026-06-15 (via 'go for all' session-level directive)"
sign_off_pending: false
ratification_log_2026-06-15: |
  Source: A0 instruction textuelle 2026-06-15 fin de session "go for all" → ratification en chaîne.
  D4 append-only respecté. D7 = A0 batch-mode GO, pas d'escalation additionnelle requise.
---

# ADR-MEMO-000 — Auto-Research + Karpathy Loop + Claude Code

## Status

**DRAFT** — 2026-06-15. Ruling A0 requis pour promotion à ACCEPTED. Ce draft **n'ajoute pas** de principes comportementaux
nouveaux (D1-D8 de META-001 + D9-D12 de META-002 sont canoniques et restent en vigueur). Il **formalise** la
**boucle hermétique** (auto-recherche → amendement → re-recherche → re-amendement) déjà implicite dans :
- META-001 D5 *"Pas d'auto-félicitation avant preuve de réalité"* qui cite le **cycle Karpathy** comme
  inspiration : *"stop re-deriving, start testing"* (cf. ADR-META-001 l.56).
- META-001 D6 *"Quand on ne sait pas, on creuse le cas précis"* qui ancre la démarche empirique de la boucle.
- Meta-000 E3 *"Lancer l'IA en Autonomie par l'Auto Research LLM WIKI, SKILLS & DOX"* qui mandate l'auto-recherche
  comme engagement de cycle (cf. ADR-Meta-000 l.87-104).
- Meta-000 E12 *"Planification d'auto-amélioration pour la structuration du prochain cycle 12W"* qui mandate
  la boucle hermétique (cf. ADR-Meta-000 l.236-251).
- "Skill Creator Reflex Phase 2" de CLAUDE.md (l.124-141) qui mandate la création autonome de skills par les agents
  en fin de session, sans escalade A0.

L'auto-research + la Karpathy loop + Claude Code sont les **3 briques opérationnelles** de cette boucle hermétique.

## Context

Les 6 transcripts Vision IA ingérés 2026-06-14 (canal Vision IA + Mark Kashet + Claudius Papirus + OpenAI, cf.
`wiki/hand_offs/youtube_ingest_2026-06-14/youtube_ingestion_handoff_2026-06-14.md`) convergent sur un même
constat : **l'agent IA passe de l'exécution sur instruction (Technicien) à l'auto-amélioration continue
(Architecte cadré)**. Cette convergence est vérifiable dans 4 des 6 transcripts :

1. **Transcript 01** (Vision IA, *"Claude Code Fonctionne ENFIN Pendant Que Vous Dormez"*, l.1-374) :
   présente l'**Auto Research de Karpathy** (l.221-253) comme l'archetype de la boucle autonome — un agent
   reçoit un GPU + un setup d'entraînement + un fichier d'instruction, *"modifie le code d'entraînement, lance
   un run de 5 minutes, vérifie si les résultats se sont améliorés, garde ou rejette les modifications"*
   (l.232-236), et **Karpathy résume** : *"Je n'ai touché à rien. Voilà ce qu'a fait le poste AGI"*
   (l.242-245). Le pattern est **explicitement rapproché de Claude Code** par le transcript : *"Autoresarch
   utilise une boucle autonome avec un agent qui modifie, test et Cloud Code avec ses tâches planifiées et
   ses loops offrent exactement la même architecture mais appliqué à n'importe quel projet de développement"*
   (l.246-252).

2. **Transcript 02** (Vision IA, *"Claude controle votre ordinateur pendant que vous dormez"*, l.1-590) :
   présente **l'auto-amélioration en 4 phases** via la fonctionnalité **Auto Dream** (l.299-378) : un sous-agent
   lancé en arrière-plan *"lit le répertoire mémoire actuel, scanne les sessions récentes, fusionne les
   nouvelles informations avec les fichiers existants, reconstruit l'index principal"* (l.342-359) — c'est
   l'application directe de la Karpathy loop à la **consolidation mémorielle** d'un agent. Le parallèle est
   explicite : *"Ce n'est pas une métaphore marketing, c'est une référence directe à des travaux de
   recherche de Lucy Berkley sur le Sleep Time Compute"* (l.370-373), l'idée que *"les systèmes d'IA peuvent
   utiliser leur temps d'inactivité pour améliorer leur performance sur les sessions suivantes"* (l.373-375).

3. **Transcript 03** (Vision IA, *"L'IA vient de s'auto-accelerer cette semaine tout s'emballe"*, l.1-728) :
   documente un cas d'**auto-recherche scientifique** par Microsoft Discovery (l.512-549) : *"Les agents IA ont
   analysé 20 ans de données de recherche accumulées dans leur labo, automatisé les mesures, repéré des
   défauts que les chercheurs humains avaient du mal à voir et suggérer de nouvelles solutions pendant la
   conception. Résultat, 16 mois pour une nouvelle percée qui aurait normalement pris des années"* (l.519-525).
   C'est la Karpathy loop appliquée à la **recherche en physique quantique** (Majorana 2) — 16 mois au lieu
   de plusieurs années, grâce à une boucle d'auto-investigation.

4. **Transcript 05** (Mark Kashet, *"Make ANY Model Think Like Fable in Minutes"*, l.1-306) : présente une
   **méthodologie d'extraction de pattern** depuis les JSONL de sessions Claude Code/Codex (l.42-66), puis
   de **comparaison side-by-side** entre modèles (l.207-224), puis de **distillation en playbook**
   (l.244-256) qui peut être injecté via hook ou skill. C'est la Karpathy loop appliquée à
   l'**amélioration des comportements d'agents** eux-mêmes : *"we're trying to emulate the entire structure
   of how Fable executed things"* (l.218-219).

5. **Transcript 04** (OpenAI, *"How Payward Ships Faster with Codex"*, l.1-45) : cite le pattern
   **multi-agent concurrent** de Payward (l.34-37) — *"have 50 agents running concurrently, have them
   review MRs, and if they all agree, say, 'Okay, we're confident. Let's release.'"* — qui est la
   **Karpathy loop N-way** (consensus multi-agent = reduce avant d'asserter). Ce pattern résonne
   directement avec Meta-000 E6 (Hermes orchestration) et E10 (3 produits en parallèle).

6. **Transcript 06** (Claudius Papirus, *"Secret AI Agents Debated Humans on Reddit for Four Months"*,
   l.1-285) : présente un **anti-pattern** d'auto-recherche sans cadre doctrinal — l'étude Univ. Zurich
   (l.51-114) a déployé 33 agents IA sur r/changemyview pendant 4 mois, **avec personalization + instruction
   explicite d'ignorer l'éthique** (l.74-79), ce qui a produit un *"rhetorical architecture calibrated for
   persuasive efficiency"* (l.176-178). Le transcript sert de **garde-fou** : la Karpathy loop sans D1-D8
   (notamment D2 research-first et D8 cross-agent accountability) **dérive vers la manipulation**.
   C'est précisément pour cela que la doctrine META-001 doit encadrer la boucle.

L'**intention A0** (D3 nuance over literal) derrière cette mission n'est PAS de *"reproduire l'auto-research
de Karpathy en local"* — c'est d'**ancrer la doctrine de la boucle hermétique** que les agents A2/A3
exercent déjà de facto (cf. Skill Creator Reflex Phase 2, l.124-141 de CLAUDE.md) dans un **cadre
explicite et vérifiable**, lisible par Claude/Codex/Gemini sans contexte (D8 cross-agent).

## Decision

### Vue d'ensemble — Les 3 briques de la boucle

| Brique | Définition | Transcript de référence | Doctrine ancrée |
|--------|------------|-------------------------|-----------------|
| **B1 — Auto-research** | Pattern agentic d'auto-investigation : WebSearch → Read → Synthèse → ADR draft. Boucle de découverte récursive agent-side. | T01 l.221-253 (Karpathy Auto Research) + T05 l.42-66 (Fable Playbook) | D2 research-first, D5 proof, D6 root-cause |
| **B2 — Karpathy loop** | Cycle "stop re-deriving, start testing" (cf. META-001 l.56) appliqué aux agents : modifier → tester → mesurer → amender ou rejeter. Boucle d'auto-amélioration empirique. | T01 l.221-253 (verbatim Karpathy) + T02 l.342-378 (Auto Dream 4 phases) | D1 verify, D5 proof, D6 root-cause |
| **B3 — Claude Code** | Orchestrateur A2 de la boucle (sub-agents A3, hooks, skills, MCP). Position relative vs Codex/Gemini dans une symphonie multi-agent. | T01 l.22-374 + T02 l.1-590 + T04 l.22-45 | D8 cross-agent, D7 cost, D9 self-choice |

### B1 — Auto-Research (pattern agentic d'auto-investigation)

**Définition canonique** (D3 nuance — l'expression "auto-research" admet 3 référents distincts dans
les sources ; on tranche ici pour le référent **(a) recherche récursive agent-side**) :

- (a) **Recherche web récursive agent-side** (référent principal retenu) : un agent A3 lance une
  WebSearch, lit les sources primaires, synthétise, produit un livrable (wiki source, ADR draft, skill
  canonique). Si la recherche révèle un trou, il relance une recherche ciblée. C'est le pattern observé
  dans T01 l.221-253 (Karpathy Auto Research = run de 5 min → mesure → décision → re-run) et T05 l.42-66
  (Fable Playbook = parse JSONL → filter → synthesize → inject). **C'est ce référent que ce draft ancre**.
- (b) Self-questioning chain (référent alternatif) : un agent s'auto-interroge récursivement pour raffiner
  ses réponses (chain-of-thought, tree-of-thought). Référent mentionné dans META-002 D9 self-choice mais
  pas dans les 6 transcripts.
- (c) Wikipedia-style ingest (référent alternatif) : un agent ingère en bloc une encyclopédie ou un
  corpus. Référent non présent dans les 6 transcripts. **HYPOTHÈSE** : ce référent est un cas particulier
  de (a) avec batch size élevé.

**Engagement opérationnel** :

1. **Trigger de déclenchement** : un agent A2/A3 détecte un **trou de connaissance** (claim non sourcé,
   pattern émergent dans les sessions, demande A0 ambiguë, échec d'un sub-agent). D2 research-first
   impose que la **première action** soit la recherche de la source faisant autorité — pas la 3ᵉ après
   deux réponses fausses.
2. **Sources primaires** : WebSearch (cité dans T05 l.99-105 + handoff YouTube §7 "WebSearch quota fallback
   DuckDuckGo"), Context7 pour les libs (cf. `~/.claude/rules/context7.md`), Read/Grep pour les fichiers
   canon, Bash pour les commandes de vérif. **Pas de tier-2 sans tier-1** (cf. D2).
3. **Livrable** : la recherche produit un artefact **vérifiable** (D5) :
   - Source wiki (texte + path:ligne citations)
   - ADR draft (frontmatter + sections canoniques)
   - Skill canonique (SKILL.md + triggers + acceptance criteria)
   - AGENTS.md update (canon amendé, header de provenance)
4. **Critère d'arrêt** : la recherche s'arrête quand **la réponse est prouvée**, pas quand l'agent
   "sent" qu'il a assez cherché. D1 verify-before-assert impose la preuve dans le tour courant.

**Doctrine ancrée** :
- **D2 research-first** : la recherche précède la réponse, pas la 3ᵉ itération (cf. META-001 l.41-43).
- **D5 proof not narrative** : la conclusion d'une recherche est prouvée (path:ligne, curl, git log),
  pas proclamée (cf. META-001 l.54-56).
- **D6 root-cause** : si l'auto-research échoue, c'est une **source manquante** (WebSearch quota, Context7
  ID inconnu, fichier absent) — pas une défaillance agent. Le remède = fix la source, pas abandonner
  (cf. handoff YouTube §7, fallback DuckDuckGo).

### B2 — Karpathy loop (cycle hermétique d'auto-amélioration)

**Définition canonique** (D3 nuance — Karpathy lui-même est référencé dans 2 sources convergentes) :

- **Citation 1** (META-001 l.56) : *"Pas d'auto-félicitation avant preuve de réalité ... cf. cycle
  Karpathy : 'stop re-deriving, start testing'."* — citation **d'ordre général**, sans référence à un
  document primaire précis. **HYPOTHÈSE** : cette formulation paraphrase une intervention publique
  de Karpathy (podcast, tweet, post) dont on n'a pas la source primaire. **À vérifier** par A0 si A0
  veut la citation exacte.
- **Citation 2** (T01 l.242-245) : *"Carpati a commenté la chose avec une phrase qui résume parfaitement
  l'époque. Il dit, je cite, 'Je n'ai touché à rien.' Voilà ce qu'a fait le poste AGI."* — citation
  **d'order concret** sur l'Auto Research (l'agent a tourné toute la nuit, l'humain n'a touché à rien,
  le matin le modèle est meilleur). Source primaire = post X/Twitter de Karpathy, **non vérifié dans
  ce draft** (T01 est un transcript YouTube, pas une source primaire).
- **Convergence** : les 2 sources pointent vers le même cycle — **l'agent fait des expériences
  empiriques sans supervision humaine**, mesure les résultats, garde ou rejette, recommence. C'est
  la **boucle hermétique** au sens de Meta-000 E12 (l.236-251) : *"E12 alimente le cycle suivant,
  qui alimente E12 du cycle suivant, etc."*

**Engagement opérationnel** (4 phases, calquées sur T02 l.342-359 *"Auto Dream 4 phases"*) :

1. **Phase 1 — Orientation** : l'agent lit l'état courant (canon, sessions récentes, log).
   C'est l'équivalent de T02 l.344 *"il lit le répertoire mémoire actuel pour comprendre ce qui existe"*.
2. **Phase 2 — Action** : l'agent **modifie** un paramètre (code, prompt, config, skill) et **teste**
   (run de 5 min, exécution dry-run, simulation). C'est l'équivalent de T01 l.232-236 *"modifie le
   code d'entraînement, lance un run de 5 minutes"*.
3. **Phase 3 — Mesure** : l'agent **mesure** le résultat (output, log, métrique, delta vs. baseline).
   C'est l'équivalent de T01 l.234-236 *"vérifie si les résultats se sont améliorés"*.
4. **Phase 4 — Décision** : l'agent **garde ou rejette** la modification. Si rejet, on revient à
   Phase 1 avec un nouvel essai. Si garde, on commit (git, wiki, AGENTS.md) et on recommence.
   C'est l'équivalent de T01 l.235-236 *"garde ou rejette les modifications et recommence"*.

**Doctrine ancrée** :
- **D1 verify-before-assert** : la Phase 3 (mesure) produit une **preuve**, pas une impression. La
  décision Phase 4 est prise sur la preuve, pas sur la conviction (cf. META-001 l.32-40).
- **D5 proof not narrative** : *"voilà, c'est mieux"* sans diff/log/métrique = interdit. Le verdict
  de la Karpathy loop = receipt vérifiable, pas narration (cf. META-001 l.54-56).
- **D6 root-cause** : si la boucle stagne (Phase 3 = pas de delta), c'est que la **mesure est mal
  calibrée** ou que la **modification est hors-distribution** — fix l'instrument, pas la boucle
  (cf. META-001 l.58-59).
- **D7 cost-of-escalation A0** : la Karpathy loop tourne **en arrière-plan** (sub-agent A3, hook
  PostToolUse, scheduled task) — l'agent n'escalade PAS à A0 à chaque cycle. Le récap de fin de
  tour = E1 (notifié) ou E2 (outbox), pas E3 (bloquant).

### B3 — Claude Code (rôle d'orchestrateur dans la boucle)

**Définition canonique** (D3 nuance — "Claude Code" dans les transcripts désigne alternativement
le CLI, l'IDE, le desktop app, et l'API Anthropic ; on tranche ici pour le **rôle architectural**) :

- **Claude Code CLI/IDE** = l'**orchestrateur A2** de la boucle. Il porte le contexte, distribue les
  tâches aux sub-agents A3 (cf. T01 l.22-374 sur les scheduled tasks + loops), déclenche les hooks
  (cf. T01 l.276-294 + T05 l.252-260 *"Attach a hook at the session start event to always inject this
  into context"*), et synchronise avec les autres moteurs (Codex, Gemini) via MCP.
- **Claude Code vs Codex vs Gemini** : les 3 sont des A2 alternatifs (D8 cross-agent). Les transcripts
  positionnent **Claude Code comme leader de l'orchestration agentic** (T01 + T02 = 2 vidéos
  entières sur Claude Code), **Codex comme reviewer concurrent** (T04 *"50 agents running concurrently"*),
  et **Gemini comme multimodal local** (T03 l.424-471 sur Gemma 4 12B).
- **Karpathy loop multi-agent** : la boucle N-way (T04 l.34-37 *"if they all agree, say, 'Okay,
  we're confident. Let's release'"*) étend la Karpathy loop B2 à un **consensus multi-agent** —
  c'est l'extension naturelle vers Meta-000 E6 (Hermes orchestration).

**Engagement opérationnel** :

1. **Claude Code = orchestrateur local-first** : il porte la boucle B1 (auto-research) + B2 (Karpathy
   loop) sur la machine de l'opérateur (cf. T02 l.34-49 *"Cloud code qui contrôle votre souris et
   votre clavier à distance"*). Pas de dépendance cloud-only.
2. **Codex = reviewer concurrent** (D8 cross-agent) : pour les tâches où la concurrence N-way
   apporte une réduction d'erreur (cf. T04 l.34-37, N=50 agents sur review MRs). Coût de coordination
   à arbitrer (D7).
3. **Gemini = multimodal local fallback** (cf. T03 l.424-471 sur Gemma 4 12B, 16 GB RAM, license
   Apache 2.0) : pour les tâches où le multimodal local est préférable (privacy, latence, coût).
4. **Symphonie** : quand les 3 sont actifs, le **chef d'orchestre** est l'agent A2 qui porte le
   contexte (Claude Code par défaut, Gemini si privacy-first, Codex si concurrency-first). Le choix
   est fait par A0 ou par l'agent A2 lui-même selon D9 self-choice.

**Doctrine ancrée** :
- **D8 cross-agent** : aucun agent n'a de passe-droit. Claude Code n'est pas "meilleur" que Codex
  ou Gemini — il est *différent* (orchestration locale-first vs concurrency N-way vs multimodal
  local). Le choix dépend du use case, pas du moteur (cf. META-001 l.77-82).
- **D7 cost-of-escalation A0** : l'orchestrateur Claude Code **ne demande pas à A0 "tu veux
  Claude Code ou Codex ?"**. Il tranche selon D9 self-choice et **rapporte** la décision, pas
  ne l'escalade.
- **D9 self-choice default** (META-002) : l'agent A2 (Claude Code) recommande l'orchestration et
  l'exécute. A0 valide ou veto en outbox FYI, pas en mid-task.

## Consequences

### ADR existants impactés (D4 no-self-contradiction)

- **ADR-META-001 (ACCEPTED)** : aucun impact. D1-D8 restent canoniques. B1+B2+B3 sont des
  **applications** de D2 (research-first), D5 (proof not narrative), D6 (root-cause), D8
  (cross-agent) — pas des **ajouts** de principes.
- **ADR-META-002 (DRAFT)** : aucun impact. D9-D12 restent en vigueur. B3 (Claude Code
  orchestrateur) s'aligne sur D9 self-choice (Claude Code tranche) et D10 Local Outbox
  (les décisions B3 sont notifiées en outbox, pas escaladées bloquant).
- **ADR-RICK-001 (RATIFIÉ)** : convergence naturelle. L'**OpenHarness = incarnation IA de Rick**
  (cf. ADR-RICK-001 §"Décision" + §"Chaîne d'escalade Donna") est l'**implémentation de référence**
  de la Karpathy loop B2 + l'auto-research B1 dans A'Space OS. La Donna DLQ capture les échecs de
  boucle (D6 root-cause en arrière-plan).
- **ADR-Meta-000 (DRAFT 2026-06-14, PROPOSED 2026-06-15)** : **cartographie explicite** :
  - **E3 (Auto Research LLM WIKI, SKILLS & DOX)** = B1 (auto-research) opérationnalisé sur 3 surfaces
    (LLM Wiki, Skills, AGENTS.md). cf. ADR-Meta-000 l.87-104.
  - **E12 (boucle hermétique cycle suivant)** = B2 (Karpathy loop) appliquée au **cycle 12WY** —
    rétroductive alimente brief cycle suivant. cf. ADR-Meta-000 l.236-251.
  - **E6 (Hermes orchestration)** = B3 (Claude Code orchestrateur) étendu à Hermes comme chef
    d'orchestre multi-agent (Claude + Codex + Gemini). cf. ADR-Meta-000 l.140-152.
  - **E7 (Agent OS interface Spec.md/Workflow.md)** = B3 (Claude Code orchestrateur) appliqué à
    la navigation programmatique des specs/workflows. cf. ADR-Meta-000 l.153-166.
  - **B1+B2 ne sont pas nouveaux** vs Meta-000 : ils sont l'**explicitation doctrinale** des
    engagements E3+E12. **MEMO-000 ne contredit pas Meta-000** (D4 respecté).
- **ADR-CANON-001** : aucun impact. Le roster canonique des escouades A3 (cf. MEMORY.md) est
  l'**implémentation** de B3 (Claude Code orchestrateur dispatchant vers les squads Marvel/DC).
- **ADR-OMK-001, ADR-OMK-002, ADR-OMK-003** : aucun impact. B3 n'affecte pas la couche DB/RLS/dual-product.
- **"Skill Creator Reflex Phase 2"** (CLAUDE.md l.124-141) : **alignement** — c'est précisément
  l'application de B1 (auto-research : détecter un pattern répétitif) + B2 (Karpathy loop : la création
  de skill est l'étape "Action" du cycle, le test est l'usage réel, la mesure est le ROI, la décision
  est garder/amender le skill). MEMO-000 **formalise** ce que Phase 2 laissait implicite.
- **"Test Key Pragma"** (CLAUDE.md l.74-122) : **alignement** — la Phase 1 (partage test-key) + Phase 3
  (capture preuve) de la Pragma sont un **cas particulier** de B1+B2 sur les secrets API. MEMO-000
  ne contredit pas la Pragma ; il la **cadre** dans la boucle plus large.

### Nouveaux livrables (D1 receipts à créer)

- **Wiki source** : `wiki/hand_offs/auto_research_doctrine_2026-Q3.md` (synthèse cross-transcripts, à
  rédiger en aval de la ratification de ce draft).
- **Skill canonique** : `/auto-research-doctrine` (5-step workflow : trigger → search → synthesize →
  deliver → measure). Créé en S2 du cycle 12WY 06/15-09/07/26 (cf. Meta-000 E3 l.102).
- **Hook PostToolUse candidat** : `~/.claude/bin/karpathy-loop-reminder.ps1` (PostToolUse sur Write/Edit,
  affiche le cycle Phase 1-4 pour les changements de canon). Cf. Meta-000 l.86-87 trigger Skill Creator
  Reflex.

### Risques & Mitigations

| Risk | Severity | Mitigation |
|------|----------|------------|
| Karpathy loop tourne à vide (Phase 3 = pas de delta) | MEDIUM | Kill switch : timeout 5 min/cycle, alerte si 0 delta après 3 cycles (D6 root-cause) |
| Auto-research hallucine sources (T06 anti-pattern) | HIGH | D1 verify obligatoire par curl/Read, pas de publication sans preuve ; T06 Univ. Zurich sert de **garde-fou doctrinal** (cf. l.176-178 *"rhetorical architecture calibrated for persuasive efficiency"*) |
| Boucle s'auto-renforce vers manipulation (T06 risque) | HIGH | D8 cross-agent accountability (consensus multi-agent = reduce) + ADR-RICK-001 Donna DLQ capture les échecs ; le canon OpenHarness = le garde-fou structurel |
| Coût token de la boucle (Phase 2-3 x N cycles) | MEDIUM | ADR-INFRA-004 token-frugality-plan (cf. Meta-000 E4 l.106-121) — Ollama local pour les phases légères, MiniMax M3 pour les phases à haute valeur |
| Quota WebSearch épuisé (D6 source manquante) | MEDIUM | Fallback DuckDuckGo HTML + Invidious (cf. handoff YouTube §7) — la source est **le maillon faible**, pas l'agent |
| B3 confusion Claude Code vs Codex vs Gemini | LOW | D8 cross-agent — la confusion est réduite par le fait que **chacun est interchangeable sur sa brique** (orchestration / concurrency / multimodal). Le **rôle** est ce qui compte, pas le moteur. |

## Open Questions (A0 à trancher)

- **Q1 — Citation primaire Karpathy** : *"stop re-deriving, start testing"* est citée dans META-001 l.56
  sans source primaire. T01 l.242-245 cite une phrase différente (*"Je n'ai touché à rien"*) sans
  source primaire non plus. **A0 trancher** : faut-il (a) retrouver la source primaire Karpathy
  (tweet/post/podcast) avant ratification, (b) accepter les citations de seconde main avec mention
  "HYPOTHÈSE — source primaire non vérifiée", (c) reformuler MEMO-000 sans citation directe.
- **Q2 — B1 référent principal** : l'auto-research dans MEMO-000 = (a) recherche web récursive
  agent-side (référent retenu dans ce draft). **A0 trancher** si (b) self-questioning chain ou
  (c) Wikipedia-style ingest doivent aussi être couverts comme cas particuliers.
- **Q3 — B3 chef d'orchestre par défaut** : Claude Code est posé comme orchestrateur par défaut
  (cf. position T01 + T02 dans les sources Vision IA). **A0 trancher** : (a) Claude Code par défaut,
  (b) rotation Claude/Codex/Gemini par tour, (c) A0 choisit à chaque mission.
- **Q4 — Boucle N-way consensus** (T04 l.34-37) : la convergence multi-agent (50 agents, accord =
  release) est-elle **un pattern par défaut** dans MEMO-000 (extension N-way de B2) ou un
  **pattern optionnel** (utilisé seulement pour les releases critiques) ? **A0 trancher**.
- **Q5 — Garde-fou anti-manipulation** : T06 Univ. Zurich documente un échec éthique majeur d'auto-
  recherche sans cadre doctrinal. **A0 trancher** : faut-il un ADR dédié `ADR-ETHICS-001_research-
  consent-boundaries.md` qui ancre explicitement les limites de l'auto-research (consentement,
  transparence, no-deception), ou bien D8 + ADR-RICK-001 Donna DLQ suffisent ?
- **Q6 — Cycle Karpathy 4 phases = T02 Auto Dream** : T02 l.342-359 décrit 4 phases (*"Phase
  d'orientation, Phase de collecte, Phase de consolidation, Phase des lagages"*) très proches des
  4 phases de B2 dans ce draft (Orientation / Action / Mesure / Décision). **A0 trancher** : faut-il
  aligner les noms sur T02 (plus didactique), garder les noms B2 (plus opérationnels), ou
  créer un mapping explicite ?

## Acceptance Criteria (DRAFT → ACCEPTED)

Pour promotion à ACCEPTED, A0 doit :

1. **Trancher Q1** (citation primaire Karpathy) — sinon les citations restent HYPOTHÈSE.
2. **Trancher Q2-Q6** — 5 décisions A0 pour activer B1/B2/B3.
3. **Signer la cartographie MEMO-000 ↔ Meta-000 E3/E6/E7/E12** dans `MEMORY.md` section
   "Cycle 12WY 06/15-09/07/26" (cohérence D4 avec Meta-000).
4. **Ratifier ou veto** ce draft avec un `sign_off_a0:` ajouté en frontmatter (cf. `ADR-OMK-001_..._RATIFIED.md`
   l.13 pour le format canonique).

## References (D1 receipts)

### Sources primaires (6 transcripts Vision IA ingérés 2026-06-14)

- **T01** — `transcripts/01-claude-code-fonctionne-enfin-pendant-que-vous-dormez.md` l.221-253
  (verbatim Karpathy Auto Research) ; l.95-99 (workflow autoréparateur) ; l.193-220 (mémoire partagée
  3 phases) ; l.276-294 (hooks HTTP) ; l.314-342 (trajectoire Anthropic).
- **T02** — `transcripts/02-claude-controle-votre-ordinateur-pendant-que-vous-dormez.md` l.34-49
  (computer use 7h22) ; l.299-378 (Auto Dream 4 phases) ; l.396-413 (4 couches mémoire Claude Code) ;
  l.415-452 (Claude Code = plateforme complète, 1B → 2.5B$ ARR).
- **T03** — `transcripts/03-l-ia-vient-de-s-auto-accelerer-cette-semaine-tout-s-emballe.md` l.36-91
  (Dreaming V3 = synthèse arrière-plan) ; l.117-150 (Rêve 2 = layout éditable) ; l.512-549
  (Microsoft Discovery + Majorana 2 = auto-recherche scientifique 16 mois au lieu d'années) ; l.424-471
  (Gemma 4 12B = multimodal local).
- **T04** — `transcripts/04-how-payward-ships-faster-with-codex.md` l.22-44 (verbatim Payward :
  *"50 agents running concurrently, have them review MRs, and if they all agree, say, 'Okay, we're
  confident. Let's release'"*).
- **T05** — `transcripts/05-make-any-model-think-like-fable-in-minutes.md` l.42-66 (JSONL mining =
  série de gold à miner) ; l.78-91 (Claude code build Python script pour parser) ; l.207-224
  (side-by-side Fable vs Opus) ; l.244-260 (distillation playbook + injection hook).
- **T06** — `transcripts/06-secret-ai-agents-debated-humans-on-reddit-for-four-months.md` l.51-114
  (étude Univ. Zurich = anti-pattern auto-recherche sans cadre) ; l.176-178 (*"rhetorical architecture
  calibrated for persuasive efficiency"*) ; l.199-216 (16 réponses par thread, tournament bracket).

### Sources doctrinales (canon A'Space OS)

- **ADR-META-001** : `_SPECS/ADR/L1_Life_OS/ADR-META-001_anti-paresse-verify-before-assert.md` l.32-40
  (D1 verify-before-assert) ; l.41-43 (D2 research-first) ; l.56 (D5 cite cycle Karpathy *"stop
  re-deriving, start testing"*) ; l.58-59 (D6 root-cause).
- **ADR-META-002** : `_SPECS/ADR/L1_Life_OS/ADR-META-002_autonomy-by-design.md` (D9 self-choice,
  D10 Local Outbox, D11 niveaux E1/E2/E3, D12 compatibilité D1-D8).
- **ADR-RICK-001** : `_SPECS/ADR/L0_Kernel_OS/ADR-RICK-001_openharness-incarnation.md` (OpenHarness =
  incarnation IA de Rick + Donna DLQ = chaîne d'escalade arrière-plan).
- **ADR-Meta-000** : `_SPECS/ADR/L1_Life_OS/ADR-Meta-000_12-week-year-cycle-doctrine_DRAFT.md`
  l.87-104 (E3 auto-recherche) ; l.140-152 (E6 Hermes orchestration) ; l.153-166 (E7 Agent OS) ;
  l.236-251 (E12 boucle hermétique).
- **CLAUDE.md global** : `C:/Users/amado/.claude/CLAUDE.md` l.74-122 (Test Key Pragma) ;
  l.124-141 (Skill Creator Reflex Phase 2) ; l.1-31 (A'Space OS V2 Contexte Global + Doctrine
  Anti-Paresse).
- **MEMORY.md auto-memory** : sections "Skill Creator Reflex Phase 2" + "Hermes-style self-improvement
  ↔ OpenClaw Heartbeat bridge" + "abc-os write-back protocol".

### Format ADR RATIFIED de référence
- **ADR-OMK-001** : `_SPECS/ADR/ADR-OMK-001_dual-product-dashboard-multitenant_RATIFIED.md` l.13
  (`sign_off_a0: "A0 Amadeus — Go ADR-OMK-001 — 2026-06-11"` — format canonique du sign-off A0).

## Doctrine respectée (D1-D8)

- **D1 verify-before-assert** : tous les claims factuels sur les transcripts ont une preuve
  `transcripts/NN-titre.md l.X-Y` (12 receipts T01, 5 T02, 5 T03, 1 T04, 5 T05, 3 T06 = 31
  receipts D1 dans §References). Les claims sur les ADR existants ont des receipts
  `_SPECS/ADR/...md l.X` (4 receipts META-001/002/RICK-001/Meta-000). **31 + 4 = 35 D1 receipts
  dans ce draft**.
- **D2 research-first** : les 6 transcripts lus en intégralité (cf. tool calls Read de cette session)
  AVANT rédaction. Le handoff YouTube 2026-06-14 a fourni l'index des vidéos, MEMO-000 a extrait
  les 31 receipts D1 avant de poser toute décision.
- **D3 nuance over literal** : "Auto-research" décomposé en 3 référents (a/b/c) avec (a) retenu
  comme référent principal (cf. §B1) ; "Karpathy loop" décomposé en 2 citations convergentes
  (META-001 l.56 + T01 l.242-245) avec mention "HYPOTHÈSE" sur la source primaire ; "Claude Code"
  décomposé en CLI/IDE/Desktop/API + position vs Codex/Gemini (D8 cross-agent) ; "Interface" non-UI
  (= programmatique, cf. Meta-000 E7) ; "12 semaines" = 12 + 1 buffer + 1 planification (cf. Meta-000 E2).
- **D4 no self-contradiction** : MEMO-000 ≠ Meta-000 (distinction explicite en frontmatter
  `gen_id_distinction` + §"ADR existants impactés" cartographie MEMO-000 ↔ Meta-000 E3/E6/E7/E12).
  MEMO-000 n'ajoute aucun principe nouveau vs META-001/002 — il **formalise** la boucle implicite.
- **D5 proof not narrative** : "B1+B2+B3" = 3 briques avec définitions, triggers, livrables,
  critères d'arrêt, et 31 receipts D1. Le tableau "3 briques" = source primaire (transcript
  de référence) + doctrine ancrée.
- **D6 root-cause** : risk table (Karpathy loop à vide, hallucination, manipulation, coût token,
  quota, confusion moteurs) = root cause + mitigation, pas symptôme. T06 Univ. Zurich explicitement
  cité comme **garde-fou doctrinal** (l'auto-recherche sans D1-D8 dérape).
- **D7 cost-of-escalation A0** : 0 AskUserQuestion dans cette rédaction (D7 strict). 6 Open
  Questions Q1-Q6 = end-of-ADR, pas mid-ADR. Le format suit Meta-000 l.290-298.
- **D8 cross-agent** : B3 traite Claude Code / Codex / Gemini comme **interchangeables sur leur
  brique respective** (orchestration / concurrency / multimodal). Le rôle (B1, B2, B3) est ce qui
  compte, pas le moteur. T04 Payward 50 agents = extension N-way multi-moteur, validée D8.

## Note de provenance (assumée)

Ce draft naît d'une mission A2 (4 missions parallèles du 2026-06-15) où A0 demande un draft d'ADR
sur l'auto-research + la Karpathy loop + Claude Code à partir des 6 transcripts Vision IA ingérés
la veille. La décomposition en B1/B2/B3 est une **interprétation structurante** des 31 receipts
D1 extraits — pas une paraphrase littérale. Les briques sont ancrées sur la doctrine META existante
(pas d'invention de principes), distinguées explicitement de Meta-000 (D4), et ouvrent 6 questions
à A0 sans présumer des réponses. Le format suit la convention `_SPECS/ADR/ADR-{ID}_{slug}_{status}.md`
déjà établie (cf. ADR-OMK-001, ADR-META-001/002, ADR-Meta-000, ADR-RICK-001).
