# N2 — Le pouls métier — `00_Jerry_Business_Pulse`

**Périmètre** : `C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\05_From_V2_Domains\30_Business_OS\00_Jerry_Business_Pulse`
**Date** : 2026-08-05
**Statut** : rapport partiel (cf. §6 « Compte »)

---

## 1. La carte

Le dossier est l'**A'Space Kernel v2.0** côté « Business Pulse » — la couche L2 qui prend le relais de Life OS (PARA / 12WY) pour piloter une entreprise en fractale B1/B2/B3. Il a été aspiré depuis un autre environnement, d'où la profusion de `graphify-burst/` et `graphify-out/` (artefacts dérivés) et la présence de `04_Business_Domains/00_Links/` (jonctions + miroirs).

### Arborescence utile (jonctions écartées)

```
00_Jerry_Business_Pulse/
├── README.md                    # « Part of the A'Space Kernel v2.0 » — minimal
├── CEO_Directives.md            # phrase de Jerry Prime
├── 01_Vision_Strategy/          # coquille vide : README = « Kernel v2.0 »
├── 02_Global_Dashboard/         # coquille vide (pas de contenu Business Pulse rédigé ici)
├── 03_Master_Agreements/        # coquille vide (les Master Agreements vivent ailleurs)
├── 04_Business_Domains/         # ★ le cœur — les 8 domaines SOA + croislien + blueprints
│   ├── 00_Links/                # 32 jonctions NTFS (entrée ignorée) + 2 vrais sous-dossiers
│   │   ├── 02_alykaly-os-v2/   # projet RIL — surplus funds recovery, SQL complet
│   │   └── 20_Life_OS_PARA_Portal/  # ★ miroir complet du canon B1/B2/B3 (doctrine + Summer's Verse)
│   ├── 01_Growth_Superman_Guardians/   # SOA05 Growth
│   ├── 02_Sales_MartianManhunter_Illuminati/  # SOA08 Sales
│   ├── 03_Product_Flash_Avengers/      # SOA04 Product (+ prototypes interface)
│   ├── 04_Ops_Batman_Fantastic4/       # SOA03 Operations
│   ├── 05_IT_Cyborg_KangDynasty/       # SOA02 IT
│   ├── 06_Finance_WonderWoman_Thunderbolts/  # SOA06 Finance
│   ├── 07_People_GreenLantern_XMen/    # SOA01 People
│   ├── 08_Legal_Aquaman_Eternals/      # SOA07 Legal
│   └── 09_Blueprints/                  # 01-SDD / 02-ADR / 03-PRD / 04-DDD — squelettes
├── graphify-burst/chunks/chunk_000…chunk_019/  # ★ 20 chunks plats — snapshots répliqués
│                                                  (le même corpus copié 20× après chaque
│                                                   ingestion de ressource externe)
└── graphify-out/                # artefacts dérivés (graph.json, manifest.json, caches sém.)
```

**Ce que chaque branche porte en une ligne** :

