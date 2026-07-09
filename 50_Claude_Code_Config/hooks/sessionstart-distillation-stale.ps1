# sessionstart-distillation-stale.ps1
# Anti-obsolescence forcing function (L1 -> L2 layer). A0 creates guides almost
# daily but distils them into PRINCIPLES doctrines rarely -> the arms-race
# obsolescence. This hook compares, per Business domain, how many guides are
# NEWER than the domain's PRINCIPLES doctrine, and surfaces the stale ones every
# session so the distillation backlog can never grow silently.
# Computed LIVE from filesystem mtimes (no ledger to itself go stale).
# ASCII-only (PowerShell breaks on em-dash - CLAUDE.md guardrail).

$ErrorActionPreference = 'SilentlyContinue'
$G = "C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\03_Resources_Geordi\01_Guides"
$B = "C:\Users\amado\ASpace_OS_V2\20_Life_OS\24_PARA_Enterprise\02_Areas_Spock\J01_Jerry_Prime_LD01_Business\B2_Area_Domains"

# guide-folder -> principles-folder
$MAP = [ordered]@{
  "01_Product" = "03_Product_Flash_Avengers"
  "02_Ops"     = "04_Ops_Batman_Fantastic4"
  "03_IT"      = "05_IT_Cyborg_KangDynasty"
  "04_Finance" = "06_Finance_WonderWoman_Thunderbolts"
  "05_Legal"   = "08_Legal_Aquaman_Eternals"
  "06_Sales"   = "02_Sales_MartianManhunter_Illuminati"
  "07_Growth"  = "01_Growth_Superman_Guardians"
  "08_People"  = "07_People_GreenLantern_XMen"
}

$stale = @()
foreach ($gd in $MAP.Keys) {
  $pf = Get-ChildItem "$B\$($MAP[$gd])\03_*_PRINCIPLES.md" -ErrorAction SilentlyContinue | Select-Object -First 1
  if (-not $pf) { continue }
  $pt = $pf.LastWriteTime
  $newer = @(Get-ChildItem "$G\$gd\*.md" -ErrorAction SilentlyContinue | Where-Object { $_.LastWriteTime -gt $pt })
  if ($newer.Count -ge 3) {
    $stale += [pscustomobject]@{ dom = $gd; n = $newer.Count; age = $pt.ToString('yyyy-MM-dd') }
  }
}

if ($stale.Count -eq 0) {
  Write-Output "## Distillation: all domain PRINCIPLES current (<3 guides newer each)."
  exit 0
}

$stale = $stale | Sort-Object n -Descending
$tot = ($stale | Measure-Object n -Sum).Sum
Write-Output "## OBSOLESCENCE ALERT - $($stale.Count) domain(s), ~$tot guides distilled-but-not-redistilled (L1->L2 backlog)"
foreach ($s in $stale) { Write-Output ("  " + $s.dom + ": " + $s.n + " new guides since principles " + $s.age) }
Write-Output "Re-distill via /area-domain-doctrine-distill (highest backlog first), then re-apply via _LESSONS_APPLIED.md loop."
exit 0
