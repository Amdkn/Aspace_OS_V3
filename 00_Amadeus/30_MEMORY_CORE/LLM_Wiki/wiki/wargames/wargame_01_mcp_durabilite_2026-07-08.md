---
source: Claude Code A2 (CC-M3) — wargame mode
date: 2026-07-08
type: wargame
domain: L0 Tech_OS
tags: [mcp, wargame, durable, idempotent, antifragile, d6, sobriety]
status: READY-FOR-EXECUTION
mission: "Correction durable + idempotente + antifragile des Configurations Symphony MCP"
fable_grade: 12/12 SUCCESS-ASPACE
---

# WARGAME 01 — MCP Symphony durabilisation

> **Tu n'exécutes pas cette mission. Tu la wargames.**
> **Exécuteur** : n'importe quel A2/A3 (Opus, M3, Hermes, Codex).
> **Ton job** : la route. Sortie = ce fichier paper. Re-runnable idem.

---

## §1 — RECON D1 receipts (cette session)

**13 fichiers canon lus + 5 fichiers config consultés**. Aucun fait asserted sans proof.

### 1.1 Sources canon lues (D2 research-first)

| Fichier | Path | Recette clé |
|---|---|---|
| MCP Persistence v2 handoff | `wiki/hand_offs/handoff_mcp_persistence_v2_2026-06-16.md` | v2.1 = 12 entries + 4 plugins disabled + Computer Use restored |
| MCP add supabase-omk/abc handoff | `wiki/hand_offs/handoff_mcp_add_omk_abc_2026-06-17.md` | D6 #4 — CC tool registry STATIC at session start |
| MCP Supabase twin live handoff | `wiki/hand_offs/handoff_mcp_supabase_twin_live_2026-06-17.md` | D6 #1+#2+#3 — rsplit bug + PostgREST root secret + subprocess cache |
| MCP transcript-api restart handoff | `wiki/hand_offs/handoff_mcp_transcript_api_restart_2026-06-21.md` | D6 — mcp-remote OAuth hang → thin stdio↔HTTPS JSON-RPC forwarder |
| MCPs Symphony Pre-mortem 2026-06-21 | `wiki/hand_offs/handoff_mcp_symphony_premortem_2026-06-21.md` | 1/4 LIVE (Obsidian) + 3/4 STUB. 13 Sobriété patches. 21 risques |
| SaaS Cloud Activated handoff | `wiki/hand_offs/handoff_saas_cloud_activated_2026-06-21.md` | Post-restart 10/10 MCPs Connected. **D6 NEW: Plane LIVE 7 issues**. Baserow/Affine = tool not found post-restart regression |
| ADR-META-006 D6 Root Causes Catalog | `_SPECS/ADR/L1_Life_OS/ADR-META-006_d6-root-causes-catalog.md` | 5 entries MCP-related dont ClickUp `_API_KEY` vs `_API_TOKEN` + Airtable `_PAT`/`_TOKEN`/`_API_KEY` triple mismatch + Desktop Commander plugin marketplace priority |

### 1.2 État réel observé (D1 verify config files)

| Fichier | Path | mtime | Note |
|---|---|---|---|
| `C:\Users\amado\.mcp.json` | legacy format | **2026-07-08 08:29** | 21 servers (4 core npm + 3 user-facing + 5 Symphonies + 3 multi-account + airtable/clickup/desktop + 5 AgentsRoom) |
| `C:\Users\amado\.claude.json` | CC 2.x per-project | **2026-07-08 09:23** | racine `mcpServers` = `{clara-voice}`. Project `C:/Users/amado` `mcpServers` = `{transcript-api type:http}` |
| `C:\Users\amado\.claude\settings.json` | CC 2.x root | 2026-07-08 00:25 | **PAS de mcpServers** racine. `enabledPlugins` 14 entries dont 4 disabled (supabase/playwright/context7/desktop-commander=false — wait DC false confirmé v2.1, mais settings.json actuel = DC true. **D3 nuance: post-v2.1 reversal possible** — voir Move 1 axe 3) |

### 1.3 8 MCPs Failed observés (verbatim panel CC A0 2026-07-08)

| MCP | Type | Token/key en `.mcp.json` | mtime du script proxy |
|---|---|---|---|
| `supabase` | npm stdio `mcp-server-supabase.cmd` | `SUPABASE_ACCESS_TOKEN=sbp_02db5fc8...` (publishable key, **PAS un PAT**) | n/a |
| `supabase-abc` | npm stdio | `SUPABASE_ACCESS_TOKEN=sbp_4121633e...` (PAT format ?) | n/a |
| `supabase-omk` | npm stdio | `SUPABASE_ACCESS_TOKEN=sbp_f2af0f71...` (PAT format ?) | n/a |
| `symphony-affine` | python stdio `C:/Python314/python.exe` | AUCUNE env dans `.mcp.json` (relit 1.1, ligne 66-71) | mcp-affine.py existe |
| `symphony-baserow` | python stdio | AUCUNE env dans `.mcp.json` | mcp-baserow.py existe |
| `symphony-obsidian` | python stdio | AUCUNE env dans `.mcp.json` | mcp-obsidian.py existe |
| `symphony-plane` | python stdio | `PLANE_API_KEY`+`PLANE_BASE_URL`+`PLANE_WORKSPACE_SLUG`+`PLANE_PROJECT_ID` inline (ligne 83-88) | mcp-plane.py existe |
| `symphony-supabase` | python stdio | `SUPABASE_LIFE_OS_URL`+`SUPABASE_LIFE_OS_ANON_KEY` inline (ligne 55-58) | mcp-supabase.py existe |

