import json
from pathlib import Path

CWD = Path('C:/Users/amado/ASpace_OS_V3/00_Amadeus/30_MEMORY_CORE/carto')

# V4 reads — paths counted (approximation: each Read invocation = 1 file read)
# I kept track during the reads. Total reads this wave ≈ 95.
v4 = {
    "seau": "03_Resources_Geordi",
    "fichiers_lus": 95,
    "fichiers_disponibles": 1826,
    "jonctions_ecartees": 832,
    "types": [],  # filled below
    "relations": [],
    "codes": [],
    "contradictions": [],
}

# NEW TYPES (not in v3) — extracted from v4 reads
v4["types"] = [
    {
        "nom": "OKF Bundle (4-pillar standard)",
        "attributs": [
            "type (REQUIRED, seul champ requis)",
            "title (recommandé)",
            "description (recommandé, critère bloquant d'indexation)",
            "resource",
            "tags",
            "timestamp (ISO 8601)",
            "okf_version (RÉSERVÉ, uniquement sur index.md racine)",
            "metadata.* (pré-OKF, à migrer top-level)",
            "source/date/domain (extension producteur, conservés tels quels)"
        ],
        "chemins": [
            "03_Resources_Geordi/00_Index/OKF_INDEX.md",
            "03_Resources_Geordi/00_Index/INDEX_OF_INDEXES.md",
            "03_Resources_Geordi/00_Index/GEORDI_KB_ROOT.md",
            "03_Resources_Geordi/00_Index/RESOURCES_INDEX.md",
            "03_Resources_Geordi/00_Index/SECOND_BRAIN_PARA_MAP.md",
            "03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/index.md",
            "03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/00_index.md"
        ]
    },
    {
        "nom": "Manifeste (couche L0/L1/L2)",
        "attributs": [
            "Guardian (A0, A1, A2, A3 nommés)",
            "Scope (mission périmètre)",
            "Prime Directives (règles absolues)",
            "Caste System (hiérarchie agents)",
            "Architectural Pattern (matryoshka, fishbone, etc.)"
        ],
        "chemins": [
            "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/Manifesto.md",
            "03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/Manifesto.md",
            "03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/Manifesto.md",
            "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/01_Identity_Core/Manifeste_Souverain.md",
            "03_Resources_Geordi/04_From_V2_Root/ARCHITECTURE_STRUCTURE.md"
        ]
    },
    {
        "nom": "Reality Map (snapshot factuel état construit)",
        "attributs": [
            "Destinataire (agent isolé sans filesystem)",
            "Objectif (transmettre réalité du système)",
            "Date de snapshot",
            "Source de vérité (path absolu)",
            "Sections catalogues (Shell, Apps, Stores, Librairies, Matrice Coopération)"
        ],
        "chemins": [
            "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/Reality_map.md",
            "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/Life_Reality_map.md",
            "03_Resources_Geordi/04_From_V2_Root/_TRASH_2026-06-22_reality_map/REALITY_MAP.md"
        ]
    },
    {
        "nom": "A0 Reasoning Map (filtre méta-conscience)",
        "attributs": [
            "Phase CLARIFY (3 questions socratiques max)",
            "Phase SCORE (grille multicritères Ikigai × Horizon × Life Wheel × Faisabilité OS × E-Myth)",
            "Phase ROUTE (verdict PASS/INCUBER/KILL + ticket Vault)",
            "5 Signaux d'alerte (CONCEPTION DRIFT, FRACTAL CREEP, TOOL HOARDING, HORIZON ESCAPE, ROLE COLLAPSE)",
            "Test 5 minutes"
        ],
        "chemins": [
            "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/a0_reasoning_map.md"
        ]
    },
    {
        "nom": "Roadmap 12WY (4 cycles × 12 Rocks × 48 sprints)",
        "attributs": [
            "Cycle (12WY-01 à 12WY-04)",
            "Fenêtre W1-W13",
            "Thème",
            "Cible MRR fin de cycle",
            "3 Rocks par cycle (moteur 3T, livrable, métrique SQL)",
            "Cadence (PICARD → SUMMERS → 8 B2 → B3 → UPLINK)",
            "5 Daily Scrums (état, conversion, système, receipt, uplink)",
            "Règle unique (chaque niveau ne remonte que du chiffré)"
        ],
        "chemins": [
            "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/ROADMAP_DEAL_12WY_2026-2027.md"
        ]
    },
    {
        "nom": "Doctrine Lock Map (map croisée plans ↔ organigramme)",
        "attributs": [
            "type (doctrine-lock-map)",
            "title (lien plans ↔ organigramme)",
            "description (pont bidirectionnel)",
            "timestamp",
            "domain (LD01_Career_Business)",
            "verified_by (Select-String cmdlet)",
            "plans_sources[] (paths absolus)",
            "rot_rate (lent)"
        ],
        "chemins": [
            "03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/99_meta/doctrine_lock_map.md"
        ]
    },
    {
        "nom": "Doctrine Index (B2 8-domain INDEX)",
        "attributs": [
            "title",
            "date",
            "amend_status (canon / évolution)",
            "total_files",
            "B1_filter (REQUIRED for /youtube-to-guide)",
            "sister_canon[] (b1-jerry-prime, b2-*, b3-*, ADRs)",
            "Owner (B1/B2/B3 by LD domain)",
            "Premium Guides (table vidéo → sujet → status)",
            "B1-filter pain-point (D6 lesson)"
        ],
        "chemins": [
            "03_Resources_Geordi/01_Guides/00_KERNEL_OS/_INDEX.md",
            "03_Resources_Geordi/01_Guides/01_Product/_INDEX.md",
            "03_Resources_Geordi/01_Guides/02_Ops/_INDEX.md",
            "03_Resources_Geordi/01_Guides/03_IT/_INDEX.md",
            "03_Resources_Geordi/01_Guides/04_Finance/_INDEX.md",
            "03_Resources_Geordi/01_Guides/05_Legal/_INDEX.md",
            "03_Resources_Geordi/01_Guides/06_Sales/_INDEX.md",
            "03_Resources_Geordi/01_Guides/07_Growth/_INDEX.md",
            "03_Resources_Geordi/01_Guides/08_People/_INDEX.md",
            "03_Resources_Geordi/09_Life_OS/LD01_Business_Picard/_INDEX.md",
            "03_Resources_Geordi/09_Life_OS/LD04_Cognition_Tilly/_INDEX.md"
        ]
    },
    {
        "nom": "Plugin Manifest Schema (Claude Code)",
        "attributs": [
            "version (MANDATORY)",
            "commands (array of paths)",
            "skills (array of paths)",
            "PAS de 'agents' (interdit, échec Invalid input)",
            "PAS de 'hooks' si hooks/hooks.json standard (auto-load)",
            "mcpServers {} (empty opt-out pour Claude plugin)",
            "hooks (additional non-standard files only)"
        ],
        "chemins": [
            "03_Resources_Geordi/06_Claude_Code_Bare/PLUGIN_SCHEMA_NOTES.md",
            "03_Resources_Geordi/06_Claude_Code_Bare/README.md"
        ]
    },
    {
        "nom": "ARCHITECTURE_SPEC (worked example, T0-T2 tiers)",
        "attributs": [
            "Design principles (one account, one orchestrator, Bedrock, KMS, WORM audit)",
            "Secure-substitute map (current tool → in-account substitute)",
            "Data flow (one account, one chokepoint)",
            "Stacks in dependency order (Network/Storage/Secrets/Data/IAM/Compute/Messaging/Security/Observability/CostGuardrails)",
            "Key decisions and tradeoffs (tier, VPC endpoints, audit Object Lock, model mix)",
            "Tier (T0 Hobby / T1 Standard / T2 Pro PHI)"
        ],
        "chemins": [
            "03_Resources_Geordi/02_Templates/Enterprise_OS_Blueprint_Kit/specs/ARCHITECTURE_SPEC.md",
            "03_Resources_Geordi/02_Templates/Enterprise_OS_Blueprint_Kit/specs/architecture_spec_omk_nexus.md",
            "03_Resources_Geordi/02_Templates/Enterprise_OS_Blueprint_Kit/examples/northgate-law/ARCHITECTURE_SPEC.md",
            "03_Resources_Geordi/02_Templates/Enterprise_OS_Blueprint_Kit/examples/riverside-clinic/ARCHITECTURE_SPEC.md",
            "03_Resources_Geordi/02_Templates/Enterprise_OS_Blueprint_Kit/examples/solo-consultant/ARCHITECTURE_SPEC.md"
        ]
    },
    {
        "nom": "Architecture Research Template (gsd-core)",
        "attributs": [
            "Domain",
            "Researched (date)",
            "Confidence (HIGH/MEDIUM/LOW)",
            "Standard Architecture (system overview ASCII)",
            "Component Responsibilities table",
            "Recommended Project Structure",
            "Architectural Patterns (3+)",
            "Data Flow (state management)",
            "Scaling Considerations (0-1k, 1k-100k, 100k+)",
            "Anti-Patterns",
            "Integration Points"
        ],
        "chemins": [
            "03_Resources_Geordi/06_Claude_Code_Bare/gsd-core/templates/research-project/ARCHITECTURE.md",
            "03_Resources_Geordi/06_Claude_Code_Bare/gsd-core/templates/codebase/architecture.md"
        ]
    },
    {
        "nom": "Phase Spec Template (gsd-core, falsifiable requirements)",
        "attributs": [
            "Phase number + name",
            "Created date",
            "Ambiguity score (gate ≤ 0.20)",
            "Requirements locked (label, current, target, acceptance)",
            "Boundaries (in scope, out of scope)",
            "Constraints",
            "Acceptance Criteria (checkboxes PASS/FAIL)",
            "Edge Coverage (covered/dismissed/backstop/UNRESOLVED)",
            "Prohibitions (must-NOT)",
            "Interview Log (round, perspective, question, decision)"
        ],
        "chemins": [
            "03_Resources_Geordi/06_Claude_Code_Bare/gsd-core/templates/spec.md"
        ]
    },
    {
        "nom": "Index (Sean Lane Symphony)",
        "attributs": [
            "source",
            "date",
            "type",
            "layer (L0/L1)",
            "lane (A_specs/B_runtime/C_capsules)",
            "status (ACTIVE/SCAFFOLD_ONLY)",
            "domain",
            "tags (Lane|Ship|Crew)"
        ],
        "chemins": [
            "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/05_OSS_TSTwin/symphony/L1/INDEX_specs.md",
            "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/05_OSS_TSTwin/symphony/L1/INDEX_runtime.md",
            "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/05_OSS_TSTwin/symphony/L1/INDEX_capsules.md"
        ]
    },
    {
        "nom": "Kit README (starter kit)",
        "attributs": [
            "What's in this kit (table file/fold → role)",
            "How to use (Path A/B/C)",
            "The principle (donnée d'ingénierie première)",
            "Status (experimental/canonical)",
            "Join CTA (community)"
        ],
        "chemins": [
            "03_Resources_Geordi/02_Templates/ClaudeClaw Mission Control Kit/README.md",
            "03_Resources_Geordi/02_Templates/Enterprise_OS_Blueprint_Kit/README.md",
            "03_Resources_Geordi/02_Templates/fable-wargame-kit/README.md"
        ]
    },
    {
        "nom": "Codex Lean Config (MiniMax M3)",
        "attributs": [
            "config.toml (model, provider, sandbox, instructions override)",
            "lean-instructions.md (minimal system instructions)",
            "PowerShell aliases (codexm, codexm-full)",
            "Maintenance rules (jamais hooks, jamais plugins, jamais MCPs)"
        ],
        "chemins": [
            "03_Resources_Geordi/04_From_V2_Root/.codex-m3-lean/README.md"
        ]
    },
    {
        "nom": "Integration Spec (CEO-BENCH + SpecLoop)",
        "attributs": [
            "11 CEO-BENCH composants (C1-C11)",
            "7 SpecLoop composants (S1-S7)",
            "Câblage dans la cadence (PICARD → SUMMERS → B2 → B3 → UPLINK)",
            "Le Next Week réel (5 étapes machine)",
            "La Base SQL réelle (6 tables, 4 vues)"
        ],
        "chemins": [
            "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/INTEGRATION_CEOBENCH_SPECLOOP.md"
        ]
    },
    {
        "nom": "Bridge README (Life OS Client)",
        "attributs": [
            "Technical Stack (React 19 + Vite 6 + Zustand 5 + Tailwind 4 + IndexedDB + Supabase)",
            "Internal Frameworks (App ID → Ship Class → Purpose)",
            "Development (Setup, Build)",
            "Architecture Note (Spec-Driven Development)"
        ],
        "chemins": [
            "03_Resources_Geordi/04_From_V2_Root/_Life-OS-2026-clone/README.md"
        ]
    },
    {
        "nom": "Sessions Indexer Spec",
        "attributs": [
            "Input (chaque *.jsonl dans ~/.claude/projects/C--Users-amado/)",
            "Output schema (sessionId, filename, startedAt, endedAt, messageCount, filesTouched, keywords)",
            "Hardcoded path constants (SESSIONS_DIR, OUTPUT)",
            "Output sort (chronological ascending)",
            "First user prompt + first assistant reply (truncated)"
        ],
        "chemins": [
            "03_Resources_Geordi/06_Claude_Code_Bare/skills/sessions-archive/references/indexer-spec.md"
        ]
    },
    {
        "nom": "LLM Wiki (Geordi wiki bundle)",
        "attributs": [
            "okf_version (0.1, sur index.md racine seul)",
            "L0 Bedrock (Rick's Verse: infra, orchestration, agent-runtime)",
            "Life Wheel (par variant Jerry: J01_Prime, J02_Bio, J03_Nexus, J04_Solarpunk)",
            "Concepts (16 pages)",
            "Entities (4 pages)",
            "Syntheses (2)",
            "Comparisons (2)",
            "Hand-offs (167)",
            "Sources (25)",
            "Audits (8)",
            "Agent Capsules (5 templates: Soul/Agent/Heartbeat/Tools/Context)",
            "Loi du harvest (W22 M5, 2026-07-13) — page evergreen n'est créée QUE depuis artefact shippé"
        ],
        "chemins": [
            "03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/index.md",
            "03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/Gemini_Takeout_2026/_index.md"
        ]
    },
    {
        "nom": "Strategy Triptych (12WY ⊃ PARA ⊃ DEAL)",
        "attributs": [
            "Source canon (plan fancy-hugging-bengio.md §3.1)",
            "3 niveaux imbrication par conception (Russian dolls)",
            "12WY outer (5 disciples SNW: Pike/Una/M'Benga/Chapel/Ortegas)",
            "PARA mid (4 A3: Picard/Spock/Geordi/Data)",
            "DEAL inner (4 A3: Dal/Rok-Tahk/Zero/Gwyn)",
            "Anti-paperclip Saru 1000T (Book LD01 + Tilly LD04 + Gwyn DEAL)",
            "Workflow example D1 trace Q3 2026 W1"
        ],
        "chemins": [
            "03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/hand_offs/architecture_triptyque_morty_2026-06-21.md",
            "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/Manifesto.md"
        ]
    },
    {
        "nom": "EM Expansion Omnibus (Domain 08 Legal Foundation)",
        "attributs": [
            "id (slug, B2_SPEC_<DOMAIN>_<SQUAD>_EXPANSION_<NNN>)",
            "title (Domain + Squad + EXPANSION MODE)",
            "type (Expansion Omnibus D4 append-only)",
            "status (PROPOSED_EXPANSION)",
            "date",
            "tick_id / cron_id",
            "parent_adr (ADR ratifié)",
            "anchor_alignment[]",
            "sources_canons[]",
            "Mission statement (verbatim)",
            "Squad roster (10 members)",
            "SOUL schema (manager/squad/expansion_mode/system_prompt/action_space_bounding/research_loop_config/gatekeeper_approval)",
            "3 base Rocks (12WY Q3) + 3 EXPANSION Rocks (X1/X2/X3)",
            "Delivery matrix (24/7 cadence)",
            "D6 honest gaps (named, not auto-fixed)",
            "D1 receipts (sources read + cited)",
            "Posture (artefact-first, no code mutation)"
        ],
        "chemins": [
            "03_Resources_Geordi/04_From_V2_Root/tmp/B2_Spec_Aquaman_Eternals_EXPANSION_2026-07-26.md",
            "03_Resources_Geordi/04_From_V2_Root/tmp/B2_Spec_GreenLantern_XMen_EXPANSION_2026-07-26.md",
            "03_Resources_Geordi/04_From_V2_Root/tmp/B2_Spec_Cognition_Illuminati_C2_EXPANSION_2026-07-26.md"
        ]
    },
    {
        "nom": "INDEX_QA_REPORT (audit sémantique de bibliothèque)",
        "attributs": [
            "domain (07_Growth)",
            "ld (LD08_Impact_Georgiou)",
            "b2_owner (superman-growth)",
            "sister_b1 (jerry-prime)",
            "b1_filter (APPLIED_* sweep)",
            "Alertes Majeures & Recommandations",
            "Doublons Identifiés & Gestion des Variantes",
            "Répartition par Confiance Sémantique (HIGH/MEDIUM/LOW/FALLBACK)",
            "Liste Fallback à auditer"
        ],
        "chemins": [
            "03_Resources_Geordi/01_Guides/07_Growth/Yann_Leonardi/INDEX_QA_REPORT.md"
        ]
    },
    {
        "nom": "ADR-INDEX (cross-reference canon)",
        "attributs": [
            "id (ADR-INDEX)",
            "title (ADR Index — Cross-Reference & doctrine_anchors Backfill)",
            "type (index)",
            "date",
            "status (ACTIVE)",
            "doctrine_anchors[]",
            "domain (L0 Tech_OS / ADR)",
            "L0 tableau (8 ADR)",
            "L1 tableau (11 ADR)",
            "L2 tableau (14 ADR)",
            "D1 receipts (chemins vérifiés + frontmatter inspection)"
        ],
        "chemins": [
            "03_Resources_Geordi/04_From_V2_Root/_SPECS/ADR/INDEX.md"
        ]
    },
    {
        "nom": "Wiki Handoff (canon D7 anti-effondrement)",
        "attributs": [
            "TL;DR (verdict + driver)",
            "Pourquoi (D6 root cause)",
            "Périmètre géographique (post ADR)",
            "Hébergement infrastructure sister scope",
            "Compliance (city/state AI laws)",
            "Pricing sister scope",
            "Sister canon modifications requises",
            "Réversibilité",
            "Cross-refs",
            "D6 Lessons shipped"
        ],
        "chemins": [
            "03_Resources_Geordi/04_From_V2_Root/wiki/hand_offs/2026-07-22_aaas_us_only_doctrine.md"
        ]
    },
    {
        "nom": "Plugin Manifest Gotchas Notes",
        "attributs": [
            "agents: Invalid input (vague error)",
            "version field mandatory",
            "Field shape rules (arrays for commands/skills/hooks)",
            "Path resolution rules",
            "Validator behavior notes",
            "Known anti-patterns",
            "Minimal known-good example",
            "Why this file exists"
        ],
        "chemins": [
            "03_Resources_Geordi/06_Claude_Code_Bare/PLUGIN_SCHEMA_NOTES.md"
        ]
    },
    {
        "nom": "Conducteur/Runtime Index (workspaces dormants)",
        "attributs": [
            "Definition (Project Definition, Workflow, Management)",
            "Tracks Registry",
            "Tracks Directory (phase_0_wsl, symphony_rag_processing, etc.)"
        ],
        "chemins": [
            "03_Resources_Geordi/08_Workspaces_Dormants_2026-08-01/conductor/index.md",
            "03_Resources_Geordi/08_Workspaces_Dormants_2026-08-01/conductor/tracks/phase_0_wsl/index.md",
            "03_Resources_Geordi/08_Workspaces_Dormants_2026-08-01/conductor/tracks/symphony_rag_processing/index.md"
        ]
    },
    {
        "nom": "README (kit/agent/citadel)",
        "attributs": [
            "Rôle (Resources 03 - lever les paliers)",
            "Critère d'entrée (description non vide)",
            "Don d'usage (catalogue des ressources PARA réutilisables)"
        ],
        "chemins": [
            "03_Resources_Geordi/04_From_V2_Root/wiki/README.md",
            "03_Resources_Geordi/06_Claude_Code_Bare/README.md",
            "03_Resources_Geordi/07_From_Home_Root_2026-08-01/README.md",
            "03_Resources_Geordi/08_Workspaces_Dormants_2026-08-01/README.md"
        ]
    },
    {
        "nom": "ADR (canonique) — Extension OpenSpec",
        "attributs": [
            "id (slug)",
            "title",
            "type (Expansion Omnibus D4 append-only)",
            "status (PROPOSED/RATIFIED/ACCEPTED/DRAFT/RADIE)",
            "date",
            "tick_id / cron_id",
            "parent_adr (sister canonique)",
            "anchor_alignment[]",
            "sources_canons[] (sisters)",
            "proposed_by (A0/A3/B-x)",
            "deciders[] (A+ ratify)",
            "domain",
            "tags[]"
        ],
        "chemins": [
            "03_Resources_Geordi/04_From_V2_Root/_DRAFTS_PPR_LANE/2026-07-25_rh_meta_gouvernance/ADR-AGENT-BENCH-SCHEMA-001_agent-bench-sql-canonique_PROPOSED.md"
        ]
    },
    {
        "nom": "LD01 Book — Index Racine (OKF v0.1)",
        "attributs": [
            "okf_version (0.1)",
            "type (book-doctrine-root)",
            "title (LD01 Book — Career & Business)",
            "description (organigramme canonique)",
            "timestamp",
            "domain (LD01_Career_Business)",
            "agent (A3_Book)",
            "horizon (H1_Weekly_PnL)",
            "variant (AaaS_Solaris_Kardashev_Type_3)",
            "parent_dox",
            "sister_plans[]",
            "children[]"
        ],
        "chemins": [
            "03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/00_index.md"
        ]
    }
]

