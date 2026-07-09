# temporal-state.ps1 - WARGAME 27 M3 (fork : Pane instable -> source affichable)
# L'AFFICHAGE de la coherence temporelle : TEMPORAL-CANON + STATE.json + compte reel.
# Utilisable par (a) un pane Pane "TEMPS" quand Pane est stable, OU (b) worklog nightly.
# La coherence cesse d'etre une relecture : elle est un OUTPUT.
#
# Usage : .\temporal-state.ps1          (affiche a l'ecran, cockpit)
#         .\temporal-state.ps1 -Worklog (fork : append 1 ligne worklog nightly)

param([switch]$Worklog)
$ErrorActionPreference = 'Continue'
$Bank = $PSScriptRoot
$Citadel = 'C:\Users\amado\agent-os\citadel'

# Source 1 : compte reel de la banque (jamais "close", graduee)
$count = (Get-ChildItem (Join-Path $Bank 'wargames') -Filter '*.md').Count

# Source 2 : STATE.json (go_until, capacity)
$statePath = Join-Path $Citadel 'loops\STATE.json'
$goUntil = 'n/a'; $capacity = 'n/a'
if (Test-Path $statePath) {
  try {
    $st = Get-Content $statePath -Raw | ConvertFrom-Json
    $goUntil = if ($st.go_until_source) { $st.go_until_source } else { '2029-07-05 (wf0-spock)' }
    $capacity = if ($st.capacity_verdict) { $st.capacity_verdict } else { "green=$($st.capacity_green)" }
  } catch {}
}

# Source 3 : TEMPORAL-CANON existe + taille
$canonPath = Join-Path $Bank 'TEMPORAL-CANON.md'
$canonLines = if (Test-Path $canonPath) { (Get-Content $canonPath).Count } else { 0 }

if ($Worklog) {
  $iso = (Get-Date).ToString('yyyy-MM-ddTHH:mm:sszzz')
  $line = "- [$iso] [temporal-state] banque=$count fichiers (graduee, jamais close) :: GO=triennal 2029-07-05 :: CAP=x4 :: capacity=$capacity :: CANON=$canonLines lignes :: preuve=TEMPORAL-CANON.md + STATE.json"
  Add-Content -LiteralPath (Join-Path $Citadel 'loops\logs\worklog.md') -Value $line -Encoding UTF8
  Write-Host "[temporal-state] worklog line appended"
} else {
  Write-Host "======================================================"
  Write-Host " COCKPIT TEMPS - coherence temporelle de la banque"
  Write-Host "======================================================"
  Write-Host " Banque    : $count wargames (graduee par W13, JAMAIS close)"
  Write-Host " GO        : triennal 2026-07-05 -> 2029-07-05 renouvelable"
  Write-Host " Compression: CAP x4 (x8 = plafond theorique, RISQUE wg08)"
  Write-Host " Cadence   : CADENCE_12WY (1 sem L1 = 1 jour L2)"
  Write-Host " Capacity  : $capacity (Beth-airlock, GREEN>6GB free)"
  Write-Host " CANON     : $canonLines lignes (source unique, cite par les rails)"
  Write-Host "------------------------------------------------------"
  Write-Host " Regle : le CANON gagne sur toute prose fossile datee."
  Write-Host "======================================================"
}