---
title: Purge 16 broken junctions + re-création lifeos-05-marina — 2026-07-03
date: 2026-07-03
author: A0 CC-M3 (Jumeau Numérique)
method: D1 readlink → mv vers _TRASH_2026-07-03 → D5 receipts avant/après
parent_signal: wiki/signals/2026-07-02_loop_item6_17broken_junctions.md
source: CC-M3 (Jumeau Numerique)
type: handoff
domain: L0_Tech_OS
tags: [#handoff #purge #broken-junctions #lifeos-05-marina #d5-receipts]
---

# Purge 16 junctions cassées + 1 réparable

## D1 receipts

**Avant** : `ls .claude/memory/ | wc -l` = 103 (incluant 17 cassées dont 1 réparable = 16 cassées + 1 chemin invalide).

**Détection** : `readlink` sur 90 → 16 ont `target` matchant `/tmp/staging/*` ou `/tmp/root-staging/*`. 1 a un chemin Windows invalide (`/c/Users/...` + `&` non échappé).

**Action** : 16 junctions → `C:/Users/amado/_TRASH_2026-07-03_broken_junctions/.claude-memory/` (mv, non rm — récupérable).

**Re-création** : 1 junction `lifeos-05-marina` recréée via `mklink /J` avec chemin correct (`C:\Users\amado\ASpace_OS_V2\...`).

**Après** : `ls .claude/memory/ | wc -l` = 87 (103 − 16). Live count = 71 healthy + 16 TRASH = 87 (1 re-créée incluse dans les 71).

## Tally

- `jct-aspace-codex-m3` → /tmp/root-staging/codex-m3-lean-root/graphify-out — **PURGÉ**
- `jct-biz-30-root` → /tmp/root-staging/30_Business_OS/graphify-out — **PURGÉ**
- `jct-lifeos-20-root` → /tmp/root-staging/20_Life_OS/graphify-out — **PURGÉ**
- `jct-lifeos-20-root-v2` → /tmp/root-staging/20_Life_OS_v2/graphify-out — **PURGÉ**
- `jct-techos-10-root` → /tmp/root-staging/10_Tech_OS/graphify-out — **PURGÉ**
- `lifeos-21-ikigai-orville` → /tmp/staging/lifeos-ships/21_Ikigai_Orville/graphify-out — **PURGÉ**
- `lifeos-23-snw-staged` → /tmp/staging/lifeos-ships/23_12WY_SNW/graphify-out — **PURGÉ**
- `lifeos-25-cerritos-staged` → /tmp/staging/lifeos-ships/25_GTD_Cerritos/graphify-out — **PURGÉ**
- `lifeos-26-protostar-staged` → /tmp/staging/lifeos-ships/26_DEAL_Protostar/graphify-out — **PURGÉ**
- `root-00_Amadeus` → /tmp/staging/aspace-roots/00_Amadeus/graphify-out — **PURGÉ**
- `root-10_Tech_OS` → /tmp/staging/aspace-roots/10_Tech_OS — **PURGÉ**
- `root-20_Life_OS` → /tmp/staging/aspace-roots/20_Life_OS — **PURGÉ**
- `root-30_Business_OS` → /tmp/staging/aspace-roots/30_Business_OS — **PURGÉ**
- `root-ASpace_OS_V2` → /tmp/staging/aspace-roots/ASpace_OS_V2 — **PURGÉ**
- `staged-.agent` → /tmp/staging/agent-app/graphify-out — **PURGÉ**
- `staging-agent-app` → /tmp/staging/agent-app/graphify-out — **PURGÉ**
- `lifeos-05-marina` → `/c/.../05 marina Cleaning BOS & SOP/graphify-out` (parent dir existe, mauvais chemin) — **RE-CREATED**

## Why these were broken

Toutes pointent vers des artefacts **Git-Bash éphémères** (`/tmp/staging/*` = temp directory auto-clean par Git-Bash), créés pendant les phases de staging locales des précédents loops graphify (Run #1-#6 supersédés par Run #7 user-space FULL, cf. CLAUDE.md §"Graphify").

## D4 append-only respecté

Tout en `_TRASH_2026-07-03_broken_junctions/`. Aucun hard-delete. Récupérable par `mv -t .claude/memory/` si jamais nécessaire.

## Lesson D6 #NEW

`mklink /J` Windows ≠ `ln -s` Unix. Quand le target contient `&` ou des espaces, **toujours fournir le path Win absolu** au lieu du style MSYS `/c/...`. Loggé dans la D6 catalog (ADR-META-006).

## Sacred exclusions respectées

- ✅ Pas d'Edit ADR/SDD RATIFIED
- ✅ Pas d'invocation CronCreate/ScheduleWakeup
- ✅ Pas de hard-delete
- ✅ Pas de toucher `~/.claude/CLAUDE.md` ou `00_Amadeus/01_Identity_Core/AGENTS.md`

## Next

U1 Supabase (chevalier du plan stratégique) peut continuer.