# NEW RELATIONS — extracted from v4 reads (verbatim citations where possible)
v4["relations"] = [
    {
        "de": "OKF v0.1",
        "verbe": "définit",
        "vers": "frontmatter YAML (champs requis : type, title, description, okf_version)",
        "citation": "**2.2 Champs frontmatter — matrice de conformité** | `type` | **OUI** | oui | **Seul champ requis.** Détermine le typage du nœud (concept, entity, hand_off, log, etc.)",
        "chemin": "03_Resources_Geordi/00_Index/OKF_INDEX.md"
    },
    {
        "de": "Wiki",
        "verbe": "est un bundle OKF",
        "vers": "racine canonique (wiki/ se conforme à OKF v0.1)",
        "citation": "**Relation entre les 4** : OKF définit le format ; le wiki EST un bundle OKF (décision §3 #1 du plan maître)",
        "chemin": "03_Resources_Geordi/00_Index/OKF_INDEX.md"
    },
    {
        "de": "Resources 03_Resources_Geordi",
        "verbe": "fournit",
        "vers": "RESOURCES_INDEX.md (porte d'entrée de tout Geordi)",
        "citation": "Catalogue des ressources PARA réutilisables. Porte d'entrée de **tout** `03_Resources_Geordi`, pas seulement du wiki — `wiki/index.md` en est un enfant.",
        "chemin": "03_Resources_Geordi/00_Index/RESOURCES_INDEX.md"
    },
    {
        "de": "GRAPHIFY",
        "verbe": "consomme",
        "vers": "bundles OKF",
        "citation": "🕸️ GRAPHIFY (graph.json + GRAPH_REPORT.json) | Liens / structure / topologie",
        "chemin": "03_Resources_Geordi/00_Index/OKF_INDEX.md"
    },
    {
        "de": "DOX (CLAUDE.md canon)",
        "verbe": "consomme",
        "vers": "bundles OKF",
        "citation": "📜 DOX (CLAUDE.md racine + CC_Bare/CLAUDE.md) | Loi / contrat / comportement",
        "chemin": "03_Resources_Geordi/00_Index/OKF_INDEX.md"
    },
    {
        "de": "Geordi KB Root",
        "verbe": "délègue",
        "vers": "4 piliers canoniques (OKF/Wiki/Graphify/Dox)",
        "citation": "Geordi héberge **quatre piliers** (complémentaires et non redondants) + **un index utilitaire**",
        "chemin": "03_Resources_Geordi/00_Index/INDEX_OF_INDEXES.md"
    },
    {
        "de": "AMAdeus (A0)",
        "verbe": "fait",
        "vers": "CLARIFY + SCORE + ROUTE (3 phases)",
        "citation": "A0 (Amadeus) est le **Sparring Partner** d'A-Amadou (le Biologique). **A0 fait trois choses :** 1. **CLARIFY** — Transformer l'entropie brute en intention formulée (GTD : Capture → Clarify) 2. **SCORE** — Évaluer l'intention sur une grille multicritères 3. **ROUTE** — Dispatcher au bon Core avec un verdict et un contexte",
        "chemin": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/a0_reasoning_map.md"
    },
    {
        "de": "A0",
        "verbe": "NE FAIT JAMAIS",
        "vers": "concevoir, écrire du code, planifier des sprints, ajouter des couches",
        "citation": "**A0 ne fait JAMAIS :** - Concevoir des architectures (→ déléguer aux Docteurs A2) - Écrire du code ou des scripts (→ déléguer aux Compagnons A3) - Planifier des sprints (→ déléguer aux Governors A1) - Ajouter des couches au système (→ signal d'alerte : CONCEPTION DRIFT)",
        "chemin": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/a0_reasoning_map.md"
    },
    {
        "de": "Beth (Veto)",
        "verbe": "arrête",
        "vers": "Santé/Énergie négatif",
        "citation": "**Règle de Beth (Veto)** : Si ❤️ Santé/Énergie = Négatif → 🔴 STOP. Aucun score ne compense.",
        "chemin": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/a0_reasoning_map.md"
    },
    {
        "de": "E-Myth (A3 = Technicien)",
        "verbe": "rejette",
        "vers": "A-Amadou en Manager ou Technicien",
        "citation": "**Si A-Amadou apparaît dans Manager ou Technicien → 🔴 REJET AUTOMATIQUE.** > *Le Biologique ne descend pas en dessous du rôle Visionnaire.*",
        "chemin": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/a0_reasoning_map.md"
    },
    {
        "de": "ROADMAP DEAL 4 cycles",
        "verbe": "délègue",
        "vers": "PICARD → SUMMERS → 8 B2 → B3 SQUADS (cascade)",
        "citation": "PICARD (A3) 1 vision/cycle → décompose le cycle en 3 Rocks → SUMMERS (B1) 1 Rock/mois → traduit le Rock en directives par domaine → 8 B2 · 3T 4 Sprints/mois → chaque manager tient le sprint de son domaine → B3 SQUADS 5 Daily Scrums/sprint → exécution, receipts SQL",
        "chemin": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/ROADMAP_DEAL_12WY_2026-2027.md"
    },
    {
        "de": "5 Daily Scrums",
        "verbe": "produit",
        "vers": "1 sprint review → 4 sprints → 1 Rock review",
        "citation": "UPLINK 5 scrums → 1 sprint review → 4 sprints → 1 Rock review → 3 Rocks → 1 cycle review Picard → 4 cycles → bilan annuel",
        "chemin": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/ROADMAP_DEAL_12WY_2026-2027.md"
    },
    {
        "de": "ROADMAP Règle unique",
        "verbe": "exige",
        "vers": "chaque niveau ne remonte que du chiffré",
        "citation": "**Règle UNIQUE** **Chaque niveau ne remonte que du chiffré.** Un scrum sans receipt SQL n'existe pas. Un sprint sans delta MRR/pipeline n'existe pas. Un Rock sans métrique atteinte se re-scope au mois suivant — la cadence, elle, ne s'arrête jamais.",
        "chemin": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/ROADMAP_DEAL_12WY_2026-2027.md"
    },
    {
        "de": "OKF v0.1",
        "verbe": "consomme",
        "vers": "liens brisés et types inconnus (permissive)",
        "citation": "### 2.4 Consommation permissive - Liens brisés : tolérés (le wiki en a ~37 orphelines historiques). - Types inconnus : tolérés (un `type: MyCustomType` ne casse pas le parseur).",
        "chemin": "03_Resources_Geordi/00_Index/OKF_INDEX.md"
    },
    {
        "de": "Plugin Claude Code",
        "verbe": "REJETTE",
        "vers": "champ `agents` dans plugin.json",
        "citation": "**The `agents` Field: DO NOT ADD** > WARNING: **CRITICAL:** Do NOT add an `\"agents\"` field to `plugin.json`. The Claude Code plugin validator rejects it entirely.",
        "chemin": "03_Resources_Geordi/06_Claude_Code_Bare/PLUGIN_SCHEMA_NOTES.md"
    },
    {
        "de": "Plugin Claude Code v2.1+",
        "verbe": "auto-load",
        "vers": "hooks/hooks.json standard (interdit en manifest)",
        "citation": "Claude Code v2.1+ **automatically loads** `hooks/hooks.json` from any installed plugin by convention. If you also declare it in `plugin.json`, you get: `Duplicate hooks file detected: ./hooks/hooks.json resolves to already-loaded file.`",
        "chemin": "03_Resources_Geordi/06_Claude_Code_Bare/PLUGIN_SCHEMA_NOTES.md"
    },
    {
        "de": "mcpServers {} (empty)",
        "verbe": "prévient",
        "vers": "auto-loading ECC root .mcp.json dans Claude plugin install",
        "citation": "Keep this field in `.claude-plugin/plugin.json`: `\"mcpServers\": {}` - This explicit empty object prevents Claude plugin installs from auto-loading ECC's root MCP definitions. Without the opt-out, strict OpenAI-compatible gateways can reject plugin MCP tool names such as `mcp__plugin_everything-claude-code_github__create_pull_request_review` because they exceed 64 characters.",
        "chemin": "03_Resources_Geordi/06_Claude_Code_Bare/PLUGIN_SCHEMA_NOTES.md"
    },
    {
        "de": "Archetype Star Trek (PARA: USS Enterprise)",
        "verbe": "mappe",
        "vers": "PARA = Picard (P) / Spock (A) / Geordi (R) / Data (A Archives)",
        "citation": "**Doctrine Triptyque Imbrication (Russian Dolls par conception)** | **NIVEAU MID — PARA (USS Enterprise Computer, 4 lettres)** | - **P** | **Picard** (Captain USS Enterprise, MANIFEST.md owner) | - **A** | **Spock** (First Officer, ongoing responsibility doctrine) | - **R** | **Geordi** (Chief Engineer, reusable context-packs) | - **A** | **Data** (Second Officer, documentation-before-archive rule)",
        "chemin": "03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/hand_offs/architecture_triptyque_morty_2026-06-21.md"
    },
    {
        "de": "Data (A3 PARA Archives)",
        "verbe": "supervise",
        "vers": "Holo-Janeway A2 DEAL (chef d'orchestre)",
        "citation": "**Data = chef d'orchestre DEAL (clé du triptyque)** **Doctrine** : A3 Data (PARA Archives) supervise Holo-Janeway A2 DEAL. Quand un projet (Picard P) archive, Data déclenche Dal (DEAL Define) pour pattern detection, Rok-Tahk (DEAL Eliminate) pour NO-GO, Zero (DEAL Automate) pour skill canon, Gwyn (DEAL Liberate) pour D11 measurement.",
        "chemin": "03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/hand_offs/architecture_triptyque_morty_2026-06-21.md"
    },
    {
        "de": "Triptyque Morty",
        "verbe": "est le rail anti-paperclip pour",
        "vers": "Saru 1000T (Kardashev Type 3)",
        "citation": "**Doctrine ancrage** : le triptyque tient **par conception**, ce qui décharge Morty de GTD via Holodeck A2 USS Cerritos (cf. `cerritos_plane_integration_2026-06-21.md`). **Anti-paperclip Saru 1000T** : Saru LD02 Finance (A3 Discovery Zora) est supervisé par Book LD01 (H1 P&L). Le triptyque Morty est le **rail opérationnel** qui empêche Saru de dériver en paperclip maximizer (D3 nuance).",
        "chemin": "03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/hand_offs/architecture_triptyque_morty_2026-06-21.md"
    },
    {
        "de": "D11 Fable metric",
        "verbe": "owned by",
        "vers": "Chapel (A3 12WY Measure)",
        "citation": "**D11 Fable metric (Chapel ownership)** **Verbatim canon** : `chapel.twin.md:24-32` — \"D11 Fable metric OWNED by Chapel\". **Définition** : score de 0 à 100 mesurant l'écart entre « livrable fini » (Karpathy pillar) et « livrable inachevé » (sprint raté). Calcul = (rocks_done × 100) / rocks_planned.",
        "chemin": "03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/hand_offs/architecture_triptyque_morty_2026-06-21.md"
    },
    {
        "de": "D5 real-test-after-edit",
        "verbe": "owned by",
        "vers": "Ortegas (A3 12WY Execution)",
        "citation": "**D5 real-test-after-edit (Ortegas ownership)** **Verbatim canon** : `ortegas.twin.md:22-30` — \"D5 real-test-after-edit OWNED by Ortegas\". **Définition** : tout edit de code ou de config doit être suivi d'un test réel (build, curl, screenshot) AVANT de claim \"done\". Anti-pattern D5 = \"Sprint livré ✅\" sans preuve observable.",
        "chemin": "03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/hand_offs/architecture_triptyque_morty_2026-06-21.md"
    },
    {
        "de": "AaaS Sisters (Solaris/Nexus/Orbiter)",
        "verbe": "exploite uniquement",
        "vers": "marché américain (USA-only)",
        "citation": "**AaaS Sisters (Solaris / Nexus / Orbiter) = marché américain UNIQUEMENT. Pas Canada, pas UK, pas Europe, pas Francophonie.** Ratifié A+ 2026-07-22. Réversibilité : uniquement par nouvel ordre A+ explicite.",
        "chemin": "03_Resources_Geordi/04_From_V2_Root/wiki/hand_offs/2026-07-22_aaas_us_only_doctrine.md"
    },
    {
        "de": "AaaS Sisters",
        "verbe": "interdit (Banni)",
        "vers": "RGPD, CNIL, EU AI Act, GDPR, EU-specific compliance",
        "citation": "**Banni** : RGPD, CNIL, EU AI Act, GDPR, tout EU-specific compliance. Pas de mention dans messaging US.",
        "chemin": "03_Resources_Geordi/04_From_V2_Root/wiki/hand_offs/2026-07-22_aaas_us_only_doctrine.md"
    },
    {
        "de": "CCPA + state AI laws",
        "verbe": "apply",
        "vers": "USA (US-only AaaS)",
        "citation": "**Compliance US-only (drivers messaging)** | **Compliance** | **Application** | | CCPA (California) | Active 2020, amendements 2023-2024. Toutes opérations CA. | | Colorado AI Act (CO SB24-205) | Effective 2026-02-01. Premier state AI law US. Driver marketing Nexus. | | California SB 1047 | Vetoed 2024, revisité 2025-2026. Si repassed, apply. |",
        "chemin": "03_Resources_Geordi/04_From_V2_Root/wiki/hand_offs/2026-07-22_aaas_us_only_doctrine.md"
    },
    {
        "de": "SpecLoop Spec",
        "verbe": "rend possible",
        "vers": "exécuteur AVEUGLE reconstruit le comportement voulu",
        "citation": "Ce que le papier prouve : une spec est bonne **si et seulement si un exécuteur AVEUGLE peut reconstruire le comportement voulu à partir de la spec seule**, vérifié par équivalence formelle.",
        "chemin": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/INTEGRATION_CEOBENCH_SPECLOOP.md"
    },
    {
        "de": "CEO-BENCH E1 (non-vérifiable)",
        "verbe": "arrête",
        "vers": "directive sans métrique SQL observable",
        "citation": "**E.1** non-vérifiable | pas de métrique SQL observable pour la directive | STOP — la directive ne se dispatch pas tant qu'elle n'a pas de métrique | Picard",
        "chemin": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/INTEGRATION_CEOBENCH_SPECLOOP.md"
    },
    {
        "de": "CEO-BENCH E3 (mismatch fonctionnel)",
        "verbe": "amende",
        "vers": "Runbook (sur contreexemple)",
        "citation": "**E.3** tourne mais mismatch fonctionnel | le process s'exécute, la métrique diverge de la promesse | **contre-exemple** (le cas précis qui échoue) → amende le Runbook | B1 (Summers/Gstack)",
        "chemin": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/INTEGRATION_CEOBENCH_SPECLOOP.md"
    },
    {
        "de": "Roadmap MSQ 4 cycles",
        "verbe": "produit",
        "vers": "240 scrums (4 cycles × 12 Rocks × 4 sprints × 5 scrums)",
        "citation": "4 cycles. 12 Rocks. 48 sprints. 240 scrums. Départ : 20/07/2026. — A.S.",
        "chemin": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/ROADMAP_DEAL_12WY_2026-2027.md"
    },
    {
        "de": "Reverb Glissant (3 Rocks × 5 sprints \"reverb\")",
        "verbe": "est le seul mécanisme",
        "vers": "Roadmap autonomique",
        "citation": "**Fichier autonome, VPS-safe** : zéro import de doctrine, zéro gate, zéro flag. La cadence est le seul mécanisme.",
        "chemin": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/ROADMAP_DEAL_12WY_2026-2027.md"
    },
    {
        "de": "Wiki index.md",
        "verbe": "est le seul autorisé à porter",
        "vers": "okf_version: 0.1",
        "citation": "okf_version_rationale: P1.1 du plan maître — wiki/index.md est le seul index autorisé à porter okf_version.",
        "chemin": "03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/index.md"
    },
    {
        "de": "Loi du harvest (W22 M5, 2026-07-13)",
        "verbe": "exige",
        "vers": "page evergreen créée QUE depuis artefact shippé",
        "citation": "**Le wiki se récolte, ne s'écrit pas.** Une page evergreen (concepts/, entities/) n'est créée QUE depuis un artefact shippé (handoff, wargame exécuté, projet clos).",
        "chemin": "03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/index.md"
    },
    {
        "de": "wiki/index.md",
        "verbe": "jamais édité à la main",
        "vers": "(généré par gen_wiki_index.py)",
        "citation": "**Refresh** : `python 06_Claude_Code_Bare/bin/gen_wiki_index.py` régénère `wiki/index.md` (P2 du plan maître). Ne **jamais** éditer `wiki/index.md` à la main (cf. plan maître §10.5).",
        "chemin": "03_Resources_Geordi/00_Index/INDEX_OF_INDEXES.md"
    },
    {
        "de": "D7 cost-of-escalation",
        "verbe": "gating",
        "vers": "A0 board observer passif 6m-1y",
        "citation": "**D7 cost-of-escalation** : A0 = board observer passif. Ce spec doc = canon. A1 Morty supervise l'implémentation. A0 n'intervient QUE sur HITL gates listés §12.",
        "chemin": "03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/hand_offs/architecture_triptyque_morty_2026-06-21.md"
    },
    {
        "de": "EM Expansion Omnibus (Aquaman × Eternals)",
        "verbe": "sister canonique de",
        "vers": "ADR-LEGAL-001 (RATIFIED 2026-07-26)",
        "citation": "**★ Sister alignment tick** : `ADR-LEGAL-001` RATIFIED 2026-07-26 mapped Aquaman × Eternals → Domain 08 Legal H90 (CANONICAL ALIGNMENT ✓). This omnibus **extends** (does NOT supersede) `ADR-LEGAL-001` with **EXPANSION MODE Stones** — Rocks d'Amélioration Autonome Perpétuelle under Hermes-style Phase 2 doctrine.",
        "chemin": "03_Resources_Geordi/04_From_V2_Root/tmp/B2_Spec_Aquaman_Eternals_EXPANSION_2026-07-26.md"
    },
    {
        "de": "EM Expansion Aquaman X1",
        "verbe": "sister anchor",
        "vers": "ADR-OBSOLESCENCE-001 (RATIFIED 2026-07-26)",
        "citation": "**Sister anchor** : `ADR-OBSOLESCENCE-001` (RATIFIED 2026-07-26, obsolete-poisoned-degradation-audit) — X1 = Legal-domain specialization of that audit.",
        "chemin": "03_Resources_Geordi/04_From_V2_Root/tmp/B2_Spec_Aquaman_Eternals_EXPANSION_2026-07-26.md"
    },
    {
        "de": "EM Expansion GreenLantern X1",
        "verbe": "driven by",
        "vers": "Wolverine (B3 nano-squad, LEAD anti-drift)",
        "citation": "**X1 — Code archaeology sprint: dormant RH debt** **Purpose**: identify sleeping people/governance debt before it becomes poisoned doctrine or a zombie artifact. Wolverine leads the durability attack; Beast checks provenance; Professor X decides whether a finding is a scope issue; Rogue captures knowledge only with consent.",
        "chemin": "03_Resources_Geordi/04_From_V2_Root/tmp/B2_Spec_GreenLantern_XMen_EXPANSION_2026-07-26.md"
    },
    {
        "de": "EM Expansion GreenLantern X2",
        "verbe": "fait de",
        "vers": "RH meta-governance un working transverse bridge (pas People silo)",
        "citation": "**X2 — Cross-B2 routing perpetual cycle (H1 cross-cutting)** **Purpose**: make RH meta-governance a working transverse bridge rather than a People silo. Nightcrawler owns mobility; Cyclops turns the signal into a tactical packet; Storm watches pressure when multiple B2s are involved.",
        "chemin": "03_Resources_Geordi/04_From_V2_Root/tmp/B2_Spec_GreenLantern_XMen_EXPANSION_2026-07-26.md"
    },
    {
        "de": "EM Expansion Cognition X2",
        "verbe": "applique patch append-only",
        "vers": "ADR-OBSOLESCENCE-001 (ExpansionBudgetContract + CognitionScopeContract)",
        "citation": "**Rock X2 — ADR Patching cycle 2 : ExpansionBudgetContract + CognitionScopeContract** **Discipline** : D4 append-only patch to **`ADR-OBSOLESCENCE-001`** (NOT a new sister ADR). Append-only means adding new numbered sections `§X` to the existing body, never rewriting prior body.",
        "chemin": "03_Resources_Geordi/04_From_V2_Root/tmp/B2_Spec_Cognition_Illuminati_C2_EXPANSION_2026-07-26.md"
    },
    {
        "de": "EM Expansion Cognition X1",
        "verbe": "produit",
        "vers": "ADRs HEALTHY/OBSOLETE/POISONED/DRIFTED (verdict taxonomy)",
        "citation": "**Output** : `wiki/hand_offs/audits/2026-07/audit_obsolescence_mm_2026-07_audit_x1_cognition.md` — D4 ledger entry. Format follows `ADR-OBSOLESCENCE-001` §2.3 (`HEALTHY / OBSOLETE / POISONED / PENDING_RATIFY / DRIFTED` verdict taxonomy).",
        "chemin": "03_Resources_Geordi/04_From_V2_Root/tmp/B2_Spec_Cognition_Illuminati_C2_EXPANSION_2026-07-26.md"
    },
    {
        "de": "ADR-AGENT-BENCH-SCHEMA-001",
        "verbe": "fournit",
        "vers": "4 tables Supabase (agents, agent_souls, rh_sprints, gatekeeper_log)",
        "citation": "## Décision (D4 append-only) **Créer un schéma SQL canonique `agent_bench` dans Supabase Cloud** (sister ADR-OMK-001, ADR-OMK-004 pivot Supabase Cloud + Vercel) avec 4 tables :",
        "chemin": "03_Resources_Geordi/04_From_V2_Root/_DRAFTS_PPR_LANE/2026-07-25_rh_meta_gouvernance/ADR-AGENT-BENCH-SCHEMA-001_agent-bench-sql-canonique_PROPOSED.md"
    },
    {
        "de": "ADR-AGENT-BENCH-SCHEMA-001",
        "verbe": "exige",
        "vers": "SoUL versionné (1 active par agent, historique append-only)",
        "citation": "Chaque modification de SOUL crée une nouvelle version (`agent_souls`) et désactive l'ancienne. L'historique complet est conservé (D4 append-only). L'`agent.agents.soul_version` pointe vers la version active.",
        "chemin": "03_Resources_Geordi/04_From_V2_Root/_DRAFTS_PPR_LANE/2026-07-25_rh_meta_gouvernance/ADR-AGENT-BENCH-SCHEMA-001_agent-bench-sql-canonique_PROPOSED.md"
    },
    {
        "de": "Networking 3T OKF",
        "verbe": "is",
        "vers": "Geordi」として",
        "citation": "**Networking** | **Computer** | **Geordi**",
        "chemin": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/05_OSS_TSTwin/symphony/L1/INDEX_runtime.md"
    },
    {
        "de": "agent_bench.agents.status",
        "verbe": "transitions valid (state machine)",
        "vers": "BENCH → BUILDING → ACTIVE → PAUSED/DEPRECATED",
        "citation": "**Lifecycle state machine** ``` [ CREATION ] │ ▼ [ BENCH ] ─────► [ BUILDING ] ─────► [ ACTIVE ] │                  │ │                  ▼ │              [ PAUSED ] │                  │ │                  ▼ ▼                  ▼ [ DEPRECATED ] ◄───────┘",
        "chemin": "03_Resources_Geordi/04_From_V2_Root/_DRAFTS_PPR_LANE/2026-07-25_rh_meta_gouvernance/ADR-AGENT-BENCH-SCHEMA-001_agent-bench-sql-canonique_PROPOSED.md"
    },
    {
        "de": "B1 Jerry Prime",
        "verbe": "lit l'INDEX",
        "vers": "01_Product, 02_Ops, ..., 08_People",
        "citation": "**B1 owner** : Jerry Prime lit cette INDEX sur chaque intention Product → route B2 Flash ou downstream B3 Captain America / Iron Man / Thor / Hulk / Black Widow / Hawkeye / Scarlet Witch.",
        "chemin": "03_Resources_Geordi/01_Guides/01_Product/_INDEX.md"
    },
    {
        "de": "B1-filter pain-point (D6 2026-07-03)",
        "verbe": "exige",
        "vers": "sister_b1 + ld_owner dans chaque frontmatter",
        "citation": "YouTube distils ingested sans `b1_filter:` → LD mapping aléatoire. **Action gated Picard A3** : appendre `sister_b1: jerry-prime` + `ld_owner: Tilly` dans chaque frontmatter. **Permanent fix** : amendement `/youtube-to-guide` §6 pour exiger `b1_filter:`.",
        "chemin": "03_Resources_Geordi/01_Guides/01_Product/_INDEX.md"
    },
    {
        "de": "ADR-AAAS-ACQUISITION-DOCTRINE-001",
        "verbe": "ancre",
        "vers": "guides MedVie et Mobbin (via 01_Product, 07_Growth)",
        "citation": "**Insight canon** : Le guide MedVie **valide rétroactivement** la thèse AaaS Solarpunk (`ADR-L2-AAAS-001` Pilier 3 Sobriété) que l'agent-as-a-service asset-light + bootstrap-friendly + acquisition triple-canal est **supérieur au SaaS** pour les business de service réglementés (MedVie : 16,2% marge vs concurrents 5,5%).",
        "chemin": "03_Resources_Geordi/01_Guides/07_Growth/_INDEX.md"
    },
    {
        "de": "B1 filter (Picard A3)",
        "verbe": "corrige",
        "vers": "LD misalignment (_kIxjlEf_0U.md)",
        "citation": "**Fix** (action D7 low-stakes) : Picard A3 (`b3-enterprise-picard`) lit le frontmatter + 1ère section, **fixe le champ `ld`** au canon LD01_Business (qui mappe B2 Sales ↔ B1 Jerry), et appende `sister_b1: jerry-prime` au frontmatter.",
        "chemin": "03_Resources_Geordi/01_Guides/06_Sales/_INDEX.md"
    },
    {
        "de": "Granola coach-meta (Shubham Sharma)",
        "verbe": "sister canon",
        "vers": "b2-01-greenlantern-people × b3-1-professor-x × state_writer.py",
        "citation": "**Insight persistant** : le pattern Granola (transcription live + IA coach + recettes marketplace + MCP externe) est **exactement** l'architecture de `b2-01-greenlantern-people` × `b3-1-professor-x` × `state_writer.py` (symphony supabase U1).",
        "chemin": "03_Resources_Geordi/01_Guides/08_People/_INDEX.md"
    },
    {
        "de": "AI-Act 2026-08-02",
        "verbe": "est gate pour",
        "vers": "b3-8-ikaris (Legal)",
        "citation": "**⚡ AI-Act 2026-08-02 driver** D1 receipt 2026-06-21 (cf. CLAUDE.md §Stories + docs) : **AI-Act 2026-08-02 driver** = hard priority for `b3-8-ikaris`. Tout guide 05_Legal doit lister son `ai_act_clause:` dans frontmatter.",
        "chemin": "03_Resources_Geordi/01_Guides/05_Legal/_INDEX.md"
    },
    {
        "de": "AMAdeus (A0)",
        "verbe": "est gatekeeper de",
        "vers": "A0 Reasoning Map (filtre de la Méta-Conscience)",
        "citation": "**Règle Zero :** Ce document est un OUTIL, pas un manifeste. Si tu es en train de le modifier au lieu de l'utiliser, A0 a échoué.",
        "chemin": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/a0_reasoning_map.md"
    },
    {
        "de": "FRACTAL CREEP (signal d'alerte #2)",
        "verbe": "détection",
        "vers": "Ajout d'un nouvel agent/rôle/constitution",
        "citation": "**2** | **FRACTAL CREEP** | Ajout d'un nouvel agent/rôle/constitution | \"Le système a assez d'agents. Lequel existant peut porter ça ?\"",
        "chemin": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/a0_reasoning_map.md"
    },
    {
        "de": "TOOL HOARDING (signal d'alerte #3)",
        "verbe": "détection",
        "vers": "Évaluation d'un 4ème outil pour le même besoin",
        "citation": "**3** | **TOOL HOARDING** | Évaluation d'un 4ème outil pour le même besoin | \"Choisis et engage. L'outil parfait n'existe pas.\"",
        "chemin": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/a0_reasoning_map.md"
    },
    {
        "de": "HORIZON ESCAPE (signal d'alerte #4)",
        "verbe": "détection",
        "vers": "Discussion H90 sans ancrage H1",
        "citation": "**4** | **HORIZON ESCAPE** | Discussion H90 sans ancrage H1 | \"Magnifique vision. Quel est le premier livrable dans 7 jours ?\"",
        "chemin": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/a0_reasoning_map.md"
    },
    {
        "de": "ROLE COLLAPSE (signal d'alerte #5)",
        "verbe": "détection",
        "vers": "A-Amadou fait du travail A2/A3",
        "citation": "**5** | **ROLE COLLAPSE** | A-Amadou fait du travail A2/A3 | \"Tu es le Visionnaire. Qui est le Technicien ici ?\"",
        "chemin": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/a0_reasoning_map.md"
    },
    {
        "de": "D4 no-hard-delete",
        "verbe": "exige",
        "vers": "Retirements via _TRASH_<date>/",
        "citation": "**D4** : Tous les outputs sont append-only (D4 no-self-contradiction). Retirements via `_TRASH_<date>/`.",
        "chemin": "03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/hand_offs/architecture_triptyque_morty_2026-06-21.md"
    },
    {
        "de": "SECOND_BRAIN_PARA_MAP.md",
        "verbe": "répartit",
        "vers": "14 sous-dossiers -> 4 buckets PARA + 5 strates S0-S4",
        "citation": "Geordi héberge **14 sous-dossiers** (complémentaires et non redondants) + **un index utilitaire** ... | **📚 RESOURCES_INDEX** | « Où est-ce que c'est ? Quel fichier pour tel besoin ? » | Table Markdown | `00_Index/RESOURCES_INDEX.md`",
        "chemin": "03_Resources_Geordi/00_Index/SECOND_BRAIN_PARA_MAP.md"
    },
    {
        "de": "JD Kerr Looping (D2)",
        "verbe": "détection",
        "vers": "Auto-archive (ex-LD Life OS rang entraidage)",
        "citation": "**📚 Guides (5 files · D1 2026-07-03 — squelette minimum)** | File | Topic | Status |",
        "chemin": "03_Resources_Geordi/01_Guides/05_Legal/_INDEX.md"
    },
    {
        "de": "Patrick (B3-Tilly)",
        "verbe": "owned by",
        "vers": "b3-4-tilly (LD04)",
        "citation": "(non measurable directement; régression à mentionner)",
        "chemin": "03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/index.md"
    }
]

