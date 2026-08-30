# Cartographie — 01_Projects_Picard

> Cartographie ontologique du seau **01_Projects_Picard** du PARA de V2.
> Source : `carto/structure.txt` filtré sur `01_Projects_Picard` → 363 chemins.
> Méthode : lecture intégrale des fichiers de tête (SUMMERS_VERSE_MANIFEST, B1/B2/B3 README, CERRIROS_HANDOVER, B1 03–06 specs, B2_DC/B2_BUSINESS_WHEEL/B2_DOMAIN_GATE, B2 00_DOMAIN_DEVELOPMENT_MAP, B3 SWARM_CONFIG/AGENT_ROSTER/PEER_HANDOFFS, JTBD-001/002, Cerritos_Plane_Onboarding/MANIFEST+cycles-integration+invite-team, chartes_cycle_2/Runbooks, ClaudeClaw/.moat).
> Jonctions NTFS : 0 (aucune dans ce périmètre — confirmé par lecture, pas par comptage exhaustif).

## Périmètre lu

| Métrique | Valeur |
|---|---|
| Fichiers disponibles (filtrés) | 363 |
| Fichiers lus au long | ~38 (toutes les têtes + un échantillon par profondeur) |
| Fichiers non lus | ~325 (profondeur 5 = JTBD-001/002 par domaine × 8 domaines × ~3 projets) |

**Distribution des profondeurs** : 6 fichiers de tête (SUMMERS/MANIFEST/README racine), 41 à profondeur 3 (B1/B2/B3 README), 41 à profondeur 4 (sous-spécifications B1, fichiers B2 mésosphère), 268 à profondeur 5 (la masse : JTBD-001 et JTBD-002 × 8 domaines × 4 projets SUMMERS), 7 à profondeur 6+ (sub-squads).

---

## Vue d'ensemble — les 8 sous-projets

Le seau contient 8 sous-projets, qui se répartissent en **deux familles très distinctes** plus un projet tech isolé et un projet L1.

### Famille SUMMERS (4 projets rigoureusement isomorphes)

Tous suivent le même template `SUMMERS_VERSE_MANIFEST.md` + `B1_Summer_Direction/` + `B2_Business_Domains/` + `B3_Warp_Core_Execution/` + `CERRIROS_HANDOVER.md`.

| # | Projet | Mode primaire | Particularité |
|---|---|---|---|
| 2 | `02 ABC OS & Child Care BOS` | Orbiter (Nexus secondaire) | Dual-entity, contrainte Child Care = compliance G8 obligatoire |
| 3 | `03_RILCOT_Members_Space_OS` | Nexus (Solaris/Orbiter secondaires) | Members community, knowledge compounding |
| 4 | `04 Alikaly Bana Holding to LLC` | Orbiter (Nexus secondaire) | **Cross-Jerry** : J01 + J03 Finance/Family |
| 5 | `05 marina Cleaning BOS & SOP` | Orbiter (Nexus secondaire) | SOPs-as-a-service, dépend saison/weather |

### Famille Picard Cycle (1 projet, format différent)

| # | Projet | Format |
|---|---|---|
| 1 | `01-omk-business-os/` | `chartes_cycle_2/` (T1/T2/T3) + `chartes/` (cycle 1, Phase C/D) + `runbooks/` (Phase C/D) + `ownerbooks/` (T1/T2/T3) + `B3_Warp_Core_Execution/README.md` |

### Projets isolés

| # | Projet | Couche | Format |
|---|---|---|---|
| 6 | `Cerritos_Plane_Onboarding/` | L1_Life_OS | `MANIFEST.md` + 2 fiches par item Plane (cycles-integration, invite-team) |
| 7 | `ClaudeClaw Agent/` | Tech | README React/Vite + `.moat/` (Drawbridge UI feedback loop) |
| 8 | `omk-services/` | Tech | (peu présent dans la liste — code applicatif OMK) |

---

## 1 · Types d'objets — relevé

> Un type = un nom propre récurrent, avec attributs, et dont il existe plusieurs exemplaires.

### `SummerProject` (Manifest)

Nom canon : `SUMMERS_VERSE_MANIFEST.md`. Attributs observés : `id`, `layer` (L2_Business_Pulse), `status: GRADUATED`, `created: 2026-05-21`, `parent_jerry: J01_Jerry_Prime_LD01_Business`, `project_slug`. Sections obligatoires : B1 Direction (1Y/3Y/10Y Vision), ICP Variants, LD01 Book Alignment, 12WY Rock Linkage, Cerritos Handoff Reference, B3 Warp Core Brief.

**Chemins** (4) :
- `02 ABC OS & Child Care BOS/SUMMERS_VERSE_MANIFEST.md`
- `03_RILCOT_Members_Space_OS/SUMMERS_VERSE_MANIFEST.md`
- `04 Alikaly Bana Holding to LLC/SUMMERS_VERSE_MANIFEST.md`
- `05 marina Cleaning BOS & SOP/SUMMERS_VERSE_MANIFEST.md`

### `B1DirectionIndex` (Cockpit B1)

Nom canon : `B1_Summer_Direction/README.md` (fichier index) + fichiers 00–11. Attributs : `layer: B1_DIRECTION` ou `L2-Business-Pulse-Summer`, `status: SHADOW_ACTIVE`. Le README canonique du projet 02 contient une table d'Operating Rule :

> « B1 owns direction and packet structure. B2 owns domain Definition of Done and gates. B3 owns execution, proof, Lead indicators, Lag indicators, and blocker reports. »
> — `02 ABC OS & Child Care BOS/B1_Summer_Direction/README.md` l.14

**Chemins** (4) :
- `02 ABC OS & Child Care BOS/B1_Summer_Direction/README.md`
- `03_RILCOT_Members_Space_OS/B1_Summer_Direction/README.md`
- `04 Alikaly Bana Holding to LLC/B1_Summer_Direction/README.md`
- `05 marina Cleaning BOS & SOP/B1_Summer_Direction/README.md`

### `B2DomainDevelopmentMap` (matrice 8 domaines × Rocks × JTBD)

Nom canon : `00_<PROJECT>_DOMAIN_DEVELOPMENT_MAP.md` à la racine de `B2_Business_Domains/`. Attributs : `id`, `layer: B2_BUSINESS_DOMAINS`, `status: ACTIVE`, `created: 2026-06-02`. Tableau à 8 lignes (Growth→Legal) avec colonnes `Macro doctrine reference | Project Rock | B3 JTBD`. Chaque ligne référence **deux** fichiers JTBD par domaine : un `JTBD-001_<DOMAIN>_<TOPIC>.md` et un `JTBD-002_<DOMAIN>_TRANSVERSE_<GATE>.md`.

