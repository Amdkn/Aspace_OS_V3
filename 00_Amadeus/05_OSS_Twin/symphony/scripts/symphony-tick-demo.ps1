# =============================================================================
# Symphony Tick Demo — PowerShell (one-tick simulation, mock Airtable record)
# =============================================================================
# Walks the 8 phases (WAKE→SLEEP) for WORKFLOW.solaris-airtable-clients.
# Injects standards from agent-os/standards/index.yml.
# Writes 8 JSONL lines to agent-os/pulse.log.
#
# Usage:  powershell -ExecutionPolicy Bypass -File symphony/scripts/symphony-tick-demo.ps1
# Env:    SYMPHONY_ROOT (defaults to parent of this script)
# =============================================================================

[CmdletBinding()]
param(
    [string]$SymphonyRoot = $env:SYMPHONY_ROOT
)

$ErrorActionPreference = 'Stop'

# --- Resolve paths -----------------------------------------------------------
if (-not $SymphonyRoot) {
    $SymphonyRoot = Split-Path -Parent $PSScriptRoot
}
$IndexFile = Join-Path $SymphonyRoot 'agent-os/standards/index.yml'
$PulseLog  = Join-Path $SymphonyRoot 'agent-os/pulse.log'
$Python    = if ($env:PYTHON) { $env:PYTHON } else { 'C:\Python314\python.exe' }