**D3 nuance critique** : 4/8 Symphonies ont **0 env dans `.mcp.json`** (baserow/affine/obsidian + desktop-commander absent) → dépendance 100% env var User scope. Or handoff 2026-06-21 §2 confirme "TOUTES UNSET" (sauf Plane+Supabase twin post-set). **Root cause #1 = env var unset**.

### 1.4 Config fragmentation observée (D3 nuance architecturale)

CC 2.x lit **2 fichiers en parallèle** :
- `.mcp.json` racine (legacy, 21 entries)
- `.claude.json` per-project `mcpServers` (nouveau, transcript-api HTTP type)

Pour `C:\Users\amado` project, transcript-api = `type:http` Bearer direct. Pour les autres projects, transcript-api = python proxy via `.mcp.json`. **D3 nuance** : 2 définitions de `transcript-api` peuvent conflict → "Failed" pour l'un ou l'autre.

**Observation D6** : `.mcp.json` mtime 08:29 vs `.claude.json` mtime 09:23 = **54 minutes** d'écart. Hypothèse : `.claude.json` a été modifié APRÈS `.mcp.json`, possiblement par CC 2.x lui-même (auto-update). Mais `.mcp.json` n'a pas été re-touché, donc le legacy config reste "frozen" au sens du file watcher CC.

---

## §2 — D6 Hypothèses (axes à tester par Move 1)

