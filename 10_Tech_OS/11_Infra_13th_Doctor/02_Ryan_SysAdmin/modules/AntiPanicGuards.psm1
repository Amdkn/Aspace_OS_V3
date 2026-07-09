#Requires -Version 7.0
<#
.SYNOPSIS
    AntiPanicGuards.psm1 — Couche de mitigation des paniques agentiques.

.DESCRIPTION
    Module canonique implementant les guards anti-panique definis par :
      - ADR-HEART-002 (couche tick anti-panique mode lean)
      - ADR-INFRA-001 (Tmux/PM2 process managers)
      - SDD-001 §1.2 (taxonomie 4+4 paniques)

    Mitige structurellement les paniques Kernel K1-K4 et complete les
    process managers (Tmux/PM2) pour les paniques Framework Type 1-4.

.NOTES
    Niveau     : L0 Tech OS
    Squad      : Ryan SysAdmin (13th Doctor)
    Statut     : Phase 1 cluster A2 — debloque Symphony Phase 2
    Date       : 2026-05-27
    Auteur     : A0 Amadeus + A2 Claude Code
    Module     : AntiPanicGuards (export 6 fonctions publiques)

.LINK
    ADR-HEART-002_heartbeat-anti-panique-openclaw-paperclip.md
    ADR-INFRA-001_tmux-wsl-dev-pm2-vps-prod.md
    ADR-RICK-001_openharness-incarnation.md
#>

# ============================================================================
# Configuration module
# ============================================================================

$Script:GuardLogPath = Join-Path $env:USERPROFILE 'ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Shadow_L0\guards.log'
$Script:DonnaDLQPath = Join-Path $env:USERPROFILE 'ASpace_OS_V2\10_Tech_OS\11_Infra_13th_Doctor\Donna_DLQ'

if (-not (Test-Path (Split-Path $Script:GuardLogPath -Parent))) {
    New-Item -ItemType Directory -Force -Path (Split-Path $Script:GuardLogPath -Parent) | Out-Null
}
if (-not (Test-Path $Script:DonnaDLQPath)) {
    New-Item -ItemType Directory -Force -Path $Script:DonnaDLQPath | Out-Null
}

function Write-GuardLog {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [ValidateSet('INFO', 'WARN', 'PANIC', 'DLQ')]
        [string]$Level,

        [Parameter(Mandatory)]
        [string]$GuardName,

        [Parameter(Mandatory)]
        [string]$Message
    )
    $ts = Get-Date -Format 'yyyy-MM-ddTHH:mm:ssK'
    $line = "[{0}] [{1}] [{2}] {3}" -f $ts, $Level, $GuardName, $Message
    Add-Content -Path $Script:GuardLogPath -Value $line -Encoding UTF8
}

# ============================================================================
# K1 GUARD — Filesystem Blindness (Write-AndVerify)
# ============================================================================
<#
.SYNOPSIS
    Ecrit un fichier puis verifie qu'il a ete reellement persiste
    (lecture + hash compare) avant de retourner success.

.DESCRIPTION
    Panique K1 SDD-001 : un agent croit avoir ecrit un fichier alors
    qu'il y a eu un echec silencieux du systeme de fichiers (permissions,
    disque plein, chemin invalide swallowed). Le guard fait un round-trip
    write -> read -> SHA256 compare pour eliminer ce mode de panique.

.PARAMETER Path
    Chemin absolu du fichier a ecrire.

.PARAMETER Content
    Contenu a ecrire (string).

.PARAMETER Encoding
    Encodage. Defaut UTF8.

.EXAMPLE
    Write-AndVerify -Path 'C:\tmp\test.txt' -Content 'hello world'
    # Retourne $true si OK, $false + log PANIC si discrepance
