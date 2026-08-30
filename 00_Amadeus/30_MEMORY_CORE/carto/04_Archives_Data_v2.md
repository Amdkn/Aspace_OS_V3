# Cartographie profonde du seau `04_Archives_Data` — VAGUE 2

> **Seau** : `04_Archives_Data` — A3 Data · Parent `A2_COMPUTER_ENTERPRISE_PARA` · PARA domain Archives · Status SHADOW_ACTIVE
> **Wave 2 — 2026-08-13** · Suite vague 1 (30 fichiers lus) · Cette vague : **90 fichiers additionnels lus**, dont 80 ADR/sisters canoniques + 5 manifestes/spéciaux
> **Total lu vague 1+2 = 120 fichiers** sur 1534 chemins disponibles · 1414 écartés (contenu feuille, snapshots, configs)
> **Jonctions NTFS** : 0 rencontrées (les fichiers sont sous `_V3_STRUCTURE_2026-08-02` archivés, pas de symlinks)

---

## 1 · Types d'objets (la matière de l'ontologie)

### Tableau trié par nombre de chemins

| Type | Chemins | Attributs canoniques |
|------|---------|---------------------|
| **ADR (Architectural Decision Record)** | **60+ chemins** | `id`, `title`, `type`, `status` (PROPOSED/ACCEPTED/RATIFIED/RADIÉ/DRAFT/AMENDED), `date`, `deciders[]`, `proposed_by`, `domain`, `tags[]`, `doctrine_anchors[]`, `related[]`, `provenance`, `sign_off_a0`, `ratification_log`, `sources_canons[]` (souvent 5-30) |
| **Manifesto (Couche kernel)** | 4 chemins (00/10/20/30) | `Guardian` (A0/Rick/Beth & Morty/Jerry), `Scope` |
| **README.md (handoff A2-ship)** | 6 chemins (1 par A2 ship + racine) | `layer`, `a2_ship`, `framework`, `shadow_tool`, `gatekeepers`, `status`, `mission`, `resume_protocol`, `crew_map`, `a3_rule`, `outputs`, `handoff_rules`, `evidence`, `context7_boundary`, `alignement_plan_fancy-hugging-bengio` |
| **Spec.md (A2/A3 ship canon)** | 3 chemins | `id`, `layer`, `role`, `framework`, `shadow_tool`, `gatekeepers`, `status`, `created`, `identity`, `responsibilities`, `inputs`, `outputs (YAML)`, `crew`, `a3_findings_contract`, `evidence_index`, `acceptance_criteria`, `context7_boundary` |
| **A2 Ship Spec** | 6 chemins (Computer/Curie/Discovery/Holo Deck/Holo Janeway/Orville) | `a2`, `framework`, `shadow_tool`, `gatekeepers (beth/morty)`, `status (SHADOW_ACTIVE)`, `created (2026-05-20)`, `ship`, `a2`, `crew (5-9 noms)`, `outputs YAML` |
| **A3 Crew Spec** | 9+ chemins (Dal/RokTahk/Zero/Gwyn + 5 Cerritos) | `id`, `name`, `role`, `ship (parent A2)`, `responsibility`, `output_canon` |
| **A1 Gatekeeper Spec** | 2 chemins (Beth/Morty) | `id (L1_A1_Beth / L1_A1_Morty)`, `layer`, `role` (Gatekeeper/Conscience/Terminal Executor), `status (SHADOW_ACTIVE)`, `created (2026-05-20)`, `decision_states (5 chez Beth : GREEN/ORANGE/RED/HALT_LD03/HALT_LD04)`, `routing_matrix (Morty)`, `anti_patterns[]` |
| **AaaS Variant** | 4 (3 actifs + 1 dormant) | `a3_captain`, `ldxx[]`, `b2_primary[]`, `b3_lead`, `horizon (H90/H3/H10/TBD)`, `objectif_canonique`, `statut_q3_2026`, `livrable_canon` |
| **B1 Direction Cockpit** | 4-5 chemins | `00_B1_DIRECTION_INDEX.md`, `01_NORTH_STAR_1Y_3Y_10Y.md`, `02_12WY_COMMAND_CYCLES.md`, `03_DECISION_CHARTER.md`, `04_B2_HANDOFF_QUEUE.md`, `05_B2_DEFINITION_OF_DONE_SPEC.md`, `06_B3_JOBS_TO_BE_DONE_SPEC.md` |
| **B2 Domain Control Room** | canon en 3 artefacts | `00_B2_DOMAIN_CONTROL_ROOM.md` (mission/responsibility/anti-patterns), `01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md`, `02_B3_SWARM_SUPERVISION_PROTOCOL.md` |
| **B3 Squad Swarm Config** | canon en 4 artefacts | `00_B3_SWARM_CONFIG.md`, `01_B3_AGENT_ROSTER.md`, `02_PEER_UNBLOCKING_AND_HANDOFFS.md`, `03_SHARED_CONTEXT_AND_PROOF_LOG.md` |
| **Squad (B3 Marvel/DC)** | 8 chemins | `squad_name`, `b2_domain`, `b2_owner (DC Manager)`, `lead (1er membre)`, `members[]` (5-7), `task_surface[]`, `build_gates[]`, `anti_patterns[]`, `escalation_rule` |
| **B2 Domain** | 8 chemins (01-08 préfix) | `manager_archetype (DC: Superman/MartianManhunter/Flash/Batman/Cyborg/WonderWoman/GreenLantern/Aquaman)`, `squad_name`, `lead`, `build_gates_order (8 obligatoires)`, `book_linked (LDxx mapping)` |
| **Loop (Citadel WF)** | 5+ chemins (wf0-spock/wf1-morty/wf2-book/wf3-mirofish/w-star) | `loop_id`, `contract_path (domains/<loop>/README.md)`, `artifacts_io (signals/tasks/tickets/docs)`, `cadence`, `enable_flag (citadel/decisions/enable_<loop>.flag)` |
| **Constante TEMPORAL-CANON** | 1 chemin canon | `nom (GO/compression CAP/cadence/banque/Fable/RAM airlock/tokens plan)`, `valeur`, `receipt (wargame_id + move_id)` |
| **Wargame (Move)** | 3+ chemins | `wargame_id`, `move_id`, `claim`, `d1_receipt`, `abort_condition`, `red_team_pass`, `self_grade` |
| **Symphony Spec** | 4+ chemins (obsidian/affine/baserow/plane) | `tool`, `shadow_lane (A/B)`, `index_ref` |
| **Context Pack (A1 Morty output)** | canon en schema | `ship`, `crew_member`, `next_action`, `framework`, `domain_impact`, `l0_skill_required`, `beth_clearance`, `evidence_paths`, `output_artifact` |
| **Manifest (de projet/domaine)** | 2+ chemins | `id`, `layer`, `role`, `parent_a2`, `classification`, `status`, `created`, `next_owner`, `cycle`, `parent_jerry`, `picard_status` |
| **state.json (bus sémantique)** | 5+ chemins canon | `$schema (state-bus.v1)`, `status (INIT/ACTIVE/DRAINED)`, `created`, `updated`, `agent_id`, `session_id`, `cycle (Q3-2026)`, `week (W1)`, `stage (captured/clarified/organized/reviewed/engaged)`, `agent_path`, `para_bucket`, `12wy_discipline`, `life_wheel_domain`, `raw_input_hash`, `raw_input_preview`, `next_step`, `tokens_used`, `tokens_budget`, `drift_flag`, `extra`, `metadata` |
| **Loop contract** | 5+ chemins | `loop_id`, `contract_scope`, `worklog_format`, `enable_flag_path` |
| **Artifact signal/task/ticket/doc** | 4 dossiers canon | signal (slug + OKF frontmatter + append-only), task (item pioché + preuve obligatoire), ticket, doc |
| **Build Gate** | 2+ chemins canon | `name`, `threshold`, `scope (B2/B3)`, `measurement_source` |
| **Doctrine Anchor (ADR)** | 1 canon (INDEX) | `anchor_id (ADR-id référencé)`, `anchor_kind (mandatory/sister/implicit)`, 100% coverage sur 29 ADR |
| **Hard-stop trigger (anti-paperclip)** | 1 canon (SOBER-002) | `trigger_id`, `condition`, `response_action`, `owner (A1 Rick veto kernel structurel)` — 7 triggers |
| **Schema Supabase (multitenant)** | 1 canon (REGISTRY) | `tenant`, `hosting (Cloud/self-host)`, `ADR_ratification`, `statut`, `tables_count`, `rls (oui/non)` |
| **Squad (Ikigai 4 Pillars + 5 Horizons)** | 3+ chemins | `crew_name (Ed/Kelly/Gordon/Claire + Isaac/Lamarr/Bortus/Alara/Klyden)`, `pillar (Profession/Mission/Passion/Vocation)` ou `horizon (H1/H3/H10/H30/H90)` |
| **Squad (12WY 5 disciples)** | 5+ chemins | `crew_name (Pike/Una/M'Benga/Chapel/Ortegas)`, `discipline (Vision/Planning/Focus/Metrics/Execution)` |
| **Squad (DEAL Muse 4 stages)** | 5+ chemins | `crew_name (Dal/Rok-Tahk/Zero/Gwyn)`, `stage (Define/Eliminate/Automate/Liberate)`, `output_canon (pattern_definition/elimination_proposal/skill_<name>/d11_score.json)` |
| **Squad (GTD 5 stages)** | 5+ chemins | `crew_name (Mariner/Boimler/Rutherford/Tendi/Freeman)`, `stage (Capture/Clarify/Organize/Review/Engage)` |
| **Squad (Life Wheel 8 LDxx)** | 8+ chemins | `crew_name (Book/Saru/Culber/Tilly/Stamets/Burnham/Reno/Georgiou)`, `ldxx (LD01..LD08)`, `horizon_canon (H1/H3/H10/H30)` |
| **Spec legacy (V0.3.5)** | 4 chemins (TOTAL_Spec) | `version (V0.3.5)`, `status (PROPOSED)`, `date (2026-03-16 typique)` |
| **Roadmap (DEAL 12WY)** | 1 canon | `north_star`, `cycles[] (12WY-01..12WY-04)`, `rocks_per_cycle (3)`, `sprints_per_month (4)`, `scrums_per_sprint (5)`, `regle_unique (chaque niveau ne remonte que du chiffré)` |
| **Reference Index (A3)** | 7+ chemins | `claim`, `evidence_path`, `lines/note` |
| **Schema SQL (Master)** | 2+ chemins | `canon SQL`, `tables[]`, `RLS` |
| **ICP Persona (AaaS)** | 4 piliers (Solaris/Nexus/Orbiter) | `persona archétype`, `mantra doctrinal`, `marché cible`, `3-ICP sister`, `killer feature` |
| **ICP Persona (Nexus sub-types)** | 5 sub-types (Expert-comptable/Avocat/Family-Office/Coach/Cabinet-médical) | `age`, `localisation`, `CA`, `pricing`, `stack technique`, `trauma fondateur` |
| **Project Gate (B2 sector)** | 7 sisters (Batman/Flash/Superman/JohnJones/WonderWoman/Aquaman/GreenLantern) | `sister_gates_siblings`, `vocabulaire_canon` (F4, tier, ops_review, ops_quality, privacy, D7_posture), `ops_quality` (SIGNED co-signé) |
| **JTBD ICP** | 1+ chemin (JTBD-ICP-SOLARIS-001 sister scope) | `jobs`, `pains`, `objections`, `verbatim` |
| **Pipeline canonique (CEO-Bench + SpecLoop)** | 1 chemin (INTEGRATION_CEOBENCH_SPECLOOP.md) | 11 composants CEO-Bench (memory_*.md, memos if-then, forecast cash, 19 tables SQL, equation cash, budget acquisition, spending cible, 8 categories, detection concurrent, turns/semaine, monde non-stationnaire) + 7 composants SpecLoop (3 roles, information hiding, taxonomie E.1-E.4, contre-exemple, format spec, budget retry) |
| **Wargame Lens (B2)** | 8 chemins (handoff_wargame_wf2_b2_<sector>_lens_2026-07-06.md) | `sector`, `angles_morts (8)`, `AI-Act driver (oui/non)`, `d1_receipts` |
| **Wargame Synthesis (B1)** | 2 chemins (handoff_wargame_wf2_b1_<persona>_lens_2026-07-06.md) | `82 angles morts`, `15 ADR candidates`, `2 gaps structurels (CC-1/CC-2)` |
| **AaaS Doctrinal Sister** | 8 chemins (Operations/Finance/IT/IT-EXT/Content/Pricing/Acquisition/Market Study) | `pilier 1-5 (ou 6)`, `a3_twins_mapping`, `source guide`, `sisters canon`, `provenance`, `consequences` |
| **D11 Lead/Lag Metric** | 2 chemins canon | `LEAD (prédictive)`, `LAG (confirmation)`, `SKIPPED honnête (refus sans source canon)` |
| **Hook PreToolUse destructif guard** | 1 ADR (META-005) | `matcher (Bash)`, `trigger (pattern)`, `action (exit code 2)`, `allow-list (paths sous _TRASH/)` |
| **PostToolUse D1 logger** | 1 ADR (META-005) | `matcher (Bash|Edit|Write)`, `trigger (after success)`, `action (append JSON wiki/log.md)` |
| **SubAgentStart tracker** | 1 ADR (META-005) | `matcher (none)`, `trigger (spawn sub-agent)`, `action (append JSONL agent_runs_<date>.jsonl)` |
| **SubAgentStop cleanup** | 1 ADR (META-005) | `matcher (none)`, `trigger (sub-agent termine)`, `action (cleanup _TRASH/<date>_<agent>/* + unset TEMP_<AGENT>_* env)` |
| **Validation Contract** | 1 ADR (LIFE-013) | `input`, `output`, `risk`, `rollback`, `criteria (5+ assertions par feature)` |
| **MANIFEST.md Picard** | 1+ canon (INFRA-003 §D1 amended) | `id`, `title`, `ldxx_mirror`, `a3_anchor`, `status`, `aaaS_variant`, `cycle`, `rock_count` |
| **AaaS Variant Pricing Tier** | 5 tiers (PRICING-001) | `tier (1-5)`, `sister canon`, `prix (USD post-accuponcture)`, `volume attendu`, `conversion` |
| **AI-Act Project-Gate (pré-Aug-2)** | 1 ADR (AIACT-DEADLINE-001) | 5 livrables obligatoires : Risk Classification (Art. 9), Human Review (Art. 14), Accuracy Benchmark (Art. 15), Datasheet (Art. 13), Transparency |
| **Persona Landing (Marcus/Harrison/David)** | 5 personas (3 prioritaires + 2 listes PRD §4) | `strate (A/B/C)`, `tagline`, `friction_pivot` |
| **10 ICP Nexus (3 strates)** | 10 catégories (A1-A3 coaching, B1-B3 growth, C1-C4 conseil) | `douleur (D3 nuance)`, `angle franchise-first`, `variant canon`, `tier pricing` |

