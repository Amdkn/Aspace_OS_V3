<#
ADR-INFRA-003 - Build the Business OS CEO Dashboard (10_Projects Matryoshka).
Moves the 8 canonical apps to short homes, junctions back into the deep Verse,
creates _doctrine junctions, quarantines the OMK duplicate tree.
Move-first strategy: Move-Item is an O(1) same-volume rename (ignores >260 children);
.next is cleaned AFTER the move, at the short path where it is < 260.
NO builds here (run separately).
#>
$ErrorActionPreference = 'Stop'
$root  = 'C:\Users\amado\ASpace_OS_V2'
$pic   = "$root\20_Life_OS\24_PARA_Enterprise\01_Projects_Picard"
$grid  = "$root\30_Business_OS\10_Projects"
$pf    = 'B2_Business_Domains\03_Product_Flash_Avengers'
New-Item -ItemType Directory -Path $grid -Force | Out-Null

function Clean-Next($repo) {
  $n = Join-Path $repo '.next'
  if (Test-Path $n) {
    try { Remove-Item -Recurse -Force $n -ErrorAction Stop }
    catch {
      $e = Join-Path $env:TEMP "empty_$(Get-Random)"; New-Item -ItemType Directory $e | Out-Null
      robocopy $e $n /MIR /R:0 /W:0 /NFL /NDL /NP | Out-Null
      Remove-Item -Recurse -Force $n -ErrorAction SilentlyContinue; Remove-Item -Recurse -Force $e
    }
  }
}

# Migrate one app: source deep repo -> short home; junction-back at the deep location.
function Migrate($srcDeep, $shortHome, $junctionAtDeep) {
  if (Test-Path $shortHome) { Write-Host "  SKIP (home exists): $shortHome"; return }
  if (-not (Test-Path $srcDeep)) { Write-Host "  MISSING source: $srcDeep"; return }
  New-Item -ItemType Directory -Path (Split-Path $shortHome) -Force | Out-Null
  Move-Item -LiteralPath $srcDeep -Destination $shortHome      # atomic same-volume rename
  Clean-Next $shortHome
  if ($junctionAtDeep) {
    if (Test-Path $srcDeep) { (Get-Item $srcDeep).Delete() }   # remove leftover if any
    New-Item -ItemType Junction -Path $srcDeep -Target $shortHome | Out-Null
  }
  Write-Host "  OK -> $shortHome"
}

function Doctrine($proj, $verseName) {
  $p = "$grid\$proj"; New-Item -ItemType Directory -Path $p -Force | Out-Null
  $j = "$p\_doctrine"; $t = "$pic\$verseName"
  if ((Test-Path $j) -or -not (Test-Path $t)) { return }
  New-Item -ItemType Junction -Path $j -Target $t | Out-Null
  Write-Host "  _doctrine -> $verseName"
}

Write-Host "== SOLARIS =="
Doctrine 'solaris' '00 Agency as a Service'
# landing: re-home the already-moved 30_Business_OS\solaris-aaas; fix its deep junction
$solDeepLeaf = "$pic\00 Agency as a Service\$pf\01_solaris-aaas"
$solOldHome  = "$root\30_Business_OS\solaris-aaas"
$solNewHome  = "$grid\solaris\apps\landing"
if (Test-Path $solOldHome) {
  if ((Test-Path $solDeepLeaf) -and (Get-Item $solDeepLeaf).LinkType -eq 'Junction') { (Get-Item $solDeepLeaf).Delete() }
  New-Item -ItemType Directory -Path (Split-Path $solNewHome) -Force | Out-Null
  Move-Item -LiteralPath $solOldHome -Destination $solNewHome
  Clean-Next $solNewHome
  New-Item -ItemType Junction -Path $solDeepLeaf -Target $solNewHome | Out-Null
  Write-Host "  re-homed solaris landing -> $solNewHome"
}
Migrate "$pic\00 Agency as a Service\$pf\02_aaas-os" "$grid\solaris\apps\dashboard" "$pic\00 Agency as a Service\$pf\02_aaas-os"

Write-Host "== OMK (canon = 01-omk-business-os) =="
Doctrine 'omk' '01-omk-business-os'
Migrate "$pic\01-omk-business-os\$pf\01-omk-services-front-end"   "$grid\omk\apps\landing"   "$pic\01-omk-business-os\$pf\01-omk-services-front-end"
Migrate "$pic\01-omk-business-os\$pf\02-omk-services-business-os" "$grid\omk\apps\dashboard" "$pic\01-omk-business-os\$pf\02-omk-services-business-os"

Write-Host "== ABC (doctrine only) =="
Doctrine 'abc' '02 ABC OS & Child Care BOS'

Write-Host "== RILCOT =="
Doctrine 'rilcot' '03_RILCOT_Members_Space_OS'
# retire the earlier reserved flat home + its _app junction
$rilReserved = "$root\30_Business_OS\rilcot-members"
$rilAppJ     = "$pic\03_RILCOT_Members_Space_OS\_app"
if ((Test-Path $rilAppJ) -and (Get-Item $rilAppJ).LinkType -eq 'Junction') { (Get-Item $rilAppJ).Delete() }
if (Test-Path $rilReserved) { Remove-Item -Recurse -Force $rilReserved }
Migrate "$pic\03_RILCOT_Members_Space_OS\$pf\01-rilcot-members-v2" "$grid\rilcot\apps\members" "$pic\03_RILCOT_Members_Space_OS\$pf\01-rilcot-members-v2"

Write-Host "== ALIKALY (both apps) =="
Doctrine 'alikaly' '04 Alikaly Bana Holding to LLC'
Migrate "$pic\04 Alikaly Bana Holding to LLC\$pf\01 alykaly-holding-front-v2" "$grid\alikaly\apps\holding" "$pic\04 Alikaly Bana Holding to LLC\$pf\01 alykaly-holding-front-v2"
Migrate "$pic\04 Alikaly Bana Holding to LLC\$pf\02_alykaly-os-v2"            "$grid\alikaly\apps\os"      "$pic\04 Alikaly Bana Holding to LLC\$pf\02_alykaly-os-v2"

Write-Host "== MARINA =="
Doctrine 'marina' '05 marina Cleaning BOS & SOP'
Migrate "$pic\05 marina Cleaning BOS & SOP\$pf\01-marina-cleaning-font-end" "$grid\marina\apps\landing" "$pic\05 marina Cleaning BOS & SOP\$pf\01-marina-cleaning-font-end"

Write-Host "== QUARANTINE OMK duplicate (spaces tree + _Inbox in canon) =="
$trash = "$root\_TRASH\omk-dedup_2026-06-04"
New-Item -ItemType Directory -Path $trash -Force | Out-Null
$omkDupSpaces = "$pic\01 OMK Business OS"
$omkInbox     = "$pic\01-omk-business-os\_Inbox"
if (Test-Path $omkDupSpaces) { Move-Item -LiteralPath $omkDupSpaces -Destination "$trash\01 OMK Business OS"; Write-Host "  quarantined spaces dup" }
if (Test-Path $omkInbox)     { Move-Item -LiteralPath $omkInbox     -Destination "$trash\_Inbox";            Write-Host "  quarantined _Inbox" }

Write-Host "`nDONE - structure + migrations + junctions + quarantine complete."
