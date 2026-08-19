---
type: Concept
title: ClaudeClaw OS Blueprint Kit V2 — superseded en entier par le Mission Control Kit V3
description: Kit V2 de 5 fichiers MD + 1 PDF qui est entièrement remplacé par ClaudeClaw Mission Control Kit V3 — collision de nommage entre les deux kits, à noter.
tags: [templates, claudeclaw, supersession, v2, v3, collision, naming]
generated: { by: minimax-m3, at: 2026-08-19T19:40:00Z }
verified:
  - { by: process:comparaison_kits_v2_vs_v3, at: 2026-08-19T19:40:00Z }
sources:
  - id: claudeclaw-v2-bluerpint-kit-listing
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/ClaudeClaw OS Blueprint Kit"
    title: "Dossier ClaudeClaw OS Blueprint Kit (5 fichiers)"
    last_modified: 2026-02
  - id: claudeclaw-v2-assessment-prompt
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/ClaudeClaw OS Blueprint Kit/CLAUDECLAW_ASSESSMENT_PROMPT.md"
    title: "ClaudeClaw V2 — assessment prompt"
    last_modified: 2026-02
  - id: claudeclaw-v2-powerpacks-guide
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/ClaudeClaw OS Blueprint Kit/POWER_PACKS_GUIDE.md"
    title: "ClaudeClaw V2 — power packs guide"
    last_modified: 2026-02
  - id: claudeclaw-v3-rebuild-prompt
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/02_Templates/ClaudeClaw Mission Control Kit/REBUILD_PROMPT_V3.md"
    title: "ClaudeClaw V3 — preuve que V3 supersede V2"
    last_modified: 2026-05
okf_version: "0.2"
---

# ClaudeClaw OS Blueprint Kit V2 — superseded

## Périmètre

5 fichiers `.md` + 1 PDF (`ClaudeClaw_v2_Visual_Guide.pdf`) :

| Fichier | Contenu succinct |
|---|---|
| `CLAUDECLAW_ASSESSMENT_PROMPT.md` | audit d'une installation V2 existante, ~185 lignes |
| `POWER_PACKS.md` | 8 packs V2 (memory v2, multi-agent, war room, mission control, security, voice upgrade, dashboard, meeting bot) |
| `POWER_PACKS_GUIDE.md` | description longue de chaque pack V2 (~456 lignes) |
| `REBUILD_PROMPT_V2.md` | méga-prompt de bootstrap V2 |
| `ClaudeClaw_v2_Visual_Guide.pdf` | visuels des packs V2 |

## Verdict

**`superseded`**, par : `ClaudeClaw Mission Control Kit V3`.

**Preuve :** le Mission Control Kit V3 contient un fichier `CLAUDECLAW_ASSESSMENT_PROMPT_V3.md` (avec suffixe `_V3` dans le nom même), un `POWER_PACKS_V3.md` (12 packs V3), un `REBUILD_PROMPT_V3.md` (avec suffixe `_V3` dans le nom), et un `_V3_BLUEPRINT.md`. La convention de nommage `_V3` explicite que ce sont les successeurs des fichiers V2.

## Collision de nommage à noter

Les deux kits coexistent dans le même dossier `02_Templates/` avec des **noms ambigus** :

- `ClaudeClaw OS Blueprint Kit` → c'est le **V2** (février 2026)
- `ClaudeClaw Mission Control Kit` → c'est le **V3** (mai 2026)

Un distillateur futur cherchant « ClaudeClaw blueprint » pourrait tomber sur le V2 en premier et le tenir pour canon. Risque réel. La mitigation est dans ce concept : **le V2 est superseded, et seul le V3 fait foi.**

## Comparaison V2 vs V3 (synthèse)

| Dimension | V2 (OS Blueprint Kit) | V3 (Mission Control Kit) |
|---|---|---|
| Modèle LLM cible | `claude-sonnet-4-6` (V2) | `claude-sonnet-4-6` (idem, conservé) |
| Modèle embeddings | `gemini-embedding-001` | `gemini-embedding-001` (idem) |
| Mémoire | 5-layer retrieval | 3-layer (FTS5 + embeddings + salience) — plus simple |
| Kill switches | 6 + intégration dans `bot.ts` | 6 + singleton hot-reload via `kill-switches.ts` |
| Voice | STT Groq/TTS cascade (4 providers) | inchangé |
| Nombre de packs | 8 | 12 (avec ajout Suggestions, Auto-Assign, Backup/Restore, CLI Integration Pattern) |
| Bridge | Telegram + Slack + Discord | inchangé |
| Audit log | single SQLite table | append-only + 90-day retention + periodic prune |

Le V3 est un **raffinement** du V2, pas une rupture. Les patterns fondamentaux sont les mêmes ; le V3 ajoute des garde-fous supplémentaires (Suggestions, Kill Switches hot-reload, Audit Log structuré).

## Concepts liés

- [[concept-claudeclaw-mission-control-kit]] — le successeur canon
- [[concept-five-cross-cutting-patterns]] — patterns qui apparaissent dans V2 et V3
