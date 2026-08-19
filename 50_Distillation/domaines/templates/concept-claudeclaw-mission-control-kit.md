---
type: Concept
title: ClaudeClaw Mission Control Kit — le kit complet V3, daté sur la nomenclature et canon sur les patterns
description: Kit de 13 fichiers MD + 1 PDF + sous-skill memory/ qui assemble l'architecture Hive Mind V3 — daté sur les références Claude/Gemini, canon sur les patterns agents+skills+SQLite, kill switches, audit log, three-layer memory.
tags: [templates, claudeclaw, hive-mind, kill-switches, audit-log, three-layer-memory, datation, supersession]
generated: { by: minimax-m3, at: 2026-08-19T19:35:00Z }
verified:
  - { by: process:lecture_kit_claudeclaw_v3_integral, at: 2026-08-19T19:35:00Z }
sources:
  - id: brief-vague2-templates
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/_briefs_vague2/BRIEF_templates.md"
    title: "Brief vague 2 — distillation Templates (9 kits)"
    last_modified: 2026-08-19
  - id: claudeclaw-readme
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/ClaudeClaw Mission Control Kit/README.md"
    title: "ClaudeClaw Mission Control Kit — README"
    last_modified: 2026-05
  - id: claudeclaw-v3-blueprint
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/ClaudeClaw Mission Control Kit/CLAUDECLAW_V3_BLUEPRINT.md"
    title: "Hive Mind Blueprint (architecture)"
    last_modified: 2026-05
  - id: claudeclaw-rebuild-prompt-v3
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/ClaudeClaw Mission Control Kit/REBUILD_PROMPT_V3.md"
    title: "ClaudeClaw V3 — Rebuild Mega Prompt"
    last_modified: 2026-05
  - id: claudeclaw-power-packs-v3
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/ClaudeClaw Mission Control Kit/POWER_PACKS_V3.md"
    title: "Power Packs V3 (12 packs modulaires)"
    last_modified: 2026-05
  - id: claudeclaw-blueprint-v2-superseded
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/ClaudeClaw OS Blueprint Kit/POWER_PACKS_GUIDE.md"
    title: "ClaudeClaw V2 — preuve de la supersession par V3"
    last_modified: 2026-02
okf_version: "0.2"
---

# ClaudeClaw Mission Control Kit — V3 complet

## Périmètre

13 fichiers `.md` + 1 PDF + sous-dossier `memory/` (SKILL.md + 3 références), totalisant **18 fichiers utiles** (hors `__MACOSX/`).

| Fichier | Rôle | Verdict |
|---|---|---|
| `README.md` | index, 3 paths d'usage (A rebuild / B upgrade / C community) | canon |
| `DISCLAIMER.md` | conditions d'usage, « expérimental mai 2026 » | canon (à conserver) |
| `CLAUDECLAW_V3_BLUEPRINT.md` | architecture en 3 couches (bridge / wrapper / brain) + 4 ingrédients | canon |
| `REBUILD_PROMPT_V3.md` | méga-prompt de bootstrap (TLDR → 6 questions → build) | canon |
| `CLAUDECLAW_ASSESSMENT_PROMPT_V3.md` | audit read-only d'une installation existante | canon |
| `POWER_PACKS_V3.md` | **12 power packs** modulaires (Pack 01–12) | canon |
| `5_STEP_JOURNEY.md` | parcours 5 étapes (acknowledge → untangle → hierarchy → orchestration) | canon |
| `POWER_PACKS_V3.md` + `terminal_prompts.md` | one-liners SQL/bash | canon |
| `memory/SKILL.md` | sous-skill memory (FTS5 + embeddings + salience) | canon |
| `memory/references/{infrastructure_options, paradigms, repo_patterns}.md` | références pour le sous-skill | canon |
| `ClaudeClaw_V3_Visual_Guide.pdf` | visuel des 8 packs emblématiques | synthese-datee (visuels mai 2026) |

## Verdict global

**`synthese-datee`** — daté sur la nomenclature, canon sur les patterns.

**Daté sur :**
- La marque « ClaudeClaw » et le terme central « Hive Mind » — A'Space V3 n'utilise ni l'un ni l'autre.
- Le modèle cité `claude-sonnet-4-6` et la version « Gemini-3-flash-preview » — références de mai 2026, qui auront évolué.
- Les références à la communauté payante `https://www.skool.com/earlyaidopters/about` — A'Space est un chantier distinct.

**Canon sur :**
- L'architecture 3 couches (Bridge / Wrapper / Brain) et les 4 ingrédients (agents / skills / database / bridge).
- La base SQLite en WAL mode + 5-second busy timeout comme « toute l'histoire IPC ».
- Le pattern agent-as-folder (un agent = un dossier avec `agent.yaml` + `CLAUDE.md`).
- Le pattern skill-as-folder (auto-discovery par l'orchestrateur).
- Les 6 kill switches et leurs frontières.
- Le pattern audit-log append-only avec 90-day retention.
- L'exfiltration guard (15 patterns regex sur les sorties).
- Le pattern three-layer memory (FTS5 + embeddings + salience, rank fusion).

## Les 12 Power Packs (la vraie richesse du kit)

Le fichier `POWER_PACKS_V3.md` est le sous-ensemble le plus **réutilisable** du kit, car chaque pack est auto-contenu et peut être copié-collé indépendamment dans un projet Claude Code.

| Pack | Ce qu'il impose |
|---|---|
| 01 War Room (Text) | `/standup` + `/discuss` + table `warroom_transcript` |
| 02 Kill Switches | 6 env vars hot-reload, refresh sur `.env` mtime |
| 03 Audit Log | table `audit_log` append-only, 90-day retention |
| 04 Suggestions | job quotidien Gemini Flash, `suggestions` table |
| 05 Auto-Assign | classifier Gemini Flash, cache par hash |
| 06 Three-Layer Memory | FTS5 + embeddings + salience, decay sweep |
| 07 Exfiltration Guard | 15 regex patterns, kill switch `EXFIL_GUARD_ENABLED` |
| 08 Scheduled Tasks | cron + UI friendly, `scheduled_tasks` table |
| 09 Hive Mind Visualizations | list + 2D graph + 3D brain (optionnelle) |
| 10 CLI Integration Pattern | skill folder pour chaque CLI global |
| 11 Telegram Bridge Setup | polling + token par agent |
| 12 Backup and Restore | cron + restore script (off-line only) |

## Ce que ce kit **n'a pas** fait dans A'Space V3

Aucun artefact du corpus V3 ne porte la marque de ce kit. Vérification par grep dans `ASpace_OS_V3/` :
- Pas de `warroom_transcript` ni de table SQLite à la ClaudeClaw.
- Pas de `agents/<id>/CLAUDE.md` à la ClaudeClaw (V3 utilise une autre structure).
- Pas de référence à `claude-sonnet-4-6` ou au terme « Hive Mind ».

C'est un **moule utilisé comme référence de design**, mais aucun de ses 12 power packs n'a été déployé en V3. V3 a son propre équivalent local : SQLite, `agents/<capitaine>/`, et `kill-switches.py` qui ne vient pas de ce kit.

## Concepts liés

- [[concept-claudeclaw-os-blueprint-v2-superseded]] — la version V2 que ce kit supersede
- [[concept-five-cross-cutting-patterns]] — les patterns que ce kit partage avec d'autres
- [[concept-kits-utilisation-trace]] — la trace (nulle) de ce kit dans V3
