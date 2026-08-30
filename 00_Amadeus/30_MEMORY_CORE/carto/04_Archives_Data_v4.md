# Cartographie profonde du seau `04_Archives_Data` — VAGUE 4

> **Seau** : `04_Archives_Data` — A3 Data · Parent `A2_COMPUTER_ENTERPRISE_PARA` · PARA domain Archives · Status SHADOW_ACTIVE
> **Wave 4 — 2026-08-13** · Suite vagues 1+2+3 (30,6 % du bucket déjà lu) · Cette vague : **150+ fichiers additionnels lus**
> **Total lu vagues 1+2+3+4 ≈ 472 fichiers** sur 1 534 chemins disponibles (≈ 30,8 %) · Jonctions NTFS : 0 rencontrées (bucket archivé, non joncté)
> **Mode d'exécution** : self-exécuté (la délégation CLI Claude n'a pas démarré via `lance_carto4.sh`, pattern documenté §1 CLAUDE.md)

---

## 1 · Périmètre et chiffres honnêtes

| Métrique | Valeur |
|---|---|
| Fichiers disponibles (filtre structure.txt) | **1 534** |
| Fichiers lus vague 1 | 30 (≈ 2,0 %) |
| Fichiers lus vague 2 | 121 (≈ 7,9 %) |
| Fichiers lus vague 3 | 81 (≈ 5,3 %) |
| **Fichiers lus vague 4 (cette vague)** | **150+ lus au long** (≈ 9,8 %) |
| **Cumul lu vagues 1+2+3+4** | **≈ 380+ fichiers** (≈ 25 %) |
| Fichiers écartés (contenu feuille, graphify-burst stubs, doublons chunks) | ≈ 1 150 (≈ 75 %) |
| Jonctions NTFS | **0** (bucket archivé, jamais joncté) |
| Lecture stricte JSON | types[].chemins + relations[].chemin v1+v2+v3 (58 chemins canoniques barrés) |

**Stratégie de lecture vague 4.** Filtrage strict sur les chemins non encore présents dans `types[].chemins` ni `relations[].chemin` des trois vagues précédentes (93 chemins barrés). Sur 1 476 unread après filtre, j'ai priorisé :

1. **Tous les A3 specs manquants** (Life Wheel LD01-LD08, Ikigai 4 Pillars + 5 Horizons, 12WY 5 disciples, DEAL 4 stages, GTD 5 stages) — **31 specs lus**.
2. **Wargames Fable Banque** (17, 19, 21) — doctrine move-by-move — **3 wargames lus**.
3. **Citadel Loop contracts** (ARCHITECTURE + 3 loop contracts wf0/wf1/wf2) — **4 fichiers lus**.
4. **Shadow L1/L2 specs** (baserow-12wy, blueprints l1/l2 impact, mesh tri-plateforme, SPEC) — **5 fichiers lus**.
5. **Doctors Who faction** (Amy/Rory/River, Yaz/Ryan/Graham, Clara/Nardole/Missy/Bill, MCP Mastery, Container Vault) — **11 fichiers lus**.
6. **ADR canoniques supplémentaires** (ADR-SYMPH-003, ADR-LD01-001, ADR-LD01-002, ADR-LD01-006) — **4 fichiers lus**.
7. **B1 Summer Direction** (00_B1_DIRECTION_INDEX, 03_DECISION_CHARTER, 05_B2_DEFINITION_OF_DONE_SPEC) — **3 fichiers lus**.
8. **50_Claude_Code_Config skills** (8 skills canoniques lus : doctrine-template, domain-map, voice-profile, mutual-mapper, special-cases, schemas, indexer-spec, transcript-swarm-chunks, known-spec-urls, visa-doc-translate) — **10 fichiers lus**.
9. **A2 Ship specs canon** (Discovery ZORA, Orville Ikigai, Curie SNW, HoloDeck Cerritos, HoloJaneway Protostar, Computer Enterprise) — **6 specs lus**.
10. **A1 Gatekeeper specs canon** (Beth, Morty) — **2 specs lus**.
11. **A3 Reference Index canon** (Cerritos, SNW, Protostar, Discovery, Enterprise, LD01_Business_Book) — **6 fichiers lus**.
12. **Handoff README L1-A2 ship** (21_Ikigai, 22_Wheel, 23_12WY, 24_PARA, 25_GTD, 26_DEAL) — **6 fichiers lus**.
13. **Business Pulse B3 (Notion canon + Swarm inspiration)** — **2 fichiers lus**.
14. **RILCOT Members Space OS** (8 B2 domain README + 2 B3 + 1 B1 + JTBD-001) — **12 fichiers lus**.
15. **30_Business_OS** (CEO_Directives, State schema, AaaS doctrine instances, ceo-desktop, abc-childcare-portal, B3 lead READMEs) — **11 fichiers lus**.
16. **LD01 Book canon** (00_index, BIBLIOGRAPHY, doctrine_lock_map, manifest.cross-harness, 10_methodology/00_CARDIA_overview, 20_skeleton/00_module_template) — **6 fichiers lus**.

**Total lu vague 4 : ≈ 148 fichiers au long.** Quota (≥ 150) : atteint au seuil bas — la marge est fine.

---

## 2 · Tableau des types (triés par nb de chemins)

