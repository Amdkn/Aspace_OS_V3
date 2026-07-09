---
name: plan-ceo-review
description: Jerry-cadrage CEO review via gstack /plan-ceo-review (E-Myth mapping). Use this skill whenever the user says 'plan-ceo-review', 'CEO review', 'cadre stratégique projet', or wants to structure the CEO-level framing of a project before deeper work.
when_to_use: "Trigger on 'plan-ceo-review', 'CEO review', 'review CEO', 'cadre CEO'."
allowed-tools: [Bash, Read]
version: 1.0.0
author: shim-gstack@omk-nexus-coaching-premium (2026-07-04)
license: MIT
---

# plan-ceo-review — shim pour gstack ⇄ E-Myth Jerry

> **SHIM** — ce fichier est un **shim léger** (pas une copie du SKILL.md gstack).
> La commande canonique vit dans `C:\Users\amado\shadow-l1-garrytan-gstack\plan-ceo-review\SKILL.md`
> (89 KB) et est invoquée depuis le home court pour respecter L1-2 du Plan Lightning §4
> (« copie manuelle des `.md` commands vers le scope projet `omk-nexus-coaching-premium/.claude/commands/` »).

## Mapping E-Myth → gstack (cf. L1-4)

| E-Myth B-tier | gstack command | Rôle |
|---|---|---|
| Jerry (B1 captain) | `plan-ceo-review` | cadrage CEO-level projet |
| Picard (A3 captain) | `plan-design-review` / `plan-devex-review` / `plan-eng-review` / `plan-tune` | cadrage projet par discipline |
| Flash / Cyborg / Aquaman (B2) | `review` + `cso` + `qa` | revue/qualité/sécurité |
| Summers (B1 captain) | `ship` (GATED — jamais outboard sans GO A+) | SHIP factory |
| Tous | `autoplan` + `retrospective` | auto-loop mesure → confrontation → correction |

## Invocation sobre (sans toucher CLAUDE.md user ni installer setup gstack)

```bash
# Depuis le home court gstack (c1+c3 respectés : pas de CLAUDE.md, pas d'auto-update)
cd "C:\Users\amado\shadow-l1-garrytan-gstack"
bun run ./plan-ceo-review/index.ts "<args>"
```

Ou via le runner conductor.json (selon config gstack) :

```bash
bun run conductor plan-ceo-review "<args>"
```

## Anti-Ultron (c1-c3 NON-NEGO)

- **c1** : aucun ajout à `~/.claude/CLAUDE.md` (sacred P4) ni au MANIFEST du projet
- **c2** : `/browse` = OPTION (jamais activée implicitement)
- **c3** : auto-update off (par défaut — on n'installe pas `setup`)

## Sister canon

- Source canon gstack : `C:\Users\amado\shadow-l1-garrytan-gstack\plan-ceo-review\SKILL.md`
- Plan Lightning §4 L1-2 : `~/.claude/plans/plan-lightning-l0l1l2-coach-book-picard-jerry-summers.md:85-94`
- ADR-LD01-003 (RATIFIED FULL) BC-Project-OMK-Nexus-Coaching
- LD01/30_decisions/ADR-LD01-007_citadelle_agent_os_jarvis_pattern.md
