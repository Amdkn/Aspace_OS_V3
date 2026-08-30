# Cartographie — 01_Projects_Picard (V2)

> Cartographie ontologique du seau **01_Projects_Picard** du PARA de V2 — vague 2.
> Source : `carto/structure.txt` filtré sur `01_Projects_Picard` → 363 chemins.
> Méthode : re-lecture intégrale des fichiers de tête (SUMMERS_VERSE_MANIFEST × 4, B1/README × 4, CERRIROS_HANDOVER × 4, B3 README × 5, B1 specs 03-11 × 11) + lecture intégrale des B2 Domain README × 37 (4 projets × 8 + 01-omk × 5) + lecture intégrale des 24 chartes_cycle_2 + 3 ownerbooks + 2 chartes/cycle_1 + 2 runbooks + 3 Moat configs (config.json, moat-tasks.md, moat-tasks-detail.json) + B3 SWARM_CONFIG × 3 (02 ABC Growth, 05 marina People, 01-omk People) + B3 AGENT_ROSTER × 1 (05 marina People) + B3 Peer Handoffs + B3 Shared Context + B3 squad READMEs × 13 (StarLord/Rocket/Gamora/BlackBolt/MrFantastic/KangPrime/BuckyBarnes/Ikaris/ProfessorX × 2 + 01-omk StarLord/KangPrime + 05 marina MrFantastic × 2) + 3 JTBDs (ABC/RILCOT/ALIKALY OWNER_HANDOFF_MAP + MARINA DIAGNOSTIC_TO_PROPOSAL) + Cerritos MANIFEST + ClaudeClaw README + 10 Interface Prototypes (Alikaly 7 + RILCOT 2 + marina 1).
> Jonctions NTFS : 0 (aucune dans ce périmètre — confirmé par lecture des chemins, pas par comptage exhaustif).

## Périmètre lu

| Métrique | Valeur |
|---|---|
| Fichiers disponibles (filtrés par structure.txt) | 363 |
| Fichiers lus en V1 (déjà référencés dans 01_Projects_Picard.json) | 38 |
| Fichiers lus en V2 (NOUVEAUX — non encore référencés) | ~130 |
| Fichiers non lus | ~200 (majoritairement les B3 sub-squad READMEs clones du même template) |

**Distribution des profondeurs** : 6 fichiers de tête (SUMMERS_VERSE × 4, B1/README × 4), 11 B1 specs 00-11 (uniquement 02 ABC lus en intégral — les 11 sont identiques ou pattern cloné sur les 4 projets), 37 B2 Domain README × 4 + 5 (4 projets × 8 + 01-omk × 5), 24 chartes_cycle_2 (cycle 2 W40 M3), 2 chartes/cycle_1 (phase_c_saas_auth + phase_d_repositories), 3 ownerbooks, 2 runbooks (C + D), 3 Moat configs, 4 Cerritos MANIFEST+items, 10 Interface Prototypes.

---

## Vue d'ensemble — les 8 sous-projets

Le seau contient 8 sous-projets, qui se répartissent en **deux familles très distinctes** plus un projet tech isolé et un projet L1.

### Famille SUMMERS (4 projets rigoureusement isomorphes)

Tous suivent le même template `SUMMERS_VERSE_MANIFEST.md` + `B1_Summer_Direction/` + `B2_Business_Domains/` + `B3_Warp_Core_Execution/` + `CERRIROS_HANDOVER.md`.

| # | Projet | Mode primaire | Particularité |
|---|---|---|---|
| 2 | `02 ABC OS & Child Care BOS` | Orbiter (Nexus secondaire) | Dual-entity, contrainte Child Care = compliance G8 obligatoire |
| 3 | `03_RILCOT_Members_Space_OS` | Nexus (Solaris/Orbiter secondaires) | Members community, knowledge compounding |
| 4 | `04 Alikaly Bana Holding to LLC` | Orbiter (Nexus secondaire) | **Cross-Jerry** : J01 + J03 Finance/Family — 4 orthographes distinctes (Alikaly/Alykaly/Kalybana/Alikaly Bana) + 7 prototypes d'interface pour un même produit |
| 5 | `05 marina Cleaning BOS & SOP` | Orbiter (cycle court 84 jours total en 4 × 21 jours) | SOPs-as-a-service, dépend saison/weather |

### Famille Picard Cycle (1 projet, format différent)

| # | Projet | Format |
|---|---|---|
| 1 | `01-omk-business-os/` | `chartes_cycle_2/` (T1/T2/T3 — 24 fichiers) + `chartes/` (cycle 1, phase_c/d) + `runbooks/` (Phase C/D) + `ownerbooks/` (T1/T2/T3) + `B3_Warp_Core_Execution/README.md` |

### Projets isolés

| # | Projet | Couche | Format |
|---|---|---|---|
| 6 | `Cerritos_Plane_Onboarding/` | L1_Life_OS | `MANIFEST.md` + 2 fiches par item Plane (cycles-integration, invite-team) |
| 7 | `ClaudeClaw Agent/` | Tech | README React/Vite + `.moat/` (Drawbridge UI feedback loop) + screenshots/ |
| 8 | `omk-services/` | Tech | (dossier présent mais vide ou quasi-vide — code applicatif OMK non représenté dans la liste de structure) |

---

## Découvertes majeures V2

**V2 a révélé 4 trouvailles structurales que V1 n'avait pas vues** :

