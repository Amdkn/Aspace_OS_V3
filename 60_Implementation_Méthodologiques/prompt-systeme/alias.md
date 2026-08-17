---
type: Concept
title: Alias — raccourcis que l'agent développe comme s'ils étaient écrits
description: Section 5 du prompt système : trois ou quatre raccourcis déclenchant un comportement nommé, qui valent autant de phrases en termes de coût de token et de précision d'intention.
tags: [prompt-systeme, alias, raccourcis, tokens]
generated: { by: minimax-m3, at: 2026-08-17T22:20:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T22:20:00Z }
sources:
  - id: indydevdan-extraction
    resource: 60_Implementation_Méthodologiques/_sources/indydevdan-prompt-systeme.md
    title: "IndyDevDan — extraction"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Le principe

IndyDevDan : *« Des raccourcis que l'agent développe comme s'ils avaient été
écrits en entier — et qu'il ignore s'ils apparaissent dans une chaîne plus
longue. »* Quatre alias dans la source :

| alias | expansion |
|---|---|
| `scr` | simplifie, compresse, et redis ta réponse |
| `eli` | explique comme si j'avais 18 ans ; simplifie et raccourcis |
| `focus` | concentre-toi sur ce qui compte le plus ; quel est le vrai signal |
| `ref` | réécris ta réponse avec des points de référence |

L'économie est double : en **tokens** (l'alias tient en quelques caractères,
l'expansion en dix fois plus), et en **intention** (l'utilisateur n'a pas
à rédiger une consigne qui se perd dans les nuances).

# L'écart mesuré

Ce poste n'a **aucun alias** déclaré. Les consignes du type « sois concis »,
« va à l'essentiel », « écris comme pour un junior » sont répétées en clair
à chaque brief qui les demande. Le coût est modeste pour un brief long ;
il devient prohibitif pour les micro-ajustements en cours de session, où
l'utilisateur doit choisir entre rédiger une phrase de dix mots et accepter
la réponse verbeuse.

L'écart est d'autant plus net que le canon a déjà une mécanique analogue
sans la nommer : la combinaison `DATA + HEURISTIQUE + PRINCIPE` dans le
canon joue le même rôle qu'un alias — une forme condensée qui vaut consigne.
La convention existe, le vocabulaire manque.

# Les alias à poser dans ce canon

Quatre alias, choisis sur la fréquence d'usage observée et la difficulté à
les rédiger en clair :

| alias | expansion | Quand l'utiliser |
|---|---|---|
| `scr` | Reprends ta réponse précédente ; trois fois plus court, zéro perte d'information. | après une réponse trop longue, ou quand on veut une version compactable |
| `okf` | Reformule selon le format OKF v0.2 : frontmatter complet, `verified` non vide, sources citables. | tout concept nouveau à verser dans un bundle |
| `bor` | Reprends ta réponse ; présente uniquement les bornes opérationnelles (périmètre, interdits, livrable). | quand on veut la liste de ce qui est tenu et de ce qui ne l'est pas |
| `rec` | Lance un agent relecteur sur ce fichier : mandat unique, trouver ce qui casse. Voir `agent-relecteur-mandat.md`. | après une passe d'écriture longue, avant de rendre |

# Les règles d'usage

- L'alias **ne s'emploie que comme instruction isolée**, jamais嵌入 dans
  une phrase. *« scr cette partie »* ne déclenche rien d'attendu. *« scr »*
  seul, oui.
- L'alias **n'est pas développé dans la réponse** : l'agent applique
  l'expansion, l'utilisateur ne voit que le résultat.
- L'alias **n'apparaît jamais dans le livrable** : un commit, un brief,
  un concept — pas d'alias. C'est une convention de session.
- Si l'alias n'est pas reconnu, l'agent **demande** avant d'agir. Pas
  d'invention silencieuse.

# Le geste

Ajouter au canon une section **« Alias »** à quatre entrées. Convention :
table à deux colonnes (alias, expansion), suivie d'un paragraphe court
donnant les quatre règles d'usage ci-dessus.

Vérifiable : à la prochaine session longue, compter les occurrences de
« sois concis » rédigées en clair. Viser une bascule vers l'alias `scr`
dans 50 % des cas au bout d'un mois.

# Pourquoi ne pas en avoir plus

Quatre est un **plafond**, pas un plancher. Au-delà, l'agent doit retenir
trop de conventions pour un gain marginal. La règle qui protège : un
alias ne s'ajoute que si la consigne en clair a été rédigée **au moins
cinq fois** en deux mois. Si la consigne n'est pas fréquente, elle
mérite d'être en clair, pas en raccourci.
