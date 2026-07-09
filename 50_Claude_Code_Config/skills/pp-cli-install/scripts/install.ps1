# pp-cli-install — Install a Printing Press CLI for <Service>
# Usage:
#   powershell -NoProfile -ExecutionPolicy Bypass -File install.ps1 -Service stripe
#   powershell -NoProfile -ExecutionPolicy Bypass -File install.ps1 -Service clickup -SpecUrl https://developer.clickup.com/openapi/ClickUp_PUBLIC_API_V3.yaml
#   powershell -NoProfile -ExecutionPolicy Bypass -File install.ps1 -Service airtable -DocsUrl https://airtable.com/developers/web/api/introduction
# Exit codes:
#   0 = success
#   2 = service not resolvable (no upstream, no spec, no docs URL)
#   3 = download failed
#   4 = go build failed
#   5 = smoke test failed

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)][string]$Service,
    [string]$SpecUrl,
    [string]$DocsUrl,
    [switch]$Force
)

$ErrorActionPreference = 'Stop'

# === Paths ===
$BinDir = 'C:\Users\amado\AppData\Local\Programs\pp-clis'
$PPExe = 'C:\Users\amado\AppData\Local\Programs\printing-press\printing-press.exe'
$GoBin = 'C:\Users\amado\AppData\Local\Programs\go\bin'
$LibraryDir = "C:\Users\amado\printing-press\library\$Service"
$SettingsJson = 'C:\Users\amado\.claude\settings.json'
$WikiLog = 'C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki\log.md'
$CliName = "$Service-pp-cli"
$McpName = "$Service-pp-mcp"
$CliExe = Join-Path $BinDir "$CliName.exe"

# Ensure Go is in PATH for any go builds
if (-not (Test-Path $BinDir)) { New-Item -ItemType Directory -Force -Path $BinDir | Out-Null }
$env:Path = "$GoBin;$BinDir;$env:Path"

function Write-Step($msg) { Write-Host "[pp-cli-install] $msg" -ForegroundColor Cyan }
function Write-Warn($msg) { Write-Host "[pp-cli-install] WARN: $msg" -ForegroundColor Yellow }
function Write-Err($msg) { Write-Host "[pp-cli-install] ERROR: $msg" -ForegroundColor Red }

# === Idempotency check ===
if ((Test-Path $CliExe) -and -not $Force) {
    Write-Step "$CliName already installed at $CliExe (use -Force to reinstall)"
    & $CliExe --version 2>&1 | Select-Object -First 1
    exit 0
}

# === STEP 1: Probe upstream printing-press-library ===
Write-Step "Probing upstream library for '$Service'..."
$Categories = @('ai', 'auth', 'cloud', 'commerce', 'developer-tools', 'devices', 'education',
    'food-and-dining', 'marketing', 'media-and-entertainment', 'monitoring', 'other',
    'payments', 'productivity', 'project-management', 'sales-and-crm',
    'social-and-messaging', 'travel')
$FoundCategory = $null
foreach ($cat in $Categories) {
    $url = "https://api.github.com/repos/mvanhorn/printing-press-library/contents/library/$cat/$Service"
    try {
        $null = Invoke-RestMethod -Uri $url -UseBasicParsing -ErrorAction Stop
        $FoundCategory = $cat
        Write-Step "Found in category: $cat"
        break
    }
    catch { continue }
}

