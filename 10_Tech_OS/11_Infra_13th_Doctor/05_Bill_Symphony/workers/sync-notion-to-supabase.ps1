#Requires -Version 7.0
<#
.SYNOPSIS
    Symphony Phase 2 Worker -- Sync Notion MASTER_SOP_DB to Supabase tenant.<slug>.sops

.DESCRIPTION
    Worker idempotent qui :
      1. Liste les SOPs depuis Notion MASTER_SOP_DB via Bearer Internal Integration
      2. Mappe vers le schema tenant_<slug>.sops
      3. UPSERT via ON CONFLICT (notion_page_id)
      4. Log dans symphony_log de la tenant

    Conforme :
      - ADR-MESH-L2-001 (Notion=WHAT, Supabase = miroir local pour Symphony)
      - ADR-INFRA-001 (cible PM2 VPS prod ; dev local via SSH pipe)
      - ADR-HEART-002 (AntiPanicGuards K1-K3 utilisees)
      - ADR-ID-001 (SOP_ID canonique)

.PARAMETER ProjectSlug
    Slug du tenant Supabase (default 'aspace_solaris').

.PARAMETER NotionDatabaseId
    Database ID MASTER_SOP_DB (default '6b07315e-06ca-4652-9049-d72a1e79e906').

.PARAMETER VpsHost
    Alias SSH du VPS (default 'aspace-vps' cf. ~/.ssh/config).

.PARAMETER DryRun
    Si specifie, n'execute pas le UPSERT, affiche seulement le SQL genere.

.EXAMPLE
    .\sync-notion-to-supabase.ps1
    # Sync vers tenant_aspace_solaris

.EXAMPLE
    .\sync-notion-to-supabase.ps1 -ProjectSlug acme -DryRun
    # Simule sync vers tenant_acme

.NOTES
    Date    : 2026-05-27
    Auteur  : A0 + A2 Claude Code
    Squad   : Bill Symphony (13th Doctor companion)
    Pre-req : NOTION_TOKEN env var User scope (Internal Integration ntn_xxx)
              + AntiPanicGuards.psm1 importable
              + SSH access to aspace-vps
              + tenant_<slug> schema deja provisionne (cf. supabase-schema-per-project.sql)
#>

[CmdletBinding()]
param(
    [string]$ProjectSlug      = 'aspace_solaris',
    [string]$NotionDatabaseId = '6b07315e-06ca-4652-9049-d72a1e79e906',
    [string]$VpsHost          = 'aspace-vps',
    [string]$NotionVersion    = '2022-06-28',
    [switch]$DryRun
)

# ============================================================================
# Bootstrap
# ============================================================================

$ErrorActionPreference = 'Stop'

$modulePath = Join-Path $PSScriptRoot '..\..\02_Ryan_SysAdmin\modules\AntiPanicGuards.psm1'
$modulePath = [System.IO.Path]::GetFullPath($modulePath)
if (-not (Test-Path $modulePath)) {
    throw "AntiPanicGuards.psm1 introuvable : $modulePath"
}
Import-Module $modulePath -Force

$NotionToken = [Environment]::GetEnvironmentVariable('NOTION_TOKEN', 'User')
if (-not $NotionToken) {
    throw "NOTION_TOKEN env var (User scope) non defini. Bascule Bearer requise."
}

$tenantSchema = "tenant_$ProjectSlug"
$startedAt    = Get-Date

Send-HeartbeatTick -AgentName 'sync-notion-to-supabase' -Status 'starting' -Extra @{
    project_slug = $ProjectSlug
    tenant       = $tenantSchema
}

# ============================================================================
# 1. Query Notion data source -- page through all SOPs
# ============================================================================

Write-Host "[1/3] Querying Notion MASTER_SOP_DB ($NotionDatabaseId)..." -ForegroundColor Cyan

$headers = @{
    'Authorization'  = "Bearer $NotionToken"
    'Notion-Version' = $NotionVersion
    'Content-Type'   = 'application/json'
}

$allResults = @()
$hasMore = $true
$nextCursor = $null
$pageCount = 0

