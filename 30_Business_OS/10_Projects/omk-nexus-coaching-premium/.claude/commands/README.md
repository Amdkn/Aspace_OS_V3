# gstack shims — portée projet (omk-nexus-coaching-premium)

> 3 SKILL.md copiés depuis `agent-os/home-court/gstack/` (MIT, garrytan).
> Wrapper sobre `gstack-env.sh` enforce les **3 clauses de sobriété** du plan
> `plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md §4`.

## Commandes disponibles

| Slash command | Skill canon | Rôle |
|---|---|---|
| `/gstack-autoplan` | `gstack/autoplan/SKILL.md` | Auto-review pipeline (CEO/design/eng/DX) |
| `/gstack-cso` | `gstack/cso/SKILL.md` | Chief Security Officer (OWASP+STRIDE+deps) |
| `/gstack-ship` | `gstack/ship/SKILL.md` | Ship workflow (merge+tests+review+PR) |

## Usage sobre — 1 ligne

```bash
source /c/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/omk-nexus-coaching-premium/.claude/commands/_lib/gstack-env.sh
# puis invoquer /gstack-* via ton harness
```

## 3 clauses enforced (c1 / c2 / c3)

| Clause | Enforcement | Source |
|---|---|---|
| **c1** ZÉRO écriture dans `~/.claude/` (sacred P4) | `gstack-env.sh` exporte PATH depuis `agent-os/home-court/gstack/bin/` — clone hors `.claude/`, notre `CLAUDE.md` jamais touché | plan §4 c1 |
| **c2** `/browse` = option, pas remplacement | harness chrome MCP `mcp__claude-in-chrome__*` reste le défaut. `GSTACK_USE_BROWSE=1` active gstack browse si besoin explicite | plan §4 c2 |
| **c3** Auto-update réseau OFF | `GSTACK_NO_UPDATE=1` + wrapper no-op `gstack-update-check` prioritaire sur PATH (no-op silencieux) | plan §4 c3 |

## Sister canon

- Source : `agent-os/home-court/gstack/` (git clone shallow, v1.58.5.0)
- Plan : `.claude/plans/plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md §3-§4`
- War Room : `citadel/decisions/2026-07-05_l0_pocock_installed.md` (L0 Pocock sister)

## Append-only

Ce fichier documente l'install. Si une clause change → éditer `gstack-env.sh` + ce README.
**Ne jamais modifier les SKILL.md canon copiés** — re-pull depuis upstream si upgrade.