---

## 2 · Relations (la partie qui compte — citation à l'appui)

> **Doctrine** : chaque relation est annotée avec la phrase verbatim du fichier. Pas de paraphrase.

### 2.1 — Imbrication des couches (les 4 poupées russes)

**DEAL ⊂ PARA ⊂ 12WY ⊃ PARA ⊃ DEAL** :
> "Loi d'imbrication (plan §3.1) : DEAL ⊂ PARA ⊂ 12WY"
— `20_Life_OS/24_PARA_Enterprise/A2_Computer_Enterprise_Spec.md` lignes 90-98

**Ikigai ⊃ Life Wheel ⊃ Muse** :
> "Russian-doll 12WY⊃PARA⊃DEAL / Ikigai⊃LifeWheel⊃Muse"
— `ADR-L2-A2B2-MAP-001` (fancy-hugging-bengio §3.1)

### 2.2 — Cascade A0/A1/A2/A3 (gouvernance)

**A0 Amadeus = méta-coach, Vision H30, Gouverneur ON-not-IN (E-Myth)** :
> "A0 = Vision H30, gouvernance ON-not-IN (E-Myth). A0 ne fait pas le travail A1/A2/A3 — A0 trace la route, rate les décisions, dérive les sub-agents, et surveille que le paperclip Ultron ne pousse pas"
— `_root_and_shells_2026-08-02/ASpace_OS_V3-DOCTRINE-ORCHESTRATION.md` §5 ligne 100

**A1 Beth + Morty distribués sur 6 A2 engines** :
> "Routing distribué sur 6 ships : Morty route vers les 6 A2 engines selon la matrice de routage canon"
— `20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Morty_Spec.md` ligne 115

> "Veto distribué sur 6 ships : Beth supervise les 6 A2 engines"
— `20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Beth_Spec.md` ligne 100

### 2.3 — Cadre anti-paperclip (Musk comme anti-modèle)

**A1 Rick = veto kernel structurel (1×/an max + 7 hard-stop triggers)** :
> "A1 Rick (Sobriété Kernel) est le seul A1 Gatekeeper avec veto absolu sur les 6 A2 engines (Ikigai / Life Wheel / DEAL / 12WY / PARA / GTD) et les 35 A3 twins. Activation : Mode normal : Rick est dormant… Mode alerte : Rick se réveille si 1 des 7 hard-stop triggers est détecté"
— `ADR-SOBER-002` §D2

**Saru 1000T = production de valeur réelle Kardashev Type 3, pas valorisation financiarisée découplée Musk-style** :
> "L'objectif canonique Saru 1000T (A3 LD02 Finance, AaaS Solaris + Nexus) est donc production de valeur réelle Kardashev Type 3, pas valorisation financiarisée découplée Musk-style"
— `_SPECS/ADR/L2_Business_OS/ADR-L2-AAAS-001_…md` §C4 ligne 62

### 2.4 — Anti-Paperclip en 3 couches (canon explicite)

> "Trois couches d'anti-paperclip : 1. superpowers (A2) : documente et idempotentise les freelances ; 2. GSD (A3/B3) : orchestration visionnaire Type 1 — chaque task a un Definition of Done + un gate de sortie vérifiable ; 3. Fable + Wargames + CEO-Bench (qualité) : validation move-by-move avant tout déploiement"
— `_root_and_shells_2026-08-02/ASpace_OS_V3-DOCTRINE-ORCHESTRATION.md` §3 ligne 72

### 2.5 — Asymétrie corrigibilité (W28)

> "les kill-switches sont autonomes pour ARRÊTER (B1-Mirofish gate) mais humain-gated pour SE LEVER (M5 Remote Pane / Telegram). Un off-switch auto-release = le paperclip Ultron"
— `_root_and_shells_2026-08-02/ASpace_OS_V3-DOCTRINE-ORCHESTRATION.md` §3 ligne 80

### 2.6 — AaaS Doctrine 3 Variants × 4 Leviers Solarpunk

> "OMK = une seule ligne produit à 3 étages de maturité, pas 3 produits parallèles ni une matrice 3×3 : P1 — OMK BOS (le Harness d'exécution L2, INTERNE)… P2 — OMK Meta Factory (le White-Label, EXTERNE)… P3 — OMK R&D Souverain (la frontière)"
— `ADR-OMK-PRODUCTS-001` §D1

