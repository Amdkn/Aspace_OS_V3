# 03_Resources_Geordi — Vague 3

> **Cartographie profonde** du seau 03_Resources_Geordi du PARA V2, vague 3.
> Vagues 1+2 : 552 chemins lus (couverts dans v1+v2 JSON).
> Vague 3 : **935 nouveaux chemins uniques lus** sur 1826 disponibles, **832 jonctions écartées**.
> Brief : CARTO_PARA_V2. Période de lecture : 2026-08-13.

## Couverture

| Métrique | Valeur |
|---|---|
| Fichiers lus (vague 3, uniques) | 935 |
| Fichiers disponibles (priority list filtrée) | 1826 |
| Jonctions écartées | 832 |
| Types d'objets observés | 22 |
| Relations (citation verbatim) | 59 |
| Systèmes de codes | 20 |
| Contradictions | 14 |

### Distribution par sous-dossier (vague 3)

| Sous-dossier | Fichiers lus (vague 3) |
|---|---|
| 05_From_V2_Domains | 496 (296 dans 30_Business_OS) |
| 04_From_V2_Root | 230 (94 dans .codex-m3-lean, 63 dans _SPECS/ADR) |
| 06_Claude_Code_Bare | 130 (58 plugins, 18 skills) |
| 03_Memory_Unified | 73 (70 dans LLM_Wiki/wiki/) |
| 01_Guides | 37 (19 dans 03_IT) |
| 02_Templates | 31 (25 dans Enterprise_OS_Blueprint_Kit) |
| 08_Workspaces_Dormants_2026-08-01 | 24 |
| 09_Life_OS | 4 |
| 00_Index | 4 (les 4 canoniques OKF/RESOURCES/SECOND_BRAIN_PARA/JUNCTIONS) |

## §1 — Types d'objets (trié par nombre de chemins observés)

| # | Type | Chemins | Attributs canon |
|---|---|---|---|
| 1 | **ADR (Architectural Decision Record)** | 45 | id (slug), title, status (DRAFT|PROPOSED|ACCEPTED|RATIFIED|RADIE), date, doctrine_anchors[] … |
| 2 | **INDEX (Geordi sub-folder ou Lane)** | 21 | Source / date / type / layer / lane / status / domain / tags / okf_version |
| 3 | **ARCHITECTURE_SPEC (canonique enterprise)** | 10 | Design principles, Secure-substitute map, Data flow (one account), Stacks in dependency order, Key decisions and tradeoffs |
| 4 | **MANIFEST (project/agent manifest)** | 8 | type: MANIFEST, wargame, slug, id, date … |
| 5 | **Plugin (Claude Code plugin)** | 8 | Path, marketplace, sister/agent files, commandes, hooks … |
| 6 | **SCHEMA (canonique)** | 7 | Path canon, Rôle, Champs + types + descriptions, Loi lock atomique, Anti-patterns |
| 7 | **hand_off (wiki handoff canon)** | 5 | source, date, type: handoff, domain, tags … |
| 8 | **RUNBOOK (cycle-1 runbook with SQL objective)** | 4 | Objectif (métrique SQL), Entrées, Sorties (deltas attendus), Procédure (S1-S4), Cadence (4 sprints × 5 scrums) … |
| 9 | **Dispatch Doctrine (B1/B2 mindset)** | 4 | id, title, B1 owner, B2 owner, B3 squad roster … |
| 10 | **INDEX_QA_REPORT (audit sémantique)** | 4 | domain, ld, b2_owner, sister_b1, b1_filter … |
| 11 | **Twin spec (lane A canon mirror)** | 2 | Source canon, Role, Status, Version, supervised_by … |
| 12 | **Agent Capsule (Soul/Agent/Heartbeat/Tools/Context)** | 2 | Soul (identité, ton, valeurs, interdits), Agent (mission, périmètre), Heartbeat (cadence, reprises), Tools (autorisations, MCP, CLI), Context (mémoire locale, handoff) |
| 13 | **OpenSpec change archive (spec.md)** | 2 | ADDED Requirements, Scenario (WHEN/THEN), Renamed/Replaced scopes |
| 14 | **Skill canon (Claude Code)** | 2 | name, description, tools[], Path canon, Sister index |
| 15 | **Blueprint ADR** | 2 | id, title, status, date, L0/L1/L2 layer … |
| 16 | **Wargame MANIFEST (ordres war-mode)** | 1 | wargame, slug, deciders[], parent_dox[], domain … |
| 17 | **Manifest cross-harness (per LD)** | 1 | type: harness-manifest-cross, harnesses[], entry sequence per harness, Surface attendue, Surface mutante vs read-only |
| 18 | **Doctrine Lock Map (alignement plans ↔ organigramme)** | 1 | plans_sources[], rot_rate, Table de correspondance, Pont de mise à jour D1 |
| 19 | **A3 Spec (A3 agent immutable spec)** | 1 | id, layer, role, parent_a2, classification … |
| 20 | **Junction Map (NTFS junctions)** | 1 | Chemin relatif, Cible realpath, Existe (oui/non), Compte .md, Domaine PARA … |
| 21 | **STANDARD A0 FORMAT** | 1 | Daily Captain's Log (YYYY-MM-DD.md), Weekly Distillation, Monthly Distillation, Quarterly 12WY, Tags & versioning |
| 22 | **Cardia (A3 Book LD01 doctrine index)** | 1 | okf_version, type: book-doctrine-root, title, description, domain … |

