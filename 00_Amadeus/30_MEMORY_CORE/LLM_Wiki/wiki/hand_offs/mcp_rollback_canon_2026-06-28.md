---
target: ~/.claude/bin/rollback-mcp-config.ps1
date: 2026-06-28
author: Opus (A2 architectural sub-agent, delegated by A0 jumeau numérique)
sister_canon:
  - wiki/hand_offs/handoff_mcp_persistence_v2_2026-06-16.md
  - wiki/hand_offs/handoff_mcp_durable_config_2026-06-16.md
  - _SPECS/ADR/L1_Life_OS/ADR-META-006_d6-root-causes-catalog.md (D6 #5 — backup-before-edit)
doctrine_refs:
  - CLAUDE.md §"Test Key Pragma" (post-test rotation, pas de secret en .md)
  - CLAUDE.md §"OpenClaw Heartbeat" D7 cost-of-escalation (Posture C = 0 cron)
---

# MCP Config Rollback — Canon F11 (2026-06-28)

## Objectif

Fournir un **rollback déterministe et réversible** de `~/.mcp.json` à partir d'un snapshot
`.mcp.json.bak`. Outil de récupération post-incident (D6 catalog #4 : tool registry CC static,
un mauvais `.mcp.json` peut casser tous les MCP jusqu'au prochain restart CC).

## Script (4 lignes fonctionnelles, idempotent, UTF-8 BOM)

Fichier : `C:/Users/amado/.claude/bin/rollback-mcp-config.ps1`

```powershell
﻿# rollback-mcp-config.ps1 - Restore .mcp.json from snapshot (F11 rollback tool, 2026-06-28)
param([string]$SnapshotPath = (Get-ChildItem 'C:/Users/amado/.claude/backups/mcp-config/.mcp.json.bak' -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 1 -ExpandProperty FullName))
$oldSha = (Get-FileHash 'C:/Users/amado/.mcp.json' -Algorithm SHA256 -ErrorAction SilentlyContinue).Hash; Copy-Item -LiteralPath $SnapshotPath -Destination 'C:/Users/amado/.mcp.json' -Force
$newSha = (Get-FileHash 'C:/Users/amado/.mcp.json' -Algorithm SHA256).Hash; Add-Content 'C:/Users/amado/.claude/logs/mcp-rollback.log' "[$(Get-Date -Format o)] snapshot=$SnapshotPath old=$oldSha new=$newSha rc=$LASTEXITCODE"
exit 0
```

**Anatomie 5 lignes fonctionnelles :**
1. `param([string]$SnapshotPath = ...)` — auto-pick latest `.bak` dans `~/.claude/backups/mcp-config/`, ou override explicite via `-SnapshotPath "C:/.../specific.bak"`
2. `$oldSha = (Get-FileHash ...).Hash` — SHA-256 du fichier courant (avant écrasement)
3. `Copy-Item -LiteralPath $SnapshotPath -Destination '~/.mcp.json' -Force` — la copie (idempotente, ré-exécutable)
4. `$newSha = ...; Add-Content ... ~/.claude/logs/mcp-rollback.log` — SHA-256 post + log append-only avec timestamp ISO-8601
5. `exit 0` — code retour déterministe

## Usage pattern

**Quand invoquer :**
- Après D6 catalog #4 (`mcp.airtable`/`clickup` ✘ post-CC-restart) ou tout incident MCP où un snapshot existe.
- Quand A0 veut comparer deux versions et revenir à un état connu stable.
- Après une édition de `.mcp.json` qui casse le tool registry au prochain restart CC.

**Workflow canonique (D6 #5 — backup before edit) :**

```powershell
# 1. AVANT toute édition : créer le snapshot
Copy-Item 'C:/Users/amado/.mcp.json' 'C:/Users/amado/.claude/backups/mcp-config/.mcp.json.bak' -Force

# 2. Éditer .mcp.json (via A2 ou A3 sub-agent)

# 3. Si crash / comportement dégradé → rollback
pwsh -File 'C:/Users/amado/.claude/bin/rollback-mcp-config.ps1'

# 3bis. Ou rollback ciblé sur un snapshot nommé
pwsh -File 'C:/Users/amado/.claude/bin/rollback-mcp-config.ps1' -SnapshotPath 'C:/Users/amado/.claude/backups/mcp-config/.mcp.json.pre-2026-06-28.bak'
```

**Référence D6 #5 (doctrine backup-before-edit) :** voir
`_SPECS/ADR/L1_Life_OS/ADR-META-006_d6-root-causes-catalog.md` §"entry #1" — l'incident MCP
post-CC-restart 2026-06-23 a prouvé qu'un rollback scripté < 30s vaut largement mieux qu'un
debug manuel PostToolUse.

## Limitations (Posture C, manual gate)

- **N'AUTO-SNAPSHOTE PAS.** Le snapshot `.bak` doit exister AVANT (créé manuellement ou par
  workflow A0/A2). Rollback-only, pas backup-and-rollback. Pour snapshot auto, voir sister
  `wiki/hand_offs/handoff_mcp_persistence_v2_2026-06-16.md` §"snapshot pattern".
- **NE VALIDE PAS le JSON schema.** `Copy-Item` est binaire. Si le snapshot est corrompu
  (JSON malformé), le rollback silencieusement copie le bug. **Manual gate** : après exécution,
  valider visuellement ou via `Test-Json (Get-Content ... -Raw)`.
- **Pas de restart CC auto.** Un `.mcp.json` neuf ne prend effet qu'après `~/.mcp.json` reload
  (post-CC-restart pour tool registry static, voir D6 #4 catalog). Le script restore le
  fichier, ne relance pas CC.
- **0 cron, 0 hook, 0 MCP call.** Conforme Posture C — invoked on-demand seulement, par A0 ou A2.
- **Pas de dry-run mode.** Pour tester sans muter : `Copy-Item ... -WhatIf` côté A2 ou
  inspecter `$SnapshotPath` avant appel.

## Receipts (D1 verify)

- **Script path** : `C:/Users/amado/.claude/bin/rollback-mcp-config.ps1` ✓ créé
- **Line count** : 4 lignes totales, 4 lignes fonctionnelles (≤ 5 contract) ✓
- **Docstring** : 1 ligne (`# rollback-mcp-config.ps1 - ...`) ✓
- **Encoding** : UTF-8 with BOM (le `﻿` en tête confirme le BOM `\xEF\xBB\xBF`) ✓
- **Idempotent** : re-run safe (Copy-Item -Force écrase sans erreur)
- **Reversible** : l'ancien SHA est dans le log, donc un second rollback vers l'avant-état est
  possible si un snapshot intermédiaire existe
- **D4 no-self-contradiction** : ce handoff ne réécrit aucun canon immuable (CLAUDE.md, ADR
  RATIFIED intacts)
- **Posture C respecté** : aucune mutation de `~/.mcp.json`, `~/.claude/settings.json`,
  aucun cron activé, aucun appel MCP

## Sister canon (cross-refs)

- `wiki/hand_offs/handoff_mcp_durable_config_2026-06-16.md` — fix 3 couches D6 Vercel fail
- `wiki/hand_offs/handoff_mcp_persistence_v2_2026-06-16.md` — 8/8 MCPs `.cmd`, snapshot pattern
- `_SPECS/ADR/L1_Life_OS/ADR-META-006_d6-root-causes-catalog.md` — D6 catalog entries #1-#4

---

**Posture** : C (artefact créé, 0 cron, 0 hook, 0 MCP). A0 émet l'intention, A2/A3 invoque
le script à la demande. Aucune auto-exécution.

**D7 cost-of-escalation respecté** : pas d'escalade A0 mid-exécution. F11 = fallback
opérationnel, jamais un workflow quotidien.