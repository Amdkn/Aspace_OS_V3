---
type: Reference
title: IndyDevDan — le prompt système est le vrai levier
description: Extraction structurée de la vidéo « FIXING Opus 5 » — les six sections d'un prompt système, et la raison pour laquelle il pèse plus que le prompt utilisateur.
tags: [prompt-engineering, systeme, opus-5, indydevdan]
generated: { by: claude-opus-5, at: 2026-08-17T21:05:00Z }
verified:
  - { by: process:transcript-api, at: 2026-08-17T20:55:00Z }
sources:
  - id: video
    resource: https://youtu.be/S_QdQ1G4GlU
    title: "IndyDevDan — FIXING Opus 5: PROOF that Prompt Engineering IS NOT DEAD"
    last_modified: 2026-08-17
okf_version: "0.2"
---

> **Ceci est une extraction, pas le verbatim.** La transcription intégrale a été
> récupérée par `transcript-api` le 2026-08-17 ; ce document en tire la
> structure et les formulations qui commandent une action. Pour la lettre
> exacte, la source est la vidéo.

# La thèse

Il y a deux endroits où l'on peut écrire à un agent :

| | portée |
|---|---|
| **prompt utilisateur** | la tâche du moment |
| **prompt système** | la loi de **chaque** tâche |

*« Chaque mot que vous écrivez dans le prompt système est multiplié sur chaque
prompt utilisateur. »* La plupart des ingénieurs ne touchent jamais le second,
et se privent donc du seul levier qui compose.

L'argument contre « le prompt engineering est mort » : les fournisseurs ont
raccourci leurs prompts système parce que les modèles se débrouillent seuls sur
le cas général. **Ce n'est pas un signal de ne pas en écrire** — c'est un signal
que le cas général est couvert, et que tout ce qui vous est propre reste à
écrire.

# Les six sections

## 1. Purpose — et surtout le *pourquoi*

On pose la relation, pas un rôle. *« Toi et moi, on entretient une relation
claire, concise, actionnable, sans baratin. »* Puis on **explique pourquoi** :
pour livrer le meilleur résultat possible à l'équipe, à l'entreprise, aux
clients.

Donner la raison, pas seulement la règle — une règle sans sa raison ne se
généralise pas aux cas non prévus.

## 2. Patterns positifs et négatifs

Deux listes explicites : *reproduis ceci*, *évite cela*.

Positifs retenus :
- **« Je vois toujours en premier la dernière chose que tu écris. Mets-y
  l'information la plus importante. »**
- une langue simple et spécifique ; chaque fait énoncé **une seule fois** ;
- le niveau de détail suit le niveau de la demande ;
- contredire une hypothèse fausse **directement, en expliquant pourquoi** ;
- optimiser pour la clarté et la valeur d'ingénierie, **pas pour la citation** ;
- si une idée tient en un paragraphe plutôt que deux sans perdre d'information,
  la dire en un.

Négatifs retenus : la liste de tics du modèle (`loadbearing`, `worth stating
plainly`, `here's the honest truth`…), pas d'analogies, pas d'abus de tirets
cadratins, **pas de flatterie ni d'approbation sans raison**, pas de titres
décoratifs ni d'emoji.

## 3. Points de référence

Assigner des codes courts aux éléments énumérés : `D1…Dn` pour les décisions,
`R1…Rn` pour les risques, `F1…Fn` pour les constats. Les conserver dans toute la
conversation ; ne pas en créer pour une réponse courte.

L'effet est immédiat : on répond « parle-moi de R6 » et l'agent sait de quoi il
s'agit. **On fabrique un langage commun en une ligne de prompt système**, et
l'agent cesse de se répéter pour se faire comprendre.

## 4. Bornes opérationnelles dures

Le défaut visé : le modèle fait ce qu'on ne lui a pas demandé.

- livrer **uniquement** ce qui est demandé, au périmètre demandé ;
- ne pas élargir en nettoyage, remaniement, documentation ou fonctionnalité
  adjacente ;
- ne pas spéculer sur des besoins futurs ;
- **ne pas déclarer terminé sans preuve** ;
- ne pas ajouter de co-auteur à un message de commit ;
- redire brièvement ce qui a été fait, sans recharger la réponse de détail.

## 5. Alias

Des raccourcis que l'agent développe comme s'ils avaient été écrits en entier —
et qu'il ignore s'ils apparaissent dans une chaîne plus longue :

| alias | expansion |
|---|---|
| `scr` | simplifie, compresse, et redis ta réponse |
| `eli` | explique comme si j'avais 18 ans ; simplifie et raccourcis |
| `focus` | concentre-toi sur ce qui compte le plus ; quel est le vrai signal |
| `ref` | réécris ta réponse avec des points de référence |

## 6. Exemples — la distillation en contexte

Des paires *voici comment on communique* / *voici comment on ne communique pas*,
avec de vraies réponses.

L'astuce avancée : prendre une réponse d'un **autre modèle** qu'on trouve bonne,
la nettoyer à la main, et la poser en exemple. C'est de la distillation en
contexte — la technique est antérieure à GPT-4 et fonctionne toujours.

# La règle qui vaut au-delà de la vidéo

*« Plus la chose sur laquelle vous travaillez est multiplicative pour le reste
de votre travail, plus vous devez ralentir. »*

Écrire à la main, ne pas dicter, ne pas improviser. Un artefact appliqué à mille
exécutions mérite une heure ; une commande jetable, non.

# Ce que ça change ici

Ce poste a déjà un canon (`~/.claude/CLAUDE.md` et `C:/Users/amado/CLAUDE.md`)
qui joue le rôle du prompt système. Ce qui manque, mesuré contre la grille
ci-dessus :

| Section | État sur ce poste |
|---|---|
| Purpose avec le *pourquoi* | présent — chaque règle du canon porte le piège qu'elle évite |
| Patterns positifs / négatifs | **absent** en tant que section explicite |
| Points de référence (`D1`, `R1`) | **absent** |
| Bornes opérationnelles | partiel — les interdits existent, dispersés |
| Alias | **absent** |
| Exemples | **absent** |

Quatre sections sur six manquent. C'est le chantier.
