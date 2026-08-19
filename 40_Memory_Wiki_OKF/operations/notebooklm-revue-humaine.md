---
type: Playbook
title: NotebookLM en assistance de revue humaine — quand la production n'est plus le goulot
description: Regrouper les concepts en 26 sources chargeables, et pourquoi la revue est devenue le point de blocage après 423 fichiers produits en une nuit.
tags: [notebooklm, gemini-notebook, revue, verification, okf, confiance, goulot]
generated: { by: claude-opus-5, at: 2026-08-18T08:00:00Z }
verified:
  - { by: process:consolider-pour-review, at: 2026-08-18T07:55:00Z }
  - { by: human:amdkn, at: 2026-08-18T07:50:00Z }
sources:
  - id: mesure-production
    resource: "comptage des .md produits en deux vagues — 70_Onthologies/pulse, 60_Implementation_Méthodologiques, 50_Distillation"
    author: process:consolider-pour-review
    last_modified: 2026-08-18
  - id: decision
    resource: "arbitrage utilisateur — « bienvenue dans le goulot de la review », NotebookLM comme assistance"
    author: human:amdkn
    last_modified: 2026-08-18
okf_version: "0.2"
---

> **Niveau de confiance : revu par un humain.** Le choix de l'outil et la
> qualification du goulot sont des décisions du propriétaire du produit ; les
> volumes viennent d'un comptage réel.

# Le constat qui rend ce playbook nécessaire

En une nuit, deux vagues d'agents ont produit **423 fichiers `.md`**, dont
**321 concepts OKF**, avec zéro échec sur 60 lancements.

**Aucun n'a été relu par un humain.** Tous portent `confiance: machine`.

La production n'est plus le goulot — elle a probablement cessé de l'être dès
le premier tour. **Le goulot est la vérification**, et il ne se résout pas en
produisant davantage.

# Pourquoi 423 fichiers ne s'uploadent pas

NotebookLM — renommé **Gemini Notebook** par Google — plafonne à **50 sources
par carnet en gratuit, 300 en Plus**. Charger le corpus tel quel est
impossible.

`scripts/consolider_pour_review.py` regroupe donc par bundle : **26 sources**
dans `_REVIEW_NOTEBOOKLM/`, 4,8 Mo.

## Ce que la consolidation préserve, et pourquoi

Chaque concept garde son **chemin d'origine**. Sans lui, un verdict de revue
serait inapplicable : le podcast dirait *« le concept sur les vetos est faux »*
sans qu'on sache lequel des trente corriger.

Il garde aussi son **niveau de confiance**, puisque c'est exactement ce que la
revue doit faire évoluer — de `machine` à `humain`.

## Ce qu'elle retire

Le frontmatter YAML brut : illisible à l'oral, sans valeur pour un relecteur.
Remplacé par deux lignes en prose.

# Pourquoi NotebookLM plutôt qu'un agent relecteur

Un agent qui relit des concepts produits par des agents reste dans la même
boucle. Il peut vérifier la forme — sources existantes, liens valides — et
c'est déjà fait par les validateurs.

**Ce qu'il ne peut pas faire, c'est décider si une affirmation est vraie pour
ce produit-là.** NotebookLM ne le peut pas non plus, mais il change le **coût
d'accès** de l'humain au corpus : un podcast de vingt minutes s'écoute en
marchant, une carte mentale se lit d'un coup d'œil.

C'est un déplacement du goulot vers un endroit où l'humain peut effectivement
se tenir — pas une suppression du goulot.

# Par où commencer la revue

1. **`50-rapports-agents.md`** — ce que les agents disent d'eux-mêmes :
   couverture réelle, ce qu'ils n'ont pas couvert, contradictions non
   tranchées. **La source la plus rentable pour une critique**, parce qu'elle
   contient déjà les aveux.
2. **`60-memoire-etat-domaines.md`** — 42 tours des huit escouades, résumés
   ligne par ligne.
3. Les domaines et étages, selon ce qu'il y a à arbitrer.

## Les questions à poser au chat

- Quelles affirmations reposent sur une **seule** source ?
- Où deux concepts se contredisent-ils sans que personne ne l'ait signalé ?
- Quelles décisions sont présentées comme acquises alors qu'aucun humain ne
  les a tranchées ?
- Qu'est-ce qui **manque**, que le corpus aurait dû contenir ?

# L'état de l'intégration, sans enjoliver

**NotebookLM n'a ni MCP ni API publique.** Le transfert est manuel : upload
depuis `_REVIEW_NOTEBOOKLM/`, ou via un flux N8N qui lit le dossier.

Une piste d'accès depuis Claude Code par **cookies de session** a déjà
fonctionné une fois sur ce poste. Elle n'est pas documentée ici parce qu'elle
n'a pas été reproduite — et une méthode qui a marché une fois n'est pas une
méthode.

# La règle qui ne se délègue pas

**Rien ne passe de `confiance: machine` à `confiance: humain` sans le
propriétaire du produit.**

C'est le seul verrou qu'aucun script ne peut poser à sa place, et c'est celui
qui fait la différence entre 321 concepts et 321 concepts *vrais*.

# Régénérer le dossier

```bash
python "C:/Users/amado/ASpace_OS_V3/scripts/consolider_pour_review.py"
```

Il écrase `_REVIEW_NOTEBOOKLM/` : c'est voulu, la source de vérité reste les
concepts eux-mêmes.
