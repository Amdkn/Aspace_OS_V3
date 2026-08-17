---
type: Integration
title: Composio comme gateway MCP Cloud (For You)
description: Branchement direct à l'endpoint MCP public de Composio via ~/.mcp.json, sans transiter par l'agentgateway local.
resource: https://connect.composio.dev/mcp
tags: [composio, mcp, cloud-gateway, for-you]
generated: { by: human:amdkn, at: 2026-08-17T03:55:00Z }
verified:
  - { by: process:test-key-pragma, at: 2026-08-17T03:55:00Z }
sources:
  - id: composio-skill
    resource: "~/.agents/skills/composio/SKILL.md"
    title: Skill ComposioHQ/composio (symlink Claude Code)
    author: ComposioHQ
    last_modified: 2026-08-17
  - id: composio-foryou
    resource: ~/.agents/skills/composio/references/for-you.md
    title: Reference For You — endpoint, header, produits concernes
    author: ComposioHQ
    last_modified: 2026-08-17
  - id: live-mcp-call
    resource: POST https://connect.composio.dev/mcp — tools/list
    title: Test Key Pragma (HTTP 200, 8 outils rendus)
    author: process:claude-code
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Composio comme gateway MCP Cloud

## Contexte et decision

L'utilisateur veut un gateway MCP stable pour ses apps cloud (Gmail, Slack,
GitHub, Notion, Calendar, Linear, Figma, web search, etc.) sans dependre de
l'agentgateway local, fragile : « des qu'un seul MCP ne fonctionne pas ».

Trois options evaluees, une choisie :

| Option | Pourquoi non |
|---|---|
| Brancher dans `mcp_sources.json` (agentgateway) | refuse par l'utilisateur — la fragilite du gateway est un risque inacceptable pour sa cle cloud |
| Brancher en `Platform` (cle `ak_*`, sessions SDK) | refuse par la doc — Platform n'a PAS d'endpoint MCP statique, MCP est session-scope via SDK. Le bon cas d'usage de Platform est une app multi-tenant, pas l'assistant personnel |
| **Brancher en `For You` (cle `ck_*`, endpoint public)** | **choisi** : endpoint MCP public `https://connect.composio.dev/mcp`, header `x-consumer-api-key`, configuration triviale dans `~/.mcp.json` |

## Cablage effectif

### 1. Cle dans `~/.claude/settings.json` (gitignore)

```json
"env": {
  "COMPOSIO_CONSUMER_KEY": "ck_…"
}
```

La cle n'apparait dans aucun autre fichier. Aucun `.env` versionne, aucun
commit, aucun brief. Elle est lue par reference au demarrage de CC.

### 2. Entree dans `~/.mcp.json` (racine, pas agentgateway)

```json
"composio": {
  "type": "http",
  "url": "https://connect.composio.dev/mcp",
  "headers": {
    "x-consumer-api-key": "${COMPOSIO_CONSUMER_KEY}"
  }
}
```

Le `${…}` est resolu par CC au demarrage — la valeur ne transite jamais par
un fichier visible.

### 3. Verification — Test Key Pragma

Appel direct a l'endpoint, header `x-consumer-api-key`, methode
`tools/list` (MCP standard) :

- **HTTP 200**
- 8 outils exposes par le gateway For You (decrits ci-dessous)

## Outils disponibles immediatement

Le gateway expose 8 outils meta. Les 250+ outils d'apps (Gmail, Slack,
GitHub, Notion, etc.) sont accessibles indirectement :

| Outil meta | Role |
|---|---|
| `COMPOSIO_SEARCH_TOOLS` | Decouvre les outils d'une app a partir d'un cas d'usage |
| `COMPOSIO_GET_TOOL_SCHEMAS` | Retourne les schemas d'entree (obligatoire avant execution) |
| `COMPOSIO_MANAGE_CONNECTIONS` | Cree/liste/supprime les connexions OAuth a vos apps |
| `COMPOSIO_WAIT_FOR_CONNECTIONS` | Attend la fin d'un OAuth |
| `COMPOSIO_MULTI_EXECUTE_TOOL` | Execute jusqu'a 50 outils en parallele |
| `COMPOSIO_REMOTE_BASH_TOOL` | Sandbox bash, 180 s max par commande |
| `COMPOSIO_REMOTE_WORKBENCH` | Sandbox Python Jupyter persistant |
| `COMPOSIO_GET_TOOL_SCHEMAS` | (deja liste) |

**Workflow type** : `COMPOSIO_SEARCH_TOOLS` (avec `use_case`) ->
`COMPOSIO_MANAGE_CONNECTIONS` (si necessaire) ->
`COMPOSIO_WAIT_FOR_CONNECTIONS` (apres l'OAuth) ->
`COMPOSIO_GET_TOOL_SCHEMAS` -> `COMPOSIO_MULTI_EXECUTE_TOOL`.

## Limites connues

- **`~/.mcp.json` n'est lu qu'au demarrage** de Claude Code. Toute
  modification necessite un redemarrage. C'est un comportement de la
  plateforme, pas un defaut.
- **Le CLI `composio` installe via npm n'a pas cree de shim Windows**, donc
  `composio` n'est pas dans le PATH. Pas grave tant qu'on utilise la cle
  directement. Si le PATH devient necessaire : `npm link` ou ajout du
  binaire au PATH Windows.
- **L'installateur officiel** (`curl -fsSL https://composio.dev/install | sh`)
  refuse Windows et exige WSL. Le paquet npm est l'alternative qu'on a
  utilisee.

## Anti-pieges

- Ne JAMAIS copier la cle `ck_…` dans une sortie de chat, un brief
  versionne, ou un log. La cle reste dans `settings.json`, et le MCP la
  lit par reference.
- Une confusion classique : `ak_…` est Platform, `ck_…` est For You. Les
  prefixes sont distincts et non interchangeables. L'utilisateur avait d'abord
  colle une cle `ak_…` — la doc Platform ne supporte pas le MCP simple,
  donc le pivot vers For You (`ck_…`) etait inevitable.
- Le chemin est **different de l'agentgateway**. Le gateway local (port
  3300) agregait 17 sources MCP derriere un seul `initialize`. Si l'une
  d'elles tombait, tout tombait — c'est exactement ce que l'utilisateur
  voulait eviter. Composio en direct contourne ce point de defaillance
  unique.

## Comment le retirer

1. Retirer l'entree `composio` de `~/.mcp.json`
2. Retirer `COMPOSIO_CONSUMER_KEY` de `~/.claude/settings.json`
3. Redemarrer CC

Aucun fichier versionne, aucun script de deploy, aucune migration. C'est
un changement de configuration utilisateur, pas de projet.
