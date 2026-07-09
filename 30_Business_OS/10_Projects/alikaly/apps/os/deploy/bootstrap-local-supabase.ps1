# ============================================================================
# Alykaly OS — Local Supabase bootstrap (Windows PowerShell)
#
# Prereqs:
#   - Docker Desktop running
#   - Supabase CLI installed (https://supabase.com/docs/guides/cli)
#
# Run from project root:
#   powershell -ExecutionPolicy Bypass -File .\deploy\bootstrap-local-supabase.ps1
# ============================================================================
$ErrorActionPreference = 'Stop'

Write-Host '== Alykaly OS / Local Supabase bootstrap ==' -ForegroundColor Cyan
Write-Host ''

# Step 1: docker check
Write-Host '[1/6] Verifying Docker daemon...'
docker info --format '{{.ServerVersion}}' | Out-Null
Write-Host 'Docker OK' -ForegroundColor Green

# Step 2: supabase cli check
Write-Host '[2/6] Verifying Supabase CLI...'
$cli = Get-Command supabase -ErrorAction SilentlyContinue
if (-not $cli) { Write-Error 'Supabase CLI not found in PATH'; exit 1 }
supabase --version
Write-Host 'Supabase CLI OK' -ForegroundColor Green

# Step 3: init if needed (idempotent)
Write-Host '[3/6] supabase init (skip if already initialized)...'
if (-not (Test-Path 'supabase/.gitignore')) {
  supabase init --workdir . | Out-Host
}

# Step 4: start
Write-Host '[4/6] Starting local Supabase stack (first run downloads ~2GB)...'
supabase start | Out-Host

# Step 5: reset DB = apply all migrations + seed
Write-Host '[5/6] supabase db reset — applying migrations + seed...'
supabase db reset --no-seed:$false | Out-Host

# Step 6: print credentials for .env.local
Write-Host ''
Write-Host '[6/6] Printing credentials for .env.local:' -ForegroundColor Cyan
supabase status | Out-Host

Write-Host ''
Write-Host '== Done. Next steps ==' -ForegroundColor Green
Write-Host '  1. Copy the API URL + anon key + service_role key from above into .env.local'
Write-Host '  2. Run: npm install'
Write-Host '  3. Run: npm run dev   (app on http://localhost:4444)'
Write-Host '  4. Supabase Studio:  http://127.0.0.1:54323'
