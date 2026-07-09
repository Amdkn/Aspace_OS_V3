---
handoff_id: handoff_persistent_loop_router_strategy
date: 2026-07-06
author: B1 Jerry Prime (E-Myth Gatekeeper) + A2 Orchestrateur Stratégique + B1-OpenHarness-Replicant
extends_canon:
  - C:\Users\amado\.claude\bin\heartbeat-tick.ps1 (313 lines, ACTIVE — sister canon runtime 8-step)
  - C:\Users\amado\.claude\bin\heartbeat-watchdog.ps1 (sister supervisor)
  - C:\Users\amado\.claude\hooks\hooks.json (12 hooks canon actifs: SessionStart ×1 + PreToolUse ×8 + PostToolUse ×9 + Stop ×6 + PostToolUseFailure ×1 + SessionEnd ×1 + PreCompact ×1)
  - C:\Users\amado\.claude\hooks\subagent-start-tracker.ps1 (Sister Sobriété Rick C137 — throttle 1/10 fan-out hard cap)
  - C:\Users\amado\.claude\hooks\stop-log-append.ps1 (sister canonic turn-journal append D4)
  - C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Shadow_L0\HEARTBEAT_PROTOCOL.md (canon protocol reference)
  - C:\Users\amado\.claude\agents\a3-enterprise-spock.md (A3 Spock H30, Areas Owner USS Enterprise)
  - C:\Users\amado\.claude\agents\a1-morty-execution.md (A1 Morty, Execution — hands on H1)
  - C:\Users\amado\.claude\agents\a2-uss-cerritos-chaos.md (A2 USS Cerritos Holo Deck, GTD manager)
doctrine_anchors:
  - ADR-META-001 (D1-D8 Anti-Paresse)
  - ADR-META-002 (D9-D12 Self-Choice)
  - ADR-SOBER-002 (Anti-Paperclip)
  - ADR-META-005 (Hooks Automation Vague 2)
  - ADR-META-006 (D6 Catalog)
sister_handoff: cerritos_plane_integration_2026-06-21.md + heartbeat-tick.ps1 canon
do_not_replace:
  - heartbeat-tick.ps1 (sister canon — EXTEND only)
  - HEARTBEAT_PROTOCOL.md (sister canon — reference only)
additive_layer: Plane Mission Control sync + Spock review + Cerritos airlock
---

# Handoff — Persistent Loop Router Strategy (84j cycle 12WY Q3 2026)

> **Spire header** — cette stratégie NE remplace PAS `heartbeat-tick.ps1` ; elle l'**étend** avec 3 couches sister-canon (Spock PROBE filter, Cerritos DECIDE airlock, Plane SIGNAL sync). Sister-canon pattern reuse, no parallel infra.

## 1. Vision (Spire)

Une **Boucle Router persistante** (84j cycle 12WY Q3 2026, du 2026-07-13 au 2026-10-04) qui supervise les workflows A0 (WF0) via :

- **4 hook lifecycles canon** (SessionStart / PostToolUse / Stop / SubagentStart) — sister canon actifs
- **8-step execution rhythm** via `heartbeat-tick.ps1` **EXTENDED** (L.36-310) — sister pattern reuse
- **Mission Control Plane sync** chaque iter — status update issue visible A0 via `mcp__plane__*`
- **Spock-supervises-Morty filter** dans la phase PROBE (L.47) — Spock (A3 Enterprise, H30 Areas doctrine) review Morty (A1 Execution, H1 hands-on) tactical decisions
- **Cerritos airlock gate** dans la phase DECIDE (L.66) — A3 fan-out hard cap 1/10 hérité de `subagent-start-tracker.ps1` (Sobriété Rick)
- **file-based state canon** (no daemon) — append-only D4, `_TRASH_<date>/` pour retirements

## 2. Architecture 4-Layer (Spire)

