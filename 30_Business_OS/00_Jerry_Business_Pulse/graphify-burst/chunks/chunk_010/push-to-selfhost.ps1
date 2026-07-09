# ============================================================================
# Alykaly OS — Push migrations to self-hosted Supabase (supabase.kalybana.com)
#
# Usage:
#   $env:SUPABASE_DB_URL="postgres://postgres:<pwd>@supabase.kalybana.com:5432/postgres"
#   powershell -ExecutionPolicy Bypass -File .\deploy\push-to-selfhost.ps1
#
# Or with link (if project ref is known):
#   supabase link --project-ref <ref>
#   supabase db push
# ============================================================================
$ErrorActionPreference = 'Stop'

Write-Host '== Push migrations to self-hosted Supabase ==' -ForegroundColor Cyan
Write-Host ''

if (-not $env:SUPABASE_DB_URL) {
  Write-Host 'ERROR: SUPABASE_DB_URL env var not set' -ForegroundColor Red
  Write-Host 'Set it like:'
  Write-Host '  $env:SUPABASE_DB_URL="postgres://postgres:PASSWORD@supabase.kalybana.com:5432/postgres"'
  exit 1
}

Write-Host '[1/3] supabase db push --db-url <REDACTED>'
supabase db push --db-url $env:SUPABASE_DB_URL

Write-Host '[2/3] Deploy edge functions:'
$functions = @('sob-engine-simulate', 'docusign-webhook', 'intake-handler', 'case-confidence-recalc', 'audit-rotate')
foreach ($fn in $functions) {
  Write-Host "  -> deploying $fn"
  supabase functions deploy $fn --no-verify-jwt
}

Write-Host '[3/3] Generate TypeScript types from production schema:'
supabase gen types typescript --db-url $env:SUPABASE_DB_URL > src/lib/supabase/database.types.ts
Write-Host 'Types written to src/lib/supabase/database.types.ts'

Write-Host ''
Write-Host '== Done ==' -ForegroundColor Green
Write-Host 'Verify:'
Write-Host '  curl https://supabase.kalybana.com/functions/v1/sob-engine-simulate -H "apikey: <ANON_KEY>"'
