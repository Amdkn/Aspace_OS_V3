<#
.SYNOPSIS
  ADR-INFRA-002 — migrate a deep build-bearing repo to a short 30_Business_OS home + junction.
.DESCRIPTION
  Proven D10 recipe. Handles the broken .next that exceeds MAX_PATH (Remove-Item cannot delete it).
  Reversible: git history is preserved; the deep path becomes a junction to the short home.
.PARAMETER Deep
  Full current path of the repo (deep, under 01_Projects_Picard\...).
.PARAMETER Short
  Target short home, e.g. C:\Users\amado\ASpace_OS_V2\30_Business_OS\<short-kebab>.
.PARAMETER SkipBuild
  Skip the final 'npm run build' verification.
.EXAMPLE
  .\migrate_repo_home.ps1 -Deep "C:\...\01_solaris-aaas" -Short "C:\Users\amado\ASpace_OS_V2\30_Business_OS\solaris-aaas"
#>
param(
  [Parameter(Mandatory=$true)][string]$Deep,
  [Parameter(Mandatory=$true)][string]$Short,
  [switch]$SkipBuild
)
$ErrorActionPreference = 'Stop'

if (-not (Test-Path $Deep))  { throw "Deep path not found: $Deep" }
if (Test-Path $Short)        { throw "Short home already exists (abort to avoid clobber): $Short" }
if ((Get-Item $Deep).LinkType -eq 'Junction') { throw "Deep path is already a junction: $Deep" }

# 0. Safety — git must be clean
Push-Location $Deep
$dirty = (git status --porcelain) 2>$null
$head  = (git rev-parse --short HEAD) 2>$null
Pop-Location
if ($dirty) { throw "Git working tree is DIRTY. Commit/stash before migrating.`n$dirty" }
Write-Host "[1/5] git clean (HEAD $head)"

# 1. Move everything EXCEPT the gitignored .next (which may itself exceed MAX_PATH)
robocopy "$Deep" "$Short" /MOVE /E /XD ".next" /R:1 /W:1 /NFL /NDL /NP | Out-Null
if ($LASTEXITCODE -ge 8) { throw "robocopy /MOVE failed (exit $LASTEXITCODE)" }
Write-Host "[2/5] repo moved -> $Short"

# 2. Mirror-empty the leftover .next from an empty temp dir (only reliable >260-char delete)
if (Test-Path "$Deep\.next") {
  $empty = Join-Path $env:TEMP "empty_mir_$(Get-Random)"
  New-Item -ItemType Directory -Path $empty | Out-Null
  robocopy "$empty" "$Deep\.next" /MIR /R:0 /W:0 /NFL /NDL /NP | Out-Null
  Remove-Item -Recurse -Force "$Deep\.next" -ErrorAction SilentlyContinue
  Remove-Item -Recurse -Force $empty
  Write-Host "[3/5] leftover .next emptied + removed"
} else {
  Write-Host "[3/5] no leftover .next"
}

# 3. Remove the now-empty deep folder
Remove-Item -Force $Deep -ErrorAction SilentlyContinue
if (Test-Path $Deep) { throw "Deep folder not empty after move — inspect manually: $Deep" }

# 4. Junction deep -> short home
New-Item -ItemType Junction -Path $Deep -Target $Short | Out-Null
if ((Get-Item $Deep).LinkType -ne 'Junction') { throw "Junction creation failed" }
Write-Host "[4/5] junction created: $Deep -> $Short"

# 5. Verify GREEN build
if ($SkipBuild) { Write-Host "[5/5] build skipped (-SkipBuild)"; return }
Push-Location $Short
Write-Host "[5/5] npm run build ..."
npm run build
$ok = ($LASTEXITCODE -eq 0)
Pop-Location
if ($ok) { Write-Host "`nDONE — build GREEN at short path. D10 closed for this repo." }
else     { throw "Build FAILED at short path (exit $LASTEXITCODE) — investigate (not necessarily MAX_PATH)." }
