# Cartographie — 04_Archives_Data

> Cartographie ontologique du seau **04_Archives_Data** du PARA de V2.
> Lecture des fichiers de structure : **1 534 chemins** dans `carto/structure.txt` filtrés sur `04_Archives_Data`.
> Fichier écrit au fil de l'eau. La structure est essentiellement celle d'un **snapshot figé** : `_V3_STRUCTURE_2026-08-02/` (1 516 fichiers), `Legacy_LifeOS_App_Specs_2026-05-22/` (15 fichiers), un dossier `03_OpenClaw_Body_Legacy/` (lu seulement en méta — il n'apparaît qu'à 1 entrée dans le filtre), un `README.md` et un `A3_Data_Archives_Spec.md` à la racine du seau.

## Périmètre lu

| Métrique | Valeur |
|---|---|
| Fichiers disponibles (filtrés) | **1 534** |
| Fichiers lus au long | ~30 (tous racine/secteur + 2 AaaS doctrine) |
| Fichiers parcourus en méta (ls) | ~80 |
| Jonctions NTFS écartées | **0** (cf. §9) |

**Choix de lecture.** Ce seau est, à 99 %, une **archive photographique** : la structuration entière d'ASpace_OS_V3 versée le 2026-08-02. Les fichiers s'y trouvent déjà ailleurs dans V2 (en particulier dans `03_Resources_Geordi/` et `24_PARA_Enterprise/01_Projects_Picard/`). Ce qui fait la **valeur propre** de ce seau, ce sont les couches qui n'existent pas ailleurs : la racine A3_Data_Archives_Spec, l'inventaire `_V3_STRUCTURE_2026-08-02/README.md` (qui **révèle** la nature du snapshot), le **TEMPORAL-CANON** de Fable Banque (constantes de temps de la banque), l'**ADR-L2-AAAS-001** (AaaS doctrine 3 variants × 4 leviers Solarpunk), et la **B1/B2/B3 Business Pulse doctrine** (Computer_B1_B2_B3_Business_Pulse_Doctrine.md) — qui étend la doctrine vue par Picard.

J'ai donc priorisé : **la racine du seau**, **les manifestes des 6 couches** (00/10/20/30/40/60), **les 6 specs A2** (Computer / Curie / Discovery / Holo Janeway / Holo Deck / Orville), **les 2 specs A1** (Beth / Morty), **l'ADR INDEX**, **le SYMPHONY_BUS/SCHEMA**, **le TEMPORAL-CANON**, **le ROADMAP_DEAL_12WY**, **le Computer_B1_B2_B3_Business_Pulse_Doctrine**, et **le AaaS doctrine** (ADR-L2-AAAS-001 + canon B3 Notion). Le reste est parcouru en listing pour confirmer l'inventaire.

## Vue d'ensemble — ce que contient le seau

```
04_Archives_Data/
├── README.md                                    — racine, mission Data A3
├── A3_Data_Archives_Spec.md                     — racine, spec identité Data
├── 03_OpenClaw_Body_Legacy/                     — 1 fichier dans le filtre (AGENTS.md/CLAUDE.md)
│                                                  Le dossier contient en fait ~70 fichiers réels
│                                                  (config openclaw, sessions, sqlite) — non
│                                                  comptés ici car leur nom ne porte pas INDEX/SPEC/etc.
├── Legacy_LifeOS_App_Specs_2026-05-22/          — 15 fichiers (snapshot du 2026-05-22, pré-AaaS)
│   ├── TOTAL_Spec/{ADR,DDD,PRD}/                — 7 fichiers structurels visibles
│   └── _SPECS/                                  — vide côté filtre (autres formats)
└── _V3_STRUCTURE_2026-08-02/                    — 1 516 fichiers : SNAPSHOT de V3
    ├── README.md                                — explique la nature de l'archive
    ├── _root_and_shells_2026-08-02/             — racine V3 originelle + DOCTRINE-ORCHESTRATION
    ├── 00_Amadeus/                              — identité A0 + Memory Core + Symphony bus (120)
    │   ├── README.md, Manifesto.md
    │   ├── ROADMAP_DEAL_12WY_2026-2027.md       — roadmap 4 cycles × 12WY
    │   ├── a0_reasoning_map.md, Life_Reality_map.md, Reality_map.md
    │   ├── INTEGRATION_CEOBENCH_SPECLOOP.md
    │   ├── 30_MEMORY_CORE/                      — Memory Core canon (42 fichiers structurels)
    │   ├── 40_SYMPHONY_BUS/SCHEMA.md            — bus sémantique d'état canon
    │   ├── 05_OSS_Twin/, 05_OSS_TSTwin/         — twin runtime canon (symphony specs)
    │   ├── 01_Identity_Core/, 02_Bio_Metrics/, 04_Digital_Memory/, sob/
    ├── 10_Tech_OS/                              — L0 Bedrock Rick (54 fichiers)
    │   ├── README.md, Manifesto.md
    │   ├── 00_Governance_Rick/                  — 33 fichiers (kernel + watchdog)
    │   ├── 11_Infra_13th_Doctor/, 12_Interface_11th_Doctor/,
    │   │  13_Data_12th_Doctor/                  — 3 Doctors Who
    │   └── 12_Blueprints/                       — 2 fichiers (SDD canon)
    ├── 20_Life_OS/                              — L1 The Fleet (752 fichiers)
    │   ├── README.md, Manifesto.md
    │   ├── 00_Gatekeepers_Beth_Morty/           — A1 Beth + Morty specs
    │   ├── 21_Ikigai_Orville/                   — Ikigai 4 Pillars + 5 Horizons (Ed/Kelly/...)
    │   ├── 22_Wheel_Discovery/                  — 8 LDxx + ZORA
    │   ├── 23_12WY_SNW/                         — 12 Week Year + 5 disciples
    │   ├── 24_PARA_Enterprise/                  — 653 fichiers (le gros du seau)
    │   │   ├── 01_Projects_Picard/              — projets Picard (Summer's Verse etc.)
    │   │   ├── 02_Areas_Spock/                  — Areas Spock
    │   │   ├── 03_Resources_Geordi/             — KB Geordi (pilar source vivante)
    │   │   ├── 04_Archives_Data/                — imbrication : ce même seau, vu depuis V3
    │   │   ├── A2_Computer_Enterprise_Spec.md   — A2 ship spec canon
    │   │   ├── A3_Enterprise_References_Index.md
    │   │   ├── Computer_B1_B2_B3_Business_Pulse_Doctrine.md
    │   │   └── Business_Pulse_B3_Notion_Canon_Lore_Index.md
    │   ├── 25_GTD_Cerritos/                     — Holo Deck + 5 GTD stages
    │   ├── 26_DEAL_Protostar/                   — Holo Janeway + 4 DEAL stages
    │   └── 27_Cognition_LD04/                   — Tilly LD04 (Cognition)
    ├── 30_Business_OS/                          — L2 The Fractal Engine (510 fichiers)
    │   ├── README.md, Manifesto.md
    │   ├── 00_Jerry_Business_Pulse/             — 404 fichiers, Jerry Macro + 8 Domaines
    │   │   ├── 01-08_<Domain>_<Manager>_<Squad>/
    │   │   └── 09_Blueprints/{01-SDD,02-ADR,03-PRD,04-DDD}
    │   ├── 00_Summers_Verse/                    — Summer Micro + B1/B2/B3 état SQL
    │   └── 10_Projects/                         — 102 fichiers, projets B1/B2/B3
    │       ├── omk/, solaris/, abc/, alikaly/, rilcot/, marina/, ceo-desktop/
    │       └── omk-nexus-coaching-premium/
    ├── 40_Fable_Banque/                         — TEMPORAL-CANON + wargames (13 fichiers)
    │   ├── TEMPORAL-CANON.md                    — constantes de temps canoniques
    │   ├── wargames/                            — 17-, 19-, 21-, 27-… (move-by-move sims)
    │   └── fable-last-week-aspace/
    ├── 50_Claude_Code_Config/                   — skills/rules/agents/hooks (16 fichiers)
    │   ├── agents/seo-specialist.md
    │   ├── hooks/README.md
    │   ├── skills/{skill-creator, ecc/brand-voice}/references/
    ├── 60_Citadel/                              — Moteur WF0 Spock (12 fichiers)
    │   ├── README.md                            — Citadelle A0 P0 dashboard
    │   └── loops/ARCHITECTURE.md                — canon queue > loop
    └── _SPECS/                                  — 36 fichiers
        ├── ADR/INDEX.md                         — INDEX 35 ADR canoniques
        ├── ADR/{L0_Kernel_OS, L1_Life_OS, L2_Business_OS}/  — 33 ADR
        ├── REGISTRY/supabase_schemas.md
        ├── PRD/PRD-PORTFOLIO-B1-FRANCHISE_index.md
        └── MCP/supabase-aspace-spec.md, mcp-supabase-aspace-v0.1/
```

**Synthèse** : ce seau est **essentiellement une archive photographique de V3**. La valeur propre à ce seau est triple : (1) le **README racine du snapshot** qui révèle la nature de l'archive et les **11 fichiers de secrets** publiés (à traiter) ; (2) la **racine A3_Data_Archives_Spec.md** qui pose l'identité de Data comme "A3 Archives + chef d'orchestre DEAL" ; (3) la **couche Business Pulse B1/B2/B3 + AaaS Doctrine** qui enrichit ce que Picard n'a pas couvert (SOB, AAAS 3 variants, etc.).

---

## 1 · Système de codes — relevé

### L0 / L1 / L2 / L3 — couches du A'Space Kernel

**Source canonique** : `00_Amadeus/README.md`, `20_Life_OS/README.md`, `30_Business_OS/README.md`, `10_Tech_OS/README.md`.

| Code | Couche | Gardien | Rôle |
|---|---|---|---|
| **L0** | Bedrock (Tech OS) | Rick (A1) | Infra, Sovereignty, anti-fragilité |
| **L1** | Life OS (The Fleet) | Beth + Morty (A1) | Holistic management, 6 ships |
| **L2** | Business Pulse (Fractal Engine) | Jerry + Summer (A1) | Macro/Micro fractal, 8 domaines |

> **Source verbatim** : `20_Life_OS/README.md` §"The Law of Balance" : *"**Layer 1 of the A'Space Kernel v2.0**."* ; `30_Business_OS/README.md` §"The Fractal Engine" : *"**Layer 2 of the A'Space Kernel v2.0**. This is the factory."* ; `10_Tech_OS/README.md` : *"**Layer 0 of the A'Space Kernel v2.0**. This is the machine room."*

### A0 / A1 / A2 / A3 — cascade agentique

