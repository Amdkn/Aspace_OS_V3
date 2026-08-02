---
type: rot-rates
title: ROT.md — péremption déclarée par module dans l'organigramme LD01
description: rot-rate canon hérité du plan-meta-memoire §6 (ROT.md v1) + étendu aux modules de l'organigramme CARDIA-TDD. Chaque module déclare sa cadence de péremption et son remède. Une cadence dépassée = signal de revue.
timestamp: 2026-07-04T12:00:00-04:00
domain: LD01_Career_Business
rot_rate: lent
inherits_from: plan-meta-memoire-okf-wiki-graphify-dox.md §6
---

# ROT.md — péremption déclarée par module

> *« La maintenance est scheduled, pas volée au temps A0. »* — plan-meta-memoire §5 (Time Use discipline).

## Rot-rates par module (initialisation 2026-07-04)

| Module / Couche | rot-rate | Remède | Cadence revue | Owner |
|---|---|---|---|---|
| `00_index.md` | lent | re-lint OKF à chaque migration plan source | 1×/cycle 12WY (W13) | A0 |
| `AGENTS.md` | lent | DOX pass après chaque ajout module | 1×/cycle 12WY | A0+Book |
| `CLAUDE.md` | lent | idem | 1×/cycle 12WY | A0+Book |
| `10_methodology/00_CARDIA_overview.md` | lent | re-test CARDIA à stress W5 | 1×/cycle 12WY | A0 |
| `20_skeleton/00_module_template.md` | lent | test sur 1 module créé W4 | 1×/cycle 12WY | A0 |
| `30_decisions/ADR-LD01-*.md` | imuable (ADR canon) | succession par ADR-NNN+1 uniquement | jamais (sauf supersede) | A0 |
| `90_manifests/manifest.cross-harness.md` | moyen | re-test surface harnesses à chaque apparition Shadow | 1×/mois | A0 |
| `99_meta/calendar.md` | rapide | append-only D4 + curation fin W13 | continu | Book+MC |
| `99_meta/rot-rates.md` (ce fichier) | lent | re-cohérence avec plan-meta-memoire §6 | 1×/cycle 12WY | A0 |
| `99_meta/doctrine_lock_map.md` | lent | re-vérification à chaque amendement plan source | 1×/cycle 12WY | A0 |
| `A3_Book_LD01_Spec.md` | imuable (canon sister) | jamais muté | jamais | — (preserve) |
| `BIBLIOGRAPHY.md` | imuable (canon sister) | jamais muté | jamais | — (preserve) |
| `README.md` | imuable (canon sister) | jamais muté | jamais | — (preserve) |

## Boucle Time Use (12WY §5)

- **W3** : cadrage (ROTs initialisés)
- **W4..W12** : scheduled — la rotation rot rapide (calendar.md) opère
- **W13** : archive + Muse DEAL — D11 mesuré par Gwyn (D11 = temps A0 libéré par la boucle)

## Anti-pattern

| Anti-pattern | Effet | Bloqué par |
|---|---|---|
| Module sans rot-rate déclaré | Drift silencieux | CARDIA-TDD §20_skeleton frontmatter |
| Rot-rate trop long sur module vivant | Pourrissement latent | audit W6 |
| Rot-rate trop court sur module stable | Charge cognitive | CADR W6 + audit |