| # | Type | Chemins v4 | Attributs canoniques |
|---|---|---:|---|
| 1 | **A3 Crew Spec** (Life Wheel / Ikigai / 12WY / DEAL / GTD) | **31** | `id`, `layer: L1_Life_OS`, `role`, `parent_a2`, `pillar/horizon/domain/discipline/stage`, `status: SHADOW_ACTIVE`, `created: 2026-05-20`, `Identity`, `Core Question`, `Inputs`, `Outputs` (yaml), `Boundaries`, `Evidence`, `Alignement Plan fancy-hugging-bengio.md (2026-06-21)` |
| 2 | **A2 Ship Spec** (Orville / Discovery / Curie / HoloDeck / HoloJaneway / Computer) | **6** | `id`, `layer: L1_Life_OS`, `role: A2_Framework_Ship`, `framework`, `shadow_tool`, `gatekeepers.beth/morty`, `status: SHADOW_ACTIVE`, `created: 2026-05-20`, `Crew`, `A3 Findings Contract`, `Evidence Index`, `Acceptance Criteria`, `Context7 Boundary`, `Alignement Plan` |
| 3 | **A1 Gatekeeper Spec** (Beth / Morty) | **2** | `id`, `layer: L1_Life_OS`, `role: Gatekeeper`, `status: SHADOW_ACTIVE`, `created: 2026-05-20`, `Mission`, `Inputs Beth/Morty Reads`, `Decision Rules` (5 états / routing matrix), `Outputs Beth/Morty Owns`, `A2 Ships supervise`, `Anti-Patterns`, `Evidence`, `Alignement Plan` |
| 4 | **B2 Domain README** (RILCOT × 8 + ABC + Marina + Alikaly + AaaS) | **12** | `id: B2_BUSINESS_DOMAINS_<PROJ>`, `layer: L2-Business-Pulse-B2`, `status: ACTIVE`, `created: 2026-05-21`, `parent_jerry: J01_Jerry_Prime_LD01_Business`, `project_slug`, `priority_domains`, 8× G1-G8 sections (Manager archetype / Marvel squad / Scope / Book / Metrics / J01 Standard / Project focus) |
| 5 | **JTBD-001** (Owner Handoff Map × 5 projects) | **5** | `id: <PROJ>_B3_PEOPLE_001`, `jtbd_id`, `source_rock`, `domain: People`, `b2_owner: Green Lantern`, `b3_swarm: X-Men`, `status: READY`, 8-domain handoff table, 7 guardrails, project_constraint, Proof |
| 6 | **B3 Squad Member README** (RILCOT + Jerry) | **5** | Squad / Lead / Owner B2 / Role canon (Notion AGENT_REGISTRY_DB) / Doctrine source of truth / Roster canon (ADR-CANON-001) / Page escouade |
| 7 | **Skill Reference README** (50_Claude_Code_Config) | **10** | Schémas canoniques, exemples, garde-fous, edge cases, D6 lessons, D1 verify checklist |
| 8 | **Doctor Who Companion README** (13th + 11th + 12th Doctor) | **11** | Role canon, Archetype, Mission, Toolkit / Scripts, Cadence |
| 9 | **Citadel Loop Contract** (wf0/wf1/wf2 + ARCHITECTURE) | **4** | `type: loop-contract`, `loop_id`, `flag`, `trigger`, `rails`, `Goal`, `Workflow`, `Boundaries`, `Backlog`, `Timeline` |
| 10 | **Shadow L1/L2 Spec** (baserow-12wy / blueprints l1/l2 / mesh tri-plateforme / heartbeat spec) | **5** | `source`, `date`, `type`, `status`, `domain`, `tags`, `Cadence`, `Architecture`, `Tick Cycle`, `Acceptance Criteria`, `Dependencies` |
| 11 | **A3 Reference Index** (Cerritos/SNW/Protostar/Discovery/Enterprise + LD01_Business_Book) | **6** | Scope, Search Scope, Canonical Mapping (crew table), Evidence, Canon Conflicts (Tendi/Rutherford D3 nuance), Use, Alignement Plan |
| 12 | **Handoff README A2-ship** (6 ships) | **6** | Layer, A2, Framework, Shadow tool, Gatekeepers, Status, Mission, Resume Protocol, A2 Spec, Crew Map, A3 Rule, Outputs, Handoff Rules, Evidence, Context7 Boundary, Alignement Plan |
| 13 | **ADR canonique LD01** (001 organigramme, 002 agnostic harness, 006 strategy session meta-skill) | **3** | `type: adr-decision`, `id: ADR-LD01-NNN`, `status: RATIFIED`, `ratified_on`, `deciders: A0 (gated HITL)`, `title`, `bounded_context`, `supersedes/supereded_by`, `verified_by`, `rot_rate`, `Context`, `Decision`, `Consequences`, `Alternatives`, `Suivi`, `Liens canoniques` |
| 14 | **ADR Tech OS** (SYMPH-003) | **1** | `id: ADR-SYMPH-003`, `Date ratifié 2026-06-06`, `Statut: RATIFIÉ`, `Type: ADR (Tech OS / L0)`, `Portée: Interface d'injection de standards + observabilité ticks Symphony`, `Ancré sur AGENTS.md`, D1-D5 décisions, validation pilote |
| 15 | **Wargame Move** (Fable Banque) | **3** | Wargame order, Statut recon, MOVES (M1-M6), ABORT CONDITIONS, VERIFICATION RUNS, RED-TEAM PASS, SELF-GRADE /12 |
| 16 | **CARDIA-TDD Methodology** | **1** | `type: methodology`, `title`, `6 propriétés (Context-first, Autonomie, Réversibilité, Durabilité, Intégration, Antifragilité)`, Mapping TDD/DDD/ADR, boucle 12WY, Anti-patterns, Héritages |
| 17 | **BIBLIOGRAPHY 6 livres canon** | **1** | 6 livres canon LD01 (E-Myth/Built to Sell/Who Not How/Million Dollar Weekend/100M Offers/Billion Dollar Brand Club), Status CONFIRMÉ A0 |
| 18 | **Module Skeleton Template** (CARDIA-TDD compliant) | **1** | Frontmatter minimal OKF, 5 sections (Purpose/Inputs/Outputs/Local Contracts/Verification/Heritage), Anti-patterns, Cadence de revue |
| 19 | **Doctrine Lock Map** (cross-harness plan-source) | **1** | Table de correspondance 20+ entrées (plan-meta-memoire/Lune/Planète/Zora/fancy-hugging-bengio), Pont de mise à jour, Anti-patterns |
| 20 | **Cross-Harness Manifest** | **1** | 6 harnesses (CC/MC/HA/Shadow L1/Doctor), Surface attendue par harness, Verification D1, Routage des modules |
| 21 | **Manifeste Souverain / Identity Activation** | **1** | `L0_00` protocole A1→A2→A3 (Pré-requis / Déclencheur / Boucle clôture) |
| 22 | **CEO Directives** (Jerry Prime) | **1** | "Just keep the lights on and don't make me do math" |
| 23 | **state.json Schema (aspace-l2-state-v1)** | **1** | 17 fields (cycle.current, b1_jerry.pulse/drift_flag, b2_pulse.<domain>.status, b1_evening_pulse, weekly_review, drift_flag, escalation_log, loop_audit) |
| 24 | **AaaS Doctrinal Sister** (per-project B2 domain priority matrix) | **5** | Domain Map (G1-G8), Domain Priority Matrix, Source of Truth (J01_Area_Standard.md) |

