# stop-log-append.ps1
# Per-response auto-journal into canon wiki/log.md (D4 append-only).
# Writes ONE compact line per turn. Reads the last assistant text from the
# transcript the Stop hook passes on stdin (transcript_path), so it is reliable
# even when last_tts.txt is stale. NEVER explodes context: it WRITES one line; the
# read side (sessionstart-log-digest.ps1) only ever tails + filters.

$ErrorActionPreference = 'SilentlyContinue'
# Isolated per-turn journal (NOT the curated canon wiki/log.md). Keeps the canon
# clean for deliberate handoffs; this file holds the noisy per-turn auto-trail.
$LOG = "C:\Users\amado\.claude\logs\turn-journal.md"
New-Item -ItemType Directory -Force -Path (Split-Path $LOG) | Out-Null

# --- read Stop hook stdin (JSON: transcript_path, session_id, ...) ---
$raw = [Console]::In.ReadToEnd()
$transcript = $null
if (-not [string]::IsNullOrWhiteSpace($raw)) {
  try { $transcript = ($raw | ConvertFrom-Json).transcript_path } catch {}
}

# --- extract last assistant text block from the transcript tail ---
$summary = $null
if ($transcript -and (Test-Path $transcript)) {
  $tail = Get-Content $transcript -Tail 60 -Encoding UTF8
  for ($i = $tail.Count - 1; $i -ge 0; $i--) {
    try { $obj = $tail[$i] | ConvertFrom-Json } catch { continue }
    if ($obj.type -ne 'assistant') { continue }
    $content = $obj.message.content
    if (-not $content) { continue }
    foreach ($b in $content) {
      if ($b.type -eq 'text' -and $b.text) { $summary = $b.text; break }
    }
    if ($summary) { break }
  }
}

# fallback: stale last_tts.txt, then a bare marker
if (-not $summary) {
  $tts = "C:\Users\amado\AppData\Local\Temp\last_tts.txt"
  if (Test-Path $tts) { $summary = (Get-Content $tts -Raw -Encoding UTF8) }
}
if ([string]::IsNullOrWhiteSpace($summary)) { $summary = '(no text response captured)' }

# --- compact to one line: strip newlines, cap 200 chars ---
$summary = ($summary -replace '\s+', ' ').Trim()
if ($summary.Length -gt 200) { $summary = $summary.Substring(0,200) + '...' }

$ts = Get-Date -Format 'yyyy-MM-ddTHH:mm:sszzz'
Add-Content -Path $LOG -Value "[$ts] [auto-turn] $summary" -Encoding UTF8
exit 0