| Code | Rôle | Exemples canoniques |
|---|---|---|
| **A0** | Jumeau Numérique Amadeus (méta-coach, vision H30) | A0 Amadeus |
| **A1** | Gatekeeper (vision 3 ans) | Rick, Beth, Morty, Sommerfield, Jerry, Summer |
| **A2** | Ingénieur / Framework Ship | Computer, Curie, Discovery, Holo Janeway, Holo Deck, Orville |
| **A3** | Méta-Orchestrateur (vision 1-10 semaines) | Picard, Spock, Geordi, Data, Dal, Rok-Tahk, Zero, Gwyn, Mariner, Boimler, Rutherford, Tendi, Freeman, Pike, Una, M'Benga, Chapel, Ortegas, Ed, Kelly, Gordon, Claire, Isaac, Lamarr, Bortus, Alara, Klyden, Book, Saru, Culber, Tilly, Stamets, Burnham, Reno, Georgiou |

> **Source verbatim** : `_root_and_shells_2026-08-02/ASpace_OS_V3-DOCTRINE-ORCHESTRATION.md` §1 : *"A0 — Jumeau Numérique Amadeus (méta-coach, vision H30, Gouverneur ON-not-IN E-Myth) … ├── A1 Gatekeepers (SOBER anti-paperclip, vision 3 ans, 2-3 membres) … ├── A2 Ingénieurs (vision 10 ans, ~6 membres) … ├── A3 Méta-Orchestrateurs (vision 1-10 semaines, ~35-100+ membres, fractal)."*

### B0 / B1 / B2 / B3 — couche Business (L2)

> **Source** : `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §"Self-Operating Business Layer" : *"Jerry J01 now carries `B0_Self_Operating_Business_Doctrine/` as the macro layer above B1/B2/B3."*

| Code | Couche | Défini dans |
|---|---|---|
| **B0** | Self-Operating Business (macro) | `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §"Self-Operating Business Layer" — *macro layer above B1/B2/B3* |
| **B1** | Direction Cockpit (North Star, 1Y/3Y/10Y) | `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §"B1 Direction Cockpit" — *every Summer project and the Jerry Area must hold direction as separate artifacts* |
| **B2** | Business Domain (8 domaines) | Même fichier §"B2 Gate Matrix" — *Every Summer's Verse project must carry a `B2_DOMAIN_GATE_MATRIX.md`* |
| **B3** | Warp Core Execution (squads) | Même fichier §"B3 Squad Swarm Configurations" |

### LD01 → LD08 — 8 Life Wheel Domains

> **Source** : `22_Wheel_Discovery/A2_Discovery_ZORA_Spec.md` §"Crew" et `22_Wheel_Discovery/README.md` §"Doctrine verrouillée (8 Life Wheel Domains)"

| Code | Domaine | A3 | Horizon canon (verrouillé §18.2 plan fancy-hugging-bengio) |
|---|---|---|---|
| LD01 | Career & Business | Book | **H1** (weekly P&L) |
| LD02 | Finance & Independence | Saru | **H3** (quarterly runway) |
| LD03 | Health, Sleep, Energy | Hugh Culber | **H10** (10-week cycle) — HARD SAFETY |
| LD04 | Mind, Cognition | Sylvia Tilly | **H30** (30-day learning) — HARD SAFETY |
| LD05 | Relations & Social | Paul Stamets | H30 (network half-life) |
| LD06 | Love, Family, Presence | Michael Burnham | H10 (family cycle) |
| LD07 | Creativity, Leisure | Jett Reno | H10 (MVP build arc) |
| LD08 | Contribution, Impact | Philippa Georgiou | H90 (quarterly legacy) |

### H1 / H3 / H10 / H30 / H90 — 5 Horizons

> **Source** : `21_Ikigai_Orville/README.md` §"Doctrine verrouillée (4 Pillars + 5 Horizons)" — *"Isaac H1 / Lamarr H3 / Bortus H10 / Alara H30 / Klyden H90"*

### W1 → W12 (12WY), W13 (13e semaine)

> **Source** : `23_12WY_SNW/README.md` §"Cycle 12WY Q3 2026 (06/15 → 09/07)" — *W1 (06/15-07/05), W2 (07/06-07/26), W3 (07/27-08/16), W4 (08/17-09/07), W5+ = 09/14 W13 / 09/21 W0 Cycle 4*

Format canon Picard : `Q[N]_[YYYY]_W[N]` (vu dans `Cerritos_Plane_Onboarding/MANIFEST.md` du seau Picard).
Format canon Curie : `cycle: Q3-2026, week: W1`.

### G1 → G8 (Picard) vs 01 → 08 (Jerry)

⚠️ **Deux numérotations cohabitent** (cf. §4 contradictions) :

- **G1 → G8** : canon Picard (vu dans Picard seau). Mapping Growth(Superman/Guardians), Sales(Martian Manhunter/Illuminati), Product(Flash/Avengers), Ops(Batman/F4), IT(Cyborg/KangDynasty), Finance(WonderWoman/Thunderbolts), People(GreenLantern/XMen), Legal(Aquaman/Eternals).
- **01 → 08** : canon Jerry Business Pulse (`30_Business_OS/00_Jerry_Business_Pulse/04_Business_Domains/`). Mêmes 8 domaines, même ordre (01_Growth_Superman_Guardians → 08_Legal_Aquaman_Eternals) — **sauf** que Jerry omet Sales (présent en `02_Sales_MartianManhunter_Illuminati/`), donc 8 dossiers numérotés en pratique.
- **00_Amadeus/README.md** §"Layer 2: Business Pulse" n'en numérote que **7** (01_People → 07_Legal), omettant Sales.

### WF / WK01-13 / W# (Citadel loops)

> **Source** : `60_Citadel/loops/ARCHITECTURE.md` §6 : *"`WF` = strates d'orchestration · `WK01-13` = semaines 12WY. `W#` nu = interdit."*

Loops canoniques : `wf0-spock · wf1-morty · wf2-book · wf3-mirofish · w-star`. Données partagées dans `artifacts/{signals, tasks, tickets, docs}/`.

### ADR — codes des Architecture Decision Records

> **Source** : `_SPECS/ADR/INDEX.md` — 35 ADR canoniques en 3 strates (L0=8 + L1=11 + L2=14 = 33 + 2 radiés REG-001, OPS-002).

Préfixes observés : `ADR-META-00X` (Life OS doctrine), `ADR-RICK-001`, `ADR-LLM-001`, `ADR-INFRA-00X`, `ADR-OMK-00X`, `ADR-ABCOS-00X`, `ADR-SUPABASE-001`, `ADR-CANON-001`, `ADR-MEM-00X`, `ADR-OBSERVABILITY-001`, `ADR-CONSENSUS-002`, `ADR-AGENT-BOUNDARY-001`, `ADR-SECURITY-001`, `ADR-SOBER-002`, `ADR-L2-AAAS-001`, `ADR-L2-MESH-001`, `ADR-AGENTIC-001`, `ADR-HERMES-001`, `ADR-INFRA-MCP-001`, `ADR-MEMO-000`, `ADR-Meta-000` (casse mixte), `ADR-WSL-001` (legacy), `ADR-ALA-001` (legacy).

⚠️ **ADR-LLM-001** marqué "fable-5-discontinuation-decision" — signale que **Fable-5 a été discontinué** (cf. aussi ADR-REG-001 et ADR-OPS-002 radiés le 2026-06-15, dépendaient de Mistral).

### ADR en attente (gap L0 → L1 Life OS)

> **Source** : `20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Morty_Spec.md` §"Alignement Plan fancy-hugging-bengio" : *"5 ADRs Life OS framework manquants : gap L0 à fermer avant Item 11 du cycle Q3 2026 (avant 2026-09-07) — **ADR-DEAL-001, ADR-GTD-001, ADR-PARA-001, ADR-LIFE-WHEEL-001, ADR-SYMPHONY-001**."*

### D0 → D8 — doctrine numérique (ADR-META-001)

> **Source** : cité dans plusieurs ADRs : D1 (verify-before-assert), D3 (no-self-contradiction), D4 (no-hard-delete / append-only), D6 (root cause / Glob deep timeout), D7 (cost-of-escalation), D8 (cross-agent).

### Cycle format

> `Q[N]-YYYY` (ex: `Q3-2026`) et `Q[N]_[YYYY]_W[N]` (ex: `Q3_2026_W3`).

### Kardashev Type 1/2/3/4

> **Source** : `_root_and_shells_2026-08-02/ASpace_OS_V3-DOCTRINE-ORCHESTRATION.md` §1 *"Kardashev types"* : *"A3/B3 = Type 1 (technicien opérationnel, 4h-semaine, délégation idempotente) ; A2 = Type 2 (Manager E-Myth, framework-impersonating) ; A1 = Type 3 (Gatekeeper Solarpunk, sovereignty + sobriété) ; A0 = Type 4 (Visionnaire méta, tue les paperclips Ultron non utiles)."*

### SOB — Self-Operating Business