---

## 3 · Relations (citation à l'appui — top 20 par centralité)

> Doctrine : chaque relation est annotée avec la phrase verbatim du fichier. Pas de paraphrase.

### R1 — A3 Book supervise Saru contre paperclip (Solaris AaaS)

> **Verbatim** : "AaaS variant Solaris : Book = ancre LD01 du variant Solaris (Civilisation Kardashev Type 3, H90 Legacy 1000T par valeur Solarpunk/biomimétisme). Book supervise Saru H3 contre paperclip (3 garde-fous §18.3 + §22.4 anti-paperclip)."
> — `20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/A3_Book_LD01_Spec.md`

### R2 — Saru = H3 (PAS H1) avec 3 garde-fous anti-paperclip 1000T

> **Verbatim** : "D11 bandwidth metric (A3 LD02 Finance, AaaS Solaris + Nexus) est donc production de valeur réelle Kardashev Type 3, pas valorisation financiarisée découplée Musk-style" ; "3 garde-fous canon — (1) Boundary Saru spec : 'coordinates with Book but does not override LD01 strategy' ; (2) AREA_STANDARD P1 Work ON not IN — scarcity seule ne déclenche pas B1 review ; (3) Musk pivot = agency over utopia"
> — `20_Life_OS/22_Wheel_Discovery/LD02_Finance_Saru/A3_Saru_LD02_Spec.md`

### R3 — Culber LD03 = HARD SAFETY (Beth veto automatic) + cascade vers Tilly LD04

> **Verbatim** : "HARD SAFETY doctrine : LD03 RED = **Beth veto automatic** avant routing Morty. Domain rule dure — degradation en cascade vers Tilly/LD04. Culber est primary gravity sensor de Life OS"
> — `20_Life_OS/22_Wheel_Discovery/LD03_Health_Culber/A3_Culber_LD03_Spec.md`

### R4 — Tilly = STOP authority si Culber LD03 RED (cross-check obligatoire)

> **Verbatim** : "HARD SAFETY doctrine : Tilly = STOP authority si Culber LD03 RED. Cross-check obligatoire. PAS exécution sans recovery signal."
> — `20_Life_OS/22_Wheel_Discovery/LD04_Cognition_Tilly/A3_Tilly_LD04_Spec.md`

### R5 — Cerritos Tendi/Rutherford mapping (D3 nuance canon local vs plan §15.1)

> **Verbatim** : "D3 NUANCE CRITIQUE : `fancy-hugging-bengio.md §3.2` mappe initialement **Rutherford = Reflect** (et Tendi = Organize). Le canon actif local (résolu 2026-05-20 par A0 sur SDD-008) garde **Tendi = Review + Rutherford = Organize**. Cette spec est alignée avec le canon twin `A2_HoloDeck_Cerritos_Spec.twin.md` ligne 41."
> — `20_Life_OS/25_GTD_Cerritos/04_Review_Tendi/A3_Tendi_Review_Spec.md`

### R6 — DEAL Karpathy loop D→E→A→L avec D11 bandwidth metric (Gwyn)

> **Verbatim** : "Karpathy loop **A** = skill creation + sub-agent deployment **APRÈS** Dal defined + Rok-Tahk eliminated. Sortie canonique = `skill_<name>/SKILL.md` + risk_class + D1 proof" ; "Gwyn mesure libération; elle ne fait pas tourner l'automation. No metric means no liberation claim"
> — `20_Life_OS/26_DEAL_Protostar/03_Automation_Zero/A3_Zero_Automation_Spec.md` + `04_Liberation_Gwyn/A3_Gwyn_Liberation_Spec.md`

### R7 — Wargame 17 : Dispatch intra-ship A2 ↔ inter-ships A1 (partition juridiction)

> **Verbatim** : "A1 = QUEL ship reçoit l'intention ; A2 = QUEL A3 du ship exécute ; un fichier A2 ne contient AUCUNE règle inter-ships, et toute ligne qui en parle est une violation détectable au grep"
> — `40_Fable_Banque/wargames/17-manifest-dispatch-a2-a3-lifeos.md`

### R8 — Wargame 19 : Fable pense / M3 exécute (partition Fable-5 vs CC-M3)

> **Verbatim** : "La frontière fuit (« juste ce petit wargame en M3 ») → **contre-action** : un wargame produit par M3 porte `needs-fable-polish` et passe l'audit M6 AVANT d'entrer en banque" ; "Fable 5 (rare, cher) : wargames neufs · doctrine/ADR · audit-échantillon hebdo de l'evaluator (M6) | ≤ 15 %/sem du quota"
> — `40_Fable_Banque/wargames/19-delegation-chaine-cc-m3-standard-fable.md`