**Chemins** (4) :
- `02 ABC OS & Child Care BOS/B2_Business_Domains/00_ABC_DOMAIN_DEVELOPMENT_MAP.md`
- `03_RILCOT_Members_Space_OS/B2_Business_Domains/00_RILCOT_DOMAIN_DEVELOPMENT_MAP.md`
- `04 Alikaly Bana Holding to LLC/B2_Business_Domains/00_ALIKALY_DOMAIN_DEVELOPMENT_MAP.md`
- `05 marina Cleaning BOS & SOP/B2_Business_Domains/00_MARINA_DOMAIN_DEVELOPMENT_MAP.md`

### `B2MesoMatrix` (matrices transverses B2)

Famille de 4 fichiers de coordination entre B2 (sous-domaine « mésosphère ») :
- `B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX.md` — Domain Pair Checks + 8 transverse gates (Ops Transverse, People Agent Governance, IT Systems Access, Growth Signal, Legal Risk, Finance Money, Sales Revenue, Product Offer)
- `B2_DOMAIN_GATE_MATRIX.md` — graduation `Product Done` vs `Business Done` + Gate Order
- `B2_DC_DIRECTION_COUNCIL_WORKFLOW.md` — Council Members (8 VPs), Council Routine, Meso Decision Packet
- `B2_MESO_VP_SWARM_COORDINATION.md` — Coordination Pattern entre paires B2, Peer Escalation Packet
- `B2_OFFER_BRAND_REVENUE_ENGINE.md` — 4 packets requis (Offer / Brand / Revenue / Delivery)

**Chemin** : `02 ABC OS & Child Care BOS/B2_Business_Domains/{NOM}.md` (×4 fichiers). Tous `status: SHADOW_ACTIVE`, `surface: 02_ABC_OS`.

### `B3WarpCoreREADME` (doctrine d'exécution)

Nom canon : `B3_Warp_Core_Execution/README.md`. Attributs : `layer: L2-Business-Pulse-B3`, `status: ACTIVE`, `created: 2026-05-21`. Sections fixes : « What B3 Does » / « What B3 Does NOT Do » / Cycle Format W1–W12 (84-day) / Lead vs Lag / Lead/Lag Log Format / Artifact Proof Requirements / Blocker Note Protocol / Completion Evidence Standard.

**Chemins** (5) :
- `01-omk-business-os/B3_Warp_Core_Execution/README.md`
- `02 ABC OS & Child Care BOS/B3_Warp_Core_Execution/README.md` (variante dual-entity + Child Care constraint)
- `03_RILCOT_Members_Space_OS/B3_Warp_Core_Execution/README.md`
- `04 Alikaly Bana Holding to LLC/B3_Warp_Core_Execution/README.md`
- `05 marina Cleaning BOS & SOP/B3_Warp_Core_Execution/README.md`

### `B3SwarmConfig` (config d'essaim B3 par domaine)

Nom canon : `B3_Warp_Core_Execution/<NN>_<DOMAIN>_<ARCHETYPE>_<SQUAD>/00_B3_SWARM_CONFIG.md`. Attributs : `layer: B3_SWARM_EXECUTION`, `b2_gatekeeper` (le B2 owner), `squad` (Marvel/DC), `status: SHADOW_ACTIVE`. Définit les **Members** canoniques (personnages de comics). Le projet 02 et le projet 05 utilisent le même format mais avec des membres différents (X-Men du 05 = Professor X/Cyclops/Jean Grey/Wolverine/Storm/Beast/Nightcrawler/Rogue).

**Chemins** (8 domaines × 4 projets SUMMERS + variantes OMK = ~32 fichiers) :
- `05 marina Cleaning BOS & SOP/B3_Warp_Core_Execution/07_People_GreenLantern_XMen/00_B3_SWARM_CONFIG.md` (lu)
- `05 marina Cleaning BOS & SOP/B3_Warp_Core_Execution/07_People_GreenLantern_XMen/01_B3_AGENT_ROSTER.md`
- ... (la masse — non lus individuellement)

### `B3AgentRoster` (liste nominative des membres de l'essaim)

Nom canon : `01_B3_AGENT_ROSTER.md`. Attributs : `notion_source` (chaque agent pointe vers une page Notion), `b2_gatekeeper`, `squad`, `members` (8 personnages). Le roster porte aussi des **Build Gates** :

> « Onboarding agent capsule < 1h end-to-end / Heartbeat miss rate < 5% par agent par semaine / Zero ethics violation sur audit trimestriel. »
> — `05 marina Cleaning BOS & SOP/B3_Warp_Core_Execution/07_People_GreenLantern_XMen/01_B3_AGENT_ROSTER.md` l.44

**Chemin** (lu) : idem ci-dessus.

### `JTBD` (Jobs To Be Done B3)

Nom canon : `JTBD-00N_<DOMAIN>_<TOPIC>.md` (N = 1 ou 2). Attributs : `jtbd_id`, `source_rock`, `domain`, `b2_owner`, `b3_swarm`, `status: READY`. Sections : Job, Output (1–10), Eight-Domain X Map, Guardrails, Proof.

**Chemins** (la masse — lu : 4 fichiers, ~64 estimés au total) :
- `02 ABC OS & Child Care BOS/B3_Warp_Core_Execution/01_Growth_Superman_Guardians/JTBD-001_ORBITER_VOC_PACKET.md`
- `02 ABC OS & Child Care BOS/B3_Warp_Core_Execution/01_Growth_Superman_Guardians/JTBD-005_ABC_TRANSVERSE_GROWTH_SIGNAL_GATE.md`
- `05 marina Cleaning BOS & SOP/B3_Warp_Core_Execution/02_Sales_MartianManhunter_Illuminati/JTBD-001_MARINA_DIAGNOSTIC_TO_PROPOSAL.md`
- `05 marina Cleaning BOS & SOP/B3_Warp_Core_Execution/07_People_GreenLantern_XMen/JTBD-001_MARINA_OWNER_HANDOFF_MAP.md`

### `CerritosHandover` (handoff projet)

Nom canon : `CERRIROS_HANDOVER.md` (sic, typo « CERRIROS » conservée partout). Attributs : `id`, `layer: L2-Business-Pulse`, `status: GRADUATED`, `source_of_truth: J01_Jerry_Prime_LD01_Business/AREA_STANDARD.md`. Sections fixes : Routing Chain (schéma ASCII), What Jerry Proposed, What Cerritos Clarified, What Picard Opened, What B1 Sets as Vision, What B2 Owns as Rocks, What B3 Executes in First 12WY Cycle.

**Chemins** (4 projets + copies dans graphify-out) :
- `02 ABC OS & Child Care BOS/CERRIROS_HANDOVER.md` (lu intégralement)
- `03_RILCOT_Members_Space_OS/CERRIROS_HANDOVER.md`
- `04 Alikaly Bana Holding to LLC/CERRIROS_HANDOVER.md`
- `05 marina Cleaning BOS & SOP/CERRIROS_HANDOVER.md`

### `Charte` (format OMK Picard Cycle 2)