> **Source** : `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §"Self-Operating Business Layer" — artefacts canoniques : `00_SOB_INDEX.md, 01_E_MYTH_FRANCHISE_PROTOTYPE.md, 02_BUILT_TO_SELL_SCORECARD.md, 03_WHO_NOT_HOW_DELEGATION_MATRIX.md, 04_OFFER_AND_BRAND_ENGINE.md, 05_PROJECT_GRADUATION_GATES.md`.

### AaaS 3 Variants (Solaris / Nexus OMK / Orbiter ABC / Family/Home dormant)

> **Source** : `_SPECS/ADR/L2_Business_OS/ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md` (statut ACCEPTED 2026-06-21, A0 batch ratification).

| Variant | A3 Captain | LDxx primaire | Statut Q3 2026 |
|---|---|---|---|
| **Solaris AaaS** | Book (LD01) + Saru (LD02) | LD01+LD02+LD04+LD07 | 🟢 ACTIF |
| **Nexus OMK AaaS** | Saru (LD02) | LD02+LD06+LD04 | � ACTIF (Zéro Bug Sprint livré 2026-06-20) |
| **Orbiter ABC AaaS** | Burnham (LD06) | LD06+LD05+LD08 | 🟢 ACTIF (17 tables abc_os 2026-06-17) |
| **Family/Home AaaS** | TBD (Jerry_4 dormant) | LD03+LD04+LD05+LD07+LD08 | 🟡 DORMANT Q3 2026 |

### 4 Leviers Solarpunk

> **Source** : ADR-L2-AAAS-001 §C1 / D4 — *"(1) Janine Benyus biomimétisme ; (2) Idriss Aberkane low-high-tech ; (3) Meta Science acceleration ; (4) circular & blue economy."*

### D11 bandwidth metric

> **Source** : `26_DEAL_Protostar/A2_HoloJaneway_Protostar_Spec.md` §"Alignement Plan" — *"D11 bandwidth metric = output Gwyn : gain bande passante cognitive (minutes libérées/semaine) vs maintenance tax (minutes upkeep/semaine)."*

### 50/30/20 rule (cadence hebdomadaire)

> **Source** : `23_12WY_SNW/README.md` §"Cycle 12WY Q3 2026" — *"les 5 disciples SNW structurent la cadence hebdo (50/30/20 rule)"*

### MUSE / DEAL 4 stages (D/E/A/L)

> **Source** : `26_DEAL_Protostar/A2_HoloJaneway_Protostar_Spec.md` §"Doctrine canon DEAL 4 stages" — *D (Dal/Define) → E (Rok-Tahk/Eliminate) → A (Zero/Automate) → L (Gwyn/Liberate) → retest (Karpathy loop)*.

### Kardashev types (cf. aussi 1.13)

### 12WY 5 disciplines

> **Source** : `23_12WY_SNW/README.md` §"Crew Map" — *Pike (Vision) / Una (Planning) / M'Benga (Focus) / Chapel (Metrics) / Ortegas (Execution)*.

### Ikigai 4 Pillars + 5 Horizons

> **Source** : `21_Ikigai_Orville/README.md` — *Ed Mercer (Profession/craft, Pillar 1) / Kelly Grayson (Mission, Pillar 2) / Gordon Malloy (Passion, Pillar 3) / Claire Finn (Vocation, Pillar 4)* + 5 horizons (Isaac H1 / Lamarr H3 / Bortus H10 / Alara H30 / Klyden H90).

### Picard G1-G8 vs Jerry 01-08

Voir §4 contradictions.

---

## 2 · Types d'objets — relevé

Liste triable : chaque type est nommé au moins à 3 endroits dans le seau, avec attributs et chemins.

### Type : `A2 Ship Spec`

**Définition** : spec canonique d'un Framework Ship L1 (A2). Frontmatter OKF : `id`, `layer: L1_Life_OS`, `role: A2_Framework_Ship`, `framework`, `shadow_tool`, `gatekeepers`, `status: SHADOW_ACTIVE`, `created: 2026-05-20`. Sections canon : Identity, Responsibilities, Inputs, Outputs (YAML), Crew, A3 Findings Contract, Evidence Index, Acceptance Criteria, Context7 Boundary, Alignement Plan fancy-hugging-bengio.

**Attributs observés** : id, layer, role, framework, shadow_tool, gatekeepers.{beth, morty}, status, created, ship, a2, crew (5 noms), outputs.stages[].

**Chemins** :
- `…/20_Life_OS/24_PARA_Enterprise/A2_Computer_Enterprise_Spec.md` (A2 Computer / Enterprise, PARA)
- `…/20_Life_OS/23_12WY_SNW/A2_Curie_SNW_Spec.md` (A2 Curie / SNW, 12WY)
- `…/20_Life_OS/22_Wheel_Discovery/A2_Discovery_ZORA_Spec.md` (A2 Discovery / ZORA, Life Wheel)
- `…/20_Life_OS/26_DEAL_Protostar/A2_HoloJaneway_Protostar_Spec.md` (A2 Holo Janeway / Protostar, DEAL)
- `…/20_Life_OS/25_GTD_Cerritos/A2_HoloDeck_Cerritos_Spec.md` (A2 Holo Deck / Cerritos, GTD)
- `…/20_Life_OS/21_Ikigai_Orville/A2_Orville_Spec.md` (A2 Orville, Ikigai)

### Type : `A3 Crew Spec`

**Définition** : spec d'un officier A3 (jumeau). Apparaît comme fichiers `A3_<Name>_<Role>_Spec.md`.

**Attributs observés** : id, name, role, ship (parent A2), responsibility, output_canon.

**Chemins** :
- `…/26_DEAL_Protostar/01_Definition_Dal/A3_Dal_Definition_Spec.md`
- `…/26_DEAL_Protostar/02_Elimination_RokTahk/A3_RokTahk_Elimination_Spec.md`
- `…/26_DEAL_Protostar/03_Automation_Zero/A3_Zero_Automation_Spec.md`
- `…/26_DEAL_Protostar/04_Liberation_Gwyn/A3_Gwyn_Liberation_Spec.md`
- `…/23_12WY_SNW/01_Vision_Pike/02_Planning_Una/…`
- `…/25_GTD_Cerritos/01_Inbox_Mariner/02_Clarify_Boimler/03_Organize_Rutherford/04_Review_Tendi/05_Engage_Freeman/`
- `…/21_Ikigai_Orville/01_Pillars_Identity/02_Horizons_Time/`
- `…/22_Wheel_Discovery/LD01_Business_Book/…LD08_Impact_Georgiou/`

### Type : `A1 Gatekeeper Spec`

**Définition** : spec d'un A1 (Beth, Morty, Rick, Sommerfield). Frontmatter : `layer: L1_Life_OS`, `role: Gatekeeper / …`, `status: SHADOW_ACTIVE`, `created: 2026-05-20`.

**Attributs** : role (Conscience / Terminal Executor / Architect / Limites), decision_states (5 chez Beth : GREEN/ORANGE/RED/HALT_LD03/HALT_LD04), routing_matrix (Morty), anti_patterns[].

**Chemins** :
- `…/20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Beth_Spec.md`
- `…/20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Morty_Spec.md`

### Type : `AaaS Variant`

**Définition** : pattern A'Space où chaque projet business majeur est incarné par un variant Jerry B1 Fractal autonome. Défini par l'ADR-L2-AAAS-001.

**Attributs** : a3_captain, ldxx[], b2_primary[], b3_lead, horizon (H90/H3/H10/TBD), objectif_canonique, statut_q3_2026.

**Chemins** :
- `_SPECS/ADR/L2_Business_OS/ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md` (canonique)
- `_SPECS/ADR/L2_Business_OS/ADR-AAAS-ACQUISITION-DOCTRINE-001_aaas-acquisition-doctrine.md`
- `_SPECS/ADR/L2_Business_OS/ADR-AAAS-CONTENT-CANON-001_aaas-content-canon.md` (et 5 autres AAAS-*)
- `30_Business_OS/10_Projects/ceo-desktop/_doctrine/B2_Business_Domains/00_AAAS_DOMAIN_DEVELOPMENT_MAP.md`
- `30_Business_OS/10_Projects/{solaris, omk, abc, omk-nexus-coaching-premium}/` (instances)

### Type : `ADR (Architectural Decision Record)`

**Définition** : décision architecturale datée, numérotée, signée. Frontmatter canon : `id`, `title`, `type: ADR`, `status`, `date`, `deciders[]`, `drafted_by`, `domain`, `tags[]`, `doctrine_anchors[]`, `related[]`, `provenance`.

**Attributs** : id, status (PROPOSED/ACCEPTED/RATIFIED/RADIÉ/DRAFT), date, doctrine_anchors[], supersedes_scope, sign_off_a0.

**Chemins** : 33 ADR canoniques dans `_SPECS/ADR/{L0_Kernel_OS, L1_Life_OS, L2_Business_OS}/` (cf. INDEX.md).

### Type : `B1 Direction Cockpit`

**Définition** : série de 7 artefacts obligatoires pour B1 (cf. `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §"B1 Direction Cockpit").

**Attributs** : nom_de_fichier (00..06), rôle (cockpit index / North Star / 12WY cycles / decision charter / handoff queue / DoD spec / JTBD spec).

**Chemins canoniques** : `00_B1_DIRECTION_INDEX.md`, `01_NORTH_STAR_1Y_3Y_10Y.md`, `02_12WY_COMMAND_CYCLES.md`, `03_DECISION_CHARTER.md`, `04_B2_HANDOFF_QUEUE.md`, `05_B2_DEFINITION_OF_DONE_SPEC.md`, `06_B3_JOBS_TO_BE_DONE_SPEC.md`.

**Présence observée** : chunk_018/019 de `30_Business_OS/00_Jerry_Business_Pulse/graphify-burst/chunks/` contiennent 00_B1_DIRECTION_INDEX, 03_DECISION_CHARTER, 05_B2_DEFINITION_OF_DONE_SPEC, 06_B3_JOBS_TO_BE_DONE_SPEC.

### Type : `B2 Domain Control Room`

**Définition** : 3 artefacts obligatoires pour chaque B2 (cf. `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §"B2 Swarm Supervision Rooms").

**Attributs** : nom_de_fichier (00/01/02), contenu canonique.

**Chemins canoniques** : `00_B2_DOMAIN_CONTROL_ROOM.md`, `01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md`, `02_B3_SWARM_SUPERVISION_PROTOCOL.md`.

### Type : `B3 Squad Swarm Config`

**Définition** : 4 artefacts obligatoires pour chaque B3 squad (cf. `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §"B3 Squad Swarm Configurations").

**Attributs** : nom_de_fichier (00..03).

**Chemins canoniques** : `00_B3_SWARM_CONFIG.md`, `01_B3_AGENT_ROSTER.md`, `02_PEER_UNBLOCKING_AND_HANDOFFS.md`, `03_SHARED_CONTEXT_AND_PROOF_LOG.md`.

### Type : `Squad (B3)`

**Définition** : équipe B3 Marvel/DC canonique associée à un B2 domain. 8 squads canoniques (cf. `30_Business_OS/Manifesto.md`).

**Attributs** : squad_name (Guardians / Illuminati / Avengers / Fantastic4 / KangDynasty / Thunderbolts / XMen / Eternals), b2_domain (LDxx mapping), b2_owner (Manager), lead (1er membre), members[] (5-7), task_surface[], build_gates[], anti_patterns[], escalation_rule.

**Chemins** : `Business_Pulse_B3_Notion_Canon_Lore_Index.md` (canonique) ; `30_Business_OS/00_Jerry_Business_Pulse/04_Business_Domains/0X_<Domain>_<Manager>_<Squad>/` ; `30_Business_OS/10_Projects/ceo-desktop/_doctrine/B3_Warp_Core_Execution/` (instance).

### Type : `B2 Domain`

**Définition** : un des 8 domaines Business (Growth, Sales, Product, Ops, IT, Finance, People, Legal).

**Attributs** : manager_archetype (DC), squad_name (Marvel/Illuminati), lead (1er membre), book_linked (LDxx Life Wheel mapping), build_gates_order (8 obligatoires).

**Chemins** : `30_Business_OS/00_Jerry_Business_Pulse/04_Business_Domains/0X_<Domain>_<Manager>_<Squad>/` (Jerry canon 8 domaines, dont Sales).

### Type : `Loop (Citadel)`

**Définition** : unité d'orchestration agentique (file d'attente typée sur trigger). 5 loops canoniques + w-star (cf. `60_Citadel/loops/ARCHITECTURE.md`).

**Attributs** : loop_id (wf0-spock, wf1-morty, wf2-book, wf3-mirofish, w-star), contract_path (`domains/<loop>/README.md`), artifacts_io, cadence, enable_flag.

