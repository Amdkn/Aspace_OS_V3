---
type: skeleton-template
title: Module Template — CARDIA-TDD compliant
description: Standard structure for any new module under LD01_Business_Book/. Copy this file, replace bracketed fields, keep the D1 receipt visible from the frontmatter.
timestamp: 2026-07-04T12:00:00-04:00
domain: LD01_Career_Business
---

# Module Template — CARDIA-TDD compliant

> *À copier pour tout nouveau module dans cet organigramme. Pas de module sans frontmatter OKF ni D1 receipt.*

## Frontmatter minimal (reproduction littérale obligatoire)

```yaml
---
type: <bounded-context>-<role>       # ex: a3-book-identity, adr-decision, harness-manifest
title: <TITRE_DU_MODULE>
description: <1 phrase en anglais, ce que ce module décide/décrit>
timestamp: 2026-07-04T12:00:00-04:00
domain: LD01_Career_Business
bounded_context: <BC-A3-Book | BC-Project-OMK-Nexus | BC-Guides-LD01 | BC-Bib6 | BC-Solaris>
inherits_from: <fichier parent dans l'organigramme>
verified_by: <commande + sortie attendue — D1 receipt>
rot_rate: <lent | moyen | rapide>
---
```

## Corps de module (5 sections standard)

### 1. Purpose (1 phrase)

> Ce module sert à <verbe à l'infinitif> <objet>. Il sert UNE fois, clairement, et fait ensuite référence.

### 2. Inputs / Outputs

- **Inputs** : ce que ce module consomme (liste à puces, ≤ 5 items)
- **Outputs** : ce qu'il produit (liste à puces, ≤ 5 items)

### 3. Local Contracts (≤ 3 règles)

1. Règle 1 (liante)
2. Règle 2 (liante)
3. Règle 3 (liante, si applicable)

### 4. Verification (D1 receipt — section la plus importante)

```
# commande
$ <commande powershell ou bash>

# sortie attendue
<chiffre | chemin | booléen>
```

> Le D1 receipt doit être **re-jouable** 4 semaines plus tard sans surprise. Si la sortie change, c'est un signal de rot et `rot-rates.md` doit déclencher une revue.

### 5. Heritage canon (liens obligatoires)

- Parent : `..\..\..\00_index.md`
- Plan source 1 : `C:\Users\amado\.claude\plans\plan-meta-memoire-okf-wiki-graphify-dox.md`
- Plan source 2 : `C:\Users\amado\.claude\plans\plan-minimax-l1-book-lune.md`
- Sister canon : `symphony/L1/lane_A_specs/03_A3_crews/discovery/book.twin.md`

## Anti-patterns

- ❌ Module > 200 lignes → split en sous-module
- ❌ Pas de `type:` dans frontmatter → refusé en lint OKF v0.1
- ❌ D1 receipt sans commande re-jouable → refusé en review
- ❌ Aucune section `Heritage canon` → cohérence DOX cassée

## Cadence de revue

| Cadence rot | Action |
|---|---|
| lent (1×/cycle 12WY) | Revue archive W13 |
| moyen (1×/mois) | Drift audit mensuel |
| rapide (1×/semaine) | Hook post-write lint |