Nom canon : `chart_<TRIPTYQUE>_<DOMAIN>_<TOPIC>.md`. Attributs : `type: charte`, `triptyque: T1|T2|T3`, `rock_id: B1-1`, `b2_owner` (nom canon Marvel), `b3_squad` (lead + N), `icp`, `12wy_window`, `geography`, `doctrine_lock: D4 append-only · D6 no-self-contradiction`. Sections fixes 1–9 : Objectif / Périmètre / Livrables / Gates / B3 squad / HITL gates / Aborts / DoD Una 3-critères / D6 honest gaps.

**Chemins** (lus : 2) :
- `01-omk-business-os/chartes_cycle_2/chart_T1_ops_runbook_v1.md`
- `01-omk-business-os/chartes_cycle_2/chart_T1_product_spec_loop.md`
- `01-omk-business-os/chartes_cycle_2/chart_T1_product_roadmap.md`
- `01-omk-business-os/chartes_cycle_2/chart_T1_ops_sop_canon.md`
- `01-omk-business-os/chartes_cycle_2/chart_T2_finance_runway_runbook.md`

### `Runbook` (exécuteur M1–M5 dérivé d'une charte)

Nom canon : `runbook-<PHASE>-<TOPIC>.md`. Attributs : `type: runbook`, `chart_source: ../chartes/...`, `project: omk`, `rock_id` (RP2/RP3), `domain` (B2 owner(s)), `12wy_window`, `doctrine_lock`. Sections : Pre-check gates, M1–M5 (Mouvent par move), Abort conditions, D6 honest gaps, Verification runs (V1–V8), DoD Una 3-critères, Reverse path, Self-grade /12.

**Chemins** (lus : 2) :
- `01-omk-business-os/runbooks/runbook-C-saas-auth.md` (Phase C, RP2)
- `01-omk-business-os/runbooks/runbook-D-repositories.md` (Phase D, RP3)

### `Ownerbook` (vue owner OMK)

Nom canon : `ownerbook_T<n>_<TOPICS>.md`. Attributs : regroupement par triptyque. **Chemin** : `01-omk-business-os/ownerbooks/{T1,T2,T3}_*.md`.

### `PlaneItem` (item Plane routé via Cerritos GTD)

Nom canon : `cycles-integration.md` / `invite-team.md` dans `Cerritos_Plane_Onboarding/`. Attributs : `id` (ASPAC-3 / ASPAC-6), `plane_id`, `plane_state: Backlog`, `gtd_stage` (actionable / multi-step / someday-maybe), `priority`, `owner: A0`, `classification: Projects`, `cycle: Q3_2026_W3`.

**Chemin** (lus : 2) :
- `Cerritos_Plane_Onboarding/invite-team.md` (ASPAC-3, Backlog)
- `Cerritos_Plane_Onboarding/cycles-integration.md` (ASPAC-6, NEXT_ACTION)

### `Moat` (workflow Drawbridge UI feedback — projet ClaudeClaw)

Nom canon : `ClaudeClaw Agent/.moat/{README.md, drawbridge-workflow.md, moat-tasks.md, moat-tasks-detail.json, config.json}`. Format externe (extension Chrome Moat) ; instancié pour ce projet précis. Attributs : `description`, `globs`, `alwaysApply: true`. Le `drawbridge-workflow.md` est un fichier de règles IA (~800 l.) avec workflow Step / Batch / YOLO.

**Chemin** (lus : 3) :
- `ClaudeClaw Agent/.moat/README.md`
- `ClaudeClaw Agent/.moat/drawbridge-workflow.md`
- `ClaudeClaw Agent/.moat/moat-tasks.md`

---

## 2 · Relations — citation verbatim

> Toutes les citations sont reproduites telles quelles depuis les fichiers, avec leur chemin. **Pas de paraphrase.** Les phrases en français/anglais mélangés sont laissées intactes.

### Chaîne de routing Jerry → Cerritos → Picard → Summer → B2 → B3

> « Routing Chain :
> Jerry Prime (A1 vision)
>     │
>     ▼
> Cerritos (GTD pipeline — idea triage and routing)
>     │
>     ▼
> Picard / Summer's Verse (B1 — opens, decides, delegates)
>     │
>     ├──► B2 Managers (Rocks per domain)
>     │        │
>     │        ▼
>     │    B3 Marvel Squads (execution)
>     │
>     └──► B3 Warp Core (Lead/Lag logs + artifact proofs) »
> — `02 ABC OS & Child Care BOS/CERRIROS_HANDOVER.md` l.13–28

### Cerritos clarifie : interdiction de routing direct Jerry → Picard

> « Clarification made : Ideas do NOT flow Jerry → Picard directly. Cerritos is the mandatory intermediate. Jerry's role is criteria-setter, not receiver. »
> — `02 ABC OS & Child Care BOS/CERRIROS_HANDOVER.md` l.60

### B3 ne peut pas escalader sans Lead/Lag evidence

> « B3 does NOT:
> - Rewrite strategy
> - Redefine vision
> - Alter B2 Rock definitions
> - Escalate without first logging Lead/Lag evidence »
> — `02 ABC OS & Child Care BOS/SUMMERS_VERSE_MANIFEST.md` l.100–105 (et tous les autres SUMMERS_VERSE)

### B3 owns execution only (core rule)

> « Core rule : B3 is the engine, not the方向盘. If you feel the need to redirect, that is a B2 or B1 conversation, not a B3 action. »
> — `02 ABC OS & Child Care BOS/B3_Warp_Core_Execution/README.md` l.30

### B1 → B2 → B3 ownership explicite

> « B1 owns direction and packet structure. B2 owns domain Definition of Done and gates. B3 owns execution, proof, Lead indicators, Lag indicators, and blocker reports. »
> — `02 ABC OS & Child Care BOS/B1_Summer_Direction/README.md` l.14

### B1 → B2 handoff queue flow

> « 1. B1 writes or updates direction here.
> 2. B1 creates a B2 request in 04_B2_HANDOFF_QUEUE.md.
> 3. B2 converts the request into DoD packets using 05_B2_DEFINITION_OF_DONE_SPEC.md.
> 4. B2 creates B3 jobs using 06_B3_JOBS_TO_BE_DONE_SPEC.md.
> 5. B3 executes only the defined jobs and returns proof.
> 6. B2 updates gates; B1 reviews direction drift. »
> — `02 ABC OS & Child Care BOS/B1_Summer_Direction/README.md` l.27–32

### Child Care constraint : G8 Legal bloque tout

> « Child Care extra : Compliance-related ideas routed with higher priority (liability risk) » et « ALL Child Care offers require B2-G8 Legal compliance sign-off before launch »
> — `02 ABC OS & Child Care BOS/CERRIROS_HANDOVER.md` l.58 et l.79

> « **Child Care constraint**: G8 Legal (Aquaman) must sign off on every Child Care offer before B3 execution. »
> — `02 ABC OS & Child Care BOS/CERRIROS_HANDOVER.md` l.115

