---
type: Playbook
title: Niveau 4 — auto-validation des concepts OKF (2026-08-31)
description: Instruments de validation automatique du bundle OKF. Mesure : 41 concepts, 0 en confiance humaine, 0 avec date de validité.
tags: [okf, validation, n4, confiance, machine, humain]
generated: { by: claude-opus-5, at: 2026-08-31T06:20:00Z }
verified:
  - { by: human:amdkn, at: 2026-08-31T21:35:17Z }
  - { by: process:valider_okf_niveau4, at: 2026-08-31T06:20:00Z }
sources:
  - id: instrument-n4
    resource: "scripts/valider_okf_niveau4.py"
    title: Validates OKF concepts per canon v0.2
    last_modified: 2026-08-31
  - id: canon-okf
    resource: "40_Memory_Wiki_OKF/OKF.md"
    title: OKF v0.2 — frontmatter contract
    last_modified: 2026-08-29
  - id: n1-nettoyage
    resource: "scripts/nettoyer_sessions_zombies.py + _ARCHIVE_sessions_zombies/2026-08-31"
    title: Niveau 1 — 4 265 vidages de sessions archivés
    last_modified: 2026-08-31
okf_version: "0.2"
---

# Niveau 4 — auto-validation des concepts OKF

## Ce qui a été exécuté ce 2026-08-31

Deux instruments, deux niveaux du plan d'autonomie :

### Niveau 1 : auto-nettoyage des vidages de sessions
`scripts/nettoyer_sessions_zombies.py` — 4 265 `.md` déplacés de
`00_Amadeus/30_MEMORY_CORE/sessions_md/` vers
`_ARCHIVE_sessions_zombies/2026-08-31/`. **Jamais supprimés**, déplacés.
La règle : un zombie est un `.md` non cité par le bundle OKF et sans wikilink
ou frontmatter exploitables. 382 `.md` gardés (distillés ou cités).

### Niveau 4 : auto-validation des concepts OKF
`scripts/valider_okf_niveau4.py` — parcourt le bundle et applique le contrat
OKF v0.2 :

| Règle | Résultat |
|---|---|
| frontmatter complet (`type`, `title`, `description`, `tags`, `sources`, `okf_version`) | 38/41 ok |
| `verified` présent et non vide | 38/41 ok |
| au moins un `verified.by: human:` | **0/41** |
| date de validité (`valide_de` / `valide_jusqu_a`) | **0/41** |

## Ce que le script a révélé — et ce qu'il ne peut pas décider

**Tous les concepts du bundle sont en « confiance : machine ».**
Aucun n'a été revu par un humain. Aucun n'a de date d'expiration.

C'est normal et correct pour des concepts générés par agent. Mais la règle
d'or s'applique : **le système signale, il ne décide pas.**

Le script **refuse** d'ajouter un `human:` à la place du propriétaire. Le
champ `verified.by: human:<id>` est une décision de validité, pas une correction
automatique. Ajouter un `human:` sans l'avoir revu serait le pire des
instrument-qui-mente : un concept qui *prétend* être revu sans l'être.

## Ce qui reste à faire (par le propriétaire)

1. **Choisir les concepts à valider** — les 38 qui passent les règles de forme
   sont candidates. Les 3 du `canon/` (sans frontmatter) sont des documents
   de Constitution, pas des concepts OKF : ils échappent par nature.
2. **Ajouter `valide_de` / `valide_jusqu_a`** aux concepts retenus.
3. **Ajouter `verified.by: human:amadou`** à ceux qui le sont vraiment.
4. **Journaliser les non-validés** dans `40_Memory_Wiki_OKF/learning/` avec
   la date et la raison.

## Pas de rejet silencieux

Un concept sans `human:` n'est pas rejeté. Il est **signalé** et reste
lisible. La règle n'est pas un mur, c'est un tag. C'est la différence entre
un filtre qui se compte lui-même (P4 — l'instrument qui ment) et un
instrument qui dit ce qu'il est.