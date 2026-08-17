---
type: Concept
title: L'examen préalable — une commande unique qui prouve avant de rendre
description: Chantier 1 du passage 1 → 2 : une commande unique qui enchaîne vitest, deux tsc et oxlint, et que l'agent doit lancer avant de présenter un livrable — pas après, pas à la demande.
tags: [autonomie, examen, verification, linter, tests]
generated: { by: minimax-m3, at: 2026-08-17T22:35:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T22:35:00Z }
sources:
  - id: ia-strategie-autonomie
    resource: 60_Implementation_Méthodologiques/_sources/echelle-autonomie-agents.md
    title: "IA et Stratégie — extraction"
    last_modified: 2026-08-17
  - id: canon-canon
    resource: C:/Users/amado/CLAUDE.md
    title: "Canon du poste — sections §1 et §1bis"
    last_modified: 2026-08-15
okf_version: "0.2"
---

# Le principe

*« Une commande unique que l'agent lance lui-même **avant** de montrer quoi
que ce soit : tests, compilation, linter, et un test bout-en-bout si c'est
de l'interface. La règle : l'agent n'a pas le droit de présenter un travail
qu'il n'a pas déjà vérifié. »*

L'examen est ce qui transforme l'agent d'**artisan** (qui fait) en
**garant** (qui prouve). Sans examen, l'humain relit tout ; avec examen,
l'humain relit le rapport de l'examen.

# L'écart mesuré

Le poste a les briques :

- `vitest` (tests unitaires, présent dans plusieurs projets) ;
- deux `tsc` (production + types stricts, l'un dans `coach-os`, l'autre
  dans un autre chantier) ;
- `oxlint` (linter rapide).

**Mais aucune commande unique ne les enchaîne.** Trois conséquences
mesurables :

1. **Un agent peut rendre un livrable en ayant oublié une brique.** L'erreur
   qui revient : tests passent, linter oubli ; types passent, tests oubliés.
2. **L'utilisateur doit relancer l'agent sur la brique oubliée.** Le coût
   d'aller-retour dépasse souvent le coût de l'examen complet.
3. **Rien n'oblige l'agent à la lancer avant de rendre.** Le canon dit
   *« un agent délégué n'est jamais cru sur parole : son résultat se
   vérifie »* — mais la vérification est à la charge de l'utilisateur, pas
   de l'agent.

L'écart est la **chaîne manquante**, plus que l'obligation. L'obligation
existe à l'état de principe, pas de commande.

# La commande d'examen

Une commande POSIX portable, à déposer dans le dépôt racine sous le nom
`tools/examen.sh` (et alias Windows `examen.cmd`) :

```bash
#!/usr/bin/env bash
set -euo pipefail
echo "== tsc strict =="
npx tsc --noEmit
echo "== tsc secondaire =="
npx tsc --noEmit -p tsconfig.test.json
echo "== oxlint =="
npx oxlint
echo "== vitest =="
npx vitest run
echo "== EXAMEN OK =="
```

**Règles :**

- **Tout en `set -euo pipefail`** — la première erreur arrête, pas
  l'avant-dernière.
- **Aucun cache** — la commande doit passer en CI sans artefacts
  pré-construits. Pas de `tsc --build`, pas de `vitest --run --coverage`.
- **Une sortie lisible** — chaque étape préfixe son nom, l'agent cite
  l'étape en erreur dans son rapport.
- **Sortie 0 = examen réussi.** Sortie ≠ 0 = l'agent **refuse** de rendre
  et écrit dans son rapport : *« examen échoué à l'étape X, voir journal. »*

# L'obligation côté brief

Tout brief de la forme *« écris X »* doit contenir une ligne :

> **OBLIGATION : lance `tools/examen.sh` avant de présenter ton livrable.
> Sortie jointe au rapport. Échec = refuse de rendre.**

Cette ligne est **invariante** : elle ne se négocie pas, ne se résume pas,
ne se déplace pas. Elle déclenche le passage de l'étape 1 (l'agent
présente, l'humain relit) à l'étape 2 (l'agent présente un livrable déjà
vérifié, l'humain relit le rapport d'examen).

# Ce que la commande doit rendre en cas d'échec

L'échec est une **information**, pas un mur. La sortie doit :

- indiquer **quelle étape** a échoué (la première qui sort en erreur) ;
- montrer les **cinq dernières lignes** de l'erreur complète, pas un
  dump ;
- donner un **hint** sur la cause probable si elle est connue du
  dépôt (par exemple, fichier `config/x.ts` cité dans le tsconfig).

# Vérification

Ouvrir un brief récent et regarder le rapport de l'agent. S'il manque
une ligne *« examen : OK »* ou *« examen : échec à l'étape Y »*, l'obligation
n'est pas en place. Viser 100 % de briefs avec cette ligne, et 0 %
d'examens « oubliés ».

# Coût

Une passe d'examen prend 30 à 90 secondes sur les projets actuels. C'est
le coût de la confiance. Tout brief long qui ne le budgette pas est un
brief qui s'est trompé d'étage.
