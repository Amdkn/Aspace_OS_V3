---
type: Concept
title: Goodhart et le compteur de jetons — la jauge situe, elle ne note pas
description: Anti-piège Goodhart appliqué à la doctrine d'économie de quota : une mesure qui devient un objectif cesse d'être une bonne mesure. Les jetons sont l'entrée du retour sur investissement, pas la sortie.
tags: [autonomie, goodhart, jetons, mesure, quota]
generated: { by: minimax-m3, at: 2026-08-17T22:50:00Z }
verified:
  - { by: process:lecture-fichiers, at: 2026-08-17T22:50:00Z }
sources:
  - id: ia-strategie-autonomie
    resource: 60_Implementation_Méthodologiques/_sources/echelle-autonomie-agents.md
    title: "IA et Stratégie — extraction"
    last_modified: 2026-08-17
  - id: canon-d6
    resource: C:/Users/amado/CLAUDE.md
    title: "Canon du poste — section §1 économie de quotas"
    last_modified: 2026-08-15
okf_version: "0.2"
---

# Le principe

*« Une mesure qui devient un objectif cesse d'être une bonne mesure. »* La
loi de Goodhart, formulée par l'économiste Charles Goodhart en 1975, et
reformulée plus tard : *« Quand une mesure devient un objectif, elle cesse
d'être une bonne mesure. »*

La vidéo applique ce principe au compteur de jetons. Une jauge indicative :

| Jetons consommés / mois | Étape |
|---|---|
| < 1 M | on discute avec un chat |
| ~ 10 M | étape 1 |
| ~ 100 M | étape 2 |
| ~ 1 Mds | une usine |

Mais : *« Mesurer les jetons brûlés donnera des jetons brûlés. »* Le
retour sur investissement se calcule en divisant la sortie par l'entrée.
**Les jetons sont l'entrée.** La jauge situe une pratique, elle ne la
note pas.

# L'écart mesuré

Le poste a déjà une doctrine d'économie de quota, codifiée dans la section
§1 du canon racine :

> *« Les quotas des modèles Anthropic sont la ressource rare. Tout
> travail long, répétitif ou volumineux se délègue au CLI Claude Code sur
> MiniMax-M3, qui ne consomme pas ces quotas. »*

La doctrine est **utile** — elle canalise le travail. Mais elle expose
**exactement** le travers identifié par la vidéo : une fois que la doctrine
est posée, l'agent et l'utilisateur peuvent confondre « brûlé moins de
jetons » avec « bien travaillé ».

# Les trois formes de perversion que la doctrine peut prendre

1. **Le micro-jeton.** Un agent qui coupe ses réponses en cinquante
   phrases d'une ligne pour économiser du quota produit un texte
   fragmentaire, illisible, où la cohérence des idées se perd. La
   verbosité de liaison est parfois nécessaire — la supprimer est une
   perte, pas un gain.
2. **La sous-traitance aveugle.** Déléguer à M3 pour déléguer, sans
   regarder si la tâche mérite la chaîne Workflow + brief + relecture.
   La délégation a un coût (rédaction du brief, vérification du rendu)
   qui dépasse souvent le coût direct d'exécution.
3. **Le court-termisme.** Mesurer « ce mois-ci, j'ai brûlé moins » sans
   regarder « ce que j'ai produit qui n'aurait pas existé sans cette
   dépense ». Une doctrine d'économie qui détruit la production n'est
   pas une économie.

# La règle de garde-fou

Le retour sur investissement, dans ce poste, se mesure en **concepts
publiés et durables** — pas en jetons. Un concept qui pose une
connaissance réutilisable pèse plus qu'une exécution qui n'a pas laissé
de trace.

Trois questions, à se poser quand une doctrine d'économie semble justifier
une dépense :

1. **Est-ce que le livrable restera dans six mois ?** Un commit jeté
   n'a pas de ROI ; un concept dans un bundle en a.
2. **Est-ce que le livrable aurait existé sans la dépense ?** Si oui,
   la dépense est superflue ; si non, c'est une création de valeur.
3. **Quel est le coût de ne pas le faire ?** Une réponse lente qui
   manque une fenêtre de déploiement coûte plus cher qu'une réponse
   rapide.

# La bonne posture

La doctrine d'économie est **un filtre**, pas un but. Elle s'applique :

- ✅ à la rédaction de briefs jetables (commande `claude -p` sans
  suite) ;
- ✅ à la sélection du modèle pour une tâche (rotation vers un modèle
  plus petit si la tâche le permet) ;
- ✅ à la mémoïre de répéter les consignes au long d'une session.

Elle ne s'applique pas :

- ❌ à la qualité d'un livrable (un concept net est plus économe en
  relectures qu'un concept flou) ;
- ❌ au canon du poste (la règle de multiplicativité s'oppose à
  l'économie sur les artefacts récurrents) ;
- ❌ à la documentation vivante (couper les commentaires pour
  économiser du quota dégrade la qualité).

# Vérification

Le test qu'on peut faire sur soi-même : à la fin d'une session, lister
**les trois livrables** principaux, et pour chacun, citer le coût en
jetons et la valeur estimée. Si la majorité des livrables *« ne vaut
pas le coup »*, la doctrine a dérapé. Si la majorité *« vaut le coup »*,
elle a tenu.

Une session qui produit un seul concept durable et consomme 100 000
jetons est **meilleure** qu'une session qui produit dix micro-tâches et
consomme 30 000 jetons. Le compteur ne dit pas ça.

# Risque résiduel

La posture « les jetons sont l'entrée » est simple à dire, difficile à
tenir quand le quota fond. La tentation de couper à la hache est réelle.
Le garde-fou externe : tenir un journal de session qui note, en une
ligne, le livrable principal et son coût — sans le rendre, le coût
devient invisible, et la doctrine devient auto-justification.
