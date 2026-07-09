# add_boot_triggers.ps1 - Doctrine Paperclip Utile: la flotte se relance seule 5-10 min apres boot.
# Idempotent: n'ajoute un LogonTrigger(delay) que s'il manque. Ne touche jamais les triggers existants.
$plan = @(
  @{ Task='AspaceWF1Runner';       Delay='PT5M' },
  @{ Task='AspaceLoopHeartbeat';   Delay='PT6M' },
  @{ Task='AspaceLoopBook';        Delay='PT7M' },
  @{ Task='AspaceLoopWF3Sim';      Delay='PT8M' },
  @{ Task='AspaceLoopZoraNuit';    Delay='PT9M' },
  @{ Task='CitadelleBookLoopEng';  Delay='PT10M' }
)
foreach ($p in $plan) {
  $t = Get-ScheduledTask -TaskName $p.Task -ErrorAction SilentlyContinue
  if (-not $t) { Write-Output "SKIP $($p.Task): introuvable"; continue }
  $hasDelayedLogon = $t.Triggers | Where-Object { $_.CimClass.CimClassName -eq 'MSFT_TaskLogonTrigger' -and $_.Delay }
  if ($hasDelayedLogon) { Write-Output "OK   $($p.Task): logon+delay deja present ($($hasDelayedLogon.Delay))"; continue }
  $newTrig = New-ScheduledTaskTrigger -AtLogOn -User "$env:USERDOMAIN\$env:USERNAME"
  $newTrig.Delay = $p.Delay
  # preserve les triggers existants NON-logon (les TimeTrigger de repetition restent)
  $keep = @($t.Triggers | Where-Object { $_.CimClass.CimClassName -ne 'MSFT_TaskLogonTrigger' })
  $all = $keep + $newTrig
  try {
    Set-ScheduledTask -TaskName $p.Task -Trigger $all | Out-Null
    Write-Output "SET  $($p.Task): LogonTrigger delay=$($p.Delay) ajoute ($($keep.Count) trigger(s) preserve(s))"
  } catch { Write-Output "FAIL $($p.Task): $($_.Exception.Message)" }
}