**Chemins** : `60_Citadel/loops/`, `60_Citadel/decisions/enable_<loop>.flag`, `60_Citadel/logs/worklog.md`.

### Type : `Manifesto`

**Définition** : manifeste de couche (L0/L1/L2/L3) ou de sous-couche. Fichier `Manifesto.md` avec sections courtes.

**Attributs** : guardian, scope, doctrine, access.

**Chemins** :
- `00_Amadeus/Manifesto.md` (Layer 0 : Amadeus, Guardian: A0)
- `10_Tech_OS/Manifesto.md` (Layer 0 : Tech OS, Guardian: Rick)
- `20_Life_OS/Manifesto.md` (Layer 1 : Life OS, Guardian: Beth & Morty)
- `30_Business_OS/Manifesto.md` (Layer 2 : Business OS, Guardian: Jerry)

### Type : `README.md (Handoff)`

**Définition** : README handoff A2/A3 (parent d'un dossier de ship). Sections canon : Layer, A2, Framework, Shadow tool, Gatekeepers, Status, Mission, Resume Protocol, A2 Spec, Crew Map, A3 Rule, Outputs, Handoff Rules, Evidence, Context7 Boundary, Alignement Plan fancy-hugging-bengio.

**Attributs** : layer, a2_ship, framework, shadow_tool, gatekeepers, status, mission, crew_map.

**Chemins** : `24_PARA_Enterprise/README.md`, `23_12WY_SNW/README.md`, `22_Wheel_Discovery/README.md`, `21_Ikigai_Orville/README.md`, `25_GTD_Cerritos/README.md`, `26_DEAL_Protostar/README.md` (6 README handoff A2-ship identiques en structure).

### Type : `Spec.md (A2/A3)`

**Définition** : spec technique avec frontmatter OKF. Distinct de README.md (qui est handoff).

**Attributs** : id, layer, role, framework, shadow_tool, gatekeepers, status, created, identity, responsibilities, inputs, outputs (YAML), crew, a3_findings_contract, evidence_index, acceptance_criteria, context7_boundary.

**Chemins** : tous les `A2_*.md`, `A3_*.md`.

### Type : `Wargame (Move)`

**Définition** : simulation move-by-move sur papier. Numéro wargame + M (move). Source canon = TEMPORAL-CANON § "Loi anti-fossile (wargame 27 M4)".

**Attributs** : wargame_id, move_id, claim, d1_receipt, abort_condition, red_team_pass, self_grade.

**Chemins** : `40_Fable_Banque/wargames/17-manifest-dispatch-a2-a3-lifeos.md`, `…/19-delegation-chaine-cc-m3-standard-fable.md`, `…/21-fable-mode-standard-agnostique.md`.

### Type : `Constante TEMPORAL-CANON`

**Définition** : entrée du tableau canonique `40_Fable_Banque/TEMPORAL-CANON.md`. Règle de préséance : "en cas de conflit prose-wargame vs ce CANON, le CANON gagne" (TC preamble).

**Attributs** : nom (GO, compression CAP, cadence, banque, Fable, RAM airlock, tokens plan), valeur, receipt (wargame_id + move_id).

**Chemins** : `40_Fable_Banque/TEMPORAL-CANON.md` (unique, canon SSOT des constantes de temps).

### Type : `Symphony Spec`

**Définition** : spec d'adaptateur Symphony (canal tool → A2 ship). Naming canon : `symphony-<tool>.spec.md`.

**Attributs** : tool (obsidian/affine/baserow/plane/airtable/notion/clickup/supabase/sheets), shadow_lane (A/B), index_ref.

**Chemins** :
- `00_Amadeus/05_OSS_Twin/symphony/L1/lane_B_runtime/01_routing/symphony-{obsidian, affine, baserow, plane}.spec.md`
- `…/L2/symphony-{airtable, clickup, notion, sheets, supabase}.spec.md`

### Type : `Context Pack`

**Définition** : enveloppe d'instruction validée par Beth, routée par Morty vers un A2 ship. Schéma canon : `required_context_pack_fields: [ship, crew_member, next_action, framework, domain_impact, l0_skill_required, beth_clearance, evidence_paths, output_artifact]` (cf. A1_Morty_Spec.md).

**Attributs** : ship, crew_member, next_action, framework, domain_impact, l0_skill_required, beth_clearance, evidence_paths, output_artifact.

**Chemins** : concept cité dans 6 A2 specs + A1_Morty_Spec.md + 40_SYMPHONY_BUS/SCHEMA.md (state.json `next_step`).

### Type : `Manifest (de projet/domaine)`

**Définition** : `MANIFEST.md` au sens du Brief Picard + canon INFRA-003 amendé (Picard). Défini par `30_Business_OS/10_Projects/<proj>/_doctrine/_manifest/` (vu dans instances).

**Attributs** : id, layer, role, parent_a2, classification, status, created, next_owner.

**Chemins** : `02 ABC OS & Child Care BOS/SUMMERS_VERSE_MANIFEST.md` (Picard seau) ; équivalent canonique pour projets du 10_Projects/.

### Type : `state.json (bus sémantique)`

**Définition** : SSOT bus entre agents A0→A1→A2→A3. Schéma canon dans `00_Amadeus/40_SYMPHONY_BUS/SCHEMA.md` (v1).

**Attributs** : $schema (state-bus.v1), status, created, updated, agent_id, session_id, cycle, week, stage, agent_path, para_bucket, 12wy_discipline, life_wheel_domain, raw_input_hash, raw_input_preview, next_step, tokens_used, tokens_budget, drift_flag, extra, metadata.

**Chemins** : `00_Amadeus/40_SYMPHONY_BUS/state.json` (+ .prev, .lock, state_writer.py).

### Type : `Loop contract`

**Définition** : fichier `domains/<loop>/README.md` (cf. ARCHITECTURE.md).

**Attributs** : loop_id, contract_scope, worklog_format, enable_flag_path.

**Chemins** : `60_Citadel/loops/domains/{wf0-spock, wf1-morty, wf2-book, wf3-mirofish, w-star}/README.md`.

### Type : `Artifact signal/task/ticket/doc`

**Définition** : 4 sous-types d'artifacts partagés entre loops (cf. ARCHITECTURE.md §3).

**Attributs signal** : slug (file `signals/<slug>.md`), OKF frontmatter, append-only des occurrences.

**Attributs task** : item pioché sur trigger, avec preuve (exit/path) obligatoire.

**Chemins** : `60_Citadel/loops/artifacts/{signals, tasks, tickets, docs}/`.

### Type : `Build Gate`

**Définition** : règle vérifiable qui autorise ou interdit promotion d'un item B2/B3 (cf. `Business_Pulse_B3_Notion_Canon_Lore_Index.md`, ex : "Win rate > 25% sur SQL", "MTTR < 30 min P0", "Release frequency >= 1 ship / 2 semaines Solaris").

**Attributs** : name, threshold, scope (B2/B3), measurement_source.

**Chemins** : cités dans B3 Notion lore index pour 8 squads.

### Type : `Doctrine Anchor`

**Définition** : référence croisée entre ADRs. Champ frontmatter `doctrine_anchors: [ADR-META-001, …]`. Cf. ADR-INDEX §"Doctrine ancrage".

**Attributs** : anchor_id (ADR-id référencé), anchor_kind (mandatory/sister/implicit).

**Chemins** : 29 ADR avec `doctrine_anchors` field (cf. ADR-INDEX D1 receipts).

### Type : `Hard-stop trigger`

**Définition** : condition qui force ARRÊT (anti-paperclip). Cité dans `ADR-SOBER-002` "Anti-Paperclip Maximizer Doctrine anti-Musk + 7 hard-stop triggers" (cf. ADR-INDEX L0 table).

**Attributs** : trigger_id, condition, response_action, owner (A1 Rick veto kernel structurel).

### Type : `Schema Supabase (multitenant)`

**Définition** : schéma Postgres pour produit AaaS. Naming : kebab-case en snake_case (`abc-os` → `abc_os`). Préfixes produits : `omk_*`, `solaris_*`, `abc_*`.

**Attributs** : tenant, hosting (Cloud/self-host), ADR_ratification, statut, tables_count, rls (oui/non).

**Chemins** : `_SPECS/REGISTRY/supabase_schemas.md` (canonique unique).

### Type : `Squad (Ikigai/12WY/DEAL/GTD)`

Sous-types distincts du type `Squad (B3)` :

- **Ikigai Pillars (4)** : Ed Mercer (Profession), Kelly Grayson (Mission), Gordon Malloy (Passion), Claire Finn (Vocation).
- **Ikigai Horizons (5)** : Isaac (H1), Lamarr (H3), Bortus (H10), Alara (H30), Klyden (H90).
- **12WY Disciples (5)** : Pike (Vision), Una (Planning), M'Benga (Focus), Chapel (Metrics), Ortegas (Execution).
- **DEAL Muse (4)** : Dal (Define), Rok-Tahk (Eliminate), Zero (Automate), Gwyn (Liberate).
- **GTD 5 Stages** : Mariner (Capture), Boimler (Clarify), Rutherford (Organize), Tendi (Review), Freeman (Engage).
- **Life Wheel 8 LDxx** : Book/Saru/Culber/Tilly/Stamets/Burnham/Reno/Georgiou.

**Chemins** : 6 specs A2 + Business_Pulse_B3_Notion_Canon_Lore_Index.md.

### Type : `Schema SQL (Master)`

**Définition** : canon SQL pour Summer's Verse state.

**Chemins** : `30_Business_OS/00_Summers_Verse/state/SCHEMA.md` ; `30_Business_OS/00_Jerry_Business_Pulse/graphify-burst/chunks/chunk_018/03_Phase3_Master_SQL_Schema.md`.

### Type : `Reference Index (A3)`

**Définition** : index canonique des preuves/references d'un A3.

**Attributs** : claim, evidence_path, lines/note.

**Chemins** :
- `24_PARA_Enterprise/A3_Enterprise_References_Index.md`
- `26_DEAL_Protostar/A3_Protostar_References_Index.md`
- `25_GTD_Cerritos/A3_Cerritos_References_Index.md`
- `23_12WY_SNW/A3_SNW_References_Index.md`
- `22_Wheel_Discovery/A3_Discovery_References_Index.md`
- `20_Life_OS/24_PARA_Enterprise/Business_Pulse_B3_Notion_Canon_Lore_Index.md`
- `20_Life_OS/24_PARA_Enterprise/Business_Pulse_B3_Swarm_Inspiration_Index.md`

### Type : `Spec legacy (V0.3.5 / TOTAL_Spec)`

**Définition** : spec d'avant la canonisation 2026-06-21 (snapshot `Legacy_LifeOS_App_Specs_2026-05-22/`).

**Attributs** : version (V0.3.5), status (PROPOSED), date (2026-03-16 typiquement).

**Chemins** : `Legacy_LifeOS_App_Specs_2026-05-22/TOTAL_Spec/{ADR, DDD, PRD}/` — 7 fichiers structurels visibles.

---

## 3 · Relations — relevé verbatim

Chaque relation est une phrase du fichier, citée intégralement, avec son chemin.

### R1 — A3 Data "supervise" Holo-Janeway A2 DEAL

> **Verbatim** : *"Data libère A1 Beth de la supervision opérationnelle de Protostar"* — `A3_Data_Archives_Spec.md` §"D3 nuance critique" ligne 64.

### R2 — A3 Data = A3 Archives (PAS un 5ème A2 ship)

> **Verbatim** : *"Data reste A3 Archives (PAS un 5ème A2 ship). Sa position "chef d'orchestre DEAL" vient de l'imbrication DEAL ⊂ PARA (Data = sentinelle des 4 lettres qui supervise aussi le 4ème quadrant Muse Libération)."* — `20_Life_OS/24_PARA_Enterprise/A2_Computer_Enterprise_Spec.md` §"Crew canon (plan §3.2 — D3 nuance)" lignes 100-110.

### R3 — DEAL ⊂ PARA ⊂ 12WY (imbrication poupée russe)

> **Verbatim** : *"**Loi d'imbrication** (plan §3.1) : DEAL ⊂ PARA ⊂ 12WY. Computer compile les findings de ses 4 A3 (Picard/Spock/Geordi/Data) mais ne touche PAS directement DEAL — Data fait l'interface opérationnelle."* — `…/24_PARA_Enterprise/A2_Computer_Enterprise_Spec.md` §"Computer (A2) = imbrication verticale triptyque MORTY" lignes 90-98.

### R4 — A1 Morty "route vers" 6 A2 ships selon routing matrix

> **Verbatim** : *"Routing distribué sur 6 ships : Morty route vers les 6 A2 engines selon la matrice de routage canon (`fancy-hugging-bengio.md §3.6`)."* — `20_Life_OS/00_Gatekeepers_Beth_Morty/A1_Morty_Spec.md` §"Alignement Plan" ligne 115.

### R5 — A1 Beth "supervise" 6 A2 ships + veto distribué

> **Verbatim** : *"Veto distribué sur 6 ships : Beth supervise les 6 A2 engines (Orville + Discovery + SNW + Enterprise + Cerritos + Protostar). Le plan §3.5 simplifie Beth = "Ikigai+Life Wheel+DEAL" comme **responsabilité principale**, pas comme exclusivité."* — `…/A1_Beth_Spec.md` §"Alignement Plan" ligne 100.

### R6 — Picard = A3 Projects (PAS A2 Computer)

> **Verbatim** : *"Computer aboard USS Enterprise is the A2 manager of durable structure. … Picard is not the A2; Picard is the A3 owner of Projects inside the PARA crew."* — `20_Life_OS/24_PARA_Enterprise/A2_Computer_Enterprise_Spec.md` §"Identity" ligne 18.

### R7 — Data (A3 Archives) → A2 Computer Enterprise

> **Verbatim** : *"Data owns `04_ARCHIVES`, completed projects or paused domains outside the active visual field."* — `…/24_PARA_Enterprise/A3_Enterprise_References_Index.md` §"Canonical Crew" ligne 15.

### R8 — Cerritos 5 stages canon : Mariner/Boimler/Rutherford/Tendi/Freeman

> **Verbatim** : *"A1 Morty Focus → A2 USS Cerritos → A3 5 Airlock (Mariner/Boimler/Rutherford/Tendi/Freeman)"* — `20_Life_OS/25_GTD_Cerritos/README.md` §"Alignement Plan fancy-hugging-bengio" ligne 70.

### R9 — SNW 5 disciples canon : Pike/Una/M'Benga/Chapel/Ortegas

> **Verbatim** : *"5 disciples canon OK : Pike/Una/M'Benga/Chapel/Ortegas"* — `…/23_12WY_SNW/A2_Curie_SNW_Spec.md` §"D1 receipts" ligne 130.

### R10 — DEAL 4 stages canon : Dal/Rok-Tahk/Zero/Gwyn

> **Verbatim** : *"Dal (Definition) — Pattern detection and recurrence counting aboard USS Protostar (A2 Holo Janeway). Rok-Tahk (Elimination) — Permission to delete and NO-GO proposals aboard USS Protostar (A2 Holo Janeway). Zero (Automation) — Skill creation and sub-agent deployment aboard USS Protostar (A2 Holo Janeway). Gwyn (Liberation) — Bandwidth tracking, D11 metrics, and A0 cognitive load measurement."* — `…/26_DEAL_Protostar/A2_HoloJaneway_Protostar_Spec.md` §"Anchor canon (plan §25.3, verbatim vérifiés)" lignes 106-111.

### R11 — Ikigai 4 Pillars + 5 Horizons canon (9 A3 crew)

> **Verbatim** : *"9 A3 crew (4 pillars + 5 horizons) = conforme plan §3.2 + §18."* — `20_Life_OS/21_Ikigai_Orville/README.md` §"D4 self-contradiction fermée" ligne 99.

### R12 — Orville "ne crée JAMAIS de Rocks" (sign-off Morty)

> **Verbatim** : *"Orville = **meaning engine**, pas execution engine. Ne crée JAMAIS de Rocks directement (handoff à SNW/Curie)."* — `…/21_Ikigai_Orville/README.md` §"D4 self-contradiction fermée" ligne 100.

### R13 — Discovery "mesure et diagnostique" — ne fait pas de tactiques

> **Verbatim** : *"Discovery measures and diagnoses; it does not execute tactics."* — `…/22_Wheel_Discovery/README.md` §"Handoff Rules" ligne 50.

### R14 — Picard/Spock : B2 Area (Areas) vs B2 Domain (Projects)

> **Verbatim** : *"Jerry → Spock (Areas) ; Summer → Picard (Projects)"* — `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §"PARA Placement" ligne 17-19.

### R15 — Saru 1000T = Kardashev Type 3 (anti-Musk paperclip)

> **Verbatim** : *"**L'objectif canonique Saru 1000T** (A3 LD02 Finance, AaaS Solaris + Nexus) est donc **production de valeur réelle Kardashev Type 3**, pas valorisation financiarisée découplée Musk-style."* — `_SPECS/ADR/L2_Business_OS/ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md` §"C4 — Le contexte civilisationnel" ligne 62.

### R16 — Solaris AaaS → Life-OS-2026 Initiative ALPHA V1.0 LIVE

> **Verbatim** : *"🟢 **ACTIF** — Life-OS-2026 Initiative ALPHA V1.0 LIVE sur https://life-os-2026-liart.vercel.app/"* — `…/ADR-L2-AAAS-001…md` §"D2 — Mapping 3 AaaS Variants × A3 Captain × LDxx Life Wheel" ligne 78.

### R17 — Nexus OMK AaaS → omk-services/00-omk-saas-os (Zéro Bug Sprint dcc1235)

> **Verbatim** : *"🟢 **ACTIF** — Sprint Zéro Bug `dcc1235` ✅ livré + déployé SHA `8ad94d1` (2026-06-20). 9 `omk_saas.*` tables + JWT hook `e47f4aa1`."* — `…/ADR-L2-AAAS-001…md` §"D2" ligne 79.

### R18 — Orbiter ABC AaaS → abc_os schema (17 tables 2026-06-17)

> **Verbatim** : *"🟢 **ACTIF (récent)** — Schema `abc_os` migré 2026-06-17. `PGRST_DB_SCHEMAS` env var = P0 blocker en cours résolution."* — `…/ADR-L2-AAAS-001…md` §"D2" ligne 80.

### R19 — Cycle 12WY Q3 2026 (06/15 → 09/07) = 12 items canoniques

> **Verbatim** : *"**Cycle 12WY Q3 2026** : 12 items canoniques A0 verbatim, tous routés via A2 Curie SNW (5 disciplines) → A1 Morty (Focus Gatekeeper) → B1/B2/B3 (Solarpunk/OMK/ABC swarms)."* — `…/23_12WY_SNW/README.md` §"Total" ligne 90.

### R20 — B3 squad "doit être pair-collaborative" (B2 intervient seulement sur exceptions)

> **Verbatim** : *"B3 swarms collaborate as peers. A blocked B3 should first ask one member of the same squad to challenge the blocker and propose a workaround. B2 intervenes only when the DoD is ambiguous, the input does not exist, a cross-domain gate is touched, acceptance risk changes, or delegated authority is exceeded."* — `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §"B3 Squad Swarm Configurations" ligne 86.

### R21 — "B2 = conductor, not babysitter"

> **Verbatim** : *"B2 is a conductor, not a babysitter. It translates B1 vision into bounded goals, guardrails, and proof requirements."* — `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §"B2 Swarm Supervision Rooms" ligne 72.

### R22 — B1 doit exister avant B2 (gate séquence)

> **Verbatim** : *"B1 must exist as a direction cockpit before B2 can responsibly define domain Rocks."* — `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §"Non-Negotiables" ligne 40.

### R23 — B2 Domain Gate Matrix = ordre canonique 1..8 (Product → People)

> **Verbatim** : *"Required gate order: 1. Product proves user value. 2. Ops proves repeatable delivery. 3. IT proves runtime, access, deployment, and backup boundaries. 4. Finance proves cost, price, and margin logic. 5. Legal proves claims, privacy, IP, and terms boundaries. 6. Sales proves qualification, objections, and handoff. 7. Growth proves ICP, message, channel, and measurement. 8. People proves ownership, training, handoff, and load."* — `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §"B2 Gate Matrix" lignes 47-61.

### R24 — `SOB (B0)` est macro au-dessus de B1/B2/B3 (SOB = Self-Operating Business)

> **Verbatim** : *"Jerry J01 now carries `B0_Self_Operating_Business_Doctrine/` as the macro layer above B1/B2/B3. This layer translates E-Myth Revisited, Built to Sell, Who Not How, Million Dollar Weekend, 100M Offers, and Billion Dollar Brand Club into local operating gates, without adopting any external tool as a dependency."* — `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §"Self-Operating Business Layer" ligne 147.

### R25 — `state.json` = SSOT bus entre agents (verrou atomique)

> **Verbatim** : *"Lock atomique : `state_writer.py` retry 3× (backoff 100/300/900ms) si `.state.lock` existe. Garde-fou : `state.json > 10 KB` → rotation `state.json.prev`."* — `00_Amadeus/40_SYMPHONY_BUS/SCHEMA.md` §"Loi lock atomique (D6 risk)" ligne 48.

### R26 — Citadel loop = QUEUE d'items typés (jamais boucle qui tourne pour tourner)

> **Verbatim** : *"**Loi** : le travail agentique est une QUEUE d'items typés piochés sur trigger — jamais une boucle qui tourne pour tourner."* — `60_Citadel/loops/ARCHITECTURE.md` §"Loi" ligne 4.

### R27 — Loop discipline : append-only worklog, preuves obligatoires

> **Verbatim** : *"Une loop doit : (a) lire son contrat `domains/<loop>/README.md`, (b) les **10 dernières lignes** de `logs/worklog.md`, (c) les signals non-traités qui matchent ses triggers. … Écriture SANS preuve = interdit (l'item retourne en queue tag `unverified`)."* — `60_Citadel/loops/ARCHITECTURE.md` §"Conventions" lignes 22-23.

### R28 — TEMPORAL-CANON prime sur prose-wargame

> **Verbatim** : *"**Règle de préséance** : en cas de conflit prose-wargame vs ce CANON, le CANON gagne — la prose d'un wargame est un fossile daté (vrai à l'écriture, non-normatif ensuite)."* — `40_Fable_Banque/TEMPORAL-CANON.md` preamble ligne 3.

### R29 — ROADMAP DEAL 4 cycles × 12WY (2026-07 → 2027-07) — North Star $1B ARR

> **Verbatim** : *"**North Star H10** : $1B ARR — OMK BOS Nexus · ICP Coach premium · Produit AaaS de SOB à 1 000 $/mois par instance."* — `00_Amadeus/ROADMAP_DEAL_12WY_2026-2027.md` §"North Star H10" ligne 3.

### R30 — ROADMAP cadence métabolique : descend puis remonte

> **Verbatim** : *"PICARD (A3) 1 vision/cycle → décompose le cycle en 3 Rocks ; SUMMERS (B1) 1 Rock/mois → traduit le Rock en directives par domaine ; 8 B2 · 3T 4 Sprints/mois → chaque manager tient le sprint de son domaine ; B3 SQUADS 5 Daily Scrums/sprint → exécution, receipts SQL ; UPLINK 5 scrums → 1 sprint review → 4 sprints → 1 Rock review → 3 Rocks → 1 cycle review Picard → 4 cycles → bilan annuel."* — `…/ROADMAP_DEAL_12WY…md` §"La cadence" ligne 57.

### R31 — A0 Amadeus = méta-coach, Gouverneur ON-not-IN (E-Myth)

> **Verbatim** : *"A0 = Vision H30, gouvernance ON-not-IN (E-Myth). A0 ne **fait pas** le travail A1/A2/A3 — A0 **trace la route, rate les décisions, dérive les sub-agents, et surveille que le paperclip Ultron ne pousse pas**."* — `_root_and_shells_2026-08-02/ASpace_OS_V3-DOCTRINE-ORCHESTRATION.md` §5 ligne 100.

### R32 — Anti-paperclip doctrine = 3 couches

> **Verbatim** : *"Trois couches d'anti-paperclip (le stack canon, D1 receipts) : 1. **superpowers (A2)** : documente et idempotentise les freelances (A2 Manager E-Myth ne laisse jamais un A3 créer un skill opaque ; tout skill a un README, des tests, un behavior contrat). 2. **GSD (A3/B3)** : orchestration visionnaire Type 1 — chaque task a un **Definition of Done** + un **gate de sortie vérifiable** (tests passent, diff < 300 lignes, etc.). 3. **Fable + Wargames + CEO-Bench (qualité)** : validation move-by-move **avant** tout déploiement. Le **budget d'entropie ≥30%** (D6) garantit l'anti-collapse (jamais rêver sur ses propres rêves)."* — `…/ASpace_OS_V3-DOCTRINE-ORCHESTRATION.md` §3 ligne 72.

### R33 — Asymétrie corrigibilité : kill-switches autonomes pour ARRÊTER, humain-gated pour SE LEVER

> **Verbatim** : *"**Asymétrie corrigibilité** (W28) : les kill-switches sont **autonomes pour ARRÊTER** (B1-Mirofish gate) mais **humain-gated pour SE LEVER** (M5 Remote Pane / Telegram). Un off-switch auto-release = le paperclip Ultron."* — `…/ASpace_OS_V3-DOCTRINE-ORCHESTRATION.md` §3 ligne 80.

### R34 — Citadel = "anti-Ultron" doctrine (lecture seule, dormants affichés dormants)

> **Verbatim** : *"**Lecture seule par défaut** : `serve.py` lit UNIQUEMENT `data/*.json` (sortie des collectors). Aucune mutation des sources canoniques (settings.json, mcp.json, skills/, ADR/, etc.). **Écriture bornée** : `collectors/*.py` écrivent UNIQUEMENT `data/*.json` (overwrite idempotent). `decisions/*.json` append-only (Gate #2 à venir). **Dormants affichés dormants** : Paperclip AI + Multica = `status: "dormant"`, jamais réveillés."* — `60_Citadel/README.md` §"Doctrine anti-Ultron" ligne 49.

### R35 — Picard = A3 Projects, Spock = A3 Areas, Geordi = A3 Resources, Data = A3 Archives

> **Verbatim** : *"Computer is A2, not Picard; Picard is A3 Projects. … Picard checks active Projects and Rock linkage. Spock checks Areas, standards, and ongoing responsibilities. Geordi checks reusable Resources and context-pack value. Data checks archive readiness and documentation-before-archive."* — `…/24_PARA_Enterprise/A2_Computer_Enterprise_Spec.md` §"A3 Findings Contract" lignes 60-66.

### R36 — Geordi = Resources = KB racine unique (D-2026-08-01-#1)

> **Verbatim** : *"Geordi est la racine unique de la KB — décision `D-2026-08-01-#1`."* — `_V3_STRUCTURE_2026-08-02/README.md` §"La source vivante" ligne 62.

### R37 — DEAL dossier imbriqué dans PARA (Data sentinelle)

> **Verbatim** : *"**DEAL ⊂ PARA** : A3 Data (Archives PARA) supervise Holo-Janeway A2 DEAL (Dal/Rok-Tahk/Zero/Gwyn). Data libère A1 Beth de la supervision opérationnelle de Protostar (plan §3.1)."* — `…/24_PARA_Enterprise/README.md` §"Triptyque MORTY (plan §3.5) — ancrage 4 lettres PARA" ligne 78.

### R38 — Picard/Spock mapping AaaS variantes

> **Verbatim** : *"Chaque projet AaaS ancre dans `30_Business_OS/10_Projects/<proj>/` (CEO Dashboard Matryoshka, `ADR-INFRA-003`) avec structure `_doctrine/` (junction deep Picard Verse) + 8 sous-dossiers alignés sur les 8 Domaines."* — `…/ADR-L2-AAAS-001…md` §"D3 — Les 8 Domaines Business × LD01" ligne 86.

### R39 — Saru 1000T = anti-paperclip guard (3 garde-fous)

> **Verbatim** : *"**Anti-paperclip Saru 1000T** (plan §18.3 + §22.4) : 3 garde-fous canon — (1) Boundary Saru spec : "coordinates with Book but does not override LD01 strategy" ; (2) AREA_STANDARD P1 Work ON not IN — scarcity seule ne déclenche pas B1 review ; (3) Musk pivot = agency over utopia — Saru DOIT évaluer si l'intention augmente agency A0 vs attend salvation externe."* — `20_Life_OS/22_Wheel_Discovery/A2_Discovery_ZORA_Spec.md` §"Alignement Plan" ligne 78.

### R40 — D11 bandwidth metric = output Gwyn (DEAL Muse Libération)

> **Verbatim** : *"**D11 bandwidth metric = output Gwyn** : gain bande passante cognitive (minutes libérées/semaine) vs maintenance tax (minutes upkeep/semaine). Upkeep > gain → route back to Zero/Rok-Tahk."* — `20_Life_OS/26_DEAL_Protostar/README.md` §"Karpathy loop appliqué D→E→A→L" ligne 101.

### R41 — Picard 12WY Q3 mapping A3 disciples

> **Verbatim** : *"Pike (Vision) → Item 2; Una (Planning) → Items 1-2; M'Benga (Focus) → Items 3-4; Chapel (Metrics) → Items 5-7; Ortegas (Execution) → Items 8-10."* — `20_Life_OS/23_12WY_SNW/README.md` §"Matrice 5 disciples × 5 horizons" lignes 72-76.

### R42 — Cerritos stage canon vs fancy-hugging-bengio §15.1 (D3 nuance)

> **Verbatim** : *"`fancy-hugging-bengio.md §15.1` identifie **Tendi = Organize** (canon twin protostar). Le terrain canon local garde **Rutherford = Organize** (résolu 2026-05-20, canon actif)."* — `20_Life_OS/25_GTD_Cerritos/README.md` §"Matrice canon 5 stages × 5 A3 twins" ligne 74.

### R43 — Cerritos = "bus horizontal" qui boucle 2 triptyques vers B1 Fractal

> **Verbatim** : *"GTD (Cerritos Holodeck) = bus horizontal qui boucle les 2 triptyques (MORTY 12WY⊃PARA⊃DEAL + BETH Ikigai⊃Life Wheel⊃Muse) vers B1 Fractal."* — `20_Life_OS/25_GTD_Cerritos/A2_HoloDeck_Cerritos_Spec.md` §"Anchor canon" ligne 87.

### R44 — Morty → Cerritos routing A0 intentions

> **Verbatim** : *"intentions A0 `Capture idée brute` (→ Mariner `/aside`), `Clarifier` (→ Boimler `/plan`), `Today focus` (→ SNW Ortegas `/plan`) routing canon A0 → A1 Morty → A2 Cerritos."* — `…/25_GTD_Cerritos/A2_HoloDeck_Cerritos_Spec.md` §"Anchor canon" ligne 88.

### R45 — Picard/Spock/Geordi/Data canon mapping (Picard NOT A2)

> **Verbatim** : *"Picard owns `01_PROJECTS`, and each project should connect to a Rock in Baserow. Spock owns `02_AREAS`, mapped to Life Wheel domains and durable standards. Geordi owns `03_RESOURCES`, the reusable knowledge base feeding Graham/RAG. Data owns `04_ARCHIVES`, completed projects or paused domains outside the active visual field."* — `…/24_PARA_Enterprise/A3_Enterprise_References_Index.md` §"Evidence" lignes 24-27.

### R46 — "A3 owns execution only" (B3 non-negotiable)

> **Verbatim** : *"B3 owns execution only. B3 does NOT: Rewrite strategy, Redefine vision, Alter B2 Rock definitions, Escalate without first logging Lead/Lag evidence."* — Picard seau, `01_Projects_Picard/02 ABC OS & Child Care BOS/SUMMERS_VERSE_MANIFEST.md` (citation reprise verbatim).

### R47 — Supabase hosting pivot 2026-06-19 (Cloud ≠ self-host)

> **Verbatim** : *"**Hosting pivot 2026-06-19** : OMK Services Org (Cloud) + ABC-OS-COMMUNITY Org (Cloud) sont les nouvelles instances prod (per `ADR-OMK-004` + `ADR-ABCOS-002`). Self-host VPS `148.230.92.235` archivé fonctionnellement mais pas encore radié (D4 no-hard-delete)."* — `_SPECS/REGISTRY/supabase_schemas.md` §"Hosting pivot" ligne 11.

### R48 — Data archive-and-document reflex (avant archive final)

> **Verbatim** : *"Data never performs final archival without `archive-and-document`."* — `A3_Data_Archives_Spec.md` §"Boundaries" ligne 43.

### R49 — Data ne détruit pas par défaut (destructive delete = A0 approval)

> **Verbatim** : *"Data does not delete by default. … Data flags destructive deletion as requiring explicit A0 approval."* — `A3_Data_Archives_Spec.md` §"Boundaries" + "Identity" lignes 44-46.

### R50 — Picard/Spock Areas vs Projects (mapping Picard = Projects, Spock = Areas)

> **Verbatim** : *"Picard owns `01_PROJECTS`, and each project should connect to a Rock in Baserow. Spock owns `02_AREAS`, mapped to Life Wheel domains and durable standards."* — `…/24_PARA_Enterprise/A3_Enterprise_References_Index.md` §"Evidence" lignes 24-25.

---

## 4 · Contradictions — relevé (sans trancher)

> **Méthode** : deux fichiers qui décrivent la même chose autrement. Je signale, je ne tranche pas.

### C1 — Picard/Spock G2 Sales : "John Jones" vs "Martian Manhunter"

- **Source A (canon Picard 02 ABC OS)** : `02 ABC OS & Child Care BOS/B2_Business_Domains/README.md` (vu via Picard seau) — *"G2 | Sales | Martian Manhunter | Illuminati | $100M Offers (Hormozi)"*.
- **Source B (canon 30_Business_OS README)** : `…/30_Business_OS/README.md` §"Domains (01-08)" — *"08_Sales (John Jones) … Squad: **Illuminati**"*.
- **Source C (canon B3 Notion lore index)** : `…/Business_Pulse_B3_Notion_Canon_Lore_Index.md` — *"Sales - Illuminati … B2 owner: John Jones / Martian Manhunter … Lead: Black Bolt"*.
- **Source D (canon 30_Business_OS/00_Jerry_Business_Pulse/04_Business_Domains/)** : `02_Sales_MartianManhunter_Illuminati/` — nomme le dossier `MartianManhunter`.

Le brief Picard lui-même signalait que `SDD-006` listait 7 domaines (manquant Sales) et que le canon à jour en compte 8 (`Sales / Illuminati / John Jones`). Le canon B3 Notion cite **les deux noms** (`John Jones / Martian Manhunter`) comme alias. Lecture : Picard = ancien canon (Martian Manhunter), 30_Business_OS README + AaaS Doctrine = canon corrigé (John Jones). Mais aucune note de supersede explicite.

### C2 — Picard 8 domaines vs Jerry 8 domaines vs 00_Amadeus 7 domaines

- **Picard (G1→G8)** : 8 domaines, G2 Sales = Martian Manhunter / Illuminati.
- **Jerry (01→08)** : 8 dossiers (01_Growth_Superman_Guardians … 08_Legal_Aquaman_Eternals), `02_Sales_MartianManhunter_Illuminati/` existe.
- **00_Amadeus/README.md** : **7** domaines (01_People → 07_Legal) — **omet Sales**.
- **30_Business_OS/README.md** : **8** domaines (01_People → 08_Sales) — inclut Sales/John Jones.

→ Picard et Jerry ont 8 (avec Sales, sous des noms différents) ; 00_Amadeus en a 7 ; 30_Business_OS en a 8 mais avec l'ordre 01_People..08_Sales ≠ 01_Growth..08_Legal de Jerry.

### C3 — Horizons Saru H3 vs lecture rapide Saru H1

- **A2 Discovery Spec** ligne 78 : *"**D3 nuance critique** (plan §18.2) : Saru = **H3**, Book = **H1**. PAS Saru=H1, Book=H10 comme une lecture rapide pourrait le suggérer."*
- Picard/Picard-derived canon antérieur pourrait avoir inversé.

### C4 — Tendi/Rutherford mapping Cerritos (D3 nuance fancy-hugging-bengio)

- **fancy-hugging-bengio §15.1** (plan canon) : Tendi = Organize, Rutherford = Reflect.
- **Canon local actif** (`A2_HoloDeck_Cerritos_Spec.md` + `25_GTD_Cerritos/README.md`) : Rutherford = Organize, Tendi = Review. Cf. `A2_HoloDeck_Cerritos_Spec.md` ligne 90 : *"Cette spec A2 = source de vérité canonique terrain, **prevaut** sur `fancy-hugging-bengio.md §15.1` tant que A0 n'inverse pas explicitement le mapping A3."*

### C5 — Picard 02 ABC OS canon `picard_status: ACTIVE` vs autres en `GRADUATED`

- Vu via Picard seau : *"**Source canonique** : `01_Projects_Picard/02 ABC OS & Child Care BOS/B2_Business_Domains/README.md` (la copie canonique — `picard_status: ACTIVE`, autres en `GRADUATED`)."* (note Picard §G1→G8 table). Pas de détails sur ce que signifie GRADUATED (vs SHADOW_ACTIVE vu ailleurs). À creuser hors-scope de ce brief.

### C6 — "Data chef d'orchestre DEAL" nuance D3

- **Anti-pattern guard** : *"Data n'est PAS un 5ème A2 ship. Data = A3 Archives PARA qui **supervise** Holo-Janeway A2 DEAL via l'imbrication DEAL ⊂ PARA."* (cf. `A2_Computer_Enterprise_Spec.md` ligne 100-110).
- Une lecture rapide pourrait suggérer Data = A2 ship #5. Le canon distingue explicitement.

### C7 — Picard A2 Computer Spec vs Picard "A2 Computer_Enterprise" → confusion Computer/Picard

- Le Brief Picard a relevé que plusieurs fichiers `SUMMERS_VERSE_MANIFEST` utilisent `parent_a2: A2_HoloDeck_Cerritos` (cf. Picard §"Architecture en trois couches B1/B2/B3"). Or canoniquement Computer = A2 Enterprise (PARA), Cerritos = A2 GTD.
- → Indique une **incohérence d'usage** dans les SUMMERS_VERSE_MANIFEST de certains projets : `parent_a2` ne pointe pas toujours vers A2 Computer (PARA parent canonique).

### C8 — "Saru coordonne with Book mais n'override pas LD01 strategy"

- Lu dans `A2_Discovery_ZORA_Spec.md` ligne 78 (Anti-paperclip Saru 1000T garde-fou #1). Cohérent dans le canon. Mais aucun mécanisme opérationnel de **mesure** de l'override n'est défini dans le seau — juste une boundary textuelle.

### C9 — ADR-INDEX table "L2=10" vs canon réel "L2=14"

> **Verbatim** : *"`_SPECS/ADR/INDEX.md` table partiellement stale : L0/L1/L2 counts à jour 2026-06-21 (L2=14 vs INDEX.md table dit 10 = à corriger formellement)."* — `…/INDEX.md` preamble ligne 14.

L'ADR-INDEX lui-même signale la stale-ness. La table Markdown affiche "💼 L2 Business OS (14 ADR)" mais une note dit 10 — contradiction interne.

### C10 — Fable-5 "discontinué" (ADR-LLM-001)

> **Verbatim** : `ADR-LLM-001` intitulé `fable-5-discontinuation-decision.md` (PROPOSED→ACCEPTED 2026-06-15). Fable-5 a été discontinué.
- Pourtant, `30_Business_OS/00_Jerry_Business_Pulse/graphify-burst/chunks/chunk_018/00_SOB_INDEX.md` mentionne SOB Index et `…/how-to-become-an-ai-engineer-fast-2026-ai-engineering-roadmap.md` est un artefact annexe.
- Et `60_Citadel/README.md` §"Méthodologie" cite `LD01/10_methodology/00_fable5_jack_roberts_meta_strategy.md` (Level 3 Jack) comme méthodologie vivante.

→ Tension : Fable-5 discontinué formellement (ADR-LLM-001), mais **méthodologie encore référencée** par Citadelle A0. Lecture : la méthodologie persiste mais la "fable-5" comme entité opérationnelle est arrêtée.

### C11 — Picard B1/B2/B3 vs 30_Business_OS README

- Picard (via SUMMERS_VERSE_MANIFEST) range Spock = Areas (B2 Area Domains), Picard = Projects (B2 Domain).
- `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §"PARA Placement" : *"Jerry → Spock (Areas) ; Summer → Picard (Projects)"* — cohérent.
- Mais le canon B1/B2/B3 doctrine parle aussi de **B2 Area Domains** (pour Jerry) vs **B2 Business Domains** (pour Summer) — deux sous-types.

### C12 — "13e semaine" canon vs "W13" notation

- `ROADMAP_DEAL_12WY_2026-2027.md` : *"12WY-01 Fondations | 20/07 → 11/10/2026 | W13 review | 12-18/10"*. W13 = review meta-cycle.
- `23_12WY_SNW/README.md` : *"W5+ | 09/14 = W13 → 09/21 W0 | Kick-off Cycle 4"*. Ici W13 = semaine suivant les 12.
- `SDD-010` "13e semaine" = semaine de cloture/meta canonique.
- → Deux usages de W13 : (a) W13 dans le cadre d'un cycle 12WY = semaine meta (post-cycle), (b) W13 calendaire = semaine #13 après démarrage. Pas explicitement distingués.

### C13 — Picard SUMMERS_VERSE "12WY 5 disciples" + canon Curie "5 disciples"

- Picard/Picard seau : 12WY 5 disciples = Pike/Una/M'Benga/Chapel/Ortegas.
- Picard `02 ABC OS & Child Care BOS/B1_Summer_Direction/README.md` mentionne "Verify LD03/LD04 exist and are current in J01 Area Standard".
- `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §"B1 Direction Cockpit" liste 7 artefacts (00..06) pour B1, pas 5 — **B1 ≠ 5 disciples (qui est SNW)**.

### C14 — Domain numbering Picard vs Jerry

- Picard G1→G8 : 01_Growth..08_Legal.
- Jerry 01→08 : 01_Growth..08_Legal.
- Picard = G-code, Jerry = numeric prefix. Même ordre (Growth..Legal), mais G-code vs numeric — Picard a adopté un mapping G1..G8 distinct, Jerry utilise directement les digits 01..08.

### C15 — "SOB" macro layer (B0) vs "B1" direction

- `Computer_B1_B2_B3_Business_Pulse_Doctrine.md` §"Self-Operating Business Layer" : *"Jerry J01 now carries `B0_Self_Operating_Business_Doctrine/` as the macro layer above B1/B2/B3."*
- B0 = SOB = E-Myth + Built to Sell + Who Not How + Million Dollar Weekend + 100M Offers + Billion Dollar Brand Club.
- Mais SOB est rangé sous **B0**, pas B1 — incohérence apparente avec Picard/Picard où B1 = direction cockpit.

---

## 5 · Le seau lui-même — particularités

### 5.1 — Nature archive photographique

Ce seau n'est pas un **domaine actif**. C'est une **archive** versée le 2026-08-02. Tous les fichiers dans `_V3_STRUCTURE_2026-08-02/` sont une **copie déplacée** de V3 vers les Archives V2 (cf. `_V3_STRUCTURE_2026-08-02/README.md` §"Pourquoi ici, dans les Archives de V2"). Le **README racine** explique :

> *"La structuration de V3 **est** celle de V2 : le dépôt V3 se définissait comme « V2 déplacé, jamais réécrit », une copie littérale du canon."*

Donc 1 516 fichiers ici sont des **doublons** de fichiers qui existent ailleurs dans V2 (en particulier dans `24_PARA_Enterprise/` et `03_Resources_Geordi/`). Ce qui en fait la valeur : le **README** et le snapshot sont **préservés intacts** pour réversibilité.

### 5.2 — Le MANIFEST.json manquant

Le README racine mentionne : *"**ARCHIVE_MANIFEST.json** — **461 entrées** `src` → `dst`."* — mais ce fichier n'apparaît **pas** dans le filtre (son nom ne porte aucun des tokens structurants — INDEX/ARCHITECTURE/etc.). Le MANIFEST n'est donc pas dans la liste de travail, mais le **contenu des 1 516 fichiers** y est.

### 5.3 — 11 secrets publiés, à traiter

> *"Un scan a relevé **au moins 11 fichiers porteurs de secrets** dans cette archive (clés d'API, jetons). … **ils sont publiés**, notamment via le commit `41c19a5`."* — `_V3_STRUCTURE_2026-08-02/README.md` §"Avertissement de sécurité".

Le déplacement ne les a pas exposés — il les a rendus visibles, et concentrés.

### 5.4 — Jonctions NTFS : 0 dans ce seau

Vérifié : 0 jonction NTFS sous `04_Archives_Data/` (cf. §9). La détection (FILE_ATTRIBUTE_REPARSE_POINT) confirme qu'aucun dossier de ce seau n'est une jonction — la totalité du contenu est **réelle** (pas des doublons via reparse point).

### 5.5 — `03_OpenClaw_Body_Legacy/` n'apparaît qu'à 1 fichier

Ce dossier contient ~70 fichiers réels (openclaw.json, sqlite main.sqlite, sessions jsonl, etc.) mais **seul 1 fichier** correspond à un token structural (probablement AGENTS.md ou CLAUDE.md). Le reste est config/sessions/credentials — **matière active** d'un runtime archivé, pas structure canonique. Cette entrée dans le filtre ne représente pas la totalité du dossier.

### 5.6 — `Legacy_LifeOS_App_Specs_2026-05-22/` (15 fichiers)

Snapshot **antérieur** au grand alignement 2026-06-21 (plan fancy-hugging-bengio). Pré-AaaS. Contient 7 fichiers structurels visibles :
- `TOTAL_Spec/ADR/ADR-ALA-001_ALA_Standard.md` (PROPOSED 2026-03-16)
- `TOTAL_Spec/ADR/ADR-ALA-002_ALA_Implementation_Resiliency.md`
- `TOTAL_Spec/ADR/ADR-FWK-011..019_*_Structure.md` (9 ADRs framework)
- `TOTAL_Spec/ADR/ADR-MEM-001_IndexedDB-Cloisonne-LD01-LD08.md`
- `TOTAL_Spec/ADR/ADR-V0.3.5_DoctrineBeth.md`
- `TOTAL_Spec/ADR/ADR-WSL-001_OpenClaw-WSL2-Architecture.md`
- `TOTAL_Spec/DDD/DDD-V0.3.5_DoctrineBeth.md`
- `TOTAL_Spec/PRD/PRD-V0.3.5_DoctrineBeth.md`

C'est le **V0.3.5** du canon Life OS — **pré-SOB**, **pré-AaaS**, **pré-ADR-L2-AAAS-001**.

---

## 6 · Fichiers lus vs laissés

### Lus au long (~30 fichiers)

- Racine du seau : `README.md`, `A3_Data_Archives_Spec.md`
- Snapshot root : `_V3_STRUCTURE_2026-08-02/README.md`, `_root_and_shells_2026-08-02/README.md`, `…/ASpace_OS_V3-DOCTRINE-ORCHESTRATION.md`
- Manifestes L0/L1/L2 : `00_Amadeus/README.md`, `00_Amadeus/Manifesto.md`, `10_Tech_OS/README.md`, `10_Tech_OS/Manifesto.md`, `20_Life_OS/README.md`, `20_Life_OS/Manifesto.md`, `30_Business_OS/README.md`, `30_Business_OS/Manifesto.md`, `30_Business_OS/00_Jerry_Business_Pulse/CEO_Directives.md`, `60_Citadel/README.md`, `40_Fable_Banque/TEMPORAL-CANON.md`
- 24_PARA_Enterprise : `README.md`, `A2_Computer_Enterprise_Spec.md`, `A3_Enterprise_References_Index.md`, `Computer_B1_B2_B3_Business_Pulse_Doctrine.md`, `Business_Pulse_B3_Notion_Canon_Lore_Index.md`
- 6 specs A2 : `A2_Curie_SNW_Spec.md`, `A2_Discovery_ZORA_Spec.md`, `A2_HoloJaneway_Protostar_Spec.md`, `A2_HoloDeck_Cerritos_Spec.md`, `A2_Orville_Spec.md` (lu via README)
- 6 README handoff A2-ship : `21_Ikigai_Orville/README.md`, `22_Wheel_Discovery/README.md`, `23_12WY_SNW/README.md`, `24_PARA_Enterprise/README.md`, `25_GTD_Cerritos/README.md`, `26_DEAL_Protostar/README.md`
- 2 specs A1 : `A1_Beth_Spec.md`, `A1_Morty_Spec.md`
- Plan canon : `00_Amadeus/ROADMAP_DEAL_12WY_2026-2027.md`
- ADR : `_SPECS/ADR/INDEX.md`, `_SPECS/ADR/L2_Business_OS/ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md` (extrait 100 lignes)
- Bus : `00_Amadeus/40_SYMPHONY_BUS/SCHEMA.md`
- Loop : `60_Citadel/loops/ARCHITECTURE.md`
- Registry : `_SPECS/REGISTRY/supabase_schemas.md`
- Legacy : `Legacy_LifeOS_App_Specs_2026-05-22/TOTAL_Spec/ADR/ADR-ALA-001_ALA_Standard.md`

### Parcourus en listing (méta)

- Arbre complet de `_V3_STRUCTURE_2026-08-02/` : 1516 fichiers
- Listing de `30_Business_OS/00_Jerry_Business_Pulse/04_Business_Domains/` : 8 domaines
- Listing de `30_Business_OS/10_Projects/` : 8 projets (abc, alikaly, ceo-desktop, marina, omk, omk-nexus-coaching-premium, rilcot, solaris)
- Listing de `Legacy_LifeOS_App_Specs_2026-05-22/` : 15 fichiers
- Listing de `03_OpenClaw_Body_Legacy/` : ~70 fichiers réels (mais 1 seul dans le filtre)

### Laissés

- **~1 400 fichiers** non lus : principalement contenu feuille (notes, guides, content) ; artefacts graphify-burst (chunks de Jerry) ; `03_OpenClaw_Body_Legacy` config/sessions/sqlite ; `50_Claude_Code_Config` skills/règles ; `60_Citadel/loops/domains/*` contrats de loops spécifiques.

### Pourquoi tant de laissés

Ce seau est une **archive photographique**. Les fichiers canoniques sont **lus** (racines, manifestes, specs A1/A2, ADR, bus). Le reste (96 % des 1534) est contenu feuille déjà dupliqué ailleurs dans V2. Les cartographier **ici** serait dupliquer ce que les autres seaux (Picard pour projets, Geordi pour KB) cartographient déjà.

---

## 7 · Notes méthodologiques

- Le brief signalait **176 jonctions NTFS** au total ; ce seau en a **0** sur 3 924 dossiers scannés. Les jonctions sont concentrées ailleurs.
- Le brief signalait **84 121 .md** au total ; ce seau en a **1 534** (tous `.md`).
- Le volume total mesuré du seau : ~20 Mo (estimation basée sur la liste de chemins ; pas mesuré au disque).
- Aucun agent délégué n'a été invoqué. Toutes les lectures et la rédaction ont été faites localement.
- Format `MEMORY.md` indexé ailleurs — non applicable ici (ce n'est pas un travail de mémoire).

---

## 8 · Synthèse en deux phrases

**04_Archives_Data** est l'**A3 Archives** du canon PARA (Data = A3 twins, USS Enterprise = A2 ship). Le seau dans V2 contient : (1) la **racine A3_Data_Archives_Spec** qui pose l'identité de Data + chef d'orchestre DEAL ; (2) un **snapshot photographique** de V3 versé le 2026-08-02 (1 516 fichiers, 461 entrées ARCHIVE_MANIFEST.json non lues, 11 secrets à traiter) ; (3) un **snapshot antérieur** `Legacy_LifeOS_App_Specs_2026-05-22/` (15 fichiers, V0.3.5 pré-AaaS). Ce que ce seau **ajoute au canon** que Picard n'a pas vu : la **B1/B2/B3 Business Pulse doctrine** (Computer_B1_B2_B3_Business_Pulse_Doctrine.md), l'**AaaS 3 variants doctrine** (ADR-L2-AAAS-001), le **SOB Self-Operating Business** (B0 macro), le **DEAL Muse Libération 4HWW** (D11 bandwidth metric), le **Citadel WF0 loop engine** (queue > loop), et le **TEMPORAL-CANON** (constantes de temps Fable Banque).

**Le seau est muet sur les questions qu'il ne pose pas** : il ne dit pas quelle version des Squads Marvel est canonique (Picard/Martian Manhunter vs 30_Business_OS/John Jones — contradiction C1) ; il ne tranche pas le statut de Sales dans le comptage des 8 domaines (00_Amadeus en omet, contradiction C2) ; il archive un canon **daté** (2026-08-02) qui a probablement évolué depuis — le snapshot est photographique, pas vivant.

---

*Cartographie rédigée le 2026-08-13, en parallèle des cartographies Picard / Spock / Geordi (3 autres seaux).*