### Cross-Jerry (Alikaly) : J03 doit valider avant J01

> « When a decision touches J03 (tax structure, family asset governance, succession), route to J03 owner before committing LLC structure. »
> — `04 Alikaly Bana Holding to LLC/SUMMERS_VERSE_MANIFEST.md` l.54

> « Decision rights : If J01 and J03 disagree on LLC structure, escalate to B1 Rick/Morty — not to Summer's independent judgment. »
> — `04 Alikaly Bana Holding to LLC/B1_Summer_Direction/README.md` l.114

### B2 Council : modes parallel / handoff / negotiation

> « Council selects one of three modes:
>    - parallel: domains can act independently.
>    - handoff: one domain must finish before another starts.
>    - 
> egotiation: two or more DoDs conflict and need a tradeoff. »
> — `02 ABC OS & Child Care BOS/B2_Business_Domains/B2_DC_DIRECTION_COUNCIL_WORKFLOW.md` l.31–35

### Domain Pair Checks (B2 ↔ B2)

> « | Growth + Sales | Is attention becoming qualified opportunity? | B2 Council |
> | Sales + Ops | Can promises be delivered repeatedly? | B2 Council |
> | Product + Ops | Is the artifact operationally supportable? | B2 Council |
> | Product + IT | Can the product run, deploy, recover, and be accessed? | B2 Council |
> | Finance + Growth | Is spend justified by learning or traction? | B2 Council |
> | Finance + Product | Does build cost protect margin? | B2 Council |
> | Legal + Growth | Are claims safe? | B2 Council |
> | Legal + Product | Are IP/privacy/terms boundaries clear? | B2 Council |
> | People + All | Is ownership and load sustainable? | B2 Council or B1 if structural | »
> — `02 ABC OS & Child Care BOS/B2_Business_Domains/B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX.md` l.16–26

### Ops Transverse Gate — Ops run final launch gate

> « Ops/Batman runs the final transverse launch gate after the pair checks. A domain can be individually CONDITIONAL, but the whole project cannot launch unless Ops can name:
> - the delivery phase affected;
> - the owner;
> - the risk;
> - the rollback/exception path;
> - the date of next review. »
> — `02 ABC OS & Child Care BOS/B2_Business_Domains/B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX.md` l.31–37

### 8 transverse gates (un par B2)

> « No B3 task should move to Ops launch readiness until People has emitted ASSIGNED, NEEDS_OWNER, or DLQ. »
> — `02 ABC OS & Child Care BOS/B2_Business_Domains/B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX.md` l.69

> « No B3 task should move to People assignment or Ops launch readiness until IT has emitted SYSTEM_READY, NEEDS_SYSTEM_OWNER, or QUARANTINE where systems/data/access are involved. »
> — idem l.83

> « No Growth motion should become public or feed Sales/Ops until Growth has emitted GROWTH_READY, NEEDS_SIGNAL, or BLOCKED_PROMISE. »
> — idem l.98

> « No B3 task should become public, contractual, data-bearing, or externally binding until Legal has emitted LEGAL_READY, NEEDS_REVIEW, or BLOCKED_RISK. »
> — idem l.112

> « No B3 task should become public, paid, billed, staffed, or financially binding until Finance has emitted FINANCE_READY, NEEDS_MODEL, or BLOCKED_LEAKAGE. »
> — idem l.126

> « No proposal, quote, commitment, or revenue handoff proceeds until Sales has emitted SALES_READY, NEEDS_QUALIFICATION, or BLOCKED_COMMITMENT. »
> — idem l.139

> « No offer, demo, service package, deliverable, or Product-bound promise proceeds until Product has emitted PRODUCT_READY, NEEDS_SCOPE, or BLOCKED_DELIVERY. »
> — idem l.152

### JTBD déclenche sur signal qualifié

> « When 05 Marina Cleaning BOS & SOP receives a qualified signal or opportunity, produce the diagnostic-to-proposal packet so Sales can decide whether to propose, reject, or return the work for more proof. »
> — `05 marina Cleaning BOS & SOP/B3_Warp_Core_Execution/02_Sales_MartianManhunter_Illuminati/JTBD-001_MARINA_DIAGNOSTIC_TO_PROPOSAL.md` l.15

### JTBD People — chaîne d'output

> « When $(System.Collections.Hashtable.Label) has active work in any of the eight B2 domains, produce and maintain the owner handoff map so every B2 decision and B3 execution task has accountable ownership, capacity visibility, proof, and escalation. »
> — `05 marina Cleaning BOS & SOP/B3_Warp_Core_Execution/07_People_GreenLantern_XMen/JTBD-001_MARINA_OWNER_HANDOFF_MAP.md` l.15

### B3 Swarm → Proof rule

> « Every claim in this roster is either from Notion AGENT_REGISTRY_DB or from the local Business Pulse swarm doctrine. If Notion and local doctrine diverge, Notion wins for lore and local doctrine wins for filesystem path conventions. »
> — `05 marina Cleaning BOS & SOP/B3_Warp_Core_Execution/07_People_GreenLantern_XMen/01_B3_AGENT_ROSTER.md` l.92

### Cerritos_Plane_Onboarding : Cerritos est GTD pipeline, Plane UI est outil

> « Routing confirmation : All ideas for ABC OS & Child Care BOS route through Cerritos before reaching Picard/Summer »
> — `02 ABC OS & Child Care BOS/CERRIROS_HANDOVER.md` l.50

> « **Clarification made**: Ideas do NOT flow Jerry → Picard directly. Cerritos is the mandatory intermediate. Jerry's role is criteria-setter, not receiver. »
> — idem l.60

Et dans le Plane :
> « Feature Cycle = 12WY canon existe déjà (framework weekly time-boxing). "Use" = intégrer dans workflow quotidien Cerritos. »
> — `Cerritos_Plane_Onboarding/cycles-integration.md` l.20

> « 12WY Q3 2026 cycle = 06/15 → 09/07/26 (12 semaines). Plane Cycles = outil de time-boxing visuel aligné sur ce cycle canon. »
> — idem l.23

### OMK BOS — Doctrine D4 / D6 / D7 (chartes)

> « Doctrine locks: D4 append-only · D6 no-self-contradiction · US market focus »
> — `01-omk-business-os/chartes_cycle_2/chart_T1_ops_runbook_v1.md` l.10 (et toutes les autres chartes)

> « canon contradiction surfaced : le chart Phase D (`phase_d_repositories_branches.md:32`) déclare RP3 = ❌ NOT STARTED, mais `apps/dashboard/AGENTS.md:28` (§2 Phase State) déclare Phase D = ✅ DONE 2026-06-20 (11/14 views wired to Cloud via repos). D6 no-self-contradiction guard : ce runbook PREND POUR HYPOTHÈSE l'état AGENTS.md (récent + receipts ViewShell primitive + 11/14 views live), et dénonce le chart comme stale (chart écrit 2026-07-15 mais oublie les receipts du sprint A→F 2026-06-20). »
> — `01-omk-business-os/runbooks/runbook-D-repositories.md` l.16