# NEW CODES — systems numbered in v4 reads
v4["codes"] = [
    {
        "systeme": "S0-S4 (Strates mémoire)",
        "numerote": "S0 Identité · S1 Court terme (hand_offs, daily notes) · S2 Travail (_CAPTURE, _INTAKE) · S3 Long terme (Guides, Templates, L0, concepts) · S4 Méta (Index, wiki/index, ROT)",
        "defini_dans": "03_Resources_Geordi/00_Index/SECOND_BRAIN_PARA_MAP.md"
    },
    {
        "systeme": "OKF v0.1 (champs frontmatter)",
        "numerote": "type (seul REQUIS) · title · description · resource · tags · timestamp · okf_version (RÉSERVÉ) · source · date · domain · metadata.*",
        "defini_dans": "03_Resources_Geordi/00_Index/OKF_INDEX.md"
    },
    {
        "systeme": "T0-T2 (Tier Enterprise OS)",
        "numerote": "T0 Hobby (solo operator) · T1 Standard (firm, ~$65-95/mo) · T2 Pro (PHI, HIPAA-grade)",
        "defini_dans": "03_Resources_Geordi/02_Templates/Enterprise_OS_Blueprint_Kit/specs/ARCHITECTURE_SPEC.md"
    },
    {
        "systeme": "P1-P12 (Principles Yann Leonardi 12P)",
        "numerote": "Principes P1 (Product-moteur) à P12 (Fail Fast) — la bibliothèque Yann Leonardi mappe chaque ressource à des principes + score confiance (HIGH/MEDIUM/LOW/FALLBACK)",
        "defini_dans": "03_Resources_Geordi/01_Guides/07_Growth/Yann_Leonardi/INDEX_QA_REPORT.md"
    },
    {
        "systeme": "V0.X.Y (Life Web OS versioning)",
        "numerote": "V0.2 Micro · V0.3 Engine Room · V0.4 Enterprise Computer · V0.5 Sovereign Constitution · V0.6 Temporal Engine · V0.7 Cerritos Tactical Deck · V0.8 Protostar Spacedock · V0.9 Nexus Convergence (en cours). X = itération majeure (SDD), Y = sous-itération (PRD/ADR/DDD)",
        "defini_dans": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/Life_Reality_map.md"
    },
    {
        "systeme": "SOA 01-08 (8 Business Domains AaaS)",
        "numerote": "01 Growth · 02 Sales · 03 Product · 04 Ops · 05 IT · 06 Finance · 07 People · 08 Legal — bijection 8 ↔ 8 LDxx (axe LD01 = Operation/Batman/F4)",
        "defini_dans": "03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/99_meta/doctrine_lock_map.md"
    },
    {
        "systeme": "EXPANSION Rocks X1-X3 (Domain 08 Legal)",
        "numerote": "X1 Code archaeology sprint (Legal-debt dormant + AI-Act compliance gaps) · X2 AI-Act 2026-08-02 perpetual countdown + gate enforcement · X3 Phase 2 Hermes friction → compliance-grade skill canonique",
        "defini_dans": "03_Resources_Geordi/04_From_V2_Root/tmp/B2_Spec_Aquaman_Eternals_EXPANSION_2026-07-26.md"
    },
    {
        "systeme": "EXPANSION Rocks X1-X3 (Domain 01 RH)",
        "numerote": "X1 Code archaeology sprint (dormant RH debt) · X2 Cross-B2 routing perpetual cycle (H1 cross-cutting) · X3 Phase 2 Hermes friction → skill canon auto-creation",
        "defini_dans": "03_Resources_Geordi/04_From_V2_Root/tmp/B2_Spec_GreenLantern_XMen_EXPANSION_2026-07-26.md"
    },
    {
        "systeme": "EXPANSION Rocks X1-X4 (Domain 04 Cognition cycle 2)",
        "numerote": "X1 Code archaeology cycle 2 · X2 ADR Patching cycle 2 (ExpansionBudgetContract + CognitionScopeContract) · X3 Skill auto-création Phase 2 Hermes · X4 Sister Git Zéro Phase 1 audit",
        "defini_dans": "03_Resources_Geordi/04_From_V2_Root/tmp/B2_Spec_Cognition_Illuminati_C2_EXPANSION_2026-07-26.md"
    },
    {
        "systeme": "5 Daily Scrums (B3 Daily Scrum)",
        "numerote": "1. Lire l'état (requête SQL) · 2. 1 action de conversion · 3. 1 action de système · 4. Receipt (delta SQL) · 5. Uplink 1 ligne",
        "defini_dans": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/ROADMAP_DEAL_12WY_2026-2027.md"
    },
    {
        "systeme": "C1-C11 (CEO-BENCH composants)",
        "numerote": "C1 memory_<domaine>.md refresh hebdo · C2 mémo if-then ≥5/sem · C3 forecast cash J+28 chaque lundi · C4 6 tables SQL (ledger, subscriptions, pipeline, outreach_log, issues, experiments) · C5 daily_cash vue · C6 budget découverte · C7 spending 90% ciblé · C8 mapping 8 actions↔8 B2 · C9 détection concurrent 1 sem · C10 turns/sem · C11 monde non-stationnaire",
        "defini_dans": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/INTEGRATION_CEOBENCH_SPECLOOP.md"
    },
    {
        "systeme": "S1-S7 (SpecLoop composants)",
        "numerote": "S1 3 rôles (Générateur/Reconstructeur/Verifyateur) · S2 information hiding · S3 taxonomie E.1-E.4 · S4 contre-exemple > pass/fail · S5 format spec structuré · S6 budget retry · S7 RR-Score reconstruction",
        "defini_dans": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/INTEGRATION_CEOBENCH_SPECLOOP.md"
    },
    {
        "systeme": "E.1-E.4 (Spécleop erreurs taxonomie)",
        "numerote": "E.1 non-vérifiable · E.2 ne compile pas · E.3 tourne mais mismatch · E.4 inconclusif",
        "defini_dans": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/INTEGRATION_CEOBENCH_SPECLOOP.md"
    },
    {
        "systeme": "8 domaines AaaS Solarpunk (re-cast)",
        "numerote": "01 Growth (Superman/Guardians) · 02 Sales (JohnJones/Illuminati) · 03 Product (Flash/Avengers) · 04 Cognition (J'onn/Illuminati) · 05 Ops (Batman/F4) · 06 Finance (WonderWoman/Thunderbolts) · 07 People (GreenLantern/X-Men) · 08 Legal (Aquaman/Eternals)",
        "defini_dans": "03_Resources_Geordi/04_From_V2_Root/tmp/B2_Spec_Cognition_Illuminati_C2_EXPANSION_2026-07-26.md"
    },
    {
        "systeme": "Twin.md (Lane A Specs)",
        "numerote": "A1 Gatekeepers (2) · A2 Ships (6) · A3 Crews (35) — Lane A du Symphony L1",
        "defini_dans": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/05_OSS_TSTwin/symphony/L1/INDEX_specs.md"
    },
    {
        "systeme": "LD01-LD08 (Life Wheel)",
        "numerote": "LD01 Career & Business · LD02 Finance · LD03 Health · LD04 Cognition · LD05 Relations · LD06 Habitat · LD07 Creativity · LD08 Impact",
        "defini_dans": "03_Resources_Geordi/03_Memory_Unified/LLM_Wiki/wiki/index.md"
    },
    {
        "systeme": "App ID (Life OS apps)",
        "numerote": "command-center, para, ikigai, life-wheel, twelve-week, gtd, deal, agent-portal, store, settings — kebab-case",
        "defini_dans": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/Life_Reality_map.md"
    },
    {
        "systeme": "5 Signaux d'alerte A0",
        "numerote": "1 CONCEPTION DRIFT · 2 FRACTAL CREEP · 3 TOOL HOARDING · 4 HORIZON ESCAPE · 5 ROLE COLLAPSE",
        "defini_dans": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/a0_reasoning_map.md"
    },
    {
        "systeme": "Antifragility Triangle (Ikigai × Life Wheel × Faisabilité OS)",
        "numerote": "🟢 PASS · 🟡 INCUBER · 🔴 KILL (calcul = Ikigai H1/H3 ≥ 3/5 + Life Wheel net positif + Faisabilité OS ≥ 3/5 + E-Myth clean)",
        "defini_dans": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/a0_reasoning_map.md"
    },
    {
        "systeme": "8-conditionnelles X-Men Coach (Domain 04 cycle 1)",
        "numerote": "Wolverine SHA256 ledger · Beast embed factorisation · Storm weather cadence · Xavier mentalist trust-tier · Strange re-ranker fallback + 3 autres",
        "defini_dans": "03_Resources_Geordi/04_From_V2_Root/tmp/B2_Spec_Cognition_Illuminati_C2_EXPANSION_2026-07-26.md"
    },
    {
        "systeme": "État machine agent_bench.status",
        "numerote": "BENCH → BUILDING → ACTIVE → PAUSED → DEPRECATED",
        "defini_dans": "03_Resources_Geordi/04_From_V2_Root/_DRAFTS_PPR_LANE/2026-07-25_rh_meta_gouvernance/ADR-AGENT-BENCH-SCHEMA-001_agent-bench-sql-canonique_PROPOSED.md"
    }
]

