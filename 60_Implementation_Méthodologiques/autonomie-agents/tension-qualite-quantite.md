---
type: Concept
title: Tension qualité-quantité — quand lisser serait trahir
description: Les deux vidéos ne tirent pas dans le même sens : l'une optimise la qualité d'une réponse, l'autre la quantité de travail délégué. Ce concept dit comment on tranche, cas par cas, sans nier la tension.
tags: [autonomie, prompt-systeme, tension, qualite, quantite]
generated: { by: minimax-m3, at: 2026-08-17T22:55:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T22:55:00Z }
sources:
  - id: indydevdan-extraction
    resource: 60_Implementation_Méthodologiques/_sources/indydevdan-prompt-systeme.md
    title: "IndyDevDan — extraction"
    last_modified: 2026-08-17
  - id: ia-strategie-autonomie
    resource: 60_Implementation_Méthodologiques/_sources/echelle-autonomie-agents.md
    title: "IA et Stratégie — extraction"
    last_modified: 2026-08-17
  - id: index-canon
    resource: 60_Implementation_Méthodologiques/index.md
    title: "Bundle index — la contradiction utile"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Le constat

Les deux vidéos convergent par leur analyse, mais **divergent par leur
optimisation** :

| Source | Optimise | Bénéfice marginal attendu |
|---|---|---|
| **IndyDevDan** | la qualité d'une réponse (moins de verbosité, points de référence, bornes opérationnelles) | un canon bien écrit élève toutes les sessions futures |
| **IA et Stratégie** | la quantité de travail délégué (plus d'agents, moins de surveillance) | un essaim qui tourne pendant qu'on dort |

**Les deux ne tirent pas dans le même sens.** Un prompt système très
contraint coûte du temps à écrire et ralentit la mise en route ; un
essaim lancé vite produit plus, moins bien.

L'index du bundle le reconnaît : *« Le canon les réconcilie par une règle
simple : plus un artefact est multiplicatif, plus on ralentit pour l'écrire
à la main. »* Cette règle est juste, mais elle ne tranche pas tout.

# Les arbitrages que la règle ne tranche pas

Quatre cas où la règle de multiplicativité ne suffit pas :

1. **Canon vs brief.** Un canon s'écrit à la main ; un brief d'agent peut
   se dicter. Mais à partir de quel taux de délégation le canon doit-il
   absorber des consignes jusqu'ici restées orales ? La règle répond *«
   plus la chose est multiplicative »* — un brief peut être réutilisé
   cinq fois, ce qui le rend multiplicatif. Le seuil est flou.
2. **Examen vs cadence.** L'examen (voir `examen-prealable.md`) ajoute
   30 à 90 secondes par livrable. Sur un essaim de dix agents, c'est
   5 à 15 minutes en plus par cycle. La règle ne dit pas si l'examen
   est *toujours* rentable.
3. **Relecture vs autonomie.** Un agent relecteur (voir
   `agent-relecteur-mandat.md`) coûte 5 à 15 minutes par livrable. Sur
   les chantiers à forts défauts attendus, c'est un gain ; sur les
   chantiers à faible risque, c'est une dépense.
4. **Bacs à sable vs complexité.** `git worktree` (voir
   `bacs-a-sable-worktree.md`) isole, mais ralentit la mise en route.
   Sur un chantier de deux jours, l'isolation est marginale ; sur un
   chantier de deux heures, elle est disproportionnée.

# Les cas qui forcent à choisir

Trois cas réels observés sur ce poste, où la tension s'est manifestée :

| Cas | Choix fait | Lecture critique |
|---|---|---|
| Distillation des sources IndyDevDan + IA et Stratégie | canon resserré (qualité) | correct — la distillation est multiplicative |
| Génération de douze concepts en une passe | cadence rapide, relecture par l'auteur | risqué — la relecture est humaine, pas automatisée |
| Adoption de `git worktree` | refus, cloisonnement par brief | prudent — l'étape 2 n'est pas acquise |

Le troisième cas est le plus instructif : à l'étape 1, le cloisonnement
par brief est plus rentable que le cloisonnement par worktree. La règle
« plus c'est multiplicatif, plus on ralentit » s'applique au worktree
lui-même : l'outillage est multiplicatif, donc on n'y touche pas avant
d'y être.

# La grille de décision, cas par cas

Quatre questions, dans l'ordre. Si la première réponse est « non »,
passer à la suivante.

1. **L'artefact est-il multiplicatif ?** (utilisé ≥ 5 fois dans les six
   mois). Si oui : temps long, qualité première.
2. **L'artefact est-il sensible à un défaut ?** (sécurité, finance,UX).
   Si oui : examen + relecture, regardless du coût.
3. **L'artefact est-il court et isolé ?** (une seule utilisation). Si
   oui : cadence rapide, pas d'examen.
4. **L'artefact est-il dans un périmètre conflictuel ?** (plusieurs
   agents en parallèle). Si oui : bac à sable, sinon cloisonnement par
   brief.

Cette grille **n'efface pas** la tension — elle la déplace. À chaque
cas, l'utilisateur choisit consciemment entre qualité et quantité, et
peut défendre son choix.

# Ce que la grille ne fait pas

Elle ne dit pas **quel arbitrage fait le bon artisan** — c'est une
question d'expérience, pas de règle. Elle dit seulement : **nommer la
tension**, et avoir un outil pour la traiter.

Ce qui serait trahir : lisser la tension, prétendre que qualité et
quantité vont de pair, et glisser vers un canon bavard et un essaim
gaspilleur. Le canon bavard ralentit sans élever ; l'essaim gaspilleur
produit sans consolider. Les deux sont desformes d'échec.

# Vérification

Une fois par mois, lister les trois principaux arbitrages du mois, et
pour chacun, citer la branche choisie (qualité ou quantité) et la
raison. Si la branche est toujours la même, le mécanisme d'arbitrage
est en train de s'éteindre — et un extrême s'installe.

# Conclusion provisoire

La tension est **structurante**, pas accidentelle. Un poste qui ne la
ressent pas a probablement choisi un pôle et oublié l'autre. La règle
qui suit cet effort de nominal : **il n'y a pas de bon arbitrage par
défaut — il n'y a que des arbitrages argumentés.**
