# worker_launch.ps1 <outfile> - lance UN worker WF1 par invocation DIRECTE (&) prouvee VIVANT.
# Raison d'etre (D6 2026-07-06) : claude = claude.ps1 (shim npm) -> Start-Process+redirect =
# InvalidOperationException. powershell.exe EST un exe -> le runner me spawn, MOI j'invoque claude en &.
#
# WARGAME 26 CAT.2 #7 - Contrat ticket (PATCH, 2026-07-07, additive) :
# Avant de spawn, je valide que le WORKER_PROMPT porte un format OPERATIONAL conforme
# (sections d'un worker canonique : START heartbeat / Séquence / EMERGENCY EXIT).
# Si le format manque, je REJECT avec exit 78 (EX_CONFIG).
#
# POURQUOI cette validation :
#   - Le WORKER_PROMPT est le MODE D'EMPLOI du worker (pas un wargame lui-même).
#   - Chaque iteration worker pioche 1 TICKET (wargame) dans la queue et l'exécute
#     selon le format de CE wargame (validé séparément par le feeder #4 cat.3).
#   - Ici on valide juste que le PROMPT INSTRUCTIONS est un worker prompt valide.
#
# Format operational attendu (le prompt doit porter ces 4 ancres) :
#   - "START" : ligne worklog de depart (preuve d'existence)
#   - "Séquence" (ou "## §1") : sequence obligatoire (lis / pioche / travaille / preuve / cloture)
#   - "PREUVE" : obligation de preuve (D1 verify-before-assert)
#   - "EMERGENCY" (ou "ctx-pressure") : sortie d'urgence si contexte sature
#
# Note PS-3 (future patch, hors C2) : wf1_runner.ps1 utilise actuellement son propre wrapper
# temp et bypasse ce script. La validation ici est CANONIQUE : tout futur feeder (#4)
# ou lancement manuel passera par worker_launch.ps1. Les wargames promus par le feeder
# seront valides par leur propre contrat (cat.3 #7 feeder-side, wargame 26 §M3).
param([Parameter(Mandatory=$true)][string]$OutFile)
$ErrorActionPreference = 'Continue'
$Citadel = $PSScriptRoot | Split-Path -Parent

# env M3 (User scope -> process) : jamais de valeur loggee
$env:ANTHROPIC_AUTH_TOKEN=[Environment]::GetEnvironmentVariable('ANTHROPIC_AUTH_TOKEN','User')
$env:ANTHROPIC_API_KEY=[Environment]::GetEnvironmentVariable('ANTHROPIC_API_KEY','User')
$env:ANTHROPIC_BASE_URL=[Environment]::GetEnvironmentVariable('ANTHROPIC_BASE_URL','User')

Set-Location $Citadel
$prompt = Get-Content (Join-Path $Citadel 'loops\domains\wf1-morty\WORKER_PROMPT.md') -Raw

# === CONTRAT TICKET (wargame 26 cat.2 #7) ============================================
# Validation OPERATIONAL du prompt (pas wargame - les wargames sont valides par le feeder #4)
$formatErrors = @()
if ($prompt -notmatch '(?i)\bSTART\b') { $formatErrors += "START heartbeat manquant" }
if ($prompt -notmatch '(?im)^##\s+(§1|S[ée]quence)') { $formatErrors += "Section Séquence obligatoire manquante" }
if ($prompt -notmatch '(?i)\bPREUVE\b') { $formatErrors += "Obligation PREUVE manquante (D1 verify-before-assert)" }
if ($prompt -notmatch '(?i)(EMERGENCY|ctx-pressure)') { $formatErrors += "Section EMERGENCY/ctx-pressure manquante" }
if ($formatErrors.Count -gt 0) {
  Write-Host "[worker_launch] CONTRAT PROMPT INVALIDE - $([string]::Join(', ', $formatErrors))"
  Write-Host "[worker_launch] Reject - WORKER_PROMPT.md ne respecte pas le format operational canonique"
  exit 78  # EX_CONFIG : format de prompt invalide
}
Write-Host "[worker_launch] CONTRAT OK - START + Séquence + PREUVE + EMERGENCY presents"
# ====================================================================================

$mcpEmpty = Join-Path $PSScriptRoot 'mcp-empty.json'
& claude -p $prompt --bare --dangerously-skip-permissions --strict-mcp-config --mcp-config $mcpEmpty *> $OutFile
exit $LASTEXITCODE