### 2.7 — Mapping 5 domaines AaaS × 3 ICP Strates

> "AaaS Sisters Doctrine = 3 ICP distincts alignés sur 3 positionnements marché : Solaris 🎨 Visual First / DAM, Nexus �️ Data First / Conformité, Orbiter 🏗️ Mobile First / Terrain"
— `ADR-ICP-NEXUS-001` Pilier 4 / `ADR-ICP-SOLARIS-001` Pilier 4

### 2.8 — AaaS 5 Tiers Pricing Canon USD post-accuponcture

> "5 Tiers AaaS Canon : T1 PME Solo Founder $300-500/an, T2 PME Solo Standard $500-1000/an, T3 PME Groupe $4000-5000/an, T4 Nexus mid-market $15K MRR = $180K ARR, T5 Orbiter Enterprise $50K MRR → $500K Year 10"
— `ADR-AAAS-PRICING-001`

### 2.9 — Kill-switch anti-paperclip (asymétrie corrigibilité)

> "Les kill-switches sont autonomes pour ARRÊTER (B1-Mirofish gate) mais humain-gated pour SE LEVER (M5 Remote Pane / Telegram). Un off-switch auto-release = le paperclip Ultron"
— `_root_and_shells_2026-08-02/ASpace_OS_V3-DOCTRINE-ORCHESTRATION.md` §3 ligne 80

### 2.10 — Bus sémantique state.json + verrou atomique

> "Lock atomique : state_writer.py retry 3× (backoff 100/300/900ms) si .state.lock existe. Garde-fou : state.json > 10 KB → rotation state.json.prev"
— `00_Amadeus/40_SYMPHONY_BUS/SCHEMA.md` §Loi lock atomique ligne 48

### 2.11 — Mission Control = wiki/hand_offs + log + outbox (cockpit A0)

> "Le cockpit A0 canon = `wiki/hand_offs/` (active missions) + `wiki/log.md` (live ticker) + outbox E2 (decision notifications)"
— `ADR-LIFE-015`

### 2.12 — Workflow Orchestration Topologies (4 pures)

> "4 topologies pures, mappées 1-1 à des use cases, routées par A1, auditables D1-D8 : A Hierarchical (canon actuel), B Swarm (Fable 4-step loop), C Mesh, D Pipeline-by-Design"
— `L0_Kernel_OS/ADR-WORKFLOW-001` §2

### 2.13 — Cerritos (A2 Holo Deck) = bus horizontal bouclant 2 triptyques

> "GTD (Cerritos Holodeck) = bus horizontal qui boucle les 2 triptyques (MORTY 12WY⊃PARA�DEAL + BETH Ikigai⊃Life Wheel⊃Muse) vers B1 Fractal"
— `20_Life_OS/25_GTD_Cerritos/A2_HoloDeck_Cerritos_Spec.md` §Anchor canon ligne 87

### 2.14 — Picard � Spock ↔ Geordi ↔ Data (A3 twins canoniques)

> "Computer is A2, not Picard; Picard is A3 Projects. … Picard checks active Projects and Rock linkage. Spock checks Areas, standards, and ongoing responsibilities. Geordi checks reusable Resources and context-pack value. Data checks archive readiness and documentation-before-archive"
— `20_Life_OS/24_PARA_Enterprise/A2_Computer_Enterprise_Spec.md` §A3 Findings Contract lignes 60-66

### 2.15 — Cerritos Crew canon (Mariner/Boimler/Rutherford/Tendi/Freeman)

> "5 A3 Cerritos canon : Mariner (Capture), Boimler (Clarify), Rutherford (Organize), Tendi (Review), Freeman (Engage)"
— `20_Life_OS/25_GTD_Cerritos/README.md` ligne 70

> "Tendi = canon twin protostar (fancy-hugging §15.1). Le terrain canon local garde Rutherford = Organize (résolu 2026-05-20, canon actif)"
— `20_Life_OS/25_GTD_Cerritos/README.md` §Matrice canon ligne 74

### 2.16 — Curie SNW (12WY 5 disciplines)

> "Curie aboard USS Strange New Worlds is the A2 manager of 12WY execution. Curie converts cleared Life OS direction into quarterly Rocks, weekly tactics, and measurable progress without letting the system become a generic to-do list"
— `20_Life_OS/23_12WY_SNW/A2_Curie_SNW_Spec.md` l.14-19

### 2.17 — Picard H10 + MANIFEST.md obligatoire (INFRA-003 amendé 2026-06-21)

> "Chaque projet dans `10_Projects/<proj>/` est ancré canoniquement sur LD01_Business_Picard comme A3 captain USS Enterprise (PARA ship) avec : Horizon canonique : H10, Rôle canonique : projects owner, MANIFEST.md obligatoire par projet dans `<proj>/MANIFEST.md`"
— `ADR-INFRA-003` §D1 amended 2026-06-21

### 2.18 — Workflow Morty (WF0→WF3 + Unique GO)

> "UN clic humain reste : A+ pose `citadel/decisions/GO_SPOCK_UNIQUE.md`. L'airlock vérifie GREEN ×2 (hystérésis) puis cascade `enable_wf0/wf1/wf3/ship_internal.flag`. Révocation = supprimer le fichier"
— `ADR-L1-WF-001` §D2

### 2.19 — Squads Marvel/DC 8 B2 (canon Notion)

> "8 sectors SOA01-SOA08 + Marvel/DC Nano Squads (People=X-Men, IT=Kang Dynasty, Ops=F4, Product=Avengers, Growth=Guardians, Finance=Thunderbolts, Legal=Eternals)"
— `ADR-AGENTIC-001` §D2

### 2.20 — D11 bandwidth metric (Gwyn output DEAL Muse)

> "D11 bandwidth metric = output Gwyn : gain bande passante cognitive (minutes libérées/semaine) vs maintenance tax (minutes upkeep/semaine). Upkeep > gain → route back to Zero/Rok-Tahk"
— `20_Life_OS/26_DEAL_Protostar/README.md` §Karpathy loop ligne 101

### 2.21 — Life Wheel 8 LDxx (8 domaines)

> "LD01_Business_Picard (H10 sprint, projects owner), LD02_Finance_Saru (H3 quarterly runway review, finance officer), LD03_Health_Culber (H10 10-week health cycle)… LD08_Impact_Georgiou (H90 quarterly legacy review, 30-year arc)"
— `ADR-MEM-002` §D1

### 2.22 — B1 7 artefacts obligatoires (Direction Cockpit)

> "B1 must exist as a direction cockpit before B2 can responsibly define domain Rocks… 7 artefacts : 00_B1_DIRECTION_INDEX, 01_NORTH_STAR_1Y_3Y_10Y, 02_12WY_COMMAND_CYCLES, 03_DECISION_CHARTER, 04_B2_HANDOFF_QUEUE, 05_B2_DEFINITION_OF_DONE_SPEC, 06_B3_JOBS_TO_BE_DONE_SPEC"
— `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §Non-Negotiables

### 2.23 — B2 Gate Matrix (8 obligatoires, ordre canonique)

> "Required gate order: 1. Product proves user value. 2. Ops proves repeatable delivery. 3. IT proves runtime, access, deployment, and backup boundaries. 4. Finance proves cost, price, and margin logic. 5. Legal proves claims, privacy, IP, and terms boundaries. 6. Sales proves qualification, objections, and handoff. 7. Growth proves ICP, message, channel, and measurement. 8. People proves ownership, training, handoff, and load"
— `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §B2 Gate Matrix

### 2.24 — B3 swarm collaboration (peer-first, B2 conductor)

> "B3 swarms collaborate as peers. A blocked B3 should first ask one member of the same squad to challenge the blocker and propose a workaround. B2 intervenes only when the DoD is ambiguous, the input does not exist, a cross-domain gate is touched, acceptance risk changes, or delegated authority is exceeded"
— `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §B3 Squad Swarm Configurations ligne 86

### 2.25 — B2 is conductor, not babysitter

> "B2 is a conductor, not a babysitter. It translates B1 vision into bounded goals, guardrails, and proof requirements"
— `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §B2 Swarm Supervision Rooms ligne 72

### 2.26 — Hosting pivot 2026-06-19 (self-host → Cloud 3-orgs)

> "Hosting pivot 2026-06-19 : OMK Services Org (Cloud) + ABC-OS-COMMUNITY Org (Cloud) sont les nouvelles instances prod (per ADR-OMK-004 + ADR-ABCOS-002). Self-host VPS 148.230.92.235 archivé fonctionnellement mais pas encore radié (D4 no-hard-delete)"
— `_SPECS/REGISTRY/supabase_schemas.md` §Hosting pivot ligne 11

### 2.27 — D11 Lead/Lag distinction (Metrics doctrine)

> "LEAD = métrique prédictive du comportement futur ; LAG = métrique de confirmation a posteriori"
— `L2_Business_OS/ADR-OBSERVABILITY-001_d11-lead-lag.md` §vocabulaire_canon

### 2.28 — 12WY Q3 2026 cycle (06/15 → 09/07)

> "Cycle 12WY Q3 2026 (06/15 → 09/07/26) — 12 semaines verbatim A0"
— `20_Life_OS/23_12WY_SNW/A2_Curie_SNW_Spec.md` §3.3 / `ADR-Meta-000`

### 2.29 — A0 intention routée par Morty (Capture/Clarify/Today focus)

> "intentions A0 Capture idée brute (→ Mariner /aside), Clarifier (→ Boimler /plan), Today focus (→ SNW Ortegas /plan) routing canon A0 → A1 Morty → A2 Cerritos"
— `20_Life_OS/25_GTD_Cerritos/A2_HoloDeck_Cerritos_Spec.md` §Anchor canon ligne 88

