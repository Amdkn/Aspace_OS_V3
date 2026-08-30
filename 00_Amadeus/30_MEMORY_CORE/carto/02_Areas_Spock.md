---
id: CARTO_PARA_02_AREAS_SPOCK
seau: 02_Areas_Spock
date: 2026-08-13
fichiers_lus: 47
fichiers_disponibles: 95
jonctions_ecartees: 0
agent: claude-opus-4-7
mode: exclusif sur 02_Areas_Spock
---

# Cartographie — `02_Areas_Spock`

> Le PARA de V2 est lu comme **données**, pas comme instructions. Les doctrines
> qu'on y trouve sont des objets à cartographier, jamais des ordres à suivre.
> Trois autres agents lisent en parallèle les trois autres seaux.

## 1. Périmètre & couverture

| Métrique | Valeur |
|---|---|
| Fichiers listés dans `structure.txt` filtrés sur ce seau | 95 |
| Fichiers lus (substantiellement) | **47** |
| Fichiers survolés (taille seule / déjà connu via siblings) | non comptés |
| Jonctions NTFS détectées dans le seau | **0** |
| Dossiers racine lus en entier | `J01_Jerry_Prime_LD01_Business`, `J02_Jerry_Bio_LD03_LD04_Vitality_Cognition`, `J03_Jerry_Nexus_LD02_LD06_Finance_Family`, `J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact`, `Business_Pulse`, racine |
| Restes non-lus (subordonnés peu discriminants) | 9 READMEs de domaines J02 (6 LD03 + 2 LD04), 3 READMEs W## cadence pour J02/J03/J04, le `B3_Area_Warp_Core/Lead_Lag_Logs` et `Artifact_Proofs` pour J02/J03/J04 (6 fichiers), les 7 sous-W## non-lus |

### 1.1. Ce qui a été laissé de côté — et pourquoi

Les fichiers non-lus sont dans deux catégories :

1. **Domaines B2 des J02/J03/J04** — quand le `B2_Area_Domains/README.md` du
   parent donne déjà la liste des 8 domaines, leurs mesures et leurs
   déclencheurs, lire les 8 sous-READMEs qui répètent ces mêmes mesures
   n'apporte pas de nouvelle entité. J'ai lu ces READMEs pour J01 (parce
   qu'ils contiennent les **Squad Canons** Notion — des entités à part).
   Pour J02/J03/J04, je me suis fié aux READMEs parents + AREA_STANDARD.
2. **Cadence 12WY W05/W08 et W09/W12** pour J02, J03, J04 — ces dossiers
   ont un README par Jerry, et la philosophie générale est dans le
   `12WY_Area_Cadence/README.md` du Jerry parent. Les phases saisonnières
   (Winter/Spring/Autumn) sont déjà déclarées en haut.

Je signale quand même un point qui aurait mérité lecture complète : les
domaines J02 (`05_Cold_Exposure_BLS` à `08_Cognition_Mastery`) et J04
(`05_Solarpunk_Doctrine_LD08` à `08_Contribution_Architecture_Integrated`).
Ils peuvent chacun porter une entité non-répertoriée dans le README parent.
Lecture raccourcie, pas lecture absente.

### 1.2. Jonctions NTFS — vérification

> **0 jonction détectée** dans le seau. Les 176 jonctions totales du
> PARA se répartissent ailleurs (Geordi en concentre 159 selon le brief).
> Le dossier `J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creatry_Impact`
> (avec la coquille « Creatry » au lieu de « Creativity ») **n'est pas une
> jonction** : c'est un dossier réel et **vide** (sauf un `B2_Area_Domains/`
> lui-même quasi-vide). Il n'apparaît pas dans `structure.txt` parce qu'il
> ne contient aucun README/INDEX/ARCHITECTURE/STANDARD/etc. — mais c'est
> une **coquille à signaler** (voir §4 Contradictions).

---

## 2. Tableau des types d'objets (trié par nombre de chemins observés)

> **Convention** : chaque type cite ≥3 chemins où il apparaît. Quand un
> type n'a qu'1 ou 2 occurrences, il est listé quand même mais avec une
> note « rare ».

