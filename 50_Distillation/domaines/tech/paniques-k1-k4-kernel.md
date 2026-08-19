---
type: Concept
title: Taxonomie des 8 paniques Framework + Kernel
description: 4 paniques Framework (approval, budget, DM pairing, WS timeout) + 4 paniques Kernel (filesystem blindness, hallucination, secret leak, dead kernel). Chaque panique a un antidote systémique.
tags: [tech, paniques, taxonomy, kernel, framework]
generated: { by: minimax-m3, at: 2026-08-19T12:00:00Z }
verified:
  - { by: process:read, at: 2026-08-19T12:00:00Z }
sources:
  - id: sdd-001-paniques
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-001_solarpunk-kernel-core.md
    title: SDD-001 § 1.2 Taxonomie 4+4 paniques
    last_modified: 2026-04-27
  - id: sdd-001-antidotes
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-001_solarpunk-kernel-core.md
    title: SDD-001 § 8 Les 4 Antidotes
    last_modified: 2026-04-27
  - id: heart-002
    resource: 05_From_V2_Domains/10_Tech_OS/12_Blueprints/02-ADR/ADR-HEART-002_heartbeat-anti-panique-openclaw-paperclip.md
    title: ADR-HEART-002 instrumentation tick
    last_modified: 2026-05-26
okf_version: "0.2"
---

La genèse de l'architecture L0 est l'**effondrement Hermes** d'avril 2026 (un agent en défaillance a paralysé le Kernel, forçant A0 à intervenir manuellement). SDD-001 §1.2 cartographie 8 types de paniques, répartis en deux groupes.

## 4 paniques Framework

| Type | Symptôme | Cause | Antidote |
|------|----------|-------|----------|
| **TYPE 1** Approval Freeze | Claude Code attend `[o/s/D]` → timeout | `bypassPermissions` non configuré ou commande hors `permissions.allow` | `defaultMode: "bypassPermissions"` + `permissions.allow` exhaustif + `dangerously-skip-permissions` |
| **TYPE 2** Budget Hard-Stop | Paperclip gelé en attente review | `budget` non défini dans AGENTS.md | Définir `soft_limit` + `hard_limit` explicites + `escalate_to_human: false` |
| **TYPE 3** DM Pairing Block | OpenClaw ignore messages | `dmPolicy: "pairing"` + `allowFrom: []` | `dmPolicy: "open"` + `allowFrom` whitelist des agents internes |
| **TYPE 4** WebSocket Timeout | Multica tasks mortes | `docker-compose.yml` absent ou mal déployé | `docker compose up -d` + healthcheck WS sur endpoint connu |

## 4 paniques Kernel

| Type | Symptôme | Cause | Antidote |
|------|----------|-------|----------|
| **TYPE K1** Filesystem Blindness | Agent écrit, lit un path différent | Pas de verify_write post-écriture | Helper `verify_write()` dans chaque script A3 |
| **TYPE K2** Hallucination Succès | EXIT 0 sans Read-After-Write | Pas de lecture indépendante post-écriture | Axiome 1 — Write-AndVerify sur tout write critique |
| **TYPE K3** Secret Leak 401 | Token expiré, handler absent, boucle muette | Variable d'env absente + pas de check_env_vars | `check_env_vars` fail-fast → exit 1 + DLQ Donna |
| **TYPE K4** Dead Kernel | L0 zombie, Donna sans récepteur actif | DLQ inactive > 5 min | `graham-dead-mans-switch.sh` cron */5 min → alerte A0 |

## Cartographie phases tick → gardes (ADR-HEART-002)

| Phase | Panique adressée | Garde |
|-------|------------------|-------|
| WAKE | T1 | Read `Context.md` + check `pending_approvals.json` |
| PROBE | K4, K3 | Ping `LLM_Wiki/wiki/log.md` + probe MCP critique |
| DECIDE | T2, T3 | Verify AGENTS.md + DM channel timeout < 30s |
| EXECUTE | K1, K2 | `Write-AndVerify` helper + read-after-write |
| OBSERVE | T4 | WS timeout 60s + fallback file-based |
| LEARN | toutes | Append WIKI.md, Pattern × 3 → Skill Hermes Nous |
| SIGNAL | K4 | Heartbeat ping `pulse.log` parent |
| SLEEP | toutes | Cleanup `outbox/.done/` > 7j |

## Modes d'opération (HEART-002 D5)

| Mode | OpenClaw | Paperclip | Cas d'usage |
|------|----------|-----------|------------|
| `lean` (défaut) | OFF | OFF | Setup minimal Symphony — 3 capsules CLI suffisent |
| `bridged` | ON (C1-C4) | OFF | DM pairing Telegram / bots externes |
| `full` | ON (C1-C4) | ON (P1-P4) | Production scale-up — budget par mission |

Mode **lean** par défaut, **bridged/full** activés seulement sur besoin concret (gating A0 via `Shadow_L0/MODE.txt`).

## Pourquoi cette taxonomie

L'**anti-panique par instrumentation tick** est moins coûteux que la réaction post-mortem : chaque phase a 1+ gardes explicites, mesurables par lecture de `pulse.log`. Le reproche « daemon obscurs » adressé à N8N ne s'applique plus — l'observabilité est native.

Voir aussi : [[axiomes-antifragilite-k1-k4]], [[symphony-bus-replace-n8n]], [[mcp-doctrine-six]].