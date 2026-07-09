# Hooks System

## Hook Types

- **PreToolUse**: Before tool execution (validation, parameter modification)
- **PostToolUse**: After tool execution (auto-format, checks)
- **Stop**: When session ends (final verification)

## Auto-Accept Permissions

Use with caution:
- Enable for trusted, well-defined plans
- Disable for exploratory work
- Never use dangerously-skip-permissions flag
- Configure `allowedTools` in `~/.claude.json` instead

## TodoWrite Best Practices

Use TodoWrite tool to:
- Track progress on multi-step tasks
- Verify understanding of instructions
- Enable real-time steering
- Show granular implementation steps

Todo list reveals:
- Out of order steps
- Missing items
- Extra unnecessary items
- Wrong granularity
- Misinterpreted requirements

## Stop Hook TTS Pattern (SAPI Hortense)

For users who can't read walls of text, configure a **Stop hook** that auto-speaks the last assistant message via Windows SAPI:

**Script** (e.g., `C:\Users\amado\AppData\Local\Temp\symphony_tts_stop.ps1`):
```powershell
$ttsFile = 'C:\Users\amado\AppData\Local\Temp\last_tts.txt'
$fallback = 'Session terminée. Vérifiez le terminal.'
if (Test-Path $ttsFile) { $text = Get-Content $ttsFile -Raw -Encoding UTF8 }
if ([string]::IsNullOrWhiteSpace($text)) { $text = $fallback }
Add-Type -AssemblyName System.Speech
$s = New-Object System.Speech.Synthesis.SpeechSynthesizer
$s.SelectVoice('Microsoft Hortense Desktop')  # fr-FR
$s.Speak($text) | Out-Null
```

**Hook** in `~/.claude/settings.json`:
```json
"Stop": [{
  "hooks": [
    {"type": "command", "command": "[System.Media.SystemSounds]::Asterisk.Play()", "async": true},
    {"type": "command", "command": "powershell -NoProfile -ExecutionPolicy Bypass -File C:\\Users\\amado\\AppData\\Local\\Temp\\symphony_tts_stop.ps1", "async": true}
  ]
}]
```

**Do NOT use** the `clara-voice` MCP for TTS — it sends audio to a sink the user cannot hear. SAPI direct to the default Windows audio device works. Voice: `Microsoft Hortense Desktop` (fr-FR). See `fable-autor-research-loop-symphony-agentos.md` for full doctrine.