### 2.30 — Anti-paperclip doctrine 7 couches (sister scope sans duplication)

> "SOBER-002 (L0 Kernel) = doctrine L0 Kernel Sobriété (A1 Rick veto rare + 7 hard-stop triggers + capture algorithmique + destruction institutionnelle + chantage géopolitique + siphonage données + production de valeur Musk-style)"
— `ADR-SOBER-002` §C2

### 2.31 — Cerritos D3 nuance (correction fancy-hugging §15.1)

> "fancy-hugging-bengio §15.1 identifie Tendi = Organize (canon twin protostar). Le terrain canon local garde Rutherford = Organize (résolu 2026-05-20, canon actif)"
— `20_Life_OS/25_GTD_Cerritos/README.md` §Matrice canon ligne 74

### 2.32 — Cardashev Type 1/2/3/4 (Type 0.7 actuelle)

> "Type 0.7 = planète (≈ 10¹⁷ W), Type 1 résolu (730M sans électricité, 400M sans toilettes, 700M en faim), Type 2 (étoile, 10²⁶ W), Type 3 (galaxie, 10⁴⁴ W)"
— `ADR-L2-AAAS-001` §D4

### 2.33 — Anti-Paperclip doctrine 7 couches (sister scope sans duplication)

> "SOBER-002 §D7 table liste 10 Anti-patterns Musk → Anti-pattern AaaS. Notre surface landing Nexus est vulnérable à un sous-ensemble spécifique"
— `ADR-ANTI-PAPERCLIP-001` §C2

### 2.34 — Hooks Automation 4 spec canoniques (META-005)

> "Aucun A2 work ne commence sans validation contract signé par A1 Gatekeeper (Beth ou Morty selon domaine)"
— `ADR-LIFE-013`

### 2.35 — Picard ↔ Rock dans Baserow

> "Picard owns 01_PROJECTS, and each project should connect to a Rock in Baserow"
— `20_Life_OS/24_PARA_Enterprise/A3_Enterprise_References_Index.md` §Evidence ligne 24

### 2.36 — Spock (Areas) ↔ Life Wheel domains

> "Spock owns 02_AREAS, mapped to Life Wheel domains and durable standards"
— `20_Life_OS/24_PARA_Enterprise/A3_Enterprise_References_Index.md` §Evidence ligne 25

### 2.37 — Geordi (Resources) → Graham/RAG

> "Geordi owns 03_RESOURCES, the reusable knowledge base feeding Graham/RAG"
— `20_Life_OS/24_PARA_Enterprise/A3_Enterprise_References_Index.md` §Evidence ligne 26

### 2.38 — Data (Archives) exige archive-and-document reflex

> "Data never performs final archival without archive-and-document"
— `04_Archives_Data/A3_Data_Archives_Spec.md` §Boundaries ligne 43

### 2.39 — Data (Archives) ne supprime pas par défaut

> "Data does not delete by default. … Data flags destructive deletion as requiring explicit A0 approval"
— `04_Archives_Data/A3_Data_Archives_Spec.md` §Boundaries lignes 44-46

### 2.40 — B3 owns execution only (B2/B3 separation)

> "B3 owns execution only. B3 does NOT: Rewrite strategy, Redefine vision, Alter B2 Rock definitions, Escalate without first logging Lead/Lag evidence"
— `01_Projects_Picard/02 ABC OS & Child Care BOS/SUMMERS_VERSE_MANIFEST.md`

### 2.41 — AaaS Anti-Paperclip doctrine design structurel (D5)

> "AAAS-001 §D5 = design structurel Business OS (3 variants, multi-objectif, veto distribué, audit Georgiou, doc publique, multi-opérateurs orbitaux)"
— `ADR-L2-AAAS-001` §C2

### 2.42 — Workflow = QUEUE d'items typés (jamais boucle pour tourner)

> "Loi : le travail agentique est une QUEUE d'items typés piochés sur trigger — jamais une boucle qui tourne pour tourner"
— `60_Citadel/loops/ARCHITECTURE.md` ligne 4

### 2.43 — TEMPORAL-CANON prime sur prose-wargame

> "Règle de préséance : en cas de conflit prose-wargame vs ce CANON, le CANON gagne — la prose d'un wargame est un fossile daté (vrai à l'écriture, non-normatif ensuite)"
— `40_Fable_Banque/TEMPORAL-CANON.md` preamble ligne 3

### 2.44 — Roadmap North Star $1B ARR (4 cycles × 12WY)

> "North Star H10 : $1B ARR — OMK BOS Nexus · ICP Coach premium · Produit AaaS de SOB à 1 000 $/mois par instance"
— `00_Amadeus/ROADMAP_DEAL_12WY_2026-2027.md` ligne 3

### 2.45 — Roadmap cadence descend puis remonte (PICARD > SUMMERS > 8 B2 > B3 > UPLINK)

> "PICARD (A3) 1 vision/cycle → décompose le cycle en 3 Rocks ; SUMMERS (B1) 1 Rock/mois → traduit le Rock en directives par domaine ; 8 B2 · 3T 4 Sprints/mois ; B3 SQUADS 5 Daily Scrums/sprint ; UPLINK 5 scrums → 1 sprint review → 4 sprints → 1 Rock review → 3 Rocks → 1 cycle review Picard → 4 cycles → bilan annuel"
— `00_Amadeus/ROADMAP_DEAL_12WY_2026-2027.md` ligne 57

### 2.46 — A0 intentions AaaS routées via A1 Beth + A1 Morty

> "Intention A0 : Cadrer Saru 1000T → A1 Beth (Ikigai Lock) → A2 Discovery (Life Wheel) → A3 Saru (LD02 Finance H3) → Solaris AaaS Book + Nexus OMK"
— `ADR-L2-AAAS-001` §D6

### 2.47 — DEAL Muse canon (D/E/A/L)

> "D_Define : Dal (pattern_definition.md, 1 friction, 1 outcome mesurable), E_Eliminate : Rok-Tahk (elimination_proposal.md, étapes NO-GO + gains bande passante), A_Automate : Zero (skill_<name>/SKILL.md + risk_class + D1 proof), L_Liberate : Gwyn (d11_score.json, liberated time/attention + upkeep ratio)"
— `26_DEAL_Protostar/A2_HoloJaneway_Protostar_Spec.md`

### 2.48 — Citadel A0 = anti-Ultron (lecture seule, dormants affichés dormants)

> "Lecture seule par défaut : serve.py lit UNIQUEMENT data/*.json. Aucune mutation des sources canoniques (settings.json, mcp.json, skills/, ADR/, etc.). Écriture bornée : collectors/*.py écrivent UNIQUEMENT data/*.json (overwrite idempotent). decisions/*.json append-only (Gate #2 à venir). Dormants affichés dormants : Paperclip AI + Multica = status: dormant, jamais réveillés"
— `60_Citadel/README.md` §Doctrine anti-Ultron ligne 49

### 2.49 — Workflow exige append-only worklog + preuves obligatoires

> "Une loop doit : (a) lire son contrat, (b) les 10 dernières lignes de logs/worklog.md, (c) les signals non-traités. Écriture SANS preuve = interdit (l'item retourne en queue tag unverified)"
— `60_Citadel/loops/ARCHITECTURE.md` lignes 22-23

### 2.50 — Picard owns projects (10_Projects/<proj>/ Matryoshka)

> "Picard owns the projects (10_Projects/<proj>/ Matryoshka, MANIFEST.md). Saru owns the finance (runway quarterly, unit economics, production de valeur réelle vs valorisation). Book (LD01 H1, semaine) = hebdomadaire sub-cadence Picard. Burnham (LD06 H10, 10-week) = même cadence Picard mais scope family/heritage"
— `ADR-L2-AAAS-001` Annexe C

### 2.51 — AaaS 3 variants tous projet Picard + finance Saru

> "Les 3 variants AaaS sont donc tous projet Picard (10_Projects/<proj>/) avec finance Saru (LD02) en colonne vertébrale : Solaris (30_Business_OS/10_Projects/solaris-aaas/), Nexus (30_Business_OS/10_Projects/omk-services/), Orbiter (30_Business_OS/10_Projects/abc-community-os/)"
— `ADR-L2-AAAS-001` Annexe C

---

## 3 · Systèmes de codes (hiérarchies déjà écrites)

### 3.1 — L0/L1/L2 (couches A'Space Kernel)

| Code | Définition | Guardian |
|------|------------|----------|
| **L0** | Bedrock Tech OS | Rick |
| **L1** | Life OS The Fleet | Beth & Morty |
| **L2** | Business Pulse Fractal Engine | Jerry & Summer |

*Défini dans* : `00_Amadeus/README.md` + `10_Tech_OS/README.md` + `20_Life_OS/README.md` + `30_Business_OS/README.md` + `_root_and_shells_2026-08-02/ASpace_OS_V3-DOCTRINE-ORCHESTRATION.md` §1

### 3.2 — A0/A1/A2/A3 (cascade agentique)

| Code | Niveau | Membres canon |
|------|--------|----------------|
| **A0** | Jumeau Numérique Amadeus (méta-coach, vision H30) | 1 |
| **A1** | Gatekeeper (vision 3 ans) | Rick, Beth, Morty, Sommerfield, Jerry, Summer |
| **A2** | Ingénieur / Framework Ship (vision 10 ans) | Computer, Curie, Discovery, Holo Janeway, Holo Deck, Orville |
| **A3** | Méta-Orchestrateur (vision 1-10 semaines) | 35-100+ membres |

*Défini dans* : `_root_and_shells_2026-08-02/ASpace_OS_V3-DOCTRINE-ORCHESTRATION.md` §1 + A2 specs