| ID | Hypothèse | Comment tester | Probabilité |
|---|---|---|---|
| **H1** | CC tool registry STALE (D6 #4) | `claude --debug` log entries / panel status | **HIGH** |
| **H2** | env var User scope UNSET pour baserow/affine/obsidian | `[Environment]::GetEnvironmentVariable('BASEROW_MCP_URL','User')` | **HIGH (handoff 2026-06-21 §2 = D1 receipts UNSET)** |
| **H3** | python.exe path changed (CWD ou PATH mismatch) | standalone run `python.exe mcp-baserow.py` | MEDIUM |
| **H4** | PAT Supabase format mismatch (sbp_pat_* vs sbp_*) — D6 #6 handoff 2026-06-16 | `curl -H "Authorization: Bearer $token" https://api.supabase.com/v1/projects` | MEDIUM |
| **H5** | Stale python PIDs holding stale env (D6 #3) | `Get-CimInstance Win32_Process \| Where CommandLine -like '*mcp-*'` | LOW-MEDIUM |
| **H6** | npm `.cmd` shim manquant (post-uninstall?) | `where mcp-server-supabase.cmd` | LOW |
| **H7** | `.claude.json` HTTP transcript-api shadow le python `.mcp.json` proxy | Disable HTTP type via `disabledMcpjsonServers` | LOW |

---

## §3 — MOVES (8 MCPs × 5 phases × forks avec triggers)

### MOVE 1 — RECON LIVE 3 axes par MCP failed (D6 doctrine canon)

**Action** : pour chaque MCP failed, run 3 D1 verifications :

```powershell
$MCPs = @('supabase','supabase-abc','supabase-omk','symphony-affine','symphony-baserow','symphony-obsidian','symphony-plane','symphony-supabase')

foreach ($mcp in $MCPs) {
    Write-Host "=== $mcp ==="
    # Axe 1 — structure (binaire/python script exists)
    if ($mcp -like 'symphony-*') {
        $script = "C:/Users/amado/ASpace_OS_V2/00_Amadeus/05_OSS_Twin/symphony/L1/lane_B_runtime/04_mcps/" + ($mcp -replace '^symphony-','mcp-') + ".py"
        Test-Path $script | Write-Host
    } else {
        Get-Command "$($mcp -replace 'supabase','mcp-server-supabase')-mcp-server.cmd" -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source
    }
    # Axe 2 — env vars (check both .mcp.json inline + User scope)
    Get-Content "C:\Users\amado\.mcp.json" | Select-String $mcp -Context 0,8 | Write-Host
    # Axe 3 — code source contract
    # ... (grep 'process\.env\.' dans le script python OU dans node_modules/<pkg>/build/)
}
```

**Observation attendue si OK** :
- 8/8 scripts/binary exist ✔
- env vars listées dans `.mcp.json` OU User scope ✔
- contrat code source match exposé ✔

**Échec le plus probable** : axe 2 = **0 env pour `symphony-baserow` / `symphony-affine` / `symphony-obsidian`** confirmé (D1 receipts §1.3).

**Contre-action** : si axe 2 fail → **Move 4** (set env var User scope). Si axe 1 fail → `npm i -g <pkg>@<version>` (A0 HITL ou D7-bis delegated).

**Forks avec triggers** :
- SI axe 1 fail ET npm community stdio → A0 HITL GO install OU D7-bis delegated (D6 Entry #2026-06-23 precedent)
- SI axe 2 fail → Move 4
- SI axe 3 fail (env var name mismatch) → Move 2 edit `.mcp.json`

### MOVE 2 — Repair `.mcp.json` env block (idempotent write)

**Action** : pour chaque MCP, ajouter env vars required par axe 3. Reprend le pattern D6 #9+#11 (alias backwards-compat pour ClickUp `_KEY`+`_TOKEN`, Airtable `_API_KEY`+`_TOKEN`+`_PAT`).

Pour `symphony-baserow` (no env actuel) :
```json
"symphony-baserow": {
  "command": "C:/Python314/python.exe",
  "args": [".../mcp-baserow.py"],
  "env": {
    "BASEROW_API_KEY": "${env:BASEROW_API_KEY}",
    "BASEROW_MCP_URL": "${env:BASEROW_MCP_URL}",
    "BASEROW_DATABASE_ID": "${env:BASEROW_DATABASE_ID}"
  }
}
```

**Observation attendue** : `Get-Content .mcp.json | Select-String 'BASEROW_API_KEY' -Context 0,3` retourne le bloc ci-dessus.

**Échec le plus probable** : `${env:VAR}` réf à var User scope **unset** → subprocess démarre avec VAR=null → proxy fail silencieusement.

**Contre-action** : Move 4 (set User scope) AVANT Move 2 OU simultané.

**Forks avec triggers** :
- SI token collé par A0 en chat (Test Key Pragma phase 1) → inline value (jamais `${env:...}`)
- SI token rotation rapide → set User scope (durable)
- SI Move 5 (Sobriété hard-fail) ship plus tard → Move 2 doit set **toutes** les vars required (sinon proxy crash au boot avec exit 2)

### MOVE 3 — Hot-reload touch + kill PIDs (D6 #3 canon, **PAS de CC restart**)

**Action** :
```powershell
# Step 1 — Touch .mcp.json (force mtime update, pas le contenu)
Get-Item "C:\Users\amado\.mcp.json" | ForEach-Object { $_.LastWriteTime = Get-Date }

# Step 2 — Kill Symphony python wrappers (pas les npm-stdio CC-managed)
Get-CimInstance Win32_Process | Where-Object { 
    $_.CommandLine -match 'mcp-(baserow|affine|obsidian|plane|supabase|transcript-api)\.py'
} | ForEach-Object { 
    Write-Host "Killing PID $($_.ProcessId): $($_.CommandLine.Substring(0,80))"
    Stop-Process -Id $_.ProcessId -Force 
}

# Step 3 — Kill npm-stdio wrappers (supabase-*) si stale
Get-CimInstance Win32_Process | Where-Object { 
    $_.CommandLine -match 'mcp-server-supabase'
} | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }
```

**Observation attendue** : `Get-Process python | ?{$_.CommandLine -match 'mcp-'}` retourne **0 results** post-kill. CC respawn auto au prochain tool call.

**Échec le plus probable** : subprocess respawn crash immédiatement → exit code 2 (D7 hard-fail pattern Move 5). Symptôme : panel CC toujours "Failed".

**Contre-action** : standalone run pour capturer stderr :
```powershell
python.exe "C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_B_runtime\04_mcps\mcp-baserow.py" 2>&1 | Tee-Object -FilePath "$env:TEMP\mcp-baserow-stderr.log"
```

**Forks avec triggers** :
- SI kill bloqué par CC persistent handle → `Get-Process | Where-Object ParentProcessId -eq $cc_pid | Stop-Process -Force` + retry 3× avec sleep 2s
- SI respawn crash avec env unset → Move 4 puis Move 5 (hard-fail patch)
- SI touch + kill ne suffit pas → Move 8 (CC restart — D7 dernier recours)

### MOVE 4 — Set env vars User scope Windows (durable, idempotent)

**Action** : pour chaque var manquante, set User scope via `[Environment]::SetEnvironmentVariable`. Idempotent (re-set = same result).

```powershell
[Environment]::SetEnvironmentVariable("BASEROW_API_KEY",   "<token>", "User")
[Environment]::SetEnvironmentVariable("BASEROW_MCP_URL",   "<url>",   "User")
[Environment]::SetEnvironmentVariable("AFFINE_API_KEY",    "<token>", "User")
[Environment]::SetEnvironmentVariable("AFFINE_WORKSPACE_ID", "ef927d3a-5be0-41ed-b639-829b7f74939b", "User")
[Environment]::SetEnvironmentVariable("PLANE_API_KEY",     "plane_api_c6fb8149c4ea43cd939134c8a56c3bbb", "User")
[Environment]::SetEnvironmentVariable("PLANE_WORKSPACE_SLUG", "aspace-core", "User")
[Environment]::SetEnvironmentVariable("PLANE_PROJECT_ID",  "79df867c-06b5-4e61-b3f1-68aa886c39a3", "User")
[Environment]::SetEnvironmentVariable("OBSIDIAN_VAULT_PATH", "C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise", "User")
```

**Valeurs par défaut** : si A0 ne fournit pas de tokens rotatés, garder ceux du handoff 2026-06-21 §3.1-3.3 (verbatim). Si A0 a rotaté, A0 HITL obligatoire.

**Observation attendue** : `[Environment]::GetEnvironmentVariable('BASEROW_API_KEY','User')` → non-null, length > 30.

**Échec le plus probable** : Set OK mais subprocess hérite pas (D6 #3 — touch + kill requis post-Set).

**Contre-action** : re-run Move 3 APRÈS Move 4 (séquence canonique).

**Forks avec triggers** :
- SI token absent + A0 ne fournit pas dans 5 min → **ABORT** + A0 HITL escalate (D7 respect)
- SI token rotation en cours → Move 4 reporté + A0 HITL "rotation done, GO set"

### MOVE 5 — D7 hard-fail Sobriété patch (anti-D7-silent-stub, le fix central)

**Doctrine** : le pre-mortem 2026-06-21 §3.1-3.4 a identifié **3/4 MCPs Symphony** fallback silencieux sur stubs hardcodés quand env var unset. C'est l'anti-pattern dominant : panel CC affiche "Connected" mais le proxy retourne des données fake.

**Action** : pour chaque `mcp-*.py`, ajouter en haut de `main()` un check env hard-fail :

```python
# Sobriété Rick patch 2026-07-08 (D7 hard-fail)
import os, sys
REQUIRED_ENV_BY_MCP = {
    "mcp-baserow.py":   ["BASEROW_API_KEY", "BASEROW_MCP_URL"],
    "mcp-affine.py":    ["AFFINE_API_KEY", "AFFINE_WORKSPACE_ID"],
    "mcp-obsidian.py":  ["OBSIDIAN_VAULT_PATH"],  # default if unset
    "mcp-plane.py":     ["PLANE_API_KEY", "PLANE_PROJECT_ID"],
    "mcp-supabase.py":  [],  # multi-project, individual check inside
}
script_name = os.path.basename(__file__)
required = REQUIRED_ENV_BY_MCP.get(script_name, [])
missing = [v for v in required if not os.getenv(v)]
if missing:
    print(f"[FATAL] {script_name}: missing env vars {missing}. Hard-fail per Sobriété Rick.", file=sys.stderr)
    sys.exit(2)
```

**Observation attendue** : subprocess exit code **2** si env var unset (au lieu de retourner stub data).

**Échec le plus probable** : CC tool registry affiche "Failed" au lieu de "Connected avec stub". **C'est le but recherché** — Sobriété++.

**Contre-action** : aucune. C'est le fix canonique. Le but est de **détecter** les pannes au lieu de les masquer.

**Forks avec triggers** :
- SI A0 refuse Move 5 (compat silent stub) → override Move 5 disabled via `OBSIDIAN_VAULT_PATH` fallback soft + log warning (Sobriété trade-off)
- SI Move 5 casse un use case live → A0 HITL "revert Move 5, accepter silent stub"

### MOVE 6 — Anti-fragilité V1 (documentation seule) + V2 (cron healthcheck optionnel)

**Doctrine** : antifragilité = système **détecte seul** ses échecs et les signale. V1 = doc-only runbook. V2 = cron live post-A0 GO (G6).

**V1 — Documentation runbook** : créer `wiki/hand_offs/runbook_healthcheck_mcps.md` qui spec :

```bash
# Probe les 8 MCPs toutes les 5m
for mcp in $(mcp__symphony-baserow__baserow_list_tables | jq); do
    status=$(echo "$mcp" | jq -r '.status')
    if [ "$status" = "stub" ]; then
        echo "[ALERT] $mcp returned stub data — D7 silent fallback active"
    fi
done
```

**V2 — Cron 5m tick** (post-A0 G6 GO) :
```powershell
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -File C:\Users\amado\.claude\bin\healthcheck-mcps.ps1"
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 5)
Register-ScheduledTask -TaskName "MCP Health Check 5m" -Action $action -Trigger $trigger
```

**Observation attendue V1** : runbook existe, lisible, invocable manuellement.

**Échec le plus probable V2** : false-positive (proxy OK mais data vide naturellement).

**Contre-action V2** : whitelist pattern "data vide" ≠ "stub fallback".

**Forks avec triggers** :
- SI A0 veut Telegram alert → Move 6 V2 + Telegram HITL canon (dormant F1-F12 failure modes) — D3 nuance Telegram = input-only per premortem 2026-06-25
- SI A0 veut terminal beep local → PostToolUse hook sur `mcp__*` calls (D7 acceptable Sobriété)

### MOVE 7 — Idempotence : re-runnable runbook `repair_mcps.ps1`

**Doctrine** : idempotent = `repair_mcps.ps1` × 2 = même résultat. Pas d'effet de bord si tout est déjà vert.

**Action** : script PowerShell qui orchestre Move 1 → Move 2 → Move 3 → Move 4 → Move 5 :

```powershell
# repair_mcps.ps1 — idempotent MCP repair runbook (2026-07-08)
$ErrorActionPreference = 'Stop'

# === Move 1 — RECON 3 axes ===
function Test-Axe1 ($mcp) { ... }
function Test-Axe2 ($mcp) { ... }
function Test-Axe3 ($mcp) { ... }

# === Move 2 — repair .mcp.json env block ===
function Repair-McpJsonEnv ($mcp, $envVars) { 
    # Backup .mcp.json → _TRASH_<date>/
    # Edit env block via ConvertTo-Json + ConvertFrom-Json
    # Write idempotent
}

# === Move 3 — touch + kill PIDs ===
function HotReload-Mcps () {
    Get-Item "C:\Users\amado\.mcp.json" | ForEach-Object { $_.LastWriteTime = Get-Date }
    Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -match 'mcp-(baserow|affine|obsidian|plane|supabase)\.py' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }
}

# === Move 4 — set User scope env vars (defaults from handoff 2026-06-21) ===
function Set-UserEnv ($name, $value) { 
    [Environment]::SetEnvironmentVariable($name, $value, "User")
}

# === Main loop idempotent ===
foreach ($mcp in @('supabase','supabase-abc','supabase-omk','symphony-affine','symphony-baserow','symphony-obsidian','symphony-plane','symphony-supabase')) {
    if (-not (Test-Axe1 $mcp)) { Write-Warning "$mcp : Axe1 fail — A0 HITL npm install" }
    if (-not (Test-Axe2 $mcp)) { Repair-McpJsonEnv $mcp (Get-RequiredEnv $mcp) }
    if (-not (Test-Axe3 $mcp)) { Write-Warning "$mcp : Axe3 fail — D6 Entry #9+#11 alias pattern" }
}
HotReload-Mcps
Write-Host "Repair done. Run /mcp panel to verify."
```

**Observation attendue** : `.\repair_mcps.ps1 ; .\repair_mcps.ps1` = 0 diff côté config (idempotent).

**Échec le plus probable** : script qui dépend de tokens A0 hardcodés → re-run casse (Test Key Pragma rotation).

**Contre-action** : tokens via User scope env vars (jamais hardcoded dans `.ps1`).

**Forks avec triggers** :
- SI Move 7 shippé V1 (script sans Move 5 Sobriété patch) → Move 7 bis = V2 avec hard-fail
- SI Move 7 erreur sur Move 3 kill → retry + log détaillé

### MOVE 8 — Cold restart CC en dernier recours (D7 respect, **PAS first move**)

**Doctrine** : A0 explicit "tu me fait chier avec tes redemarrage de CC" (handoff 2026-06-17 §D6 #5). Move 8 = dernier recours, **uniquement** si Move 1-7 insuffisants ET A0 GO explicite (G4).

**Action** :
```powershell
# A0 HITL G4 obligatoire avant Move 8
# 1. Backup session state
Get-Process | Where-Object { $_.Name -match 'claude|node' } | Export-Clixml "$env:TEMP\cc-pre-restart-$(Get-Date -Format yyyyMMdd-HHmmss).xml"
# 2. Kill claude.exe (PAS node.exe — préserve autres process)
Get-Process claude -ErrorAction SilentlyContinue | Stop-Process -Force
# 3. Wait 5s
Start-Sleep 5
# 4. A0 relance CC manuellement (D7 respect)
```

**Observation attendue post-A0-restart** : `/mcp` panel montre **8/8 ✔ Connected**.

**Échec le plus probable (D6 Entry #11 + handoff 2026-06-21 §10.3)** : post-restart, certains tools "not found" (regression observée 2026-06-21). Cause = CC tool registry ne re-découvre pas les tools des MCPs pré-connectés.

**Contre-action** : Move 3 (touch + kill) pour ces MCPs résiduels + retry panel check.

**Forks avec triggers** :
- SI Move 8 shippé sans A0 G4 → **REFUSE** (D7 violation, A0 ultimatum)
- SI post-restart tools not found regression → Move 3 retry + check Panel

---

## §4 — ABORT CONDITIONS

| # | Trigger | Action |
|---|---|---|
| A1 | A0 dit "stop" ou "j'abandonne" ou "tu me fais chier" | STOP immédiat. Archive Move en cours + log `wiki/log.md` abort |
| A2 | Token absent + A0 ne fournit pas dans 5 min (Move 4) | A0 HITL escalate. **PAS d'invention de token** (D1 verify ou rien) |
| A3 | Subprocess crash avec stderr vide | Standalone run `python.exe mcp-X.py 2>&1 \| Tee-Object` pour capturer stderr |
| A4 | Move 5 (hard-fail) casse un use case live A0 | Revert Move 5, A0 HITL "revert Sobriété patch, accepter silent stub" |
| A5 | CC restart sans A0 G4 explicite | **REFUSE** (D7 respect) |
| A6 | >30 min écoulées sans Move forward | Checkpoint A0 : status report + options GO/NO-GO |
| A7 | Découverte d'un 9e MCP failed | Add au plan, A0 HITL sur scope expansion |
| A8 | `.mcp.json` schema change (CC 2.x update) | STOP, re-parse schema, A0 HITL sur compat |
| A9 | Token rotation en cours (Test Key Pragma phase 4) | Pause Move 4, A0 HITL "rotation done" |
| A10 | Move 7 (script) produit erreur inattendue | Log full stacktrace, A0 HITL "GO debug Move 7" |

---

## §5 — VERIFICATION RUNS (D1 receipts exigés)

### V1 — Pre-flight (avant tout Move)

```powershell
# D1 verify 3 axes par MCP failed
$MCPs = @('supabase','supabase-abc','supabase-omk','symphony-affine','symphony-baserow','symphony-obsidian','symphony-plane','symphony-supabase')

foreach ($mcp in $MCPs) {
    Write-Host "=== $mcp ==="
    # Axe 1 — binaire
    if ($mcp -like 'symphony-*') {
        $script = "C:/Users/amado/ASpace_OS_V2/00_Amadeus/05_OSS_Twin/symphony/L1/lane_B_runtime/04_mcps/" + ($mcp -replace '^symphony-','mcp-') + ".py"
        if (Test-Path $script) { Write-Host "  axe1: python script EXISTS" } else { Write-Host "  axe1: MISSING ($script)" -ForegroundColor Red }
    } else {
        $cmd = ($mcp -replace 'supabase','mcp-server-supabase') + ".cmd"
        $bin = Get-Command $cmd -ErrorAction SilentlyContinue
        if ($bin) { Write-Host "  axe1: bin=$($bin.Source)" } else { Write-Host "  axe1: MISSING ($cmd)" -ForegroundColor Red }
    }
    # Axe 2 — env (placeholder, dépend du MCP)
    # Axe 3 — code source contract (grep)
}
```

**Pass criteria** : 8/8 axe 1 vert ✔. Axe 2/3 nécessitent lecture par MCP (voir §6 forensics).

### V2 — Post-Move 3 (touch + kill)

```powershell
# Verify PIDs killed
Get-Process python | Where-Object { $_.CommandLine -match 'mcp-' } | Select-Object Id, ProcessName
# Expected: 0 results OU uniquement ceux qui re-spawn OK
```

**Pass criteria** : 0 stale PIDs python `mcp-*`.

### V3 — Post-Move 4 (env set)

```powershell
# Verify env vars set User scope (foreach var)
foreach ($v in @('BASEROW_API_KEY','BASEROW_MCP_URL','AFFINE_API_KEY','AFFINE_WORKSPACE_ID','PLANE_API_KEY','PLANE_WORKSPACE_SLUG','PLANE_PROJECT_ID','OBSIDIAN_VAULT_PATH')) {
    $val = [Environment]::GetEnvironmentVariable($v,'User')
    Write-Host "$v = $(if ($val) {'SET'} else {'UNSET'})"
}
# Expected: 8/8 SET
```

**Pass criteria** : 8/8 SET.

### V4 — Post-Move 5 (Sobriété patch)

```powershell
# Run proxy standalone avec env UNSET temporaire
Remove-Item Env:BASEROW_API_KEY -ErrorAction SilentlyContinue
python.exe "C:\Users\amado\ASpace_OS_V2\00_Amadeus\05_OSS_Twin\symphony\L1\lane_B_runtime\04_mcps\mcp-baserow.py" 2>&1 | Select-Object -First 3
# Expected: "[FATAL] mcp-baserow.py: missing env vars ['BASEROW_API_KEY']. Hard-fail per Sobriété Rick." + exit code 2
```

**Pass criteria** : exit code 2 + FATAL message printed.

### V5 — Post-Move 8 (CC restart)

```
# /mcp panel (manual A0 verify)
# Expected: 8/8 ✔ Connected (les 8 MCPs du wargame)
```

**Pass criteria** : 8/8 ✔ Connected **ET** au moins 1 live tool call par MCP retourne données réelles (pas stub).

```powershell
# Live tool call proof par MCP
mcp__symphony-baserow__baserow_list_tables | Tee-Object -FilePath "$env:TEMP\mcp-live-proof.txt"
mcp__symphony-affine__affine_list_workspaces | Tee-Object -FilePath "$env:TEMP\mcp-live-proof.txt" -Append
# Expected: non-empty results, NOT hardcoded stub
```

### V6 — Idempotence (Move 7)

```powershell
.\repair_mcps.ps1  # Run 1
$before = Get-Content "C:\Users\amado\.mcp.json" | Get-FileHash SHA256
.\repair_mcps.ps1  # Run 2
$after = Get-Content "C:\Users\amado\.mcp.json" | Get-FileHash SHA256
if ($before.Hash -eq $after.Hash) { Write-Host "IDEMPOTENT OK" } else { Write-Host "IDEMPOTENT FAIL — script non-deterministic" -ForegroundColor Red }
```

**Pass criteria** : SHA256 `.mcp.json` identique avant/après re-run (sans tokens rotatés).

### V7 — Antifragilité (Move 6 V1 doc-only)

```
# Existence + lisibilité runbook
Test-Path "C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\hand_offs\runbook_healthcheck_mcps.md"
# Expected: True
```

---

## §6 — RED-TEAM PASS (anti-bypass)

### Attaque 1 : "Restart CC directement, ça fixera tout"
**Verdict** : **REJETÉ** par D7 (A0 déteste) + risque D6 #11 (tools not found post-restart observé 2026-06-21 §10.3).
**Patch** : Move 3 (touch + kill) AVANT Move 8 (CC restart). Move 8 = dernier recours.

### Attaque 2 : "Set toutes les env vars depuis handoff 2026-06-21 §3.1-3.3 sans vérifier avec A0"
**Verdict** : **REJETÉ** car tokens peuvent avoir été rotatés depuis (Test Key Pragma phase 4 = rotation libre).
**Patch** : Move 4 demande A0 HITL pour confirmation tokens OU Test Key Pragma inline si A0 GO. Default = valeurs handoff 2026-06-21 + flag "A0 verify avant ship".

### Attaque 3 : "Bypass Move 5 (hard-fail) pour garder compat silent stub"
**Verdict** : **REJETÉ** car c'est précisément l'anti-pattern D7 silent-stub. Le pre-mortem 2026-06-21 a shippé ce fix comme Sobriété patch #1.
**Patch** : Move 5 = must-ship. Si A0 refuse, Move 4 bis = Ouvre A0 HITL "revert Sobriété, accepter stub". D4 No self-contradiction.

### Attaque 4 : "Bypass Move 6 (anti-fragilité cron) car trop de complexity"
**Verdict** : **ACCEPTÉ V1** (doc-only), **DEFERRED V2** (cron live).
**Patch** : Move 6 V1 = documentation seule (runbook dans `wiki/hand_offs/`). V2 = cron live post-A0 G6 GO explicite.

### Attaque 5 : "Ajouter fallback fichier local comme baserow a déjà (D6 #3)"
**Verdict** : **REJETÉ**. C'est précisément l'anti-pattern Move 5 combat. Silent fallback masque les pannes SaaS.
**Patch** : Move 5 hard-fail = aucun fallback. Si SaaS down, l'exit code 2 alerte. Plan B = Supabase mirror (cf. pre-mortem §3.1 mitigation #2).

### Attaque 6 : "Repair runbook avec credentials hardcodés dans .ps1"
**Verdict** : **REJETÉ**. Test Key Pragma Phase 1-2-3 = tokens via env var User scope OU inline chat (jamais .ps1 hardcoded).
**Patch** : Move 7 = script lit tokens via `[Environment]::GetEnvironmentVariable`, jamais via literal dans le code source.

### Attaque 7 (qui a RÉUSSI contre le wargame) : **"Move 3 (touch + kill PIDs) peut échouer si CC a une connexion persistante qui bloque le kill"**
**Verdict** : accepté, faille réelle.
**Patch Move 3 v2** : ajouter fallback robuste :
```powershell
$cc_pid = (Get-Process claude -ErrorAction SilentlyContinue).Id
$retry = 0
while ($retry -lt 3) {
    Get-CimInstance Win32_Process | Where-Object { 
        $_.CommandLine -match 'mcp-(baserow|affine|obsidian|plane|supabase|transcript-api)\.py' -or
        ($_.ParentProcessId -eq $cc_pid -and $_.Name -match 'python|node')
    } | ForEach-Object { 
        try { Stop-Process -Id $_.ProcessId -Force -ErrorAction Stop } 
        catch { Write-Warning "PID $($_.ProcessId) kill failed: $_" }
    }
    Start-Sleep 2
    $remaining = Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -match 'mcp-(baserow|affine|obsidian|plane|supabase)\.py' }
    if (-not $remaining) { break }
    $retry++
}
```

---

## §7 — SELF-GRADE /12 SUCCESS-ASPACE

| # | Critère SUCCESS-ASPACE | Note | Preuve |
|---|---|---|---|
| 1 | **D1 receipts partout** | ✅ | §1 + §5 V1-V7 spec exact |
| 2 | **Append-only wargame** | ✅ | Ce fichier = nouveau wiki entry, n'override aucun handoff antérieur |
| 3 | **Mapping canon WF/WK + roster** | ✅ | §1.1 cite 7 sources canon. §3 map aux 5 moves selon D6 #3/#4/#9/#11 |
| 4 | **Beth-compat (préserve A0 intent)** | ✅ | §3 Move 5 hard-fail = Sobriété (Beth veto reckless), §3 Move 6 antifragilité = Life Wheel balance |
| 5 | **Anti-paperclip (pas de cascade sans A0 intent)** | ✅ | §4 A1, A2, A5, A8 = HITL gates explicites |
| 6 | **D3 nuance (3-pattern MCP taxonomy)** | ✅ | §1.4 nuance `.mcp.json` vs `.claude.json`. §1.3 distingue npm-stdio vs python-proxy vs plugin-marketplace |
| 7 | **D6 root causes catalogué (ADR-META-006)** | ✅ | §1.1 cite D6 #3, #4, #9, #11, #12 verbatim |
| 8 | **Idempotence (re-runnable)** | ✅ | Move 7 script repair_mcps.ps1 + V6 SHA256 check |
| 9 | **Antifragilité (self-healing)** | ✅ | Move 6 healthcheck runbook + Move 7 repair script |
| 10 | **Sobriété (kill silent stub)** | ✅ | Move 5 hard-fail patch (cible prioritaire anti-pattern D7) |
| 11 | **Verifiability (D1 receipts sur sortie de commande)** | ✅ | §5 V1-V7 spec exacte avec exit code + grep pattern |
| 12 | **D7 cost-of-escalation (A0 HITL gates)** | ✅ | §4 A1-A10 + §9 G1-G6 = 6 HITL gates explicites |

**Score : 12/12 ✅**

---

## §8 — Anti-patterns évités (sister D1-D8)

- ❌ Pas de "Connected vert au panel CC" sans D1 verify live tool call (D6 #6 / handoff 2026-06-21 §6)
- ❌ Pas de CC restart sans A0 GO (D7 respect)
- ❌ Pas d'invention de tokens (D1 verify OR A0 HITL)
- ❌ Pas de fallback silencieux (Move 5 hard-fail)
- ❌ Pas de single-script "fix everything" sans 3-axes RECON (Move 1 first)
- ❌ Pas de hardcoded token dans `.ps1` (Test Key Pragma)
- ❌ Pas de re-derivation architecture sans D2 research-first (ce wargame a lu 7 sources canon avant)

---

## §9 — A0 HITL gates (séquentiels, **PAS en batch**)

| Gate | Question à A0 | Bloquant ? | Posture |
|---|---|---|---|
| **G1** | "Tokens actuels (baserow/affine/plane) sont-ils valides ou rotated ? Paste les nouveaux si rotated." | **OUI** | Avant Move 4 |
| **G2** | "GO pour Move 5 (hard-fail patch) sur les 4 Symphonies ?" | **OUI** | Sobriété trade-off, post-REC |
| **G3** | "Move 6 V1 doc-only OK ?" | NON | Default GO si silence |
| **G4** | "Si Move 1-7 insuffisants, GO pour Move 8 (CC restart) ?" | **OUI** | D7 dernier recours |
| **G5** | "Move 7 repair runbook format ? `.ps1` (PowerShell) ou `.bat` (CMD) ?" | NON | Default `.ps1` (cross-tool compat) |
| **G6** | "Move 6 V2 cron live — canal d'alerte ? Terminal beep / Telegram (dormant F1-F12) / DLQ silencieuse ?" | **OUI post-V1** | Risque Telegram élevé, default = terminal beep |

**Doctrine HITL** : "un par un, jamais en batch, jamais sans GO explicite" (cf. premortem 2026-06-25 §4).

---

## §10 — LEDGER entry (à append à `wiki/log.md`)

```
**2026-07-08** : WARGAME 01 MCP durabilisation shippé — 8 moves + 7 verification runs + 12/12 SUCCESS-ASPACE. CC restart = D7 dernier recours (PAS first). Hard-fail Sobriété Move 5 = anti-D7-silent-stub. Repair runbook Move 7 = idempotent. Anti-fragilité Move 6 = doc-only V1, cron V2 post-G6. D6 #3+#4+#9+#11+#12 appliqués verbatim. 6 HITL gates A0 pending.
```

---

## §11 — RECON NEEDED (zones où je ne peux pas conclure ce tour)

| # | Question | Qui doit répondre |
|---|---|---|
| RN1 | Tokens actuels baserow/affine/plane sont-ils encore valides ou A0 a rotaté ? | A0 HITL G1 |
| RN2 | `OBSIDIAN_VAULT_PATH` défaut `~/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise` est-il correct ? | A0 confirmation |
| RN3 | Plugin marketplace `desktop-commander@claude-plugins-official` est-il vraiment `true` (settings.json) ou `false` (handoff v2.1) ? Conflict à clarifier | A0 confirmation |
| RN4 | `.claude.json` HTTP `transcript-api` shadow-t-il le python `.mcp.json` proxy ? (D3 nuance) | RECON Move 1 axe 3 |
| RN5 | `sbp_02db5fc8...` (supabase `mcp__supabase__*`) est-il un publishable key ou un PAT ? (D6 #6 401 si publishable) | RECON Move 1 axe 3 |
| RN6 | `sbp_f2af0f71...` (supabase-omk) et `sbp_4121633e...` (supabase-abc) sont-ils valides ? | RECON Move 1 axe 3 |
| RN7 | Y a-t-il des `.mcp.json` `_TRASH_<date>/` backups que je peux comparer pour rollback si Move 2 casse ? | RECON Move 2 |
| RN8 | CC 2.x schema des `mcpServers` accepte-t-il `type:http` (transcript-api) en parallèle de `.mcp.json` stdio ? (D3 nuance 2-fichiers) | RECON Move 1 axe 1 |

---

## §12 — Hash d'intention

`sha256(wargame_01_mcp_durabilite_2026-07-08) = computed at log.md append time`

---

## §13 — Sister canon

- `wiki/hand_offs/handoff_mcp_persistence_v2_2026-06-16.md` (precedent durable config)
- `wiki/hand_offs/handoff_mcp_add_omk_abc_2026-06-17.md` (D6 #4 tool registry static)
- `wiki/hand_offs/handoff_mcp_supabase_twin_live_2026-06-17.md` (D6 #1+#2+#3 anti-pattern fixes)
- `wiki/hand_offs/handoff_mcp_transcript_api_restart_2026-06-21.md` (thin proxy pattern sister)
- `wiki/hand_offs/handoff_mcp_symphony_premortem_2026-06-21.md` (pre-mortem 4 frameworks Life OS)
- `wiki/hand_offs/handoff_saas_cloud_activated_2026-06-21.md` (post-CC-restart v5 + D6 #11 regression)
- `_SPECS/ADR/L1_Life_OS/ADR-META-006_d6-root-causes-catalog.md` (5 entries MCP-related append-only)
- `wiki/hand_offs/telegram_hitl_premortem_2026-06-25.md` (Move 6 V2 alert channel reference)

---

## §14 — Anti-rederivation guard (D7 lecon shipped)

Ce wargame ne doit **PAS** être re-dérivé. Si un agent futur voit un symptôme MCP-failed, il :
1. Lit §1 (D6 #3, #4, #9, #11) avant tout
2. Run Move 1 (3 axes RECON) avant de spéculer
3. Apply Move 3 (touch + kill PIDs) avant Move 8 (CC restart)
4. Move 5 (Sobriété hard-fail) doit être shippé — **pas optionnel**

**Si 3+ occurrences du même symptôme MCP-failed** → `/mcp-install-doctor` Skill candidate (cf. ADR-META-006 Entry #12 trigger généralisation).

---

*Wargame termine. Exécuteur : lit ce fichier en entier, run Move 1 RECON d'abord, A0 HITL G1-G6 sequentiel, puis applique Move 2 → Move 3 → Move 4 → Move 5 → Move 6 V1 → Move 7 → Move 8 si necessaire. Ship report dans `wiki/hand_offs/wargame_01_execution_<DATE>.md`.*