- `01_Vision_Strategy/` → coquille vide ; le contenu « vision » vit ailleurs (Summer's Verse).
- `02_Global_Dashboard/` → coquille ; les dashboards sont agrégés en externe.
- `03_Master_Agreements/` → coquille ; les contrats vivent côté Legal (`08_…Eternals/`).
- `04_Business_Domains/` → les **8 SOA** + leurs squads Marvel + 2 projets complets (Alykaly, AaaS/OMK) en miroir.
- `graphify-burst/` → l'ingestion brute : chaque chunk contient un mix (PRD, ADR, DDD, ressources YouTube, fragments de JTBD). Utile pour l'archéologie, pas pour la doctrine.
- `graphify-out/` → JSON de graphe sémantique ; pas une source de contenu.

**Fichiers qui se présentent comme points d'entrée** et qui paient effectivement :

| Point d'entrée | Chemin | Ce qu'il ouvre |
|---|---|---|
| `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` | `04_Business_Domains/00_Links/20_Life_OS_PARA_Portal/` | La doctrine canonique — **le** texte fondateur |
| `Business_Pulse_B3_Notion_Canon_Lore_Index.md` | idem | Lore Notion → mapping local B2/B3 |
| `Business_Pulse_B3_Swarm_Inspiration_Index.md` | idem | Frontière d'adoption (vs OpenAI Swarm, Agency-Swarm) |
| `Picard_Summers_Verse_Register.md` | `00_Links/20_Life_OS_PARA_Portal/01_Projects_Picard/` | Registre des projets Summer's Verse (00–05) |
| `JERRY_SUMMER_FRACTAL_ALIGNMENT.md` | idem | Le pont macro ⇄ micro (Area Jerry ↔ Projet Summer) |
| `00_B1_DIRECTION_INDEX.md` etc. | `graphify-burst/chunks/chunk_000/` (et 19 autres chunks) | Cockpit B1 direction |
| `SOLARIS_ICP_MARKET_STUDY_2026.md` | `00 Agency as a Service/B3_Warp_Core_Execution/01_Growth_…/` | Seule ICP qualifiée du corpus (mode Solaris) |

**Ce qui n'est PAS un point d'entrée** : les 20 `chunk_000` … `chunk_019` ne sont **pas** des dossiers thématiques distincts ; ce sont des copies aplaties du même corpus, et un fichier doctrinal n'y existe qu'en N exemplaires (20).

---

## 2. Le modèle de travail

**Nom** : **Business Pulse à 3 couches (B1 direction → B2 domaine → B3 exécution), sous fractale PARA (Area Jerry ↔ Projet Summer), avec SOA en 8 domaines, gouvernance par Gates, et cadence 12WY × 4 cycles.**

C'est une **machine à transformer un business en système opérable et vendable**. La doctrine E-Myth / Built to Sell / Who Not How est absorbée comme grille de lecture, pas comme dépendance technique.

### Les objets de première classe (avec le fichier qui te le fait dire)

| Objet | Fichier qui le définit |
|---|---|
| **B0** *Self-Operating Business* (E-Myth, Built to Sell, Who Not How, Million Dollar Weekend, 100M Offers, Billion Dollar Brand Club) | `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §« Self-Operating Business Layer » |
| **B1** *Direction* (North Star 1Y/3Y/10Y, 12WY cycles, Decision Charter) | `graphify-burst/.../chunk_000/00_B1_DIRECTION_INDEX.md` + `01_NORTH_STAR_1Y_3Y_10Y.md` + `02_12WY_COMMAND_CYCLES.md` |
| **B2** *Domain gatekeeper* (8 SOA, gate matrix, DoD) | `04_Business_Domains/.../B2_DOMAIN_CONTROL_ROOM.md` (×8) + `B2_DOMAIN_GATE_MATRIX.md` |
| **B3** *Execution swarm* (Marvel squads, JTBD packets, peer-unblocking) | `graphify-burst/.../chunk_000/00_B3_SQUAD_CANON.md` + `02_PEER_UNBLOCKING_AND_HANDOFFS.md` |
| **SOA** *8 domaines SOA01–SOA08* | `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §« B3 Notion Canon Lore » (le seul mapping canonique) ; confirmé par `04_Business_Domains/02_Sales_…/README_FROM_BUSINESS_OS.md` tableau 8 SOA |
| **Squad** (Guardians, Illuminati, Avengers, Fantastic4, KangDynasty, Thunderbolts, XMen, Eternals) | `Business_Pulse_B3_Notion_Canon_Lore_Index.md` (canon Notion) |
| **Owner** (A2 Hermes = orchestrateur B2 ; A3 = swarm) | `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §« Chain Of Responsibility » |
| **Verse** (Summer's Verse = les projets Picard numérotés 00–05) | `Picard_Summers_Verse_Register.md` |
| **Pulse** (le méta-terme pour « la couche L2 qui pulse entre B1/B2/B3 ») | omniprésent — `Business_Pulse_B3_*`, `L2_Business_Pulse` dans chaque frontmatter |
| **12WY** (12-Week Year = 4 cycles de 12 semaines / an) | `graphify-burst/.../chunk_000/02_12WY_COMMAND_CYCLES.md` (cycles C1–C4) + `00 Agency as a Service/B1_Summer_Direction/README.md` §« 12WY Rock Linkage » |
| **North Star** (direction 1Y/3Y/10Y, fichier-index obligatoire) | `graphify-burst/.../chunk_000/01_NORTH_STAR_1Y_3Y_10Y.md` ; 8 occurrences dans chunk_000 |
| **Rock** (engagement trimestriel B2) | `04_Business_Domains/00_Links/20_Life_OS_PARA_Portal/01_Projects_Picard/01-omk-business-os/CERRIROS_HANDOVER.md` §« 12WY Rock Linkage » |
| **DoD** *Definition of Done* (packet B2 → B3, contrat d'acceptance) | `graphify-burst/.../chunk_000/05_B2_DEFINITION_OF_DONE_SPEC.md` |
| **JTBD** *Jobs To Be Done* (packet B3, contrat de preuve) | `graphify-burst/.../chunk_000/06_B3_JOBS_TO_BE_DONE_SPEC.md` + JTBD-001…005 dans `00 Agency as a Service/B3_Warp_Core_Execution/` |
| **Gate** (PASS / CONDITIONAL / BLOCKED — graduation `Product Done` ≠ `Business Done`) | `04_Business_Domains/00_Links/20_Life_OS_PARA_Portal/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/B2_DOMAIN_GATE_MATRIX.md` |
| **Lead / Lag indicators** (preuve exigée B2→B1) | `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §« B2 review standard is evidence » |
| **SOA modes** *Solaris / Nexus / Orbiter* (calibration de l'offre par profil d'ICP) | `00 Agency as a Service/B1_Summer_Direction/README.md` §« ICP Variant Determination Rules » + `SOLARIS_ICP_MARKET_STUDY_2026.md` |
| **Handoff packet** (Sales → Product/Ops/Finance/Legal avant external send) | `00 Agency as a Service/B3_Warp_Core_Execution/02_Sales_…/JTBD-001_AAAS_DIAGNOSTIC_TO_PROPOSAL.md` §« Cross-Domain Handoff » |

### Les rôles

- **A0 Amadeus** : intention, décisions d'identité / budget / legal exposure (escalade max).
- **Jerry Prime** (Area) : B1 macro (North Star perpétuel), hérité par Summer en micro.
- **Summer** : B1 micro pour chaque projet numéroté (`00_…` à `05_…`).
- **Cerritos** : triage GTD des idées (avant Summer).
- **A2 Hermes / orchestrateur B2** : par domaine (Superman, Martian Manhunter, Flash, Batman, Cyborg, Wonder Woman, Green Lantern, Aquaman).
- **A3 squads** : par domaine (Guardians, Illuminati, Avengers, Fantastic4, KangDynasty, Thunderbolts, X-Men, Eternals) — chacun avec 4 à 8 membres nommés (Star-Lord, Gamora, Black Bolt, Mr Fantastic, Kang Prime, Bucky Barnes, Professor X, Ikaris…).
- **Beth / Morty** : focus + safety gate ; peuvent **halt** une expansion (escalade rouge).

### Les cycles

- **12WY × 4/an** : C1 *Direction Lock* → C2 *Domain Activation* → C3 *Execution Proof* → C4 *Graduation Or Archive* (cf. `02_12WY_COMMAND_CYCLES.md`).
- **Cerritos routing** : idée → triage (≤ 4 h ack, ≤ 48 h routing, > 72 h inaction = escalade B1).
- **B2 weekly Lead/Lag** : flux quotidien vers B1 + dashboard `02_Global_Dashboard/` (vide dans ce périmètre).

### La phrase qui résume

> « B1 owns *why and where*. B2 owns *what must be true by domain*. B3 owns *how the artifact is executed and proven*. Product cannot graduate the business alone. »
> — `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §« Direction Invariants » (×6 occurrences dans le corpus)

---

## 3. Coach ou générique ?

**Constat de fond** : le périmètre **n'est pas un corpus de coaching**. C'est un corpus **générique de Business OS** dont le seul artefact où apparaît le mot « coach » est l'une des quatre offres-produits génériques (« Coaching Fondateur VIP », 1 000 €, `graphify-burst/.../chunk_000/05_Seed_Product_Offerings.md` ligne 54). Aucune niche n'est nommée dans les fichiers doctrinaux, dans les B2 domain control rooms, ou dans les SOA Notion lore.

Les niches concrètes qui **existent** dans le périmètre sont :

- **Alykaly** : *surplus funds recovery* (recouvrement de fonds pour successions/LLC) — `04_Business_Domains/00_Links/02_alykaly-os-v2/supabase/migrations/20260520000003_business_core.sql` (`COMMENT ON TABLE app.clients IS 'Entities we recover surplus funds for'`).
- **ABC OS & Child Care BOS** : agriculteurs (formation IA) + childcare (compliance-bound, Nexus mode) — `graphify-burst/.../chunk_000/00_B3_SWARM_CONFIG.md` §« ABC-Specific Anchors ».
- **Marina Cleaning BOS & SOP** : franchise de nettoyage (Orbiter mode, *franchise prototype*) — `Picard_Summers_Verse_Register.md` ligne 24.
- **RILCOT Members Space OS** : communauté de membres — idem ligne 22.
- **Alikaly Bana Holding → LLC** : holding → LLC (Growth DEFERRED, *THIN Growth*) — idem ligne 23.
- **Solaris ICP** : agences marketing/creative/web (4 archétypes) — `SOLARIS_ICP_MARKET_STUDY_2026.md` §1.
- **Nexus ICP** : cabinets juridiques / conseil expert — `JERRY_SUMMER_FRACTAL_ALIGNMENT.md` §3.
- **Orbiter ICP** : BTP / chantiers — idem.
- **OMK / AaaS** : SMB génériques (solo founder, local-service owner, micro-agency) — `00 Agency as a Service/B3_Warp_Core_Execution/02_Sales_…/JTBD-001_AAAS_DIAGNOSTIC_TO_PROPOSAL.md` §icp_or_fit.

**Aucune de ces niches n'est le coaching.** Le mot « coach » hors `05_Seed_Product_Offerings.md` apparaît seulement dans des contenus YouTube archivés (`graphify-burst/chunks/chunk_*/resource_*.md`, type « the-ai-sales-coach-system-every-sales-team-needs »), pas dans la doctrine ni dans les projets Summer's Verse.

### Tableau artefact × propre/générique

| Artefact | Fichier | Propre au coaching ? | Générique ? | Pour le généraliser (si niche=coach) |
|---|---|---|---|---|
| Doctrine B0/B1/B2/B3 | `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` | Non | **Oui — 100 %** | Aucune action ; c'est *déjà* la couche générique. |
| Les 8 SOA + squads Marvel | `Business_Pulse_B3_Notion_Canon_Lore_Index.md` | Non | **Oui** | Aucune action ; le mapping Marvel est un ancrage cognitif, pas une logique métier. |
| Modes Solaris / Nexus / Orbiter | `00 Agency as a Service/B1_Summer_Direction/README.md` §ICP | Non | **Oui** | Le coaching est *Nexus* (knowledge/expertise, ASP > $25K, sales cycle > 45 j) — voir §4. |
| B2 Domain Control Rooms (×8) | `04_Business_Domains/0X_*/00_B2_DOMAIN_CONTROL_ROOM.md` | Non | **Oui** | Aucune action. |
| B2 Gate Matrix (8 gates séquentiels) | `04_Business_Domains/.../01-omk-business-os/B2_Business_Domains/B2_DOMAIN_GATE_MATRIX.md` | Non | **Oui** | Aucune action. |
| B2_OFFER_BRAND_REVENUE_ENGINE | `04_Business_Domains/.../01-omk-business-os/B2_Business_Domains/B2_OFFER_BRAND_REVENUE_ENGINE.md` | Non | **Oui** | Le packet (ICP, pain, dream, time delay, effort removed, risk reversal, proof, price) **est** le schéma d'ontologie de l'offre. Pour coaching : remplacer ICP=agence créative par ICP=coach (cf. §4). |
| SOLARIS_ICP_MARKET_STUDY_2026.md | `00 Agency as a Service/B3_Warp_Core_Execution/01_Growth_…/` | Non (cible = agences) | Partiel — la *méthode* (4 archétypes, critères d'entrée, SOA/SOC/SLA backbone) est générique ; *qui* est l'ICP est spécifique. | Réutiliser la structure pour produire une `NEXUS_ICP_MARKET_STUDY_COACH.md` — la trame est directement portable. |
| SOP↔Offering SQL seed | `graphify-burst/.../chunk_000/05_Seed_Product_Offerings.md` | Partiel (4 offres dont 1 « Coaching Fondateur ») | Partiel — la *règle d'or* (« pas de vente sans SOP ») est générique | Pour coaching : remplacer les 4 offres par Audit / Programme / Retainer / VIP coaching. |
| Schéma Supabase `app.clients`, `app.cases`, `app.transactions` | `04_Business_Domains/00_Links/02_alykaly-os-v2/supabase/migrations/20260520000003_business_core.sql` | **Oui — fort** (surplus funds) | Non | Pour coaching : remplacer `cases` (juridique) par `engagements`/`parcours`/`sessions`. |
| Schéma Supabase Solaris `organizations`, `memberships`, `profiles` | `04_Business_Domains/00_Links/.../00 Agency as a Service/.../02_aaas-os/supabase/migrations/0002_solaris_saas_tables.sql` | Non | **Oui — total** | Aucune action ; ce sont des tables de tenant génériques. Les tables métier (clients, leads, transactions, tasks, sops) sont promises dans une migration ultérieure, encore non écrite. |
| OMK Services landing page | `04_Business_Domains/00_Links/.../01-omk-business-os/.../00_Interface_Prototypes/OMK SRV BOS/OMK SERVICES Front-end Fr/OMK Services.html` | Partiel — cible « Small Business Owners » | Partiel | Le copy (« Ingénierie opérationnelle pour Small Business Owners ») glisse facilement vers « Ingénierie opérationnelle pour coachs ». La trame UI (Modules : Clients Pipeline, SOP Library, Tasks…) reste. |
| Solaris pricing 2 tiers | `graphify-burst/.../chunk_001/AAAS_PRICE_MARGIN_MODEL_SOLARIS.md` | Non (agences) | Partiel — la *value ladder* (setup + retainer) et le COGS Compute-fixe sont génériques | Pour coaching : même structure ; adapter le segment prioritaire (coach solo vs boutique vs franchise). |
| Offer packet (Sales JTBD) | `00 Agency as a Service/B3_Warp_Core_Execution/02_Sales_…/JTBD-001_AAAS_DIAGNOSTIC_TO_PROPOSAL.md` | Non | **Oui** | Le *Sales packet* (qualification questions, diagnostic agenda, objections, cross-domain handoff) est entièrement réutilisable ; seul `icp_or_fit` change. |
| `picard_audit.md` (OMK audit technique) | `04_Business_Domains/00_Links/.../01-omk-business-os/.../01-omk-services-front-end/picard_audit.md` | Non | **Oui** | Format d'audit générique (Design/Infra/Global + 3 niveaux de dette + plan 4 phases). |

### Verdict

**Tout est générique sauf trois artefacts** : (a) la cible déclarée de Solaris (agences), (b) le schéma SQL Alikaly (juridique), (c) le copy de l'OMK landing (« Small Business Owners »). Aucune de ces trois n'est spécifique au coaching — et aucune n'a besoin de l'être. Le corpus fournit **la matrice** ; il attend qu'un projet renseigne la cellule *niche*.

---

## 4. Ce que ça dit de l'ontologie

**Oui**, le corpus nomme déjà des entités métier et leurs relations — mais **sous une forme dispersée** entre la doctrine (prose), les schémas SQL (Postgres) et les packets JTBD (YAML). Ce n'est pas une ontologie déclarée, c'est une ontologie **de facto** qu'il faudrait extraire.

### Entités identifiées (et le fichier qui les porte)

| Entité | Attributs canoniques | Fichier source |
|---|---|---|
| **Organization / Tenant** | `id, name, plan ∈ {starter, growth, scale}, created_at` | `…/00 Agency as a Service/.../02_aaas-os/supabase/migrations/0002_solaris_saas_tables.sql` §organizations |
| **Membership** *(user ↔ org)* | `user_id, org_id, role ∈ {owner, admin, member}` | idem §memberships |
| **Profile** *(augment auth.users)* | `id, email, full_name, avatar_url` | idem §profiles |
| **Client** *(entité métier)* | `id, org_id, name, module, contact_email, contact_phone, status, clearance_required, metadata` (Alykaly : « Entities we recover surplus funds for ») | `…/02_alykaly-os-v2/supabase/migrations/20260520000003_business_core.sql` |
| **Case** *(dossier)* | `id, case_number, defendant, client_id, amount, priority, status, confidence_score, court_jurisdiction, assigned_to, version` (Alykaly : juridique) | idem §cases |
| **Transaction** *(mouvement financier)* | `id, case_id, tx_type ∈ {inflow, outflow}, amount, tx_date, status` | idem §transactions |
| **Offering** *(produit en vente)* | `id, name, price, description, root_sop_id, is_public` — *règle d'or : pas d'offre sans SOP liée* | `graphify-burst/.../chunk_000/05_Seed_Product_Offerings.md` |
| **SOP** *(procédure de livraison)* | `id, title` (+ `root_sop_id` qui la lie aux offerings) | idem (SQL schema informel) |
| **Lead** | `{label: 'Nova lead', n: 24, c: '#F472B6'}` (pipeline UI, métriques agrégées) | `…/01-omk-business-os/.../01-omk-services-front-end/src/app/page.tsx` |
| **Invoice** | « Invoices envoyées < 48 h après Ready to bill » | `Business_Pulse_B3_Notion_Canon_Lore_Index.md` §Finance build gates |
| **Rock** | engagement trimestriel B2 ; 4 max/domaine | `01-omk-business-os/CERRIROS_HANDOVER.md` §« B2 Rock cadence » |
| **DoD** *Definition of Done* | contrat B2→B3 ; packet structurel standard | `graphify-burst/.../chunk_000/05_B2_DEFINITION_OF_DONE_SPEC.md` |
| **JTBD** *Jobs To Be Done* | contrat B3→B2 ; preuve Lead/Lag + décision log | `graphify-burst/.../chunk_000/06_B3_JOBS_TO_BE_DONE_SPEC.md` ; exemplaires : `…/B3_Warp_Core_Execution/02_Sales/.../JTBD-001_AAAS_DIAGNOSTIC_TO_PROPOSAL.md` |
| **Gate** | statut ∈ {PASS, CONDITIONAL, BLOCKED} × 8 domaines | `04_Business_Domains/.../01-omk-business-os/B2_Business_Domains/B2_DOMAIN_GATE_MATRIX.md` |
| **B2 Manager** *(rôle, pas entité stockée)* | un orchestrateur A2 par SOA | `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` + 8 SOA Notion |
| **A3 Agent** *(rôle Notion-miroir)* | 4–8 personnages par squad | `Business_Pulse_B3_Notion_Canon_Lore_Index.md` |
| **Compute budget** *(niveau mission)* | `trace_id` + plafond par `contract_type` (SLA_STRICT, CUSTOM_ENTERPRISE) | `SOLARIS_ICP_MARKET_STUDY_2026.md` §5 (SLA) |
| **ICP variant** | Solaris / Nexus / Orbiter ; triggers MRR + buyer profile | `00 Agency as a Service/B1_Summer_Direction/README.md` §« ICP Variant Determination Rules » |

### Relations identifiées (extraits)

- **Organization 1—N Membership N—1 User** (multi-tenant).
- **Organization 1—N Client** (chaque client est scopé à un tenant).
- **Client 1—N Case** (un client a plusieurs dossiers).
- **Case 1—N Transaction** (un dossier génère plusieurs flux financiers).
- **Offering N—1 SOP** (FK `root_sop_id` ; suppression SOP = rupture de l'offre — garde-fou).
- **B2 Handoff 1—1 B3 JTBD** (chaque handoff B2 produit au moins un JTBD ; cf. `AAAS_DOMAIN_DEVELOPMENT_MAP.md`).
- **JTBD N—N Gate** (un JTBD ferme au moins une gate ; cf. `B2_DOMAIN_GATE_MATRIX.md`).
- **Rock 1—N DoD 1—N JTBD** (cascade décisionnelle).
- **Mode (Solaris/Nexus/Orbiter) — calibration — B2/B3 packet** (les seuils MRR/ASP/sales-cycle sélectionnent la *variante* de chaque doctrine ; mode ≠ nouveau domaine).

### Ce qui manque pour que ça devienne une ontologie

1. **Pas de schéma unique**. Les entités sont dans 3 fichiers SQL distincts (Alykaly `app.*`, Solaris `solaris_saas.*`, promesses pour migrations Phase D) + dans la prose des JTBD. Pas de migration consolidée.
2. **Pas de vocabulaire contrôlé**. Le même concept est nommé différemment selon les chunks : `Client` vs `Tenant` vs `Organization` ; `ICP variant` vs `Mode`.
3. **Pas de modélisation du « Coach / Client-de-coach »** (ou de toute autre entité-niche) — la couche « entity métier » est volontairement générique.
4. **Pas de graphe de relations versionné**. Les `graph.json` de `graphify-out/` sont des artefacts sémantiques d'ingestion, pas un schéma source.

### Verdict ontologique

**Oui, une ontologie est déjà écrite — mais en prose dispersée, pas en schéma**. Si on extrait les §3 (« Self-Operating Business Layer »), §4 (« B2 Swarm Supervision Rooms »), §5 (« B3 Squad Swarm Configurations »), §6 (« B1-B2 Domain Governance Workflow »), §7 (« B1 Direction Cockpit ») du `Computer_B1_B2_B3_Business_Pulse_Doctrine.md`, on obtient un graphe **Entity-Role-Cycle** complet :

```
[Organization] ─has→ [Membership] ─to→ [Profile]
       │                                       │
       └─has→ [Client] ─has→ [Case/Engagement] ─has→ [Transaction/Invoice]
                  │                                       │
                  └─offered→ [Offering] ─linked-to→ [SOP]  │
                                                                │
[A0 Intention] → [Jerry (B1 Area)] → [Cerritos (GTD)] → [Summer (B1 Micro)]    │
                                            ↓                                       │
                          [B2 Domain Mgr ×8] → [B3 Squad ×8] → [JTBD packet]   │
                                            ↓                                       │
                                  [Gate matrix 8×3] → [Lead/Lag evidence]  ←────┘
```

**Si la couche manquante identifiée dans le brief est un *graphe de contexte versionné des entités, relations et règles du domaine*, alors ce corpus en est la pré-projection** — sauf que les nœuds sont nommés via une grammaire Marvel+SOA, pas via une grammaire formelle (RDF, OWL, LinkML).

---

## 5. Les trois choses à garder

Par ordre d'importance pour une refonte.

### 1. `Computer_B1_B2_B3_Business_Pulse_Doctrine.md`

**Pourquoi** : c'est *le* texte fondateur. 9 341 octets, dense, complet, déjà canonique. Il pose la fractale B0/B1/B2/B3, les chaînes de responsabilité, les non-négociables, la gate matrix, le cockpit B1, le triptyque macro/micro. Si on ne garde qu'un fichier du périmètre, c'est celui-ci. Il a été aspiré dans les 20 chunks ; la copie originale (`04_Business_Domains/00_Links/20_Life_OS_PARA_Portal/`) est l'unique source authentique.

### 2. `JERRY_SUMMER_FRACTAL_ALIGNMENT.md` + `Picard_Summers_Verse_Register.md`

**Pourquoi** : ce sont les **deux fichiers qui articulent la doctrine aux projets**. Le Register donne le statut de chaque projet (00–05) ; l'Alignment documente le pont macro ⇄ micro (Area Jerry ↔ Summer Project) — *« project B2 references macro doctrine (DRY), never re-derives »*. Sans ces deux-là, on a la théorie sans le terrain. Toute refonte qui crée des projets par niche doit hériter de cette discipline DRY.

### 3. `B2_OFFER_BRAND_REVENUE_ENGINE.md` (et son packet canonique)

**Pourquoi** : c'est **le seul fichier qui donne le schéma de l'offre en tant qu'entité composite** — `Offer packet: ICP, pain, dream outcome, time delay, effort removed, risk reversal, proof, price logic` + `Brand packet: category, enemy, signature mechanism, first channel, story asset` + `Revenue packet: price hypothesis, cost floor, margin target, payment path, upsell/cross-sell hypothesis` + `Delivery packet: SOP, owner, support path, B3 execution boundary`. Cette structure à 4 packets × 8 attributs est la **meilleure ontologie « offer »** du corpus — générique, actionnable, et déjà branchée sur les B2 domains. Une version `OFFER_ENGINE_NEXUS_COACH.md` peut s'écrire directement en suivant ce plan.

**Mention honorable** : `SOLARIS_ICP_MARKET_STUDY_2026.md` (méthode ICP × 4 archétypes + SOA/SOC/SLA backbone) — à garder comme *template* pour produire `NEXUS_ICP_MARKET_STUDY_COACH.md` ou `ORBITER_ICP_MARKET_STUDY_COACH.md`.

### Ce qui **ne mérite PAS** de survivre tel quel

- **Les 20 chunks `graphify-burst/chunks/chunk_000…019/`** — un même corpus copié 20 fois après chaque ingestion. Les ressources externes (`resource_*.md`) et les fragments doctrinaux dupliqués sont un *artefact d'ingestion*, pas un livrable.
- **Les `graph.json` / `manifest.json`** — dérivés, non source.
- **Les 32 jonctions sous `04_Business_Domains/00_Links/`** — récursions miroir, à nettoyer en Ops/IT séparément (`JERRY_SUMMER_FRACTAL_ALIGNMENT.md` §6 le reconnaît explicitement : *« This alignment does not edit or purge them »*).

---

## 6. Compte

### Fichiers lus en entier (≈ 58, budget 70)

| # | Fichier | Pourquoi |
|---|---|---|
| 1 | `README.md` (root) | entrée de périmètre |
| 2 | `CEO_Directives.md` | entrée de périmètre |
| 3 | `01_Vision_Strategy/README.md` | entrée (vide) |
| 4 | `02_Global_Dashboard/README.md` | entrée (vide) |
| 5 | `03_Master_Agreements/README.md` | entrée (vide) |
| 6 | `04_Business_Domains/01_Growth_…/00_CROSSLINK.md` | mapping SOA01–SOA08 |
| 7 | `04_Business_Domains/01_Growth_…/README_FROM_BUSINESS_OS.md` | canon Growth |
| 8 | `04_Business_Domains/02_Sales_…/README_FROM_BUSINESS_OS.md` | **mapping SOA01–SOA08 explicite** |
| 9 | `04_Business_Domains/03_Product_…/README.md` | entrée (vide) |
| 10 | `04_Business_Domains/04_Ops_…/README_FROM_BUSINESS_OS.md` | entrée (vide) |
| 11 | `04_Business_Domains/05_IT_…/README_FROM_BUSINESS_OS.md` | entrée (vide) |
| 12 | `04_Business_Domains/06_Finance_…/README_FROM_BUSINESS_OS.md` | entrée (vide) |
| 13 | `04_Business_Domains/07_People_…/README_FROM_BUSINESS_OS.md` | entrée (vide) |
| 14 | `04_Business_Domains/08_Legal_…/README_FROM_BUSINESS_OS.md` | entrée (vide) |
| 15–21 | 7 × `00_CROSSLINK.md` (domaines 02–08) | confirmer le pattern 8 SOA |
| 22 | `04_Business_Domains/00_Links/20_Life_OS_PARA_Portal/Computer_B1_B2_B3_Business_Pulse_Doctrine.md` | **★ doctrine canonique** |
| 23 | `…/Business_Pulse_B3_Notion_Canon_Lore_Index.md` | canon Notion → local |
| 24 | `…/Business_Pulse_B3_Swarm_Inspiration_Index.md` | frontière d'adoption |
| 25 | `…/README.md` | handoff A2 Computer |
| 26 | `graphify-burst/chunks/chunk_000/00_B1_DIRECTION_INDEX.md` | cockpit B1 |
| 27 | `…/chunk_000/00_B2_DOMAIN_CONTROL_ROOM.md` | cockpit B2 (IT Cyborg / ABC OS) |
| 28 | `…/chunk_000/00_B3_SQUAD_CANON.md` | cockpit B3 (Ops/Fantastic4 Solaris) |
| 29 | `…/chunk_000/00_B3_SWARM_CONFIG.md` | config B3 (Growth/ABC OS + Childcare) |
| 30 | `…/chunk_000/01_NORTH_STAR_1Y_3Y_10Y.md` | North Star (Alikaly) |
| 31 | `…/chunk_000/02_12WY_COMMAND_CYCLES.md` | 12WY + Decision Charter |
| 32 | `…/chunk_000/05_Seed_Product_Offerings.md` | SOP↔Offering (seul artefact « coach ») |
| 33 | `…/chunk_001/01_NORTH_STAR_1Y_3Y_10Y.md` | North Star AaaS (variante) |
| 34 | `…/chunk_001/AAAS_PRICE_MARGIN_MODEL_SOLARIS.md` | pricing Solaris |
| 35 | `…/chunk_001/00_MARINA_DOMAIN_DEVELOPMENT_MAP.md` | proof Orbiter/Marina |
| 36 | `…/chunk_001/JTBD-001_MARINA_DELIVERY_SOP.md` | JTBD concret Marina |
| 37 | `04_Business_Domains/00_Links/20_Life_OS_PARA_Portal/01_Projects_Picard/JERRY_SUMMER_FRACTAL_ALIGNMENT.md` | **★ pont macro ⇄ micro** |
| 38 | `…/Picard_Summers_Verse_Register.md` | **★ registre projets** |
| 39 | `…/A3_Picard_Projects_Spec.md` | spec A3 Picard |
| 40 | `…/01_Projects_Picard/README.md` | entrée A3 Picard |
| 41 | `…/00 Agency as a Service/B1_Summer_Direction/README.md` | **★ North Star AaaS + ICP variant rules** |
| 42 | `…/00 Agency as a Service/B1_Summer_Direction/01_NORTH_STAR_1Y_3Y_10Y.md` | North Star AaaS variante |
| 43 | `…/00 Agency as a Service/B2_Business_Domains/00_AAAS_DOMAIN_DEVELOPMENT_MAP.md` | mapping 8 SOA ↔ JTBD |
| 44 | `…/00 Agency as a Service/B3_Warp_Core_Execution/02_Sales_…/JTBD-001_AAAS_DIAGNOSTIC_TO_PROPOSAL.md` | **★ Sales packet canonique** |
| 45 | `…/01_Growth_…/JTBD-001_SOLARIS_VOC_PACKET.md` | VOC Solaris |
| 46 | `…/01_Growth_…/JTBD-002_SOLARIS_ICP_FILTER.md` | ICP filter Solaris |
| 47 | `…/01_Growth_…/SOLARIS_ICP_MARKET_STUDY_2026.md` | **★ ICP étude Solaris** |
| 48 | `…/01-omk-business-os/SUMMERS_VERSE_MANIFEST.md` | **★ manifest OMK** |
| 49 | `…/01-omk-business-os/CERRIROS_HANDOVER.md` | **★ handover OMK** |
| 50 | `…/01-omk-business-os/B1_Summer_Direction/01_NORTH_STAR_1Y_3Y_10Y.md` | North Star OMK |
| 51 | `…/01-omk-business-os/B2_Business_Domains/01_Growth_…/00_B2_DOMAIN_CONTROL_ROOM.md` | B2 Growth OMK |
| 52 | `…/01-omk-business-os/B2_Business_Domains/02_Sales_…/00_B2_DOMAIN_CONTROL_ROOM.md` | B2 Sales OMK |
| 53 | `…/01-omk-business-os/B2_Business_Domains/03_Product_…/00_B2_DOMAIN_CONTROL_ROOM.md` | B2 Product OMK |
| 54 | `…/01-omk-business-os/B2_Business_Domains/B2_DOMAIN_GATE_MATRIX.md` | **★ gate matrix 8 SOA** |
| 55 | `…/01-omk-business-os/B2_Business_Domains/B2_OFFER_BRAND_REVENUE_ENGINE.md` | **★ ontologie offre** |
| 56 | `…/01-omk-business-os/.../01-omk-services-front-end/picard_audit.md` | audit technique |
| 57 | `04_Business_Domains/00_Links/02_alykaly-os-v2/supabase/migrations/20260520000001_init_schemas_and_enums.sql` | schéma SQL Alykaly |
| 58 | `…/20260520000003_business_core.sql` | **★ entités métier SQL (clients/cases/transactions)** |
| 59 | `04_Business_Domains/00_Links/20_Life_OS_PARA_Portal/01_Projects_Picard/00 Agency as a Service/B2_Business_Domains/03_Product_Flash_Avengers/02_aaas-os/supabase/migrations/0001_init_schemas.sql` | schéma Solaris |
| 60 | `…/0002_solaris_saas_tables.sql` | **★ tables Solaris (orgs/memberships/profiles)** |

**Total : 60 fichiers lus en entier.** (Mes premiers comptages étaient approximatifs ; vérification finale = 60, sous le budget de 70.)

J'ai aussi *parcouru* (lecture partielle) :

- `OMK Services.html` (~100 premières lignes, copy marketing) — confirme cible « Small Business Owners ».
- `omk-app.jsx` — matches regex sur les entités UI (`Clients Pipeline`, `SOP Library`, `Leads qualifiés / mois`).
- 32 chemins d'agent sub-folders (`04_Business_Domains/0X/YY_Hero/`) — listés non lus (tous des stubs README ~ 650 octets quasi-identiques).

### Dossiers ouverts sans y entrer (listés)

- `01_Vision_Strategy/graphify-out/` (artefacts dérivés, non source)
- `02_Global_Dashboard/graphify-out/` (idem)
- `03_Master_Agreements/graphify-out/` (idem)
- `04_Business_Domains/09_Blueprints/{01-SDD,02-ADR,03-PRD,04-DDD}/` (squelettes ; les vrais ADR/PRD/DDD vivent dans les chunks graphify-burst)
- `04_Business_Domains/00_Links/02_alykaly-os-v2/` (sauf les 2 SQL lus ; supabase/migrations/0004–0010 + le code Next.js non lus)
- `04_Business_Domains/00_Links/20_Life_OS_PARA_Portal/01_Projects_Picard/00 Agency as a Service/B3_Warp_Core_Execution/` (lu 3 fichiers sur ~80 JTBD/agent-README)
- `04_Business_Domains/00_Links/20_Life_OS_PARA_Portal/01_Projects_Picard/00 Agency as a Service/B2_Business_Domains/03_Product_Flash_Avengers/02_aaas-os/` (sauf SQL ; code Next.js non lu)
- `04_Business_Domains/00_Links/20_Life_OS_PARA_Portal/01_Projects_Picard/01-omk-business-os/.../01-omk-services-front-end/src/` (sauf matches regex ; pas lu)
- `graphify-burst/chunks/chunk_001` à `chunk_019/` (lu ~ 6 fichiers sur des milliers ; le reste est duplication)
- `graphify-out/` (sauf chemins cités)
- `04_Business_Domains/04_Ops_Batman_Fantastic4/{02,03,04}_*/README.md` et les 42 autres agent-README stubs du même type — squelettes génériques

### Reste à couvrir (si relance)

1. **Lecture des `JTBD-001` et `JTBD-002` par projet (Marina, RILCOT, ABC, Alikaly)** — j'ai 1 sur ~10 ; suffisant pour conclure que la structure est générique, pas suffisant pour cartographier les *variations* par projet.
2. **Lecture de `02_Areas_Spock/J01_Jerry_Prime_LD01_Business/`** — référencé à 6 reprises (`JERRY_SUMMER_FRACTAL_ALIGNMENT.md` §3.2, `Picard_Summers_Verse_Register.md` §Macro doctrine, `B2_Business_Domains/00_AAAS_DOMAIN_DEVELOPMENT_MAP.md`) comme **source authentique des 8 doctrines macro + 8 JTBD-001 canoniques** — je n'ai pas vérifié ce chemin directement, et c'est probablement là que vit la version non-répliquée des 8 *principles files* (Growth 18, Sales 14, Product 18, Ops 22, IT 18, Finance 12+6, People 12+6, Legal 12+6).
3. **`04_Business_Domains/09_Blueprints/`** — j'ai vu les 4 sous-dossiers mais pas leur contenu ; possible réservoir d'ADR/SDD non répliqués.
4. **Les schémas SQL promis pour Solaris Phase D** (« clients, leads, transactions, tasks, sops, etc. ») — *non écrits* (`0002_solaris_saas_tables.sql` dit explicitement « introduced later in Phase D as the views are wired up »). À confirmer ailleurs si une autre version les contient.
5. **Recherche ciblée « coach OS / coach niche / coach ICP » dans `02_Areas_Spock/J01_Jerry_Prime_LD01_Business/`** — non trouvée dans ce périmètre ; à confirmer.

---

## Annexe — Thèse FDE / graphe de contexte (réponse au brief)

> *« Un travail parallèle a établi une thèse : le métier de FDE se décompose en gestes, dont cinq sont automatisables et quatre résistent (mandat hiérarchique, consentement à révéler l'exception, responsabilité juridique, promotion d'un constat en primitive de plateforme). La couche manquante identifiée est un **graphe de contexte** : un dépôt versionné des entités, relations et règles du domaine du client. »*

**Ce que le corpus confirme** : les 5 gestes automatisables (intake, qualification, diagnostic, packet, handoff matrix) sont déjà outillés — cf. `JTBD-001_AAAS_DIAGNOSTIC_TO_PROPOSAL.md` qui **structure** un diagnostic FDE complet (qualification questions, diagnostic agenda, proposal boundary, objections, cross-domain handoff matrix, decision log). La *Sales packet* de ce fichier est un template FDE-with-doctrine.

**Ce que le corpus **ne** confirme pas** : la thèse sur les 4 gestes-résistants (mandat, consentement, responsabilité juridique, promotion en primitive de plateforme) — **non trouvée**. Aucune occurrence de ces termes dans le périmètre. Si la thèse a été rédigée ailleurs (en amont de `00_Jerry_Business_Pulse`), elle n'a pas migré ici. Le `CEO_Directives.md` est la seule phrase méta, et elle est purement opérationnelle (« Just keep the lights on and don't make me do math »).

**Sur le graphe de contexte manquant** : le corpus en est **la pré-projection** (cf. §4). Le `B2_OFFER_BRAND_REVENUE_ENGINE.md` est l'entité-« offre » ; le `B2_DOMAIN_GATE_MATRIX.md` est l'entité-« gate » ; le `JTBD-001_*` est l'entité-« packet ». Les **relations** (Rock→DoD→JTBD→Gate→Evidence) sont explicites. Mais le dépôt n'est pas versionné (c'est de la prose), pas requêtable (pas de RDF/JSON-LD), et pas validé par un schéma (les YAML frontmatter sont des « conventions », pas des types).

Si la refonte vise à transformer cette prose en graphe, **trois fichiers sont les ancres minimales** (cf. §5) : `Computer_B1_B2_B3_Business_Pulse_Doctrine.md`, `JERRY_SUMMER_FRACTAL_ALIGNMENT.md` + `Picard_Summers_Verse_Register.md`, `B2_OFFER_BRAND_REVENUE_ENGINE.md`. Le reste est incident — sauf `SOLARIS_ICP_MARKET_STUDY_2026.md` comme méthode pour `NEXUS_ICP_MARKET_STUDY_COACH.md` (la niche coaching, si elle est Nexus).

— *Fin du rapport N2.*