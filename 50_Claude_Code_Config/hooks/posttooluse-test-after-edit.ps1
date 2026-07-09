# posttooluse-test-after-edit.ps1
# ADR-META-005 sibling hook — mechanizes M3's worst measured gap:
# "runs the real test after editing" = 33% (vs Opus 50%), 2026-06-25 analysis.
#
# DESIGN (sober, distinct from the Rick-vetoed hard-block Hook 1):
#   - fires only on code-file edits (skips .md / canon / _SPECS / wiki / json)
#   - runs the project's test command ONLY if one is auto-detectable
#   - timeout-capped (120s) so it can never hang a session
#   - LOG-ONLY: never blocks the turn (exit 0 always); appends a receipt
#   - if no test command is found -> silent no-op (D1: never invent a command)
#
# Reads PostToolUse hook input as JSON on stdin (tool_input.file_path).

$ErrorActionPreference = 'SilentlyContinue'
$LOG = "C:\Users\amado\.claude\logs\test-after-edit.log"
New-Item -ItemType Directory -Force -Path (Split-Path $LOG) | Out-Null

function Write-Receipt($line) {
  $ts = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
  Add-Content -Path $LOG -Value "[$ts] $line" -Encoding UTF8
}

# --- read hook stdin ---
$raw = [Console]::In.ReadToEnd()
if ([string]::IsNullOrWhiteSpace($raw)) { exit 0 }
try { $hook = $raw | ConvertFrom-Json } catch { exit 0 }

$file = $hook.tool_input.file_path
if ([string]::IsNullOrWhiteSpace($file)) { exit 0 }

# --- gate 1: code files only ---
$codeExt = @('.ts','.tsx','.js','.jsx','.mjs','.cjs','.py','.go','.rs','.java','.kt','.swift','.cs','.rb','.php')
$ext = [System.IO.Path]::GetExtension($file).ToLower()
if ($codeExt -notcontains $ext) { exit 0 }

# --- gate 2: skip canon / docs / specs even if code-ish ---
$skip = @('\wiki\','\_SPECS\','\30_MEMORY_CORE\','\graphify-out\','\node_modules\','\_TRASH')
foreach ($s in $skip) { if ($file -like "*$s*") { exit 0 } }

if (-not (Test-Path $file)) { exit 0 }

# --- find project root + derive a REAL test command (D1: only what exists) ---
$dir = Split-Path $file -Parent
$root = $null; $cmd = $null
for ($i = 0; $i -lt 8 -and $dir; $i++) {
  if (Test-Path (Join-Path $dir 'package.json')) {
    $pkg = Get-Content (Join-Path $dir 'package.json') -Raw | ConvertFrom-Json
    if ($pkg.scripts.test -and $pkg.scripts.test -notmatch 'no test specified') {
      $runner = if (Test-Path (Join-Path $dir 'pnpm-lock.yaml')) { 'pnpm' }
                elseif (Test-Path (Join-Path $dir 'yarn.lock')) { 'yarn' } else { 'npm' }
      $root = $dir; $cmd = "$runner test"; break
    }
  }
  if (Test-Path (Join-Path $dir 'pyproject.toml')) { $root = $dir; $cmd = 'pytest -q'; break }
  if (Test-Path (Join-Path $dir 'pytest.ini'))     { $root = $dir; $cmd = 'pytest -q'; break }
  if (Test-Path (Join-Path $dir 'Cargo.toml'))     { $root = $dir; $cmd = 'cargo test'; break }
  if (Test-Path (Join-Path $dir 'go.mod'))         { $root = $dir; $cmd = 'go test ./...'; break }
  $dir = Split-Path $dir -Parent
}

if (-not $cmd) {
  Write-Receipt "NO-TEST-CMD edited=$file  (M3 33% gap: no detectable test command, skipped)"
  exit 0
}

# --- run, timeout-capped, log-only ---
Write-Receipt "RUN  cmd='$cmd'  root=$root  edited=$file"
$job = Start-Job -ScriptBlock {
  param($r, $c)
  Push-Location $r
  $out = & cmd /c $c 2>&1 | Out-String
  Pop-Location
  [pscustomobject]@{ code = $LASTEXITCODE; out = $out }
} -ArgumentList $root, $cmd

if (Wait-Job $job -Timeout 120) {
  $res = Receive-Job $job
  $tail = ($res.out -split "`n" | Select-Object -Last 3) -join ' | '
  if ($res.code -eq 0) { Write-Receipt "PASS cmd='$cmd'  $tail" }
  else { Write-Receipt "FAIL($($res.code)) cmd='$cmd'  $tail" }
} else {
  Stop-Job $job
  Write-Receipt "TIMEOUT(120s) cmd='$cmd' root=$root  (capped, did not hang session)"
}
Remove-Job $job -Force
exit 0
