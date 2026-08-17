---
type: Reference
title: L'échelle d'autonomie — le goulot n'est jamais la motivation
description: Extraction de la vidéo « Vos agents travaillent seuls » — les cinq étapes de Boris Cherny, les quatre chantiers du passage 1→2, et les chiffres qui disent que les équipes abandonnent la vérification au lieu de la construire.
tags: [autonomie, agents, verification, delegation, cherny, goodhart]
generated: { by: claude-opus-5, at: 2026-08-17T21:10:00Z }
verified:
  - { by: process:transcript-api, at: 2026-08-17T20:57:00Z }
sources:
  - id: video
    resource: https://youtu.be/8ZJI4uCp6bA
    title: "IA et Stratégie — Vos agents travaillent seuls. Alors pourquoi êtes-vous encore devant l'écran ?"
    last_modified: 2026-08-17
okf_version: "0.2"
---

> **Ceci est une extraction, pas le verbatim.** Les chiffres cités viennent de
> la vidéo, qui les attribue à ses propres sources (Cherny, Microsoft, METR,
> une télémétrie sur 22 000 développeurs, Ramp). **Ils n'ont pas été vérifiés à
> la source ici** — c'est pourquoi ce document reste au niveau « confirmé par
> machine » pour la transcription, et non pour les faits qu'elle rapporte.

# L'échelle, en cinq étapes

| Étape | Situation | Le goulot |
|---|---|---|
| 0 | l'accès est verrouillé, l'outil acheté ne sort pas des approbations | le processus |
| 1 | un ingénieur, un agent, tout supervisé | **votre attention** |
| 2 | une dizaine d'agents en parallèle, chacun dans son bac à sable ; on relit les résultats | **le débit de revue** |
| 3 | une centaine d'agents ; plus personne ne relit ligne à ligne | la confiance dans la boucle |
| 4 | le millier ; pilotage par intention | — |

Microsoft a publié sa propre version de la même montée, tirée de sa télémétrie :
auteur, éditeur, directeur, orchestrateur. **Deux concurrents décrivant la même
progression depuis leurs propres données, ça cesse d'être une opinion.**

# La phrase qui porte tout

**Le goulot n'est jamais la motivation.** À chaque étage, ce qui bloque est un
système de vérification qui n'existe pas encore.

L'image : le moniteur d'auto-école, pied au-dessus du double frein. Il ne lâche
pas le frein le jour où il devient courageux — il le lâche le jour où l'élève
sait conduire.

# Les chiffres, et ce qu'ils racontent ensemble

- **METR** : l'étude qui mesurait les développeurs 19 % *plus lents* avec l'IA a
  été révisée sur la même cohorte à ~**+18 %**. L'explication tenue par le labo
  tient en un mot : l'**apprentissage**. La première année coûte, la suivante
  paie.
- **Télémétrie sur 22 000 développeurs** : le temps médian en revue de code a
  bondi de **+441 %** en un an, et **31 % de fusions supplémentaires se font
  sans aucune revue**.
- **Ramp** : l'entreprise médiane dépense **11 $ par employé et par mois** en IA.
  Le haut du panier, plusieurs milliers.

Les deux chiffres du milieu se lisent **ensemble**, et c'est là qu'est
l'enseignement : *les équipes ne montent pas en capacité de vérification, elles
abandonnent la vérification.* Le moniteur ne forme pas l'élève — il descend de
la voiture en laissant le moteur tourner.

# Les quatre chantiers du passage 1 → 2

1. **Le contrat.** Le fichier lu à chaque session (`CLAUDE.md`, `AGENTS.md`).
   *Tout ce qu'on répète à l'oral, session après session, doit y redescendre.*
   Tant qu'une consigne reste orale, l'agent l'oubliera à la session suivante.
2. **L'examen.** Une **commande unique** que l'agent lance lui-même **avant** de
   montrer quoi que ce soit : tests, compilation, linter, et un test bout-en-bout
   si c'est de l'interface. La règle : *l'agent n'a pas le droit de présenter un
   travail qu'il n'a pas déjà vérifié.*
3. **Les bacs à sable.** Une copie de travail isolée par chantier (`git
   worktree`), pour que deux agents ne se marchent jamais dessus. Plus une liste
   de commandes sûres autorisées une fois pour toutes — **en gardant
   l'approbation manuelle pour le réseau, les secrets et les suppressions.**
   Commencer à **deux** agents, pas dix.
4. **La relecture.** Un agent neuf, qui n'a pas écrit le code, avec un seul
   mandat : trouver ce qui casse. *Le fabricant ne se juge jamais lui-même.*

Ce qui change n'est pas le niveau d'exigence — **il ne bouge pas d'un
millimètre**. Ce qui change, c'est le moment où l'on intervient : à la fin, sur
des résultats, plus jamais pendant, plus jamais sur des frappes.

# Les deux tests de montée

- **Le test de Cherny** : « est-ce qu'un ingénieur l'aurait fait comme ça ? »
- **Le test physique** : lancer deux chantiers, fermer l'écran, partir deux
  heures. *Si l'idée est insupportable, c'est la boucle de vérification qu'il
  faut renforcer, pas votre tolérance au risque.*

# Le piège, contre-intuitif

Ce n'est pas de rester trop prudent. **C'est d'augmenter le nombre d'agents
avant que la boucle ait mérité la confiance.** Le travail sort plus vite, la
qualité s'effondre en silence, et la facture revient quelques mois plus tard.

# Goodhart, et le compteur de jetons

Une jauge indicative : sous 1 M de jetons par mois on discute avec un chat ;
~10 M, on est à l'étape 1 ; ~100 M, étape 2 ; le milliard, une usine.

Mais **une mesure qui devient un objectif cesse d'être une bonne mesure.**
Mesurer les jetons brûlés donnera des jetons brûlés. Le retour sur
investissement se calcule en divisant la sortie par l'entrée — **les jetons sont
l'entrée.** La jauge situe une pratique ; elle ne la note pas.

# Les trois questions pour situer une équipe

1. Combien d'agents tournent en parallèle un jour normal, et dans quoi sont-ils
   isolés ?
2. Montrez-moi la boucle de vérification — ce qui tourne **sans qu'un humain la
   déclenche**.
3. Qui relit le livrable final, et selon quel standard ?

Une organisation à l'étape 0 répond le nom de sa licence. Une organisation à
l'étape 2 répond une chaîne d'outils avec des noms de commande.

# Ce que ça change ici

Mesuré contre les quatre chantiers, ce poste est **à l'étape 2 sur trois
chantiers et à l'étape 1 sur un** :

| Chantier | État |
|---|---|
| Le contrat | **fait** — deux `CLAUDE.md`, et les pièges y redescendent à mesure |
| L'examen | **partiel** — `vitest`, deux `tsc`, `oxlint` existent, mais **aucune commande unique** ne les enchaîne, et rien n'oblige l'agent à la lancer avant de présenter |
| Les bacs à sable | **partiel** — périmètres d'écriture disjoints par brief, mais pas de `git worktree` ; le cloisonnement tient à la discipline du brief, pas à l'outil |
| La relecture | **absent** — aucun agent relecteur neuf ; c'est Opus qui relit, et il a parfois écrit |

Le chantier le plus rentable est donc **l'examen** : une commande unique,
et l'obligation faite à l'agent de la lancer avant de rendre.
