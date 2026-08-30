# Cartographie de A'Space OS V3

> Genere par `scripts/cartographier_v3.py` le 2026-08-30 04:30 UTC, en 0.3 s.
> **Ne pas editer a la main** : une carte ecrite a la main vieillit et ment.
> Regenerer par `python scripts/cartographier_v3.py`.

## Le corpus en un coup d'oeil

| | |
|---|---|
| Fichiers | **10,731** |
| Poids | **2.8 Go** |
| Documents `.md` | **6,531** |
| Triplets `.ttl` | 31 |
| Substrat `.jsonl` | 45 |
| Scripts `.py` | 282 |

Exclus du compte : `.cache`, `.git`, `.mypy_cache`, `.next`, `.nuxt`, `.obsidian`, `.pytest_cache`, `.venv`, `__pycache__`, `build`, `coverage`, `dist`, `node_modules`, `openwiki`, `site-packages`, `target`, `vendor`, `venv`.

`openwiki/` est exclu volontairement : c'est un **clone amont** avec son
propre `.git`, pas une partie du corpus. Le compter melangerait un depot
etranger au notre.

## Les etages de premier niveau

| Etage | Fichiers | dont `.md` | Poids | Ce qu'il porte |
|---|---:|---:|---:|---|
| `00_Amadeus/` | 5,132 | 4,705 | 228.7 Mo | Ontologie V2, MEMORY_CORE, cartographie des contradictions, sessions |
| `10_Tech_OS/` | 97 | 71 | 2.2 Mo | Gouvernance Rick, cascade E-Myth |
| `20_Life_OS/` | 361 | 291 | 1.0 Go | Domaines de vie migres depuis V2 |
| `30_Business_OS/` | 3,750 | 538 | 1.3 Go | Projets, blueprints, coach-os |
| `40_Memory_Wiki_OKF/` | 36 | 36 | 239.5 Ko | Bundle OKF v0.2 — integrations, operations, securite, learning |
| `50_Distillation/` | 362 | 299 | 69.9 Mo | Methode, substrat, briefs de distillation |
| `60_Implementation_Méthodologiques/` | 173 | 76 | 1.3 Mo | Verdicts du triptyque par domaine |
| `70_Onthologies/` | 396 | 324 | 6.8 Mo | Sujets, triplets RDF, revue |
| `80_Agent-OS/` | 7 | 2 | 64.3 Ko | Observabilite — tableaux de revue et schema de cadence |
| `_ARCHIVE_coach-os-briefs/` | 349 | 154 | 109.2 Mo | Briefs archives de coach-os |
| `_INBOX/` | 9 | 5 | 10.9 Ko | Capture GTD, non trie |
| `_REVIEW_NOTEBOOKLM/` | 26 | 26 | 4.7 Mo | 26 sources consolidees pour la revue humaine |
| `scripts/` | 27 | 0 | 235.1 Ko | Porte d'argent, cartographie, generateurs |
| *(racine)* | 6 | 4 | 33.4 Ko | fichiers de tete |

## Arborescence, 3 niveaux