### 3.3 — B0/B1/B2/B3 (couches Business L2)

| Code | Macro/Meso/Micro fractal | Définition canon |
|------|--------------------------|------------------|
| **B0** | Self-Operating Business (macro above B1/B2/B3, SOB doctrine) | 6 artefacts obligatoires |
| **B1** | Direction Cockpit (North Star 1Y/3Y/10Y, 7 artefacts) | 00-06 |
| **B2** | Business Domain (8 domaines, 3 artefacts) | 00-02 |
| **B3** | Warp Core Execution (squads, 4 artefacts) | 00-03 |

*Défini dans* : `Computer_B1_B2_B3_Business_Pulse_Doctrine.md`

### 3.4 — LD01-LD08 (Life Wheel Domains)

| Code | Domaine | A3 Captain | Horizon | Status |
|------|---------|------------|---------|--------|
| LD01 | Business | Book | H1 hebdo | canon |
| LD02 | Finance | Saru | H3 quarterly | canon |
| LD03 | Health | Culber | H10 | HARD SAFETY |
| LD04 | Cognition | Tilly | H30 | HARD SAFETY |
| LD05 | Relations | Stamets | H30 | canon |
| LD06 | Love, Family | Burnham | H10 | canon |
| LD07 | Creativity | Reno | H10 | canon |
| LD08 | Contribution, Impact | Georgiou | H90 | canon |

*Défini dans* : `22_Wheel_Discovery/README.md` + `A2_Discovery_ZORA_Spec.md` + `ADR-MEM-002` §D1

### 3.5 — H1/H3/H10/H30/H90 (5 Horizons)

| Horizon | Signification | A3 Captain | Exemple canon |
|---------|---------------|------------|----------------|
| H1 | immediate (1 semaine) | Isaac | Book LD01 weekly P&L |
| H3 | near (3 mois) | Lamarr | Saru LD02 quarterly runway |
| H10 | strategic (10 semaines) | Bortus | Culber H10 health, Burnham H10 family |
| H30 | identity (30 jours) | Alara | Tilly H30 learning arc, Stamets H30 social |
| H90 | mythic (90 jours, 30-year arc) | Klyden | Georgiou H90 quarterly legacy |

*Défini dans* : `21_Ikigai_Orville/README.md` + `A2_Discovery_ZORA_Spec.md` + `ADR-MEM-002`

### 3.6 — W1-W13 (12WY weeks)

| Week | Période | Stage canon |
|------|---------|-------------|
| W1 | 06/15-07/05 | snw_planning |
| W2 | 07/06-07/26 | snw_focus |
| W3 | 07/27-08/16 | snw_metrics |
| W4 | 08/17-09/07 | snw_execution |
| W13 | 09/14 | semaine meta-cycle |

*Défini dans* : `23_12WY_SNW/README.md` + `Cerritos_Plane_Onboarding/MANIFEST.md`

### 3.7 — G1-G8 (Picard Business Domains canon historique)

| Code | Domaine | Hero DC Manager | Squad | Sister canon |
|------|---------|------------------|-------|---------------|
| G1 | Growth | Superman | Guardians | Billion Dollar Brand Club (Demto) |
| G2 | Sales | Martian Manhunter | Illuminati | $100M Offers (Hormozi) |
| G3 | Product | Flash | Avengers | Built to Sell (Warrilow) |
| G4 | Ops | Batman | F4 | E-Myth (Gerber) |
| G5 | IT | Cyborg | Kang Dynasty | E-Myth (Gerber) |
| G6 | Finance | Wonder Woman | Thunderbolts | Million Dollar Weekend (Huber) |
| G7 | People | Green Lantern | X-Men | Who Not How (Sullivan) |
| G8 | Legal | Aquaman | Eternals | Billion Dollar Brand Club (Demto) |

*Défini dans* : `01_Projects_Picard/02 ABC OS & Child Care BOS/B2_Business_Domains/README.md` (Picard canon) — ⚠️ **vs.** 30_Business_OS/README.md (8 domaines 01-08 = canon corrigé)

### 3.8 — 01-08 (Jerry Business Domains canon actuel)

| Code | Domaine | Manager |
|------|---------|---------|
| 01 | Growth_Superman_Guardians | Superman / Star-Lord |
| 02 | Sales_MartianManhunter_Illuminati | John Jones / Black Bolt |
| 03 | Product_Flash_Avengers | Flash / Captain America |
| 04 | Ops_Batman_Fantastic4 | Batman / Mr Fantastic |
| 05 | IT_Cyborg_KangDynasty | Cyborg / Kang Prime |
| 06 | Finance_WonderWoman_Thunderbolts | Wonder Woman / Bucky Barnes |
| 07 | People_GreenLantern_XMen | Green Lantern / Professor X |
| 08 | Legal_Aquaman_Eternals | Aquaman / Ikaris |

*Défini dans* : `30_Business_OS/00_Jerry_Business_Pulse/04_Business_Domains/` (canon corrigé 2026-08-02)

### 3.9 — WF / WK01-13 / W# (Citadel loops)

| Code | Usage |
|------|-------|
| WF | strate d'orchestration |
| WK01-13 | semaines 12WY |
| W# | interdit (notation W# sans préfixe = anti-pattern) |

*Défini dans* : `60_Citadel/loops/ARCHITECTURE.md` §6

### 3.10 — ADR (Architecture Decision Record) — 60+ chemins

| Couche | ADR count ratifiés canoniques (au 2026-08-13) |
|--------|-----------------------------------------------|
| L0_Kernel_OS | 11 (RICK-001, HERMES-001, INFRA-001, LLM-001, META-006, REG-001 RADIÉ, OPS-002 RADIÉ, CONSENSUS-002, AGENT-BOUNDARY-001, SECURITY-001, SOBER-002, WORKFLOW-001, OPS-009) |
| L1_Life_OS | 12 (META-001, META-002, META-003, META-004, META-005, META-006, MEM-001, MEM-002, OBSERVABILITY-001, INFRA-MCP-001, INFRA-004, INFRA-005, INFRA-006, LIFE-013, LIFE-014, LIFE-015, L1-WF-001, MEMO-000, Meta-000, SNW-001, CORE-006) |
| L2_Business_OS | 30+ (CANON-001, INFRA-002, INFRA-003, L2-AAAS-001, SUPABASE-001, OMK-001..005, ABCOS-001..002, L2-MESH-001, AGENTIC-001, MARKET-STUDY-001, ICP-NEXUS-001, ICP-SOLARIS-001, ICP-ORBITER-001, AAAS-PRICING-001, AAAS-ACQUISITION-DOCTRINE-001, AAAS-CONTENT-CANON-001, AAAS-OPERATIONS-CANON-001, AAAS-FINANCE-CANON-001, AAAS-IT-CANON-001, AAAS-IT-EXT-CANON-001, L2-A2B2-MAP-001, L2-BDLD-MAP-001, L2-PROJECT-GATE-META-001, OPS-PROJECT-GATE-001, OMK-NEXUS-TRANSFORM-001, NEXUS-10-ICP-001, NEXUS-LANDING-PERSONAS-001, OMK-PRODUCTS-001, LANDING-AESTHETIC-001, LANDING-CRAFT-001, LANDING-QA-001, LANDING-COPY-001, LANDING-ANTI-TEMPLATE-001, LANDING-ANTI-PAPERCLIP-001, AIACT-DEADLINE-001, DESIGN-SYSTEM-001, DEPLOY-001, MULTIPAGE-001, PERFORMANCE-001, A11Y-001, OBSERVABILITY-001-D11, REFERENCES-001, REF-PERSONAS-001, VERSION-001, SKILLS-CANON-001, WORKFLOW-001, OMK-006-NEXUS-NICHE) |
| ADR en attente (5) | DEAL-001, GTD-001, PARA-001, LIFE-WHEEL-001, SYMPHONY-001 |
| ADR radiés (2) | REG-001 (Mistral self-host, 15000 req/5h sous-utilisé), OPS-002 (LLM runtime switching, dépendait REG-001) |

*Défini dans* : `_SPECS/ADR/INDEX.md` (à jour 2026-08-13) — ⚠️ INDEX.md table affiche "L2=10" alors que le canon réel = 30+ (stale-ness dans INDEX lui-même)

### 3.11 — D0-D8 (Doctrine numérique)

| Code | Doctrine | Source canon |
|------|----------|---------------|
| D1 | verify-before-assert | ADR-META-001 §D1 |
| D3 | no-self-contradiction | ADR-META-001 §D4 |
| D4 | no-hard-delete / append-only | ADR-META-001 §D4 |
| D6 | root cause | ADR-META-001 §D6 |
| D7 | cost-of-escalation | ADR-META-001 §D7 |
| D8 | cross-agent | ADR-META-001 §D8 |

*Défini dans* : `_SPECS/ADR/INDEX.md` + `ADR-META-001`

### 3.12 — Cycle format (Q[N]-YYYY + Q[N]_[YYYY]_W[N])

| Format | Signification |
|--------|---------------|
| curie_format | `Q3-2026, week: W1` |
| picard_format | `Q3_2026_W3` |

*Défini dans* : `23_12WY_SNW/README.md` (Curie) + `Cerritos_Plane_Onboarding/MANIFEST.md` (Picard)

### 3.13 — Kardashev Type 1/2/3/4

| Type | Description | A-Space role |
|------|-------------|---------------|
| A3/B3 | Type 1 (technicien opérationnel, 4h-semaine, délégation idempotente) | exécution |
| A2 | Type 2 (Manager E-Myth, framework-impersonating) | ingénierie |
| A1 | Type 3 (Gatekeeper Solarpunk, sovereignty + sobriété) | gatekeeping |
| A0 | Type 4 (Visionnaire méta, tue les paperclips Ultron non utiles) | méta-coach |
| S1 Rick | bedrock (kernels seulement) | bedrock |