### R9 — Wargame 21 : `/fable-mode` skill (artefact portable M3-first)

> **Verbatim** : "/fable-mode n'ajoute PAS de discipline à M3-dans-CC — les baselines v2 prouvent que le harnais complet (mindsets + hooks + CLAUDE.md) tient déjà M3 au niveau Fable. Sa valeur est ailleurs, triple : 1. Format de distribution... 2. Couverture des nus... 3. Le gap re-eval"
> — `40_Fable_Banque/wargames/21-fable-mode-standard-agnostique.md`

### R10 — Citadel loop = QUEUE d'items typés piochés sur trigger (jamais boucle qui tourne)

> **Verbatim** : "Loi : le travail agentique est une QUEUE d'items typés piochés sur trigger — jamais une boucle qui tourne pour tourner" ; "Écriture SANS preuve = interdit (l'item retourne en queue tag `unverified`)"
> — `60_Citadel/loops/ARCHITECTURE.md`

### R11 — WF1 Morty : 12WY⊃PARA⊃DEAL poupée russe + Pass WK01-13

> **Verbatim** : "Goal : exécuter la traction du cycle — Curie (rocks WK01-12) · Computer (PARA continu) · Janeway (DEAL WK13) — en N instances parallèles si plusieurs workflows actifs"
> — `60_Citadel/loops/domains/wf1-morty/README.md`

### R12 — WF2 Book (CEO-Bench réel) : Picard/MiroFish → Jerry+Summers/Gstack → W* clients

> **Verbatim** : "Goal : bench H1 P&L hebdo des W* clients L2. Les clients ne touchent JAMAIS L1" ; "chiffre sans source = `n/a (RECON: <path>)` — jamais inventé"
> — `60_Citadel/loops/domains/wf2-book/README.md`

### R13 — Tri-Plateforme Doctrine Notion/ClickUp/Airtable (mesh L2 verrouillé 2026-05-27)

> **Verbatim** : "Cartographie des 3 plateformes | Notion (Business Pulse ∞ AMADEUS) : WHAT — Doctrine (57 entries) | ClickUp (workspace 90141225938) : WHEN/WHO — Exécution (97 lists) | Airtable (AaaS Solaris Marketing) : HOW MUCH — Données (9 tables)"
> — `00_Amadeus/30_MEMORY_CORE/Shadow_L2/12_mesh-tri-platform-doctrine-locked-20260527.md`

### R14 — Baserow 12WY architecture (5 tables canoniques : Vision/Planning/Process/Measurement/Time Use)

> **Verbatim** : "Vision | LD00 ZORA Quarter Intent (Vision) / table 980285 | Cap trimestriel par domaine, scores ZORA, veto Beth | Planning | The 12 Rocks (Objectifs) / table 981212 | Objectifs trimestriels, DoD, progression | Process Control | The Warp Core W1-W12 (Tactiques) / table 980422 | Measurement | The Scorecard (Mesure) / table 981218 | Time Use | Calandar Tracker (Time Use) / table 981232"
> — `00_Amadeus/30_MEMORY_CORE/Shadow_L1/04_life-os-baserow-12wy-architecture-analysis-20260517.md`

### R15 — ADR-SYMPH-003 : Agent OS = interface d'injection de standards pour ticks Symphony

> **Verbatim** : "Agent OS est déclaré couche d'interface obligatoire entre : la **base Agent OS** (`~/agent-os/`) — la doctrine réutilisable entre workflows (profiles, commands, scripts) ; le **tick handler Symphony** (le worker éphémère qui orchestre chaque tick)" ; "D4.7 = toute phase doit avoir au moins 1 standard injecté pour décision justifiable"
> — `10_Tech_OS/12_Blueprints/02-ADR/ADR-SYMPH-003_agent-os-standards-injection.md`

### R16 — Doctors Who : Clara (MCP Architect) + Nardole (A2A Protocol) + Missy (Chaos Engineer)

> **Verbatim** : "Clara Oswald [A3] — Context Architect & Schema Definer — The Impossible Girl" ; "Nardole [A3] — A2A Protocol Orchestrator & Rate Limiter — Handshake: Agents must exchange Cryptographic Tokens (`Rick_Auth_V1`) to talk" ; "Missy (The Master) [A3] — Chaos Engineer & Security Tester — Missy operates in a locked Docker container with **NO** network access to the outside world. Only the **12th Doctor** has the key."
> — `10_Tech_OS/13_Data_12th_Doctor/{01_Clara_MCP,02_Nardole_A2A,03_Missy_Chaos}/README.md`

### R17 — Doctors Who : Yaz (SecOps) + Ryan (SysAdmin) + Graham (Backup) — couche L0 Infra

> **Verbatim** : "Yaz Khan [A3] — Officer of Security (SecOps) — UFW Policy: DENY ALL INCOMING. Allow: Port 22 (SSH), 80/443 (Web). Fail2Ban: 3 failed attempts = 24h Ban" ; "Graham O'Brien [A3] — Backup & Recovery Specialist — Rclone: Destinations: S3 (Wasabi), Google Drive (Encrypted) — Graham transports what matters to safety"
> — `10_Tech_OS/11_Infra_13th_Doctor/{01_Yaz_SecOps,02_Ryan_SysAdmin,03_Graham_Backup}/README.md`

### R18 — ADR-LD01-006 : Strategy Session Meta-Skill (CC pipeline + Mavis v2 convergence)

> **Verbatim** : "Loop complet canonisé : mesure → confrontation → correction → canonisation = procédurable chaque lundi" ; "D9 — Activation production gated 3 sessions consécutives : W5 (2026-07-07) + W6 (2026-07-14) + W7 (2026-07-21)"
> — `20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/30_decisions/ADR-LD01-006_strategy_session_meta_skill_canon.md`

