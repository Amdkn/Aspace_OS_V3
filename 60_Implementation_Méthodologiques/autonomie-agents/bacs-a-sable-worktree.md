---
type: Concept
title: Bacs à sable — ce que git worktree changerait, et ce qu'il coûterait
description: Chantier 3 du passage 1 → 2 : remplacer la discipline du brief par un cloisonnement d'outil. Une copie de travail isolée par chantier, branches parallèles sans collision.
tags: [autonomie, bac-a-sable, worktree, cloisonnement, git]
generated: { by: minimax-m3, at: 2026-08-17T22:45:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T22:45:00Z }
sources:
  - id: ia-strategie-autonomie
    resource: 60_Implementation_Méthodologiques/_sources/echelle-autonomie-agents.md
    title: "IA et Stratégie — extraction"
    last_modified: 2026-08-17
  - id: canon-section-1
    resource: C:/Users/CLAUDE.md
    title: "Canon du poste — agents en parallèle sur le même arbre"
    last_modified: 2026-08-15
okf_version: "0.2"
---

# Le principe

*« Les bacs à sable. Une copie de travail isolée par chantier (`git worktree`),
pour que deux agents ne se marchent jamais dessus. Plus une liste de
commandes sûres autorisées une fois pour toutes — en gardant l'approbation
manuelle pour le réseau, les secrets et les suppressions. Commencer à
deux agents, pas dix. »*

Le principe est simple : la séparation doit tenir à l'**outil**, pas à la
**discipline**. Une discipline peut s'oublier ; un outil physique ne
s'oublie pas.

# L'écart mesuré

Le cloisonnement actuel est de **deuxième ordre** : il tient à la
rigueur du brief, pas à la grille du système.

Conséquence observée : *« Quatre agents ont rapporté '94 erreurs' puis '83
erreurs' de typage en mesurant chacun les éditions en vol des trois
autres. »* L'agent ne savait pas qu'il mesurait du code en train de
changer. Le brief limitait ses fichiers en écriture, mais pas en lecture.

L'écart est typique de l'étape 1 : la confiance repose sur l'auteur du
brief, pas sur l'infrastructure. À l'étape 2, l'infrastructure prend le
relais.

# Ce que `git worktree` changerait

Une commande, et chaque agent a sa copie :

```bash
git worktree add ../repo-agent-A main
git worktree add ../repo-agent-B main
```

Chaque agent travaille dans son répertoire, voit **uniquement** ses
fichiers, et **ne peut pas** écrire dans celui du voisin sans merge
explicite. La séparation physique remplace la séparation déclarative.

Trois propriétés nouvelles :

1. **Les tests se lancent en isolation.** Un agent qui lance `vitest`
   dans son worktree ne dépend pas de l'état du voisin.
2. **Les merges sont visibles.** Quand deux agents ont touché au même
   fichier, Git le dit — plus d'écrasement silencieux.
3. **L'examen est traçable.** Le rapport de l'agent cite son worktree,
   l'utilisateur peut y aller voir sans naviguer dans le dépôt principal.

# Ce que `git worktree` coûterait

Le coût n'est pas nul, et il mérite d'être nommé :

| Aspect | Coût |
|---|---|
| Disque | × N copies du dépôt. Sur un dépôt de 200 MB et 4 agents, **800 MB** pris. À dix agents, 2 GB. |
| Commandes shell | les chemins absolus changent par agent. Les scripts qui supposent `pwd` se cassent. |
| Hooks git | les hooks du dépôt principal (pre-commit) ne tournent pas dans les worktrees. C'est un bien (isolement) et un mal (perte de garde-fou). |
| Branches | il faut merger en fin de chantier. Si l'agent ne le fait pas, les worktrees s'accumulent. |
| Indice IA | certains outils (CC, Cursor, Continue) indexent par répertoire. Un worktree change l'indexation. |

# Les raisons de **ne pas** adopter tout de suite

Trois raisons qui poussent à la prudence :

1. **Le poste n'est pas à l'étape 2.** L'étape 1 autorise un agent
   principal supervisé ; le passage à 2-4 agents parallèles n'est pas
   acquis. Installer l'outillage de l'étape 2 avant d'y être crée un
   stock d'outils dormants, et des worktrees non mergés depuis six mois.
2. **La discipline du brief fonctionne, et l'a prouvé.** Aucune collision
   majeure n'a abouti à une perte de travail, dans les sessions
   consignées. Le risque zéro n'existe pas, mais le risque courant est
   borné.
3. **Le coût d'indexation est non trivial.** Reconfigurer CC pour
   travailler sur quatre worktrees换个模式。 Ce n'est pas un
   quart d'heure, c'est une demi-journée, et ça touche à l'outillage
   commun — voir la règle du canon : *« faire passer seul, en premier,
   l'agent qui touche à l'outillage commun »*.

# Le geste à poser — un seul agent, le moment venu

Quand le poste passe à l'étape 2 (deux agents parallèles), introduire
un worktree **à la fois**, sur un chantier-pilote. Recommandations :

1. **Choisir un chantier à fort cloisonnement** — par exemple, une
   distillation sur bundle OKF, où la lecture de `ASpace_OS_V2` est
   readonly et l'écriture se fait dans un sous-ensemble de
   `60_Implementation_Méthodologiques/`.
2. **Créer le worktree via une commande documentée** dans le canon, pas
   découverte au fil de l'eau.
3. **Mesurer sur un mois** : zéro collision, zéro erreur de mesure,
   gain de confiance ou pas. Décider ensuite si l'étape 3 (quatre
   agents) mérite le même investissement.

# Vérification

L'indicateur qu'on est **prêt** à adopter `git worktree` :

- deux courtes sessions ont déjà tourné en parallèle sur le même
  arbre, sans collision, et l'utilisateur les a laissées filer ;
- le canon mentionne déjà la pratique dans un brief ;
- l'utilisateur a accepté de merger en fin de chantier, sans
  AUTOMATIQUE.

Tant qu'un de ces trois manque, le worktree est prématuré.

# Risque résiduel

Un worktree n'est pas une cage. Un agent qui **veut** lire hors
périmètre peut le faire — `git worktree` n'empêche pas la lecture, il
isole l'écriture. La borne « périmètre strict » reste déclarative, et
le relecteur (voir `agent-relecteur-mandat.md`) est ce qui la fait
respecter.
