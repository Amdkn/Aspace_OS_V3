---
name: ship
description: SHIP factory via gstack /ship — JAMAIS outboard sans GO A+ explicite. Use this skill whenever the user says 'ship', 'deploy', 'release', or wants to push outward to production.
when_to_use: "Trigger on 'ship', 'deploy', 'release'. C'est une action SHIP — JAMAIS auto, JAMAIS batché."
allowed-tools: [Bash, Read]
version: 1.0.0
author: shim-gstack@omk-nexus-coaching-premium (2026-07-04)
license: MIT
---

# ship — shim pour gstack ⇄ Summers SHIP factory

> ⚠️ **DANGER ZONE** : cette commande = SHIP outboard-facing.

## Doctrine anti-Ultron OUTBOUND

- **ÉCRAN par défaut** : `SKIP_SHIP=1` activé dans l'env si A0 n'a pas explicitement GO
- **Audit obligatoire** : avant tout `git push` / `vercel deploy` / `npm publish` → toast A0 HITL
- **Pas d'auto-approval** : aucune action batchée, aucun rollback auto

## Mapping E-Myth → gstack

| Summers captain | gstack command | Variant ICP |
|---|---|---|
| Summers-Solaris | `ship` | AaaS Solaris variant |
| Summers-Nexus | `ship` | AaaS Nexus variant |
| Summers-Orbiter | `ship` | OMK spearhead |

## Invocation (PRÊT ship requires A0 HITL pre-flight)

```bash
# Étape 1 : smoke check
cd "C:\Users\amado\shadow-l1-garrytan-gstack"
bun run ./ship/smoke.ts  # vérifie pre-deploy conditions

# Étape 2 : si A0 GO explicite
A0_GO_SHIP=1 bun run ./ship/index.ts "<env>"

# Si SKIP_SHIP=1 ou A0_GO_SHIP absent → audit fail-safe → aucun push
```

## Anti-Ultron (c1-c3 NON-NEGO)

- **c1** : aucun ajout à CLAUDE.md
- **c2** : `/browse` = OPTION
- **c3** : auto-update off
- **Outbound** : outboard-facing = **JAMAIS automatique** — Tony Stark appuie sur le bouton

## Sister canon

- Source canon gstack : `C:\Users\amado\shadow-l1-garrytan-gstack\ship\SKILL.md` (81 KB)
- Plan Lightning §4 L1-2 + §8 sobriété Rick