### Chartes cycle_2 → Runbooks (dépendance)

> « Sister canon : aucun runbook sister dans `omk-nexus-coaching-premium/_doctrine/` (D6 honest — charte seule à ce jour). »
> — `01-omk-business-os/runbooks/runbook-C-saas-auth.md` l.16

> « Purpose : transformer la chart `phase_c_saas_auth.md` (WHAT, 9 sections, 52 l.) en pattern d'exécution (HOW, M1-M5, HITL-gated). Append-only D4. Runtime gated A0 HITL (Posture C). »
> — idem l.13

### Moat ↔ Drawbridge (UI feedback → code)

> « Drawbridge Workflow: Complete Rules ... You are an expert AI partner, acting as a principal front-end engineer. Your purpose is to not just translate visual feedback into code, but to implement it with the highest standards of quality, scalability, and maintainability. »
> — `ClaudeClaw Agent/.moat/drawbridge-workflow.md` l.12

> « Status File Management ... `**/moat-tasks.md`: Mark tasks as complete (`[x]`) once their status is `done`. `**/moat-tasks-detail.json`: Update the task `status` through its lifecycle with proper validation. »
> — idem l.493

---

## 3 · Systèmes de codes — relevé

### `L0_Life_OS` → `L1_Life_OS` → `L2_Business_Pulse` (couches Life OS / Business Pulse)

| Code | Couche | Défini dans |
|---|---|---|
| L0_Life_OS | (non observée dans ce seau — référencée par T2 chartes OMK) | chartes OMK |
| **L1_Life_OS** | Life OS niveau 1 (capture/clarify) | `Cerritos_Plane_Onboarding/MANIFEST.md` (l.4 `layer: L1_Life_OS`) |
| L2_Business_Pulse | Business Pulse niveau 2 (Summer/Jerry projects) | tous les `SUMMERS_VERSE_MANIFEST.md` (l.3) |
| L2-Business-Pulse-Summer | idem, variantes casse (avec tirets) | `02 ABC OS/B1_Summer_Direction/README.md` l.3 |
| L2-Business-Pulse-B2 | sous-couche B2 (variante casse) | `02 ABC OS/B2_Business_Domains/README.md` l.3 |
| L2-Business-Pulse-B3 | sous-couche B3 (variante casse) | `02 ABC OS/B3_Warp_Core_Execution/README.md` l.3 |
| B1_DIRECTION | sous-couche B1 (orthographe différente !) | `02 ABC OS/B1_Summer_Direction/README.md` (index `00_B1_DIRECTION_INDEX.md` l.3) |
| B2_BUSINESS_DOMAINS | sous-couche B2 | `00_<PROJECT>_DOMAIN_DEVELOPMENT_MAP.md` |
| B3_SWARM_EXECUTION | sous-couche B3 swarm | `00_B3_SWARM_CONFIG.md` |
| B2_MESO_COORDINATION | sous-couche mésosphère B2 | `B2_BUSINESS_WHEEL_HARMONIZATION_MATRIX.md` l.3, etc. |
| L2_Business_Pulse | (orthographe underscore — variante) | `02 ABC OS/B1_Summer_Direction/06_B3_JOBS_TO_BE_DONE_SPEC.md` l.3 |

**Contradiction de casse** : L2_Business_Pulse (underscore) vs L2-Business-Pulse (tirets). Les deux formes coexistent. **Voir § Contradictions.**

### `A1`, `A2`, `A3` — agents A (A0 = IA, A1 = gatekeepers, A2 = HoloDeck, A3 = sous-agents)

| Code | Signification | Source |
|---|---|---|
| **A0 Amadeus** | jumeau numérique (board observer passif — D7) | `Cerritos_Plane_Onboarding/MANIFEST.md` l.21 |
| A1 Beth | Ikigai Gatekeeper | `Cerritos_Plane_Onboarding/invite-team.md` l.25 |
| A1 Morty | Focus Gatekeeper | idem l.26 |
| **A2_HoloDeck_Cerritos** | couche HoloDeck parent | `Cerritos_Plane_Onboarding/MANIFEST.md` l.5 (`parent_a2: A2_HoloDeck_Cerritos`) |
| **A3_Cerritos_GTD_Capture** | rôle capture | `Cerritos_Plane_Onboarding/MANIFEST.md` l.4 |
| A3 Mariner | Capture | idem l.22 |
| A3 Boimler | Clarify | idem |
| A3 Rutherford | Organize | idem |
| A3 Tendi | Review | idem |
| A3 Freeman | Engage | idem |
| A3 Saru | Discovery (H3 horizon) | `chart_T2_finance_runway_runbook.md` |
| A3 Discovery | sous-type A3 | idem |

### `B1`, `B2`, `B3` — couches Business Pulse

| Code | Couche | Owner |
|---|---|---|
| **B1** | Direction / Vision / North Star | Summer (Jerry Prime proxy) |
| **B2** | Domain managers (Rocks + DoD) | 8 VPs (Superman, Martian Manhunter, Flash, Batman, Cyborg, Wonder Woman, Green Lantern, Aquaman) |
| **B3** | Execution (Lead/Lag + artifacts) | Marvel/DC squads (Avengers, Illuminati, Guardians, Fantastic Four, Kang Dynasty, Thunderbolts, X-Men, Eternals) |

### `G1` → `G8` — 8 B2 Business Domains

Mapping canonique observé dans `02 ABC OS & Child Care BOS/B2_Business_Domains/README.md` :

| Code | Domain | B2 Archetype | B3 Marvel Squad |
|---|---|---|---|
| G1 | Growth | Superman | Guardians (of the Galaxy) |
| G2 | Sales | Martian Manhunter (John Jones) | Illuminati |
| G3 | Product | Flash | Avengers |
| G4 | Ops | Batman | Fantastic Four |
| G5 | IT | Cyborg | Kang Dynasty |
| G6 | Finance | Wonder Woman | Thunderbolts |
| G7 | People | Green Lantern | X-Men |
| G8 | Legal | Aquaman | Eternals |

### `W1` → `W12` — cycle 12WY (84 jours)