while ($hasMore) {
    $body = @{ page_size = 100 }
    if ($nextCursor) { $body.start_cursor = $nextCursor }
    $bodyJson = $body | ConvertTo-Json -Compress

    $resp = Invoke-AuthSafeCall `
        -Uri "https://api.notion.com/v1/databases/$NotionDatabaseId/query" `
        -Method 'POST' `
        -Headers $headers `
        -Body $bodyJson `
        -MaxRetries 3

    $allResults += $resp.results
    $hasMore    = $resp.has_more
    $nextCursor = $resp.next_cursor
    $pageCount++
    Write-Host "  page $pageCount -> $($resp.results.Count) results (cumulative: $($allResults.Count))" -ForegroundColor DarkGray
}

Write-Host "  Total SOPs fetched: $($allResults.Count)" -ForegroundColor Green

# ============================================================================
# 2. Map Notion -> SQL rows
# ============================================================================

Write-Host "[2/3] Mapping to SQL rows..." -ForegroundColor Cyan

function ConvertTo-PgString {
    param([string]$Value)
    if ($null -eq $Value -or $Value -eq '') { return 'NULL' }
    "'" + ($Value -replace "'", "''") + "'"
}

function ConvertTo-PgArray {
    param([string[]]$Values)
    if (-not $Values -or $Values.Count -eq 0) { return 'NULL' }
    $escaped = $Values | ForEach-Object { '"' + ($_ -replace '"', '\"') + '"' }
    "'{" + ($escaped -join ',') + "}'"
}

function ConvertTo-PgNumeric {
    param($Value)
    if ($null -eq $Value) { return 'NULL' }
    return $Value.ToString([Globalization.CultureInfo]::InvariantCulture)
}

function ConvertTo-PgDate {
    param([string]$Value)
    if (-not $Value) { return 'NULL' }
    "'" + $Value + "'::date"
}

function ConvertTo-PgTimestamptz {
    param([string]$Value)
    if (-not $Value) { return 'NULL' }
    "'" + $Value + "'::timestamptz"
}

$rows = foreach ($page in $allResults) {
    $props = $page.properties

    $title = ($props.Title.title | ForEach-Object { $_.plain_text }) -join ''
    $domain = $props.Domain.select.name
    $status = $props.Status.select.name
    $owner_vp = $props.Owner_VP.select.name
    $executor_b3 = @($props.Executor_B3.multi_select | ForEach-Object { $_.name })
    $trigger = ($props.Trigger.rich_text | ForEach-Object { $_.plain_text }) -join ''
    $build_gate = ($props.Build_Gate.rich_text | ForEach-Object { $_.plain_text }) -join ''
    $template_version = ($props.Template_Version.rich_text | ForEach-Object { $_.plain_text }) -join ''
    $loom_url = $props.Loom_URL.url
    $context_pack_url = $props.Context_Pack_URL.url
    $number = $props.Number.number
    $last_audited = $props.Last_Audited.date.start
    $notion_updated_at = $page.last_edited_time

    $sopIdRaw = "SOP-L2-$($domain.ToUpper())-$(([int]$number).ToString('00'))"
    if (-not $domain -or -not $number) {
        Send-ToDonnaDLQ -Source 'sync-notion-to-supabase' -Reason 'missing_domain_or_number' -Payload @{
            page_id = $page.id
            title   = $title
            domain  = $domain
            number  = $number
        } | Out-Null
        continue
    }

    [PSCustomObject]@{
        sop_id            = $sopIdRaw
        notion_page_id    = $page.id
        title             = $title
        domain            = $domain
        status            = $status
        owner_vp          = $owner_vp
        executor_b3       = $executor_b3
        trigger           = $trigger
        build_gate        = $build_gate
        template_version  = $template_version
        loom_url          = $loom_url
        context_pack_url  = $context_pack_url
        number            = $number
        last_audited      = $last_audited
        notion_updated_at = $notion_updated_at
    }
}

Write-Host "  Mapped $(@($rows).Count) valid rows" -ForegroundColor Green

# ============================================================================
# 3. Build UPSERT SQL + send via SSH/psql
# ============================================================================

Write-Host "[3/3] Building UPSERT SQL..." -ForegroundColor Cyan

$sqlLines = @(
    "SET search_path = $tenantSchema;",
    "BEGIN;"
)

foreach ($r in $rows) {
    $sql = @"
INSERT INTO sops (sop_id, notion_page_id, title, domain, status, owner_vp, executor_b3, trigger, build_gate, template_version, loom_url, context_pack_url, number, last_audited, synced_at, notion_updated_at)
VALUES ($(ConvertTo-PgString $r.sop_id), $(ConvertTo-PgString $r.notion_page_id), $(ConvertTo-PgString $r.title), $(ConvertTo-PgString $r.domain), $(ConvertTo-PgString $r.status), $(ConvertTo-PgString $r.owner_vp), $(ConvertTo-PgArray $r.executor_b3), $(ConvertTo-PgString $r.trigger), $(ConvertTo-PgString $r.build_gate), $(ConvertTo-PgString $r.template_version), $(ConvertTo-PgString $r.loom_url), $(ConvertTo-PgString $r.context_pack_url), $(ConvertTo-PgNumeric $r.number), $(ConvertTo-PgDate $r.last_audited), now(), $(ConvertTo-PgTimestamptz $r.notion_updated_at))
ON CONFLICT (notion_page_id) DO UPDATE SET
  sop_id            = EXCLUDED.sop_id,
  title             = EXCLUDED.title,
  domain            = EXCLUDED.domain,
  status            = EXCLUDED.status,
  owner_vp          = EXCLUDED.owner_vp,
  executor_b3       = EXCLUDED.executor_b3,
  trigger           = EXCLUDED.trigger,
  build_gate        = EXCLUDED.build_gate,
  template_version  = EXCLUDED.template_version,
  loom_url          = EXCLUDED.loom_url,
  context_pack_url  = EXCLUDED.context_pack_url,
  number            = EXCLUDED.number,
  last_audited      = EXCLUDED.last_audited,
  synced_at         = now(),
  notion_updated_at = EXCLUDED.notion_updated_at;
"@
    $sqlLines += $sql
}

$sqlLines += "INSERT INTO symphony_log (worker, level, message, payload) VALUES ('sync-notion-to-supabase', 'INFO', 'Sync completed', jsonb_build_object('count', $($rows.Count), 'at', now()::text));"
$sqlLines += "COMMIT;"

$finalSql = $sqlLines -join "`n"

if ($DryRun) {
    Write-Host "[DRY-RUN] SQL preview:" -ForegroundColor Yellow
    Write-Host ($finalSql.Substring(0, [Math]::Min(1500, $finalSql.Length))) -ForegroundColor DarkGray
    Write-Host "... (truncated; $($finalSql.Length) total chars)" -ForegroundColor DarkGray
    Send-HeartbeatTick -AgentName 'sync-notion-to-supabase' -Status 'dryrun-ok'
    return
}

# ============================================================================
# Pipe via SSH to docker exec psql
# ============================================================================

Write-Host "  Piping to $VpsHost -> docker exec supabase-db psql..." -ForegroundColor Cyan

$tmpSqlLocal = Join-Path $env:TEMP "sync-notion-to-supabase-$($PID).sql"
$ok = Write-AndVerify -Path $tmpSqlLocal -Content $finalSql
if (-not $ok) {
    throw "Cant write tmp SQL file. K1 guard failed."
}

$remotePath = "/tmp/sync-notion-to-supabase-$([Guid]::NewGuid().ToString('N')).sql"
& scp $tmpSqlLocal "$VpsHost`:$remotePath"
if ($LASTEXITCODE -ne 0) { throw "scp failed (exit $LASTEXITCODE)" }

$sshCmd = "docker cp $remotePath supabase-db:$remotePath && docker exec supabase-db psql -U postgres -d postgres -f $remotePath -q && rm $remotePath"
$result = & ssh $VpsHost $sshCmd 2>&1
$sshExit = $LASTEXITCODE

Remove-Item $tmpSqlLocal -Force -ErrorAction SilentlyContinue

if ($sshExit -ne 0) {
    Send-ToDonnaDLQ -Source 'sync-notion-to-supabase' -Reason 'psql_apply_failed' -Payload @{
        exit   = $sshExit
        stderr = ($result -join "`n")
        rows   = $rows.Count
    } | Out-Null
    Send-HeartbeatTick -AgentName 'sync-notion-to-supabase' -Status 'panic' -Extra @{
        exit = $sshExit
    }
    throw "SSH/psql apply failed (exit $sshExit). DLQ entry written."
}

$durationSec = [int]((Get-Date) - $startedAt).TotalSeconds

Write-Host ""
Write-Host "[OK] Sync completed in ${durationSec}s. $($rows.Count) SOPs upserted into $tenantSchema.sops" -ForegroundColor Green

Send-HeartbeatTick -AgentName 'sync-notion-to-supabase' -Status 'ok' -Extra @{
    duration_sec = $durationSec
    rows         = $rows.Count
    tenant       = $tenantSchema
}
