---
type: Concept
title: CEO-BENCH et SpecLoop — ce que les sources disent vraiment
description: Le briefing D.E.A.L attribue aux deux dépôts des architectures qu'ils ne contiennent pas, et lit le résultat principal de CEO-BENCH à l'envers.
tags: [ceobench, specloop, deal, lights-out, verification, benchmark, b1-summers, confiance]
generated: { by: "claude-opus-5", at: "2026-08-22T22:40:00Z" }
verified:
  - { by: "claude-opus-5", at: "2026-08-22T22:40:00Z" }
sources:
  - id: ceobench-repo
    resource: "https://github.com/zlab-princeton/ceobench-src"
    title: "CEO-Bench: Can Agents Play the Long Game? — dépôt source"
    last_modified: 2026-08-22
  - id: ceobench-paper
    resource: "https://arxiv.org/abs/2606.18543"
    title: "CEO-Bench, Chen · Narasimhan · Liu (Princeton Z-Lab)"
    last_modified: 2026-08-22
  - id: specloop-repo
    resource: "https://github.com/dpolivaev/spec-loop"
    title: "spec-loop — framework of reusable skills"
    last_modified: 2026-08-22
  - id: briefing-deal
    resource: "Briefing Stratégique : Intégration CEO-BENCH, SpecLoop et Roadmap D.E.A.L"
    title: "Synthèse NotebookLM soumise à vérification"
    last_modified: 2026-08-22
okf_version: "0.2"
---

# CEO-BENCH et SpecLoop — ce que les sources disent vraiment

## L'erreur de catégorie

**CEO-BENCH est un banc d'essai, pas une méthode de management.** Il simule une
startup sur 500 jours ; l'agent dispose de 1 M$ de trésorerie initiale, de
34 outils et de 19 bases SQL. La métrique est le solde de trésorerie final.
Son objet est de **mesurer** des agents, pas de prescrire des disciplines.

**SpecLoop est un ensemble de compétences réutilisables** pour le développement
assisté, d'orientation *design-first* : « écrire la prochaine petite spec, la
relire, l'implémenter avec des tests. Garder la spec locale à l'étape
suivante. » Livré en paquets npm.

Traiter l'un comme un corpus de « Disciplines et Principes » et l'autre comme
une architecture de rôles est le même glissement que confondre un routeur avec
une source de quota : le nom est emprunté, le contenu est ailleurs.

## Ce que le briefing attribue, et ce qui existe

| Affirmation du briefing | Statut |
|---|---|
| CEO-BENCH définit **11 composants décisionnels** | **absent** du dépôt et de l'article |
| Rafraîchissement mémoire hebdomadaire, fichier de 150 lignes max (C1) | **absent** |
| Mémos à contingences, densité ≥5 `if-then` (C2) | **absent** |
| Forecast cash à 4 semaines, re-scoping si erreur >50 % (C3) | **absent** sous cette forme |
| Équation de cash quotidienne, bascule sous 2 mois de burn (C5) | **absent — et contredit**, voir ci-dessous |
| **90 % des dépenses de dev sur des segments nommés (C6/C7)** | **réel** — mesure de l'article |
| Discipline des turns (C10) | **absent** |
| SpecLoop : triade Générateur / Reconstructeur / Vérificateur (S1) | **absent** |
| SpecLoop : *information hiding*, exécuteur aveugle (S2) | **absent** |
| SpecLoop : taxonomie d'erreurs E.1 à E.4 (S3) | **absent** |
| SpecLoop : RR-Score, seuils 70 % et 95 % « franchisable » | **absent** |

Une affirmation sur onze est sourcée. C'est le même profil que le barème
d'affiliation 50/150/250 $ trouvé introuvable dans le corpus wonder-woman :
des chiffres précis, une nomenclature crédible, aucune origine.

## L'inversion la plus coûteuse

Le briefing prescrit (C5) :

> *« Si la trésorerie tombe sous 2 mois de burn, le système bascule
> mécaniquement en mode préservation. »*

L'article mesure l'inverse. Parmi ce qui **sépare les agents qui réussissent** :

> Opus 4.7 *« se limite à une stratégie passive, ce qui donne de mauvaises
> performances — précisément une stratégie passive de préservation de
> trésorerie »*, là où GPT-5.5 et Opus 4.8 explorent un large espace
> stratégique.

Le briefing érige donc en règle mécanique le comportement que le banc d'essai
identifie comme perdant. Ce n'est pas une nuance : c'est le signe inverse.

## Ce que CEO-BENCH dit du projet lights-out

Le résultat principal est un avertissement, pas un encouragement.

- **La plupart des agents font faillite** avant la fin des 500 jours.
- **Seuls Claude Opus 4.8 et GPT-5.5** terminent au-dessus du solde de départ et
  au-dessus d'une référence non-LLM à base de règles — et **même eux ne
  dégagent pas de profit de façon constante** d'une expérience à l'autre.
- **Un script à base de règles a battu la majorité des LLM de pointe.**
- Les meilleurs restent très loin de la borne théorique estimée à 2,2 Md$.

Et le point qui touche directement ce chantier :

> **Envelopper un modèle de tête dans un harnais de code réputé l'a rendu
> moins performant.**

Un harnais mal ajusté dégrade un bon modèle. Construire une couche
d'orchestration au-dessus de ces agents n'est donc pas neutre par défaut : il
faut mesurer que le harnais aide, sinon il nuit.

**Conclusion de portée.** CEO-BENCH est une preuve **contre** l'autonomie
lights-out en l'état, pas une base pour elle. L'invoquer comme fondation d'un
système sans intervention humaine, c'est lire son résultat à l'envers.

## Deux articles portent le nom CEO-Bench

Risque de confusion à connaître :

- **arXiv 2606.18543** — Princeton Z-Lab (Chen, Narasimhan, Liu) : simulation
  de startup sur 500 jours. C'est celui du dépôt `zlab-princeton/ceobench-src`.
- **arXiv 2606.17459** — MBZUAI/Yale : réallocation de ressources au niveau
  CEO avec quatre conseillers *C-suite* conditionnés par rôle. **Sans rapport.**

Une citation « CEO-Bench » sans numéro d'article ne désigne rien de précis.

## Ce qui reste utilisable

L'exercice n'invalide pas la démarche, il en corrige l'assise. Sont réellement
étayés par l'article, et transposables :

- **Concentrer les dépenses sur des segments nommés** plutôt que sur des
  améliorations génériques — 90 % contre 43 % sépare les forts des faibles.
- **Explorer activement** plutôt que préserver passivement.
- **Écrire du code pour prévoir** : les meilleurs modèles écrivent des scripts
  qui simulent le futur et déduisent l'information cachée.
- **La cohérence dans la durée** prime sur la capacité brute : intégrer les
  décisions, transformer les preuves accumulées en signaux actionnables.

Le reste — les onze composants numérotés, la triade SpecLoop, le RR-Score —
est une construction propre au briefing. Elle peut être bonne ; elle n'est pas
sourcée. La distinction est exactement celle que le format OKF existe pour
tenir : une affirmation mesurée et une affirmation supposée ne doivent jamais
se ressembler.

## Anti-pièges

- **Ne pas citer « CEO-BENCH » sans numéro d'arXiv.** Deux papiers homonymes.
- **Un banc d'essai ne prescrit rien.** Il classe. Transformer un classement en
  méthode demande une étape de conception qui doit être assumée comme telle.
- **Vérifier le signe avant de reprendre une règle.** La bascule en mode
  préservation a été reprise avec le signe inverse de la mesure d'origine.
