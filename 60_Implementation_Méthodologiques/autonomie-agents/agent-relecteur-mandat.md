---
type: Concept
title: Agent relecteur — mandat unique, contexte vierge
description: Chantier 4 du passage 1 → 2 : un agent neuf qui n'a pas écrit le code, avec un mandat unique — trouver ce qui casse. Pas un copiste qui valide, pas un professeur qui note, un testeur qui signale.
tags: [autonomie, relecture, revue, separation, conflit]
generated: { by: minimax-m3, at: 2026-08-17T22:40:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T22:40:00Z }
sources:
  - id: ia-strategie-autonomie
    resource: 60_Implementation_Méthodologiques/_sources/echelle-autonomie-agents.md
    title: "IA et Stratégie — extraction"
    last_modified: 2026-08-17
  - id: canon-1bis
    resource: C:/Users/amado/CLAUDE.md
    title: "Canon du poste — section §1bis « Vérifier, c'est regarder »"
    last_modified: 2026-08-15
okf_version: "0.2"
---

# Le principe

*« La relecture. Un agent neuf, qui n'a pas écrit le code, avec un seul
mandat : trouver ce qui casse. Le fabricant ne se juge jamais lui-même. »*

Le point n'est pas d'avoir un deuxième avis — c'est d'avoir un avis
**indépendant** du contexte de production. Un agent qui vient d'écrire le
code a deux handicaps :

- il **sait** pourquoi le code est correct, et projette cette certitude
  sur la relecture ;
- il a **investi** dans la solution, et le biais de confirmation lui fait
  défendre ce qu'il a produit.

Un agent neuf, sans contexte de production, n'a pas ces biais. Il regarde
le code **comme un utilisateur le rencontrera**.

# L'écart mesuré

Sur ce poste, la relecture est faite par **Opus** — la session qui
exécute. Trois défaillances observées :

| Qui relit | Problème |
|---|---|
| Opus en direct, sur son propre code | il a écrit, il a le pourquoi en tête, il valide |
| Opus en direct, sur le code d'un agent délégué | il n'a pas le contexte de production, et doit le reconstituer — coût élevé, conclusions fragiles |
| Un agent ré-invoqué en mode « vérifie » | il hérite souvent du contexte qui a produit le code, et le biais rejoue |

L'absence d'un **vrai relecteur** coûte cher : un agent a déjà déclaré
*« section réparée »* alors qu'une capture montrait les titres toujours
coupés. Il avait corrigé une cause sur deux — parce qu'il **savait** qu'il
avait identifié deux causes, et son attention s'est relâchée sur la
seconde.

# Le mandat du relecteur

Un brief ré-utilisable, à passer tel quel :

> **MANDAT RELECTEUR.** Tu es un agent neuf. Tu n'as pas écrit le code
> ni participé à la décision. Tu lis les fichiers nommés ci-dessous et
> tu produis un rapport de relecture.
>
> Tu ne fais **rien d'autre** :
> - tu ne corriges pas, tu ne suggères pas de patch, tu n'écris pas ;
> - tu ne compiles pas, tu ne lances pas les tests, tu ne mesures rien ;
> - tu ne complètes pas le contexte que l'auteur n'a pas explicité.
>
> Ton livrable est une **liste de défauts**, structurée : chemin du
> fichier, ligne approximative, défaut observé, défaut attendu. Si tu
> ne trouves rien, écris *« néant »* — ne cherche pas à me convaincre
> que tout va bien.
>
> **Périmètre de lecture :** [liste explicite]
> **Périmètre exclu :** [le reste du dépôt]

# Les règles du mandat

- **Contexte vierge.** Le relecteur reçoit le strict minimum : périmètre
  de lecture, et l'énoncé du problème que le code est censé résoudre. Pas
  le brief qui a guidé l'écriture, pas le journal du travail, pas la
  liste des décisions.
- **Mandat unique.** Trouver ce qui casse. Pas ce qui peut être
  amélioré, pas ce qui suit la convention, pas ce qui gagnerait à être
  refactoré. Un relecteur qui élargit son mandat devient un consultant,
  et le coût de son rapport grimpe.
- **Liste, pas prose.** Format imposé : tableau ou liste à puces, une
  ligne par défaut. Le rapport en prose mélange des défauts graves et
  des chipotages, et l'auteur ne sait pas par où commencer.
- **Droit au néant.** *« néant »* est une réponse recevable. Mieux : un
  relecteur qui dit *« néant »* à un auteur connu pour ses cochages
  endormis a probablement mal cherché. Mais un relecteur qui force
  trois défauts pour faire sérieux est pire qu'un relecteur honnête.

# Vérification

Le test de Cherny, à passer par le relecteur lui-même : *« est-ce qu'un
ingénieur l'aurait fait comme ça ? »* Si la réponse est systématiquement
oui, le relecteur est complaisant. Si la réponse est systématiquement non,
il est de mauvaise foi.

# Coût

Une relecture sur un livrable de 200-400 lignes prend 5 à 15 minutes
selon la complexité. C'est le coût de la séparation. À comparer au coût
d'un défaut livré qui revient six semaines plus tard — toujours supérieur
d'un ordre de grandeur au moins.

# Pourquoi ne pas automatiser

Des outils de revue automatisée (lint, types, format) couvrent les
défauts **mécaniques**. Le relecteur couvre les défauts **sémantiques** :
le code fait ce qu'on voulait, l'API est utilisable, le bord inattendu
est traité. Ces défauts-là sont précisément ceux qu'un agent qui a écrit
le code ne voit pas.
