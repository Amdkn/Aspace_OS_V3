"""Generate 03_Resources_Geordi_v3.json + .md with all observed types, relations, codes, contradictions."""
import json, os

CARTO = r"C:\Users\amado\ASpace_OS_V3\00_Amadeus\30_MEMORY_CORE\carto"
BASE = r"C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi"

v3 = {
    "seau": "03_Resources_Geordi",
    "fichiers_lus": 935,
    "fichiers_disponibles": 1826,
    "jonctions_ecartees": 832,
    "types": [],
    "relations": [],
    "codes": [],
    "contradictions": []
}

# Helper for paths
def P(rel): return "03_Resources_Geordi/" + rel.replace("\\","/").lstrip("/")

# === TYPES ===
v3["types"] = [
    {
        "nom": "ADR (Architectural Decision Record)",
        "attributs": ["id (slug)", "title", "status (DRAFT|PROPOSED|ACCEPTED|RATIFIED|RADIE)", "date", "doctrine_anchors[]", "sister_canon[]", "supersedes_scope", "deciders[]", "provenance", "sign_off_a0", "ratification_log"],
        "chemins": [
            P("04_From_V2_Root/_SPECS/ADR/INDEX.md"),
            P("04_From_V2_Root/_SPECS/ADR/L0_Kernel_OS/ADR-SOBER-002_anti-paperclip-maximizer-doctrine.md"),
            P("04_From_V2_Root/_SPECS/ADR/L0_Kernel_OS/ADR-META-006_droid-whispering-doctrine.md"),
            P("04_From_V2_Root/_SPECS/ADR/L0_Tech_OS/ADR-EXTRA-PPR-001_preventive-construction-doctrine.md"),
            P("04_From_V2_Root/_SPECS/ADR/L0_Tech_OS/ADR-LOOP-001_canon-loop-verification-first.md"),
            P("04_From_V2_Root/_SPECS/ADR/L0_Tech_OS/ADR-MCP-PLUGIN-001_supabase-canonical-OFF.md"),
            P("04_From_V2_Root/_SPECS/ADR/L1_Life_OS/ADR-INFRA-005_idb-singleton-doctrine.md"),
            P("04_From_V2_Root/_SPECS/ADR/L1_Life_OS/ADR-INFRA-006_hydrate-aggregate-8-lds-doctrine.md"),
            P("04_From_V2_Root/_SPECS/ADR/L1_Life_OS/ADR-LIFE-015_mission-control-ui-canon.md"),
            P("04_From_V2_Root/_SPECS/ADR/L1_Life_OS/ADR-MEM-001_memory-fabric-unified-doctrine.md"),
            P("04_From_V2_Root/_SPECS/ADR/L1_Life_OS/ADR-MEM-002_wiki-lifewheel-mapping-doctrine.md"),
            P("04_From_V2_Root/_SPECS/ADR/L1_Life_OS/ADR-META-003_model-agnostic-runtime-doctrine.md"),
            P("04_From_V2_Root/_SPECS/ADR/L1_Life_OS/ADR-META-004_doctrine-anti-paresse-linkage.md"),
            P("04_From_V2_Root/_SPECS/ADR/L1_Life_OS/ADR-Meta-000_12-week-year-cycle-doctrine_DRAFT.md"),
            P("04_From_V2_Root/_SPECS/ADR/L1_Life_OS/ADR-OBSERVABILITY-001_sessions-canon-md-rotation.md"),
            P("04_From_V2_Root/_SPECS/ADR/L1_Life_OS/ADR-RITUAL-001_slashcommand-canon-library_PROPOSED.md"),
            P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-ACQUISITION-DOCTRINE-001_aaas-acquisition-doctrine.md"),
            P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-CONTENT-CANON-001_aaas-content-canon.md"),
            P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-FINANCE-CANON-001_aaas-finance-canon.md"),
            P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-IT-CANON-001_aaas-it-canon.md"),
            P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-IT-EXT-CANON-001_aaas-it-ext-canon.md"),
            P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-OPERATIONS-CANON-001_aaas-operations-canon.md"),
            P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-001_aaas-pricing-canon.md"),
            P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-CANON-001_roster-source-of-truth.md"),
            P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-CANON-002_RHA-Workflow_W20-M5.md"),
            P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md"),
            P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-KARDASHEV-TYPE-FRACTAL-001_multiverse-architecture_RATIFIED_2026-07-16.md"),
            P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-NAMING-CONVENTION-001_session-canon_RATIFIED_2026-07-15.md"),
            P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-PAPERCLIPAI-001_governance-mirror-doctrine.md"),
            P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-PAPERCLIPAI-002_anti-paperclip-irony-doctrine.md"),
            P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-PAPERCLIPAI-003_paperclip-delegation-not-creation-doctrine.md"),
            P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-PAPERCLIPAI-004_paperclip-calibration-doctrine_RATIFIED_2026-07-16.md"),
            P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-LANDING-AESTHETIC-001_doctrine-esthetique.md"),
            P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-LANDING-COPY-001_doctrine-copywriting.md"),
            P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-NEXUS-10-ICP-001_3-strates-10-cibles-canon.md"),
            P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-OPS-009_worker-git-commit-doctrine.md"),
            P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-RH-META-GOUVERNANCE-001-canonical-v2_PROPOSED_2026-07-25.md"),
            P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-RH-META-GOUVERNANCE-001-canonical-v3_RATIFIED_2026-07-26.md"),
            P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-SKILLS-CANON-001_inventory-skills-landing.md"),
            P("04_From_V2_Root/_SPECS/ADR/META_Organization/ADR-AGENTIC-ARCH-001_fareedkhan-architectures-integration-RATIFIED_2026-07-26.md"),
            P("04_From_V2_Root/_SPECS/ADR/META_Organization/ADR-AGENTIC-LONG-HORIZON-001_3-long-horizon-doctrines-integration-RATIFIED_2026-07-26.md"),
            P("04_From_V2_Root/_DRAFTS_PPR_LANE/2026-07-25_rh_meta_gouvernance/ADR-AGENT-BENCH-SCHEMA-001_agent-bench-sql-canonique_PROPOSED.md"),
            P("04_From_V2_Root/wiki/hand_offs/2026-07-22_aaas_us_only_doctrine.md"),
            P("05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-FWK-021_blueprints-canon-tripartite.md"),
            P("05_From_V2_Domains/30_Business_OS/09_Blueprints/02-ADR/ADR-MESH-L2-001_tri-plateforme-doctrine.md")
        ]
    },
    {
        "nom": "RUNBOOK (cycle-1 runbook with SQL objective)",
        "attributs": ["Objectif (métrique SQL)", "Entrées", "Sorties (deltas attendus)", "Procédure (S1-S4)", "Cadence (4 sprints × 5 scrums)", "Notes (cas limites)", "Amendement (date + §)"],
        "chemins": [
            P("05_From_V2_Domains/00_Amadeus/sob/RUNBOOK_C1-R1.md"),
            P("05_From_V2_Domains/00_Amadeus/sob/RUNBOOK_C1-R2.md"),
            P("05_From_V2_Domains/00_Amadeus/sob/RUNBOOK_C1-R3.md"),
            P("05_From_V2_Domains/30_Business_OS/10_Projects/omk/runbooks/runbook-coach-premium-capsule.md")
        ]
    },
    {
        "nom": "MANIFEST (project/agent manifest)",
        "attributs": ["type: MANIFEST", "wargame", "slug", "id", "date", "deciders[]", "parent_dox[]", "sister", "domain", "tags[]", "war_mode", "append_only", "granularity", "self_grade"],
        "chemins": [
            P("05_From_V2_Domains/30_Business_OS/10_Projects/omk/MANIFEST.md"),
            P("05_From_V2_Domains/30_Business_OS/10_Projects/omk/MANIFEST_coaching_premium.md"),
            P("05_From_V2_Domains/30_Business_OS/10_Projects/ceo-desktop/MANIFEST.md"),
            P("05_From_V2_Domains/30_Business_OS/10_Projects/cerritos-gtd-dispatch/MANIFEST.md"),
            P("05_From_V2_Domains/30_Business_OS/10_Projects/abc/MANIFEST.md"),
            P("05_From_V2_Domains/30_Business_OS/10_Projects/rilcot/MANIFEST.md"),
            P("05_From_V2_Domains/30_Business_OS/10_Projects/solaris/MANIFEST.md"),
            P("05_From_V2_Domains/30_Business_OS/10_Projects/wargames/wargame-30-out/MANIFEST_Triptyque_1_BusinessOS.md")
        ]
    },
    {
        "nom": "SCHEMA (canonique)",
        "attributs": ["Path canon", "Rôle", "Champs + types + descriptions", "Loi lock atomique", "Anti-patterns"],
        "chemins": [
            P("05_From_V2_Domains/00_Amadeus/40_SYMPHONY_BUS/SCHEMA.md"),
            P("05_From_V2_Domains/30_Business_OS/00_Summers_Verse/state/SCHEMA.md"),
            P("03_Memory_Unified/LLM_Wiki/wiki/schema.md"),
            P("03_Memory_Unified/LLM_Wiki/wiki/Shadow_L0/SPEC.md"),
            P("03_Memory_Unified/LLM_Wiki/wiki/Shadow_L1/SPEC.md"),
            P("03_Memory_Unified/LLM_Wiki/wiki/Shadow_L2/SPEC.md"),
            P("06_Claude_Code_Bare/PLUGIN_SCHEMA_NOTES.md")
        ]
    },
    {
        "nom": "ARCHITECTURE_SPEC (canonique enterprise)",
        "attributs": ["Design principles", "Secure-substitute map", "Data flow (one account)", "Stacks in dependency order", "Key decisions and tradeoffs"],
        "chemins": [
            P("02_Templates/Enterprise_OS_Blueprint_Kit/specs/ARCHITECTURE_SPEC.md"),
            P("02_Templates/Enterprise_OS_Blueprint_Kit/specs/architecture_spec_omk_nexus.md"),
            P("02_Templates/Enterprise_OS_Blueprint_Kit/examples/northgate-law/ARCHITECTURE_SPEC.md"),
            P("02_Templates/Enterprise_OS_Blueprint_Kit/examples/riverside-clinic/ARCHITECTURE_SPEC.md"),
            P("02_Templates/Enterprise_OS_Blueprint_Kit/examples/solo-consultant/ARCHITECTURE_SPEC.md"),
            P("05_From_V2_Domains/00_Amadeus/05_OSS_Twin/_reference/drawbridge/chrome-extension/ARCHITECTURE.md"),
            P("08_Workspaces_Dormants_2026-08-01/Antigravity-Kit-Source/.agent/ARCHITECTURE.md"),
            P("06_Claude_Code_Bare/gsd-core/templates/codebase/architecture.md"),
            P("06_Claude_Code_Bare/gsd-core/templates/research-project/ARCHITECTURE.md"),
            P("04_From_V2_Root/ARCHITECTURE_STRUCTURE.md")
        ]
    },
    {
        "nom": "INDEX (Geordi sub-folder ou Lane)",
        "attributs": ["Source / date / type / layer / lane / status / domain / tags / okf_version"],
        "chemins": [
            P("00_Index/INDEX_OF_INDEXES.md"),
            P("00_Index/OKF_INDEX.md"),
            P("00_Index/RESOURCES_INDEX.md"),
            P("00_Index/SECOND_BRAIN_PARA_MAP.md"),
            P("00_Index/JUNCTIONS_MAP_2026-08-02.md"),
            P("01_Guides/00_KERNEL_OS/_INDEX.md"),
            P("01_Guides/01_Product/_INDEX.md"),
            P("01_Guides/02_Ops/_INDEX.md"),
            P("01_Guides/03_IT/_INDEX.md"),
            P("01_Guides/04_Finance/_INDEX.md"),
            P("01_Guides/05_Legal/_INDEX.md"),
            P("01_Guides/06_Sales/_INDEX.md"),
            P("01_Guides/07_Growth/_INDEX.md"),
            P("01_Guides/08_People/_INDEX.md"),
            P("09_Life_OS/LD01_Business_Picard/_INDEX.md"),
            P("09_Life_OS/LD04_Cognition_Tilly/_INDEX.md"),
            P("01_Guides/_BATCH_2026-06-19_INDEX.md"),
            P("01_Guides/_BATCH_RECLASSIFICATION_INDEX.md"),
            P("05_From_V2_Domains/00_Amadeus/05_OSS_TSTwin/symphony/L1/INDEX_capsules.md"),
            P("05_From_V2_Domains/00_Amadeus/05_OSS_TSTwin/symphony/L1/INDEX_runtime.md"),
            P("05_From_V2_Domains/00_Amadeus/05_OSS_TSTwin/symphony/L1/INDEX_specs.md")
        ]
    },
    {
        "nom": "hand_off (wiki handoff canon)",
        "attributs": ["source", "date", "type: handoff", "domain", "tags", "related[]", "D1 receipts (paths canon + statuts)", "Doctrine", "Anti-pattern"],
        "chemins": [
            P("03_Memory_Unified/LLM_Wiki/wiki/hand_offs/2026-07-31_gemini_brainstorms/_INDEX.md"),
            P("03_Memory_Unified/LLM_Wiki/wiki/hand_offs/sessions_archive/INDEX_sessions.md"),
            P("03_Memory_Unified/LLM_Wiki/wiki/hand_offs/architecture_triptyque_morty_2026-06-21.md"),
            P("03_Memory_Unified/LLM_Wiki/wiki/hand_offs/youtube_to_guide_b1_filter_amend_2026-07-03.md"),
            P("04_From_V2_Root/wiki/hand_offs/2026-07-22_aaas_us_only_doctrine.md")
        ]
    },
    {
        "nom": "Twin spec (lane A canon mirror)",
        "attributs": ["Source canon", "Role", "Status", "Version", "supervised_by", "oversees[]", "lane", "twin_of (pointer)"],
        "chemins": [
            P("05_From_V2_Domains/00_Amadeus/05_OSS_TSTwin/symphony/L1/INDEX_specs.md"),
            P("05_From_V2_Domains/00_Amadeus/05_OSS_Twin/symphony/L1/INDEX_specs.md")
        ]
    },
    {
        "nom": "Agent Capsule (Soul/Agent/Heartbeat/Tools/Context)",
        "attributs": ["Soul (identité, ton, valeurs, interdits)", "Agent (mission, périmètre)", "Heartbeat (cadence, reprises)", "Tools (autorisations, MCP, CLI)", "Context (mémoire locale, handoff)"],
        "chemins": [
            P("05_From_V2_Domains/00_Amadeus/05_OSS_TSTwin/symphony/L1/INDEX_capsules.md"),
            P("05_From_V2_Domains/00_Amadeus/05_OSS_Twin/symphony/L1/INDEX_capsules.md")
        ]
    },
    {
        "nom": "Dispatch Doctrine (B1/B2 mindset)",
        "attributs": ["id", "title", "B1 owner", "B2 owner", "B3 squad roster", "horizon", "dispatch protocol", "D6 lesson learned", "anti-patterns guarded"],
        "chemins": [
            P("06_Claude_Code_Bare/mindsets/Beth_Dispatch_Doctrine.md"),
            P("06_Claude_Code_Bare/mindsets/Jerry_Dispatch_Doctrine.md"),
            P("06_Claude_Code_Bare/mindsets/Morty_Dispatch_Doctrine.md"),
            P("06_Claude_Code_Bare/mindsets/Summers_Dispatch_Doctrine.md")
        ]
    },
    {
        "nom": "Wargame MANIFEST (ordres war-mode)",
        "attributs": ["wargame", "slug", "deciders[]", "parent_dox[]", "domain", "tags[]", "war_mode", "append_only", "granularity", "self_grade", "Frame Signal (M1)", "Adversarial Proof (M2)", "Sub-MANIFEST per B2"],
        "chemins": [
            P("05_From_V2_Domains/30_Business_OS/10_Projects/wargames/wargame-30-out/MANIFEST_Triptyque_1_BusinessOS.md")
        ]
    },
    {
        "nom": "OpenSpec change archive (spec.md)",
        "attributs": ["ADDED Requirements", "Scenario (WHEN/THEN)", "Renamed/Replaced scopes"],
        "chemins": [
            P("08_Workspaces_Dormants_2026-08-01/openspec/changes/archive/2026-03-08-amadeus-akh-identity-fusion/specs/identity-core/spec.md"),
            P("08_Workspaces_Dormants_2026-08-01/openspec/changes/archive/2026-03-08-amadeus-control-room-a0/specs/amadeus-digital-twin/spec.md")
        ]
    },
    {
        "nom": "Manifest cross-harness (per LD)",
        "attributs": ["type: harness-manifest-cross", "harnesses[]", "entry sequence per harness", "Surface attendue", "Surface mutante vs read-only"],
        "chemins": [
            P("05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/90_manifests/manifest.cross-harness.md")
        ]
    },
    {
        "nom": "Doctrine Lock Map (alignement plans ↔ organigramme)",
        "attributs": ["plans_sources[]", "rot_rate", "Table de correspondance", "Pont de mise à jour D1"],
        "chemins": [
            P("05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/99_meta/doctrine_lock_map.md")
        ]
    },
    {
        "nom": "Skill canon (Claude Code)",
        "attributs": ["name", "description", "tools[]", "Path canon", "Sister index"],
        "chemins": [
            P("06_Claude_Code_Bare/skills/sessions-archive/references/indexer-spec.md"),
            P("06_Claude_Code_Bare/skills/skill-creator/references/schemas.md")
        ]
    },
    {
        "nom": "Plugin (Claude Code plugin)",
        "attributs": ["Path", "marketplace", "sister/agent files", "commandes", "hooks", "MCP servers"],
        "chemins": [
            P("06_Claude_Code_Bare/plugins/marketplaces/claude-plugins-official/plugins/code-modernization/agents/architecture-critic.md"),
            P("06_Claude_Code_Bare/plugins/marketplaces/agents-observe/docs/plans/implemented/spec-cli-event-descriptors.md"),
            P("06_Claude_Code_Bare/plugins/marketplaces/agents-observe/docs/plans/implemented/spec-configurable-notification-events.md"),
            P("06_Claude_Code_Bare/plugins/marketplaces/agents-observe/docs/plans/implemented/spec-fresh-install-test-harness.md"),
            P("06_Claude_Code_Bare/plugins/marketplaces/agents-observe/docs/plans/implemented/spec-notification-envelope-flags.md"),
            P("06_Claude_Code_Bare/plugins/marketplaces/agents-observe/docs/plans/implemented/spec-session-labels.md"),
            P("06_Claude_Code_Bare/plugins/marketplaces/agents-observe/docs/plans/implemented/spec-timeline-animation-bugs.md"),
            P("06_Claude_Code_Bare/plugins/marketplaces/agents-observe/docs/plans/implemented/spec-timeline-rewind.md")
        ]
    },
    {
        "nom": "A3 Spec (A3 agent immutable spec)",
        "attributs": ["id", "layer", "role", "parent_a2", "classification", "status", "Identity / Core Question / Inputs / Outputs / Boundaries / Evidence"],
        "chemins": [
            P("A3_Geordi_Resources_Spec.md")
        ]
    },
    {
        "nom": "Junction Map (NTFS junctions)",
        "attributs": ["Chemin relatif", "Cible realpath", "Existe (oui/non)", "Compte .md", "Domaine PARA", "Catégorie de risque", "Cible typique"],
        "chemins": [
            P("00_Index/JUNCTIONS_MAP_2026-08-02.md")
        ]
    },
    {
        "nom": "Blueprint ADR",
        "attributs": ["id", "title", "status", "date", "L0/L1/L2 layer", "isomorph structure (01-SDD / 02-ADR / 03-PRD / 04-DDD)", "Junction aliasing rules"],
        "chemins": [
            P("05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-FWK-021_blueprints-canon-tripartite.md"),
            P("05_From_V2_Domains/30_Business_OS/09_Blueprints/02-ADR/ADR-MESH-L2-001_tri-plateforme-doctrine.md")
        ]
    },
    {
        "nom": "STANDARD A0 FORMAT",
        "attributs": ["Daily Captain's Log (YYYY-MM-DD.md)", "Weekly Distillation", "Monthly Distillation", "Quarterly 12WY", "Tags & versioning"],
        "chemins": [
            P("03_Memory_Unified/LLM_Wiki/wiki/_CAPTURE_2026-08-01/vendor_openclaw_workspace_memory/STANDARD_A0_FORMAT.md")
        ]
    },
    {
        "nom": "INDEX_QA_REPORT (audit sémantique)",
        "attributs": ["domain", "ld", "b2_owner", "sister_b1", "b1_filter", "Statut INDEX (V0/V1)", "Distribution par confiance (HIGH/MEDIUM/LOW/FALLBACK)", "Doublons identifiés", "Alertes"],
        "chemins": [
            P("01_Guides/07_Growth/Yann_Leonardi/INDEX_QA_REPORT.md"),
            P("05_From_V2_Domains/30_Business_OS/00_Jerry_Business_Pulse/graphify-burst/chunks/chunk_013/INDEX_QA_REPORT.md"),
            P("05_From_V2_Domains/30_Business_OS/00_Jerry_Business_Pulse/graphify-burst/chunks/chunk_014/INDEX_QA_REPORT.md"),
            P("05_From_V2_Domains/30_Business_OS/00_Jerry_Business_Pulse/graphify-burst/chunks/chunk_015/INDEX_QA_REPORT.md")
        ]
    },
    {
        "nom": "Cardia (A3 Book LD01 doctrine index)",
        "attributs": ["okf_version", "type: book-doctrine-root", "title", "description", "domain", "agent", "horizon", "variant", "parent_dox", "sister_plans", "children", "Doctrine de traversée"],
        "chemins": [
            P("05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/00_index.md")
        ]
    }
]

