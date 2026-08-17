---
type: Bundle guide
title: Instructions du bundle mémoire
description: Ce qui a sa place dans 40_Memory_Wiki_OKF, ce qui n'en a pas, et comment le bundle se distingue d'un wiki de code.
tags: [okf, memoire, gouvernance]
generated: { by: claude-opus-5, at: 2026-08-17T15:10:00Z }
verified:
  - { by: human:amdkn, at: 2026-08-17T15:05:00Z }
sources:
  - id: canon-local
    resource: "~/.claude/CLAUDE.md — « Ce qui ne va PAS dans le bundle »"
    title: Canon du poste
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Ce bundle n'est pas un wiki de code

Un wiki de code décrit un dépôt : son architecture, ses commandes, ses points
d'entrée. Il se **régénère** quand le code change.

Ce bundle décrit ce que le code **ne dit pas** : pourquoi une décision a été
prise, ce qu'une mesure a réellement montré, quel piège a déjà coûté une
journée. Il ne se régénère pas — il s'accumule.

La conséquence pratique : une page qui pourrait être reconstruite en lisant le
dépôt n'a rien à faire ici.

# Ce qui a sa place

- Une **décision** et sa raison — surtout quand l'option écartée était
  défendable.
- Une **mesure** et sa portée exacte — ce qui a été regardé, avec quel outil.
- Un **piège payé** : le symptôme, la fausse piste, la cause réelle.
- Un **câblage** : ce qui est branché à quoi, avec le chemin pour le défaire.

# Ce qui n'a pas sa place

- **Les secrets.** Ni valeur, ni fragment. Le préfixe suffit (`ck_…`, `sbp_…`).
  Cette règle n'a pas d'exception, y compris dans un exemple de configuration.
- Ce que le dépôt raconte déjà : structure du code, historique git, contenu
  d'un `CLAUDE.md` versionné.
- Ce qui n'intéresse que la conversation en cours.
- Une affirmation qu'on n'a pas vérifiée et qu'on présente comme vérifiée —
  c'est le seul défaut que le format ne pardonne pas, parce qu'il contamine
  tout ce qui s'appuiera dessus.

# Le doute se consigne, il ne se lisse pas

Quand une connaissance est partielle, l'écrire partielle : `verified` absent
vaut « non vérifié », et c'est une information utile. Une page honnêtement
incomplète sert le lecteur suivant. Une page faussement assurée le trompe.

# Structure

Quatre sous-bundles, chacun avec son `index.md` :

| Sous-bundle | Contenu |
|---|---|
| `architecture/` | décisions de structure et leurs raisons |
| `integrations/` | ce qui est branché à quoi, et ce que ça a coûté |
| `operations/` | playbooks, runbooks, gestes de remise en route |
| `security/` | modèles de sécurité, vulnérabilités, cloisonnements |

Un sous-bundle vide garde son `index.md` : il déclare une case qui attend, ce
qui vaut mieux qu'un lien vers un dossier absent.