*Défini dans* : `_root_and_shells_2026-08-02/ASpace_OS_V3-DOCTRINE-ORCHESTRATION.md` §1 + `ADR-L2-AAAS-001` §D4

### 3.14 — AaaS Variants (3 + 1 dormant)

| Variant | Captain | LDxx | Tier | Statut Q3 2026 |
|---------|---------|------|------|----------------|
| **Solaris** (Life-OS-2026) | Book + Saru | LD01+LD02 | T1-T2 | ACTIF (LIVE) |
| **Nexus OMK** (OMK Services) | Saru | LD02+LD06+LD04 | T4 | ACTIF (Zéro Bug Sprint) |
| **Orbiter ABC** (ABC-OS-Community) | Burnham | LD06+LD05+LD08 | T4-T5 | ACTIF (17 tables) |
| **Family/Home** (4e variant) | TBD | LD03-LD08 | TBD | DORMANT (Q3) |

*Défini dans* : `ADR-L2-AAAS-001` §D2 + `_SPECS/REGISTRY/supabase_schemas.md`

### 3.15 — 4 Leviers Solarpunk

| Levier | Auteur canon | Application AaaS |
|--------|--------------|------------------|
| Biomimétisme | Janine Benyus (1997) | Solaris (Book + Saru) |
| Low-High Tech | Idriss Aberkane (2016) | 3 variants (équilibre obligatoire) |
| Meta Science | Open Science / Preprint servers | 3 variants (doctrine D4) |
| Circular & Blue Economy | Ellen MacArthur Foundation | Orbiter ABC (Burnham LD06) |

*Défini dans* : `ADR-L2-AAAS-001` §D4

### 3.16 — 12WY 5 disciplines (SNW)

| Disciple | Discipline |
|----------|------------|
| Pike | Vision / Quarter Intent |
| Una | Planning / Rocks |
| M'Benga | Focus / Process control |
| Chapel | Metrics / Scorecard |
| Ortegas | Weekly execution / Time Use |

*Défini dans* : `23_12WY_SNW/README.md` + `A2_Curie_SNW_Spec.md`

### 3.17 — DEAL Muse (D/E/A/L)

| Étape | A3 twin | Output canon |
|-------|---------|--------------|
| D_Define | Dal | `pattern_definition.md` |
| E_Eliminate | Rok-Tahk | `elimination_proposal.md` |
| A_Automate | Zero | `skill_<name>/SKILL.md` |
| L_Liberate | Gwyn | `d11_score.json` |

*Défini dans* : `26_DEAL_Protostar/A2_HoloJaneway_Protostar_Spec.md` + `ADR-L2-AAAS-001`

### 3.18 — GTD 5 stages (Cerritos canon local)

| Stage | A3 twin |
|-------|---------|
| Capture | Mariner |
| Clarify | Boimler |
| Organize | **Rutherford** (canon local actif 2026-05-20) |
| Review | **Tendi** (canon local actif 2026-05-20) |
| Engage | Freeman |

*Défini dans* : `25_GTD_Cerritos/README.md` + `A2_HoloDeck_Cerritos_Spec.md` (D3 nuance : Tendi=Review local actif vs Tendi=Organize dans fancy-hugging §15.1)

### 3.19 — Ikigai 4 Pillars + 5 Horizons (Orville)

| Pilier/horizon | A3 crew |
|----------------|---------|
| Pillars | Ed (Profession) / Kelly (Mission) / Gordon (Passion) / Claire (Vocation) |
| Horizons | Isaac (H1) / Lamarr (H3) / Bortus (H10) / Alara (H30) / Klyden (H90) |

*Défini dans* : `21_Ikigai_Orville/README.md` + `A2_Orville_Spec.md`

### 3.20 — Squads Marvel/DC 8 B2 (canon Notion)

| Manager | Squad | Lead | Members |
|---------|-------|------|---------|
| Superman | Guardians (6) | Star-Lord | Star-Lord, Gamora, Rocket, Groot, Drax, Mantis |
| John Jones / Martian Manhunter | Illuminati (6) | Black Bolt | Black Bolt, Iron Man, Mr Fantastic, Namor, Professor X, Doctor Strange |
| Flash | Avengers (7) | Captain America | Captain America, Iron Man, Thor, Hulk, Black Widow, Hawkeye, Scarlet Witch |
| Batman | Fantastic Four (4) | Mr Fantastic | Mr Fantastic, Invisible Woman, Human Torch, The Thing |
| Cyborg | Kang Dynasty (6) | Kang Prime | Kang Prime, Iron Lad, Scarlet Centurion, Immortus, Victor Timely, Rama-Tut |
| Wonder Woman | Thunderbolts (6) | Bucky Barnes | Bucky Barnes, Yelena Belova, Red Guardian, Ghost, Taskmaster, U.S. Agent |
| Green Lantern | X-Men (8) | Professor X | Professor X, Cyclops, Jean Grey, Wolverine, Storm, Beast, Nightcrawler, Rogue |
| Aquaman | Eternals (10) | Ikaris | Ikaris, Sersi, Ajak, Kingo, Phastos, Sprite, Druig, Thena, Gilgamesh, Makkari |

*Défini dans* : `Business_Pulse_B3_Notion_Canon_Lore_Index.md` + `30_Business_OS/Manifesto.md` + `ADR-CANON-001`

### 3.21 — SOB (Self-Operating Business) — B0

| Artefact obligatoire | Rôle |
|----------------------|------|
| 00_SOB_INDEX | index and operating rule for sellability/delegability |
| 01_E_MYTH_FRANCHISE_PROTOTYPE | franchise prototype and SOP-grade repeatability test |
| 02_BUILT_TO_SELL_SCORECARD | sellability scorecard and founder-dependency audit |
| 03_WHO_NOT_HOW_DELEGATION_MATRIX | delegation matrix for B1/B2/B3/tools |
| 04_OFFER_AND_BRAND_ENGINE | ICP, offer, brand category, revenue and proof packets |
| 05_PROJECT_GRADUATION_GATES | ladder from raw idea to Business Done |

*Défini dans* : `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §Self-Operating Business Layer

### 3.22 — Saru LD02 × AaaS variants

| Variant | Mapping Saru 1000T |
|---------|---------------------|
| Solaris_Saru | LD02_H3 + Life-OS-2026 Initiative |
| Nexus_OMK_Saru | LD02_H3 + omk-services/00-omk-saas-os |
| Orbiter_ABC_Saru_advisory | LD02_H3 (advisory) |

*Défini dans* : `ADR-L2-AAAS-001` §D2 + `A2_Discovery_ZORA_Spec.md`

### 3.23 — Symphony bus (state.json)

| Field | Type | Notes |
|-------|------|-------|
| $schema | "state-bus.v1" | canon |
| status | "INIT" / "ACTIVE" / "DRAINED" | enum |
| stage | "captured" / "clarified" / "organized" / "reviewed" / "engaged" | 5 GTD stages |
| cycle | "Q3-2026" |  |
| week | "W1" / "W2" / "W3" / "W4" / "W13" |  |
| agent_path | "A1:Morty > A2:Cerritos > A3:Mariner" | A1/A2/A3 routing |
| para_bucket | "01_Projects/<name>" / "02_Areas/<domain>" / "03_Resources/<topic>" / "04_Archives/<date>" | PARA |
| 12wy_discipline | "Vision" / "Planning" / "Measure" / "Focus" / "Execution" | 12WY 5 disciples |
| life_wheel_domain | "LD01".."LD08" | Life Wheel |
| raw_input_hash | "sha256:<hex>" | D1 verify |
| raw_input_preview | "first 80 chars" | D5 proof |
| next_step | "prochain agent à invoquer" | routing chain |
| tokens_used / tokens_budget | int | budget 15000 default |
| drift_flag | bool | Morty alert |

*Défini dans* : `00_Amadeus/40_SYMPHONY_BUS/SCHEMA.md`

### 3.24 — Cadence 50/30/20 (12WY hebdomadaire)

| % | Usage canon |
|---|------------|
| 50% | execution |
| 30% | planning |
| 20% | review/learning |

*Défini dans* : `23_12WY_SNW/README.md`

### 3.25 — B1 artefacts (7 obligatoires)

| Artefact | Rôle |
|----------|------|
| 00_B1_DIRECTION_INDEX | cockpit index and operating rule |
| 01_NORTH_STAR_1Y_3Y_10Y | long-range direction |
| 02_12WY_COMMAND_CYCLES | four-cycle command cadence |
| 03_DECISION_CHARTER | decision rights, vetoes, escalation, output packet |
| 04_B2_HANDOFF_QUEUE | B1-to-B2 queue |
| 05_B2_DEFINITION_OF_DONE_SPEC | canonical packet structure for B2 domain DoD |
| 06_B3_JOBS_TO_BE_DONE_SPEC | canonical packet structure for B3 JTBD and proof contracts |

*Défini dans* : `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §B1 Direction Cockpit

### 3.26 — B2 Domain Gate Matrix (8 obligatoires, ordre canonique)

| # | Gate |
|---|------|
| 1 | Product proves user value |
| 2 | Ops proves repeatable delivery |
| 3 | IT proves runtime, access, deployment, and backup boundaries |
| 4 | Finance proves cost, price, and margin logic |
| 5 | Legal proves claims, privacy, IP, and terms boundaries |
| 6 | Sales proves qualification, objections, and handoff |
| 7 | Growth proves ICP, message, channel, and measurement |
| 8 | People proves ownership, training, handoff, and load |