# --- Helpers -----------------------------------------------------------------
function IsoUtc {
    return (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ss.fffZ')
}

function MsSince([string]$a, [string]$b) {
    $da = [datetime]::ParseExact($a, 'yyyy-MM-ddTHH:mm:ss.fffZ', $null)
    $db = [datetime]::ParseExact($b, 'yyyy-MM-ddTHH:mm:ss.fffZ', $null)
    return [int]([decimal]($db - $da).TotalMilliseconds)
}

# pulse: append a JSONL line to pulse.log
# Args: phase, decision, [hasIssue], [extras hashtable]
function Pulse {
    param(
        [string]$Phase,
        [string]$Decision,
        [bool]$HasIssue = $true,
        [hashtable]$Extras = @{}
    )
    $ts = IsoUtc

    # Build base object
    $base = [ordered]@{
        ts                  = $ts
        tick_id             = $script:TickId
        workflow_id         = $script:WorkflowId
        phase               = $Phase
        aspace_layer        = 'L2'
        decision            = $Decision
    }
    if ($HasIssue) {
        $base['issue_id'] = $script:IssueId
    }
    if ($Phase -in @('DECIDE','EXECUTE','OBSERVE','LEARN','SIGNAL')) {
        $base['soc_target_domain'] = $script:SocDomain
    }
    if ($Phase -in @('EXECUTE','OBSERVE','LEARN','SIGNAL','SLEEP')) {
        $base['cumulative_cost_usd'] = $script:CumCost
    }
    if ($Phase -in @('EXECUTE','OBSERVE')) {
        $base['cost_delta_usd'] = $script:DeltaCost
    }
    if ($Phase -in @('DECIDE','EXECUTE','OBSERVE')) {
        $base['standards_injected'] = $script:StandardsJson
    }
    if ($Phase -in @('EXECUTE','OBSERVE','SIGNAL') -and $script:EvidenceUrl) {
        $base['evidence_url'] = $script:EvidenceUrl
    }
    $base['error'] = $null

    # Merge extras
    foreach ($k in $Extras.Keys) { $base[$k] = $Extras[$k] }

    # Drop $null values for cleaner JSONL
    $clean = [ordered]@{}
    foreach ($k in $base.Keys) {
        if ($null -ne $base[$k]) { $clean[$k] = $base[$k] }
    }

    $line = $clean | ConvertTo-Json -Compress -Depth 5
    Add-Content -Path $PulseLog -Value $line -Encoding UTF8
}

# --- Init ---------------------------------------------------------------------
$WorkflowId = 'solaris-airtable-clients'
$TickId     = "$WorkflowId-$((Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH-mm-ss'))"
$IssueId    = 'recDEMO001'
$SocDomain  = 'Growth'
$CumCost    = 0.0
$DeltaCost  = 0.0
$EvidenceUrl = ''
$StandardsJson = @('mission-contract.md','soa-routing.md','gate-decisions.md','forbidden-words.md','sla-triple.md','expected-proof.md','writeback-policy.md')

# Count standards from index.yml via Python
$env:PYTHONIOENCODING = 'utf-8'
$StdCount = & $Python -c "
import yaml
data = yaml.safe_load(open(r'$IndexFile', encoding='utf-8'))
total = sum(len(v) for v in data.values())
print(total)
"

Write-Host "=== Symphony Tick Demo (PowerShell) ==="
Write-Host "Tick ID:     $TickId"
Write-Host "Workflow:    $WorkflowId"
Write-Host "Issue:       $IssueId ($SocDomain)"
Write-Host "Standards:   $StdCount available in index.yml"
Write-Host "Pulse log:   $PulseLog"
Write-Host ""

# Truncate pulse.log for the demo (Clear-Content is cleaner than Set-Content '' which leaves a blank line)
Clear-Content -Path $PulseLog -ErrorAction SilentlyContinue

# --- Phase 1: WAKE -----------------------------------------------------------
$T0 = IsoUtc
Pulse -Phase 'WAKE' -Decision "tick start, index loaded, $StdCount standards available" -HasIssue $false -Extras @{duration_ms = 12}
Start-Sleep -Milliseconds 50
$T1 = IsoUtc

# --- Phase 2: PROBE ----------------------------------------------------------
Pulse -Phase 'PROBE' -Decision "polled 42 records, 3 eligible (incl. $IssueId), 39 not_eligible" -HasIssue $false -Extras @{duration_ms = 1234}
Start-Sleep -Milliseconds 50
$T2 = IsoUtc

# --- Phase 3: DECIDE ---------------------------------------------------------
Pulse -Phase 'DECIDE' -Decision 'build mission_contract v1.0, inject 7 standards, route to orchestrator+researcher+strategist' -Extras @{duration_ms = 87}
Start-Sleep -Milliseconds 50
$T3 = IsoUtc

# --- Phase 4: EXECUTE --------------------------------------------------------
$EvidenceUrl = "https://airtable.com/$($IssueId.ToLower())"
$DeltaCost = 0.012
$CumCost   = 0.012
Pulse -Phase 'EXECUTE' -Decision 'proof built (4/4 types: summary + recommendation + risks+blockers + gate=PASS)' -Extras @{duration_ms = 4521}
Start-Sleep -Milliseconds 50
$T4 = IsoUtc

# --- Phase 5: OBSERVE --------------------------------------------------------
$DeltaCost = 0.003
$CumCost   = 0.015
Pulse -Phase 'OBSERVE' -Decision 'lexique clean (no forbidden match), gate=PASS, cumulative=0.015 USD' -Extras @{duration_ms = 203}
Start-Sleep -Milliseconds 50
$T5 = IsoUtc

# --- Phase 6: LEARN ----------------------------------------------------------
Pulse -Phase 'LEARN' -Decision 'metrics updated, retries=1/3, no Donna escalation' -Extras @{duration_ms = 15}
Start-Sleep -Milliseconds 50
$T6 = IsoUtc

# --- Phase 7: SIGNAL ---------------------------------------------------------
Pulse -Phase 'SIGNAL' -Decision 'drafts written: 1x airtable_update_draft (Gate Status=PASS), 1x proof_summary' -Extras @{duration_ms = 78}
Start-Sleep -Milliseconds 50
$T7 = IsoUtc

# --- Phase 8: SLEEP ----------------------------------------------------------
$TotalMs = MsSince $T0 $T7
Pulse -Phase 'SLEEP' -Decision "tick complete, total_duration_ms=$TotalMs, final_cost=0.015 USD" -HasIssue $false -Extras @{duration_ms = 3}

# --- Summary -----------------------------------------------------------------
Write-Host ""
Write-Host "=== Tick summary ==="
Write-Host "Lines written:   $((Get-Content $PulseLog).Count) (expected 8)"
Write-Host "Phases:          WAKE PROBE DECIDE EXECUTE OBSERVE LEARN SIGNAL SLEEP"
Write-Host "Standards used:  7 (mission-contract, soa-routing, gate-decisions, forbidden-words, sla-triple, expected-proof, writeback-policy)"
Write-Host "Total cost:      0.015 USD (mock MiniMax 2.7 rates)"
Write-Host "Total duration:  ${TotalMs}ms"
Write-Host "Final gate:      PASS"
Write-Host ""
Write-Host "=== pulse.log ==="
Get-Content $PulseLog
