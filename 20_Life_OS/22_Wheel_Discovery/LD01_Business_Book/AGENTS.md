---
type: dox-family-agents
parent: ..\..\..\00_Amadeus\01_Identity_Core\AGENTS.md
zone: 20_Life_OS\22_Wheel_Discovery\LD01_Business_Book
sibling_zones:
  - 20_Life_OS\22_Wheel_Discovery\LD02_Finance_Saru
  - 20_Life_OS\22_Wheel_Discovery\LD03_Health_Culber
  - 20_Life_OS\22_Wheel_Discovery\LD04_Cognition_Tilly
  - 20_Life_OS\22_Wheel_Discovery\LD05_Social_Stamets
  - 20_Life_OS\22_Wheel_Discovery\LD06_Family_Burnham
  - 20_Life_OS\22_Wheel_Discovery\LD07_Creativity_Reno
  - 20_Life_OS\22_Wheel_Discovery\LD08_Impact_Georgiou
applied_doctrine: ..\plan-meta-memoire-okf-wiki-graphify-dox.md §3.9
---

# AGENTS.md — LD01 Business Book (zone filesystem)

> DOX family contract (cf. `agent0ai/dox` + plan-meta-memoire §P4.0). Ce contrat lie la zone filesystem ; les harnesses consomment via leur propre `CLAUDE.md` (sister).

## Purpose

Stocker et organiser la doctrine canonique du **domain LD01 Career & Business** (A3 Book agent, Discovery crew), alignée `plan-meta-memoire-okf-wiki-graphify-dox.md` (4 couches OKF/Wiki/Graphify/DOX) et `plan-minimax-l1-book-lune.md` §0 (organigramme Doctrine au lieu de plans markdown plats).

## Ownership

- **Owner canon** : `A3_Book` (Cleveland "Book" Booker)
- **Parent A2** : `A2_DISCOVERY_ZORA`
- **Maintener** : A0 + Book A3 en tandem, **gated HITL** pour toute mutation (Posture C — cf. plan-meta-memoire §3 décision #2 « additif, jamais destructif »)
- **Twin sister** : `symphony/L1/lane_A_specs/03_A3_crews/discovery/book.twin.md`

## Local Contracts (verrouillés, lecture-seule ici)

1. **Additivité stricte** : toute mutation = append (`.md` nouveau ou section nouvelle dans un fichier existant). Jamais de réécriture d'un fichier canon.
2. **Frontmatter OKF** : tout `.md` créé dans cette zone DOIT ouvrir par un frontmatter YAML conforme §6 OKF (au minimum `type` top-level — cf. plan-meta-memoire §3.5).
3. **D1 receipt** : tout nouveau module DOIT avoir au moins 1 vérifieur chiffré (commande → sortie).
4. **ROT déclaré** : tout nouveau module DOIT apparaître dans `99_meta/rot-rates.md` avec sa cadence de péremption.
5. **Heritage canon** : `A3_Book_LD01_Spec.md`, `BIBLIOGRAPHY.md`, `README.md`, `01_Guides_Business/` = **intouchables**. Toute référence passe par eux.

## Work Guidance (règles opérationnelles)

- **Avant tout edit dans cette zone** : lire ce `AGENTS.md` + `00_index.md` + le module ciblé parent.
- **Après changement significatif** : DOX pass — append à `99_meta/calendar.md` (épisode-mémoire) + mettre à jour `90_manifests/manifest.cross-harness.md` si la surface de harness change.
- **Si divergence cross-plan** : `plan-meta-memoire-okf-wiki-graphify-dox.md` §3 tranche (canon mémo-mémoire) ; `plan-minimax-l1-book-lune.md` §0 tranche (organigrammes Doctrine) ; `fancy-hugging-bengio.md` §3.2-§18.1 tranche (alignement matrice Discovery).

## Verification (DoD mesurable)

| Test | Attendu |
|---|---|
| `Get-ChildItem` racine | présence de `00_index.md`, `AGENTS.md`, `CLAUDE.md`, `10_methodology/`, `20_skeleton/`, `30_decisions/`, `90_manifests/`, `99_meta/` |
| `grep -c "^type:" 00_index.md` | ≥ 1 (frontmatter OKF) |
| `grep -l "ADR-LD01" 30_decisions/*.md` | ≥ 1 fichier matchant |
| `cat 99_meta/calendar.md \| wc -l` | ≥ 5 lignes (au moins 1 entrée d'épisode) |
| `git -C $root diff --name-only HEAD~1` | ≤ 1 nouveau fichier par édition (additivité) |

## Child DOX Index (descente)

Voir `00_index.md` §5 (canonique) — registres minimaux :

- `10_methodology/00_CARDIA_overview.md` ← méthode CARDIA-TDD
- `20_skeleton/00_module_template.md` ← squelette-type de module
- `30_decisions/ADR-LD01-*.md` ← ADRs canon (append-only)
- `90_manifests/manifest.cross-harness.md` ← qui consomme quoi
- `99_meta/calendar.md` ← épisode-mémoire
- `99_meta/doctrine_lock_map.md` ← pont avec les plans source
- `99_meta/rot-rates.md` ← péremption déclarée par module

> Last DOX pass : 2026-07-04T12:00:00-04:00 (création). Prochain pass : fin de phase P2 organigrammes-doctrine-registry.