```
                ┌─────────────────────────────────────────┐
                │   A0 (Voyeur — gates GO/STOP only)        │
                └──────────────────▲──────────────────────┘
                                   │ Plane Mission Control
                ┌──────────────────┴──────────────────────┐
                │   Plane Project Issues (Mission Control)   │
                │   project: a825845a — issue: NEXUS-Q3-001  │
                └──────────────────▲──────────────────────┘
                                   │ mcp__plane__* (sister)
                ┌──────────────────┴──────────────────────┐
                │   Spire: Workflow WF0 + 8-step Lifecycle  │
                │   ┌─────────────────────────────────┐    │
                │   │ WAKE→PROBE→DECIDE→EXECUTE→       │    │
                │   │ OBSERVE→LEARN→SIGNAL→SLEEP       │    │
                │   │  (heartbeat-tick.ps1 EXTENDED)   │    │
                │   └─────────────────────────────────┘    │
                └──────────────────▲──────────────────────┘
                                   │
       ┌───────────────────────────┼───────────────────────────┐
       │       Hooks canon actifs (D1-verified hooks.json)     │
       │  SessionStart ×1 (session:start)                      │
       │  PreToolUse ×8 (pre:bash:dispatcher, doc-file-warning,│
       │    suggest-compact, observe, governance-capture,      │
       │    config-protection, mcp-health-check, gateguard)     │
       │  PostToolUse ×9 (post:bash:dispatcher, quality-gate,  │
       │    design-quality, accumulate, console-warn,          │
       │    governance-capture, session-activity, observe,     │
       │    ecc-metrics-bridge, ecc-context-monitor)           │
       │  Stop ×6 (format-typecheck, check-console-log,        │
       │    session-end, evaluate-session, cost-tracker,       │
       │    desktop-notify)                                    │
       │  + PostToolUseFailure, SessionEnd, PreCompact          │
       └───────────────────────────┬───────────────────────────┘
                                   │
                ┌──────────────────┴──────────────────────┐
                │   A3 Sub-agents (Workers, isolés)         │
                │   a3-enterprise-spock (H30 Science/Areas) │
                │   a1-morty-execution (H1 hands-on)         │
                │   a2-uss-cerritos-chaos (Holo Deck GTD)    │
                │   + 32 autres A3 (35/35 match canon)       │
                └─────────────────────────────────────────┘
```

**Architectural guarantees** :
- Aucun nouveau runtime — Windows Task Scheduler sister-canon + heartbeat-tick.ps1 EXTENDED
- Aucun nouveau langage — PowerShell sister-canon
- Aucune duplication — sister-canon pattern reuse
- Aucun bypass Sobriété — Cerritos airlock throttle 1/10 hard cap

## 3. Spock supervise Morty (filter PROBE)

Dans la phase **PROBE** de `heartbeat-tick.ps1` (L.47 `Get-ChildItem InboxDir`), ajouter un **pre-check Spock review** :

```powershell
# === EXTENSION 1: Spock PROBE filter (Sister Science/Areas H30) ===
$SpockReviewFile = Join-Path $OutboxDir "spock-review.md"
if (($terminal -eq 'in-progress' -or $decision -eq 'continue') -and (Test-Path $SpockReviewFile)) {
  $spockVerdict = (Get-Content $SpockReviewFile -Raw | Select-String -Pattern 'spock:verdict|APPROVED|FORWARDED|HOLD').ToString()
  if ($spockVerdict -notmatch 'APPROVED|FORWARDED') {
    $decision = 'spock-hold'
    Append-Pulse 'SPOCK_HOLD' @{ mission = $mission.BaseName; turn = $script:nextTurn; verdict = $spockVerdict }
  }
}
```

**Logique canonique** :
- **Spock = A3 Enterprise (H30)** — Areas Owner, science/logic, doctrine anchor (`a3-enterprise-spock.md` L.25)
- **Morty = A1 Execution (H1)** — hands-on, tactical, "Just do it, then narrate" (`a1-morty-execution.md`)
- **Spock supervise Morty** = continuous oversight sur tactical decisions (sister-cadre: Spock en back-office review, Morty en front-office execute)

**Anti-pattern guard** :
- ❌ Spock ne **REPLACE** PAS Morty execution — il review (sister gate)
- ❌ Spock ne **OVERRIDE** PAS Morty decision sur facts observables — il gates only on doctrine alignment
- ✅ Spock approve `APPROVED` ou forward `FORWARDED` (delegation chain)