# === STEP 2: If found upstream, grab the pre-built binary ===
if ($FoundCategory) {
    $tag = "$Service-current"
    Write-Step "Downloading pre-built release '$tag'..."
    $cliUrl = "https://github.com/mvanhorn/printing-press-library/releases/download/$tag/$Service-pp-cli-windows-amd64.exe"
    $mcpUrl = "https://github.com/mvanhorn/printing-press-library/releases/download/$tag/$Service-pp-mcp-windows-amd64.mcpb"
    try {
        Invoke-WebRequest -Uri $cliUrl -OutFile $CliExe -UseBasicParsing
        try { Invoke-WebRequest -Uri $mcpUrl -OutFile (Join-Path $BinDir "$McpName.mcpb") -UseBasicParsing } catch { Write-Warn "MCP bundle not available (skipped)" }
        Write-Step "Downloaded $CliExe"
    }
    catch {
        Write-Err "Download failed from $cliUrl : $($_.Exception.Message)"
        exit 3
    }
}
else {
    # === STEP 3-5: Generate locally ===
    Write-Step "Service '$Service' not in upstream library. Falling back to local generation."

    if (-not (Test-Path $PPExe)) {
        Write-Err "printing-press not installed at $PPExe"
        exit 2
    }

    $genArgs = @('generate', '--name', $Service, '--output', $LibraryDir)
    if ($SpecUrl) {
        Write-Step "Generating from --spec $SpecUrl"
        $genArgs += @('--spec', $SpecUrl)
    }
    elseif ($DocsUrl) {
        Write-Warn "Using --docs path. This consumes Claude/Codex LLM quota."
        $genArgs += @('--docs', $DocsUrl)
    }
    else {
        Write-Err "No upstream pre-built found, and no -SpecUrl or -DocsUrl provided."
        Write-Host "Suggestions:"
        Write-Host "  - Check references/catalog-snapshot.md for the exact service name."
        Write-Host "  - Add a direct OpenAPI URL via -SpecUrl <url>."
        Write-Host "  - Use -DocsUrl <docs-url> as last resort."
        exit 2
    }

    & $PPExe @genArgs
    if ($LASTEXITCODE -ne 0) {
        Write-Err "printing-press generate failed (exit $LASTEXITCODE)"
        exit 4
    }

    # Build each cmd/<binary>/ subdir
    Push-Location $LibraryDir
    try {
        & "$GoBin\go.exe" mod tidy
        if ($LASTEXITCODE -ne 0) { throw "go mod tidy failed" }
        Get-ChildItem -Path 'cmd' -Directory | ForEach-Object {
            $name = $_.Name
            Write-Step "Building $name..."
            & "$GoBin\go.exe" build -o "$name.exe" "./cmd/$name"
            if ($LASTEXITCODE -ne 0) { throw "go build $name failed" }
            Copy-Item -Path "$name.exe" -Destination $BinDir -Force
        }
    }
    catch {
        Write-Err $_.Exception.Message
        Pop-Location
        exit 4
    }
    Pop-Location
}

# === STEP 6: Register bypass wildcard in settings.json ===
Write-Step "Registering bypass wildcard..."
$settings = Get-Content $SettingsJson -Raw | ConvertFrom-Json
$wildcard = "Bash($CliName" + ":*)"
if ($settings.permissions.allow -notcontains $wildcard) {
    $settings.permissions.allow += $wildcard
    $settings | ConvertTo-Json -Depth 100 | Set-Content -Path $SettingsJson -Encoding UTF8
    Write-Step "Added $wildcard to settings.json"
}
else {
    Write-Step "Wildcard already present"
}

# === STEP 7: Smoke test ===
Write-Step "Smoke test --help"
& $CliExe --help 2>&1 | Select-Object -First 5
if ($LASTEXITCODE -ne 0) { Write-Err "--help failed"; exit 5 }

Write-Step "Smoke test doctor (best effort)"
try { & $CliExe doctor 2>&1 | Select-Object -First 10 } catch { Write-Warn "doctor unavailable (may require auth)" }

# === LOG ===
$today = Get-Date -Format 'yyyy-MM-dd'
$logEntry = @"

## [$today] proof    | pp-cli-install $Service via /pp-cli-install skill

**Action :** Skill /pp-cli-install ran end-to-end for ``$Service``.

**Path taken :** $(if ($FoundCategory) { "upstream library category=$FoundCategory" } elseif ($SpecUrl) { "local generate --spec $SpecUrl" } else { "local generate --docs $DocsUrl" })

**Binary :** ``$CliExe`` (registered in settings.json with ``$wildcard``)

**Smoke test :** ``$CliName --help`` exit 0.

"@
Add-Content -Path $WikiLog -Value $logEntry
Write-Step "Logged to $WikiLog"

Write-Host ""
Write-Step "DONE - $CliName ready. Use it via Bash (bypass-allowed)."
exit 0