# === RELATIONS (verbatim citations) ===
v3["relations"] = [
    {
        "de": "ADR-SOBER-002 (anti-paperclip maximizer doctrine)",
        "verbe": "anchor sister",
        "vers": "ADR-L2-AAAS-001",
        "citation": "doctrine_anchors: [ADR-META-001, ADR-META-001-D1, ADR-META-001-D5, ADR-META-001-D7, ADR-META-002, ADR-META-003, ADR-META-005, RICK-001, **L2-AAAS-001**, INFRA-003, CANON-001]",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/INDEX.md")
    },
    {
        "de": "ADR-MEM-001 (Memory Fabric)",
        "verbe": "sister scope",
        "vers": "ADR-MEM-002 (Wiki ↔ Life Wheel Mapping)",
        "citation": "Cette ADR résout les 2 gaps en un seul document canonique, **sister scope stricte à ADR-MEM-001** (Memory Fabric) — scope = Memory Fabric ↔ Life Wheel LDxx mapping, PAS IndexedDB Cloisonnement.",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L1_Life_OS/ADR-MEM-002_wiki-lifewheel-mapping-doctrine.md")
    },
    {
        "de": "ADR-MEM-002",
        "verbe": "resolves ID collision with",
        "vers": "ADR-MEM-001 (historique IndexedDB)",
        "citation": "(2) ADR-MEM-001 actuel a un D4 collision warn avec un ADR historique IndexedDB (NOT in _SPECS/ADR/ canonique). Hash d'intention résolvant la collision : `adr_mem_002_proposed_2026-06-21_wiki_lifewheel_mapping`.",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L1_Life_OS/ADR-MEM-002_wiki-lifewheel-mapping-doctrine.md")
    },
    {
        "de": "ADR-META-003 (Model-Agnostic Runtime)",
        "verbe": "extends/sépare",
        "vers": "ADR-META-002 (Autonomy by Design)",
        "citation": "recommandé en Open Question (META-002 l.144) la création d'un ADR-META-003 séparant proprement harness (invariant) de modèle (variable).",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L1_Life_OS/ADR-META-003_model-agnostic-runtime-doctrine.md")
    },
    {
        "de": "ADR-AAAS-OPERATIONS-CANON-001",
        "verbe": "sister doctrinal direct",
        "vers": "ADR-AAAS-ACQUISITION-DOCTRINE-001",
        "citation": "ADR-AAAS-ACQUISITION-DOCTRINE-001 (RATIFIED 2026-06-24, 25 455 chars, doctrinal sister direct — Acquisition-First MedVie 400M$)",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-OPERATIONS-CANON-001_aaas-operations-canon.md")
    },
    {
        "de": "ADR-AAAS-PRICING-001",
        "verbe": "amend (USD post-accupuncture SUPERSEDE EUR)",
        "vers": "Pricing historique EUR (Takeout 2026-05)",
        "citation": "amended: 2026-06-24 (Hypothèse A retenue : USD post-accuponcture SUPERSEDE EUR takeout)",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-001_aaas-pricing-canon.md")
    },
    {
        "de": "ADR-AAAS-ACQUISITION-DOCTRINE-001",
        "verbe": "sister canon",
        "vers": "ADR-AAAS-PRICING-001 (5 Tiers USD post-accuponcture)",
        "citation": "Guide 2/02_Ops/solopreneur-ai-agent-business-BI-MNjm1tTQ.md (22 708 chars, Antigravity Premium)",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-ACQUISITION-DOCTRINE-001_aaas-acquisition-doctrine.md")
    },
    {
        "de": "ADR-AAAS-FINANCE-CANON-001",
        "verbe": "construit sur",
        "vers": "ADR-MARKET-STUDY-001 (The Builders 2026 TAM 136,1 Mds$)",
        "citation": "ADR-MARKET-STUDY-001 (RATIFIED 2026-06-24, The Builders 2026 TAM 136,1 Mds USD)",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-FINANCE-CANON-001_aaas-finance-canon.md")
    },
    {
        "de": "ADR-AAAS-IT-CANON-001",
        "verbe": "construit sur / sister direct",
        "vers": "ADR-AAAS-OPERATIONS-CANON-001",
        "citation": "ADR-AAAS-OPERATIONS-CANON-001 (RATIFIED 2026-06-24, sister scope canon direct — Operations 5 Piliers)",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-IT-CANON-001_aaas-it-canon.md")
    },
    {
        "de": "ADR-AAAS-IT-EXT-CANON-001",
        "verbe": "extends",
        "vers": "ADR-AAAS-IT-CANON-001",
        "citation": "ADR-AAAS-IT-EXT-CANON-001 (RATIFIED 2026-06-25, 6 Piliers IT Stack ... ADR-AAAS-IT-CANON-001 (RATIFIED 2026-06-24, 5 Piliers AaaS IT canon - SISTER DIRECT)",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-IT-EXT-CANON-001_aaas-it-ext-canon.md")
    },
    {
        "de": "ADR-AAAS-OPERATIONS-CANON-001",
        "verbe": "sister doctrinal direct",
        "vers": "ADR-AAAS-ACQUISITION-DOCTRINE-001",
        "citation": "doctrinal sister direct — Acquisition-First MedVie 400M$",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-OPERATIONS-CANON-001_aaas-operations-canon.md")
    },
    {
        "de": "ADR-CANON-001 (Roster Source of Truth)",
        "verbe": "supersedes_scope (AGENTS.md membership)",
        "vers": "AGENTS.md §Macro Squads (lore only)",
        "citation": "supersedes_scope: AGENTS.md §\"Macro Squads\" roster membership (lore only — NOT structure)",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-CANON-001_roster-source-of-truth.md")
    },
    {
        "de": "ADR-L2-AAAS-001 (3 Variants Solarpunk)",
        "verbe": "carries",
        "vers": "3 variants AaaS (Solaris / Nexus-OMK / Orbiter-ABC) × 4 Leviers Solarpunk",
        "citation": "AaaS Doctrine 3 Variants (Solaris/Nexus-OMK/Orbiter-ABC) × 4 Leviers Solarpunk (biomimétisme Benyus + low-high tech Aberkane + Meta Science + circular & blue economy) + Saru 1000T Kardashev Type 3.",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/INDEX.md")
    },
    {
        "de": "ADR-L2-PAPERCLIPAI-001",
        "verbe": "extends/sister",
        "vers": "ADR-SOBER-002 (anti-paperclip kernel)",
        "citation": "doctrine_anchors: [ADR-META-001 D1-D8, ADR-EXTRA-PPR-001 (PPR-only), **ADR-SOBER-002 (anti-paperclip kernel)**, ADR-OMK-MULTICA-001 (sister substrate)...]",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-PAPERCLIPAI-001_governance-mirror-doctrine.md")
    },
    {
        "de": "ADR-L2-PAPERCLIPAI-002 (Anti-paperclip irony)",
        "verbe": "sister de",
        "vers": "ADR-L2-PAPERCLIPAI-001 (governance-mirror)",
        "citation": "doctrine_anchors: ... **ADR-L2-PAPERCLIPAI-001 (sister)**, **ADR-L2-PAPERCLIPAI-003 (sister delegation-not-creation, NEW per Nick LECTURE 2)** ...",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-PAPERCLIPAI-002_anti-paperclip-irony-doctrine.md")
    },
    {
        "de": "ADR-L2-PAPERCLIPAI-003 (delegation-not-creation)",
        "verbe": "amends sister",
        "vers": "ADR-L2-PAPERCLIPAI-001 / -002",
        "citation": "extends: ADR-L2-PAPERCLIPAI-001 (governance-mirror-doctrine), ADR-L2-PAPERCLIPAI-002 (anti-paperclip irony), ADR-L2-PAPERCLIPAI-003 (delegation-not-creation), ADR-SOBER-002 (anti-paperclip kernel)",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-PAPERCLIPAI-004_paperclip-calibration-doctrine_RATIFIED_2026-07-16.md")
    },
    {
        "de": "ADR-L2-PAPERCLIPAI-004 (Calibration)",
        "verbe": "amends",
        "vers": "All 3 sister ADRs above + Dev Gate autopilot",
        "citation": "amends: All 3 sister ADRs above + Dev Gate autopilot description (multica id 2dabf5b8-dc6a-4629-a866-8c7493652a22)",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-PAPERCLIPAI-004_paperclip-calibration-doctrine_RATIFIED_2026-07-16.md")
    },
    {
        "de": "ADR-L2-KARDASHEV-TYPE-FRACTAL-001",
        "verbe": "extends",
        "vers": "ADR-L2-AAAS-001, ADR-CANON-001, ADR-OMK-MULTICA-001, MEMORY.md, ADR-A0-L-META-001, ADR-A0-L-COACH-AMEND-001",
        "citation": "extends: ADR-L2-AAAS-001, ADR-CANON-001, ADR-OMK-MULTICA-001, MEMORY.md, ADR-A0-L-META-001, ADR-A0-L-COACH-AMEND-001",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-KARDASHEV-TYPE-FRACTAL-001_multiverse-architecture_RATIFIED_2026-07-16.md")
    },
    {
        "de": "ADR-L2-NAMING-CONVENTION-001",
        "verbe": "sister scope",
        "vers": "ADR-L2-MULTIVERSE-CD-001, ADR-L2-TRIPTYQUE-V4-001, SPEC-ENTERPRISE-OS-100M-001, ADR-CANON-001, ADR-META-001",
        "citation": "related: [ADR-L2-MULTIVERSE-CD-001, ADR-L2-TRIPTYQUE-V4-001, ADR-AAAS-PRICING-001-AMEND-003, SPEC-ENTERPRISE-OS-100M-001, ADR-CANON-001, ADR-META-001]",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-NAMING-CONVENTION-001_session-canon_RATIFIED_2026-07-15.md")
    },
    {
        "de": "ADR-RITUAL-001 (SlashCommand Canon)",
        "verbe": "sister scope",
        "vers": "ADR-META-005, ADR-HARNESS-001, ADR-LIFE-013, ADR-LIFE-014, ADR-AAAS-002",
        "citation": "doctrine_anchors: [ADR-META-005, ADR-META-001-D7, ADR-HARNESS-001, ADR-LIFE-013, ADR-LIFE-014, ADR-AAAS-002]",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L1_Life_OS/ADR-RITUAL-001_slashcommand-canon-library_PROPOSED.md")
    },
    {
        "de": "ADR-OPS-009 (Worker Git Commit)",
        "verbe": "extends",
        "vers": "ADR-META-001 D4 (no-amnesia append-only) + .claude/rules/git-workflow.md",
        "citation": "extends: [ADR-META-001 D4 (no-amnesia append-only), .claude/rules/git-workflow.md (conventional commits format)]",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-OPS-009_worker-git-commit-doctrine.md")
    },
    {
        "de": "ADR-RH-META-GOUVERNANCE-001-canonical-v2",
        "verbe": "supersedes_scope = nothing (D4 append-only, canonical alignment)",
        "vers": "ADR-CANON-001, ADR-CANON-002, ADR-AGENT-BENCH-SCHEMA-001, ADR-LANDING-AESTHETIC-001, ADR-META-001, ADR-META-002, ADR-SOBER-002, ADR-A0-L-META-001",
        "citation": "sister_canon: - ADR-CANON-001 (Roster Source of Truth, ACCEPTED 2026-06-02) — Green Lantern × X-Men = Domain 01 ✓ CANONICAL ALIGNMENT",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-RH-META-GOUVERNANCE-001-canonical-v2_PROPOSED_2026-07-25.md")
    },
    {
        "de": "ADR-RH-META-GOUVERNANCE-001-canonical-v3",
        "verbe": "supersedes",
        "vers": "ADR-RH-META-GOUVERNANCE-001-canonical-v2",
        "citation": "supersedes_scope: ADR-RH-META-GOUVERNANCE-001-canonical-v2 (PROPOSED 2026-07-25) — D4 append-only, v3 body extends v2 body, no overwrite",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-RH-META-GOUVERNANCE-001-canonical-v3_RATIFIED_2026-07-26.md")
    },
    {
        "de": "ADR-AGENT-BENCH-SCHEMA-001 (agent_bench SQL)",
        "verbe": "sister",
        "vers": "ADR-CANON-002 (RHA Workflow) + ADR-RH-META-GOUVERNANCE-001",
        "citation": "Pas de schéma canon pour ça actuellement. Les agents vivent dans `~/.claude/agents/*.md` (frontmatter YAML) et Notion `AGENT_REGISTRY_DB`. Pas de versionning de SOUL, pas de lifecycle state machine, pas d'audit trail.",
        "chemin": P("04_From_V2_Root/_DRAFTS_PPR_LANE/2026-07-25_rh_meta_gouvernance/ADR-AGENT-BENCH-SCHEMA-001_agent-bench-sql-canonique_PROPOSED.md")
    },
    {
        "de": "ADR-L2-AAAS-US-ONLY-001 (US-only doctrine)",
        "verbe": "amend sister",
        "vers": "ADR-ICP-SOLARIS-001 / ADR-ICP-NEXUS-001 / ADR-ICP-ORBITER-001 (géographie amendée)",
        "citation": "| `ADR-ICP-SOLARIS-001` | RATIFIED 2026-06-24 | 🔄 AMEND sister scope à venir — ajouter note \"géographie amendée par ADR-L2-AAAS-US-ONLY-001\" ...",
        "chemin": P("04_From_V2_Root/wiki/hand_offs/2026-07-22_aaas_us_only_doctrine.md")
    },
    {
        "de": "ADR-LANDING-AESTHETIC-001 (Doctrine Esthétique Positive)",
        "verbe": "sister (negative mirror)",
        "vers": "ADR-ANTI-TEMPLATE-001 (liste noire)",
        "citation": "tags: [\"#ADR #aesthetic #doctrine #anti-ai-slop #landing-page ...\"] — related: [ADR-ANTI-TEMPLATE-001, ADR-DESIGN-SYSTEM-001, ADR-NEXUS-LANDING-PERSONAS-001, ADR-ICP-NEXUS-001, ADR-AAAS-PRICING-001, ADR-L2-AAAS-001, ADR-SOBER-002, ADR-META-001]",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-LANDING-AESTHETIC-001_doctrine-esthetique.md")
    },
    {
        "de": "ADR-LANDING-COPY-001",
        "verbe": "sister-canon negative-rules-source",
        "vers": "ADR-ANTI-PAPERCLIP-001",
        "citation": "related_adrs: - id: ADR-ANTI-PAPERCLIP-001 type: sister-canon role: negative-rules-source",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-LANDING-COPY-001_doctrine-copywriting.md")
    },
    {
        "de": "ADR-NEXUS-10-ICP-001",
        "verbe": "supersedes_scope",
        "vers": "ADR-OMK-PRODUCTS-001 + 3-sequences-outbound (Strate A + C ajoutées)",
        "citation": "supersedes_scope: corrige l'omission Strate A + Strate C dans les drafts antérieurs (ADR-OMK-PRODUCTS-001 §\"Matrice d'Offre\" et 3-sequences-outbound 2026-07-08) qui se limitaient à la Strate B.",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-NEXUS-10-ICP-001_3-strates-10-cibles-canon.md")
    },
    {
        "de": "RUNBOOK_C1-R1",
        "verbe": "amend §4.2",
        "vers": "Design initial (Docker)",
        "citation": "amendé 2026-07-20 §4.2 : design Docker initial remplacé par design léger fichier pour portabilité VPS sans service",
        "chemin": P("05_From_V2_Domains/00_Amadeus/sob/RUNBOOK_C1-R1.md")
    },
    {
        "de": "RUNBOOK_C1-R1",
        "verbe": "suit de",
        "vers": "Plan `fancy-hugging-bengio.md`",
        "citation": "Plan `fancy-hugging-bengio.md` §3.1 + AGENTS.md canon (Pattern: Russian dolls nesting par conception)",
        "chemin": P("03_Memory_Unified/LLM_Wiki/wiki/hand_offs/architecture_triptyque_morty_2026-06-21.md")
    },
    {
        "de": "Architecture Triptyque Morty (12WY⊃PARA⊃DEAL)",
        "verbe": "compose nested",
        "vers": "12WY / PARA / DEAL (3 A2 ships)",
        "citation": "Doctrine canon : Le triptyque Morty = **3 A2 ships imbriqués par conception** (Russian dolls) : - **12WY** (USS Curie SNW) = couche **extérieure** — cadence hebdo 12 Week Year - **PARA** (USS Enterprise Computer) = couche **intermédiaire** - **DEAL** (USS Protostar Holo Janeway) = couche **intérieure**",
        "chemin": P("03_Memory_Unified/LLM_Wiki/wiki/hand_offs/architecture_triptyque_morty_2026-06-21.md")
    },
    {
        "de": "Lane A Spec (symphony twin)",
        "verbe": "vient de",
        "vers": "20_Life_OS canon",
        "citation": "Le canon reste **source de vérité** ; les twins sont des **vues runtime** consommables par Symphony/Agents.",
        "chemin": P("05_From_V2_Domains/00_Amadeus/05_OSS_TSTwin/symphony/L1/INDEX_specs.md")
    },
    {
        "de": "A1 capsule",
        "verbe": "rattachée à (A1 supervisé par)",
        "vers": "A0_Amadeus",
        "citation": "A1 `supervised_by: A0_Amadeus` + `oversees:` list 6 A2 ajoutée.",
        "chemin": P("05_From_V2_Domains/00_Amadeus/05_OSS_TSTwin/symphony/L1/INDEX_specs.md")
    },
    {
        "de": "Twin (lane A)",
        "verbe": "pointe vers capsule (lane C)",
        "vers": "Soul/Agent/Heartbeat/Tools/Context",
        "citation": "Chaque capsule pointe vers son spec twin dans Lane A via `[[<X>_Spec.twin]]` dans `Agent.md`.",
        "chemin": P("05_From_V2_Domains/00_Amadeus/05_OSS_TSTwin/symphony/L1/INDEX_capsules.md")
    },
    {
        "de": "geordi/01_Guides (à reclassifier)",
        "verbe": "doit passer par",
        "vers": "Picard A3 via ADR-L2-BDLD-MAP-001 (bijection 8 B2 ↔ 8 LD)",
        "citation": "Picard A3 lit frontmatter + 1ère section, **fixe le champ `ld`** au canon LD01_Business (qui mappe B2 Sales ↔ B1 Jerry), et appende `sister_b1: jerry-prime` au frontmatter.",
        "chemin": P("01_Guides/06_Sales/_INDEX.md")
    },
    {
        "de": "b1-jerry-prime",
        "verbe": "lit chaque INDEX sur intention",
        "vers": "01_Product / 02_Ops / 03_IT / 04_Finance / 05_Legal / 06_Sales / 07_Growth / 08_People",
        "citation": "B1 owner : Jerry Prime lit cette INDEX sur chaque intention Product → route B2 Flash ou downstream B3 Captain America / Iron Man / Thor / Hulk / Black Widow / Hawkeye / Scarlet Witch.",
        "chemin": P("01_Guides/01_Product/_INDEX.md")
    },
    {
        "de": "guide 02_Ops BI-MNjm1tTQ",
        "verbe": "couvre",
        "vers": "5 sub-types persona Structuration-First",
        "citation": "**Guide BI-MNjm1tTQ** (22 708 chars) couvre les **5 sub-types persona** Structuration-First canon",
        "chemin": P("01_Guides/02_Ops/_INDEX.md")
    },
    {
        "de": "guide 07_Growth N-9rovSvCEA (MedVie)",
        "verbe": "valide rétroactivement",
        "vers": "thèse AaaS Solarpunk (ADR-L2-AAAS-001 Pilier 3 Sobriété)",
        "citation": "Le guide MedVie **valide rétroactivement** la thèse AaaS Solarpunk (`ADR-L2-AAAS-001` Pilier 3 Sobriété) que l'agent-as-a-service asset-light + bootstrap-friendly + acquisition triple-canal est **supérieur au SaaS**",
        "chemin": P("01_Guides/07_Growth/_INDEX.md")
    },
    {
        "de": "JUNCTION_MAP",
        "verbe": "détecte via",
        "vers": "stat.FILE_ATTRIBUTE_REPARSE_POINT (0x400)",
        "citation": "Detection : `stat.FILE_ATTRIBUTE_REPARSE_POINT` (0x400) sur `os.DirEntry.stat(follow_symlinks=False)`",
        "chemin": P("00_Index/JUNCTIONS_MAP_2026-08-02.md")
    },
    {
        "de": "Jonctions NTFS",
        "verbe": "sont écartées",
        "vers": "aspace-graphify-out (808), cross-PARA (24), _TRASH (16), external_home_dot (26)",
        "citation": "**Note importante** : le brief de Geordi annonçait 47 jonctions (11 + 36). Les 47 sont confirmees ; le scan exhaustif en revele **112 supplementaires**, majoritairement dans `06_Claude_Code_Bare` (91)",
        "chemin": P("00_Index/JUNCTIONS_MAP_2026-08-02.md")
    },
    {
        "de": "03_Resources_Geordi/01_Guides (dossier)",
        "verbe": "appartient au bucket",
        "vers": "Resources (S3)",
        "citation": "Guides canon 8 Domaines + premium ... `01_Guides/` (15 560)",
        "chemin": P("00_Index/SECOND_BRAIN_PARA_MAP.md")
    },
    {
        "de": "OKF v0.1",
        "verbe": "définit format",
        "vers": "bundle = arbre de .md + frontmatter YAML",
        "citation": "```\nbundle = arbre de .md + frontmatter YAML\n``` Un bundle OKF est : - Un répertoire contenant des fichiers `.md`. - Chaque fichier (sauf exceptions nommées) porte un frontmatter YAML. - Les liens sont **bundle-relatifs** (`/path.md`), pas absolus. - La consommation est **permissive** : liens brisés et types inconnus sont tolérés.",
        "chemin": P("00_Index/OKF_INDEX.md")
    },
    {
        "de": "B1 Manifest (caste B1/B2/B3)",
        "verbe": "ancre dynamique",
        "vers": "ADR-CANON-002 (RHA Workflow)",
        "citation": "**SPEC ONLY** — ce workflow est la dynamique du B1_Manifesto. Toute création d'agent (B1/B2/B3/B4) DOIT passer par ce pipeline après ratification A0.",
        "chemin": P("04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-CANON-002_RHA-Workflow_W20-M5.md")
    },
    {
        "de": "Symbiose Lane A ↔ Lane C",
        "verbe": "suit le symbiose",
        "vers": "canon 20_Life_OS/<ship>/<X>_Spec.md",
        "citation": "20_Life_OS/<ship>/<X>_Spec.md   ──►   OSS_Twin/symphony/L1/lane_A_specs/<X>_Spec.twin.md SOURCE                                 VUE RUNTIME",
        "chemin": P("05_From_V2_Domains/00_Amadeus/05_OSS_TSTwin/symphony/L1/INDEX_specs.md")
    },
    {
        "de": "state.json (40_SYMPHONY_BUS)",
        "verbe": "est SSOT pour",
        "vers": "A0 → A1 → A2 → A3 → B1/B2/B3",
        "citation": "`40_SYMPHONY_BUS/` est le **SSOT (Single Source Of Truth)** de l'état canonique entre agents A0 → A1 → A2 → A3 → B1/B2/B3. Chaque transition écrit dans `state.json` via `state_writer.py` (lock atomique + tempfile + rename).",
        "chemin": P("05_From_V2_Domains/00_Amadeus/40_SYMPHONY_BUS/SCHEMA.md")
    },
    {
        "de": "Doctrine Lock Map LD01",
        "verbe": "aligne",
        "vers": "plan-meta-memoire-okf-wiki-graphify-dox + plan-minimax-l1-book-lune + plan-strategie-cc-l1-zora-macro + fancy-hugging-bengio",
        "citation": "plans_sources: - C:\\Users\\amado\\.claude\\plans\\plan-meta-memoire-okf-wiki-graphify-dox.md - C:\\Users\\amado\\.claude\\plans\\plan-minimax-l1-book-lune.md - C:\\Users\\amado\\.claude\\plans\\plan-strategie-cc-l1-zora-macro.md - C:\\Users\\amado\\.claude\\plans\\fancy-hugging-bengio.md",
        "chemin": P("05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/99_meta/doctrine_lock_map.md")
    },
    {
        "de": "B3-Enterprise-Geordi (3 personas)",
        "verbe": "réfère canoniquement",
        "vers": "Apartamento Magazine / Linear / Teenage Engineering",
        "citation": "**3 WebFetch réussis** (budget=3, épuisé) : apartamentomagazine.com · linear.app · teenage.engineering — analyses couleurs/fonts/composants en live. **6 WebSearch échoués** (API 400 \"params empty\") → découverte gallery (awwwards/land-book/godly/dribbble) **SKIPPED honnêtement**.",
        "chemin": P("05_From_V2_Domains/30_Business_OS/10_Projects/omk/repos/omk-nexus-landing-3-personas/_references/00_INDEX.md")
    },
    {
        "de": "manifest.cross-harness (LD01)",
        "verbe": "considère",
        "vers": "Claude Code, MiniMax Code, Hermes Agent, Shadow L1 (Agent Zero), Doctor, future-shadow",
        "citation": "harnesses: - claude-code - minimax-code - hermes-agent - shadow-l1-agent-zero - mavis-doctor - future-shadow",
        "chemin": P("05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/90_manifests/manifest.cross-harness.md")
    },
    {
        "de": "Phase 47 doctrine",
        "verbe": "canalise toutes notes Gemini vers",
        "vers": "wiki/hand_offs/2026-07-31_gemini_brainstorms/ (PAS ~/.claude/memory, ~/.codex/memory, etc.)",
        "citation": "Toutes notes Gemini vont ici, pas dans : - `~/.claude/memory` (CC) - `~/.codex/memory` (OpenAI Codex) - `~/.openclaw/memory` (OpenClaw) - `~/.minimax/memory` (Minimax/M3) - `AIOS/aios/memory` (legacy) - `AppData/Roaming\\Canon` (orphan)",
        "chemin": P("03_Memory_Unified/LLM_Wiki/wiki/hand_offs/2026-07-31_gemini_brainstorms/_INDEX.md")
    },
    {
        "de": "AaaS Sisters (Solaris / Nexus / Orbiter)",
        "verbe": "exploite marché",
        "vers": "USA UNIQUEMENT (pas Canada, UK, EU, France)",
        "citation": "**AaaS Sisters (Solaris / Nexus / Orbiter) = marché américain UNIQUEMENT. Pas Canada, pas UK, pas Europe, pas Francophonie.** Ratifié A+ 2026-07-22. Réversibilité : uniquement par nouvel ordre A+ explicite.",
        "chemin": P("04_From_V2_Root/wiki/hand_offs/2026-07-22_aaas_us_only_doctrine.md")
    },
    {
        "de": "AaaS Sisters US-only",
        "verbe": "applique compliance",
        "vers": "CCPA / Colorado AI Act (CO SB24-205) / HIPAA, pas RGPD",
        "citation": "| CCPA (California) | Active 2020, amendements 2023-2024. Toutes opérations CA. | | Colorado AI Act (CO SB24-205) | Effective 2026-02-01. Premier state AI law US. Driver marketing Nexus. | | **Banni** : RGPD, CNIL, EU AI Act, GDPR, tout EU-specific compliance. Pas de mention dans messaging US. |",
        "chemin": P("04_From_V2_Root/wiki/hand_offs/2026-07-22_aaas_us_only_doctrine.md")
    },
    {
        "de": "Book LD01",
        "verbe": "vaut",
        "vers": "H1 Weekly P&L (PAS H10)",
        "citation": "**Horizon canon** : **H1 Weekly P&L** — PAS H10. Verrouillé par `symphony/L1/lane_A_specs/03_A3_crews/discovery/book.twin.md`",
        "chemin": P("05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/00_index.md")
    },
    {
        "de": "Variant AaaS Book",
        "verbe": "est",
        "vers": "Solaris (Kardashev Type 3)",
        "citation": "**Variant AaaS** : **Solaris** (Civilisation Kardashev Type 3, H90 Legacy 1000T par valeur Solarpunk/biomimétisme — Benyus + Aberkane)",
        "chemin": P("05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/00_index.md")
    },
    {
        "de": "Geordi (A3 Resources)",
        "verbe": "est",
        "vers": "A3 Resources canon",
        "citation": "**Verbatim canon** : \"USS Enterprise (Computer) ... PARA 4 lettres | Picard, Spock, **Geordi**, Data\".",
        "chemin": P("A3_Geordi_Resources_Spec.md")
    },
    {
        "de": "Geordi (A3)",
        "verbe": "ne fait pas",
        "vers": "Park active deliverables / Archive retired material",
        "citation": "Geordi does not park active deliverables in Resources. Geordi does not archive retired material.",
        "chemin": P("README.md")
    },
    {
        "de": "Triples Plateforme Doctrine (MESH-L2-001)",
        "verbe": "produit 3 plate-formes",
        "vers": "Solaris, Nexus-OMK, Orbiter-ABC",
        "citation": "Three variants Agency-as-a-Service: Solaris, Nexus-OMK, Orbiter-ABC (cf. ADR-L2-AAAS-001 sister scope)",
        "chemin": P("05_From_V2_Domains/30_Business_OS/09_Blueprints/02-ADR/ADR-MESH-L2-001_tri-plateforme-doctrine.md")
    },
    {
        "de": "ADR-FWK-021 (Canon Tripartite)",
        "verbe": "isomorph L0/L1/L2",
        "vers": "12_Blueprints/ (L0) · 28_Blueprints/ (L1) · 09_Blueprints/ (L2)",
        "citation": "Chaque niveau a son canon Blueprints isomorphe : `12_Blueprints\\` (L0) · `28_Blueprints\\` (L1) · `09_Blueprints\\` (L2)",
        "chemin": P("05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-FWK-021_blueprints-canon-tripartite.md")
    },
    {
        "de": "Wargame 30 Triptyque 1",
        "verbe": "produit 3 B2 frames (GreenLantern, Batman, Cyborg)",
        "vers": "9/8/6 B3 squads (X-Men, Fantastic Four, Kang Dynasty)",
        "citation": "| GreenLantern | People (X-Men) | 8/8 (ProfessorX, Cyclops, JeanGrey, Wolverine, Storm, Beast, Nightcrawler, Rogue) | OK | | Batman | Ops (Fantastic Four) | 4/4 (MrFantastic, InvisibleWoman, HumanTorch, TheThing) | OK | | Cyborg | IT (Kang Dynasty) | 6/6 (KangPrime, IronLad, ScarletCenturion, Immortus, VictorTimely, RamaTut) | OK |",
        "chemin": P("05_From_V2_Domains/30_Business_OS/10_Projects/wargames/wargame-30-out/MANIFEST_Triptyque_1_BusinessOS.md")
    },
    {
        "de": "MANIFEST Wargame 30",
        "verbe": "porte tri-horizon emboîté",
        "vers": "B1 Summers 1y / B1 Jerry 3y / A3 Picard 10y",
        "citation": "3 horizons emboîtés : B1 Summers 1y / B1 Jerry 3y / A3 Picard 10y. Cyborg (IT) apporte la dimension R&D innovation filter via YouTube last30days guides + Geordi corpus.",
        "chemin": P("05_From_V2_Domains/30_Business_OS/10_Projects/wargames/wargame-30-out/MANIFEST_Triptyque_1_BusinessOS.md")
    }
]