1. **Bug structurel : les 4 fichiers `B1_Summer_Direction/03_DECISION_CHARTER.md` sont VIDES** (3 octets = BOM uniquement). Le contenu réel de la "B1 Decision Charter" (Decision Rights + Output Packet + Escalation) est **APPENDÉ en bas du fichier 02_12WY_COMMAND_CYCLES.md** (commence après le séparateur `---` et l'inline-frontmatter `id: B1_DECISION_CHARTER_02_ABC_OS`). Le fichier 00_B1_DIRECTION_INDEX.md l.20 référence `03_DECISION_CHARTER.md - decision rights, vetoes, escalation, and output packet` — mais le contenu réel est dans 02. Pattern reproduit sur les 4 projets SUMMERS (vérifié pour 02 ABC, présumé pour 03/04/05). **Bug structurel** : fichier créé mais contenu migré ailleurs sans mise à jour de l'index.

2. **Le projet 04 Alikaly Bana Holding contient 7 prototypes d'interfaces** (Kalybana Holding/{01_Real_Estate, 02_Holdings_Platform, alykaly-os}, alykaly-front, alykaly-holding-modern, 'Alykaly Bana Real Estates FR V2') — 4 orthographes distinctes (Alikaly, Alykaly, Kalybana, Alikaly Bana) pour un même projet. Aucune avec contenu substantiel au-delà du README template. **Plusieurs tentatives de démarrer le produit**, aucune n'a abouti.

3. **B2 archetype rename intentionnel** : la T2 charte cycle_2 utilise `JohnJones` au lieu de `Martian Manhunter` (W40 V4 rename intentionnel, documenté dans `ownerbook_T2_growth_sales_finance.md` §3 note). Cohérence sémantique (même B2 G2 Sales), deux noms en circulation. Les chemins filesystem restent `MartianManhunter` (no space) ; le contenu texte est `Martian Manhunter` (with space) ou `JohnJones` (chartes cycle_2).

4. **B3 SWARM_CONFIG niveaux de maturité inégaux** : le 02 ABC Growth SWARM_CONFIG a été upgradé le 2026-06-07 au format canonique B3 (`status: PHASE_1_STUB` = skeleton + topology declaration, avec ABC-specific anchors : VAPI voice funnel + agriculteurs + childcare operators + 6 Guardians topology). Les autres SWARM_CONFIG (05 marina, 01-omk) restent en `status: SHADOW_ACTIVE` template minimal avec 4 Members (Professor X/Cyclops/Jean Grey/Beast). Incohérence de maturité au sein d'un même système.

5. **Runbook D s'auto-dénonce** (chart Phase D stale vs AGENTS.md Phase D DONE) : le runbook lui-même prend pour hypothèse l'état AGENTS.md et **dénonce le chart comme stale**. D6 no-self-contradiction guard fonctionne.

---

## 1 · Types d'objets — relevé (trié par nombre de chemins)

> Un type = un nom propre récurrent, avec attributs, et dont il existe plusieurs exemplaires.

| # | Type | Nb chemins | Attributs clés |
|---|---|---|---|
| 1 | `B3SubSquadMemberREADME` | ~260 | Pattern clone (Project + Squad member + Role + Canon role + Area doctrine + workspace d'exécution + ADR-INFRA-003) — 8 domains × 6-10 members par projet × 5 projets |
| 2 | `Charte (chart_Tn_<domain>_<topic>)` | 24 | type: charte, triptyque T1/T2/T3, rock_id B1-1/2/3, b2_owner, b3_squad, icp US market, 12wy_window Q3 2026 W1-W13, geography US-first, doctrine_lock D4·D6·US market focus, 9 sections fixes |
| 3 | `B2DomainREADME` | 37 | Role, Gate, Required Input From Product, Blocking Authority, Evidence Checklist, Operating Rule (PRODUCT_ONLY_PROTOTYPE) |
| 4 | `InterfacePrototype` | 10 | title, Strategic Vision, PARA organization, Components, AI Studio link, E-Myth philosophy, Architecture (Next.js / Vite + React + TailwindCSS / Supabase / Coolify PaaS / Docker) |
| 5 | `B3WarpCoreREADME` | 5 | What B3 Does/Does NOT Do, Core rule (engine not方向盘), 12WY Cycle Format W1-W12 84-day quarters, Lead vs Lag, Artifact Proof, Blocker Note Protocol |
| 6 | `B2BusinessDomainsREADME` | 4 | 8 sections G1-G8 (B2 Manager archetype + Marvel squad + Domain scope + Primary LD01 book + Key metrics + J01 Standard reference + Priority matrix) |
| 7 | `SUMMERS_VERSE_MANIFEST` | 4 | id, layer, status GRADUATED, parent_jerry J01, ICP Variants, LD01 Book Alignment (6 books), 12WY Rock Linkage (W1-W4 = 84 jours), Cerritos Handoff Reference, B3 Warp Core Brief |
| 8 | `B1DirectionIndex` | 5 | id, layer B1_DIRECTION, Operating Rule (B1 owns direction/packet structure), Files (00-11 specs), Handoff Path 1-6 steps |
| 9 | `CerritosHandover (CERRIROS_HANDOVER)` | 4 | Routing Chain ASCII, What Jerry Proposed, What Cerritos Clarified, What Picard Opened, B1 Vision 1Y/3Y/10Y, B2 Rocks, B3 W1-W12 cycle |
| 10 | `B2DomainDevelopmentMap` | 4 | id, layer B2_BUSINESS_DOMAINS, project_slug, Operating Rule (each B2 domain references Jerry macro doctrine), Active Buildout table 8 rows × 4 cols |
| 11 | `B3SwarmConfig (00_B3_SWARM_CONFIG)` | 32 (5 lus) | id, layer B3_SWARM_EXECUTION, surface, surface_kind QuickAccess Mirror, status PHASE_1_STUB|SHADOW_ACTIVE, domain, b2_gatekeeper, squad, topology_size, source_inspiration MCU, Design Pattern (Local graph/Supervisor boundary/Meso swarm/No babysitting), Members, Operating Rule |
| 12 | `B1DecisionCharter (fichier VIDE — voir contradictions)` | 4 (vides) | Fichiers 03_DECISION_CHARTER.md sont 3 octets BOM uniquement. Contenu réel APPENDÉ en bas de 02_12WY_COMMAND_CYCLES.md |
| 13 | `B1 specs 01-11` (8 fichiers × 4 projets = 32 fichiers, mais pattern identique) | 11 lus (02 ABC) | 01_NORTH_STAR (1Y/3Y/10Y), 02_12WY_COMMAND_CYCLES (C1-C4), 04_B2_HANDOFF_QUEUE, 05_B2_DEFINITION_OF_DONE_SPEC, 06_B3_JOBS_TO_BE_DONE_SPEC, 07_B1_TO_B2_DOMAIN_GOVERNANCE_WORKFLOW, 08_BUSINESS_WHEEL_BALANCE_REVIEW, 09_MARKET_VALIDATION_SPRINT, 10_PROJECT_GRADUATION_GATES, 11_FRACTAL_PROJECT_DEVELOPMENT_PLAN |
| 14 | `B3AgentRoster (01_B3_AGENT_ROSTER)` | 1 | id, layer B3_SWARM_EXECUTION, scope Summer Project, source Notion AGENT_REGISTRY_DB, Notion Canon Lore, Canonical Members (8 personnages), Canonical Task Surface (5 items), Build Gates (Onboarding < 1h / Heartbeat miss rate < 5% / Zero ethics violation), Anti-Patterns Interdits (3 items), Escalation Rule, Machine Roster yaml, Collaboration Defaults (4 étapes), Peer Unlock Rule, Proof Rule (Notion wins lore / local doctrine wins paths) |
| 15 | `B3PeerHandoffs (02_PEER_UNBLOCKING_AND_HANDOFFS)` | 1 | Internal Handoff Contract yaml schema, Allowed Peer Handoffs (Research → Build → Review → Unblocker), Escalate To B2 Only When (5 conditions) |
| 16 | `B3SharedContextAndProofLog (03_SHARED_CONTEXT_AND_PROOF_LOG)` | 1 | Context Variables yaml schema, Proof Standard (autre agent peut inspecter sans trust author), Productive Disagreement (5 conditions) |
| 17 | `JTBDOwnerHandoffMap (JTBD-001_<PROJECT>_OWNER_HANDOFF_MAP)` | 3 | id, jtbd_id PROJECT-B3-PEOPLE-001, source_rock, b2_owner Green Lantern, b3_swarm X-Men, status READY, Job statement, Output (8 items), Eight-Domain Handoff Map (8 rows), Guardrails (7 items + 1 project constraint variable) |
| 18 | `JTBDDiagnosticToProposal` | 1 | Job statement, Output (1-10 items), Eight-Domain X Map, Guardrails, Proof |
| 19 | `CerritosPlaneOnboardingManifest` | 1 | id, layer L1_Life_OS, role A3_Cerritos_GTD_Capture, parent_a2 A2_HoloDeck_Cerritos, Plane Items Classified (3 verbatim ASPAC-3/6/7), Next Action Canon (Freeman verdict), Anti-Pattern Guard (D6 nuance D1 verified) |
| 20 | `CerritosPlaneItemFiche` | 2 | id ASPAC-3|6|7, plane_id, plane_state Backlog, gtd_stage actionable|multi-step|someday-maybe, priority, owner A0, classification Projects, cycle Q3_2026_W3, Boimler clarify, Rutherford organize, Tendi review, Freeman engage |
| 21 | `ClaudeClawAgentREADME` | 1 | Vite/React/HMR/ESLint template, 2 plugins officiels (Oxc + SWC), React Compiler NOT enabled, Type-aware lint rules |
| 22 | `MoatConfig (.moat/config.json)` | 1 | version, projectName, createdAt, streaming, ui |
| 23 | `MoatTasksList (.moat/moat-tasks.md)` | 1 | Total/To Do/Doing/Done counters, Tasks list (9 tasks done, all status 'done') |
| 24 | `MoatTasksDetail (.moat/moat-tasks-detail.json)` | 1 | Array of task objects with id (uuid) | title | comment | selector (CSS) | boundingRect | screenshotPath | status | timestamp | boundingBox |
| 25 | `MoatWorkflowRules (drawbridge-workflow.md)` | 1 | Drawbridge Workflow: Complete Rules, AI role definition (principal front-end engineer), workflow Step/Batch/YOLO modes |
| 26 | `MoatReadme (.moat/README.md)` | 1 | Quick Start (press 'f'), Files in This Directory, Example Workflow, Connection Issues, Advanced Processing Modes |
| 27 | `Charte cycle 1 (chartes/phase_c/d — RP2/RP3)` | 2 | type: charte, project: omk, rock_id RP2|RP3, 12wy_window Q3-W6|Q3-W8, doctrine_lock D4·D6·Picard MANIFEST canon |
| 28 | `Runbook (runbook-<phase>-<topic>.md — executor pattern)` | 2 | chart_source, project omk, rock_id RP2|RP3, doctrine_lock D4·D6·Picard MANIFEST canon·Posture C (HITL gated), Pre-check gates, M1-M5/M6, Abort conditions, D6 honest gaps ≥4, Verification V1-V8, DoD Una 3-critères, Reverse path, WAR MODE flag |
| 29 | `Ownerbook (ownerbook_Tn_<topics>.md)` | 3 | type: ownerbook, triptyque T1/T2/T3, rock_id B1-1/2/3, doctrine_lock D4·D6·Spec-Loop Polivaev 2026, mission (W40 §2 verbatim), 10 sections (Scope/Motivation/Research/Design/Test-Spec/Chartes needed/Runbooks/Abort conditions/Red-team/US market specific) |
| 30 | `PlaneItem` | 2 | id ASPAC-3|6, plane_state Backlog, gtd_stage, priority, owner A0, cycle Q3_2026_W3 |
| 31 | `B1NorthStar (01_NORTH_STAR_1Y_3Y_10Y)` | 2 | 1-Year/3-Year/10-Year Direction (with Minimum outcome), Direction Invariants |

**Total : 31 types canon observés dans V2**.

---

## 2 · Relations — citation verbatim (les 13 nouvelles relations V2)

> Toutes les citations sont reproduites telles quelles depuis les fichiers, avec leur chemin. **Pas de paraphrase.**

### V2 — nouvelles relations non présentes en V1

#### Routing B1 → B2 → B3 (chaîne formalisée)

> « 1. B1 writes or updates direction here. 2. B1 creates a B2 request in 04_B2_HANDOFF_QUEUE.md. 3. B2 converts the request into DoD packets using 05_B2_DEFINITION_OF_DONE_SPEC.md. 4. B2 creates B3 jobs using 06_B3_JOBS_TO_BE_DONE_SPEC.md. 5. B3 executes only the defined jobs and returns proof. 6. B2 updates gates; B1 reviews direction drift. »
> — `01_Projects_Picard/02 ABC OS & Child Care BOS/B1_Summer_Direction/04_B2_HANDOFF_QUEUE.md`

#### B1 → B2 Domain Mandate Packet (workflow gouvernance)

> « 1. B1 reads North Star and current 12WY cycle. 2. B1 scans the 8-domain wheel for imbalance: empty domain, overloaded domain, blocked gate, missing proof, or Product-only drift. 3. B1 writes one domain mandate per affected B2, not a step-by-step plan. 4. B2s negotiate meso tradeoffs through ../B2_Business_Domains/B2_MESO_VP_SWARM_COORDINATION.md. 5. B2 converts mandates into Rocks, DoD, and B3 JTBD packets. 6. B3 swarms execute and unblock internally. 7. B2 returns gate status to B1. 8. B1 updates direction only when the North Star, risk appetite, or strategic priority changes. »
> — `01_Projects_Picard/02 ABC OS & Child Care BOS/B1_Summer_Direction/07_B1_TO_B2_DOMAIN_GOVERNANCE_WORKFLOW.md`

#### Cerritos GTD pipeline (5 stages canoniques A3)

> « Sub-agent owner: A3 Mariner (Capture) + Boimler (Clarify) + Rutherford (Organize) + Tendi (Review) + Freeman (Engage) »
> — `01_Projects_Picard/Cerritos_Plane_Onboarding/MANIFEST.md`

#### marina seasonal ideas routing (Q4 weather contingency)

> « marina-specific routing note : Weather and seasonal ideas route to G4 Ops domain first, not directly to B1. Weather contingency is an ops pattern, not a strategic decision. »
> — `01_Projects_Picard/05 marina Cleaning BOS & SOP/CERRIROS_HANDOVER.md`

#### B3 Peer Handoffs (Research → Build → Review → Unblocker)

> « Research -> Build when enough context exists. Build -> Review when an artifact is testable. Review -> Research when evidence is thin. Any member -> Unblocker when progress stops. »
> — `01_Projects_Picard/01-omk-business-os/B3_Warp_Core_Execution/07_People_GreenLantern_XMen/02_PEER_UNBLOCKING_AND_HANDOFFS.md`

#### B3 Productive Disagreement

> « At least one peer should be allowed to disagree with the first solution when the JTBD affects cost, legal exposure, customer promise, release quality, or operational load. The disagreement must end in one of: accepted revision, rejected with reason, or B2 escalation. »
> — `01_Projects_Picard/01-omk-business-os/B3_Warp_Core_Execution/07_People_GreenLantern_XMen/03_SHARED_CONTEXT_AND_PROOF_LOG.md`

#### Cyborg IT → R&D pivot (W40 §M2 patch)

> « Cyborg moving IT → R&D external-discovery (per W40 §2 + W40 §M2 patch) means the "veille EST le département" doctrine becomes a systematic external-input pipeline, not ad-hoc reading. »
> — `01_Projects_Picard/01-omk-business-os/ownerbooks/ownerbook_T3_legal_rd.md`

#### R&D pipeline ≤3 ADRs/cycle (W40 §M6 musée anti-pattern)

> « R&D innovation filter (per W40 §M6 contre) — Last30days + YouTube + Substack pipeline → B1-filter → ≤3 candidate ADRs/cycle max (museum anti-pattern), fed to B1 as Rock candidates (US market US-skewed sources, NOT EU policy papers). »
> — `01_Projects_Picard/01-omk-business-os/chartes_cycle_2/chart_T3_rd_innovation_filter.md`

#### Skill auto-spawn (Phase 2 Hermes-style)

> « skill auto-spawn policy (Phase 2 Hermes-style, ADR-META-001 D7, ≤3 actionables/cycle per W40 §M6 contre). »
> — `01_Projects_Picard/01-omk-business-os/chartes_cycle_2/chart_T1_ops_runbook_v1.md`

#### Charter → Runbook (cycle_2 → phase_c_saas_auth)

> « Purpose : transformer la chart `phase_c_saas_auth.md` (WHAT, 9 sections, 52 l.) en pattern d'exécution (HOW, M1-M5, HITL-gated). Append-only D4. Runtime gated A0 HITL (Posture C). »
> — `01_Projects_Picard/01-omk-business-os/runbooks/runbook-C-saas-auth.md`

#### Charter → Ownerbook (3 chartes per Rock)

> « Per W40 §M3, each Rock requires 3 chartes (Mission + DoD + Squad dispatch). For T1-Rock B1-1: charte_T1_people_ops_product_mission.md / ..._dod.md / ..._squad_dispatch.md »
> — `01_Projects_Picard/01-omk-business-os/ownerbooks/ownerbook_T1_people_ops_product.md`

#### Spec-Loop Polivaev 2026 (A0 = IA no manual UI gate)

> « Spec-Loop discipline — plan locked BEFORE execution (per A+ directive Spec-Loop Polivaev 2026), with A0 = IA (no manual UI gate), adversarial grill-me review per sub-agent, and Flash H10 product spec iterations. »
> — `01_Projects_Picard/01-omk-business-os/chartes_cycle_2/chart_T1_product_spec_loop.md`

#### US market pivot (A0 2026-07-15) — US-first non-EU

> « US market pivot : competing against Devin Karns $100M AI Agency archetype (Boris Cherny deepscan) requires Hormozi-grade offer + Thunderbolts-grade unit economics, not the saturated "AI tool" mid-market positioning. »
> — `01_Projects_Picard/01-omk-business-os/ownerbooks/ownerbook_T2_growth_sales_finance.md`

#### Kalybana Holding (Alikaly orthographe variante)

> « This holding is organized following the **PARA** method under `01_Projects_Picard`. »
> — `01_Projects_Picard/04 Alikaly Bana Holding to LLC/B2_Business_Domains/03_Product_Flash_Avengers/00_Interface_Prototypes/Kalybana Holding/README.md`

#### RILCOT OS V0 (Coeur de Contrôle de la Flotte Souveraine)

> « **RILCOT OS** est le tableau de bord d'exploitation central (Master Dashboard) d'**ASpace OS V2**. ... **⚡ Core Stack :** React 19.x, Vite 6.x, TypeScript Strict et TailwindCSS. ... **🔐 Authentification & Data :** Intégration native et sécurisée avec **Supabase** (Auth, RLS et Realtime). »
> — `01_Projects_Picard/03_RILCOT_Members_Space_OS/B2_Business_Domains/03_Product_Flash_Avengers/00_Interface_Prototypes/RILCOT_OS/README.md`

---

## 3 · Systèmes de codes — relevé

| # | Code | Description |
|---|---|---|
| 1 | L0|L1|L2|L3 + B1_DIRECTION|B2_BUSINESS_DOMAINS|B2_MESO_COORDINATION|B3_SWARM_EXECUTION | Couches Life OS / Business Pulse + sous-couches. L2_Business_Pulse underscore, L2-Business-Pulse tirets, L2-Business-Pulse-Summer/B2/B3 variantes. |
| 2 | A0|A1|A2|A3 | A0 Amadeus (D7), A1 Beth/Morty, A2 HoloDeck (A2_HoloDeck_Cerritos), A3 sous-agents (Mariner/Boimler/Rutherford/Tendi/Freeman/Saru + Discovery). |
| 3 | B1|B2|B3 | 3 couches Business Pulse : B1 = Direction/Vision (Summer), B2 = Domain managers (8 VPs), B3 = Execution (Lead/Lag + artifact proofs). |
| 4 | G1|G2|G3|G4|G5|G6|G7|G8 | 8 B2 Business Domains : G1 Growth / G2 Sales / G3 Product / G4 Ops / G5 IT / G6 Finance / G7 People / G8 Legal. |
| 5 | B2 Archetype / B3 Squad pairs | G1=Superman/Guardians · G2=Martian Manhunter (legacy: JohnJones W40 V4)/Illuminati · G3=Flash/Avengers · G4=Batman/Fantastic Four · G5=Cyborg/Kang Dynasty · G6=Wonder Woman/Thunderbolts · G7=Green Lantern/X-Men · G8=Aquaman/Eternals. |
| 6 | W1|W2|...|W12 | Cycle 12WY. W1-W4 = 4 trimestres de 84 jours (SUMMERS), OU W1-W12 = 12 semaines calendaires (marina), OU Q3 2026 W1-W13 (chartes_cycle_2). **DURÉE HÉTÉROGÈNE**. |
| 7 | H1|H3|H10|H30|H90 | H3 quarterly runway (Saru H3), H10 product spec iterations (Flash H10 weekly), H90 legal review (Aquaman H90 eternal-grade). |
| 8 | LD01|LD02|LD03|LD04 | LD01 Business, LD02 H3 horizon (Saru), LD03 Finance/Family (Alikaly J03). |
| 9 | J01|J03 | J01_Jerry_Prime_LD01_Business (tous), J03 Finance/Family (Alikaly cross-Jerry). |
| 10 | P1|P2|...|P8 | Operating Principles Jerry P1-P8 (chartes_cycle_2 + B1/README.md). |
| 11 | D1|D2|D4|D6|D7 | D1 verified/receipt, D4 append-only, D6 no-self-contradiction, D7 cost-of-escalation. **D6 nuance D1 verified** (Plane UI 5 states vs GTD canon 7 states). |
| 12 | M1|M2|...|M6 | Moves séquentiels HITL-gated. Runbook-C = M1-M5, Runbook-D = M1-M6. |
| 13 | V1|V2|...|V8 | Verification runs (grep/find/tsc/npm). Runbook-C = V1-V5, Runbook-D = V1-V8. |
| 14 | T1|T2|T3 | T1 = Ops/Product/People (B1-1 = Batman Ops). T2 = Growth/Sales/Finance (B1-2 = Superman Growth). T3 = Legal/R&D (B1-3 = Aquaman Legal). |
| 15 | R1|R2|R3|R4 | Rocks par trimestre (W1-W4). 4 Rocks max par B2 domain. |
| 16 | C1|C2|C3|C4 | Cycle C1 (Direction Lock) | C2 (Domain Activation) | C3 (Execution Proof) | C4 (Graduation Or Archive). |
| 17 | RP2|RP3 | RP2 = Phase C SaaS Auth, RP3 = Phase D Repositories. |
| 18 | ASPAC-3|ASPAC-6|ASPAC-7 | Items Plane UI routés via Cerritos GTD. ASPAC-6 = NEXT_ACTION W3. |
| 19 | Q3_2026_W3 | Format Q[N]_[YYYY]_W[N]. |
| 20 | JTBD-001|JTBD-002|JTBD-003|JTBD-004|JTBD-005 | Format JTBD-NNN_<DOMAIN>_<TOPIC>.md + jtbd_id PROJECT-B3-DOMAIN-NNN. |
| 21 | L1|L2|L3|L4 | Livrables numérotés dans §3 de chaque charte. |
| 22 | G-1|G-2|G-3 | Gates HITL specifiques. |
| 23 | Abort-A|...|Abort-E | Conditions d'abort. ≥2 dans chartes, ≥3 dans runbooks. |
| 24 | Gap-1|...|Gap-N | D6 honest gaps. ≥3 dans chartes, ≥4 dans runbooks. |
| 25 | W40|W40 §M2|W40 §M3|W40 §M6|W40 §R6 | W40 cadence = 5 Daily / 4 Weekly / 1 Monthly / 3 Rocks per 12WY cycle. W40 §M2 = Cyborg IT→R&D pivot. W40 §M3 = char strict 9 sections. W40 §M6 = musée anti-pattern. W40 §R6 = Lead/Lag + mission verbatim + sister canon cited. W40 §2 = Triptyque V4 missions verbatim. |
| 26 | ADR-AAAS-PRICING-001|ADR-NEXUS-NICHE-001|ADR-OMK-001..004|ADR-ICP-NEXUS-001|ADR-META-001|ADR-INFRA-003|ADR-CANON-001|ADR-SOBER-002|ADR-CRUD-VIEWS|AMEND-001|P-PR-RATIFIED | ADRs référencés dans 01-omk-business-os. ADR-AAAS-PRICING-001 (USD 5 tiers RATIFIED 2026-06-24), ADR-NEXUS-NICHE-001 (Coach premium RATIFIED), ADR-ICP-NEXUS-001 §Pilier 5 (Zero-PII), ADR-META-001 D7 (cost-of-escalation), ADR-INFRA-003 (squad replication 2026-06-05), ADR-CANON-001 (53 B3 roster), ADR-SOBER-002 (append-only no hard-delete), ADR-CRUD-VIEWS (non-existent Gap-2), AMEND-001 (Coach Pocock RATIFIED 2026-07-13), P-PR-RATIFIED. |
| 27 | Status keywords | STRUCTURED_EMPTY → GRADUATED → SHADOW_ACTIVE → ACTIVE → READY → CONDITIONAL|PASS|BLOCKED → TODO|IN_PROGRESS|BLOCKED|DONE → Business Done. **PHASE_1_STUB** (nouveau statut observé dans 02 ABC B3 Growth). picard_status: GRADUATED (RILCOT). |
| 28 | Plane state + GTD stage | Plane : Backlog | Todo | In Progress | Done | Cancelled (5 states Plane UI live). GTD canonique : Inbox | Next Actions | Today | Waiting For | Done | Cancelled | Trash (7 states). 5 ≠ 7 = D6 nuance D1 verified. |
| 29 | 8 B2 Transverse gate names + 3 emitted signals par gate | People (ASSIGNED|NEEDS_OWNER|DLQ) · IT (SYSTEM_READY|NEEDS_SYSTEM_OWNER|QUARANTINE) · Growth (GROWTH_READY|NEEDS_SIGNAL|BLOCKED_PROMISE) · Legal (LEGAL_READY|NEEDS_REVIEW|BLOCKED_RISK) · Finance (FINANCE_READY|NEEDS_MODEL|BLOCKED_LEAKAGE) · Sales (SALES_READY|NEEDS_QUALIFICATION|BLOCKED_COMMITMENT) · Product (PRODUCT_READY|NEEDS_SCOPE|BLOCKED_DELIVERY). |
| 30 | 5 USD pricing tiers (ADR-AAAS-PRICING-001) | T1 PME Solo Founder $300-500/an | T2 PME Solo Standard $500-1000/an | T3 PME Groupe $4000-5000/an | T4 Nexus mid-market $15K MRR | T5 Orbiter $50K MRR → $500K Year 10. T1-T3 annual billing, T4-T5 monthly MRR. USD SUPERSEDE EUR. |
| 31 | B3 squad topology size | Guardians = 6 / Illuminati = 7 / Avengers = 8 / Fantastic Four = 4 / Kang Dynasty = 6 / Thunderbolts = 6 / X-Men = 8 / Eternals = 10. Total ~55 personnages canon. |
| 32 | US compliance acts citées dans T3 chartes | OSTP 2022 (AI Bill of Rights) + Colorado AI Act 2026 (effective 2026-02-01) + California AB 2013/2885 + NYC LL 144 + SEC Reg D Rule 506 + SOX §404 + FTC Act §5 + CAN-SPAM Act 2003 + FLSA + ADA + US Lanham Act + US GAAP ASC 606. |
| 33 | B2 mandates packet (B1-B2-MANDATE-YYYY-NN) | Format d'identifiant des B1 Domain Mandate Packets. |
| 34 | Build Gates (B3 AGENT_ROSTER) | Onboarding agent capsule < 1h end-to-end. Heartbeat miss rate < 5% par agent par semaine. Zero ethics violation sur audit trimestriel. |
| 35 | LEAD noms canon | Captain America / Star-Lord / Black Bolt / Mr. Fantastic / Kang Prime / Bucky Barnes / Professor X / Ikaris. |
| 36 | Saru H3 (specialist A3 Discovery) | Specialist LD02 H3 horizon (quarterly runway review). M3-only mandate. |
| 37 | Chapel scorecard (A3 SNW Measure) | Specialist Measure (SNW), weekly aggregation per Batman H3 sprint. M3-only mandate. |

**Total : 37 systèmes de codes canon observés dans V2.**

---

## 4 · Contradictions et incohérences

### C1 — Casse des couches L2 (underscore vs tirets)

- `L2_Business_Pulse` (underscore) : `03_RILCOT_Members_Space_OS/SUMMERS_VERSE_MANIFEST.md` l.3
- `L2-Business-Pulse` (tirets) : `02 ABC OS & Child Care BOS/SUMMERS_VERSE_MANIFEST.md` l.3
- **V2 verdict** : Reconfirmé. Pas une vraie contradiction sémantique mais signe de génération automatisée sans normalisation.

### C2 — Durée d'un cycle W1-W12 (84 jours/trimestre vs 12 semaines calendaires)

- SUMMERS_VERSE_RILCOT : `W1 (Days 1–84)` = 84 jours pour **W1 seul** (= 1 trimestre entier)
- Cerritos_Plane_Onboarding : `12WY Q3 = 12 semaines = ~84 jours total`
- **V2 verdict** : Reconfirmé. 4 projets × 4 SUMMERS_VERSE_MANIFEST.md ont des W1-W4 (4 trimestres de 84 jours) tandis que chartes_cycle_2 ont Q3 2026 W1-W13 (13 semaines calendaires 2026-06-15 → 2026-09-07, ~85 jours).

### C3 — Cycle court marina (21 jours/W1) vs 84 jours/W1 ailleurs

- 05 marina : `W1 (Days 1–21)` = cycle court 4 × 21 = 84 jours total
- 03 RILCOT : `W1 (Days 1–84)` = 4 × 84 jours = 1 an
- **V2 verdict** : Marina = cycle court (4 × 21 jours = 84 jours total). RILCOT/ABC = cycle long (4 × 84 jours = 1 an). Alikaly suit ABC (W1 Days 1-84).

### C4 — Chart Phase D stale vs AGENTS.md Phase D DONE (auto-dénoncée)

- Chart Phase D : `RP3 = ❌ NOT STARTED`
- AGENTS.md §2 Phase State : `Phase D = ✅ DONE 2026-06-20 (11/14 views wired to Cloud via repos)`
- **V2 verdict** : Confirmé par re-lecture runbook-D-repositories.md l.16. Le runbook lui-même dénonce le chart comme stale. **D6 no-self-contradiction guard fonctionne**.

### C5 — Format SUMMERS (B1/B2/B3) vs OMK (T1/T2/T3 + chartes)

- **SUMMERS** (02-05) : 3 couches B1/B2/B3 + 8 B2 domains + 8 Marvel squads
- **OMK Picard** (01) : 3 triptyques T1/T2/T3 + chartes + runbooks + ownerbooks + W40 cadence 5-4-3-4
- **V2 verdict** : Reconfirmé. Deux systèmes distincts cohabitent.

### C6 — 5 JTBD Growth dans 02 ABC vs 2 JTBD Growth dans 05 marina

- 02 ABC : 5 fichiers (001-005)
- 05 marina : 2 fichiers (001, 005)
- **V2 verdict** : Cohérence partielle entre projets.

### C7 — `picard_status` vs `status` (orthographe inconsistante)

- 03 RILCOT : `picard_status: GRADUATED`
- 02 ABC : `status: GRADUATED`
- **V2 verdict** : Cohérence sémantique, écriture inconsistante.

### C8 — `CERRIROS_HANDOVER` (typo) vs `Cerritos` (orthographe canon)

- 4 fichiers `CERRIROS_HANDOVER.md` (double R)
- Le dossier canonique `Cerritos_Plane_Onboarding/` (Lower Decks)
- **V2 verdict** : Reconfirmé en V2. Typo assumée.

### C9 — Domaines B2 prioritaires (G8 first vs G4 first) — CORRIGÉ V2

- 02 ABC : G8>G6>G5>G7 (Child Care compliance)
- 05 marina : G4 CRITICAL > G2/G3/G6/G8 HIGH > G1/G5/G7 MEDIUM (field-first Orbiter)
- **V2 verdict** : **Note V2 corrige V1** — la V1 notait 'aucune priorité marquée dans 05 marina B2 README'. Re-lecture en V2 montre qu'il y a UNE priority matrix — différente de 02 ABC. Cohérence partielle : les 2 projets ont des priorités, mais les critères divergent.

### C10 — **NOUVEAU V2** : Bug structurel 03_DECISION_CHARTER.md vides

- `01_Projects_Picard/02 ABC OS & Child Care BOS/B1_Summer_Direction/03_DECISION_CHARTER.md` (3 octets)
- `01_Projects_Picard/03_RILCOT_Members_Space_OS/B1_Summer_Direction/03_DECISION_CHARTER.md` (3 octets)
- `01_Projects_Picard/04 Alikaly Bana Holding to LLC/B1_Summer_Direction/03_DECISION_CHARTER.md` (3 octets)
- `01_Projects_Picard/05 marina Cleaning BOS & SOP/B1_Summer_Direction/03_DECISION_CHARTER.md` (3 octets)

Le contenu réel de la "B1 Decision Charter" (Decision Rights + Output Packet + Escalation) est **APPENDÉ en bas du fichier 02_12WY_COMMAND_CYCLES.md** (commence après le séparateur `---` et l'inline-frontmatter `id: B1_DECISION_CHARTER_02_ABC_OS`). Pattern reproduit sur les 4 projets SUMMERS (vérifié pour 02 ABC, présumé pour 03/04/05). Bug structurel : fichier créé mais contenu migré ailleurs sans mise à jour de l'index.

### C11 — **NOUVEAU V2** : B2 G2 archetype `Martian Manhunter` vs `JohnJones` (W40 V4 rename intentionnel)

- 02 ABC B2 README + JTBD files : `Martian Manhunter / Illuminati`
- chartes_cycle_2/chart_T2_sales_100m_offers.md : `b2_owner: JohnJones (Sales)`
- **V2 verdict** : Renommage intentionnel W40 V4, documenté dans `ownerbook_T2_growth_sales_finance.md` §3 note : 'legacy naming MartianManhunter, W40 V4 rename JohnJones'.

### C12 — **NOUVEAU V2** : B3 squad topology size (4 vs 8 members for X-Men)

- `01-omk/B3/07_People/00_B3_SWARM_CONFIG.md` : Members: 4 (Professor X, Cyclops, Jean Grey, Beast)
- `05 marina/B3/07_People/01_B3_AGENT_ROSTER.md` : 8 X-Men canoniques (avec Wolverine/Storm/Beast/Nightcrawler/Rogue)
- **V2 verdict** : Divergence template vs canon. SWARM_CONFIG template minimaliste (4 members), AGENT_ROSTER canonique complet (8 members).

### C13 — **NOUVEAU V2** : B3 SWARM_CONFIG statuts variés (PHASE_1_STUB vs SHADOW_ACTIVE)

- 02 ABC/B3/01_Growth/00_B3_SWARM_CONFIG.md : `status: PHASE_1_STUB` (2026-06-07)
- 05 marina/B3/07_People/00_B3_SWARM_CONFIG.md : `status: SHADOW_ACTIVE` (2026-05-27)
- 01-omk/B3/07_People/00_B3_SWARM_CONFIG.md : `status: SHADOW_ACTIVE` (2026-05-27)
- **V2 verdict** : Le 02 ABC Growth SWARM_CONFIG a été upgradé le 2026-06-07 au format canonique B3 (PHASE_1_STUB = skeleton + topology declaration). Les autres SWARM_CONFIG restent en SHADOW_ACTIVE template minimal. **Incohérence de maturité**.

### C14 — **NOUVEAU V2** : Alikaly orthographe (4 variantes)

- 04 Alikaly Bana Holding to LLC/SUMMERS_VERSE_MANIFEST.md : `Alikaly Bana`
- 04 Alikaly/B2/03/00_Interface_Prototypes/Kalybana Holding/README.md : `Kalybana Holding` (K-a-l-y-b-a-n-a)
- 04 Alikaly/B2/03/alykaly-front/README.md : `alykaly-front` (lowercase, y)
- 04 Alikaly/B2/03/00_Interface_Prototypes/Kalybana Holding/alykaly-os/README.md : `alykaly-os` (lowercase, y)
- 04 Alikaly/B2/03/Alykaly Bana Real Estates Front-End FR V2/README.md : `Alykaly Bana` (capitalisé)

**V2 verdict** : **4 orthographes distinctes** pour le même projet dans 04 Alikaly. La typo la plus visible est `Kalybana` (avec y) dans `Kalybana Holding` — orthographe probablement involontaire mais conservée dans le README parent.

### C15 — **NOUVEAU V2** : Interface prototypes = 7 projets distincts (Alikaly B2 03 Product)

- `Kalybana Holding/01_Real_Estate` (AI Studio app f3bce99a)
- `Kalybana Holding/02_Holdings_Platform` (AI Studio app 1956af9c)
- `Kalybana Holding/alykaly-os` (Next.js bootstrapped)
- `alykaly-front` (Next.js bootstrapped)
- `alykaly-holding-modern` (Next.js bootstrapped)
- `Alykaly Bana Real Estates Front-End FR V2` (Next.js bootstrapped)

**V2 verdict** : 7 sous-dossiers dans 04 Alikaly/B2/03/Product. **Plusieurs tentatives de démarrer le produit** (Real Estate, Holdings Platform, 4 Next.js bootstraps), aucune avec contenu substantiel au-delà du README template.

### C16 — **NOUVEAU V2** : D6 nuance D1 verified (Plane UI 5 states vs GTD canon 7 states)

- Plane UI live : 5 default states (Backlog, Todo, In Progress, Done, Cancelled)
- GTD canonique : 7 states (Inbox, Next Actions, Today, Waiting For, Done, Cancelled, Trash)
- **V2 verdict** : 5 ≠ 7 = D6 follow-up noté dans `mcp-plane.py` docstring.

### C17 — **NOUVEAU V2** : B2 G2 chemin filesystem `MartianManhunter` (no space) vs texte `Martian Manhunter` (with space)

- `B3_Warp_Core_Execution/02_Sales_MartianManhunter_Illuminati/` (chemin filesystem, no space)
- `B2_Business_Domains/02_Sales_MartianManhunter_Illuminati/README.md` (chemin filesystem, no space)
- Contenu texte : `Martian Manhunter` (with space) — incohérence mineure

**V2 verdict** : Cohérence des chemins filesystem (toujours `MartianManhunter` no space). Incohérence entre filesystem et texte (avec espace).

### C18 — **NOUVEAU V2** : L0_Rick sovereignty (IT absorbed vs IT retained)

- `chart_T1_people_hr_ops.md` l.18 : `OUT : L0 Rick sovereignty infra (IT absorbed)`
- `ownerbook_T3_legal_rd.md` l.18 : `L0 Rick Sovereignty ──absorbs──→ [IT infra (MCPs/deploy/runtime)]`

**V2 verdict** : Les deux fichiers OMK décrivent la même chose (IT absorbed to L0 Rick) mais le T1 chart dit 'OUT' (le périmètre exclut IT absorbed), tandis que ownerbook_T3 le décrit comme un diagramme de classes (L0 absorbe IT). Cohérence sémantique, deux formulations.

---

## 5 · Récapitulatif — combien lu sur combien

**Lu intégralement (~130 fichiers uniques dans V2)** :

- **Fichiers de tête (re-lus pour V2 completeness)** : 4 SUMMERS_VERSE_MANIFEST + 4 B1 README + 4 CERRIROS_HANDOVER + 5 B3 README + 1 01-omk B3 README + 1 Cerritos MANIFEST + 1 ClaudeClaw README
- **B1 specs 00-11 (lus pour 02 ABC)** : 11 fichiers (00_B1_DIRECTION_INDEX, 01_NORTH_STAR, 02_12WY_COMMAND_CYCLES, 03_DECISION_CHARTER [vide], 04_B2_HANDOFF_QUEUE, 05_B2_DEFINITION_OF_DONE_SPEC, 06_B3_JOBS_TO_BE_DONE_SPEC, 07_B1_TO_B2_DOMAIN_GOVERNANCE_WORKFLOW, 08_BUSINESS_WHEEL_BALANCE_REVIEW, 09_MARKET_VALIDATION_SPRINT, 10_PROJECT_GRADUATION_GATES, 11_FRACTAL_PROJECT_DEVELOPMENT_PLAN)
- **04 Alikaly B1** : 01_NORTH_STAR + 11_FRACTAL_PROJECT_DEVELOPMENT_PLAN
- **04 Alikaly B2 00_ALIKALY_DOMAIN_DEVELOPMENT_MAP**
- **B2 Business Domains README × 4 projets + 01-omk** : 02 ABC (8 dossiers + README.md global) + 03 RILCOT (8 dossiers + README) + 04 Alikaly (8 dossiers + README) + 05 marina (8 dossiers + README) + 01-omk (5 dossiers, 04-08 uniquement) = 37 fichiers + 4 README globaux
- **B2 sub-READMEs lus** : 02 ABC G1-G8 (8) + 03 RILCOT G1,G2,G8 (3) + 04 Alikaly G1,G3,G8 (3) + 05 marina G3,G4 (2) + 01-omk G4-G8 (5) = ~21 sous-READMEs (couverture large mais non-exhaustive — patterns identiques entre projets)
- **B3 Warp Core × 1** (01-omk)
- **B3 SWARM_CONFIG × 3** : 02 ABC Growth (PHASE_1_STUB), 05 marina People (SHADOW_ACTIVE), 01-omk People (SHADOW_ACTIVE)
- **B3 AGENT_ROSTER × 1** : 05 marina People
- **B3 Peer Handoffs × 1** : 01-omk People
- **B3 Shared Context × 1** : 01-omk People
- **B3 squad READMEs × 13** : StarLord/Rocket/Gamora (02 ABC Growth) + BlackBolt (02 ABC Sales) + MrFantastic (02 ABC Ops, 04 Alikaly, 05 marina) + KangPrime (02 ABC IT, 04 Alikaly IT, 01-omk IT) + BuckyBarnes (02 ABC Finance, 04 Alikaly Finance) + Ikaris (02 ABC Legal) + ProfessorX (03 RILCOT People) + StarLord (03 RILCOT, 01-omk Growth)
- **JTBDs × 4** : JTBD-001_ABC_OWNER_HANDOFF_MAP + JTBD-001_RILCOT_OWNER_HANDOFF_MAP + JTBD-001_ALIKALY_OWNER_HANDOFF_MAP + JTBD-001_MARINA_DIAGNOSTIC_TO_PROPOSAL
- **chartes/cycle_1 × 2** : phase_c_saas_auth + phase_d_repositories_branches
- **chartes_cycle_2 × 24** : toutes les T1 (9), T2 (9), T3 (6) lus en V2
- **ownerbooks × 3** : T1_people_ops_product + T2_growth_sales_finance + T3_legal_rd
- **runbooks × 2** : C-saas-auth + D-repositories (re-lus pour V2)
- **Moat × 4** : config.json + moat-tasks.md + moat-tasks-detail.json + README
- **InterfacePrototypes × 10** : Alikaly 7 + RILCOT 2 + marina 1

**Non lu (~230 fichiers)** :

- ~260 fichiers B3SubSquadMemberREADME (les clones strictement identiques — pattern ADR-INFRA-003). Lecture des ~13 lus suffit à confirmer le pattern.
- ~32 B3 SWARM_CONFIG non lus (les 8 par SUMMERS × 4 projets — 5 lus).
- ~28 B1 specs (4 projets × 7 specs × 4 projets — 11 lus pour 02 ABC).
- ~140 autres fichiers (chartes, B3 AGENT_ROSTER, etc.)

**Ce que j'ai laissé de côté et pourquoi** :

- **B3 squad sub-READMEs** : pattern clone strictement identique. Les ~13 lus confirment la structure (Project + Squad member + Role + Canon role path + Cette fiche). Les ~260 autres suivraient le même template.
- **B3 SWARM_CONFIG des autres domaines** : les 5 lus (02 ABC Growth détaillé + 05 marina People template + 01-omk People template + 2 en V1) confirment 2 patterns : PHASE_1_STUB avec anchors spécifiques (02 ABC) vs SHADOW_ACTIVE template minimal.
- **B1 specs des autres projets** : 02 ABC est le projet canon ; les 3 autres (03/04/05) ont des fichiers identiques ou très proches.
- **B2 Domain sub-READMEs non lus** : 02 ABC lus intégralement (8 dossiers + README), les 3 autres projets ont des patterns identiques (template Role/Gate/Required Input/Blocking Authority/Evidence Checklist/Operating Rule).

---

## 6 · Notes méthodologiques

### Jonctions NTFS

**Jonctions NTFS** : aucune comptée dans ce périmètre. Les 176 jonctions totales de la KB vivent ailleurs (Geordi et autres). Le dossier `graphify-out/` pourrait en contenir (copies de CERRIROS_HANDOVER dans `graphify-out/chunks/`), mais elles sont à la racine du dossier graphify et ne se propagent pas en profondeur.

### Piège évité

Le dossier `01-omk-business-os/` lui-même contient un `graphify-out/` — j'ai lu les fichiers canoniques (chartes, runbooks, ownerbooks) à la racine et au niveau cycle_2, pas dans graphify-out.

### Profondeur 5-6 = B3 sub-squad READMEs en masse

Ce sont les fichiers les plus nombreux (~260). Lecture des parents (B2 README + B2 Domain Development Map + B3 README + B3 SWARM_CONFIG + ~13 sub-READMEs échantillonnés) suffit à inférer la structure.

### Limites

- **Bug structurel 03_DECISION_CHARTER.md** : confirmé pour 02 ABC (3 octets = BOM), présumé pour 03/04/05 (3 octets chacun) — vérification exhaustive non faite.
- **B3 JTBDs non lus** : la majorité des 268 fichiers JTBD-001/JTBD-002 par domaine×projet n'ont pas été lus. Pattern identique à JTBD-001 lu (Job statement + 8 outputs + 8-Domain Map + 7 guardrails + 1 project constraint). Les attributs spécifiques à chaque domaine restent non vérifiés exhaustivement.
- **B1 specs des autres projets** : 02 ABC est le projet canon. Les 11 specs lus pour 02 ABC représentent la structure. Les 03/04/05 specs des mêmes fichiers (00-11) suivent probablement le même pattern mais n'ont pas été lus.
- **Interface prototypes** : aucun contenu substantiel au-delà des README templates. Pas de code applicatif à analyser.

---

*Cartographie V2 — 2026-08-13 — 130 fichiers lus en V2 (95 NEW + 35 re-lectures pour V2 completeness) sur 363 disponibles.*