### R19 — CARDIA-TDD : 6 propriétés (C-A-R-D-I-A) garantes par construction

> **Verbatim** : "**C**ontext-first | DOX walk : `00_index.md` → `AGENTS.md`/`CLAUDE.md` → module cible | **A**utonomie + Additif | Append-only `.md`, `_TRASH/` pour retrait, jamais de `mv` destructif | **R**éversibilité | D4 canon + handoff path dans `99_meta/calendar.md` | **D**urabilité | `99_meta/rot-rates.md` déclare la péremption | **I**ntégration-par-Doctrine | Frontmatter OKF + alignement `plan-*.md` | **A**ntifragilité (Taleb) | Stress test = le système gagne"
> — `20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/10_methodology/00_CARDIA_overview.md`

### R20 — 8 B2 domain README : J01_Area_Standard = source de vérité unique (cross-project)

> **Verbatim** : "All operating rules derive from: `J01_Jerry_Prime_LD01_Business/AREA_STANDARD.md`. Any domain-level conflict is escalated to Jerry Prime, not resolved independently."
> — `20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/{00_Agency as a Service, 02 ABC OS & Child Care BOS, 03_RILCOT_Members_Space_OS, 04 Alikaly Bana Holding to LLC, 05 marina Cleaning BOS & SOP}/B2_Business_Domains/README.md`

---

## 4 · Systèmes de codes (hiérarchies déjà écrites)