#>
function Write-AndVerify {
    [CmdletBinding()]
    [OutputType([bool])]
    param(
        [Parameter(Mandatory)]
        [string]$Path,

        [Parameter(Mandatory)]
        [string]$Content,

        [string]$Encoding = 'UTF8'
    )

    try {
        $parent = Split-Path -Parent $Path
        if (-not (Test-Path $parent)) {
            New-Item -ItemType Directory -Force -Path $parent | Out-Null
        }

        Set-Content -Path $Path -Value $Content -Encoding $Encoding -NoNewline -ErrorAction Stop

        if (-not (Test-Path $Path)) {
            Write-GuardLog -Level 'PANIC' -GuardName 'K1-Write-AndVerify' `
                -Message "File NOT found after write: $Path"
            return $false
        }

        $readBack = Get-Content -Path $Path -Raw -Encoding $Encoding
        $readBack = $readBack -replace "`r`n", "`n"
        $expected = $Content -replace "`r`n", "`n"

        $hashRead = [System.BitConverter]::ToString(
            [System.Security.Cryptography.SHA256]::Create().ComputeHash(
                [System.Text.Encoding]::UTF8.GetBytes($readBack)
            )
        ).Replace('-', '')

        $hashExpected = [System.BitConverter]::ToString(
            [System.Security.Cryptography.SHA256]::Create().ComputeHash(
                [System.Text.Encoding]::UTF8.GetBytes($expected)
            )
        ).Replace('-', '')

        if ($hashRead -ne $hashExpected) {
            Write-GuardLog -Level 'PANIC' -GuardName 'K1-Write-AndVerify' `
                -Message "Hash mismatch on $Path. Expected=$($hashExpected.Substring(0,12)) Got=$($hashRead.Substring(0,12))"
            return $false
        }

        Write-GuardLog -Level 'INFO' -GuardName 'K1-Write-AndVerify' `
            -Message "Verified write: $Path ($($Content.Length) chars)"
        return $true
    }
    catch {
        Write-GuardLog -Level 'PANIC' -GuardName 'K1-Write-AndVerify' `
            -Message "Exception on $Path : $($_.Exception.Message)"
        return $false
    }
}

# ============================================================================
# K2 GUARD — Hallucination Succes (Result-After-Write check)
# ============================================================================
<#
.SYNOPSIS
    Verifie qu'un resultat d'operation correspond a une condition observable
    avant de declarer success.

.DESCRIPTION
    Panique K2 SDD-001 : un agent halluciner du succes ("done", "completed")
    sans avoir verifie un effet de bord observable. Le guard force une
    verification factuelle par ScriptBlock fourni par l'appelant.

.PARAMETER Operation
    Nom de l'operation (pour log).

.PARAMETER VerifyScript
    ScriptBlock qui retourne $true si l'effet observable est present.

.PARAMETER TimeoutSec
    Timeout en secondes pour l'observation. Defaut 30.

.PARAMETER PollIntervalMs
    Intervalle entre les checks. Defaut 500ms.

.EXAMPLE
    Confirm-RealOutcome -Operation 'CreateBucket' -VerifyScript {
        Test-Path 'C:\storage\new_bucket'
    }
#>
function Confirm-RealOutcome {
    [CmdletBinding()]
    [OutputType([bool])]
    param(
        [Parameter(Mandatory)]
        [string]$Operation,

        [Parameter(Mandatory)]
        [scriptblock]$VerifyScript,

        [int]$TimeoutSec = 30,

        [int]$PollIntervalMs = 500
    )

    $deadline = (Get-Date).AddSeconds($TimeoutSec)
    $checks = 0

    while ((Get-Date) -lt $deadline) {
        $checks++
        try {
            $result = & $VerifyScript
            if ($result -eq $true) {
                Write-GuardLog -Level 'INFO' -GuardName 'K2-Confirm-RealOutcome' `
                    -Message "Operation '$Operation' confirmed after $checks check(s)"
                return $true
            }
        }
        catch {
            Write-GuardLog -Level 'WARN' -GuardName 'K2-Confirm-RealOutcome' `
                -Message "VerifyScript threw on '$Operation' check #$checks : $($_.Exception.Message)"
        }
        Start-Sleep -Milliseconds $PollIntervalMs
    }

    Write-GuardLog -Level 'PANIC' -GuardName 'K2-Confirm-RealOutcome' `
        -Message "Operation '$Operation' NOT confirmed after $checks checks in $TimeoutSec sec"
    return $false
}

# ============================================================================
# K3 GUARD — Secret Leak 401 (auth-error halt)
# ============================================================================
<#
.SYNOPSIS
    Invoque un appel API en arretant immediatement si 401/403 est detecte
    (au lieu de retry en boucle et leak un secret).

.DESCRIPTION
    Panique K3 SDD-001 : un agent reessaie un appel auth-failed en boucle,
    consommant des credits, leakant des logs, et masquant le vrai probleme
    (token revoke/expire). Le guard intercepte 401/403, ecrit un DLQ
    Donna, et halt immediatement.

.PARAMETER Uri
    URL de l'endpoint.

.PARAMETER Method
    HTTP method. Defaut GET.

.PARAMETER Headers
    Hashtable des headers.

.PARAMETER Body
    Body pour POST/PUT/PATCH.

.PARAMETER MaxRetries
    Nombre de retries autorises pour erreurs NON-auth (network etc). Defaut 3.

.EXAMPLE
    Invoke-AuthSafeCall -Uri 'https://api.notion.com/v1/users/me' -Headers @{
        Authorization = "Bearer ntn_..."
        'Notion-Version' = '2022-06-28'
    }
#>
function Invoke-AuthSafeCall {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$Uri,

        [string]$Method = 'GET',

        [hashtable]$Headers = @{},

        $Body = $null,

        [int]$MaxRetries = 3
    )

    $attempt = 0
    while ($attempt -lt $MaxRetries) {
        $attempt++
        try {
            $params = @{
                Uri             = $Uri
                Method          = $Method
                Headers         = $Headers
                ErrorAction     = 'Stop'
                TimeoutSec      = 30
            }
            if ($Body) { $params.Body = $Body }
            if ($Body -and $Method -in @('POST', 'PUT', 'PATCH')) {
                $params.ContentType = 'application/json'
            }

            $response = Invoke-RestMethod @params
            Write-GuardLog -Level 'INFO' -GuardName 'K3-Invoke-AuthSafeCall' `
                -Message "$Method $Uri OK (attempt $attempt)"
            return $response
        }
        catch {
            $statusCode = $null
            if ($_.Exception.Response) {
                $statusCode = [int]$_.Exception.Response.StatusCode
            }

            if ($statusCode -in @(401, 403)) {
                $dlqFile = Join-Path $Script:DonnaDLQPath ("auth-fail-{0}.json" -f (Get-Date -Format 'yyyyMMddHHmmss'))
                $dlqPayload = @{
                    timestamp = (Get-Date -Format 'o')
                    uri = $Uri
                    method = $Method
                    statusCode = $statusCode
                    error = $_.Exception.Message
                    headerKeys = $Headers.Keys
                } | ConvertTo-Json -Depth 5
                Set-Content -Path $dlqFile -Value $dlqPayload -Encoding UTF8

                Write-GuardLog -Level 'PANIC' -GuardName 'K3-Invoke-AuthSafeCall' `
                    -Message "AUTH FAIL ($statusCode) on $Method $Uri. HALT. DLQ written: $dlqFile"
                throw "K3 PANIC HALT: $statusCode on $Uri. Rotate secret. DLQ: $dlqFile"
            }

            if ($attempt -ge $MaxRetries) {
                Write-GuardLog -Level 'PANIC' -GuardName 'K3-Invoke-AuthSafeCall' `
                    -Message "Max retries ($MaxRetries) reached on $Method $Uri : $($_.Exception.Message)"
                throw
            }

            $backoffMs = [int]([math]::Pow(2, $attempt) * 500)
            Write-GuardLog -Level 'WARN' -GuardName 'K3-Invoke-AuthSafeCall' `
                -Message "Retry $attempt/$MaxRetries after ${backoffMs}ms : $($_.Exception.Message)"
            Start-Sleep -Milliseconds $backoffMs
        }
    }
}

# ============================================================================
# K4 GUARD — Dead Kernel (runner health probe)
# ============================================================================
<#
.SYNOPSIS
    Sonde la sante d'un runner Tmux session ou PM2 process.

.DESCRIPTION
    Panique K4 SDD-001 : kernel mort silencieusement (process zombie,
    tmux session frozen). Le guard ping les runners et retourne un
    bilan structure.

.PARAMETER RunnerType
    'Tmux' ou 'PM2' ou 'Both'.

.PARAMETER TmuxSessionName
    Nom de la session Tmux a verifier. Defaut 'aspace'.

.EXAMPLE
    Test-RunnerHealth -RunnerType Both
#>
function Test-RunnerHealth {
    [CmdletBinding()]
    param(
        [ValidateSet('Tmux', 'PM2', 'Both')]
        [string]$RunnerType = 'Both',

        [string]$TmuxSessionName = 'aspace'
    )

    $report = [ordered]@{
        timestamp = (Get-Date -Format 'o')
        tmux = $null
        pm2 = $null
        healthy = $true
    }

    if ($RunnerType -in @('Tmux', 'Both')) {
        try {
            $tmuxList = wsl tmux ls 2>&1
            if ($LASTEXITCODE -ne 0 -or $tmuxList -match 'no server running') {
                $report.tmux = @{ status = 'DOWN'; sessions = @() }
                $report.healthy = $false
                Write-GuardLog -Level 'WARN' -GuardName 'K4-Test-RunnerHealth' `
                    -Message "Tmux server not running"
            }
            else {
                $sessions = @($tmuxList | Select-String -Pattern '^([^:]+):' | ForEach-Object { $_.Matches[0].Groups[1].Value })
                $hasAspace = $sessions -contains $TmuxSessionName
                $report.tmux = @{
                    status   = if ($hasAspace) { 'UP' } else { 'PARTIAL' }
                    sessions = $sessions
                }
                if (-not $hasAspace) { $report.healthy = $false }
            }
        }
        catch {
            $report.tmux = @{ status = 'ERROR'; error = $_.Exception.Message }
            $report.healthy = $false
        }
    }

    if ($RunnerType -in @('PM2', 'Both')) {
        try {
            $pm2json = pm2 jlist 2>&1 | Out-String
            if ($LASTEXITCODE -ne 0) {
                $report.pm2 = @{ status = 'DOWN'; processes = @() }
                Write-GuardLog -Level 'INFO' -GuardName 'K4-Test-RunnerHealth' `
                    -Message "PM2 not installed or no processes (dev workstation OK)"
            }
            else {
                $procs = $pm2json | ConvertFrom-Json
                $report.pm2 = @{
                    status    = if ($procs.Count -gt 0) { 'UP' } else { 'EMPTY' }
                    processes = @($procs | ForEach-Object { @{
                        name   = $_.name
                        status = $_.pm2_env.status
                        uptime = $_.pm2_env.pm_uptime
                    }})
                }
                $deadOnes = @($procs | Where-Object { $_.pm2_env.status -ne 'online' })
                if ($deadOnes.Count -gt 0) {
                    $report.healthy = $false
                    Write-GuardLog -Level 'WARN' -GuardName 'K4-Test-RunnerHealth' `
                        -Message "PM2 has $($deadOnes.Count) non-online process(es)"
                }
            }
        }
        catch {
            $report.pm2 = @{ status = 'ERROR'; error = $_.Exception.Message }
        }
    }

    return [PSCustomObject]$report
}

# ============================================================================
# DLQ helper — Donna Dead Letter Queue
# ============================================================================
<#
.SYNOPSIS
    Ecrit un payload dans Donna DLQ pour traitement humain ulterieur.
#>
function Send-ToDonnaDLQ {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$Source,

        [Parameter(Mandatory)]
        $Payload,

        [string]$Reason = 'unspecified'
    )
    $fname = "{0}-{1}.json" -f $Source, (Get-Date -Format 'yyyyMMddHHmmssfff')
    $fpath = Join-Path $Script:DonnaDLQPath $fname
    $envelope = @{
        timestamp = (Get-Date -Format 'o')
        source    = $Source
        reason    = $Reason
        payload   = $Payload
    } | ConvertTo-Json -Depth 10
    Set-Content -Path $fpath -Value $envelope -Encoding UTF8
    Write-GuardLog -Level 'DLQ' -GuardName 'DonnaDLQ' `
        -Message "Wrote to DLQ: $fname (source=$Source reason=$Reason)"
    return $fpath
}

# ============================================================================
# Heartbeat tick (mode lean ADR-HEART-002)
# ============================================================================
<#
.SYNOPSIS
    Emet un heartbeat tick pour une capsule agent. Mode lean = file-based.
#>
function Send-HeartbeatTick {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$AgentName,

        [string]$Status = 'alive',

        [hashtable]$Extra = @{}
    )
    $tickDir = Join-Path $env:USERPROFILE 'ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Shadow_L0\heartbeats'
    if (-not (Test-Path $tickDir)) {
        New-Item -ItemType Directory -Force -Path $tickDir | Out-Null
    }
    $tickFile = Join-Path $tickDir "$AgentName.json"
    $payload = @{
        agent     = $AgentName
        status    = $Status
        timestamp = (Get-Date -Format 'o')
        extra     = $Extra
    } | ConvertTo-Json -Depth 5
    Set-Content -Path $tickFile -Value $payload -Encoding UTF8
}

# ============================================================================
# Exports
# ============================================================================

Export-ModuleMember -Function @(
    'Write-AndVerify',          # K1 guard
    'Confirm-RealOutcome',       # K2 guard
    'Invoke-AuthSafeCall',       # K3 guard
    'Test-RunnerHealth',         # K4 guard
    'Send-ToDonnaDLQ',           # DLQ helper
    'Send-HeartbeatTick'         # Heartbeat tick
)