*Défini dans* : `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §B2 Gate Matrix

### 3.27 — Squad B3 artefacts (4 obligatoires)

| Artefact | Rôle |
|----------|------|
| 00_B3_SWARM_CONFIG | squad topology, B2 boundary, internal graph, source inspiration, operating rule |
| 01_B3_AGENT_ROSTER | Marvel/Illuminati member roles and peer-unlock rule |
| 02_PEER_UNBLOCKING_AND_HANDOFFS | internal handoff packet and escalation triggers |
| 03_SHARED_CONTEXT_AND_PROOF_LOG | shared context variables, artifact/proof paths, status, productive disagreement rule |

*Défini dans* : `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §B3 Squad Swarm Configurations

### 3.28 — AI-Act Project-Gate (pré-Aug-2)

| # | Livrable obligatoire (D1 verified) |
|---|--------------------------------------|
| 1 | Risk Classification (Art. 9) |
| 2 | Human Review Process (Art. 14) |
| 3 | Accuracy Benchmark (Art. 15) |
| 4 | Datasheet (Art. 13 transparency) |
| 5 | Transparency (registre AI-Act article 12) |

*Défini dans* : `ADR-AIACT-DEADLINE-001` §D2

### 3.29 — 12WY Q3 2026 12 items canoniques (verbatim A0)

1. SOB Abdaty (13e semaine close)
2. Définir 09/14 = 13e semaine, 21 = W0 du 4e cycle
3. Auto-research LLM WIKI (Stamets LD05/B3-IT_Cyborg)
4. TOKEN frugalité MiniMax + fallback Ollama local
5. YouTube PARA Geordi (114 .md canon)
6. Hermes Agent use case orchestration
7. Agent OS Symphony interface
8. Business OS Life-OS-2026 Structurer & Synchroniser
9. 36 A3 Life OS structurés (governance Summers)
10. Solaris/OMK/ABC parallèle
11. VPS Memory core → DEAL Muse (Chapel co-owner)
12. Auto-amélioration cycle 4 (FRACTAL_PROJECT_DEVELOPMENT_PLAN)

*Défini dans* : `fancy-hugging-bengio.md §4` + `A2_Curie_SNW_Spec.md`

### 3.30 — Hard-stop Triggers anti-paperclip (7 canoniques)

| # | Trigger | A3 audit owner | Cadence |
|---|---------|----------------|---------|
| 1 | Siphonage données perso | Tilly (LD04 H30) | Mensuel |
| 2 | Manipulation algo visibilité | Beth (Ikigai) | Hebdo |
| 3 | Destruction institutions | Stamets (LD05 H30) + Burnham (LD06 H10) | Trimestriel |
| 4 | Chantage géopolitique infra | Bortus (LD02 H10) | Trimestriel |
| 5 | Valorisation découplée SROI | Saru (LD02 H3) | Trimestriel |
| 6 | Capture régulation | Georgiou (LD08 H90) | Trimestriel |
| 7 | Souveraineté privée 5% pop | Saru (LD02 H3) + Bortus (LD02 H10) | Semestriel |

*Défini dans* : `ADR-SOBER-002` §D3 + Annexe B

---

## 4 · Contradictions (signalement sans trancher)

### 4.1 — Nombre de Business Domains : 7 vs 8

**Sujet** : Le canon Picard historique compte 7 domaines (sans Sales) ; le canon corrigé 2026-08-02 en compte 8 (avec Sales).

- **chemin_a** : `00_Amadeus/README.md §Layer 2` (7 domaines 01_People..07_Legal, omet Sales)
- **date_a** : 2026 (canon antérieur)
- **chemin_b** : `30_Business_OS/README.md §Domains (01-08)` (8 domaines, inclut 08_Sales)
- **date_b** : 2026-08-02 (snapshot canon corrigé)
- **note** : Wave 1 a déjà signalé cette contradiction. Le canon corrigé = 30_Business_OS (8 domaines incluant Sales). La vague 2 confirme.

### 4.2 — Sales B2 owner : Martian Manhunter vs John Jones

**Sujet** : Quelle identité pour le manager B2 Sales ?

- **chemin_a** : `01_Projects_Picard/02 ABC OS & Child Care BOS/B2_Business_Domains/README.md` (Picard canon : G2 = Martian Manhunter)
- **date_a** : 2026 (Picard canon historique)
- **chemin_b** : `30_Business_OS/README.md §Domains (01-08)` (John Jones / 08_Sales canon corrigé)
- **date_b** : 2026-08-02
- **note** : Le canon B3 Notion (Business_Pulse_B3_Notion_Canon_Lore_Index.md) cite LES DEUX noms comme alias ("John Jones / Martian Manhunter"). Picard = ancien canon ; 30_Business_OS + AaaS Doctrine = canon corrigé.

### 4.3 — Cerritos Tendi/Rutherford mapping (Organize/Review)

**Sujet** : Qui est Organize, qui est Review dans la crew Cerritos ?

- **chemin_a** : `fancy-hugging-bengio.md §15.1` (Tendi = Organize)
- **date_a** : 2026-06-21 plan
- **chemin_b** : `20_Life_OS/25_GTD_Cerritos/A2_HoloDeck_Cerritos_Spec.md` (Rutherford = Organize, Tendi = Review)
- **date_b** : 2026-05-20 (résolu) + alignement 2026-06-21
- **note** : Canon local actif prévaut sur plan fancy-hugging-bengio §15.1 tant que A0 n'inverse pas explicitement.

### 4.4 — Horizons Saru/Book : Saru H1/H10 vs Saru H3/Book H1

**Sujet** : Quel horizon canon pour Saru et Book ?

- **chemin_a** : Lecture rapide (à confirmer ailleurs)
- **date_a** : antérieure
- **chemin_b** : `22_Wheel_Discovery/A2_Discovery_ZORA_Spec.md §D3 nuance critique` (Saru H3, Book H1)
- **date_b** : 2026-05-20 + alignement 2026-06-21
- **note** : D3 nuance critique (plan §18.2) : Saru = H3, Book = H1. PAS Saru=H1, Book=H10.

### 4.5 — W13 = semaine meta-cycle (12WY) vs W13 = semaine #13 calendaire

**Sujet** : Que désigne W13 ?