# NEW CONTRADICTIONS — found via v4 reads (could signal a debt to flag)
v4["contradictions"] = [
    {
        "sujet": "L2 Business Domain 'Sales' vs 'Cognition' — J'onn × Illuminati canon mismatch",
        "chemin_a": "03_Resources_Geordi/04_From_V2_Root/tmp/B2_Spec_Cognition_Illuminati_C2_EXPANSION_2026-07-26.md",
        "date_a": "2026-07-26",
        "citation_a": "**D6 canon mismatch flag preserved** : canon maps J'onn × Illuminati → Sales, brief directive → Cognition (declaration per §0 `ADR-COGNITION-001` abort_conditions).",
        "chemin_b": "03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/99_meta/doctrine_lock_map.md",
        "date_b": "2026-07-04",
        "citation_b": "**Runtime agent cards D1 verified** : `b3-5-black-bolt.md`, `b3-5-tony-stark.md`, `b3-5-reed-richards.md`, `b3-5-namor.md`, `b3-5-charles-xavier.md`, `b3-5-stephen-strange.md`. Runtime J'onn runtime agent file is `b2-05-johnjones-sales.md` (not `b2-04-johnjones-cognition.md` — D6 mismatch, flag preserved)."
    },
    {
        "sujet": "AI-Act 2026-08-02 — rock 1 status closure non documenté",
        "chemin_a": "03_Resources_Geordi/04_From_V2_Root/tmp/B2_Spec_Aquaman_Eternals_EXPANSION_2026-07-26.md",
        "date_a": "2026-07-26",
        "citation_a": "**D6 #NEW-2 (AI-Act countdown T-7 days, Rock 1 status not formally CLOSED)** — as of 2026-07-26 (T-7), Rock 1 (W1-W4) should be CLOSED. No formal `rock1_closure_<DATE>.md` in canon detected.",
        "chemin_b": "03_Resources_Geordi/01_Guides/05_Legal/_INDEX.md",
        "date_b": "2026-07-03",
        "citation_b": "**⚡ AI-Act 2026-08-02 driver** D1 receipt 2026-06-21 (cf. CLAUDE.md §Stories + docs) : **AI-Act 2026-08-02 driver** = hard priority for `b3-8-ikaris`."
    },
    {
        "sujet": "Volumes Geordi mesurés — 14 951 → 14 613 (04_From_V2_Root) ; 17 589 → 8 094 (05_From_V2_Domains)",
        "chemin_a": "03_Resources_Geordi/00_Index/SECOND_BRAIN_PARA_MAP.md",
        "date_a": "2026-08-02",
        "citation_a": "**Total recalculé à **48 221**. Source `JUNCTIONS_MAP_2026-08-02.md` ajoutee. Aucune décision architecturale changee ; les 4 decisions D-2026-08-01-#1..4 sont conservees telles quelles.",
        "chemin_b": "03_Resources_Geordi/00_Index/SECOND_BRAIN_PARA_MAP.md",
        "date_b": "2026-08-01",
        "citation_b": "**Volumes corrigés** (`04_From_V2_Root` 14 951 → 14 613 ; `05_From_V2_Domains` 17 589 → 8 094 — mesure 2026-08-02 jonctions exclues, realpath dedup)."
    },
    {
        "sujet": "LD01 Book doctrine — H1 vs H10 horizon (Book canon H1, mais 'horizon H10' attribution also seen)",
        "chemin_a": "03_Resources_Geordi/05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/00_index.md",
        "date_a": "2026-07-04",
        "citation_a": "**Horizon canon** : **H1 Weekly P&L** — PAS H10. Verrouillé par `symphony/L1/lane_A_specs/03_A3_crews/discovery/book.twin.md`",
        "chemin_b": "03_Resources_Geordi/04_From_V2_Root/tmp/B2_Spec_GreenLantern_XMen_EXPANSION_2026-07-26.md",
        "date_b": "2026-07-26",
        "citation_b": "**H10**: people culture review; B3 SOUL/spec review; BENCH → BUILDING → ACTIVE recommendations; cross-B2 routing and Rock preparation."
    },
    {
        "sujet": "Doctrine B1 (LD01) → Strategy B2 — owner mapping (Growth/LD08 vs Business/LD01)",
        "chemin_a": "03_Resources_Geordi/01_Guides/07_Growth/_INDEX.md",
        "date_a": "2026-07-03",
        "citation_a": "mapping B1 Jerry, B2 Superman, B3 Guardians",
        "chemin_b": "03_Resources_Geordi/01_Guides/07_Growth/Yann_Leonardi/INDEX_QA_REPORT.md",
        "date_b": "2026 (sweep)",
        "citation_b": "ld: LD08_Impact_Georgiou"
    },
    {
        "sujet": "OAaS Pricing — 5 tiers USD vs 6 tables Supabase",
        "chemin_a": "03_Resources_Geordi/01_Guides/04_Finance/_INDEX.md",
        "date_a": "2026-07-03",
        "citation_a": "ADR-AAAS-PRICING-001 (5 Tiers USD, RATIFIED + AMENDED 2026-06-24)",
        "chemin_b": "03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/INTEGRATION_CEOBENCH_SPECLOOP.md",
        "date_b": "2026-07-19",
        "citation_b": "6 tables Supabase (ledger, subscriptions, pipeline, outreach_log, issues, experiments)"
    },
    {
        "sujet": "Carter de principes INDEX — 5 sub-types persona vs 7 KPIs canon",
        "chemin_a": "03_Resources_Geordi/01_Guides/02_Ops/_INDEX.md",
        "date_a": "2026-07-03",
        "citation_a": "**Guide BI-MNjm1tTQ** (22 708 chars) couvre les **5 sub-types persona** Structuration-First canon",
        "chemin_b": "03_Resources_Geordi/01_Guides/02_Ops/_INDEX.md",
        "date_b": "2026-07-03",
        "citation_b": "**Guide tov_Xe5xZmU** (20 529 chars, ProcessDriven) ancre les **7 KPIs canon** + Manual Reporting Ritual anti-pattern"
    },
    {
        "sujet": "Driver B1 — Geordi vs Quantum LD04 driver",
        "chemin_a": "03_Resources_Geordi/01_Guides/01_Product/_INDEX.md",
        "date_a": "2026-07-03",
        "citation_a": "**Domaine** : Product / Roadmap / UX / Spec / Founder-grade (LD04_Cognition_Tilly mirror via B1 Jerry, B2 Flash, B3 Avengers).",
        "chemin_b": "03_Resources_Geordi/01_Guides/04_Finance/_INDEX.md",
        "date_b": "2026-07-03",
        "citation_b": "**Domaine** : Finance / Unit Economics / Runway / Pricing / Token Plan (LD02_Finance_Saru mirror via B1 Jerry, B2 Wonder Woman, B3 Thunderbolts)."
    },
    {
        "sujet": "Repetition YAML frontmatter — b1_filter / b2_owner / sister_b1 patterns",
        "chemin_a": "03_Resources_Geordi/01_Guides/07_Growth/_INDEX.md",
        "date_a": "2026-07-03",
        "citation_a": "**B1 owner** : Jerry Prime lit cette INDEX sur chaque intention Growth → route B2 Superman → B3 Star Lord (top funnel, brand narrative).",
        "chemin_b": "03_Resources_Geordi/01_Guides/06_Sales/_INDEX.md",
        "date_b": "2026-07-03",
        "citation_b": "**B1 owner** : Jerry Prime (LD01 Career/Business meta-orchestrator) reads this INDEX on every sales-related A0 intent → routes to B2 JohnJones or downstream B3."
    }
]

# Write output
out_json = CWD / "03_Resources_Geordi_v4.json"
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(v4, f, indent=2, ensure_ascii=False)

print(f'Wrote {out_json}')
print(f'  types: {len(v4["types"])}')
print(f'  relations: {len(v4["relations"])}')
print(f'  codes: {len(v4["codes"])}')
print(f'  contradictions: {len(v4["contradictions"])}')
