# sessionstart-load-disposition.ps1
# Charge ~/.hermes/disposition.md + _DISCIPLINE_BASELINES.md a chaque SessionStart.
# Idempotent. Bounded reads (Get-Content -Tail). ASCII-only (Powershell em-dash guard).
# POSTURE C: hook present but settings.json wiring PENDING A0 GO.

$ErrorActionPreference = 'SilentlyContinue'
$DISP  = 'C:\Users\amado\.hermes\disposition.md'
$BASE  = 'C:\Users\amado\.hermes\_ssot_claude\mindsets\_DISCIPLINE_BASELINES.md'

if (-not (Test-Path $DISP)) { Write-Output '[disposition] SKIP | missing=disposition.md'; exit 0 }
if (-not (Test-Path $BASE)) { Write-Output '[disposition] SKIP | missing=_DISCIPLINE_BASELINES.md'; exit 0 }

# bounded tail-read (200 / 100 lines per spec)
$dSections = (Get-Content $DISP -Tail 200 -Encoding UTF8 | Select-String -Pattern '^## ').Count
# dormant mindsets = count of Mindset files tagged dormant in canonical mindsets/ (truthful signal)
$mDir = 'C:\Users\amado\.hermes\_ssot_claude\mindsets'
$dDormant = 0
if (Test-Path $mDir) {
  $dDormant = @(Get-ChildItem $mDir -Filter '*Mindset*.md' | Where-Object { $_.Name -match 'Telegram|DesktopCommander' }).Count
}
$cutoff    = (Get-Item $DISP).LastWriteTime.ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ')

Write-Output "[disposition] Loaded | sections=$dSections | mindsets_dormant=$dDormant | cutoff=$cutoff"
exit 0