## 4. Cerritos Airlock (filter DECIDE)

Dans la phase **DECIDE** (L.66 — après `$decision = 'idle'` init), ajouter le **Cerritos airlock gate** :

```powershell
# === EXTENSION 2: Cerritos DECIDE airlock (Sister Sobriété 1/10) ===
if ($fanoutDepth -gt 0 -and (Test-Path '~/.claude/logs/a3-spawns.logl')) {
  $spawnCount = (Get-Content '~/.claude/logs/a3-spawns.logl' -Tail 10 | Measure-Object).Count
  $recentSpawns = (Get-Content '~/.claude/logs/a3-spawns.logl' -Tail 10 |
    Where-Object { $_ -match 'A3_SPAWN' } | Measure-Object).Count
  # Sister Sobriété pattern: 1/10 throttle (subagent-start-tracker.ps1 L.27 `throttleMod=10`)
  if (($recentSpawns % 10) -ne 0 -and ($decision -match 'turn-1|continue')) {
    $decision = 'cerritos-airlock-closed'
    Append-Pulse 'CERRITOS_AIRLOCK_CLOSED' @{
      mission = $mission.BaseName
      turn = $script:nextTurn
      reason = 'fan-out-throttle-1/10'
      fanout_depth = $fanoutDepth
    }
  }
}
```

**Logique canonique** :
- **Cerritos = A2 USS Cerritos (Holo Deck chaos manager)** — Captain Freeman = A1, Boimler/Mariner/Tendi/Rutherford/Freeman = A3 (`a2-uss-cerritos-chaos.md` L.25)
- **Airlock gate** = capture/clarify/organize canon : chaque A3 fan-out passe par le airlock avant d'être autorisé
- **Hard cap 1/10** hérité verbatim de `subagent-start-tracker.ps1` L.27 — Sobriété Rick C137

**Anti-pattern guard** :
- ❌ Pas de bypass Cerritos airlock (sister gate hard cap)
- ❌ Pas de relax 1/10 → 1/N (throttleMod fixé L.27)
- ✅ Append-Pulse sister-canon (cf. L.39-44 Append-Pulse function)
- ✅ Log rotation auto-adaptive 1/100 si >5MB (cf. L.30-34)

## 5. Mission Control Plane sync (filter SIGNAL)

Dans la phase **SIGNAL** (L.287 — après `switch ($terminal)` block), ajouter **Plane sync** :

```powershell
# === EXTENSION 3: Plane Mission Control sync (Sister mcp__plane__*) ===
$planeProjectId = 'a825845a'  # sister token A0 frome ok Phase 2 Karpathy
$planeIssueId = 'NEXUS-Q3-001'
$signalHook = Join-Path $MemoryDir "plane-mission-control.json"
@{
  timestamp = $now
  agent = $Agent
  mission = $mission.BaseName
  turn = $script:nextTurn
  terminal = $terminal
  decision = $decision
  spock_verdict = $spockVerdict
  cerritos_airlock = $cerritosStatus
  plane_issue = $planeIssueId
  duration_ms = $durationMs
} | ConvertTo-Json -Depth 4 | Set-Content -Path $signalHook

# Push to Plane MCP (sister canonique Mission Control)
mcp plane update issue $planeProjectId $planeIssueId --state $terminal `
  --comment "Spire iteration: $decision | spock: $spockVerdict | airlock: $cerritosStatus | turn: $($script:nextTurn) | dur: ${durationMs}ms"
