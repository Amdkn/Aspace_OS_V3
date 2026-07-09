---
name: autoplan
description: Boucle mesure → confrontation → correction via gstack /autoplan. Use this skill whenever a fresh signal lands in `omk-nexus-coaching-premium/signals/` or the user wants to generate a de-novo plan from a signal.
when_to_use: "Trigger on new signal in signals/, 'autoplan', 'plan from signal', or weekly cadence Monday."
allowed-tools: [Bash, Read]
version: 1.0.0
author: shim-gstack@omk-nexus-coaching-premium (2026-07-04)
license: MIT
---

# autoplan — shim pour gstack ⇄ boucle auto-loop canon

> **Boucle canon** : signal → autoplan → review (gate Jerry) → retro (gate Chapel) → ship (gate Summers).

## Mapping E-Myth → gstack

gstack `/autoplan` = la première brique de la chaîne Canonh. Lit les signals,
produit 1 plan de-novo, le présente pour review (Picard) avant exécution (Jerry) puis SHIP (Summers).

## Invocation sobre

```bash
# Étape 1 : check signals/ pour inputs non lus
ls C:\Users\amado\ASpace_OS_V2\30_Business_OS\10_Projects\omk-nexus-coaching-premium\signals\

# Étape 2 : run autoplan sur le premier signal
cd "C:\Users\amado\shadow-l1-garrytan-gstack"
bun run ./autoplan/index.ts --signal "<signal-filename>"
```

## Sortie canonique

`autoplan` produit 1 plan YAML dans `signals/.plans/<signal>.plan.yaml`
conforme au format Strategy Session (ce qui permet audit Picard post).

## Anti-Ultron (c1-c3 NON-NEGO)

- Lecture seule sur sources canoniques
- Append-only dans `signals/.plans/` (plans auto sont append-only)
- Aucune mutation hors `signals/` directory

## Sister canon

- Source canon gstack : `C:\Users\amado\shadow-l1-garrytan-gstack\autoplan\SKILL.md` (100 KB)
- Plan Lightning §4 L1-5 + §6 Zora nocturne