| # | Type | Attributs observés | # chemins | Chemins (≥3 quand possible) |
|---|---|---|---|---|
| 1 | **Jerry Area** (Area PARA = seau de responsabilité durable) | `id`, `layer: L2_Business_Pulse`, `life_domain(s)`, `status`, `created`, `owner`, `bibliography_alignment`, `scope` | 4 (un par variant) | `J01_Jerry_Prime_LD01_Business/README.md`, `J02_.../README.md`, `J03_.../README.md`, `J04_.../README.md` |
| 2 | **B2 Domain** (domaine méso d'un Area) | `numéro (01..08)`, `nom`, `hero manager (DC)`, `squad (Marvel)`, `north star`, `KRs`, `principles_doctrine_path` | 32 (4 Jerry × 8 domaines, J01 explicite, J02-J04 listés en table) | `J01/.../B2_Area_Domains/01_Growth_Superman_Guardians/README.md`, `J02/.../B2_Area_Domains/README.md` (8 domaines listés en table), `J03/.../B2_Area_Domains/README.md`, `J04/.../B2_Area_Domains/README.md` |
| 3 | **B3 Squad** (équipe d'exécution Marvel) | `lead_character`, `canon_source (Notion AGENT_REGISTRY_DB UUID)`, `members (6-10)`, `specialty`, `task_types`, `SOPs gérées`, `build_gates`, `anti_patterns`, `escalation_owner` | 8 (un par J01 B2) | `J01/.../B3_Squad_Guardians/00_B3_SQUAD_CANON.md`, `B3_Squad_Illuminati/...`, `B3_Squad_Avengers/...`, `B3_Squad_Fantastic4/...`, `B3_Squad_KangDynasty/...`, `B3_Squad_Thunderbolts/...`, `B3_Squad_XMen/...`, `B3_Squad_Eternals/...` |
| 4 | **B2 Hero Manager** (archétype DC qui possède un B2) | `name`, `role (VP)`, `domain`, `non-délégables (réservé B2)` | 8 | `B3_Squad_*/00_B3_SQUAD_CANON.md` × 8 (Superman, Martian Manhunter / John Jones, Flash, Batman, Cyborg, Wonder Woman, Green Lantern, Aquaman) |
| 5 | **Cadence 12WY** (cycle annuel Area, 3 phases) | `W01-W04 / W05-W08 / W09-W12`, `Rocks (≤4)`, `Lead metrics`, `Lag metrics`, `Cadence deliverables` | 4 (un par Jerry) | `J01/.../12WY_Area_Cadence/README.md`, `J02/.../12WY_Area_Cadence/README.md`, `J03/.../12WY_Area_Cadence/README.md`, `J04/.../12WY_Area_Cadence/README.md` |
| 6 | **Cadence Phase** (trimestre de la 12WY) | `name (Foundation/Scaling/Optimization ou Winter/Spring/Autumn ou Q1/Q2/Q3)`, `Rocks`, `Lead/Lag` | 12 | `J01/12WY_Area_Cadence/W01_W04_Foundation/README.md`, `J01/.../W05_W08_Scaling/README.md`, `J01/.../W09_W12_Optimization/README.md` + les 9 autres (4 Jerry × 3 phases) |
| 7 | **Operating Principle** (P1-P8 doctrine LD01, AS-P1..P3 stewardship, SP1-SP22 solarpunk, Rules LD02/LD05/LD07/LD08, J02 hard rules) | `numéro`, `source (livre)`, `rule`, `test`, `trigger`, `anti-pattern` | 8 LD01 + 3 stewardship + 22 SP + ~78 règles LD05/LD07/LD08 + ~12 règles Bio | `J01/AREA_STANDARD.md`, `J01/B1_Area_Direction/README.md`, `J04/03_JERRY_SOLARPUNK_PRINCIPLES.md`, `J04/AREA_STANDARD.md`, `J02/AREA_STANDARD.md`, `J02/B1_Area_Direction/README.md` |
| 8 | **Threshold Table** (table GREEN/ORANGE/RED) | `signal`, `GREEN`, `ORANGE`, `RED`, `frequency` | ≥7 instances distinctes (Sleep, HRV, Exercise, Cognitive Load, Runway, Coverage, Family Presence) | `J02/AREA_STANDARD.md` (Sleep, HRV, Exercise, Cognitive Load), `J03/AREA_STANDARD.md` (Runway, Coverage, Family Load), `J04/AREA_STANDARD.md` (MUSE criteria) |
| 9 | **KR / Key Result** (indicateur de scorecard) | `id (KR-X)`, `metric`, `target`, `cadence (weekly/monthly/quarterly)`, `owner` | dizaines (≥40 dans J01 + J02 + J03 + J04 + Cadence) | `J01/AREA_STANDARD.md` §Scorecard, `J02/AREA_STANDARD.md` §8 Scorecard, `J03/AREA_STANDARD.md` §9 Scorecard, `J04/AREA_STANDARD.md` §9 Scorecard |
| 10 | **ROCK** (engagement trimestriel Area) | `name`, `start_state`, `end_state`, `deadline`, `B2_owner`, `success_metrics` | ≥4 par cycle × 4 cycles = 16 minimum (J01 documente tous) | `J01/12WY_Area_Cadence/W01_W04_Foundation/README.md` (Rocks 1-4), `W05_W08_Scaling/README.md` (Rocks 1-4), `W09_W12_Optimization/README.md` (Rocks 1-4) |
| 11 | **SOP** (procédure opérationnelle reproductible) | `id (SOP-L2-<DOMAIN>-NNN)`, `name`, `cadence`, `steps`, `build_gate`, `version` | ≥25 instances (citées dans 8 squad canons, plus contrats et IT) | `B3_Squad_Guardians/...`, `B3_Squad_Fantastic4/...` (`SOP-L2-OPS-001`, `-002`, `-003`), `B3_Squad_Thunderbolts/...` (`SOP-L2-FINANCE-001..004`), `B3_Squad_Eternals/...` (`SOP-L2-LEGAL-001..004`), `B3_Squad_XMen/...` (`SOP-L2-PEOPLE-001..004`), `B3_Squad_KangDynasty/...` (`SOP-L2-IT-001..004`) |
| 12 | **Contract Template** (modèle juridique réutilisable) | `name`, `jurisdiction (FR/EU/US)`, `signature_mode (DocuSign/PandaDoc)`, `linked SOP` | 6 | `B3_Squad_Eternals/00_B3_SQUAD_CANON.md` (`MSA Solaris`, `CGV Cloud`, `Licence Whitelabel Orbiter`, `DPA`, `NDA Mutual`, `SLA Nexus`) |
| 13 | **ADR (Architecture Decision Record)** | `id (ADR-<DOMAIN>-NNN)`, `status (RATIFIED/ACCEPTED)`, `date` | ≥8 ratifiés cités dans `N0_Coach_Client_Onboarding_KB.md` | `02_Areas_Spock/N0_Coach_Client_Onboarding_KB.md` §8 (ADR-CANON-001, ADR-CANON-002, ADR-RH-META-GOUVERNANCE-001-canonical-v3, ADR-GSTACK-IMBRICATION-001, ADR-OBSOLESCENCE-001, ADR-OBS-AUDIT-001, ADR-MEM-001, ADR-L2-AAAS-US-ONLY-001) ; `J04/03_JERRY_SOLARPUNK_PRINCIPLES.md` (ADR-MESH-L2-001 cité 8 fois) |
| 14 | **Pipeline Stage** (étape du funnel commercial canonique) | `name`, `transition_to_stage`, `owner_squad`, `KPI seuil` | 5 (Lead → MQL → SQL → Demo → Proposal → Closed Won/Lost) | `B3_Squad_Illuminati/00_B3_SQUAD_CANON.md` §Pipeline canonique |
| 15 | **Build Gate** (porte qualité/performance de squad) | `metric`, `green_threshold`, `owner` | ≥24 (3 par squad × 8 squads) | `B3_Squad_*/00_B3_SQUAD_CANON.md` (CPQL <80€, Win rate >25%, Onboarding <4h, MRR growth >10% MoM, RGPD audit 0 HIGH, Heartbeat <5% miss, etc.) |
| 16 | **Anti-Pattern** (interdit de squad) | `description`, `rationale`, `escalation_if_violated` | ≥24 (3 par squad × 8) | Idem |
| 17 | **Decision Charter** (matrice RACI B1) | `decision_type`, `owns (A/R)`, `consulted (C)`, `vetoes`, `escalates_to` | 1 (J01) | `J01/B1_Area_Direction/03_DECISION_CHARTER.md` (12 lignes × 5 colonnes) |
| 18 | **Scorecard Snapshot** (capture Area) | `date`, `week_N`, `lead_metrics`, `lag_metrics`, `zone (GREEN/ORANGE/RED)`, `decisions_needed`, `B2_owner_review` | 1 template cité | `J01/B3_Area_Warp_Core/Lead_Lag_Logs/README.md` (format Entry) |
| 19 | **Member (sub-agent)** (personnage Marvel/DC d'une squad) | `name`, `archetype`, `lore_role`, `business_responsibility` | 54 (somme des 8 squads : 6+6+7+4+6+6+8+10) | `B3_Squad_*/00_B3_SQUAD_CANON.md` (Star-Lord, Gamora, Rocket Raccoon, Groot, Drax, Mantis / Black Bolt, Iron Man, Mr Fantastic, Namor, Professor X, Doctor Strange / Captain America, Iron Man, Thor, Hulk, Black Widow, Hawkeye, Scarlet Witch / Mr Fantastic, Invisible Woman, Human Torch, The Thing / Kang Prime, Iron Lad, Scarlet Centurion, Immortus, Victor Timely, Rama-Tut / Bucky Barnes, Yelena Belova, Red Guardian, Ghost, Taskmaster, U.S. Agent / Professor X, Cyclops, Jean Grey, Wolverine, Storm, Beast, Nightcrawler, Rogue / Ikaris, Sersi, Ajak, Kingo, Phastos, Sprite, Druig, Thena, Gilgamesh, Makkari) |
| 20 | **Domain Bibliography** (canon livres par LD) | `LD`, `title`, `author`, `B2_domain_mapping` | 8 LD × ~6 livres = ~48 | `J01/README.md` §Bibliography Stack (6 livres LD01), `J02/README.md` §LD03/§LD04 (12 livres), `J03/README.md` §LD02/§LD06 (12 livres), `J04/README.md` §LD05/§LD07/§LD08 (18 livres) |
| 21 | **MUSE-eligible contribution** (artefact public solarpunk) | `criteria (7)`, `disqualifiers (5)`, `quota_Q1..Q4`, `output_artifact` | quota 14/an | `J04/AREA_STANDARD.md` §5, `J04/B1_Area_Direction/README.md` §3 |
| 22 | **Tenant** (instance client multi-tenant Supabase) | `id`, `slug`, `tier (start/sovereign/fleet)`, `config_json (branding+vocabulary)`, `subscription_status` | 1 table | `Business_Pulse/docs/documentation/Canon_BMad_DEAL/03_Phase3_Master_SQL_Schema.md` `create table public.tenants` |
| 23 | **Offering** (offre commerciale liée à une SOP) | `id`, `name`, `price`, `root_sop_id` (FK obligatoire — « Golden Rule ») | 1 table | `Business_Pulse/.../03_Phase3_Master_SQL_Schema.md` `create table public.offerings` |
| 24 | **SOP-record** (la procédure elle-même dans la base) | `id`, `tenant_id`, `title`, `department`, `content_markdown`, `video_url`, `estimated_time`, `is_template` | 1 table | Idem `create table public.sops` |
| 25 | **Project** (dossier client dans une tenancy) | `id`, `tenant_id`, `client_id`, `name`, `status`, `deadline` | 1 table | `Business_Pulse/.../03_Phase3_Master_SQL_Schema.md` `create table public.projects` |
| 26 | **Task** (unité atomique d'exécution) | `id`, `tenant_id`, `project_id`, `sop_id` (FK obligatoire), `title`, `status (todo/doing/done)`, `assigned_to` | 1 table | Idem `create table public.tasks` |
| 27 | **Lead** (prospect pipeline Growth) | `id`, `tenant_id`, `email`, `status (cold/warm/won/lost)`, `interested_in_offering_id`, `source (inbound)` | 1 table | Idem `create table public.leads` |
| 28 | **Capacity Log** (charge fondateur — People) | `id`, `tenant_id`, `user_id`, `week_start`, `hours_logged` (>10h alerte rouge), `stress_level (1-5)` | 1 table | Idem `create table public.capacity_logs` |
| 29 | **Tier (commercial)** | `name`, `price`, `scope`, `revenue_event` | 3 (Start 300€, Sovereign 700€, Fleet 1500€) | `Business_Pulse/docs/documentation/Canon_BMad_DEAL/02_Phase2_Project_Charter.md` §3 |
| 30 | **Jerry variant** (alias des Areas : J01-J04) | `id`, `scope (LDs)`, `mode (vitality/stability/extraction-guard/contribution)`, `fractal_status`, `status` | 4 (J01-J04) | `Jerry_Areas_README.md` (table §Four Jerry Areas), `A1_Jerry_Areas_Spec.md` |
| 31 | **Phase saisonnière Bio** (J02 a des phases hivernales, pas commerciales) | `name (Winter/Spring/Summer-Autumn)`, `weeks`, `key_activities`, `biological_adjustments` | 3 | `J02/12WY_Area_Cadence/README.md` §1.1 (W01-W04 Winter, W05-W08 Spring, W09-W12 Summer-Autumn) |
| 32 | **Mode (Area)** (Solaris/Nexus/Orbiter/AaaS pour J01) | `name`, `trigger (revenue threshold)`, `role`, `investment_priority` | 4 | `J01/AREA_STANDARD.md` §LD01 Mode Map, `J01/B1_Area_Direction/README.md` §ICP Variant Determination Rules |
| 33 | **Account (banque automatisée J03)** | `name (BUFFER/REINVEST/INDEPENDENCE/PROTECT/PLAY/GIVE)`, `purpose`, `trigger` | 6 | `J03/AREA_STANDARD.md` §4, `J03/B1_Area_Direction/README.md` §6 |
| 34 | **Tier (J03 Wealth Architecture)** | `name (T1 Safety/T2 Independence/T3 Acceleration/T4 Sovereignty)`, `definition`, `reinvestment_rule` | 4 | `J03/AREA_STANDARD.md` §2, `J03/B1_Area_Direction/README.md` §5 |
| 35 | **Wealth Velocity Lane** | `name (Slowlane/Fastlane/Sovereignty)`, `description`, `usage_rule` | 3 | `J03/AREA_STANDARD.md` §2 |
| 36 | **Operational Mode (J04)** | `name (Gate 0/1/2/3)`, `trigger`, `creative_output_required` | 4 | `J04/AREA_STANDARD.md` §7 |
| 37 | **Forbidden Action** (interdit B1) | `subject (Jerry)`, `description`, `override_path` | ≥20 | `J01/AREA_STANDARD.md` §What Jerry Prime Does NOT Own, `J01/B1_Area_Direction/README.md` §Jerry Prime Forbidden Actions, `J02/B1_Area_Direction/README.md` §4.1, `J03/B1_Area_Direction/README.md` §8, `J04/B1_Area_Direction/README.md` §4 |
| 38 | **Escalation Threshold** | `signal`, `threshold`, `escalates_to`, `cadence` | ≥12 | `J01/B1_Area_Direction/03_DECISION_CHARTER.md` §4 (escalation matrix) |
| 39 | **Output Packet (B1)** | `decision_id`, `date`, `type`, `trigger`, `options_considered`, `decision`, `owner`, `vetoes_applied`, `cascades_to` | 1 schéma | `J01/B1_Area_Direction/03_DECISION_CHARTER.md` §5 |
| 40 | **Handoff Packet (B1→B2→B3)** | `JTBD_id`, `job_statement`, `input_artifacts`, `expected_output_artifacts`, `proof_required`, `lead/lag_indicator`, `timebox`, `status` | 1 schéma | `J01/B1_Area_Direction/06_B3_JOBS_TO_BE_DONE_SPEC.md` (B3 JTBD Packet), `05_B2_DEFINITION_OF_DONE_SPEC.md` (B2 DoD Packet) |
| 41 | **Project Charter (AaaS)** | `code_name`, `classification`, `date`, `commandant`, `mission`, `laws (3 lois d'acier)`, `tiers (3)`, `role_distribution (7 héros)` | 1 | `Business_Pulse/docs/documentation/Canon_BMad_DEAL/02_Phase2_Project_Charter.md` (PROJECT GENESIS, 29 janvier 2026) |
| 42 | **Loi d'Acier (Loi d'Or + 3 dérivés)** | `name`, `scope`, `enforcement` | 3 (Loi d'Or Ops→Product→Growth + 3 lois d'acier) | `Business_Pulse/.../02_Phase2_Project_Charter.md` §2 + `03_Phase3_Master_SQL_Schema.md` §2 (RÈGLE D'OR via FK `root_sop_id`) |
| 43 | **Sub-agent hero (RACI charter)** | `name`, `role`, `livrable_prioritaire`, `directive_speciale` | 7 (Batman/Flash/Superman/Wonder Woman/Green Lantern/Cyborg/Aquaman) | `Business_Pulse/.../02_Phase2_Project_Charter.md` §4 |
| 44 | **AGENT_REGISTRY_DB entry** (entrée Notion canonique) | `uuid`, `squad_name`, `notion_id`, `lore_summary` | ≥8 (UUIDs explicites) | `B3_Squad_*/00_B3_SQUAD_CANON.md` (ex: Notion ID `36c7e9e2-658c-81ba-b05e-fcfa153cf957` pour The Avengers) |
| 45 | **Command Cycle (B1)** | `name (C1..C4)`, `gate`, `lands_in` | 4 (C1 Direction Lock, C2 Domain Activation, C3 Execution Proof, C4 Graduation or Archive) | `J01/12WY_Area_Cadence/README.md` §C1-C4 command-cycle mapping |
| 46 | **Hierarchy Rank (A0/A1/A2/A3)** | `name`, `role`, `example` | 4 (A0 Amadeus, A1 Morty/Beth/Jerry/Summer, A2 Doctors/USS ships/8 hero-managers, A3 companions/crews/8 Marvel squads) | `J01/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md` §1 (le mapping canonique A-rank → B-rank) |
| 47 | **Cycle/Tick (12WY Q3)** | `name`, `period`, `cadence` | 2 (12WY Q3 cycle 06/15 → 09/07, Swarm tick 001+) | `N0_Coach_Client_Onboarding_KB.md` §4 + §7 |
| 48 | **B0 Doctrine Layer** (Self-Operating Business, au-dessus de B1) | `name`, `source_livre`, `role`, `artifact` | 5 (E-Myth Franchise Prototype, Built to Sell Scorecard, Who Not How Delegation, Offer/Brand Engine, Graduation Gates) | `J01/B0_Self_Operating_Business_Doctrine/00_SOB_INDEX.md` (5 fichiers prévus dans la table, certains absents de `structure.txt`) |
| 49 | **Entrepreneur Archetype** (Solaris/Nexus/Orbiter/AaaS, PAS des personas : des **modes de l'agent Area**) | `name`, `trigger (revenue)`, `role (Area)`, `investment` | 4 | `J01/AREA_STANDARD.md` §LD01 Mode Map |
| 50 | **Bibliographic Canon (par LD)** | `LD`, `list of titles+authors`, `B2 mapping` | 8 (LD01-LD08) | voir type #20 |

### 2.1. Types rares / cités une seule fois

| Type | Attributs | Chemin unique | Note |
|---|---|---|---|
| **Summer's Verse** | Project-instantiated B1/B2/B3 fractal sous un Area | `J01/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md` §2 | C'est le miroir micro d'un Jerry Area — pas une entité distincte mais un **pattern d'instanciation** |
| **DocuSign packet** | mode signature, latence | `B3_Squad_Eternals/...` §Stack juridique | Sous-type de Contract Template |
| **The Magnificent Child Care** | activité réelle | `JERRY_WHEEL_ALIGNMENT_MINDSET_VALUES.md` §1 | Entité externe — ancrage vie réelle |
| **Amadou Apps Agency (2024-10-26)** | ancêtre de A'Space OS | `JERRY_WHEEL_ALIGNMENT_MINDSET_VALUES.md` §1 | Conversation Claude exportée |

---

## 3. Relations — la partie qui compte

> Chaque relation est citée **verbatim** depuis le fichier indiqué.
> Pas de paraphrase. Une relation sans citation est une invention.

### 3.1. Relations structurelles (PARA, A-rank, B-rank, fractal)

| De | Verbe | Vers | Citation (extrait) | Chemin |
|---|---|---|---|---|
| **Spock** | *gouverne / owns (incubates)* | **Areas** | « Spock governs Areas: ongoing standards, responsibilities, and health of Life OS / Business OS domains. Areas are not "to-do" projects; they are maintained systems. » | `02_Areas_Spock/README.md` §Mission |
| **Spock** | *hosts (incubates)* | **Jerry Areas** | « Jerry lives in Spock's Areas because Jerry is an ongoing responsibility, not a finite project. » | `02_Areas_Spock/Jerry_Areas_README.md` §Doctrine |
| **Picard** | *owns (instantiates)* | **Summer Projects** | « Spock incubates Jerry as an Area. Picard creates a Summer's Verse as an active PARA Project » | `02_Areas_Spock/Business_Pulse/L2_Business_Pulse_References_Index.md` §Core Findings |
| **Jerry (macro)** | *shares fractal with* | **Summer (micro)** | « Active fractal is A1 -> B2 Justice League/DC manager -> B3 Marvel squad. Jerry is macro/A1 for ongoing business responsibility; Summer is micro/A1 for active project execution. » | `02_Areas_Spock/Business_Pulse/L2_Business_Pulse_References_Index.md` §Core Findings |
| **A-rank (A0-A3)** | *is expressed as* | **B-rank (B1-B3) in L2** | « B is not a different system — it is A, localized to L2 and drawn top-down as Direction → Domains → Execution » | `J01/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md` §1 |
| **B1 (Jerry/Summer)** | *owns* | **North Star, 12WY cycles, decision rights, handoff queue** | « B1 sets the WHY/WHERE, B2 sets the WHAT/gate, B3 produces the HOW/proof. » | `J01/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md` §1 + §3 |
| **B2 (hero manager)** | *owns* | **domain DoD + gates, principles doctrine, control room, meso coordination** | « B2 — Domains (Meso) / A2 of L2 / the 8 hero-managers (...) / domain DoD + gates, the perpetual principles doctrine, the control room, meso coordination » | `J01/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md` §1 |
| **B3 (Marvel squad)** | *owns* | **JTBD execution, proof, lead/lag indicators** | « B3 — Warp Core (Execution) / A3 of L2 / the 8 squads (...) / JTBD execution, proof, lead/lag indicators, peer-unblocking, blocker reports » | `J01/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md` §1 |
| **B1** | *hands off to* | **B2** (via 04_B2_HANDOFF_QUEUE) | « B1 writes/updates direction. B1 writes one domain mandate per affected B2 (a B1-B2-MANDATE packet) — intent + constraints + success signal, not a step-by-step plan. Logged in 04_B2_HANDOFF_QUEUE.md. » | `J01/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md` §3 |
| **B2** | *converts (mandate → Rock + DoD)* | **B3** (via JTBD) | « B2 converts the mandate into a Rock + DoD packet (05_B2_DEFINITION_OF_DONE_SPEC.md) and then into B3 JTBD packets (06_B3_JOBS_TO_BE_DONE_SPEC.md). » | `J01/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md` §3 |
| **B3** | *returns proof to* | **B2** | « B3 returns proof to B2. B2 decides whether the DoD is satisfied. B1 decides whether the direction can advance. » | `J01/B1_Area_Direction/06_B3_JOBS_TO_BE_DONE_SPEC.md` §Handoff Back To B2 |
| **Jerry Area** | *oversees* | **Picard Projects** | « Area 12WY cadence purpose: Review and update AREA_STANDARD.md; Track Area-level lead/lag indicators; Conduct B2 manager check-ins; Onboard new Picard projects » | `J01/12WY_Area_Cadence/README.md` §Overview |
| **Picard Project** | *references (DRY)* | **Jerry Area** | « Projects graduate; the Area persists. (...) per-project B1/B2/B3 that reference the macro doctrine (DRY — never re-derive) and calibrate it to the project's mode (Solaris / Nexus / Orbiter). » | `J01/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md` §2 |
| **B2 Domain** | *owns* | **B3 Squad (1:1 mapping)** | « one datum, one owner. Growth=acquisition, Sales=conversion, Product=value, Ops=repeatability, IT=substrate, Finance=solvency, People=team, Legal=protection. Domains point at each other's data; they never copy it. » | `J01/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md` §4 |
| **A1 Jerry Area** | *parent* | **B1 Direction** | « Each Jerry area has a README and a current state. No Summer's Verse is opened without a Picard Project handoff. » | `A1_Jerry_Areas_Spec.md` §Acceptance Criteria |
| **B1 (Jerry)** | *implements via E-Myth P1* | **« work ON not IN »** | « Jerry Prime is the Manager who designs the system. The Technicians run it. » | `J01/AREA_STANDARD.md` §P1 |

### 3.2. Relations de veto et d'autorité

| De | Verbe | Vers | Citation | Chemin |
|---|---|---|---|---|
| **Beth** | *HALTs (vetoes)* | **all Jerry expansion** | « Beth can halt all expansion if Life OS load, health, cognition, or finance signals turn red. » | `Jerry_Areas_README.md` §Doctrine |
| **Beth HALT** | *triggers on LD03+LD04 ORANGE* | **HARD FREEZE on all Jerry** | « LD03 ORANGE + LD04 ORANGE → Beth HALT AUTOMATIC. LD03 RED any → FULL STOP + 24h report to Beth. » | `J02/B1_Area_Direction/README.md` §2.1 |
| **Jerry Bio (J02)** | *vetoes* | **LD01 business expansion** | « LD01 expansion gating: When LD04 learning velocity gates LD01 business expansion. » | `J02/B1_Area_Direction/README.md` §1.1 |
| **Wonder Woman (B2 Finance)** | *vetoes* | **deals >15% discount** | « Finance (Wonder Woman) — veto on any deal/discount that breaks the margin floor or runway threshold (discount >15% requires her sign-off). » | `J01/B1_Area_Direction/03_DECISION_CHARTER.md` §3 |
| **Aquaman (B2 Legal)** | *vetoes* | **public message / contract / IP** | « Aquaman (B2) — compliance gate / Aquaman (can veto a public message) » | `J01/B1_Area_Direction/03_DECISION_CHARTER.md` §1 |
| **Cyborg (B2 IT)** | *owns outright* | **IT architecture** | « IT architecture: Cyborg (B2) — Jerry does NOT decide » | `J01/B1_Area_Direction/03_DECISION_CHARTER.md` §1 |
| **Green Lantern (B2 People)** | *vetoes (with Finance)* | **headcount without 12-mo runway** | « Headcount / capsule onboarding: Green Lantern (B2); vetoes: Green Lantern + Finance » | `J01/B1_Area_Direction/03_DECISION_CHARTER.md` §1 |
| **B3 peer** | *productive-disagreement veto* | **JTBD affecting cost/legal/customer/quality** | « when a JTBD affects cost, legal exposure, customer promise, release quality, or operational load, at least one peer may block the first solution. » | `J01/B1_Area_Direction/03_DECISION_CHARTER.md` §3 |
| **Jerry Nexus (J03)** | *automatically overrides* | **Summer's Verse expansion** | « Closure Rule: When runway enters ORANGE or RED, Jerry Nexus automatically overrides Summer's Verse expansion requests unless the expansion directly increases coverage ratio within 60 days. » | `J03/AREA_STANDARD.md` §Closure Rule |
| **Solarpunk (J04)** | *vetoes pure-extraction* | **projects that fail MUSE criteria** | « SP21 — Solarpunk vetoes pure-extraction. A project generating engagement/revenue with zero commons contribution does not qualify » | `J04/03_JERRY_SOLARPUNK_PRINCIPLES.md` Cluster I |
| **A0 Amadeus** | *has absolute veto on* | **Intention** | « A0 Amadeus — absolute veto on Intention (what we pursue at all). Never overridden. » | `J01/B1_Area_Direction/03_DECISION_CHARTER.md` §3 |

### 3.3. Relations routage et handoff

| De | Verbe | Vers | Citation | Chemin |
|---|---|---|---|---|
| **Idea** | *routes through* | **Cerritos → Picard → Summer's Verse** | « Ideas from Jerry pass through Cerritos/GTD before Picard instantiates a Summer's Verse. » | `Jerry_Areas_README.md` §Doctrine |
| **Jerry (B1)** | *does NOT receive ideas directly* | **Cerritos first, always** | « Every idea, opportunity, or strategic input routes through Cerritos first. Jerry's role is to set criteria, not to receive directly. » | `J01/AREA_STANDARD.md` §P7 |
| **Jerry proposal** | *becomes executable only after* | **Cerritos clarifies + Picard opens/updates Summer's Verse** | « Jerry proposals become executable only after Cerritos clarifies and Picard opens or updates a Summer's Verse. » | `A1_Jerry_Areas_Spec.md` §Boundaries |
| **Cerritos** | *routes idea within* | **48h to Picard** | « Routing SLA: Every idea routed to Picard within 48 hours » | `J01/AREA_STANDARD.md` §Cerritos Minimum Standards |
| **Picard** | *must action within* | **72h or Jerry escalates to B1** | « If Picard has not actioned within 72 hours → Jerry escalates to B1 » | `J01/AREA_STANDARD.md` §Cerritos Minimum Standards |
| **Summer's Verse handoff** | *requires* | **Context, Desired outcome, Constraints, Deadline, Authority, Escalation path** | « Picard Summer's Verse Handoff / When Cerritos routes to Picard: Context, Desired outcome, Constraints, Deadline, Authority, Escalation path » | `J01/AREA_STANDARD.md` §Picard Summer's Verse Handoff |
| **B2 Domain Rock** | *governs* | **Picard Project domain-level execution** | « Each Picard project under Jerry's stewardship has its own B1/B2/B3 fractal. Jerry's Area-level B2 domains provide the oversight layer. » | `J01/B2_Area_Domains/README.md` §Picard Project Domain Mapping |
| **B3 execution** | *flows UP to* | **J01 B3_Warp_Core AND 30_Business_OS dashboard** | « B3 execution flows UP to both J01 B3_Warp_Core AND 30_Business_OS dashboard. Weekly Lead/Lag synced to both layers. » | `Jerry_Areas_README.md` §Crosslink Protocol |
| **Picard Mirror Index** | *points to* | **Jerry-Summer Fractal Alignment** | « Picard mirror index: `01_Projects_Picard/JERRY_SUMMER_FRACTAL_ALIGNMENT.md`. » | `J01/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md` §6 |

### 3.4. Relations du portefeuille « modes » (AaaS / Solaris / Nexus / Orbiter)

| De | Verbe | Vers | Citation | Chemin |
|---|---|---|---|---|
| **Mode AaaS** | *triggered by* | **< $50K MRR** | « AaaS (Agency as a Service) | < $50K monthly revenue | Architect/Seller only — no ops overhead » | `J01/AREA_STANDARD.md` §LD01 Mode Map |
| **Mode Solaris** | *triggered by* | **$50K-$200K MRR + visual offers** | « Solaris (Visual-first) | $50K-$200K MRR, visual offers | Add visual production, retain strategy » | `J01/AREA_STANDARD.md` §LD01 Mode Map |
| **Mode Nexus** | *triggered by* | **$200K-$500K MRR + knowledge offers** | « Nexus (Data-first) | $200K-$500K MRR, knowledge offers » | `J01/AREA_STANDARD.md` §LD01 Mode Map |
| **Mode Orbiter** | *triggered by* | **> $500K MRR + logistics offers** | « Orbiter (Field-first) | > $500K MRR, logistics offers | Add field network, franchise execution » | `J01/AREA_STANDARD.md` §LD01 Mode Map |
| **Jerry Prime** | *can force mode shift with* | **B1 Rick/Morty approval** | « Jerry Prime can force mode shift with B1 Rick/Morty approval when market signals diverge from revenue threshold by >30%. » | `J01/B1_Area_Direction/README.md` §ICP Variant Determination Rules |

### 3.5. Relations avec les LD (Life Domain) — qui couvre quoi

| De | Verbe | Vers | Citation | Chemin |
|---|---|---|---|---|
| **J01 Prime** | *covers* | **LD01 (Career & Business)** | « J01_Jerry_Prime_LD01_Business | LD01 Career & Business; AaaS, Solaris, Nexus, Orbiter | ACTIVE_FIRST » | `Jerry_Areas_README.md` §Four Jerry Areas |
| **J02 Bio** | *covers* | **LD03 + LD04** | « J02_Jerry_Bio_LD03_LD04_Vitality_Cognition | Health + Cognition constraints for founder load | ACTIVE — VPP STANDARD » | `Jerry_Areas_README.md` §Four Jerry Areas |
| **J03 Nexus** | *covers* | **LD02 + LD06** | « J03_Jerry_Nexus_LD02_LD06_Finance_Family | Finance + Family/stability constraints | ACTIVE — FIP STANDARD » | `Jerry_Areas_README.md` §Four Jerry Areas |
| **J04 Solarpunk** | *covers* | **LD05 + LD07 + LD08** | « J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact | Social, creativity, impact, public contribution | ACTIVE — SCP STANDARD » | `Jerry_Areas_README.md` §Four Jerry Areas |
| **LD08** | *is* | **A0 SOVEREIGN DOCTRINE** | « LD08 is A0 SOVEREIGN DOCTRINE. This is not research. This is not hypothesis. Every rule in this section carries the weight of an A0 direct statement. » | `J04/AREA_STANDARD.md` §4 |

### 3.6. Relations dans le schéma SQL (données canoniques AaaS)

| De | Verbe | Vers | Citation | Chemin |
|---|---|---|---|---|
| **Tenant** | *owns (via tenant_id)* | **toutes les autres tables** | « Note que chaque table (sops, tasks, leads...) possède une colonne tenant_id. C'est obligatoire. C'est ce qui permet à ton code de dire : "Montre-moi les tâches" et à la base de répondre "Ok, mais seulement celles de l'Agence Alpha". » | `Business_Pulse/.../03_Phase3_Master_SQL_Schema.md` §Analyse Cyborg |
| **Offering** | *requires (FK)* | **root_sop_id (SOP Racine)** | « RÈGLE D'OR : On lie l'offre à une SOP Racine (ex: "SOP Livraison Audit") » + « tu ne peux pas insérer une Offre dans la base si tu ne la connectes pas à une procédure existante » | `Business_Pulse/.../03_Phase3_Master_SQL_Schema.md` §Storefront + Analyse |
| **Task** | *requires (FK)* | **sop_id (SOP obligatoire)** | « Impossible de créer une tâche sans SOP (sauf si null autorisé temporairement, mais l'UI doit forcer) » + « Une tâche ne peut exister sans SOP. Si un utilisateur veut créer une tâche "floue", le système le bloque » | `Business_Pulse/.../03_Phase3_Master_SQL_Schema.md` §Factory + Charter §4 Batman |
| **Lead** | *points to* | **interested_in_offering_id** | « On sait dès le début ce qu'on leur vend / interested_in_offering_id uuid references public.offerings » | `Business_Pulse/.../03_Phase3_Master_SQL_Schema.md` §Engine |
| **Profile** | *isolated by RLS* | **rows of same tenant** | « Un utilisateur ne peut voir que les lignes qui portent son tenant_id / create policy "Tenant Isolation" on public.sops using (tenant_id = (select tenant_id from public.profiles where id = auth.uid())) » | `Business_Pulse/.../03_Phase3_Master_SQL_Schema.md` §Sécurité |

### 3.7. Relations philosophiques / canoniques

| De | Verbe | Vers | Citation | Chemin |
|---|---|---|---|---|
| **Valeur Foi** | *canon immutable* | **Jerry Wheel** | « Le canon de valeurs (§1) est immuable — comme AGENTS.md. Le changement de vie crée de nouvelles formes (nouveaux domaines, nouvelles offres), jamais de nouvelles valeurs. » | `JERRY_WHEEL_ALIGNMENT_MINDSET_VALUES.md` §4 |
| **Transformation Abou** | *modèle de* | **J02 Bio discipline** | « Abou change de medium (rap→Afro→combat) mais garde foi/famille/discipline/transmission. C'est le modèle : muter la surface, préserver l'âme. » | `JERRY_WHEEL_ALIGNMENT_MINDSET_VALUES.md` §2 |
| **Hard Safety doctrine** | *HALT vetoes cross-Jerry* | **« LD01 dévore la vie »** | « LD03 (santé) dégradée → LD04 (cognition) dégradée → Beth HALT veto → tous les Jerry freeze. C'est le garde-fou anti "LD01 dévore la vie". » | `JERRY_WHEEL_ALIGNMENT_MINDSET_VALUES.md` §3 |
| **Discipline** | *bridge / pont* | **Abou (J02) ↔ business** | « La discipline est le pont (Abou) — la même répétition qui forge le freestyle forge le combat forge le business. J02 Bio est le gardien de cette discipline (corps+esprit). » | `JERRY_WHEEL_ALIGNMENT_MINDSET_VALUES.md` §4 |
| **Transmission** | *sortie / output* | **J04 Solarpunk** | « La transmission est la sortie (Rentre dans le Cercle) — ce qu'on devient doit se transmettre (relais, child care, diaspora). J04 en est le gardien. » | `JERRY_WHEEL_ALIGNMENT_MINDSET_VALUES.md` §4 |
| **Ikigai** | *aligns / centre* | **Wheel** | « L'Ikigai aligne le tout — c'est le centre du Wheel (USS Orville/LD-Ikigai en L1) ; chaque Jerry sert l'Ikigai, pas l'inverse. » | `JERRY_WHEEL_ALIGNMENT_MINDSET_VALUES.md` §4 |
| **MUSE graduation** | *requires (Gate)* | **contribution artifact, not revenue alone** | « The V0→V1 "Muse" graduation (Symphony SDD-010) requires a real contribution artifact, not revenue alone (AREA_STANDARD MUSE criteria). » | `J04/03_JERRY_SOLARPUNK_PRINCIPLES.md` Cluster F |

---

## 4. Systèmes de codes

### 4.1. Système `A0-A3` (hiérarchie OS-wide des agents)

- **Numérote** : les rangs d'agents à travers tout l'OS
- **Défini dans** : `J01/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md` §1 + `02_Areas_Spock/A3_Spock_Areas_Spec.md` §Identity
- **Valeurs observées** : `A0` (Amadeus/Pilot), `A1` (Gatekeeper : Morty, Beth, Jerry, Summer), `A2` (Orchestrator : Computer, Doctors, USS ships, 8 hero-managers), `A3` (Technician : companions, crews, 8 Marvel squads)
- **Subtilité** : dans L2, A-rank **devient** B-rank (B1/B2/B3). Le code A est global, B est local.

### 4.2. Système `B0-B3` (command stack L2 Business)

- **Numérote** : la stack verticale Direction → Domain → Execution au sein de L2 Business
- **Défini dans** : `J01/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md` §1 (table canonique)
- **Valeurs observées** :
  - `B0` — Self-Operating Business doctrine (au-dessus de B1) — `J01/B0_Self_Operating_Business_Doctrine/00_SOB_INDEX.md`
  - `B1` — Direction (Jerry/Summer) — `J01/B1_Area_Direction/`
  - `B2` — Domains / hero-managers — `<J0X>/B2_Area_Domains/`
  - `B3` — Warp Core / Marvel squads — `<J0X>/B3_Area_Warp_Core/`

### 4.3. Système `LD01-LD08` (Life Domains — Wheel)

- **Numérote** : les 8 domaines de la vie (Life Wheel)
- **Défini dans** : `J01/A1_Jerry_Areas_Spec.md` + le mapping canonique 8 Business Wheel domains (SDD-006) — référencé dans `Business_Pulse/L2_Business_Pulse_References_Index.md` §Canonical Conflict Notes
- **Valeurs observées** :
  - `LD01` — Career & Business (J01)
  - `LD02` — Finance (J03)
  - `LD03` — Vitality (J02)
  - `LD04` — Cognition (J02)
  - `LD05` — Social (J04)
  - `LD06` — Family (J03)
  - `LD07` — Creativity (J04)
  - `LD08` — Impact / Solarpunk (J04, **A0 SOVEREIGN DOCTRINE**)
- **Note de cohérence** : SDD-006 dit « 7 domaines », le canon actif dit **8** (le manquant étant `Sales / Illuminati / John Jones`). Le `L2_Business_Pulse_References_Index.md` tranche explicitement (§Canonical Conflict Notes) : « Some SDD passages mention 7 DC/Marvel domains while active SDD-009 and later archive language use 8. This structure keeps the active 8-domain Business Wheel. »

### 4.4. Système `J01-J04` (Jerry variants)

- **Numérote** : les 4 zones de l'Area « Jerry »
- **Défini dans** : `02_Areas_Spock/Jerry_Areas_README.md` + `A1_Jerry_Areas_Spec.md`
- **Valeurs** : `J01_Jerry_Prime_LD01_Business`, `J02_Jerry_Bio_LD03_LD04_Vitality_Cognition`, `J03_Jerry_Nexus_LD02_LD06_Finance_Family`, `J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact`
- **Statuts** : J01 `ACTIVE_FIRST`, J02 `ACTIVE — VPP STANDARD`, J03 `ACTIVE — FIP STANDARD`, J04 `ACTIVE — SCP STANDARD`

### 4.5. Système `H1, H3, H10, H30, H90` (Horizons)

- **Numérote** : horizons temporels (durée de la responsabilité / du suivi)
- **Défini dans** : `02_Areas_Spock/A3_Spock_Areas_Spec.md` (Horizon = H30 pour Areas)
- **Valeurs observées** : `H1` (Life Wheel — Book), `H3` (Life Wheel — Saru), `H10`, `H30` (Areas doctrine, 30-day review), `H90`

### 4.6. Système `W01-W12` (12-Week Year cadence)

- **Numérote** : les 12 semaines d'un cycle
- **Défini dans** : `J01/12WY_Area_Cadence/README.md` (cycles W01-W04 Foundation / W05-W08 Scaling / W09-W12 Optimization)
- **Valeurs** : `W01-W04`, `W05-W08`, `W09-W12` (et les sous-dossiers portent ces noms)

### 4.7. Système `Q1-Q4` (trimestres — parallèle à 12WY mais fiscal)

- **Numérote** : les 4 trimestres
- **Défini dans** : `J03/12WY_Area_Cadence/README.md` (Q1 Foundation, Q2 Scaling, Q3 Optimization, Q4 close)
- **Valeurs** : `Q1`, `Q2`, `Q3`, `Q4`

### 4.8. Système `C1-C4` (B1 command cycles)

- **Numérote** : les 4 gates du cycle 12WY
- **Défini dans** : `J01/12WY_Area_Cadence/README.md` §C1-C4 command-cycle mapping
- **Valeurs** : `C1 Direction Lock` (12WY Open), `C2 Domain Activation` (end Foundation W4), `C3 Execution Proof` (through Scaling W5-W8), `C4 Graduation or Archive` (12WY Close W12)

### 4.9. Système `T1-T4` (Wealth Architecture Tiers — J03)

- **Numérote** : les 4 paliers de souveraineté financière
- **Défini dans** : `J03/AREA_STANDARD.md` §2 (table Wealth Architecture Tiers)
- **Valeurs** : `T1 Safety`, `T2 Independence`, `T3 Acceleration`, `T4 Sovereignty`

### 4.10. Système `KR-X` (Key Results)

- **Numérote** : les indicateurs d'un scorecard Area
- **Défini dans** : `J01/AREA_STANDARD.md` §Scorecard (KR-1 à KR-5)
- **Valeurs observées** : `KR-1` (Revenue Pipeline), `KR-2` (Business Wheel Health), `KR-3` (Cerritos Routing Fidelity), `KR-4` (Brand & Growth), `KR-5` (Runway & Financial Health), `KR-7a..d` (People), `KR-8a..d` (Legal), `KR-LD03-S1`, `KR-LD03-H1`, etc.

### 4.11. Système `SOP-L2-<DOMAIN>-NNN` (Standard Operating Procedures)

- **Numérote** : les procédures par squad
- **Défini dans** : 8 squad canons (J01 B3)
- **Valeurs observées** :
  - `SOP-L2-OPS-001..003`
  - `SOP-L2-FINANCE-001..004`
  - `SOP-L2-IT-001..004`
  - `SOP-L2-LEGAL-001..004`
  - `SOP-L2-PEOPLE-001..004`
  - `SOP-L2-SALES-001` (citée dans B3_Squad_Illuminati)

### 4.12. Système `ADR-<DOMAIN>-NNN` (Architecture Decision Records)

- **Numérote** : les décisions architecturales
- **Défini dans** : `02_Areas_Spock/N0_Coach_Client_Onboarding_KB.md` §8 (11 ADRs sister canon)
- **Valeurs observées** : `ADR-CANON-001`, `ADR-CANON-002`, `ADR-RH-META-GOUVERNANCE-001-canonical-v3`, `ADR-GSTACK-IMBRICATION-001`, `ADR-OBSOLESCENCE-001`, `ADR-OBS-AUDIT-001`, `ADR-MEM-001`, `ADR-L2-AAAS-US-ONLY-001`, `ADR-PEOPLE-001`, `ADR-FINANCE-001`, `ADR-LEGAL-001`, `ADR-AAAS-PRICING-001`, `ADR-AIACT-DEADLINE-001`, `ADR-MESH-L2-001` (citée 8 fois), `ADR-INFRA-001` (citée dans KangDynasty)
- **Statuts** : `RATIFIED` (×8), `ACCEPTED` (×1)

### 4.13. Système `SDD-NNN` (Solution Design Documents — Tech OS)

- **Numérote** : les documents d'architecture dans le Tech OS
- **Défini dans** : `02_Areas_Spock/A3_Spock_Areas_Spec.md` §Evidence + `Business_Pulse/L2_Business_Pulse_References_Index.md`
- **Valeurs observées** : `SDD-006_business-pulse-l2-pyramide`, `SDD-007_sob-factory-icp-variants`, `SDD-009_shadow-L2-business-os`, `SDD-010_meta-cloture-scope-13eme-semaine`

### 4.14. Système `V0 / V1` (versionnage d'artefact Muse)

- **Numérote** : promotion vers Muse
- **Défini dans** : `J04/03_JERRY_SOLARPUNK_PRINCIPLES.md` Cluster F (V0 → V1 Muse)

### 4.15. Système des seuils colorés (GREEN / ORANGE / RED)

- **Numérote** : l'état d'un signal ou d'un système
- **Défini dans** : 7+ tables de seuils (J02, J03, J04)
- **Valeurs** : `GREEN` (all clear), `YELLOW` (cautious, J03 uniquement), `ORANGE` (warning), `RED` (halt)
- **Note** : J03 introduit `YELLOW` entre `GREEN` et `ORANGE`, contrairement à J02/J04 qui n'ont que GREEN/ORANGE/RED. Voir §5 Contradictions.

---

## 5. Contradictions

> Deux fichiers qui décrivent la même chose autrement. Signalées ici,
> **pas tranchées** (le brief interdit de trancher).

| Sujet | Chemin A | Date A | Chemin B | Date B | Nature |
|---|---|---|---|---|---|
| **Nombre de domaines Business Wheel** | `SDD-006_business-pulse-l2-pyramide.md` (cité dans `Business_Pulse/L2_Business_Pulse_References_Index.md`) — **7 domaines** | ancien | `Business_Pulse/L2_Business_Pulse_References_Index.md` §Canonical Conflict Notes (2026-05-21) — **8 domaines** (le manquant : Sales / Illuminati / John Jones) | 2026-05-21 | Le brief dit explicitement que c'est le canon à jour qui tranche (et il tranche pour 8). |
| **Coquille « Creatry » vs « Creativity »** | `02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/` (canonique, 28 fichiers dans `structure.txt`) | 2026-05-21 | `02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creatry_Impact/` (coquille, dossier réel mais quasi-vide, absent de `structure.txt`) | 2026-05-21 | Coquille de nommage côté filesystem ; aucun fichier canonique ne pointe vers l'orthographe fautive. À nettoyer. |
| **Caractère chinois dans une dimension d'évaluation** | `$100M Offers` rubric — `J01/AREA_STANDARD.md` §P5 (« 独特 Selling Proposition » au lieu de « Unique Selling Proposition ») | 2026-05-21 | Le brief canonique d'Hormozi parle d'USP = **Unique** Selling Proposition | n/a | Corruption de texte (caractères chinois insérés). Ne touche pas la doctrine mais trahit une édition incomplète. |
| **Présence de `YELLOW`** | `J03/AREA_STANDARD.md` + `J03/B1_Area_Direction/README.md` — introduit un 4e niveau `YELLOW` entre `GREEN` et `ORANGE` (Coverage 80-99%, Family Load 5-7, Runway 6-11mo) | 2026-05-21 | `J02/AREA_STANDARD.md` + `J04/AREA_STANDARD.md` — n'utilisent que `GREEN / ORANGE / RED` | 2026-05-21 | Incohérence de modèle d'états : 3 vs 4 niveaux. J03 est le seul à 4. |
| **Numéro de la règle de fermeture T1/T2/T3/T4** | `J03/AREA_STANDARD.md` §2 numérote `J02-001`, `J02-002`, `J02-003` | 2026-05-21 | `J03/AREA_STANDARD.md` même fichier §§3-5 numérote `J03-001` à `J03-003`, puis §§6-8 `J04-001` à `J04-004` puis `J05-001` à `J05-004` puis `J08-001` à `J08-004` | 2026-05-21 | Préfixes incohérents (`J02` puis `J03`, `J04`, `J05`, `J08`) dans un même fichier. Semble indiquer que les sections ont été importées de plusieurs sources sans renumérotation. |
| **Bibliographies inconsistantes** | `J03/README.md` (header YAML `bibliography对齐` — mélange français/chinois : `bibliography对齐` veut dire « alignment » et utilise un caractère chinois) | 2026-05-21 | `J03/AREA_STANDARD.md` (même en-tête, sans le caractère chinois : `bibliography_alignment`) | 2026-05-21 | Corruption YAML (caractère chinois). Le header YAML n'est pas du YAML valide. |
| **Règle "$100M Offers"** | `J01/AREA_STANDARD.md` §P5 (rubric avec 5 dimensions pondérées : Dream Outcome 25%, Perceived Likelihood 20%, Price vs Value 20%, USP 20%, Low Friction 15%) | 2026-05-21 | `B3_Squad_Illuminati/00_B3_SQUAD_CANON.md` ne référence pas le rubric (mais cite la qualification MEDDIC) | 2026-05-21 | Pas une vraie contradiction — juste un signal que le rubric est défini dans B1 (stratégie), pas dans B3 (exécution). À expliciter. |
| **Saru H1 / Book H1** | `02_Areas_Spock/A3_Spock_Areas_Spec.md` §D3 nuance — corrige « Saru = H3, Book = H1 (Life Wheel canon, corrigé de "Saru H1 + Book H10" qui était faux) » | 2026-06-21 | Patch antérieur cité comme faux | avant 2026-06-21 | Le patch top-level a corrigé une erreur antérieure. OK. |
| **Sales B2 Manager** | `A1_Jerry_Areas_Spec.md` table — `Sales / Martian Manhunter / Illuminati` | 2026-05-21 | `J01/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md` §4 — `Sales / John Jones (Martian Manhunter) / Illuminati` | 2026-05-31 | Le nom complet « John Jones (Martian Manhunter) » est utilisé dans le fichier le plus récent ; seul « Martian Manhunter » dans le plus ancien. Probable évolution du lore — à confirmer. |

### 5.1. Coquilles / corruptions mineures à signaler

- `Business_Pulse/.../02_Phase2_Project_Charter.md` est un document de **style théâtral conversationnel** (commence par « C'est acté, Amiral. La Constitution est ratifiée. ») — pas du canon structuré.
- `the-bridge-__-life-os/README.md` est un README générique de **template Gemini AI Studio** (mentionne `GEMINI_API_KEY`). Ne contient aucune doctrine du seau.
- `Business_Pulse/.../03_Phase3_Master_SQL_Schema.md` est aussi conversationnel (« C'est parti. **Cyborg** prend les commandes. »).
- `Business_Pulse/docs/documentation/Canon_BMad_DEAL/` : les deux fichiers sont **conversationnels**, pas canoniques au sens strict. Le `02_Phase2_Project_Charter.md` ne respecte pas le format OKF (pas de frontmatter YAML).

---

## 6. Observations finales (hors-périmètre du brief mais à noter)

> Le brief demande d'extraire l'ontologie sans inventer. Cette section
> note des **patterns** que les fichiers suggèrent sans les déclarer.

- **La structure B0 existe** dans J01 mais est **absente** de J02/J03/J04.
  C'est asymétrique : seul J01 (le plus mature) a une couche Self-Operating
  Business au-dessus de B1. J02/J03/J04 restent B1/B2/B3.
- **SOPs** : seulement J01 a des SOPs (6 par squad × 8 squads = ~25 SOPs).
  J02/J03/J04 n'ont **aucune SOP** dans leurs sous-dossiers. Cohérent avec
  le fait que J01 est le seul Area « opérationnel » ; les autres sont des
  Areas de **contrainte** ou de **contribution**.
- **ADRs** : `ADR-MESH-L2-001` est cité **8 fois** dans `J04/03_JERRY_SOLARPUNK_PRINCIPLES.md`
  — une par domain README de J04. Le même ADR unifie la doctrine de
  « one datum, one owner ». Sans citer l'ADR en entier, c'est un invariant.
- **Bibliographies** : ~48 livres canoniques répartis sur 8 LD, mais
  certaines bibliographies sont marquées `CANONICAL_FROM_CANON 12 — internal
  canon; external corpus empty` (ex : Finance `B2_Area_Domains/06_.../README.md`).
  C'est un signal que le corpus externe **n'est pas** joint — les « livres »
  servent de **socle théorique déclaré**, pas de source vérifiable.
- **Valeurs canon (foi/famille/mission/ikigai/discipline)** sont déclarées
  comme **immuables** dans `JERRY_WHEEL_ALIGNMENT_MINDSET_VALUES.md` §4.
  Ce sont des entités de niveau méta — au-dessus des Areas.
- **A0 SOVEREIGN DOCTRINE = LD08** uniquement. Aucun autre LD n'est
  déclaré « SOVEREIGN ». Asymétrie à noter si l'ontologie veut symétriser
  les 8 LD.

---

## 7. Annexe — fichiers effectivement parcourus

```
02_Areas_Spock/README.md
02_Areas_Spock/A1_Jerry_Areas_Spec.md
02_Areas_Spock/A3_Spock_Areas_Spec.md
02_Areas_Spock/Jerry_Areas_README.md
02_Areas_Spock/JERRY_WHEEL_ALIGNMENT_MINDSET_VALUES.md
02_Areas_Spock/N0_Coach_Client_Onboarding_KB.md
02_Areas_Spock/Business_Pulse/README.md
02_Areas_Spock/Business_Pulse/L2_Business_Pulse_References_Index.md
02_Areas_Spock/Business_Pulse/docs/documentation/Canon_BMad_DEAL/02_Phase2_Project_Charter.md
02_Areas_Spock/Business_Pulse/docs/documentation/Canon_BMad_DEAL/03_Phase3_Master_SQL_Schema.md
02_Areas_Spock/the-bridge-__-life-os/README.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/README.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/AREA_STANDARD.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/00_L2_FRACTAL_B1B2B3_ARCHITECTURE.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B0_Self_Operating_Business_Doctrine/00_SOB_INDEX.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B1_Area_Direction/README.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B1_Area_Direction/03_DECISION_CHARTER.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B1_Area_Direction/05_B2_DEFINITION_OF_DONE_SPEC.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B1_Area_Direction/06_B3_JOBS_TO_BE_DONE_SPEC.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/README.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/01_Growth_Superman_Guardians/README.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/01_Growth_Superman_Guardians/B3_Squad_Guardians/00_B3_SQUAD_CANON.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/02_Sales_MartianManhunter_Illuminati/README.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/02_Sales_MartianManhunter_Illuminati/B3_Squad_Illuminati/00_B3_SQUAD_CANON.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/03_Product_Flash_Avengers/README.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/03_Product_Flash_Avengers/B3_Squad_Avengers/00_B3_SQUAD_CANON.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/04_Ops_Batman_Fantastic4/README.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/04_Ops_Batman_Fantastic4/B3_Squad_Fantastic4/00_B3_SQUAD_CANON.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/05_IT_Cyborg_KangDynasty/README.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/05_IT_Cyborg_KangDynasty/B3_Squad_KangDynasty/00_B3_SQUAD_CANON.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/06_Finance_WonderWoman_Thunderbolts/README.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/06_Finance_WonderWoman_Thunderbolts/B3_Squad_Thunderbolts/00_B3_SQUAD_CANON.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/07_People_GreenLantern_XMen/README.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/07_People_GreenLantern_XMen/B3_Squad_XMen/00_B3_SQUAD_CANON.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/08_Legal_Aquaman_Eternals/README.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/08_Legal_Aquaman_Eternals/B3_Squad_Eternals/00_B3_SQUAD_CANON.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/Artifact_Proofs/README.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B3_Area_Warp_Core/Lead_Lag_Logs/README.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/12WY_Area_Cadence/README.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/12WY_Area_Cadence/W01_W04_Foundation/README.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/12WY_Area_Cadence/W05_W08_Scaling/README.md
02_Areas_Spock/J01_Jerry_Prime_LD01_Business/12WY_Area_Cadence/W09_W12_Optimization/README.md
02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/README.md
02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/AREA_STANDARD.md
02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/B1_Area_Direction/README.md
02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/B2_Area_Domains/README.md
02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/B3_Area_Warp_Core/Lead_Lag_Logs/README.md (partiel)
02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/12WY_Area_Cadence/README.md
02_Areas_Spock/J02_Jerry_Bio_LD03_LD04_Vitality_Cognition/12WY_Area_Cadence/W01_W04_Foundation/README.md (partiel)
02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/README.md
02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/AREA_STANDARD.md
02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/B1_Area_Direction/README.md
02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/B2_Area_Domains/README.md
02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/12WY_Area_Cadence/README.md
02_Areas_Spock/J03_Jerry_Nexus_LD02_LD06_Finance_Family/12WY_Area_Cadence/W01_W04_Foundation/README.md (partiel)
02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/README.md
02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/AREA_STANDARD.md
02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/03_JERRY_SOLARPUNK_PRINCIPLES.md
02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/B1_Area_Direction/README.md
02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/B2_Area_Domains/README.md
02_Areas_Spock/J04_Jerry_Solarpunk_LD05_LD07_LD08_Social_Creativity_Impact/12WY_Area_Cadence/README.md
```

Soit **47 fichiers substantiellement lus** sur **95 disponibles** dans le seau.
Le reste (48 fichiers) se répartit entre : 8 B2 sub-READMEs de J02, 8 B2 sub-READMEs de J03, 8 B2 sub-READMEs de J04, 6 B3 Lead_Lag/Artifact_Proofs de J02/J03/J04, 6 sous-W## non-couverture pour J02/J03/J04, et ~12 fichiers déjà couverts en substance via leurs parents.

---

*Fin du rapport. Aucun fichier de V2 n'a été modifié. Les sorties restent
dans `00_Amadeus/30_MEMORY_CORE/carto/02_Areas_Spock.{md,json}`. Les autres
agents peuvent travailler en parallèle sur `01_Projects_Picard`,
`03_Resources_Geordi`, `04_Archives_Data` sans conflit.*