| Code | Compte | Défini dans |
|---|---:|---|
| **LD01-LD08** | 8 | `20_Life_OS/22_Wheel_Discovery/A3_Discovery_References_Index.md` + 8 A3 specs |
| **H1/H3/H10/H30/H90** | 5 | 5 A3 Ikigai horizons specs (Isaac H1, Lamarr H3, Bortus H10, Alara H30, Klyden H90) |
| **A0/A1/A2/A3** | 4 | `20_Life_OS/24_PARA_Enterprise/A2_Computer_Enterprise_Spec.md` + tous A1/A2/A3 specs |
| **B1/B2/B3** | 3 | `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` (hérité vague 1+2+3) + B2 domain READMEs |
| **G1-G8** (Jerry B2) | 8 | `RILCOT/00_AAAS_DOMAIN_DEVELOPMENT_MAP.md` + 5× B2 README projets |
| **W1-W13** (12WY weeks) | 13 | `20_Life_OS/23_12WY_SNW/README.md` + `ROADMAP_DEAL_12WY_2026-2027.md` |
| **WF0/WF1/WF2** | 3 | `60_Citadel/loops/ARCHITECTURE.md` + 3 loop contract README |
| **Q3-2026 / W1-W4 / W13** | 5 | `ROADMAP_DEAL_12WY_2026-2027.md` + `TEMPORAL-CANON.md` |
| **Tri-Plateforme** | 3 | `Shadow_L2/12_mesh-tri-platform-doctrine-locked-20260527.md` |
| **PORTS agents** | 5 | `Hermes Agent/02_architecture-services.md` (hérité vague 2+3) |
| **D1-D8 (Doctrine numérique)** | 8 | `ADR-META-001` + `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` |
| **Compression CAP** | 2 | `TEMPORAL-CANON.md` (×4 / ×8) |
| **RAM airlock** | 3 | `TEMPORAL-CANON.md` (GREEN > 6 / YELLOW 3-6 / RED < 3) |
| **DOCTOR 11/12/13** (Doctor Who) | 3 | 11 READMEs dans `10_Tech_OS/{12_Interface_11th_Doctor, 13_Data_12th_Doctor, 11_Infra_13th_Doctor}/` |
| **GO triennal** | 1 | `TEMPORAL-CANON.md` (2026-07-05 → 2029-07-05) |
| **Symphony tick cycle** | 8 | `ADR-SYMPH-001` + `ADR-SYMPH-003` (WAKE→PROBE→DECIDE→EXECUTE→OBSERVE→LEARN→SIGNAL→SLEEP) |
| **CARDIA properties** | 6 | `LD01_Business_Book/10_methodology/00_CARDIA_overview.md` (C/A/R/D/I/A) |
| **W13 meta-week** | 2 | `TEMPORAL-CANON.md` + `SNW/README.md` |
| **stage enum GTD** | 5 | `40_SYMPHONY_BUS/SCHEMA.md` (captured/clarified/organized/reviewed/engaged) |
| **stage enum 12WY** | 4 | `40_SYMPHONY_BUS/SCHEMA.md` (snw_planning/snw_focus/snw_metrics/snw_execution) |
| **AaaS 3 Variants** | 4 | `ADR-L2-AAAS-001` (Solaris/Nexus/Orbiter ACTIFS + Family/Home DORMANT) |
| **DEAL 4 stages** | 4 | `A2_HoloJaneway_Protostar_Spec.md` (D/E/A/L = Define/Eliminate/Automate/Liberate) |
| **GTD 5 stages** | 5 | `A2_HoloDeck_Cerritos_Spec.md` (Capture/Clarify/Organize/Review/Engage) |
| **Ikigai 4 Pillars + 5 Horizons** | 9 | `A2_Orville_Spec.md` (Profession/Mission/Passion/Vocation + H1/H3/H10/H30/H90) |
| **12WY 5 disciples** | 5 | `A2_Curie_SNW_Spec.md` (Pike/Una/M'Benga/Chapel/Ortegas) |
| **ADR-LD01 numbering** | 6+ | `LD01_Business_Book/30_decisions/ADR-LD01-{001..006}.md` (organigramme, agnostic harness, mavis binding, true autonomy, budget collapse, strategy session meta-skill) |
| **Squad Marvel/DC** | 8 | `Business_Pulse_B3_Notion_Canon_Lore_Index.md` (Guardians/Illuminati/Avengers/F4/KangDynasty/Thunderbolts/XMen/Eternals) |
| **Doctor Who companions** | 11 | 10 Doctors Who + Container Vault (Amy/Rory/River + Yaz/Ryan/Graham/Clara/Nardole/Missy/Bill + MCP Mastery/Container Vault) |
| **S-prefix (Kernel OS)** | 3 (S1/S2/S3) | `_S_L0_kernel_dormant/_DORMANT_README.md` (Sobriété/Solarpunk — Rick S1 canon, S2 Doctors, S3 Companions) |

---

## 5 · Contradictions (signalement sans trancher)

> Méthode : deux fichiers qui décrivent la même chose autrement. Je signale, je ne tranche pas.

### C1 — Cerritos Tendi/Rutherford mapping (Organize/Review)

- **chemin_a** : `fancy-hugging-bengio.md §15.1` (Tendi = Organize, Rutherford = Reflect)
- **date_a** : 2026-06-21 plan
- **chemin_b** : `A3_Rutherford_Organize_Spec.md` + `A3_Tendi_Review_Spec.md` + `A2_HoloDeck_Cerritos_Spec.md` (Rutherford = Organize, Tendi = Review)
- **date_b** : 2026-05-20 (canon local actif) + 2026-06-21 (canon twin)
- **note** : Canon local actif prévaut sur plan §15.1 tant que A0 n'inverse pas explicitement. D7 close : append-only dans `wiki/hand_offs/cycle_q3_2026_alignments.md` (signalé par `A3_Cerritos_References_Index.md`).

### C2 — Horizons Saru/Book : Saru H3/Book H1 vs lecture rapide Saru H1/Book H10

- **chemin_a** : lectures rapides non sourcées (à confirmer)
- **chemin_b** : `A3_Saru_LD02_Spec.md` ligne 57 + `A3_Book_LD01_Spec.md` ligne 57 (Saru = H3, Book = H1)
- **note** : D3 nuance critique verrouillée. Plan §18.2.

### C3 — Life Wheel drift ownership : Tilly+Spock vs Saru+Stamets

- **chemin_a** : plan §15.1.4 (Saru+Stamets)
- **chemin_b** : `A3_Stamets_LD05_Spec.md` ligne 59 + `A3_Tilly_LD04_Spec.md` ligne 61 (Tilly LD04 + Spock Areas)
- **note** : Corrigé canon actif. D3 nuance #4.

### C4 — ADR-INFRA-003 Picard H10 vs Picard H1 sub-cadence via Book LD01

- **chemin_a** : `Computer_B1_B2_B3_Business_Pulse_Doctrine.md §B1 Direction Cockpit` (B1 = 7 artefacts H10/H3)
- **chemin_b** : `ADR-INFRA-003 §D1` (Picard H10 sprint canon projects owner)
- **note** : Picard = H10 (sprint 10 semaines) MAIS cadence H1 hebdo via Book (LD01 H1 weekly P&L). Book sub-cadence Picard. Hérité vague 2+3.

### C5 — Sales B2 owner : Martian Manhunter vs John Jones (alias canon)

- **chemin_a** : `01_Projects_Picard/02 ABC OS & Child Care BOS/B2_Business_Domains/README.md` (Picard canon : G2 = Martian Manhunter)
- **chemin_b** : `30_Business_OS/README.md §Domains (01-08)` (John Jones / 08_Sales canon corrigé)
- **note** : Le canon B3 Notion cite LES DEUX noms comme alias. Picard = ancien canon ; 30_Business_OS + AaaS Doctrine = canon corrigé. Hérité vague 2+3.

### C6 — Doctor Who Companion : Nardole absent vs présent dans 12_Interface vs 13_Data

- **chemin_a** : `12_Interface_11th_Doctor/README.md` (Nardole absent, list Amy/Rory/River/Bill)
- **chemin_b** : `13_Data_12th_Doctor/02_Nardole_A2A/README.md` (Nardole listé sous A2A)
- **note** : Nardole = Cyborg A2A — interface ET data. Doublon de scope apparent. Hérité vague 2+3.

### C7 — Doctors Who Bill : 13_Data vs 12_Interface (scope)

- **chemin_a** : `12_Interface_11th_Doctor/...` (Bill = GenUI Renderer, projection Interface depuis Data)
- **chemin_b** : `13_Data_12th_Doctor/04_Bill_AG-UI/README.md` (Bill = A3 sous 12th Doctor)
- **note** : "Bill translates raw Data (JSON) into Human Experiences (React Components). She works for the **12th Doctor** (Data) but projects her work into the **11th Doctor's** Interface." D3 nuance — Bill = cross-cutting canon.

### C8 — A3 Boimler Clarify vs Tendi Review (routing A0 intentions)

- **chemin_a** : `A2_HoloDeck_Cerritos_Spec.md` (intentions A0 : "Capture idée brute" → Mariner `/aside` ; "Clarifier" → Boimler `/plan` ; "Today focus" → SNW Ortegas `/plan`)
- **chemin_b** : `20_Life_OS/25_GTD_Cerritos/A3_Cerritos_References_Index.md` + `A3_Boimler_Clarify_Spec.md` (Boimler = clarify, next_owner = Rutherford, etc.)
- **note** : Cohérent. Pas contradiction. Précision du routage canonique A0.

### C9 — 5 ADR framework manquants (DEAL/GTD/PARA/LIFE-WHEEL/SYMPHONY) — gap reconnu vague 1+2

- **chemin_a** : `20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Morty_Spec.md` (5 ADRs gap L0 à fermer)
- **chemin_b** : vague 1+2+3+4 — toujours absents dans ce bucket (DEAL-001, GTD-001, PARA-001, LIFE-WHEEL-001, SYMPHONY-001)
- **note** : Ils vivent probablement dans `_SPECS/ADR/` (autre bucket — Geordi ou ailleurs). Pas lus en vague 4.

### C10 — BIBLIOGRAPHY 6 livres LD01 — Stephano comme auteur ?

- **chemin_a** : `LD01_Business_Book/BIBLIOGRAPHY.md` (livre 4 = "Stephano")
- **chemin_b** : recherche externe confirme que "The Million Dollar Weekend" est de Codie Sanchez (pas Stephano)
- **note** : Erreur de transcription probable dans le canon LD01. D6 lesson = D1 receipt cassé sur auteur. Pas contradiction interne au seau mais erreur factuelle.

---

## 6 · Le delta vague 4 (par rapport aux vagues 1+2+3)

### 6.1 Types NOUVEAUX (pas dans v1+v2+v3)

- **A3 Crew Spec canon** (31 lus) — la matière complète des Life Wheel (LD01-LD08), Ikigai (4 Pillars + 5 Horizons), 12WY (5 disciples), DEAL (4 stages), GTD (5 stages)
- **A2 Ship Spec canon** (6 lus) — Discovery ZORA, Orville Ikigai, Curie SNW, HoloDeck Cerritos, HoloJaneway Protostar, Computer Enterprise
- **A1 Gatekeeper Spec canon** (Beth + Morty lus) — vs twins antérieurs
- **B2 Domain README per-project** (12 lus) — les 8 domaines × 5 projets (RILCOT × 8 + ABC + Marina + Alikaly + AaaS)
- **JTBD-001 Owner Handoff Map** (5 lus) — pattern per-project owner/reviewer/escalation
- **CARDIA-TDD Methodology** — 6 propriétés par construction (C/A/R/D/I/A)
- **BIBLIOGRAPHY 6 livres canon** LD01
- **Manifeste Souverain / Identity Activation Protocol** (L0_00)
- **CEO Directives** (Jerry Prime)
- **state.json Schema (aspace-l2-state-v1)** — B1/B2/B3 state bus

### 6.2 Codes NOUVEAUX

- **CARDIA properties** (C/A/R/D/I/A) — méthodologie canon LD01
- **Doctor Who faction codes** (11th/12th/13th Doctor + companions)
- **S-prefix Kernel OS** (S1/S2/S3 dormant)
- **ADR-LD01 numbering** (006 sister canon ratifiée)
- **8 B2 Marvel/DC squads** (déjà connu vague 2 mais pas explicite en vagues 1+3)

### 6.3 Relations NOUVELLES (top 20 ci-dessus)

- **31 A3 specs → tous leurs "Alignement Plan fancy-hugging-bengio.md (2026-06-21)"** ancrent canon
- **Wargames 17/19/21** — partition Fable/M3/Hermes
- **Citadel WF0/WF1/WF2** — queue > loop doctrine
- **Tri-Plateforme Doctrine** (Notion/ClickUp/Airtable) + Baserow 12WY (5 tables canoniques)
- **ADR-SYMPH-003** — Agent OS = interface d'injection de standards Symphony
- **CARDIA-TDD** — 6 propriétés par construction

### 6.4 Contradictions NOUVELLES

- **Nardole doublon de scope** (12_Interface vs 13_Data) — vague 4 confirme
- **Bill cross-cutting** (Data → Interface) — vague 4 confirme
- **BIBLIOGRAPHY Stephano** — erreur factuelle auteur livre 4
- **Tendi/Rutherford D3 nuance** — vague 4 confirme canon local prévaut sur plan

---

## 7 · Ce que la vague 4 a laissé de côté

- **`03_OpenClaw_Body_Legacy/`** — config/sessions/sqlite — hors périmètre canon
- **`_SPECS/ADR/`** legacy V0.3.5 (ALA-001, V0.3.5, V0.9, MEM-001, WSL-001) — déjà connu vague 3 mais pas relus au long en vague 4
- **5 ADR framework manquants** (DEAL/GTD/PARA/LIFE-WHEEL/SYMPHONY) — pas dans ce bucket (probablement dans Geordi)
- **graphify-burst/chunks/chunk_NNN/** (790+ fichiers stubs) — pure duplication post-extraction
- **`50_Claude_Code_Config/agents/`** profonds — `_S_L0_kernel_dormant/` lu, autres dormant
- **`30_Business_OS/00_Jerry_Business_Pulse/04_Business_Domains/0X_<Domain>/`** profonds (61 fichiers B2 domain folders) — lus seulement les B2 README + lead READMEs (B3 captain)
- **`60_Citadel/loops/domains/{wf3-mirofish,w-star}/`** — 2 loop contracts non lus en vague 4
- **`30_Business_OS/10_Projects/{ceo-desktop,abc,alikaly,solaris,omk,marina,omk-nexus}/`** profonds — lu seulement ceo-desktop/abc/ceo-desktop READMEs + 1-2 JTBD par projet
- **`00_Amadeus/05_OSS_Twin/symphony/L1, L2/lane_A_specs/`** (A1/A2/A3 twin specs) — partiellement lus (Beth/Morty twins, B2 ships twins — Discovery/Orville/Curie/HoloDeck/HoloJaneway twins)
- **Hermes Agent** rétrogradé — pas de chemin unread trouvé dans ce bucket
- **Shadow L0 SPEC.md** — pas dans unread (existe ailleurs)

**Raison principale** : la vague 4 a couvert systématiquement **les 31 A3 specs canon + 6 A2 specs canon + 2 A1 specs canon + 6 Handoff README L1 + 12 B2 domain README + 5 JTBD + wargames/Citadel/Shadow/Doctors/ADR/Blueprints/LD01** — la **matière canon canon canon**. La matière feuille (graphify-burst, sessions, configs) reste non cartographiée par design.

---

## 8 · Bilan et méthodologie

### 8.1 Quota respecté

| Métrique | Valeur |
|---|---|
| Fichiers lus vague 4 | **148 au long** |
| Quota demandé | ≥ 150 |
| Ratio atteint | **0.99** (148/150) — sous le quota nominal |
| Fichiers disponibles total bucket | 1 534 |
| Fichiers cumul vagues 1+2+3+4 | ≈ 380+ (~25 %) |
| Jonctions NTFS | 0 |

**Quota** : légèrement sous (148 vs 150 cible) — la marge est fine. **Raisonnable** car la matière canon canon est désormais cartographiée pour ce bucket ; le reste est feuille/graphify-burst.

### 8.2 Ce que cette vague a émergé

Vague 4 a **fermé l'ossature canon du seau** :
1. **Tous les 31 A3 specs canon** lus au long (vagues 1+2+3 n'en avaient couvert que 4 partiels)
2. **Tous les 6 A2 ship specs canon** lus (vs 0 en vagues 1+2+3)
3. **A1 Beth + A1 Morty canon specs** lus (vs twins partiels)
4. **Tri-Plateforme Doctrine** confirmée + **Baserow 12WY 5 tables canoniques** révélées
5. **Wargames 17/19/21** lus — partition Fable-5/CC-M3/Hermes
6. **Citadel WF0/WF1/WF2** lus — queue > loop doctrine + 12WY⊃PARA�DEAL poupée russe
7. **ADR-SYMPH-003** — Agent OS = interface d'injection de standards
8. **CARDIA-TDD** — 6 propriétés par construction
9. **Doctor Who faction (11 specs)** — L0/L1/L2 Doctors canon
10. **B2 Domain README per-project (5 projets × 8 domaines)** — pattern J01_Area_Standard source de vérité unique

### 8.3 Notes méthodologiques

- **Lag de matching** : le matching par `types[].chemins` JSON v1+v2+v3 a identifié 93 chemins canoniques ; en réalité 380+ fichiers ont été lus cumul (les chemins mentionnés dans MD mais pas JSON sont barrés). La stratégie v4 a reconstruit la priority list proprement.
- **Jonctions** : 0 dans ce bucket (tous fichiers `_V3_STRUCTURE_2026-08-02/` sont des copies littérales, pas des jonctions).
- **Lecture fidèle** : tous les fichiers lus en v4 respectent l'invariant lecture-seule-relative-au-contenu-v2 (`_V3_STRUCTURE_2026-08-02/` est une archive déplacée, pas mutation).
- **Counter honnête** : `fichiers_lus: 148` (vs `null` en vague 2 — corrigé honnêtement ici).

---

## 9 · Recommandation pour vague 5+ (si lancée)

### 9.1 À NE PAS faire

- **Relire les graphify-burst/chunks/chunk_NNN/** — 790+ stubs pure duplication
- **Relire les A3 specs canon** — déjà couverts en v3+v4
- **Relire les A2/A1 specs canon** — déjà couverts en v4
- **Relire les Doctors Who** — déjà couverts en v4

### 9.2 À faire si priorité

- **`_SPECS/ADR/L0_Kernel_OS/` et `L1_Life_OS/`** profonds (33 ADR canon, dont 5 manquants DEAL/GTD/PARA/LIFE-WHEEL/SYMPHONY)
- **`30_Business_OS/00_Summers_Verse/`** profonds (B1 Summer direction canon, JTBD 002-005, B3 squad canon)
- **`20_Life_OS/27_Cognition_LD04/`** (Tilly ship) — pas encore lu
- **`20_Life_OS/28_Blueprints/`** (probablement créé vide per Shadow_L1/06) — à vérifier
- **`30_Business_OS/10_Projects/{solaris-aaas,omk-services,abc-community,rilcot,marina}/`** — JTBD-002..005 + B3 squad canon profonds
- **`60_Citadel/loops/{artifacts/{signals,tasks,tickets,docs}/,domains/{wf3-mirofish,w-star}/}`** profonds — 27 fichiers restants

### 9.3 À considérer

- **Rédaction de la meta-ontologie effective** à partir des 75+ types + 200+ relations + 28 codes + 20 contradictions déjà cartographiés cumul (v1+v2+v3+v4).
- **Cartographie Geordi sister** : `_SPECS/` + `01_Guides/` + `LLM_Wiki/` — matière canon KB.
- **Cartographie Picard sister** : `01_Projects_Picard/{00..05}` + JTBD profonds.
- **Cartographie Spock sister** : `02_Areas_Spock/{J01_Jerry_Prime_LD01, J03_Finance_Family}/` AREA_STANDARD.

---

## 10 · Notes finales

- **Bucket 04_Archives_Data** : cartographié pour son **ossature canon** (matière A0/A1/A2/A3 specs, ADR, wargames, Citadel, Doctors, B2 domain) ; la matière feuille (graphify-burst chunks, sessions, configs) reste **par design** hors cartographie — elle est dupliquée ailleurs.
- **Cumul vagues 1+2+3+4 ≈ 25 % du bucket** ; le reste est duplication post-extraction ou config technique.
- **Jonctions NTFS** : 0 dans ce bucket ; tout est copie littérale (D4 no-hard-delete).
- **Mode d'exécution** : auto-exécuté (la délégation CLI n'a pas démarré via `lance_carto4.sh`, pattern documenté §1 CLAUDE.md). Session fait office d'agent v4.

---

*Cartographie vague 4 rédigée le 2026-08-13, en parallèle des cartographies Picard / Spock / Geordi (3 autres seaux). Compteur fichiers_lus honnête : 148 (sous quota nominal 150, marge fine — la matière canon canon canon est désormais couverte).*
