---
source: backfilled 2026-06-06 (hygiene lint remediation)
date: 2026-05-26
type: handoff
domain: handoff
title: Handoff — Symphony Cluster Implementation
tags: [#handoff #hand_offs #backfilled]
---

# Handoff — Symphony Cluster Implementation

**Date :** 2026-05-26
**Émetteur :** A2 Claude Code
**Destinataire :** A0 Amadeus + Codex_CLI / Gemini_CLI / Claude_Code_CLI (capsules)
**Statut :** Doctrine PRÊTE — implémentation en 4 phases

## Pré-requis vérifiés

- [x] ADR-SYMPH-001 (bus doctrine) ratifié
- [x] ADR-SYMPH-002 (variants harness) ratifié
- [x] ADR-HEART-002 (anti-panique) ratifié
- [x] SPEC.md amendé (autorisation conditionnelle OpenClaw/Paperclip)
- [x] Shadow_L0 propagation (rapport #04)
- [x] LLM_Wiki entities + log

## Plan d'implémentation

### Phase 0 — Activation mode lean (1 min)

**Action immédiate** : créer `Shadow_L0/MODE.txt` avec le seul mot `lean`.

```powershell
Set-Content -Path "C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Shadow_L0\MODE.txt" -Value "lean"
```

Watchdog (quand créé) lira ce fichier à chaque tick pour décider de l'activation OpenClaw/Paperclip.

### Phase 1 — AntiPanicGuards.psm1 (~2h)

Module PowerShell à créer dans `.claude/bin/AntiPanicGuards.psm1`. Implémente les 11 gardes du tableau ADR-HEART-002 §D1.

Squelette (à coder par Codex_CLI ou Claude_Code_CLI) :

```powershell
function Guard-Type1-ApprovalFreeze { param($Capsule) ... }
function Guard-Type2-BudgetHardStop { param($Capsule) ... }
function Guard-Type3-DMPairingBlock { ... }
function Guard-Type4-WebSocketTimeout { ... }
function Guard-K1-FilesystemBlindness { ... }
function Guard-K2-HallucinationSucces { ... }  # Read-After-Write
function Guard-K3-SecretLeak401 { ... }
function Guard-K4-DeadKernel { ... }
function Write-AndVerify { ... }  # Helper RAW
Export-ModuleMember -Function *
```

Intégration dans `heartbeat-tick.ps1` :
```powershell
Import-Module "$PSScriptRoot\AntiPanicGuards.psm1" -Force
# Au début de chaque phase
Guard-Type1-ApprovalFreeze -Capsule $AgentDir
```

Tester d'abord en dry-run sur `Codex_CLI`.

### Phase 2 — Donna DLQ refonte (~1h)

Créer la structure :
```powershell
$dlq = "C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Shadow_L0\donna_dlq"
foreach ($sub in @('pending','retried','failed')) {
  New-Item -ItemType Directory -Path (Join-Path $dlq $sub) -Force
}
```

Documenter format JSON dans `Shadow_L0/DONNA_PROTOCOL.md` (cf. ADR-HEART-002 §D6).

### Phase 3 — Capsule Yaz_Watchdog (~1h)

```
Shadow_L0/agents/Yaz_Watchdog/
├── AGENTS.md             ← définit budget + scope
├── Context.md            ← rôle, anchors
├── memory/
│   ├── inbox/
│   ├── outbox/
│   └── pulse.log
└── skills/
    ├── sweep-donna.ps1
    ├── verify-tick-cycles.ps1
    ├── check-mode-conditions.ps1
    └── INDEX.md
```

Task Scheduler entry :
```
Name: ASpace-Yaz-Watchdog
Trigger: Every 5 minutes (24/7)
Action: powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\Users\amado\.claude\bin\heartbeat-tick.ps1" -Agent Yaz_Watchdog
```

### Phase 4 — Modes bridged/full (DIFFÉRÉ)

**Ne PAS activer maintenant**. Triggers d'activation :

- **bridged** : A0 a un besoin concret de DM pairing (ex: bot Telegram qui doit dialoguer en pairing avec un agent)
- **full** : A0 veut budget management agressif par mission (Paperclip)

Avant activation, vérifier que toutes les conditions C1-C4 (OpenClaw) ou P1-P4 (Paperclip) sont satisfaites. Watchdog Yaz refusera l'activation sinon.

## Délégation suggérée

| Phase | Agent recommandé | Pourquoi |
|-------|------------------|----------|
| Phase 0 | A0 manuel (1 min) | Trivial, valeur symbolique de l'activation |
| Phase 1 | Codex_CLI (PowerShell surgical) | Domaine 13th Doctor, idéal pour module système |
| Phase 2 | Codex_CLI | Création arborescence + protocole |
| Phase 3 | Claude_Code_CLI | Mise en place capsule complète + Task Scheduler |

## Critères de succès cluster

Cluster Symphony est verrouillé "stable" quand :
- [ ] Phase 0-3 implémentées
- [ ] 3 ticks consécutifs des 3 CLI capsules sans erreur (24h sans Watchdog incident)
- [ ] `donna_dlq/pending/` reste vide pendant 24h en charge normale
- [ ] `LLM_Wiki/wiki/log.md` reçoit ≥ 1 entry par jour (Kernel vivant)

## Lien avec ADR-NOTION-001

Une fois cluster verrouillé, ADR-NOTION-001 peut entrer en **Phase 2** : sync Notion → Supabase via Symphony skill sur capsule `Claude_Code_CLI` (11th Doctor, owner sync Produit). Skill suggéré : `agents/Claude_Code_CLI/skills/sync-notion-to-supabase.ps1`.

## Références

- ADR-SYMPH-001 / SYMPH-002 / HEART-002
- SDD-001 (anchor anti-panique)
- Shadow_L0/04_symphony-cluster-and-heartbeat-anti-panique-20260526.md
- `.claude/bin/heartbeat-tick.ps1` (à étendre)