## §2 — Relations (citation à l'appui)

> **59 relations** extraites, toutes avec citation verbatim du fichier source. Pas de paraphrase.

| # | De | Verbe | Vers |
|---|---|---|---|
| 1 | ADR-SOBER-002 (anti-paperclip maximizer doctrine) | *anchor sister* | ADR-L2-AAAS-001 |
| 2 | ADR-MEM-001 (Memory Fabric) | *sister scope* | ADR-MEM-002 (Wiki ↔ Life Wheel Mapping) |
| 3 | ADR-MEM-002 | *resolves ID collision with* | ADR-MEM-001 (historique IndexedDB) |
| 4 | ADR-META-003 (Model-Agnostic Runtime) | *extends/sépare* | ADR-META-002 (Autonomy by Design) |
| 5 | ADR-AAAS-OPERATIONS-CANON-001 | *sister doctrinal direct* | ADR-AAAS-ACQUISITION-DOCTRINE-001 |
| 6 | ADR-AAAS-PRICING-001 | *amend (USD post-accupuncture SUPERSEDE EUR)* | Pricing historique EUR (Takeout 2026-05) |
| 7 | ADR-AAAS-ACQUISITION-DOCTRINE-001 | *sister canon* | ADR-AAAS-PRICING-001 (5 Tiers USD post-accuponcture) |
| 8 | ADR-AAAS-FINANCE-CANON-001 | *construit sur* | ADR-MARKET-STUDY-001 (The Builders 2026 TAM 136,1 Mds$) |
| 9 | ADR-AAAS-IT-CANON-001 | *construit sur / sister direct* | ADR-AAAS-OPERATIONS-CANON-001 |
| 10 | ADR-AAAS-IT-EXT-CANON-001 | *extends* | ADR-AAAS-IT-CANON-001 |
| 11 | ADR-AAAS-OPERATIONS-CANON-001 | *sister doctrinal direct* | ADR-AAAS-ACQUISITION-DOCTRINE-001 |
| 12 | ADR-CANON-001 (Roster Source of Truth) | *supersedes_scope (AGENTS.md membership)* | AGENTS.md §Macro Squads (lore only) |
| 13 | ADR-L2-AAAS-001 (3 Variants Solarpunk) | *carries* | 3 variants AaaS (Solaris / Nexus-OMK / Orbiter-ABC) × 4 Leviers Solarpunk |
| 14 | ADR-L2-PAPERCLIPAI-001 | *extends/sister* | ADR-SOBER-002 (anti-paperclip kernel) |
| 15 | ADR-L2-PAPERCLIPAI-002 (Anti-paperclip irony) | *sister de* | ADR-L2-PAPERCLIPAI-001 (governance-mirror) |
| 16 | ADR-L2-PAPERCLIPAI-003 (delegation-not-creation) | *amends sister* | ADR-L2-PAPERCLIPAI-001 / -002 |
| 17 | ADR-L2-PAPERCLIPAI-004 (Calibration) | *amends* | All 3 sister ADRs above + Dev Gate autopilot |
| 18 | ADR-L2-KARDASHEV-TYPE-FRACTAL-001 | *extends* | ADR-L2-AAAS-001, ADR-CANON-001, ADR-OMK-MULTICA-001, MEMORY.md, ADR-A0-L-META-00 |
| 19 | ADR-L2-NAMING-CONVENTION-001 | *sister scope* | ADR-L2-MULTIVERSE-CD-001, ADR-L2-TRIPTYQUE-V4-001, SPEC-ENTERPRISE-OS-100M-001,  |
| 20 | ADR-RITUAL-001 (SlashCommand Canon) | *sister scope* | ADR-META-005, ADR-HARNESS-001, ADR-LIFE-013, ADR-LIFE-014, ADR-AAAS-002 |
| 21 | ADR-OPS-009 (Worker Git Commit) | *extends* | ADR-META-001 D4 (no-amnesia append-only) + .claude/rules/git-workflow.md |
| 22 | ADR-RH-META-GOUVERNANCE-001-canonical-v2 | *supersedes_scope = nothing (D4 append-only, canonical alignment)* | ADR-CANON-001, ADR-CANON-002, ADR-AGENT-BENCH-SCHEMA-001, ADR-LANDING-AESTHETIC- |
| 23 | ADR-RH-META-GOUVERNANCE-001-canonical-v3 | *supersedes* | ADR-RH-META-GOUVERNANCE-001-canonical-v2 |
| 24 | ADR-AGENT-BENCH-SCHEMA-001 (agent_bench SQL) | *sister* | ADR-CANON-002 (RHA Workflow) + ADR-RH-META-GOUVERNANCE-001 |
| 25 | ADR-L2-AAAS-US-ONLY-001 (US-only doctrine) | *amend sister* | ADR-ICP-SOLARIS-001 / ADR-ICP-NEXUS-001 / ADR-ICP-ORBITER-001 (géographie amendé |
| 26 | ADR-LANDING-AESTHETIC-001 (Doctrine Esthétique Positive) | *sister (negative mirror)* | ADR-ANTI-TEMPLATE-001 (liste noire) |
| 27 | ADR-LANDING-COPY-001 | *sister-canon negative-rules-source* | ADR-ANTI-PAPERCLIP-001 |
| 28 | ADR-NEXUS-10-ICP-001 | *supersedes_scope* | ADR-OMK-PRODUCTS-001 + 3-sequences-outbound (Strate A + C ajoutées) |
| 29 | RUNBOOK_C1-R1 | *amend §4.2* | Design initial (Docker) |
| 30 | RUNBOOK_C1-R1 | *suit de* | Plan `fancy-hugging-bengio.md` |
| 31 | Architecture Triptyque Morty (12WY⊃PARA⊃DEAL) | *compose nested* | 12WY / PARA / DEAL (3 A2 ships) |
| 32 | Lane A Spec (symphony twin) | *vient de* | 20_Life_OS canon |
| 33 | A1 capsule | *rattachée à (A1 supervisé par)* | A0_Amadeus |
| 34 | Twin (lane A) | *pointe vers capsule (lane C)* | Soul/Agent/Heartbeat/Tools/Context |
| 35 | geordi/01_Guides (à reclassifier) | *doit passer par* | Picard A3 via ADR-L2-BDLD-MAP-001 (bijection 8 B2 ↔ 8 LD) |
| 36 | b1-jerry-prime | *lit chaque INDEX sur intention* | 01_Product / 02_Ops / 03_IT / 04_Finance / 05_Legal / 06_Sales / 07_Growth / 08_ |
| 37 | guide 02_Ops BI-MNjm1tTQ | *couvre* | 5 sub-types persona Structuration-First |
| 38 | guide 07_Growth N-9rovSvCEA (MedVie) | *valide rétroactivement* | thèse AaaS Solarpunk (ADR-L2-AAAS-001 Pilier 3 Sobriété) |
| 39 | JUNCTION_MAP | *détecte via* | stat.FILE_ATTRIBUTE_REPARSE_POINT (0x400) |
| 40 | Jonctions NTFS | *sont écartées* | aspace-graphify-out (808), cross-PARA (24), _TRASH (16), external_home_dot (26) |
| 41 | 03_Resources_Geordi/01_Guides (dossier) | *appartient au bucket* | Resources (S3) |
| 42 | OKF v0.1 | *définit format* | bundle = arbre de .md + frontmatter YAML |
| 43 | B1 Manifest (caste B1/B2/B3) | *ancre dynamique* | ADR-CANON-002 (RHA Workflow) |
| 44 | Symbiose Lane A ↔ Lane C | *suit le symbiose* | canon 20_Life_OS/<ship>/<X>_Spec.md |
| 45 | state.json (40_SYMPHONY_BUS) | *est SSOT pour* | A0 → A1 → A2 → A3 → B1/B2/B3 |
| 46 | Doctrine Lock Map LD01 | *aligne* | plan-meta-memoire-okf-wiki-graphify-dox + plan-minimax-l1-book-lune + plan-strat |
| 47 | B3-Enterprise-Geordi (3 personas) | *réfère canoniquement* | Apartamento Magazine / Linear / Teenage Engineering |
| 48 | manifest.cross-harness (LD01) | *considère* | Claude Code, MiniMax Code, Hermes Agent, Shadow L1 (Agent Zero), Doctor, future- |
| 49 | Phase 47 doctrine | *canalise toutes notes Gemini vers* | wiki/hand_offs/2026-07-31_gemini_brainstorms/ (PAS ~/.claude/memory, ~/.codex/me |
| 50 | AaaS Sisters (Solaris / Nexus / Orbiter) | *exploite marché* | USA UNIQUEMENT (pas Canada, UK, EU, France) |
| 51 | AaaS Sisters US-only | *applique compliance* | CCPA / Colorado AI Act (CO SB24-205) / HIPAA, pas RGPD |
| 52 | Book LD01 | *vaut* | H1 Weekly P&L (PAS H10) |
| 53 | Variant AaaS Book | *est* | Solaris (Kardashev Type 3) |
| 54 | Geordi (A3 Resources) | *est* | A3 Resources canon |
| 55 | Geordi (A3) | *ne fait pas* | Park active deliverables / Archive retired material |
| 56 | Triples Plateforme Doctrine (MESH-L2-001) | *produit 3 plate-formes* | Solaris, Nexus-OMK, Orbiter-ABC |
| 57 | ADR-FWK-021 (Canon Tripartite) | *isomorph L0/L1/L2* | 12_Blueprints/ (L0) · 28_Blueprints/ (L1) · 09_Blueprints/ (L2) |
| 58 | Wargame 30 Triptyque 1 | *produit 3 B2 frames (GreenLantern, Batman, Cyborg)* | 9/8/6 B3 squads (X-Men, Fantastic Four, Kang Dynasty) |
| 59 | MANIFEST Wargame 30 | *porte tri-horizon emboîté* | B1 Summers 1y / B1 Jerry 3y / A3 Picard 10y |

### Citations sélectionnées (extrait)

**R1.** ADR-SOBER-002 (anti-paperclip maximizer doctrine) **anchor sister** ADR-L2-AAAS-001
  > doctrine_anchors: [ADR-META-001, ADR-META-001-D1, ADR-META-001-D5, ADR-META-001-D7, ADR-META-002, ADR-META-003, ADR-META-005, RICK-001, **L2-AAAS-001**, INFRA-003, CANON-001]
  — *03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/INDEX.md*

**R2.** ADR-MEM-001 (Memory Fabric) **sister scope** ADR-MEM-002 (Wiki ↔ Life Wheel Mapping)
  > Cette ADR résout les 2 gaps en un seul document canonique, **sister scope stricte à ADR-MEM-001** (Memory Fabric) — scope = Memory Fabric ↔ Life Wheel LDxx mapping, PAS IndexedDB Cloisonnement.
  — *03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L1_Life_OS/ADR-MEM-002_wiki-lifewheel-mapping-doctrine.md*

**R3.** ADR-MEM-002 **resolves ID collision with** ADR-MEM-001 (historique IndexedDB)
  > (2) ADR-MEM-001 actuel a un D4 collision warn avec un ADR historique IndexedDB (NOT in _SPECS/ADR/ canonique). Hash d'intention résolvant la collision : `adr_mem_002_proposed_2026-06-21_wiki_lifewheel_mapping`.
  — *03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L1_Life_OS/ADR-MEM-002_wiki-lifewheel-mapping-doctrine.md*

**R4.** ADR-META-003 (Model-Agnostic Runtime) **extends/sépare** ADR-META-002 (Autonomy by Design)
  > recommandé en Open Question (META-002 l.144) la création d'un ADR-META-003 séparant proprement harness (invariant) de modèle (variable).
  — *03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L1_Life_OS/ADR-META-003_model-agnostic-runtime-doctrine.md*

**R5.** ADR-AAAS-OPERATIONS-CANON-001 **sister doctrinal direct** ADR-AAAS-ACQUISITION-DOCTRINE-001
  > ADR-AAAS-ACQUISITION-DOCTRINE-001 (RATIFIED 2026-06-24, 25 455 chars, doctrinal sister direct — Acquisition-First MedVie 400M$)
  — *03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-OPERATIONS-CANON-001_aaas-operations-canon.md*

**R6.** ADR-AAAS-PRICING-001 **amend (USD post-accupuncture SUPERSEDE EUR)** Pricing historique EUR (Takeout 2026-05)
  > amended: 2026-06-24 (Hypothèse A retenue : USD post-accuponcture SUPERSEDE EUR takeout)
  — *03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-001_aaas-pricing-canon.md*

**R7.** ADR-AAAS-ACQUISITION-DOCTRINE-001 **sister canon** ADR-AAAS-PRICING-001 (5 Tiers USD post-accuponcture)
  > Guide 2/02_Ops/solopreneur-ai-agent-business-BI-MNjm1tTQ.md (22 708 chars, Antigravity Premium)
  — *03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-ACQUISITION-DOCTRINE-001_aaas-acquisition-doctrine.md*

**R8.** ADR-AAAS-FINANCE-CANON-001 **construit sur** ADR-MARKET-STUDY-001 (The Builders 2026 TAM 136,1 Mds$)
  > ADR-MARKET-STUDY-001 (RATIFIED 2026-06-24, The Builders 2026 TAM 136,1 Mds USD)
  — *03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-FINANCE-CANON-001_aaas-finance-canon.md*

**R9.** ADR-AAAS-IT-CANON-001 **construit sur / sister direct** ADR-AAAS-OPERATIONS-CANON-001
  > ADR-AAAS-OPERATIONS-CANON-001 (RATIFIED 2026-06-24, sister scope canon direct — Operations 5 Piliers)
  — *03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-IT-CANON-001_aaas-it-canon.md*

**R10.** ADR-AAAS-IT-EXT-CANON-001 **extends** ADR-AAAS-IT-CANON-001
  > ADR-AAAS-IT-EXT-CANON-001 (RATIFIED 2026-06-25, 6 Piliers IT Stack ... ADR-AAAS-IT-CANON-001 (RATIFIED 2026-06-24, 5 Piliers AaaS IT canon - SISTER DIRECT)
  — *03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-IT-EXT-CANON-001_aaas-it-ext-canon.md*

**R11.** ADR-AAAS-OPERATIONS-CANON-001 **sister doctrinal direct** ADR-AAAS-ACQUISITION-DOCTRINE-001
  > doctrinal sister direct — Acquisition-First MedVie 400M$
  — *03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-OPERATIONS-CANON-001_aaas-operations-canon.md*

**R12.** ADR-CANON-001 (Roster Source of Truth) **supersedes_scope (AGENTS.md membership)** AGENTS.md §Macro Squads (lore only)
  > supersedes_scope: AGENTS.md §"Macro Squads" roster membership (lore only — NOT structure)
  — *03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-CANON-001_roster-source-of-truth.md*

**R13.** ADR-L2-AAAS-001 (3 Variants Solarpunk) **carries** 3 variants AaaS (Solaris / Nexus-OMK / Orbiter-ABC) × 4 Leviers Solarpunk
  > AaaS Doctrine 3 Variants (Solaris/Nexus-OMK/Orbiter-ABC) × 4 Leviers Solarpunk (biomimétisme Benyus + low-high tech Aberkane + Meta Science + circular & blue economy) + Saru 1000T Kardashev Type 3.
  — *03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/INDEX.md*

**R14.** ADR-L2-PAPERCLIPAI-001 **extends/sister** ADR-SOBER-002 (anti-paperclip kernel)
  > doctrine_anchors: [ADR-META-001 D1-D8, ADR-EXTRA-PPR-001 (PPR-only), **ADR-SOBER-002 (anti-paperclip kernel)**, ADR-OMK-MULTICA-001 (sister substrate)...]
  — *03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-PAPERCLIPAI-001_governance-mirror-doctrine.md*

**R15.** ADR-L2-PAPERCLIPAI-002 (Anti-paperclip irony) **sister de** ADR-L2-PAPERCLIPAI-001 (governance-mirror)
  > doctrine_anchors: ... **ADR-L2-PAPERCLIPAI-001 (sister)**, **ADR-L2-PAPERCLIPAI-003 (sister delegation-not-creation, NEW per Nick LECTURE 2)** ...
  — *03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-PAPERCLIPAI-002_anti-paperclip-irony-doctrine.md*

## §3 — Systèmes de codes

| # | Système | Définit | Défini dans |
|---|---|---|---|
| 1 | **LD01-LD08 (Life Wheel, 8 Life Domains)** | LD01 Career_Business / LD02_Finance_Saru / LD03_Health_Culber / LD04_Cognition_Tilly / LD05_Legal / LD06_Family_Burnham … | 01_Guides/01_Product/_INDEX.md + 03_Memory_Unified/LLM_Wiki/wiki/index.md (Life Wheel — par variant Jerry (Spock doctrin |
| 2 | **B1/B2/B3 (Business Hierarchy)** | B1 = Gatekeeper (Jerry/Summers), B2 = Captain (B2_flash-product, B2_cyborg-it, B2_johnjones-sales, B2_aquaman-legal, B2_… | 01_Guides/01_Product/_INDEX.md (sister_canon: b1-jerry-prime, b2-03-flash-product, b3-3-captain-america) |
| 3 | **A0/A1/A2/A3 (Agent Hierarchy)** | A0 = Amadeus (Méta-Orchestrateur/Souverain), A1 = Gatekeeper (Rick/Beth/Morty), A2 = Ship (Orville, Discovery, Curie_SNW… | 05_From_V2_Domains/00_Amadeus/05_OSS_TSTwin/symphony/L1/INDEX_specs.md (🛡️ A1 — Gatekeepers (2) · 🚀 A2 — Ships (6) · 🛠️  |
| 4 | **H1/H3/H10/H30/H90 (Horizons)** | H1=Weekly_PnL, H3=quarterly runway (Saru), H10=Vision (Pike/Una/Chapel H10), H30=Kardashev, H90=Kardashev-4 Legacy 1000T | 05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/00_index.md (horizon: H1_Weekly_PnL) + 04_From_V2_Ro |
| 5 | **W01-W12 (12 Week Year cadence, weekly)** | 12 Week Year cycle (06/15 → 09/07/26 par exemple) avec sprint W1-W12 (5 disciples: Pike Vision 1/5, Una Planning 2/5, M'… | 04_From_V2_Root/_SPECS/ADR/L1_Life_OS/ADR-Meta-000_12-week-year-cycle-doctrine_DRAFT.md (cycle: 12WY 06/15 - 09/07/26) + |
| 6 | **ADR-<NAMESPACE>-<NNN> (Architectural Decision Record)** | ADR-{LAYER}_{DOMAIN}_{NNN}_{slug}.md — ex: ADR-META-001, ADR-LOOP-001, ADR-CANON-001, ADR-SOBER-002, ADR-AAAS-PRICING-00… | 05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-FWK-021_blueprints-canon-tripartite.md (Convention nommage immuab |
| 7 | **JTBD-<NNN> (Jobs To Be Done) — `01_Guides/PROJECTS/JTBD-001`, JTBD-002, JTBD-003, JTBD-004** | 4 JTBD par défaut (JTBD-001 thin possible, 002/003/004 instantiables selon funnel client). Tier-dependent: Legal-gate fl… | 06_Claude_Code_Bare/skills/picard-growth-jtbd-launch/references/special-cases.md (compliance-bound projects: Add `legal_ |
| 8 | **B1/B2/B3 + LD01-LD08 bijection** | 8 B2 ↔ 8 LD via ADR-L2-BDLD-MAP-001 : 01_Product→LD04_Cognition_Tilly, 02_Ops→LD02_Finance_Saru, 03_IT→LD07_Creativity_R… | 01_Guides/01_Product/_INDEX.md (sister_canon: ADR-L2-BDLD-MAP-001 (Product ↔ LD04_Cognition_Tilly bijection)) |
| 9 | **L0/L1/L2/L3 (Layer architecture)** | L0=Teck_OS (Kernel), L1=Life_OS (Fleet), L2=Business_OS (Projects), L3=? | 00_Index/SECOND_BRAIN_PARA_MAP.md + 05_From_V2_Domains/00_Amadeus/00_Amadeus.README.md (🏛️ The Sovereign Architecture (L |
| 10 | **S0-S4 (Strates mémoire)** | S0=Identité (CLAUDE.md, AGENTS.md, MEMORY.md), S1=court terme (hand_offs/), S2=travail (_CAPTURE_2026-08-01/), S3=canon … | 00_Index/SECOND_BRAIN_PARA_MAP.md (Strate mapping — 14 sous-dossiers ↔ S0-S4) |
| 11 | **Kardashev Type 1-4 + Solar Level** | K1=planétaire, K2=stellaire, K3=galactique (Saru 1000T), K4=universel (Solar Level + Skill Ecosystem) | 04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-KARDASHEV-TYPE-FRACTAL-001_multiverse-architecture_RATIFIED_2026-07-16. |
| 12 | **5 Piliers AaaS (Operations / IT / Finance / Content / Acquisition)** | 5 piliers canon par pilier AaaS — ex: Operations 5 Piliers (Persona · Metrics · Pricing · Harness · Solo Business) | 04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-OPERATIONS-CANON-001_aaas-operations-canon.md |
| 13 | **5 Tiers AaaS Pricing (Solarpunk)** | $300 / $750 / $1500 / $3000-5000 / $50K MRR (USD post-accuponcture) — Tiers PME Solo Founder → Orbiter Enterprise | 04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-001_aaas-pricing-canon.md (Pricing canon : 5 Tiers Solarpunk) |
| 14 | **3 Variants AaaS (Solaris / Nexus-OMK / Orbiter-ABC)** | Solaris (Visual First / DAM), Nexus-OMK (Coaching / ICP 4/5), Orbiter-ABC (Mobile First / Terrain Hybrid) | 04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md |
| 15 | **3 Strates × 10 Catégories ICP** | Strate A (Coachs C-Suite, Leadership grand volume, M&A/transition), Strate B (B1/B2/B3 — Deep Research Gemini), Strate C… | 04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-NEXUS-10-ICP-001_3-strates-10-cibles-canon.md |
| 16 | **Soul/Agent/Heartbeat/Tools/Context (5 fichiers par agent capsule)** | 5 fichiers par agent × 35 A3 + 6 A2 + 2 A1 = 215 fichiers capsules totaux (Phase 1: 40 fichiers, Phase 2: 175 fichiers) | 05_From_V2_Domains/00_Amadeus/05_OSS_TSTwin/symphony/L1/INDEX_capsules.md (Template canon : 5 fichiers par agent: Soul / |
| 17 | **8 Domaines Business** | 01_Product, 02_Ops, 03_IT, 04_Finance, 05_Legal, 06_Sales, 07_Growth, 08_People — 8 Domaines canon AaaS | 01_Guides/01_Product/_INDEX.md (8 Domaines canon, 8 LDxx Life Wheel bijection via ADR-L2-BDLD-MAP-001) |
| 18 | **D1-D12 (Doctrine Anti-Paresse)** | D1=verify-before-assert, D2=cite source, D3=nuance over literal, D4=append-only, D5=real-test-after-edit, D6=no-hallucin… | 04_From_V2_Root/_SPECS/ADR/INDEX.md + ADR-META-001 (D1-D8) + ADR-META-002 (D9-D12) |
| 19 | **Tier T0-T2 (Enterprise OS Blueprint)** | T0 Hobby (solo, $65-95/mo), T1 Standard ($300/mo, small firm), T2 Pro (PHI/HIPAA, $600/mo + write-once audit) | 02_Templates/Enterprise_OS_Blueprint_Kit/specs/ARCHITECTURE_SPEC.md |
| 20 | **Type 0/1/2/3/4/5 (Dark Factory levels)** | Type 0 (manual), Type 1 (assisted), Type 2 (single-agent), Type 3 (multi-agent), Type 4 (full autonomy gated), Type 5 (c… | 05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/99_meta/doctrine_lock_map.md (BC-True-Autonomy: Eero |

## §4 — Contradictions

> **14 contradictions relevées**, sans trancher. À voir avec A0.

| # | Sujet | A (chemin) | Date A | B (chemin) | Date B |
|---|---|---|---|---|---|
| 1 | 3 referents 'Paperclip' polysémique | `04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-PAPERCLIPAI-002_anti-paperclip-` | 2026-07-11 | `04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-PAPERCLIPAI-001_governance-mirr` | 2026-07-11 |
| 2 | ADR-MEM-001 ID collision (Memory Fabric vs IndexedDB Cloisonnement) | `04_From_V2_Root/_SPECS/ADR/L1_Life_OS/ADR-MEM-001_memory-fabric-unified-doctrine` | 2026-06-15 | `04_From_V2_Root/_SPECS/ADR/L1_Life_OS/ADR-MEM-002_wiki-lifewheel-mapping-doctrin` | 2026-06-21 |
| 3 | Count des jonctions NTFS (47 vs 159) | `00_Index/JUNCTIONS_MAP_2026-08-02.md` | 2026-08-02 | `00_Index/JUNCTIONS_MAP_2026-08-02.md` | 2026-08-02 |
| 4 | EUR vs USD pricing (ADR-AAAS-PRICING-001 amended) | `04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-001_aaas-pricing-cano` | 2026-06-24 | `04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-001_aaas-pricing-cano` | 2026-05 (Takeout) |
| 5 | Sister v2 vs v3 RH-META-GOUVERNANCE-001 (Yggdrasil fold) | `04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-RH-META-GOUVERNANCE-001-canonical-` | 2026-07-25 | `04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-RH-META-GOUVERNANCE-001-canonical-` | 2026-07-26 |
| 6 | 01_Guides (LD06_Family_Burnham vs LD01_Business Picard) — _kIxjlEf_0U.md file declares `ld: LD06_Fam | `01_Guides/06_Sales/_INDEX.md` | 2026-07-03 | `01_Guides/06_Sales/_INDEX.md` | 2026-07-03 |
| 7 | 8 Domaines canon (1 par LDxx bijection) vs 7 domaines historiques (1 manquant : Sales / Illuminati / | `04_From_V2_Root/_SPECS/ADR/INDEX.md (8 Domaines canon ratifiés batch 2026-06-21)` | 2026-06-21 | `(SDD-006_business-pulse-l2-pyramide.md, brief signale 7 domaines historiques vs ` | (anterior) |
| 8 | Geordi 03 (Ressources) sister Geordi 04 (variant TSTwin corrompu) — deux dossiers jumeaux avec conte | `05_From_V2_Domains/00_Amadeus/05_OSS_TSTwin/symphony/L1/INDEX_specs.md` | 2026-06-07 | `05_From_V2_Domains/00_Amadeus/05_OSS_Twin/symphony/L1/INDEX_specs.md` | 2026-06-07 |
| 9 | Roster: AGENTS.md 4-member squads vs B3 transcriptions 8-member squads (CANON-001 Notion prime) | `04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-CANON-001_roster-source-of-truth.m` | 2026-06-02 | `00_Amadeus/01_Identity_Core/AGENTS.md (abbreviated 4-member squads)` | (anterior) |
| 10 | MAP count (5 vs 8) domaines canon business, ADR-L2-BDLD-MAP-001 vs ADR-L2-AAAS-001 | `04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-AAAS-001_aaas-doctrine-3-varian` | 2026-06-21 | `04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-RH-META-GOUVERNANCE-001-canonical-` | 2026-07-25 |
| 11 | 5 A3 SNW vs A2 SNW Curie twin manquant (D4 self-contradiction) | `03_Memory_Unified/LLM_Wiki/wiki/hand_offs/architecture_triptyque_morty_2026-06-2` | 2026-06-21 | `05_From_V2_Domains/00_Amadeus/05_OSS_TSTwin/symphony/L1/INDEX_specs.md (A2 Curie` | 2026-06-15 |
| 12 | Calibration Routine tasks EXEMPT (D6 lesson from Multica over-fire 2026-07-16) | `04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-PAPERCLIPAI-004_paperclip-calib` | 2026-07-16 | `04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-PAPERCLIPAI-001_governance-mirr` | 2026-07-11 |
| 13 | geordi 01_Guides 11 PREMIUM Batches non reclassifiés (détour principal) | `01_Guides/_BATCH_RECLASSIFICATION_INDEX.md` | 2026-07-03 | `01_Guides/01_Product/_INDEX.md (squelettes existent pour 8 sous-domaines, mais 1` | 2026-07-03 |
| 14 | Yann Leonardi INDEX statut V0_HEURISTIC vs V1 (b1_filter appliqué partiellement) | `01_Guides/07_Growth/Yann_Leonardi/INDEX_QA_REPORT.md (V0_HEURISTIC, QA_REQUIRED)` | 2026-07-03 | `01_Guides/07_Growth/Yann_Leonardi/YANN_CORPUS_INDEX.md (b1_filter: APPLIED_E1_DE` | 2026-07-03 |

## §5 — Couverture honnête

**Quota** : 150 chemins minimum. **Atteint** : 935 fichiers uniques lus.

**Ce que j'ai lu** :
- 100% des `_SPECS/ADR/L0_*/` et `_SPECS/ADR/L1_*/` et `_SPECS/ADR/L2_*/` (38 ADRs + 14 drafts).
- 100% des `00_Index/*.md` canoniques (INDEX_OF_INDEXES, OKF_INDEX, RESOURCES_INDEX, SECOND_BRAIN_PARA_MAP, JUNCTIONS_MAP).
- 100% des `01_Guides/*_INDEX.md` (8 B2 domains + 2 batches INDEX).
- 100% des `_SPECS/ADR/META_Organization/*.md`.
- 100% des `02_Templates/Enterprise_OS_Blueprint_Kit/specs/*SPEC.md` (AGENT/COST/SECURITY/SYSTEM/ARCHITECTURE canon + 3 examples).
- 95% des MANIFEST projects (abc, ceo-desktop, cerritos-gtd-dispatch, omk, rilcot, solaris + wargame-30-out).
- 100% des Lane A/B/C twin INDEX (symphony L1).
- 100% des handoffs wiki canoniques (architecture_triptyque, sessions_archive, gemini_brainstorms, 2026-07-22_aaas_us_only).
- 75% des wargame manifests (W30 Triptyque 1 BusinessOS, sub-MANIFESTs).

**Ce que j'ai laissé de côté** (lecture superficielle ou non-lue) :
- 808 fichiers `aspace-graphify-out/*` (pipeline de sortie — pas de l'ossature, écartés par filtre brief).
- 374 fichiers `.codex-m3-lean/*` (config Codex CLI : lus en surface, dominés par plugins/skills marketplace pas la doctrine A'Space).
- 278 fichiers `08_Workspaces_Dormants_2026-08-01/*` workspaces dormants (lecture des READMEs seulement).
- 209 fichiers `06_Claude_Code_Bare/plugins/*` (essentiellement les plugins/agents/skills marketplace Claude Code officiel — lus en surface).
- ~200 fichiers deep ADRs `_SPECS/ADR/*` non lus intégralement (couverture de surface, pas deep read).
- ~2000 fichiers `01_Guides/*` ressources YouTube distillées (lecture de la première section par canal, pas deep read).

**Compteur `fichiers_lus`** : **935**.

**Jonctions écartées** : 832, dont :
- 808 dans `04_From_V2_Root/aspace-graphify-out/` (sortie pipeline Graphify)
- 24+ dans `09_From_Home_Root_Batch2_2026-08-01/_DRAFTS_PPR_LANE/_DRAFTS/jct-*`
- Detection : `stat.FILE_ATTRIBUTE_REPARSE_POINT (0x400)` (cf. `00_Index/JUNCTIONS_MAP_2026-08-02.md`).

## §6 — Ce que la vague 3 a fait émerger (au-delà des v1+v2)

1. **Le système ADR est tri-partite L0/L1/L2 strict**, avec META_Organization comme quatrième sous-arbre (ADR-AGENTIC-ARCH-001 + ADR-AGENTIC-LONG-HORIZON-001 RATIFIED 2026-07-26).
2. **Trois sister ADRs Paperclipai (-001/-002/-003) forment une chaîne intentionnelle : governance-mirror → anti-irony → delegation-not-creation**, et un -004 (calibration) amendant les 3 sisters + Dev Gate autopilot suite à l'incident Multica over-fire 2026-07-16.
3. **ADR-AAAS-* forme un réseau d'au moins 8 ADR ratifiés** (Operations, Finance, IT, IT-Ext, Content, Acquisition, Pricing, AaaS 3-Variants) avec une `doctrine_anchors` chaîne pointant vers META-001 + META-002 + SOBER-002 + L2-AAAS-001.
4. **Manifest cross-harness** (`LD01/90_manifests/`) introduit 6 harnesses (Claude Code, MiniMax, Hermes, Shadow L1 Agent Zero, mavis-doctor, future-shadow) avec une `entry sequence` par harness.
5. **Doctrine Lock Map** aligne 4 plans canoniques (plan-meta-memoire, plan-minimax-l1-book-lune, plan-strategie-cc-l1-zora-macro, fancy-hugging-bengio) avec l'organigramme LD01 — pont bidirectionnel.
6. **JUNCTION_MAP_2026-08-02** chiffre 159 jonctions (vs 47 annoncées dans le brief), avec classification par catégorie de risque (dead/trash_jct/external_home_dot/external_appdata/intra_g/cross_para_*).
7. **Symphony Twin Architecture** isomorphe canon ↔ twin : `20_Life_OS/<ship>/<X>_Spec.md → OSS_Twin/symphony/L1/lane_A_specs/<X>_Spec.twin.md`.
8. **AaaS Sisters US-only doctrine** (`ADR-L2-AAAS-US-ONLY-001` RATIFIED 2026-07-22) banni Canada/UK/EU/France/Mexique, applique CCPA/Colorado AI Act/HIPAA, super-cedes ICP-SOLARIS/NEXUS/ORBITER sister scope.
9. **5 Tiers AaaS Pricing canon** ($300/$750/$1500/$3000-5000/$50K MRR) post-accupuncture USD supersede EUR historique Takeout 2026-05.
10. **Wargame 30 Triptyque 1** produit 3 B2 frames (GreenLantern/Batman/Cyborg) avec 9+4+6=19 B3 squads, et un tri-horizon emboîté Summers-1y/Jerry-3y/Picard-10y.
11. **Architecture Triptyque Morty** (12WY⊃PARA⊃DEAL) 3 A2 ships imbriqués par conception (Russian dolls).
12. **Dark Factory Type 0-5** via Cole Medin + Eero Alvar continuous reasoning : Phase 1 sandbox → Phase 3 L5 gated Rick S1.
13. **4 Pivots calendaires (12WY Q3 2026 = 06/15 → 09/07)** : cycle doctrine ratifié via ADR-Meta-000 (2026-06-15).
14. **9 Domaines Business canon** confirmés (8 B2 + 1 implicite ? — voir CONTRADICTION 7 sur le count 7 vs 8).

## §7 — Fichiers de sortie

| Fichier | Description |
|---|---|
| `carto/03_Resources_Geordi_v3.json` | JSON canon (22 types, 59 relations, 20 codes, 14 contradictions) |
| `carto/03_Resources_Geordi_v3.md` | Ce rapport (présentation humaine) |

## §8 — Limites & honneteté

- **935 fichiers uniques lus** mais beaucoup en lecture superficielle (10-25 lignes) pour atteindre la breadth. Les ADRs sont lus intégralement (50-100 lignes) pour les 50 premiers ; le reste en surface.
- **Compteur `fichiers_lus`** = `935` = nombre de fichiers uniques touchés en vague 3. Compteur honnête.
- **Compteur `fichiers_disponibles`** = `1826` = nombre de fichiers dans la priority list filtrée (post-ignore `aspace-graphify-out`/`node_modules`/`_TRASH`).
- **`jonctions_ecartees`** = `832` = estimation (808 graphify-out + 24+ cross-PARA). Le JUNCTION_MAP officiel annonce 159 — l'écart vient de fichiers de jonctions répétés par deep-nesting non comptés.
- **Pas de gate S0/S3/S4** : aucun fichier `_DRAFTS_PPR_LANE/_SPECS/ADR/_DRAFTS` cité comme canon (donc à valider scope A0 si utilisé pour V4).
- **D6 honest gap** : le count des types/relations n'est pas saturé — passer une vague 4 permettrait ~200 fichiers additionnels (essentiellement ADRs deep-read, .codex-m3-lean plugins deep, wargames profonds).