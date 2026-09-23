param(
  [Parameter(Mandatory=$true)]
  [ValidateSet('supervisor','dispatcher')]
  [string]$Mode
)

$ErrorActionPreference = 'Stop'
$Root = 'C:\Users\amado\ASpace_OS_V3'
$Orca = 'C:\Users\amado\AppData\Local\Programs\orca\resources\bin\orca.exe'
$LogDir = Join-Path $env:USERPROFILE '.aspace\hermes-cron'
$LogFile = Join-Path $LogDir ($Mode + '.log')
$StateFile = Join-Path $env:USERPROFILE '.aspace\hermes-executive.json'
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

function Log([string]$Message) {
  Add-Content -LiteralPath $LogFile -Value ("[{0}] {1}" -f (Get-Date -Format o), $Message)
}

function OrcaJson([string[]]$CliArgs) {
  $raw = & $Orca @CliArgs 2>&1 | Out-String
  if ($LASTEXITCODE -ne 0) { throw "orca failed: $raw" }
  return ($raw | ConvertFrom-Json)
}

try {
  # A no-work supervisor cycle must not consume an LLM turn or create a terminal.
  if ($Mode -eq 'supervisor') {
    $guard = Join-Path $Root '10_Tech_OS\kernel\fleet_ownership.py'
    $preflightRaw = & python $guard --supervisor-preflight 2>&1 | Out-String
    if ($LASTEXITCODE -ne 0) { throw "WorkGraph preflight failed: $preflightRaw" }
    $preflight = $preflightRaw | ConvertFrom-Json
    if (-not $preflight.wake) {
      Log 'No active Jules binding or ambiguous dispatch; skipped without LLM.'
      exit 0
    }
  }
  $status = OrcaJson @('status','--json')
  if (-not $status.ok) { throw 'Orca runtime not ready' }

  $list = OrcaJson @('terminal','list','--worktree',"path:$Root",'--json')
  $preferredHandle = $null
  if (Test-Path -LiteralPath $StateFile) {
    try { $preferredHandle = (Get-Content -Raw -LiteralPath $StateFile | ConvertFrom-Json).handle } catch {}
  }

  $term = $null
  if ($preferredHandle) {
    $term = @($list.result.terminals) |
      Where-Object { $_.connected -eq $true -and $_.agentIdentity -eq 'hermes' -and $_.handle -eq $preferredHandle } |
      Select-Object -First 1
  }

  if (-not $term) {
    Log 'Pinned Hermes executive absent; creating replacement Hermes terminal.'
    $created = OrcaJson @('terminal','create','--worktree',"path:$Root",'--title','HERMES_EXECUTIVE','--command','hermes','--json')
    $handle = $created.result.terminal.handle
    if (-not $handle) { $handle = $created.result.handle }
    if (-not $handle) { throw 'Could not resolve newly created Hermes terminal handle' }
    @{handle=$handle; workspace=$Root; role='Hermes Executive'} | ConvertTo-Json | Set-Content -LiteralPath $StateFile -Encoding UTF8
    Start-Sleep -Seconds 8
    $bootstrap = "Load C:/Users/amado/ASpace_OS_V3/40_Memory_Wiki_OKF/architecture/hermes_field_visionary_orca_jules_2026-09-19.md. You are Hermes field visionary/executive operator beneath Amadeus/Kirby A0. Linear projects are the human control tower; uc.db/WorkGraph is source of truth. Acknowledge internally and remain ready."
    OrcaJson @('terminal','send','--terminal',$handle,'--text',$bootstrap,'--enter','--wait-submit','5','--json') | Out-Null
    Start-Sleep -Seconds 5
  } else {
    $handle = $term.handle
  }

  $idleRaw = & $Orca terminal wait --terminal $handle --for tui-idle --timeout-ms 1500 --json 2>&1 | Out-String
  if ($LASTEXITCODE -ne 0) {
    Log "Hermes busy; skipped $Mode tick."
    exit 0
  }

  if ($Mode -eq 'supervisor') {
    $prompt = @'
SCHEDULED HERMES SUPERVISOR TICK — EXECUTE, DO NOT JUST REPORT.

Use the existing Jules bridge http://127.0.0.1:43118 and uc.db / WorkGraph as source of truth. Inspect every session_binding where harness=jules and status=active. Resolve each Jules session by actual API state.

Rules:
- IN_PROGRESS: verify the same work_id/session binding and renew only its existing claim via uc.py beat; no duplicate session and no noisy Linear comment.
- Inspect unresolved fleet_dispatch_attempt events without a binding; reconcile actual provider sessions before any retry. Never clear an ambiguous attempt without evidence.
- AWAITING_USER_FEEDBACK / waiting for interaction: inspect the existing session and send a continuation message to THAT SAME session telling Jules to proceed autonomously with the already-scoped work, run tests, finish/create the PR, and ask A0 only for an irreversible decision or unavailable external credential.
- COMPLETED: capture PR/output evidence, reconcile the binding to closed, update the matching Linear issue with one concise evidence delta, and move to In Review only if acceptance is actually satisfied.
- FAILED: record failure honestly. Reuse/recover existing sessions where possible; create a new recovery session only if continuation is impossible and work is still required.
- Never create duplicates for a live work_id.
- Do not edit repo code yourself.
- Linear semantic grouping is Project-first: Tech OS — Kernel Core, Tech OS — Life Core, Tech OS — Buzz Core. Teams are only routing constraints.
- Do not start Life OS or Business OS feature work.
Return a compressed executive delta only after actions are taken.
'@
  } else {
    $prompt = @'
SCHEDULED HERMES EXECUTIVE DISPATCH TICK — ADVANCE REAL TECH OS WORK.

Scan open issues only in these Linear projects: Tech OS — Kernel Core, Tech OS — Life Core, Tech OS — Buzz Core. Teams are routing constraints, not the semantic primitive. Do not start Life OS or Business OS feature work.

Use orca linear list-issues --project for each exact project name (not an invented list command). Process Review first, then genuine In Progress, then Backlog. For each issue, reconcile its work_id against uc.db/WorkGraph and current session bindings. Pick the highest-priority READY issue that is not already covered by a live worker/session. Prefer existing Hermes/Jules sessions over duplicates. Use Orca for task/dispatch provenance. Delegate bounded repo-backed implementation to Jules; otherwise choose another harness only when its needed capability is proven. Before launch, acquire an atomic uc.py claim on the eligible work_id. Immediately bind the returned external session to that work_id. In Progress requires an unexpired claim, active binding and freshly observed executing worker; queued or historic sessions do not qualify. Post one concise Linear progress comment with provenance. Do not mark done because a provider answered: require durable evidence, tests/PR when applicable, and independent review. If no issue is safely dispatchable, do nothing except record the concrete blocker. Never ask A0 to manage terminals, PIDs, retries, or plumbing.
'@
  }

  $send = OrcaJson @('terminal','send','--terminal',$handle,'--text',$prompt,'--enter','--wait-submit','5','--json')
  Log ("Submitted $Mode tick to $handle request=" + $send.id)
  exit 0
}
catch {
  Log ("ERROR: " + $_.Exception.Message)
  exit 1
}
