$ErrorActionPreference = 'Stop'

$runtimeRoot = Split-Path -Parent $PSScriptRoot
$memoryCore = Split-Path -Parent $runtimeRoot
$source = Join-Path $memoryCore 'LLM_Wiki\wiki'
$target = Join-Path $runtimeRoot 'import\llm-wiki'

if (-not (Test-Path -LiteralPath $source)) {
  throw "LLM Wiki source not found: $source"
}

New-Item -ItemType Directory -Force -Path $target | Out-Null

$excludeDirs = @('.git', 'node_modules', '_daily', '_manual')
$excludeFiles = @('.DS_Store', 'Thumbs.db')

Get-ChildItem -LiteralPath $target -Force | Remove-Item -Recurse -Force

Get-ChildItem -LiteralPath $source -Recurse -Force | ForEach-Object {
  $relative = $_.FullName.Substring($source.Length).TrimStart('\', '/')
  if (-not $relative) { return }

  $parts = $relative -split '[\\/]'
  if ($parts | Where-Object { $excludeDirs -contains $_ }) { return }
  if (-not $_.PSIsContainer -and ($excludeFiles -contains $_.Name)) { return }

  $destination = Join-Path $target $relative
  if ($_.PSIsContainer) {
    New-Item -ItemType Directory -Force -Path $destination | Out-Null
  } else {
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $destination) | Out-Null
    Copy-Item -LiteralPath $_.FullName -Destination $destination -Force
  }
}

$home = Join-Path $target 'home.md'
@'
---
title: A'Space LLM Wiki
description: Surface Wiki.js locale pour naviguer la memoire Markdown A'Space OS V2.
published: true
---

# A'Space LLM Wiki

Cette instance Wiki.js est une surface locale de navigation.

La source de verite reste le Markdown dans:

`C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\LLM_Wiki\wiki`

## Entrées principales

- [Index](index)
- [Log](log)
- [Concepts](concepts)
- [Entities](entities)
- [Sources](sources)
- [Agent Capsules](agent_capsules)
- [Hand Offs](hand_offs)

## Regle

Les changements systemiques durables doivent rester documentes dans Memory Core et LLM Wiki Markdown.
Wiki.js sert d'interface de lecture, d'audit et de navigation.
'@ | Set-Content -LiteralPath $home -Encoding UTF8

$mdCount = (Get-ChildItem -LiteralPath $target -Recurse -Filter '*.md' -File).Count
"Prepared Wiki.js import staging: $target"
"Markdown files: $mdCount"