# === CODES ===
v3["codes"] = [
    {
        "systeme": "LD01-LD08 (Life Wheel, 8 Life Domains)",
        "numerote": "LD01 Career_Business / LD02_Finance_Saru / LD03_Health_Culber / LD04_Cognition_Tilly / LD05_Legal / LD06_Family_Burnham / LD07_Creativity_Reno / LD08_Impact_Georgiou",
        "defini_dans": "01_Guides/01_Product/_INDEX.md + 03_Memory_Unified/LLM_Wiki/wiki/index.md (Life Wheel — par variant Jerry (Spock doctrine × Discovery/Zora observation))"
    },
    {
        "systeme": "B1/B2/B3 (Business Hierarchy)",
        "numerote": "B1 = Gatekeeper (Jerry/Summers), B2 = Captain (B2_flash-product, B2_cyborg-it, B2_johnjones-sales, B2_aquaman-legal, B2_superman-growth, B2_greenlantern-people, B2_batman-ops, B2_wonderwoman-finance), B3 = Squad (Avengers, X-Men, F4, Kang, Thunderbolts, Illuminati, Eternals, Guardians, Flash)",
        "defini_dans": "01_Guides/01_Product/_INDEX.md (sister_canon: b1-jerry-prime, b2-03-flash-product, b3-3-captain-america)"
    },
    {
        "systeme": "A0/A1/A2/A3 (Agent Hierarchy)",
        "numerote": "A0 = Amadeus (Méta-Orchestrateur/Souverain), A1 = Gatekeeper (Rick/Beth/Morty), A2 = Ship (Orville, Discovery, Curie_SNW, Computer_Enterprise, HoloDeck_Cerritos, HoloJaneway_Protostar), A3 = Crew (35 agents A3)",
        "defini_dans": "05_From_V2_Domains/00_Amadeus/05_OSS_TSTwin/symphony/L1/INDEX_specs.md (🛡️ A1 — Gatekeepers (2) · 🚀 A2 — Ships (6) · 🛠️ A3 — Crews (35))"
    },
    {
        "systeme": "H1/H3/H10/H30/H90 (Horizons)",
        "numerote": "H1=Weekly_PnL, H3=quarterly runway (Saru), H10=Vision (Pike/Una/Chapel H10), H30=Kardashev, H90=Kardashev-4 Legacy 1000T",
        "defini_dans": "05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/00_index.md (horizon: H1_Weekly_PnL) + 04_From_V2_Root/ARCHITECTURE_STRUCTURE.md (H1_Sovereignty, H3_Agency_as_a_Service, H10_DIKW_Wisdom, H30_Kardashev, H90_Kardashev_4)"
    },
    {
        "systeme": "W01-W12 (12 Week Year cadence, weekly)",
        "numerote": "12 Week Year cycle (06/15 → 09/07/26 par exemple) avec sprint W1-W12 (5 disciples: Pike Vision 1/5, Una Planning 2/5, M'Benga Focus 3/5, Chapel Measure 4/5, Ortegas Execution 5/5)",
        "defini_dans": "04_From_V2_Root/_SPECS/ADR/L1_Life_OS/ADR-Meta-000_12-week-year-cycle-doctrine_DRAFT.md (cycle: 12WY 06/15 - 09/07/26) + 03_Memory_Unified/LLM_Wiki/wiki/hand_offs/architecture_triptyque_morty_2026-06-21.md (5 disciples SNW)"
    },
    {
        "systeme": "ADR-<NAMESPACE>-<NNN> (Architectural Decision Record)",
        "numerote": "ADR-{LAYER}_{DOMAIN}_{NNN}_{slug}.md — ex: ADR-META-001, ADR-LOOP-001, ADR-CANON-001, ADR-SOBER-002, ADR-AAAS-PRICING-001, ADR-L2-AAAS-001, ADR-L2-PAPERCLIPAI-001, ADR-FWK-021, ADR-MESH-L2-001",
        "defini_dans": "05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-FWK-021_blueprints-canon-tripartite.md (Convention nommage immuable : `<TYPE>-<NAMESPACE>-<NNN>_<kebab-case>.md`)"
    },
    {
        "systeme": "JTBD-<NNN> (Jobs To Be Done) — `01_Guides/PROJECTS/JTBD-001`, JTBD-002, JTBD-003, JTBD-004",
        "numerote": "4 JTBD par défaut (JTBD-001 thin possible, 002/003/004 instantiables selon funnel client). Tier-dependent: Legal-gate flag pour compliance-bound projects",
        "defini_dans": "06_Claude_Code_Bare/skills/picard-growth-jtbd-launch/references/special-cases.md (compliance-bound projects: Add `legal_gate: true` to JTBD-003 and JTBD-004 frontmatter)"
    },
    {
        "systeme": "B1/B2/B3 + LD01-LD08 bijection",
        "numerote": "8 B2 ↔ 8 LD via ADR-L2-BDLD-MAP-001 : 01_Product→LD04_Cognition_Tilly, 02_Ops→LD02_Finance_Saru, 03_IT→LD07_Creativity_Reno, 04_Finance→LD02_Finance_Saru, 05_Legal→LD03_Health_Culber, 06_Sales→LD01_Business_Picard, 07_Growth→LD08_Impact_Georgiou, 08_People→LD06_Family_Burnham",
        "defini_dans": "01_Guides/01_Product/_INDEX.md (sister_canon: ADR-L2-BDLD-MAP-001 (Product ↔ LD04_Cognition_Tilly bijection))"
    },
    {
        "systeme": "L0/L1/L2/L3 (Layer architecture)",
        "numerote": "L0=Teck_OS (Kernel), L1=Life_OS (Fleet), L2=Business_OS (Projects), L3=?",
        "defini_dans": "00_Index/SECOND_BRAIN_PARA_MAP.md + 05_From_V2_Domains/00_Amadeus/00_Amadeus.README.md (🏛️ The Sovereign Architecture (Layers): L0 The Bedrock, L1 Life OS, L2 Business OS, L3?)"
    },
    {
        "systeme": "S0-S4 (Strates mémoire)",
        "numerote": "S0=Identité (CLAUDE.md, AGENTS.md, MEMORY.md), S1=court terme (hand_offs/), S2=travail (_CAPTURE_2026-08-01/), S3=canon (wiki, Plans, harness, agents), S4=maître (graphify-out/, 00_Index/)",
        "defini_dans": "00_Index/SECOND_BRAIN_PARA_MAP.md (Strate mapping — 14 sous-dossiers ↔ S0-S4)"
    },
    {
        "systeme": "Kardashev Type 1-4 + Solar Level",
        "numerote": "K1=planétaire, K2=stellaire, K3=galactique (Saru 1000T), K4=universel (Solar Level + Skill Ecosystem)",
        "defini_dans": "04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-KARDASHEV-TYPE-FRACTAL-001_multiverse-architecture_RATIFIED_2026-07-16.md"
    },
    {
        "systeme": "5 Piliers AaaS (Operations / IT / Finance / Content / Acquisition)",
        "numerote": "5 piliers canon par pilier AaaS — ex: Operations 5 Piliers (Persona · Metrics · Pricing · Harness · Solo Business)",
        "defini_dans": "04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-OPERATIONS-CANON-001_aaas-operations-canon.md"
    },
    {
        "systeme": "5 Tiers AaaS Pricing (Solarpunk)",
        "numerote": "$300 / $750 / $1500 / $3000-5000 / $50K MRR (USD post-accuponcture) — Tiers PME Solo Founder → Orbiter Enterprise",
        "defini_dans": "04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-001_aaas-pricing-canon.md (Pricing canon : 5 Tiers Solarpunk)"
    },
    {
        "systeme": "3 Variants AaaS (Solaris / Nexus-OMK / Orbiter-ABC)",
        "numerote": "Solaris (Visual First / DAM), Nexus-OMK (Coaching / ICP 4/5), Orbiter-ABC (Mobile First / Terrain Hybrid)",
        "defini_dans": "04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md"
    },
    {
        "systeme": "3 Strates × 10 Catégories ICP",
        "numerote": "Strate A (Coachs C-Suite, Leadership grand volume, M&A/transition), Strate B (B1/B2/B3 — Deep Research Gemini), Strate C (Fractional COOs, SOP vaulting, Gestion patrimoine B2B, Conduite du changement). 10 catégories total.",
        "defini_dans": "04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-NEXUS-10-ICP-001_3-strates-10-cibles-canon.md"
    },
    {
        "systeme": "Soul/Agent/Heartbeat/Tools/Context (5 fichiers par agent capsule)",
        "numerote": "5 fichiers par agent × 35 A3 + 6 A2 + 2 A1 = 215 fichiers capsules totaux (Phase 1: 40 fichiers, Phase 2: 175 fichiers)",
        "defini_dans": "05_From_V2_Domains/00_Amadeus/05_OSS_TSTwin/symphony/L1/INDEX_capsules.md (Template canon : 5 fichiers par agent: Soul / Agent / Heartbeat / Tools / Context)"
    },
    {
        "systeme": "8 Domaines Business",
        "numerote": "01_Product, 02_Ops, 03_IT, 04_Finance, 05_Legal, 06_Sales, 07_Growth, 08_People — 8 Domaines canon AaaS",
        "defini_dans": "01_Guides/01_Product/_INDEX.md (8 Domaines canon, 8 LDxx Life Wheel bijection via ADR-L2-BDLD-MAP-001)"
    },
    {
        "systeme": "D1-D12 (Doctrine Anti-Paresse)",
        "numerote": "D1=verify-before-assert, D2=cite source, D3=nuance over literal, D4=append-only, D5=real-test-after-edit, D6=no-hallucination root-cause, D7=anti-paperclip cost-of-escalation, D8=honest gaps, D9-D12=self-choice autonomy",
        "defini_dans": "04_From_V2_Root/_SPECS/ADR/INDEX.md + ADR-META-001 (D1-D8) + ADR-META-002 (D9-D12)"
    },
    {
        "systeme": "Tier T0-T2 (Enterprise OS Blueprint)",
        "numerote": "T0 Hobby (solo, $65-95/mo), T1 Standard ($300/mo, small firm), T2 Pro (PHI/HIPAA, $600/mo + write-once audit)",
        "defini_dans": "02_Templates/Enterprise_OS_Blueprint_Kit/specs/ARCHITECTURE_SPEC.md"
    },
    {
        "systeme": "Type 0/1/2/3/4/5 (Dark Factory levels)",
        "numerote": "Type 0 (manual), Type 1 (assisted), Type 2 (single-agent), Type 3 (multi-agent), Type 4 (full autonomy gated), Type 5 (continuous reasoning)",
        "defini_dans": "05_From_V2_Domains/20_Life_OS/22_Wheel_Discovery/LD01_Business_Book/99_meta/doctrine_lock_map.md (BC-True-Autonomy: Eero Alvar (continuous reasoning) × Cole Medin (5 niveaux) — Phase 1 sandbox → Phase 3 L5 gated Rick S1)"
    }
]

