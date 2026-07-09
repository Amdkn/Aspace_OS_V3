---
source: Shadow_L1
date: 2026-05-19
type: agent-tools
agent: Claude_Code_CLI
layer: L1
tags: [#Tools, #ClaudeCode, #L1, #LifeOS]
---

# Tools.md — Surface capability Claude Code L1

## CLI tools (always available)

- `Read`, `Write`, `Edit`, `Glob`, `Grep`, `Bash` (filesystem Trust Zone)
- `WebFetch`, `WebSearch` (research, on-demand)

## MCP servers utiles L1

| Server | Usage L1 |
|---|---|
| `context7` | Vérifier doc Baserow API / Plane API / Obsidian plugins |
| `supabase` | Pas pertinent L1 |
| Baserow CLI (à venir via pp-cli-install) | Read tables Life OS |
| Plane CLI (quand 403 résolu) | Read work-items |

## Skills relevant L1

- `/skill-creator` (orchestration uniquement Claude Code)
- `/airtable-enrich` (NON L1 — c'est L2/Marketing)
- `/learn` (cristalliser patterns récurrents Life OS)
- `/learn-eval` (qualifier avant save)
- `/checkpoint` (sauvegarder état mission longue)
- `/save-session` / `/resume-session` (continuation cross-tick)

## Environment vars consommées

```
ANTHROPIC_BASE_URL=https://api.minimax.io/anthropic
ANTHROPIC_API_KEY=<MiniMax Token Plan key>
BASEROW_API_TOKEN=<scope read Life OS>
BASEROW_LIFE_OS_BASE_ID=<id>
PLANE_API_TOKEN=<currently 403>
ASPACE_ROOT=C:\Users\amado\ASpace_OS_V2
```

## Forbidden tools L1

- Aucun outil de mutation Baserow / Plane / Obsidian sans mission card signoff
- Pas de `gh` writes (réservé L2 build/release)
- Pas de `vercel deploy` (réservé L2)

## Inbounds

- `./Heartbeat.md`
- `./Agent.md`
