$ErrorActionPreference='Stop'
$src='C:\Users\amado\ASpace_OS_V2\30_Business_OS\00_Jerry_Business_Pulse\04_Business_Domains'
$grid='C:\Users\amado\ASpace_OS_V2\30_Business_OS\10_Projects'
$projects = @{
 'solaris'='Solaris AaaS (00 Agency as a Service)';
 'omk'='OMK Business OS';
 'abc'='ABC OS & Child Care';
 'rilcot'='RILCOT Members Space';
 'alikaly'='Alikaly Bana Holding';
 'marina'='Marina Cleaning'
}
# source domains (0N_*) + their member subfolders
$domains = Get-ChildItem $src -Directory | Where-Object { $_.Name -match '^0[1-8]_' } | Sort-Object Name
$totMembers=0; $totCreated=0
foreach($proj in $projects.Keys | Sort-Object){
  $projDisplay=$projects[$proj]
  $b3 = Join-Path $grid "$proj\_doctrine\B3_Warp_Core_Execution"
  if(-not (Test-Path $b3)){ Write-Host ("SKIP "+$proj+" (no B3_Warp_Core_Execution)"); continue }
  $created=0
  foreach($dom in $domains){
    $domName=$dom.Name
    $tgtDom = Join-Path $b3 $domName
    New-Item -ItemType Directory -Path $tgtDom -Force | Out-Null
    foreach($mem in (Get-ChildItem $dom.FullName -Directory | Where-Object { $_.Name -match '^[0-9][0-9]_' })){
      $tgtMem = Join-Path $tgtDom $mem.Name
      if(Test-Path $tgtMem){ continue }
      New-Item -ItemType Directory -Path $tgtMem | Out-Null
      $parts = $mem.Name -split '_',3
      $member = if($parts.Count -ge 2){$parts[1]}else{$mem.Name}
      $role = if($parts.Count -ge 3){$parts[2]}else{''}
      $readme = @"
# $member ($role) - $projDisplay / $domName (B3 execution workspace)

- **Project** : $projDisplay
- **Squad member** : $member  |  **Role** : $role
- **Canon role (Notion AGENT_REGISTRY_DB)** : voir 00_Jerry_Business_Pulse\04_Business_Domains\$domName\$($mem.Name)\README.md
- **Area doctrine (B2/why)** : J01 Jerry Prime. **Cross-project doctrine** : 00_Jerry_Business_Pulse.
- **Cette fiche** : workspace d'execution B3 de ce membre POUR ce projet (JTBD, proofs, handoffs specifiques projet).

*Replicated from Jerry Business Pulse squads - ADR-INFRA-003. 2026-06-05.*
"@
      Set-Content -Path (Join-Path $tgtMem 'README.md') -Value $readme -Encoding UTF8
      $created++
    }
  }
  $totCreated+=$created
  Write-Host ("OK "+$proj+" : +"+$created+" dossiers membres")
}
Write-Host ("TOTAL membres crees: "+$totCreated)