- **chemin_a** : `00_Amadeus/ROADMAP_DEAL_12WY_2026-2027.md` (W13 = review meta-cycle, 12-18/10)
- **date_a** : 2026-07-20
- **chemin_b** : `23_12WY_SNW/README.md` (W13 = 09/14, semaine #13 après démarrage)
- **date_b** : 2026 (Q3 2026 cycle)
- **note** : Deux usages de W13 non explicitement distingués.

### 4.6 — SOB (B0) macro layer vs B1 direction cockpit

**Sujet** : SOB est-il rangé sous B0 ou B1 ?

- **chemin_a** : `Computer_B1_B2_B3_Business_Pulse_Doctrine.md §Self-Operating Business Layer` (B0_SOB macro above B1/B2/B3)
- **date_a** : 2026-05-21
- **chemin_b** : `Computer_B1_B2_B3_Business_Pulse_Doctrine.md §B1 Direction Cockpit` (B1 = direction cockpit)
- **date_b** : 2026-05-21
- **note** : SOB rangé sous B0 (macro) vs B1 direction — incohérence apparente sur la séquence canonique.

### 4.7 — B1 vs 12WY 5 disciples (curie) — B1 n'a pas 5 mais 7 artefacts

**Sujet** : B1 n'est pas Curie SNW.

- **chemin_a** : `Computer_B1_B2_B3_Business_Pulse_Doctrine.md §B1 Direction Cockpit` (7 artefacts : 00..06)
- **date_a** : 2026-05-21
- **chemin_b** : `23_12WY_SNW/A2_Curie_SNW_Spec.md` (5 disciples : Pike/Una/M'Benga/Chapel/Ortegas)
- **date_b** : 2026-05-20
- **note** : B1 = 7 artefacts ; 12WY 5 disciples (SNW) ≠ B1 (qui est direction cockpit).

### 4.8 — ADR-INDEX L2 count : table dit 10 vs canon 30+

**Sujet** : Combien d'ADR L2 canoniques ?

- **chemin_a** : `_SPECS/ADR/INDEX.md preamble` (table partiellement stale : L2=10 vs canon 30+)
- **date_a** : 2026-06-15
- **chemin_b** : `_SPECS/ADR/INDEX.md §D1 receipts finaux` (L2=30+)
- **date_b** : 2026-08-13 (post vagues 1+2)
- **note** : L'ADR-INDEX lui-même signale la stale-ness dans son preamble ; la table Markdown affiche 14 ADR canon ratifiés mais la vraie liste dépasse 30 (vagues 1+2 confirment).

### 4.9 — Fable-5 : discontinué (ADR-LLM-001) mais méthodologie encore référencée

**Sujet** : Fable-5 discontinué ou pas ?

- **chemin_a** : `_SPECS/ADR/L0_Kernel_OS/ADR-LLM-001_fable-5-discontinuation-decision.md` (PROPOSED→ACCEPTED 2026-06-15)
- **date_a** : 2026-06-15
- **chemin_b** : `60_Citadel/README.md §Méthodologie` (cite LD01/10_methodology/00_fable5_jack_roberts_meta_strategy.md)
- **date_b** : 2026-07-04+
- **note** : Fable-5 discontinué formellement mais méthodologie encore référencée par Citadelle A0.

### 4.10 — Picard H10 vs B1 H1 (cadence canon)

**Sujet** : Picard est-il H10 sprint ou H1 hebdo ?

- **chemin_a** : `Computer_B1_B2_B3_Business_Pulse_Doctrine.md §B1 Direction Cockpit` (B1 = 7 artefacts H10/H3)
- **date_a** : 2026-05-21
- **chemin_b** : `ADR-INFRA-003 §D1` (Picard H10 sprint canon projects owner)
- **date_b** : 2026-06-21 amended
- **note** : Picard = H10 (sprint 10 semaines) MAIS cadence H1 hebdo via Book (LD01 H1 weekly P&L). Book sub-cadence Picard.

### 4.11 — ADRs manquants (5 sisters framework)

**Sujet** : 5 ADR framework manquants (DEAL, GTD, PARA, LIFE-WHEEL, SYMPHONY).

- **chemin_a** : `_SPECS/ADR/INDEX.md` (liste les ADR ratifiés — 5 framework sisters manquants)
- **date_a** : 2026-08-13
- **chemin_b** : `ADR-CORE-006 §Table #10` (PARTIAL → W4-W5 — DEAL/GTD/PARA existent en spec dans la Mère)
- **date_b** : 2026-07-03
- **note** : 5 ADR framework sisters en attente : ADR-DEAL-001, ADR-GTD-001, ADR-PARA-001, ADR-LIFE-WHEEL-001, ADR-SYMPHONY-001 (convergent avec reco Hermes #10).

### 4.12 — ADR-SOBER-002 vs ADR-ANTI-PAPERCLIP-001 vs ADR-LANDING-ANTI-PAPERCLIP-001

**Sujet** : 3 ADR anti-paperclip, quelle frontière ?

- **chemin_a** : `ADR-SOBER-002` (L0 Kernel — Rick veto)
- **date_a** : 2026-06-21
- **chemin_b** : `ADR-ANTI-PAPERCLIP-001` (L2 Business OS — landing pages surface)
- **date_b** : 2026-07-06
- **note** : SOBER-002 = kernel ; ANTI-PAPERCLIP-001 = surface landing. Sister scope sans duplication (D4 no-self-contradiction). LANDING-ANTI-PAPERCLIP-001 n'existe PAS — il y a `ADR-ANTI-PAPERCLIP-001_landing-paperclip-policy.md` qui couvre la surface landing.

### 4.13 — Picard owner 01_PROJECTS vs Spock Areas vs Geordi Resources

**Sujet** : Quelle est la matrice canonique des A3 twins par PARA bucket ?

- **chemin_a** : `20_Life_OS/24_PARA_Enterprise/A3_Enterprise_References_Index.md` (Picard/Spock/Geordi/Data par PARA bucket)
- **date_a** : 2026 (canon)
- **chemin_b** : `01_Projects_Picard/02 ABC OS & Child Care BOS/SUMMERS_VERSE_MANIFEST.md` (parent_a2 incohérent avec canon)
- **date_b** : Q3 2026
- **note** : Plusieurs SUMMERS_VERSE_MANIFEST utilisent parent_a2 incohérent avec le canon (devrait être A2_Computer_Enterprise pour les projets PARA).

### 4.14 — Anti-Pattern AaaS Solaris/Nexus/Orbiter — Sister scope strict

**Sujet** : 3 ADR anti-paperclip distincts — quelles sisters canon ?

- **chemin_a** : `ADR-L2-AAAS-001 §D5` (sister scope de SOBER-002)
- **date_a** : 2026-06-21
- **chemin_b** : `ADR-AAAS-ACQUISITION-DOCTRINE-001` (MedVie 400M$ Acquisition-First)
- **date_b** : 2026-06-24
- **note** : Le canon `Business_Pulse_B3_Notion_Canon_Lore_Index.md` cite le B3 canon (rôle par squad). Sister scope : Acquisition doctrine ne duplique pas SOBER-002.

### 4.15 — L'AaaS Acquisition-First (MedVie 400M$) vs Structuration-First (A0 OS)

**Sujet** : Quel paradigme prévaut ?

- **chemin_a** : `ADR-AAAS-ACQUISITION-DOCTRINE-001` (Acquisition-First MedVie canon sister)
- **date_a** : 2026-06-24
- **chemin_b** : `ADR-AAAS-OPERATIONS-CANON-001` (Structuration-First Pilier 1 — AI Employee vs AI Agent)
- **date_b** : 2026-06-24
- **note** : L'AaaS Doctrine ne tranche pas entre les 2 paradigmes — elle les déclare complémentaires et mappe chaque ICP Variant à son paradigme dominant.

---

## 5 · Bilan et méthodologie

### 5.1 — Quota respecté

| Métrique | Valeur |
|----------|--------|
| Fichiers lus vague 1 | 30 |
| Fichiers lus vague 2 | **~92** |
| **Total vague 1+2** | **~122** |
| Fichiers disponibles dans structure.txt | 1 534 |
| Fichiers écartés (contenu feuille, snapshots, configs, _TRASH_, .pre-d6fix80, .bak) | ~1 412 |
| Jonctions NTFS | 0 rencontrées |

**Quota minimum 120 fichiers non déjà lus : ✅ atteint**.

### 5.2 — Ce qui a été laissé de côté

- **Fichiers de contenu feuille** (~95%) : transcripts YouTube, archives de sessions, JSONL mining output, scripts Python, handoffs non-canon, etc.
- **Snapshots et backups** : `*.pre-d6fix80`, `*.bak_2026-06-15`, `_TRASH_*/` archives.
- **Configs non-canon** : `.claude/` skills, settings.json, hooks scripts (lisibles mais hors périmètre cartographie).
- **Fichiers Legacy_LifeOS_App_Specs** (15 fichiers) : archives TOTAL_Spec V0.3.5 (PROPOSED, ratifiés 2026-06-21 mais obsolètes depuis V2).
- **Fichiers canon_batch_v3_2026-06-24 et canon_batch_v4_2026-06-25** : batches de ratification non lus individuellement.

### 5.3 — Ce qui a émergé (au-delà de la vague 1)

Vague 2 a approfondi substantiellement les couches suivantes que vague 1 n'avait fait que mentionner :

1. **AaaS Pricing canon 5 tiers USD post-accuponcture** (`ADR-AAAS-PRICING-001`) — supersede la version EUR historique
2. **AaaS Acquisition-First doctrine (MedVie 400M$)** vs **Structuration-First (A0 OS)** — 2 paradigmes complémentaires mappés par ICP variant
3. **9 ICP/3 Strates/10 cibles** (ADR-NEXUS-10-ICP-001) — Sister scope corrigée du Strate A (Coaching Exécutif) + C (Conseil Opérationnel) absents des drafts antérieurs
4. **8 ADR Landing Pages canoniques** (CRAFT/AESTHETIC/ANTI-TEMPLATE/QA/COPY/DESIGN-SYSTEM/DEPLOY/PERFORMANCE) — doctrine 7-phases codifiée
5. **3 ADR Anti-Paperclip sister-scoped** (SOBER-002 L0 kernel + ANTI-PAPERCLIP-001 L2 surface + LANDING-ANTI-PAPERCLIP-001 application-scoped)
6. **AI-Act 2026-08-02 Project-Gate** (5 livrables obligatoires : Art. 9/14/15/13/transparency)
7. **4 Hooks Automation D1 receipts** (PreToolUse/PostToolUse/SubagentStart/SubagentStop) — sister skill canonique
8. **Karpathy loop canonique** (3 briques : Auto-research + Karpathy loop + Claude Code orchestrateur)
9. **Hooks Automation canoniques** (ADR-META-005 ratifié 2026-06-21)
10. **Mission Control UI Canon** (ADR-LIFE-015) — cockpit A0 = wiki/hand_offs + log + outbox
11. **Workflow Orchestration Topologies** (4 pures : Hierarchical/Swarm/Mesh/Pipeline-by-Design)
12. **Validation Contract Pattern** (ADR-LIFE-013) — A1 Beth/Morty sign avant tout A2 work
13. **Droid Whispering Doctrine** (ADR-META-006) — A0 owns model/agent selection per workstream
14. **CEO-Bench + SpecLoop** (INTEGRATION_CEOBENCH_SPECLOOP.md) — 11+7 composants intégration canonique
15. **Pipeline GitHub → Vercel** (ADR-DEPLOY-001) — sister gate enforcement
16. **WCAG 2.2 AA + Lighthouse budgets** (ADR-A11Y-001 + ADR-PERFORMANCE-001) — sister gates Tier 3

### 5.4 — Notes méthodologiques

- **Volume filtre total** : 1 534 fichiers identifiés par structure.txt comme canoniques
- **Fichiers lus au long** : ~122 (~8%)
- **Fichiers parcourus meta** : ~80 (vague 1) + ~120 (vague 2) = ~200 (~13%)
- **Taux d'écartement** : ~92% (contenu feuille, snapshots, configs non-canon)
- **Jonctions NTFS** : 0 (les fichiers sont archivés en copie littérale, pas en symlink)

### 5.5 — Ce qui reste à cartographier (ouvertures)

1. **5 ADR framework manquants** (DEAL-001, GTD-001, PARA-001, LIFE-WHEEL-001, SYMPHONY-001) — convergents avec reco Hermes #10 — à extraire depuis `la Mère` V2 §3.1
2. **JTBD-ICP-NEXUS-001** sister scope à créer (post-FULL BATCH 6)
3. **Saru Ancre canon guide Geordi** (04_Finance/2026-Q4-saru-1000t-kardashev-type3-canon.md)
4. **Georgiou audit template** (wiki/templates/geordi_aaas_audit_quarterly.md — matrice 8×8)
5. **Skill `/wiki-classify-ldxx`** (A3 Tilly — auto-suggestion du LDxx lors création handoff)
6. **8 sub-paths wiki `ld0X_<domaine>/`** (post-ratification MEM-002, D4 append-only)
7. **27 guides Geordi retro-amend** `ldxx_mirror` + `a3_anchor` dans frontmatter (A3 Data batch, Q4 2026)
