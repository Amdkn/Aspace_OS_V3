---
source: Claude Code (Opus 4.7) / 3-Turn Air Lock + Docs Dogmatique
date: 2026-05-16
type: provider-configuration
domain: L2_Business_OS / Shadow_Stack
tags: [#ShadowL2 #MCP #Notion #ClickUp #Airtable #DocsDogmatique #placeholder-config]
status: pending-keys
related:
  - C:\Users\amado\.claude.json
  - 00_Amadeus\30_MEMORY_CORE\Hermes Agent\README.md (Doctrine Docs Dogmatique)
---

# Shadow L2 — MCP Configuration (Notion / ClickUp / Airtable) — 2026-05-16

## Intent

Configurer les 3 MCP servers de la **Stack Shadow L2** (Business OS), conformément à SDD-009 §Shadow-Stack :

- **Notion** — knowledge base / docs business
- **ClickUp** — task/project management transversal
- **Airtable** — bases relationnelles SOA01-08

## État avant intervention

| Service | État | Mécanisme |
|---|---|---|
| Airtable | ✅ Déjà chargé (UUID `4ff1230b-e0c5-4213-bd4c-3ceec6487209`) | Claude Desktop connector registry (UI) |
| ClickUp | ✅ Enregistré (tools `createTask`, `searchTasks`...) | Claude Desktop connector registry (UI) |
| Notion | ❌ Absent | — |

**Constat** : Claude Desktop UI a déjà 2/3, mais sans contrôle versionnable.

## Décision

Ajouter les **3 entries en `.claude.json` global** comme **couche souveraine fichier** :

- Pilotable par Git / ADR
- Survit aux mises à jour Claude Desktop
- Permet duplication contrôlée avec connectors Desktop (à arbitrer plus tard)

Scope choisi par A0 : **Global** (.claude.json, pas .mcp.json projet).

## Packages canoniques (vérifiés via Context7)

| Service | Library ID Context7 | Package / URL | Source |
|---|---|---|---|
| Notion | `/websites/developers_notion_guides_mcp` | `mcp-remote` bridge → `https://mcp.notion.com/mcp` | Notion HQ officiel |
| ClickUp | `/taazkareem/clickup-mcp-server` | `@taazkareem/clickup-mcp-server@latest` | High reputation, 161 snippets |
| Airtable | (npm direct) | `airtable-mcp-server` (domdomegg) | Référence communauté |

## Configuration écrite dans `.claude.json`

```json
"notion": {
  "command": "npx",
  "args": ["-y", "mcp-remote", "https://mcp.notion.com/mcp"]
},
"clickup": {
  "command": "npx",
  "args": ["-y", "@taazkareem/clickup-mcp-server@latest"],
  "env": {
    "CLICKUP_API_KEY": "${CLICKUP_API_KEY}",
    "CLICKUP_TEAM_ID": "${CLICKUP_TEAM_ID}",
    "DOCUMENT_SUPPORT": "true"
  }
},
"airtable": {
  "command": "npx",
  "args": ["-y", "airtable-mcp-server"],
  "env": {
    "AIRTABLE_API_KEY": "${AIRTABLE_API_KEY}"
  }
}
```

Backup créé : `C:\Users\amado\.claude.json.bak.20260516_shadowL2`

## ⚠️ Limitation Claude Code — Expansion `${VAR}`

Claude Code **ne fait pas** d'expansion shell automatique sur les valeurs `env` de `mcpServers`. Les `${CLICKUP_API_KEY}` etc. sont passées **littéralement** au sous-process npx.

Trois options pour activer :

### Option A — Variables d'environnement Windows utilisateur (recommandé)

```powershell
[Environment]::SetEnvironmentVariable("CLICKUP_API_KEY", "pk_xxx", "User")
[Environment]::SetEnvironmentVariable("CLICKUP_TEAM_ID", "12345678", "User")
[Environment]::SetEnvironmentVariable("AIRTABLE_API_KEY", "patXXX.YYY", "User")
```

Puis remplacer dans `.claude.json` les `${VAR}` par les vraies valeurs OU laisser Claude Code passer la variable d'environnement (à confirmer empiriquement par redémarrage Claude Code après set User env vars).

### Option B — Hard-code dans `.claude.json` (rapide mais expose si dump)

Remplacer les `${VAR}` par les vraies valeurs. Risque : leak si fichier partagé/dump.

### Option C — Script masqué (style Hermes MiniMax)

À écrire : `C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\Shadow_L2\scripts\Set-ShadowL2-Keys.ps1`

- Prompt SecureString pour les 3 tokens
- Écrit en Windows User env vars
- Patch `.claude.json` pour remplacer `${VAR}` par valeurs OU laisser tel quel

**Notion** : pas de clé requise — OAuth in-browser au premier appel (`mcp-remote` ouvre une page Notion login).

## Cohabitation avec Claude Desktop Connectors

Airtable et ClickUp existent **en double** :

- Claude Desktop registry → tools préfixe `mcp__4ff1230b-...` (Airtable)
- `.claude.json` → tools préfixe `mcp__airtable__*` (à venir après redémarrage)

**Risque** : confusion + double appel API.

**Recommandation future** : désactiver les deux connectors Desktop (Settings → Connectors → Airtable/ClickUp → off) pour ne garder que la version fichier.

## Vérification

Après redémarrage Claude Code :

```bash
# Dans Claude Code (PowerShell)
claude mcp list   # Doit afficher notion, clickup, airtable
```

Ou directement :

```powershell
node -e "console.log(Object.keys(require('C:/Users/amado/.claude.json').mcpServers))"
```

## Sources

- Notion MCP docs : `https://developers.notion.com/guides/mcp/get-started-with-mcp`
- ClickUp MCP : `https://github.com/taazkareem/clickup-mcp-server`
- Airtable MCP : `https://github.com/domdomegg/airtable-mcp-server`
- Context7 query session : 2026-05-16 (libraryIds résolus)

## Doctrine appliquée

> **Docs Dogmatique** (Hermes Agent README §1) — Aucune config MCP n'a été inventée. Les 3 packages ont été résolus + vérifiés via Context7 avant écriture. Backup `.claude.json` créé avant edit.

## Next Steps

1. ⚠️ Choisir option clé (A/B/C ci-dessus)
2. Redémarrer Claude Code → tester `notion`, `clickup`, `airtable` tools
3. Si OK → désactiver connectors Desktop dupliqués (Airtable, ClickUp)
4. Créer `ADR-SHADOW-L2-001_mcp-stack-souveraine.md` formalisant le pattern fichier > Desktop UI
