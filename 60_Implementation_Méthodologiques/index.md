---
type: Bundle index
title: 60_Implementation_Méthodologiques — les méthodes qu'on applique, et pourquoi
description: Principes tirés de sources externes datées et transcrites, convertis en pratiques appliquées à ce poste. Deux entrées fondatrices — l'ingénierie du prompt système, et l'échelle d'autonomie des agents.
tags: [methode, prompt-engineering, autonomie, agents, okf]
generated: { by: claude-opus-5, at: 2026-08-17T21:00:00Z }
verified:
  - { by: process:transcript-api, at: 2026-08-17T20:55:00Z }
sources:
  - id: indydevdan-prompt
    resource: https://youtu.be/S_QdQ1G4GlU
    title: "IndyDevDan — FIXING Opus 5: PROOF that Prompt Engineering IS NOT DEAD"
    last_modified: 2026-08-17
  - id: ia-strategie-autonomie
    resource: https://youtu.be/8ZJI4uCp6bA
    title: "IA et Stratégie — Vos agents travaillent seuls. Alors pourquoi êtes-vous encore devant l'écran ?"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Ce que ce bundle contient

Des **méthodes**, pas des opinions. Chaque page part d'une source datée et
transcrite, et se termine par ce qui change concrètement sur ce poste.

Une méthode qu'on ne peut pas rattacher à une source ni traduire en geste n'a
rien à faire ici. C'est ce qui la distingue d'un résumé de vidéo.

# Les deux entrées fondatrices

| Source | Thèse | Ce qu'elle commande |
|---|---|---|
| IndyDevDan | le **prompt système** est démultiplié sur chaque tâche ; le prompt utilisateur ne l'est pas | écrire le contrat à la main, une fois, plutôt que le répéter à chaque session |
| IA et Stratégie | le goulot n'est **jamais la motivation**, c'est la boucle de vérification qui n'existe pas | construire l'examen avant d'augmenter le nombre d'agents |

# Ce qu'elles disent ensemble

Les deux vidéos ne parlent pas du même sujet — l'une de rédaction, l'autre
d'organisation — et arrivent au même endroit : **le levier n'est pas dans la
demande, il est dans le cadre posé une fois pour toutes.**

IndyDevDan l'écrit dans le prompt système : « chaque mot que vous y écrivez est
multiplié sur chaque prompt utilisateur ». IA et Stratégie l'écrit dans le
`CLAUDE.md` : « tout ce que vous répétez à l'oral, session après session, doit
redescendre dans ce fichier ».

C'est la même opération, vue depuis deux métiers. Et elle se vérifie ici : le
canon de ce poste existe précisément parce que cinq pièges d'invocation ont été
payés une fois chacun, puis écrits.

# La contradiction utile entre les deux

IndyDevDan optimise la **qualité d'une réponse** : moins de verbosité, des
points de référence, des bornes opérationnelles.

IA et Stratégie optimise la **quantité de travail délégué** : plus d'agents,
moins de surveillance.

**Les deux ne tirent pas dans le même sens.** Un prompt système très contraint
coûte du temps à écrire et ralentit la mise en route ; un essaim lancé vite
produit plus, moins bien. Le canon les réconcilie par une règle simple : *plus
un artefact est multiplicatif, plus on ralentit pour l'écrire à la main.*
Un brief lancé sur quatre agents mérite qu'on y passe une heure. Une commande
jetable, non.

# Files

*Les concepts arrivent par distillation déléguée. Voir [_briefs](_briefs/).*

# Directories

- [_sources](_sources/) - Les transcriptions intégrales, telles que récupérées, avec leur date.
- [_briefs](_briefs/) - Le brief de conversion des transcriptions en concepts OKF.
- [prompt-systeme](prompt-systeme/) - Ce qui relève de la rédaction du cadre.
- [autonomie-agents](autonomie-agents/) - Ce qui relève de l'échelle de délégation et de la vérification.