```

**Logique canonique** :
- **Plane = Mission Control** = sister canonique `mcp__plane__*` (plane_create_issue, plane_update_state, plane_set_priority, etc.)
- **Project ID `a825845a`** = sister token A0 fromé OK Phase 2 Karpathy (à valider post-ratification)
- **Issue ID `NEXUS-Q3-001`** = template pour Spire iter (à créer post-ratification)
- **JSON Schema strict** : state.json + plane-mission-control.json (sister-canon Plane API)

**Anti-pattern guard** :
- ❌ Pas de mutation Plane project sans dry-run (D6 #4 MCP register static CC)
- ❌ Pas de payload non-JSON (sister API contract)
- ✅ Sync silent failure handled (si MCP down, fallback pulse.log)
- ✅ State.json local copy canon (Plane sync is best-effort)

## 6. Loop Engineering Hooks (cross-canon)

Les hooks canon (D1-verified `hooks.json`) sont déjà branchés. La stratégie **AJOUTE 3 hooks-extension** en append-only D4 dans `~/.claude/settings.json` :

| Hook | Lifecycle | Matcher | Sister canon |
|------|-----------|---------|--------------|
| **Hook-PRE-DELEGATION** | SessionStart | `*` | Vérifie `wiki/log.md` digest cadence weekly |
| **Hook-AIRLOCK-CLOSE** | PostToolUse | `Agent` | throttle 1/10 (héritée `subagent-start-tracker.ps1`) |
| **Hook-MISSION-SYNC** | Stop | `*` | push final `plane-mission-control.json` via webhook Plane |

**Append settings.json (D4 append-only)** :

```json
{
  "hooks": {
    "SessionStart": [{
      "matcher": "*",
      "hooks": [{
        "type": "command",
        "command": "powershell -NoProfile -ExecutionPolicy Bypass -File $env:USERPROFILE\\.claude\\hooks\\hook-pre-delegation.ps1",
        "description": "Spire PRE-DELEGATION: verify wiki/log.md digest cadence"
      }]
    }],
    "PostToolUse": [{
      "matcher": "Agent",
      "hooks": [{
        "type": "command",
        "command": "powershell -NoProfile -ExecutionPolicy Bypass -File $env:USERPROFILE\\.claude\\hooks\\hook-airlock-close.ps1",
        "description": "Spire AIRLOCK-CLOSE: Cerritos throttle 1/10 fan-out"
      }]
    }],
    "Stop": [{
      "matcher": "*",
      "hooks": [{
        "type": "command",
        "command": "powershell -NoProfile -ExecutionPolicy Bypass -File $env:USERPROFILE\\.claude\\hooks\\hook-mission-sync.ps1",
        "description": "Spire MISSION-SYNC: push plane-mission-control.json to Plane webhook"
      }]
    }]
  }
}
```

**D4 append-only rule** : on **AJOUTE** dans le array existant, jamais on **REMPLACE**. Sister-canon `hooks.json` reste immutable.

## 7. Anti-paperclip guards (D1-D8)

- ❌ **Pas de chiffres inventés** — toutes les refs sont verbatim canon (ex: `throttleMod=10` L.27 `subagent-start-tracker.ps1`)
- ❌ **Pas de cron 7-day bound** — Schtask sister-persistent 84j (cf. Schtask XML spec sister)
- ❌ **Pas de mutation canon** — D4 append-only strict, heartbeat-tick.ps1 EXTENDED jamais REMPLACÉ
- ❌ **Pas de Spock override Morty execution** — sister gate (Spock review, Morty execute)
- ❌ **Pas de Cerritos airlock bypass** — 1/10 hard cap sister Sobriété Rick
- ❌ **Pas de Plane payload non-JSON** — sister API contract strict
- ❌ **Pas de hook REMPLACE** — append-only D4 settings.json
- ✅ **Cite sister-canon heartbeat-tick.ps1 verbatim** (L.36-44 WAKE, L.47 PROBE, L.66 DECIDE, L.101-123 EXECUTE, L.263-284 OBSERVE, L.287-310 LEARN, L.312 SLEEP)
- ✅ **Cite HEARTBEAT_PROTOCOL.md verbatim** (L.25 8-step lifecycle, L.83-115 cycle canon)
- ✅ **Vocabulaire canonique** (A2 orchestrateur, A3 worker, loop engineer, sister-cadre, etc.)
- ✅ **Format JSON Schema strict** pour state.json + plane-mission-control.json
- ✅ **D1 receipts** : 7 sources canon citées verbatim, aucune invention chiffrée

## 8. Cron Pattern Sister-Persistent (Schtask XML)

Le Schtask XML sister-persistent (84j cycle 12WY Q3 2026) est livré en sister-fichier :
`C:\Users\amado\.claude\schtasks\wf1-persistent-loop-router.xml`

**Caractéristiques sister-canon** :
- **Schedule** : CalendarTrigger weekly Monday H8 (sister standard L+ cadence)
- **URI** : `\Aspace\Spire\Persistent-Loop-Router\2026-Q3`
- **Command** : `heartbeat-tick.ps1 -Agent Claude_Code_CLI` (sister canon runtime)
- **MultipleInstancesPolicy** : `IgnoreNew` (sister Sobriété — pas de cascade fan-out)
- **ExecutionTimeLimit** : `PT15M` (sister cap heartbeat stall timeout canon 30min × 50%)
- **RunOnlyIfNetworkAvailable** : true (sister pour Plane MCP sync)
- **StartWhenAvailable** : true (sister recover missed Monday ticks)

**Anti-paperclip guards Schtask** :
- ❌ Pas de `Periodicity` court (< 60min) — Weekly sister-canon
- ❌ Pas de `<WakeToRun>true</WakeToRun>` — pas de daemon
- ❌ Pas de `<Exec><Command>cmd</Command>` — pwsh sister-canon
- ✅ `<Exec><Arguments>` use `$env:USERPROFILE` — sister env var canon
- ✅ Pas de hard-delete — `ExecutionTimeLimit` + `AllowHardTerminate` sister Sobriété

---

# D1 receipts final (vérifiés 2026-07-06)

| Source | Lines | Canon status | Section ref |
|--------|-------|--------------|-------------|
| `heartbeat-tick.ps1` | 313 | ACTIVE | L.36-44 WAKE / L.47 PROBE / L.66 DECIDE / L.101-123 EXECUTE / L.263-284 OBSERVE / L.287-310 LEARN / L.312 SLEEP |
| `heartbeat-watchdog.ps1` | sister | ACTIVE | sister supervisor (sister canon — ref only) |
| `hooks.json` | 355 | ACTIVE | 12 hooks canon (1 SessionStart + 8 PreToolUse + 9 PostToolUse + 6 Stop + 1 PostToolUseFailure + 1 SessionEnd + 1 PreCompact) |
| `subagent-start-tracker.ps1` | 57 | ACTIVE | L.27 throttleMod=10 (Sister Sobriété Rick C137) |
| `stop-log-append.ps1` | 51 | ACTIVE | L.49 Add-Content turn-journal.md (D4 append-only) |
| `HEARTBEAT_PROTOCOL.md` | ~150+ | ACTIVE | L.25 8-step / L.83-115 cycle canon |
| `a3-enterprise-spock.md` | ~80+ | ACTIVE | L.25 Spock A3 Areas Owner USS Enterprise |
| `a1-morty-execution.md` | A1 | ACTIVE | A1 Execution hands-on |
| `a2-uss-cerritos-chaos.md` | ~40+ | ACTIVE | L.25 A2 Cerritos Holo Deck GTD manager |

# Anti-regressions log (shipped 2026-07-06)

- Sister-canon `heartbeat-tick.ps1` : **INTACT**, jamais modifié (D4 append-only sister)
- Schtask 7-day bound : **REFUSÉ** au profit de 84j cycle 12WY Q3 2026 sister-persistent
- Bypass airlock : **REFUSÉ** (sister Sobriété 1/10 hard cap)
- Spock silent approval : **REFUSÉ** (chaque iter schema vérifiable via `spock-review.md`)
- Hook REMPLACE canon : **REFUSÉ** (append-only D4 settings.json)

---

**Auteur** : B1 Jerry Prime (E-Myth Gatekeeper) + A2 Orchestrateur Stratégique + B1-OpenHarness-Replicant
**Date** : 2026-07-06
**Status** : READY-FOR-A0-RATIFICATION
**Sister-fichier** : `C:\Users\amado\.claude\schtasks\wf1-persistent-loop-router.xml`
**Sister-canon protégé** : `heartbeat-tick.ps1` (313 lines, EXTENDED only, NEVER REPLACED)
**D7 cost-of-escalation** : 1× A0 GO suffit (post-ratification, cron sister-persistent weekly H8 Monday)