```
ASpace_OS_V3/
|-- 00_Amadeus/  (5132 fich., 4705 md, 228.7 Mo)
|   |-- 10_Observers/  (9 fich., 3.7 Ko)
|   |   |-- _placeholder_agent-os_2026-08-06/  (1 fich.)
|   |   |-- agent-os/  -> JONCTION (non suivie)
|   |   |-- agent-super-spy/  (1 fich.)
|   |   |-- agentpulse/  (1 fich.)
|   |   |-- agents-observe/  (1 fich.)
|   |   |-- aios/  (1 fich.)
|   |   |-- langsmith/  (1 fich.)
|   |   |-- opik/  (1 fich.)
|   |   |-- phoenix/  (1 fich.)
|   |   |-- pocketbase-vec/  -> JONCTION (non suivie)
|   |   `-- super-simple-software-factory/  -> JONCTION (non suivie)
|   |-- 20_Harness/  (300 fich., 33 md, 110.2 Mo)
|   |   |-- agentgateway/  (24 fich., 95.4 Mo)
|   |   |-- antigravity/  (1 fich.)
|   |   |-- bmad-loop/  (225 fich., 28 md, 9.5 Mo)
|   |   |   ... 5 sous-dossiers, non deplies
|   |   |-- buzz/  (1 fich.)
|   |   |-- cc/  (1 fich.)
|   |   |-- codex/  (1 fich.)
|   |   |-- herdr/  (1 fich.)
|   |   |-- hermes/  (1 fich.)
|   |   |-- multica/  (1 fich.)
|   |   |-- multica_export_2026-08-02/  (18 fich., 3.5 Mo)
|   |   |-- omnigent/  (1 fich.)
|   |   |-- openrouter/  (11 fich., 1 md, 54.3 Ko)
|   |   |   ... 1 sous-dossiers, non deplies
|   |   |-- orca/  (1 fich.)
|   |   |-- paperclip/  (2 fich., 1 md, 3.6 Ko)
|   |   `-- routers/  (6 fich., 1.8 Mo)
|   |-- 30_MEMORY_CORE/  (4794 fich., 4670 md, 118.5 Mo)
|   |   |-- carto/  (103 fich., 17 md, 7.8 Mo)
|   |   |   ... 1 sous-dossiers, non deplies
|   |   `-- sessions_md/  (4647 fich., 4647 md, 109.8 Mo)
|   |       ... 304 sous-dossiers, non deplies
|   |-- 30_Shadow/  (3 fich., 578 o)
|   |   |-- l0-omnigent/  (1 fich.)
|   |   `-- l1-agent-zero/  (1 fich.)
|   |-- 40_Predictions/  (2 fich.)
|   |   |-- pending/  (1 fich.)
|   |   `-- scored/  (1 fich.)
|   |-- 50_Bench/  (2 fich.)
|   |   |-- ceo-bench/  (1 fich.)
|   |   `-- vec/  (1 fich.)
|   |-- 60_Tape_Specs/  (16 fich., 1 md, 427 o)
|   |   |-- ADR/  (7 fich.)
|   |   |   ... 6 sous-dossiers, non deplies
|   |   |-- MCP/  (1 fich.)
|   |   |   ... 1 sous-dossiers, non deplies
|   |   |-- PRD/  (1 fich.)
|   |   |-- REGISTRY/  (1 fich.)
|   |   |-- graphify-out/  (2 fich.)
|   |   |   ... 2 sous-dossiers, non deplies
|   |   |-- hand_offs/  (1 fich.)
|   |   `-- heartbeat/  (1 fich.)
|   |-- 70_Skills/  (4 fich.)
|   |   |-- goal-loop/  (1 fich.)
|   |   |-- multi-session/  (1 fich.)
|   |   `-- mythos/  (1 fich.)
|   `-- 90_Doctrine/  (1 fich.)
|       `-- adr/  (1 fich.)
|-- 10_Tech_OS/  (97 fich., 71 md, 2.2 Mo)
|   |-- 00_Governance_Rick/  (35 fich., 22 md, 2.0 Mo)
|   |   |-- Donna_DLQ/  (1 fich., 1 md, 308 o)
|   |   `-- replicator/  (7 fich., 5 md, 21.8 Ko)
|   |       ... 1 sous-dossiers, non deplies
|   |-- 11_Kernel_Core_13th/  (16 fich., 15 md, 34.4 Ko)
|   |   |-- compagnons/  (10 fich., 10 md, 26.0 Ko)
|   |   |   ... 3 sous-dossiers, non deplies
|   |   `-- tapes/  (1 fich.)
|   |-- 12_Life_Core_11th/  (16 fich., 15 md, 23.6 Ko)
|   |   |-- compagnons/  (9 fich., 9 md, 9.9 Ko)
|   |   |   ... 3 sous-dossiers, non deplies
|   |   `-- tapes/  (2 fich., 1 md, 3.7 Ko)
|   |       ... 1 sous-dossiers, non deplies
|   |-- 13_Buzz_Core_12th/  (18 fich., 17 md, 21.4 Ko)
|   |   |-- compagnons/  (12 fich., 12 md, 13.1 Ko)
|   |   |   ... 3 sous-dossiers, non deplies
|   |   `-- tapes/  (1 fich.)
|   `-- kernel/  (10 fich., 1 md, 94.3 Ko)
|       `-- agentpulse/  -> JONCTION (non suivie)
|-- 20_Life_OS/  (361 fich., 291 md, 1.0 Go)
|   |-- 00_Gatekeepers_Beth_Morty/  (8 fich., 7 md, 35.6 Ko)
|   |   |-- Beth_Alignment_Log/  (1 fich., 1 md, 4.7 Ko)
|   |   |-- Morty_Global_Queue/  (1 fich., 1 md, 5.5 Ko)
|   |   `-- Sunday_Uplink_Protocols/  (1 fich., 1 md, 5.3 Ko)
|   |-- 21_Ikigai_Orville/  (53 fich., 53 md, 78.3 Ko)
|   |   |-- 01_Pillars_Identity/  (21 fich., 21 md, 26.2 Ko)
|   |   |   ... 4 sous-dossiers, non deplies
|   |   `-- 02_Horizons_Time/  (26 fich., 26 md, 29.5 Ko)
|   |       ... 5 sous-dossiers, non deplies
|   |-- 22_Wheel_Discovery/  (113 fich., 109 md, 3.1 Mo)
|   |   |-- LD01_Business_Book/  (72 fich., 68 md, 3.0 Mo)
|   |   |   ... 6 sous-dossiers, non deplies
|   |   |-- LD02_Finance_Saru/  (5 fich., 5 md, 7.2 Ko)
|   |   |-- LD03_Health_Culber/  (5 fich., 5 md, 6.2 Ko)
|   |   |-- LD04_Cognition_Tilly/  (5 fich., 5 md, 6.3 Ko)
|   |   |-- LD05_Social_Stamets/  (5 fich., 5 md, 6.2 Ko)
|   |   |-- LD06_Family_Burnham/  (6 fich., 6 md, 11.2 Ko)
|   |   |-- LD07_Creativity_Reno/  (5 fich., 5 md, 5.8 Ko)
|   |   `-- LD08_Impact_Georgiou/  (5 fich., 5 md, 6.4 Ko)
|   |-- 23_12WY_SNW/  (28 fich., 28 md, 61.4 Ko)
|   |   |-- 01_Vision_Pike/  (4 fich., 4 md, 5.4 Ko)
|   |   |-- 02_Planning_Una/  (4 fich., 4 md, 5.4 Ko)
|   |   |-- 03_Focus_MBenga/  (4 fich., 4 md, 5.9 Ko)
|   |   |-- 04_Metrics_Chapel/  (4 fich., 4 md, 5.9 Ko)
|   |   `-- 05_Execution_Ortegas/  (4 fich., 4 md, 6.1 Ko)
|   |-- 24_PARA_Enterprise/  (108 fich., 47 md, 1.0 Go)
|   |   |-- 00_Links/  (1 fich.)
|   |   |-- 01_Projects_Picard/  (2 fich., 2 md, 2.3 Ko)
|   |   |-- 02_Areas_Spock/  (3 fich., 3 md, 4.8 Ko)
|   |   |-- 03_Resources_Geordi/  (91 fich., 31 md, 1.0 Go)
|   |   |   ... 4 sous-dossiers, non deplies
|   |   `-- 04_Archives_Data/  (3 fich., 3 md, 5.6 Ko)
|   |-- 25_GTD_Cerritos/  (25 fich., 25 md, 41.5 Ko)
|   |   |-- 01_Inbox_Mariner/  (4 fich., 4 md, 4.9 Ko)
|   |   |-- 02_Clarify_Boimler/  (4 fich., 4 md, 4.6 Ko)
|   |   |-- 03_Organize_Rutherford/  (4 fich., 4 md, 6.0 Ko)
|   |   |-- 04_Review_Tendi/  (4 fich., 4 md, 5.5 Ko)
|   |   `-- 05_Engage_Freeman/  (4 fich., 4 md, 5.3 Ko)
|   |-- 26_DEAL_Protostar/  (21 fich., 21 md, 36.1 Ko)
|   |   |-- 01_Definition_Dal/  (4 fich., 4 md, 4.9 Ko)
|   |   |-- 02_Elimination_RokTahk/  (4 fich., 4 md, 4.9 Ko)
|   |   |-- 03_Automation_Zero/  (4 fich., 4 md, 5.0 Ko)
|   |   `-- 04_Liberation_Gwyn/  (4 fich., 4 md, 5.0 Ko)
|   `-- 28_Blueprints/  (4 fich.)
|       |-- 01-SDD/  (1 fich.)
|       |-- 02-ADR/  (1 fich.)
|       |-- 03-PRD/  (1 fich.)
|       `-- 04-DDD/  (1 fich.)
|-- 30_Business_OS/  (3750 fich., 538 md, 1.3 Go)
|   |-- 00_Jerry_Business_Pulse/  (1 fich.)
|   |-- 00_Summers_QuickAccess/  (1 fich.)
|   |-- 00_Summers_Verse/  (1 fich.)
|   |-- 02_Meta_Factory/  (1 fich.)
|   |-- 09_Blueprints/  (2784 fich., 234 md, 1.3 Go)
|   |   |-- agentic-os/  (116 fich., 13 md, 99.1 Mo)
|   |   |   ... 8 sous-dossiers, non deplies
|   |   |-- coach-os-refonte/  (794 fich., 194 md, 497.4 Mo)
|   |   |   ... 11 sous-dossiers, non deplies
|   |   |-- gateways/  (6 fich., 4 md, 100.2 Ko)
|   |   |-- ontologie-trois-couches/  (12 fich., 2 md, 91.0 Ko)
|   |   |-- ontologie-vocale/  (373 fich., 6 md, 214.0 Mo)
|   |   |   ... 3 sous-dossiers, non deplies
|   |   |-- outils-micro-saas/  (74 fich., 3 md, 74.0 Mo)
|   |   |   ... 2 sous-dossiers, non deplies
|   |   |-- palantir-2.0/  (1055 fich., 1 md, 253.1 Mo)
|   |   |   ... 4 sous-dossiers, non deplies
|   |   `-- vision-v1/  (353 fich., 11 md, 180.7 Mo)
|   |       ... 4 sous-dossiers, non deplies
|   `-- 10_Projects/  (960 fich., 303 md, 20.7 Mo)
|       `-- coach-os-app/  (959 fich., 303 md, 20.7 Mo)
|           ... 29 sous-dossiers, non deplies
|-- 40_Memory_Wiki_OKF/  (36 fich., 36 md, 239.5 Ko)
|   |-- architecture/  (7 fich., 7 md, 47.7 Ko)
|   |-- canon/  (4 fich., 4 md, 40.1 Ko)
|   |-- integrations/  (8 fich., 8 md, 79.9 Ko)
|   |-- learning/  (2 fich., 2 md, 8.9 Ko)
|   |-- operations/  (8 fich., 8 md, 40.7 Ko)
|   `-- security/  (3 fich., 3 md, 10.6 Ko)
|-- 50_Distillation/  (362 fich., 299 md, 69.9 Mo)
|   |-- _briefs/  (24 fich., 16 md, 145.2 Ko)
|   |-- _briefs_domaines/  (14 fich., 9 md, 84.7 Ko)
|   |-- _briefs_vague2/  (14 fich., 9 md, 83.4 Ko)
|   |-- _mesures/  (4 fich., 33.1 Ko)
|   |-- _substrat/  (25 fich., 1 md, 65.5 Mo)
|   |-- _substrat_domaines/  (9 fich., 4 md, 1.7 Mo)
|   |-- archives/  (17 fich., 17 md, 86.4 Ko)
|   |-- areas/  (22 fich., 22 md, 136.0 Ko)
|   |-- domaines/  (161 fich., 161 md, 654.8 Ko)
|   |   |-- amadeus/  (32 fich., 32 md, 103.6 Ko)
|   |   |-- business/  (20 fich., 20 md, 93.0 Ko)
|   |   |-- life/  (21 fich., 21 md, 87.1 Ko)
|   |   |-- life-wheel/  (18 fich., 18 md, 75.3 Ko)
|   |   |-- normatif-adr/  (20 fich., 20 md, 80.8 Ko)
|   |   |-- normatif-sdd-prd/  (20 fich., 20 md, 80.7 Ko)
|   |   |-- tech/  (16 fich., 16 md, 57.4 Ko)
|   |   `-- templates/  (14 fich., 14 md, 77.0 Ko)
|   |-- ontologie/  (20 fich., 9 md, 1.3 Mo)
|   |-- projets/  (21 fich., 21 md, 96.5 Ko)
|   `-- ressources/  (27 fich., 27 md, 129.8 Ko)
|-- 60_Implementation_Méthodologiques/  (173 fich., 76 md, 1.3 Mo)
|   |-- _briefs/  (5 fich., 3 md, 19.3 Ko)
|   |-- _loop/  (100 fich., 28 md, 914.7 Ko)
|   |-- _sources/  (2 fich., 2 md, 12.4 Ko)
|   |-- autonomie-agents/  (6 fich., 6 md, 27.9 Ko)
|   |-- domaines/  (28 fich., 8 md, 131.1 Ko)
|   |-- frameworks/  (6 fich., 6 md, 39.8 Ko)
|   |-- primitives/  (3 fich., 1 md, 17.5 Ko)
|   |-- prompt-systeme/  (8 fich., 8 md, 32.1 Ko)
|   `-- protocoles/  (12 fich., 12 md, 112.9 Ko)
|-- 70_Onthologies/  (396 fich., 324 md, 6.8 Mo)
|   |-- _briefs/  (24 fich., 15 md, 150.7 Ko)
|   |-- _revue/  (30 fich., 9 md, 170.4 Ko)
|   |-- _structure/  (3 fich., 1 md, 595.7 Ko)
|   |-- pulse/  (298 fich., 298 md, 3.7 Mo)
|   |   |-- b1/  (15 fich., 15 md, 127.5 Ko)
|   |   |-- b2/  (12 fich., 12 md, 109.9 Ko)
|   |   |-- b3/  (11 fich., 11 md, 118.5 Ko)
|   |   `-- domaines/  (259 fich., 259 md, 3.3 Mo)
|   |       ... 8 sous-dossiers, non deplies
|   |-- sujets/  (20 fich., 1.6 Mo)
|   |-- triplets/  (19 fich., 626.8 Ko)
|   `-- verbes/  (0 fich.)
|-- 80_Agent-OS/  (7 fich., 2 md, 64.3 Ko)
|   |-- donnees/  (2 fich., 1 md, 13.2 Ko)
|   |   |-- mermaid/  (1 fich., 1 md, 3.2 Ko)
|   |   `-- schema/  (1 fich., 10.0 Ko)
|   `-- tableaux/  (4 fich., 47.2 Ko)
|       `-- reviews/  (3 fich., 36.7 Ko)
|-- _ARCHIVE_coach-os-briefs/  (349 fich., 154 md, 109.2 Mo)
|   `-- _briefs/  (349 fich., 154 md, 109.2 Mo)
|       |-- 2026-08-09_prod/  (14 fich., 12 md, 72.9 Ko)
|       |-- 2026-08-10_audit_crud/  (10 fich., 7 md, 60.8 Ko)
|       |-- 2026-08-10_dettes/  (8 fich., 6 md, 35.9 Ko)
|       |-- 2026-08-10_vague2/  (11 fich., 9 md, 77.1 Ko)
|       |-- 2026-08-10_vague3/  (12 fich., 10 md, 58.4 Ko)
|       |-- 2026-08-11_production/  (221 fich., 53 md, 108.3 Mo)
|       |   ... 4 sous-dossiers, non deplies
|       |-- 2026-08-15_AUDIT_LOG/  (3 fich., 3 md, 22.2 Ko)
|       |-- 2026-08-15_AUTH_FIX/  (3 fich., 3 md, 17.2 Ko)
|       |-- 2026-08-15_MEMBERSHIPS/  (3 fich., 3 md, 29.5 Ko)
|       |-- 2026-08-15_W03_fermeture/  (3 fich., 3 md, 21.4 Ko)
|       |-- 2026-08-15_W13_QUOTAS/  (3 fich., 3 md, 16.5 Ko)
|       |-- 2026-08-15_WORKSPACE_BRANCHES/  (3 fich., 3 md, 27.6 Ko)
|       |-- 2026-08-15_saas_builder_v1/  (1 fich., 1 md, 26.3 Ko)
|       |-- 2026-08-16_WARGAME_ANTIFRAGILITE/  (8 fich., 8 md, 41.9 Ko)
|       |-- 2026-08-17_APPS_IFRAME/  (4 fich., 3 md, 43.4 Ko)
|       |-- 2026-08-17_CANON_UUID/  (4 fich., 2 md, 23.0 Ko)
|       |-- 2026-08-17_CORRECTIFS_M3/  (26 fich., 17 md, 199.6 Ko)
|       `-- 2026-08-17_PENTEST_M3/  (12 fich., 8 md, 98.3 Ko)
|-- _INBOX/  (9 fich., 5 md, 10.9 Ko)
|   |-- A1_Beth_Morty/  (2 fich., 1 md, 8.7 Ko)
|   |-- B1_Jerry_Summers/  (1 fich.)
|   |-- S1_Rick/  (1 fich.)
|   |-- _admis/  (1 fich., 1 md, 427 o)
|   |   `-- B1_Jerry_Summers/  (1 fich., 1 md, 427 o)
|   `-- _refuses/  (2 fich., 2 md, 603 o)
|       `-- S1_Rick/  (2 fich., 2 md, 603 o)
|-- _REVIEW_NOTEBOOKLM/  (26 fich., 26 md, 4.7 Mo)
`-- scripts/  (27 fich., 235.1 Ko)
```

## Ou vit reellement la connaissance

Deux classements, parce qu'un seul mentirait. Les vidages de sessions
ecrasent tout en volume sans etre de la connaissance **redigee**.

### Connaissance redigee (hors sessions)

| Dossier | `.md` |
|---|---:|
| `30_Business_OS/09_Blueprints/coach-os-refonte` | 70 |
| `_ARCHIVE_coach-os-briefs/_briefs/2026-08-11_production` | 52 |
| `70_Onthologies/pulse/domaines/wonder-woman` | 35 |
| `70_Onthologies/pulse/domaines/green-lantern` | 35 |
| `70_Onthologies/pulse/domaines/flash` | 35 |
| `70_Onthologies/pulse/domaines/batman` | 33 |
| `70_Onthologies/pulse/domaines/superman` | 32 |
| `50_Distillation/domaines/amadeus` | 32 |
| `70_Onthologies/pulse/domaines/john-jones` | 30 |
| `70_Onthologies/pulse/domaines/cyborg` | 30 |
| `70_Onthologies/pulse/domaines/aquaman` | 28 |
| `60_Implementation_Méthodologiques/_loop` | 28 |

### Vidages de sessions (matiere premiere, pas connaissance)

| Dossier | `.md` |
|---|---:|
| `00_Amadeus/30_MEMORY_CORE/sessions_md/_recuperees_claude` | 2,305 |
| `00_Amadeus/30_MEMORY_CORE/sessions_md/_03_Resources_Geordi_06_Claude_Code_Bare/projects/C--Users-amado/de35c5f1-6944-47f6-b8bc-849452b0313a/subagents` | 412 |
| `00_Amadeus/30_MEMORY_CORE/sessions_md/C--Users-amado-ASpace-OS-V2-20-Life-OS-24-PARA-Enterprise-03-Resources-Geordi-05-From-V2-Domains-30-Business-OS-10-Projects-omk-repos-coach-os` | 150 |
| `00_Amadeus/30_MEMORY_CORE/sessions_md/_03_Resources_Geordi_06_Claude_Code_Bare/_ARCHIVE_2026-06-16_sessions/projects/C--Users-amado/9627821e-356b-43f0-b67d-695b6e8979c9/subagents` | 88 |
| `00_Amadeus/30_MEMORY_CORE/sessions_md/C--Users-amado-ASpace-OS-V3` | 85 |

### Le point qui compte

Le `CLAUDE.md` designe `40_Memory_Wiki_OKF/` comme « la memoire du
poste ». Ce bundle porte **36 fichiers `.md` sur 6,531**, soit **0.6 %** du corpus.

Chercher la et s'arreter, c'est manquer le reste. Le bundle est un
**index de concepts consolides**, pas le corpus. Les deux tableaux
ci-dessus disent ou chercher avant lui.

## Comment verifier que cette carte dit vrai

```bash
python C:/Users/amado/ASpace_OS_V3/scripts/cartographier_v3.py
```

Si un compte differe d'un `find` sur le corpus, c'est **l'instrument**
qu'il faut reparer, pas le chiffre qu'il faut ajuster.