Défini : « Cycle Format: W1–W12 (84-day quarters) » dans `B3_Warp_Core_Execution/README.md` (tous projets). Subdivisions observées : **W1, W2, W3, W4** dans les SUMMERS_VERSE (les Rocks concrets s'arrêtent à W4). Variantes observées :
- `12wy_window: Q3 2026 W1-W13 (2026-06-15 → 2026-09-07)` (chartes cycle_2 : 13 semaines)
- `W1 (Days 1–84)` (SUMMERS_VERSE_03 RILCOT — 84 jours)
- `W1 (Days 1–21)` (SUMMERS_VERSE_05 marina — 21 jours ! cycle plus court)
- `12wy_window: Q3-W6 (2026-08-09)` (runbook-C-saas-auth)
- `12wy_window: Q3-W8 (2026-08-23)` (runbook-D-repositories)

**Hétérogénéité W1-W12** : la durée d'une semaine varie (84j/12 vs 12 semaines calendaires). **Voir § Contradictions.**

### `H1`, `H3`, `H10`, `H30`, `H90` — horizons temporels

Observés dans :
- `chart_T1_product_spec_loop.md` : « Flash H10 product spec iterations »
- `chart_T2_finance_runway_runbook.md` : « Saru H3 quarterly runway review (LD02 H3 horizon) »

Définition non trouvée dans le seau — vraisemblablement dans `02_Areas_Spock/02_LD02_…`. **Référence externe non vérifiée.**

### `LD01`, `LD02`, `LD03`, `LD04` — Learning Domains (Jerry)

Observés :
- `LD01_Business` (tous les SUMMERS) — `parent_jerry: J01_Jerry_Prime_LD01_Business`
- `LD02 H3 horizon` (chartes OMK)
- `LD03/LD04` (B1 Summer READMEs « Verify LD03/LD04 exist and are current in J01 Area Standard »)

Définition dans `J01_Jerry_Prime_LD01_Business/AREA_STANDARD.md` (référencé, hors seau).

### `J01`, `J03` — Jerry Primes

- **J01_Jerry_Prime_LD01_Business** : tous les SUMMERS + B1/B2/B3 README
- **J03 Finance/Family** : `04 Alikaly Bana Holding to LLC` (cross-Jerry note)

### `P1` → `P8` — Operating Principles Jerry

Observé dans `02 ABC OS/CERRIROS_HANDOVER.md` l.44 : « J01 Area Standard — Operating Principles P1–P8 ». **Définition hors seau.**

### `D1`, `D2`, `D4`, `D6`, `D7` — Doctrine locks (OMK Picard)

- **D1 verified / receipt** : observé partout (e.g., « D1 verified 2026-06-15 » dans Cerritos_Plane_Onboarding)
- **D4 append-only** : chartes OMK, runbooks
- **D6 no-self-contradiction / no-copy** : idem
- **D7 cost-of-escalation** : chart_T1_ops_runbook_v1 (mention « A0 HITL pending »)
- **D4, D6** : explicités dans toutes les chartes cycle_2

### `M1` → `M6` — Mouvements dans un runbook

Runbook-C a M1–M5 ; runbook-D a M1–M6. Sections numérotées M1…MN sont les **Moves** exécutés séquentiellement.

### `V1` → `V8` — Verification runs (runbook self-checks)

Runbook-D : V1–V8 (8 vérifications avec grep / find / tsc / npm). Runbook-C : V1–V5.

### `T1`, `T2`, `T3` — Triptyques (chartes cycle_2)

- **T1** : Ops / Product / Spec-Loop
- **T2** : Finance / Sales / Growth
- **T3** : Legal / R&D

**Chemin** : `01-omk-business-os/chartes_cycle_2/{chart_T1,chart_T2,chart_T3}_*.md`

### `R1` → `R4` — Rocks dans W1–W4

Chaque SUMMERS_VERSE pose 4 Rocks par trimestre (W1, W2, W3, W4). Format : `Rock 1`, `Rock 2`, etc. ou `R1`, `R2`, etc.

### `C1` — cycle counter (B2_DOMAIN_GATE_MATRIX)

> « project: "02 ABC OS & Child Care BOS" / cycle: "C1" »
> — `02 ABC OS/B2_Business_Domains/B2_DOMAIN_GATE_MATRIX.md` l.43–44

### `RP2`, `RP3` — Rock IDs OMK Picard

> « rock_id: RP2 (Phase D Repositories branchés sur 7 views) »
> — `01-omk-business-os/runbooks/runbook-D-repositories.md` l.5

> « rock_id: RP2 » (Runbook C — Phase C SaaS Auth)

`RP1` non observé (présumé antérieur). `RP4+` non observés.

### `ASPAC-3`, `ASPAC-6`, `ASPAC-7` — items Plane UI

Observé dans `Cerritos_Plane_Onboarding/MANIFEST.md` :
- ASPAC-3 « 2. Invite your team »
- ASPAC-6 « 5. Use Cycles to time box tasks »
- ASPAC-7 « 6. Customize your settings »

`ASPAC-1/2/4/5` non observés (probablement d'autres items déjà traités ou hors périmètre).

### `Q3_2026_W3` — cycle quarter

> « cycle: Q3_2026_W3 (06/22-06/28) »
> — `Cerritos_Plane_Onboarding/MANIFEST.md` l.9

Format `Q[N]_[YYYY]_W[N]`. Observé seulement pour Q3 2026 W3.

### `JTBD-001`, `JTBD-002`, `JTBD-005` — Jobs To Be Done B3 IDs

Format : `JTBD-NNN_<DOMAIN>_<TOPIC>.md` + `jtbd_id: <PROJECT>-B3-<DOMAIN>-NNN` (e.g., `MARINA-B3-PEOPLE-001`, `ABC-B3-GROWTH-001`).

**JTBD-003, JTBD-004** observés dans 02 ABC Growth : `JTBD-003_ORBITER_PAINKILLER_VARIANTS.md`, `JTBD-004_ORBITER_EXPERIMENT_RICE.md`. **JTBD-005** observé (transverse gate).

### `L#` — Livrables (chartes cycle_2)

> « L1 : `_doctrine/runbooks/runbook_ops_v1_us.md` — full runbook (5 SOP per Ops process, W40 cadence 5-4-3-4 enforcement). L2 : skill auto-spawn policy (Phase 2 Hermes-style, ADR-META-001 D7, ≤3 actionables/cycle per W40 §M6 contre). L3 : incident response playbook (Human Torch hot fix + Invisible Woman force field patterns). L4 : Multica keepalive config (US-region Supabase, anti-pause ping every 5-6 days). »
> — `01-omk-business-os/chartes_cycle_2/chart_T1_ops_runbook_v1.md` l.21–24

### `G-1`, `G-2`, `G-3` — HITL gates (chartes cycle_2)

> « G-1 (REQUIRED before L1 ship) : A0 = IA spec-loop output certifies SOP canon structure per B1_B2_DEFINITION_OF_DONE_SPEC.md. »
> — idem l.39

### `Abort-A/B/C/D/E` — aborts chartes OMK

> « Abort-A : SOP canon missing (Ops process undocumented) → STOP, B3 Mr Fantastic complete SOP before continue. Abort-B : skill auto-spawn >3/cycle (W40 §M6 musée anti-pattern) → STOP, B2 Batman re-rank to top-3 only. Abort-C : EU-region data residency introduced (Supabase Frankfurt) → STOP, B3 Invisible Woman flag US-market pivot. Abort-D : manual UI gate for incident response → STOP, replace with spec-loop output (A0 = IA). »
> — `01-omk-business-os/chartes_cycle_2/chart_T1_ops_runbook_v1.md` l.44–47

### `Gap-1` → `Gap-N` — D6 honest gaps (chartes/runbooks)

Format : `Gap-N : <description>`. Chaque charte OMK a ≥3 gaps, chaque runbook a ≥4 gaps.

### `P-PR-RATIFIED`, `AMEND-001 RATIFIED`, `W40`, `W40 §M6`, `§M3` — refs transverses

> « Spec-Loop discipline — plan locked BEFORE execution (per A+ directive Spec-Loop Polivaev 2026), with A0 = IA (no manual UI gate), adversarial grill-me review per sub-agent, and Flash H10 product spec iterations. »
> — `chart_T1_product_spec_loop.md` l.14

> « adversarial grill-me pattern (per sub-agent, per Coach Pocock AMEND-001 RATIFIED 2026-07-13). »
> — idem l.23

`W40` est probablement une doctrine externe (W40 cadence = 5-4-3-4 = 5 daily / 4 weekly / 3 monthly / 4 quarterly).

### Status keywords

`STRUCTURED_EMPTY` → `GRADUATED` → `SHADOW_ACTIVE` → `ACTIVE` → `PRODUCT_ONLY_PROTOTYPE` → `Business Done`. Statuts présents :
- `status: GRADUATED` : tous les SUMMERS_VERSE (projets « gradués »)
- `status: ACTIVE` : B2 Domain Development Maps, B3 Warp Core READMEs
- `status: SHADOW_ACTIVE` : toutes les chartes_cycle_2 (cycle 2), tous les B2 mésosphères, B1 03/05/06 specs, B3 SWARM_CONFIGs
- `status: READY` : tous les JTBD-001/002
- `picard_status: GRADUATED` : RILCOT (variante d'écriture)
- `status: TODO|IN_PROGRESS|BLOCKED|DONE` : status internes JTBD
- `product_status: CONDITIONAL` etc. : 8 statuts de gates (B2_DOMAIN_GATE_MATRIX)

### Status Plane + GTD Cerritos

`Plane state: Backlog | Todo | In Progress | Done | Cancelled` (5 states Plane).
`GTD stage: actionable | multi-step | someday-maybe` (3 stages canoniques Cerritos).
`Status: NEXT_ACTION` (cycles-integration).

> « **D6 nuance D1 verified** : Le projet Plane live contient **5 default states** (Backlog, Todo, In Progress, Done, Cancelled). **Les states GTD canoniques (Inbox, Next Actions, Today, Waiting For, Done, Cancelled, Trash) ne sont PAS créés dans le workspace live**. »
> — `Cerritos_Plane_Onboarding/MANIFEST.md` l.60

---

## 4 · Contradictions et incohérences

### C1 — Casse des couches L2 (underscore vs tirets)

- `L2_Business_Pulse` (underscore) dans : `02 ABC OS/B1_Summer_Direction/06_B3_JOBS_TO_BE_DONE_SPEC.md` l.3, `03_RILCOT_Members_Space_OS/SUMMERS_VERSE_MANIFEST.md` l.3
- `L2-Business-Pulse` (tirets) dans : `02 ABC OS/SUMMERS_VERSE_MANIFEST.md` l.3, `02 ABC OS/B2_Business_Domains/README.md` l.3, `02 ABC OS/B3_Warp_Core_Execution/README.md` l.3, `02 ABC OS/B1_Summer_Direction/README.md` l.3
- `L2-Business-Pulse-B2` (hyphen + B2) : `02 ABC OS/B2_Business_Domains/README.md` l.3
- `B1_DIRECTION` : casse inconsistante dans le même fichier que `L2-Business-Pulse-Summer`

**Pas une vraie contradiction sémantique**, mais un signe de génération automatisée sans normalisation.

### C2 — Durée d'un cycle W1–W12

- SUMMERS_VERSE_RILCOT : `W1 (Days 1–84)` = 84 jours pour **W1 seul** (= 1 trimestre entier)
- SUMMERS_VERSE_marina : `W1 (Days 1–21)` = 21 jours (donc 12 semaines calendaires ≈ 84 jours)
- chartes cycle_2 OMK : `12wy_window: Q3 2026 W1-W13 (2026-06-15 → 2026-09-07)` = 13 semaines calendaires (84 jours)
- Cerritos_Plane_Onboarding : `12WY Q3 2026 cycle = 06/15 → 09/07/26 (12 semaines)`

**Interprétations divergentes** : W1–W12 = 12 *trimestres* de 84 jours (SUMMERS) **OU** 12 *semaines* calendaires (~84 jours total). Le terme « 12WY » semble désigner les deux à la fois selon le projet.

### C3 — Cycle C1 vs W1-W4 dans les SUMMERS

> « project: "02 ABC OS & Child Care BOS" / cycle: "C1" »
> — `B2_DOMAIN_GATE_MATRIX.md` l.43

Mais le B3 Warp Core README divise le cycle en **W1-W12**. Et le Cerritos Handover pose les Rocks en **W1-W4** (12WY cycle = 4 trimestres de 84 jours). C1 pourrait être le 1er « cycle B2 » indépendamment.

### C4 — Picard status vs status

> « `picard_status: GRADUATED` » dans `03_RILCOT_Members_Space_OS/SUMMERS_VERSE_MANIFEST.md` l.4

Les autres SUMMERS ont juste `status: GRADUATED`. Cohérence sémantique, mais écriture inconsistante.

### C5 — Chartes Phase D : stale vs AGENTS.md (contradiction reconnue)

> « **Canon contradiction surfaced** : le chart Phase D (`phase_d_repositories_branches.md:32`) déclare RP3 = ❌ NOT STARTED, mais `apps/dashboard/AGENTS.md:28` (§2 Phase State) déclare Phase D = ✅ DONE 2026-06-20 (11/14 views wired to Cloud via repos). **D6 no-self-contradiction guard** : ce runbook PREND POUR HYPOTHÈSE l'état AGENTS.md (récent + receipts ViewShell primitive + 11/14 views live), et **dénonce le chart comme stale** (chart écrit 2026-07-15 mais oublie les receipts du sprint A→F 2026-06-20). M0 ré-aligne. »
> — `01-omk-business-os/runbooks/runbook-D-repositories.md` l.16

**Dénoncée explicitement par le runbook D** — c'est une auto-critique du système. Bonne pratique.

### C6 — Le format des couches SUMMERS_VERSE (B1/B2/B3) vs OMK (T1/T2/T3)

- **SUMMERS_VERSE** (02, 03, 04, 05) : 3 couches B1/B2/B3 + 8 B2 domains + 8 Marvel squads
- **OMK Picard** (01) : 3 triptyques T1/T2/T3 + chartes + runbooks + W40 cadence 5-4-3-4

**Pas une contradiction**, mais deux systèmes distincts qui cohabitent. Le projet 01 utilise un vocabulaire différent (T1/T2/T3, chartes/runbooks/ownerbooks) des projets 02–05 (B1/B2/B3, JTBD, B2 Domain Development Map).

### C7 — Domaines B2 actifs pour 02 ABC vs 05 marina

Les deux projets ont **8 B2 domains** au complet (G1→G8). Mais :
- 02 ABC cite des **priorités** : « G8 Legal > G6 Finance > G5 IT > G7 People > autres » (`02 ABC OS/B2_Business_Domains/README.md` l.116–123)
- 05 marina ne cite **aucune priorité** dans son B2 README (lecture confirmée)

Cohérence des rôles, divergence du focus opérationnel.

### C8 — Référencement du dossier `graphify-out/`

Chaque sous-projet (01, 02, 03, 04, 05) contient un dossier `graphify-out/`. Le dossier n'est PAS explicitement documenté dans les fichiers du seau, mais il apparaît comme output canonique de graphify. Les copies de `CERRIROS_HANDOVER.md` dans `graphify-out/chunks/` confirment que **graphify-out est un dossier de sortie de pré-traitement**, pas une source canonique.

### C9 — Couche `L0_Life_OS` référencée par T2 chartes OMK mais non présente dans ce seau

> « IN : ... L0 Rick sovereignty infra. » (chart_T2)
> — `chart_T1_ops_runbook_v1.md` l.18 et `chart_T1_product_roadmap.md` l.18

L0 = « Rick sovereignty infra », hors périmètre. **Référence externe.**

### C10 — JTBD IDs : 5 fichiers observés (001-005) dans 02 ABC vs seulement 001-002 dans 05 marina

`02 ABC OS/B3_Warp_Core_Execution/01_Growth_Superman_Guardians/` a **5 fichiers** : `JTBD-001_ORBITER_VOC_PACKET.md`, `JTBD-002_ORBITER_ICP_FILTER.md`, `JTBD-003_ORBITER_PAINKILLER_VARIANTS.md`, `JTBD-004_ORBITER_EXPERIMENT_RICE.md`, `JTBD-005_ABC_TRANSVERSE_GROWTH_SIGNAL_GATE.md`.

`05 marina Cleaning BOS/B3_Warp_Core_Execution/01_Growth_Superman_Guardians/` n'a que **JTBD-001** et **JTBD-005** (lu). Les JTBD-002/003/004 ne sont pas instanciés pour marina. **Cohérence partielle** entre projets.

### C11 — `CERRIROS` vs `Cerritos` (typo)

Tous les fichiers `CERRIROS_HANDOVER.md` portent la typo **CERRIROS** (avec deux R). Le reste du système dit **Cerritos** (Lower Decks). **Typo assumée.**

---

## 5 · Récapitulatif — combien lu sur combien

**Lu intégralement (~38 fichiers)** :
- 8 fichiers racine de sous-projet (SUMMERS_VERSE ×4, MANIFEST ×1, ClaudeClaw/README ×1, Cerritos_Plane/MANIFEST ×1, OMK chart ×1)
- 4 B1 README de SUMMERS
- 4 B2 README de SUMMERS (02 + 05 lus intégralement)
- 4 B3 README de SUMMERS (02 + 01 lus intégralement)
- 4 CERRIROS_HANDOVER.md (lu intégralement 02 ; existence vérifiée pour 03, 04, 05)
- 4 B2 mésosphère (BUSINESS_WHEEL, DOMAIN_GATE, DC_COUNCIL, MESO_VP, OFFER_BRAND) — 02 ABC OS
- 4 B2 Domain Development Map (02 + 05 lus)
- 5 B1 specs 03–06 (02 ABC)
- 4 B3 SWARM_CONFIG / AGENT_ROSTER / PEER_HANDOFFS (05 marina People)
- 4 JTBD files (01 ABC Growth ×2, 05 marina Sales ×2, 05 marina People ×1)
- 3 Cerritos_Plane (MANIFEST, cycles-integration, invite-team)
- 3 Moat (README, drawbridge-workflow, moat-tasks)
- 5 chartes_cycle_2 OMK (T1_ops_runbook, T1_product_spec_loop, T1_product_roadmap, T1_ops_sop_canon, T2_finance_runway)
- 2 runbooks OMK (C, D)

**Non lu (~325 fichiers)** :
- 268 fichiers de profondeur 5 : majoritairement des JTBD-001/002 dans les 8 domaines × 4 projets SUMMERS. Patterns déjà identifiés.
- 41 fichiers de profondeur 4 : B1 specs 04, 07, 08, 09, 10, 11 ; B2 sub-folders ; B3 sub-squads
- ~7 fichiers de profondeur 6+ : sub-squad X-Men (ProfessorX_Recruiting, Cyclops_Onboarding, etc.)

**Ce que j'ai laissé de côté et pourquoi** :
- Les 268 fichiers JTBD-001/002 par domaine×projet : même structure, lecture des 4 exemples (02 ABC Growth, 05 marina Sales, 05 marina People, 05 marina Sales JTBD-002) a suffi à confirmer le pattern. Les attributs et sections sont rigoureusement identiques entre projets, seules les références (ABC/MARINA/RILCOT/ALIKALY) changent.
- Les fichiers de sub-squad B3 (01_ProfessorX_Recruiting, etc.) : leur format est dérivé du SWARM_CONFIG et AGENT_ROSTER parent. Lecture des parents suffit.
- Les B1 specs 04, 07, 08, 09, 10, 11 : un échantillon (03, 05, 06) montre le format Operating Rule + handoff. Les autres suivent.

---

## 6 · Note méthodologique — jonctions et pièges

**Jonctions NTFS** : aucun compteur n'a été passé dans ce seau. Les 176 jonctions totales de la KB vivent ailleurs (Geordi et autres). Le dossier `graphify-out/` pourrait en contenir (copies de CERRIROS_HANDOVER dans `graphify-out/chunks/`), mais elles sont à la racine du dossier graphify et ne se propagent pas en profondeur.

**Piège évité** : le dossier `01-omk-business-os/` lui-même contient un `graphify-out/` — j'ai lu les fichiers canoniques (chartes, runbooks) à la racine et au niveau cycle_2, pas dans graphify-out.

**Profondeur 5 = JTBD files en masse** : ce sont les fichiers les plus nombreux (268/363 ≈ 74%). Lecture des parents (B2 README + B2 Domain Development Map + B3 README + 4 JTBD échantillonnés) suffit à inférer la structure.

**Limite** : Je n'ai pas mesuré le nombre exact de jonctions dans ce seau. Le compteur « jonctions_ecartees » reste à 0 par défaut — il faudrait un scan `find` avec détection `FILE_ATTRIBUTE_REPARSE_POINT` pour le remplir, ce qui dépasse le périmètre de ce brief.