# === CONTRADICTIONS ===
v3["contradictions"] = [
    {
        "sujet": "3 referents 'Paperclip' polysémique",
        "chemin_a": "04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-PAPERCLIPAI-002_anti-paperclip-irony-doctrine.md",
        "date_a": "2026-07-11",
        "chemin_b": "04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-PAPERCLIPAI-001_governance-mirror-doctrine.md",
        "date_b": "2026-07-11"
    },
    {
        "sujet": "ADR-MEM-001 ID collision (Memory Fabric vs IndexedDB Cloisonnement)",
        "chemin_a": "04_From_V2_Root/_SPECS/ADR/L1_Life_OS/ADR-MEM-001_memory-fabric-unified-doctrine.md",
        "date_a": "2026-06-15",
        "chemin_b": "04_From_V2_Root/_SPECS/ADR/L1_Life_OS/ADR-MEM-002_wiki-lifewheel-mapping-doctrine.md",
        "date_b": "2026-06-21"
    },
    {
        "sujet": "Count des jonctions NTFS (47 vs 159)",
        "chemin_a": "00_Index/JUNCTIONS_MAP_2026-08-02.md",
        "date_a": "2026-08-02",
        "chemin_b": "00_Index/JUNCTIONS_MAP_2026-08-02.md",
        "date_b": "2026-08-02"
    },
    {
        "sujet": "EUR vs USD pricing (ADR-AAAS-PRICING-001 amended)",
        "chemin_a": "04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-001_aaas-pricing-canon.md (Hypothèse A USD post-accuponcture SUPERSEDE EUR)",
        "date_a": "2026-06-24",
        "chemin_b": "04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-AAAS-PRICING-001_aaas-pricing-canon.md (Takeout 2026-05 L28276-28328 EUR historique — Solaris 25€/mois, Nexus 750€/an, Orbiter 1555€/an)",
        "date_b": "2026-05 (Takeout)"
    },
    {
        "sujet": "Sister v2 vs v3 RH-META-GOUVERNANCE-001 (Yggdrasil fold)",
        "chemin_a": "04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-RH-META-GOUVERNANCE-001-canonical-v2_PROPOSED_2026-07-25.md",
        "date_a": "2026-07-25",
        "chemin_b": "04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-RH-META-GOUVERNANCE-001-canonical-v3_RATIFIED_2026-07-26.md",
        "date_b": "2026-07-26"
    },
    {
        "sujet": "01_Guides (LD06_Family_Burnham vs LD01_Business Picard) — _kIxjlEf_0U.md file declares `ld: LD06_Family_Burnham, domain: 06_Sales`",
        "chemin_a": "01_Guides/06_Sales/_INDEX.md",
        "date_a": "2026-07-03",
        "chemin_b": "01_Guides/06_Sales/_INDEX.md",
        "date_b": "2026-07-03"
    },
    {
        "sujet": "8 Domaines canon (1 par LDxx bijection) vs 7 domaines historiques (1 manquant : Sales / Illuminati / John Jones)",
        "chemin_a": "04_From_V2_Root/_SPECS/ADR/INDEX.md (8 Domaines canon ratifiés batch 2026-06-21)",
        "date_a": "2026-06-21",
        "chemin_b": "(SDD-006_business-pulse-l2-pyramide.md, brief signale 7 domaines historiques vs canon 8)",
        "date_b": "(anterior)"
    },
    {
        "sujet": "Geordi 03 (Ressources) sister Geordi 04 (variant TSTwin corrompu) — deux dossiers jumeaux avec contenu légèrement divergent",
        "chemin_a": "05_From_V2_Domains/00_Amadeus/05_OSS_TSTwin/symphony/L1/INDEX_specs.md",
        "date_a": "2026-06-07",
        "chemin_b": "05_From_V2_Domains/00_Amadeus/05_OSS_Twin/symphony/L1/INDEX_specs.md",
        "date_b": "2026-06-07"
    },
    {
        "sujet": "Roster: AGENTS.md 4-member squads vs B3 transcriptions 8-member squads (CANON-001 Notion prime)",
        "chemin_a": "04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-CANON-001_roster-source-of-truth.md",
        "date_a": "2026-06-02",
        "chemin_b": "00_Amadeus/01_Identity_Core/AGENTS.md (abbreviated 4-member squads)",
        "date_b": "(anterior)"
    },
    {
        "sujet": "MAP count (5 vs 8) domaines canon business, ADR-L2-BDLD-MAP-001 vs ADR-L2-AAAS-001",
        "chemin_a": "04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-AAAS-001_aaas-doctrine-3-variants-solarpunk.md (mapping 3 variants ↔ LD01+LD02+LD06 = Picard+Book, Saru, Burnham)",
        "date_a": "2026-06-21",
        "chemin_b": "04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-RH-META-GOUVERNANCE-001-canonical-v2_PROPOSED_2026-07-25.md (Domain 01 RH & Méta-Gouv = Green Lantern × X-Men canonical alignment)",
        "date_b": "2026-07-25"
    },
    {
        "sujet": "5 A3 SNW vs A2 SNW Curie twin manquant (D4 self-contradiction)",
        "chemin_a": "03_Memory_Unified/LLM_Wiki/wiki/hand_offs/architecture_triptyque_morty_2026-06-21.md (5 A3 SNW réfèrent à A2 SNW Curie manquant)",
        "date_a": "2026-06-21",
        "chemin_b": "05_From_V2_Domains/00_Amadeus/05_OSS_TSTwin/symphony/L1/INDEX_specs.md (A2 Curie SNW ACTIVE twin)",
        "date_b": "2026-06-15"
    },
    {
        "sujet": "Calibration Routine tasks EXEMPT (D6 lesson from Multica over-fire 2026-07-16)",
        "chemin_a": "04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-PAPERCLIPAI-004_paperclip-calibration-doctrine_RATIFIED_2026-07-16.md",
        "date_a": "2026-07-16",
        "chemin_b": "04_From_V2_Root/_SPECS/ADR/L2_Business_OS/ADR-L2-PAPERCLIPAI-001_governance-mirror-doctrine.md",
        "date_b": "2026-07-11"
    },
    {
        "sujet": "geordi 01_Guides 11 PREMIUM Batches non reclassifiés (détour principal)",
        "chemin_a": "01_Guides/_BATCH_RECLASSIFICATION_INDEX.md",
        "date_a": "2026-07-03",
        "chemin_b": "01_Guides/01_Product/_INDEX.md (squelettes existent pour 8 sous-domaines, mais 11 Batches en vrac à la racine)",
        "date_b": "2026-07-03"
    },
    {
        "sujet": "Yann Leonardi INDEX statut V0_HEURISTIC vs V1 (b1_filter appliqué partiellement)",
        "chemin_a": "01_Guides/07_Growth/Yann_Leonardi/INDEX_QA_REPORT.md (V0_HEURISTIC, QA_REQUIRED)",
        "date_a": "2026-07-03",
        "chemin_b": "01_Guides/07_Growth/Yann_Leonardi/YANN_CORPUS_INDEX.md (b1_filter: APPLIED_E1_DETERMINISTIC)",
        "date_b": "2026-07-03"
    }
]

# Write JSON
out = json.dumps(v3, ensure_ascii=False, indent=2)
with open(os.path.join(CARTO, "03_Resources_Geordi_v3.json"), "w", encoding="utf-8") as fh:
    fh.write(out)
print("JSON written, types:", len(v3["types"]), "relations:", len(v3["relations"]), "codes:", len(v3["codes"]), "contradictions:", len(v3["contradictions"]))
