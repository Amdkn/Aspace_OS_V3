---
type: Architecture memory
title: Clara Design-of-Design — Fractal Software Factory
description: Reframes Clara from a sequential review slot into the compiler of interaction topology across orchestration patterns, SDLC phases, GitHub surfaces, memory, research and execution.
date: 2026-09-28
tags: [clara, design-of-design, fractal, software-factory, orchestration, sdlc, github, bill, graham, antigravity]
generated: { by: chatgpt-clara, at: 2026-09-28T12:20:00-04:00 }
okf_version: "0.2"
confidence: A0-directed-design
---

# Clara Design-of-Design — Fractal Software Factory

## Correction de rôle

Clara n'est pas un slot `Design -> Review` placé avant ou après Ryan.
Clara est la fonction **Design of Design** : elle compile la forme de collaboration qu'une mission doit prendre pour rester une seule A'Space.

Ryan BUILD, Bill RESEARCH, Graham STATE et Nardole DISPATCH ne forment pas une chaîne fixe.
Ils sont des capacités réentrantes qu'une mission peut invoquer plusieurs fois, en parallèle ou récursivement.

L'implémentation Antigravity `e0a342b3` prouve déjà `Rick -> Doctors -> Companions`, `send_message`, worktrees isolés et PDR.
La correction porte sur la dynamique d'interaction : la topologie d'orchestration doit être choisie par la mission et peut changer à chaque phase.## La Factory n'est pas un pipeline : c'est un espace de coordonnées

Chaque unité de travail est décrite simultanément par plusieurs axes, sans créer une nouvelle ontologie globale :

1. **Signal / Intent** — ce qui déclenche la mission.
2. **Cycle** — Discover, Design, Build, Test, Review, Ship, Monitor, Learn.
3. **Pattern d'orchestration** — Orchestrator-Worker, Pipeline, Swarm, Mesh, Hierarchical, ou hybride.
4. **Capability pole** — RESEARCH, DESIGN/FORGE, BUILD, OBSERVE, STATE, INTERFACE, PERSISTENCE, FLOW, DISPATCH.
5. **Scope** — action, PDR, issue, mission, projet, Core, World.
6. **Evidence state** — hypothesis, bounded, claimed, executing, verified, shipped, monitored, reopened.
7. **Memory/provenance** — sources, décisions, artefacts, tests, version du modèle/harness/policy.

La fractalité vient du fait qu'une cellule peut contenir une Factory plus petite.
Un `Build` peut utiliser un swarm de workers; un `Review` peut utiliser un mesh Clara/Yaz/Graham; un `Discover` peut lancer plusieurs Bill en parallèle; un `Ship` peut redevenir `Triage` si Monitor détecte un défaut.

## Pattern selector

Clara compile le **pattern de collaboration**, pas seulement la forme de l'artefact.

- Incertitude élevée / recherche large -> **Swarm Bill** puis convergence.
- Dépendances strictement ordonnées -> **Pipeline**.
- Sous-problèmes indépendants -> **Orchestrator-Worker** ou hiérarchie Doctor/Companions.
- Co-construction sur artefact partagé -> **Mesh**.
- Mission multi-Core -> **Hierarchical + Mesh transversal**.
- Production réelle -> hybride; aucun pattern n'est doctrine universelle.## Boucle de Design-of-Design

`Signal -> Recall -> Explore -> Compose -> Execute -> Verify -> Ship -> Observe -> Remember -> Recompose`

### Recall — Graham avant la solution
Avant de compiler une solution durable, Clara demande à Graham un paquet borné de mémoire/provenance :
- intention/source et historique pertinent;
- décisions/artefacts déjà produits;
- contraintes et échecs précédents;
- preuves récentes et versions de harness/policy.

Graham ne "donne pas la solution". Il rend le contexte rejouable.
Clara utilise ce contexte avec Bill pour éviter le rejeu et avec Ryan pour éviter de reconstruire ce qui existe.

### Explore — Bill comme système sensoriel R&D
Bill doit transformer les vidéos, papiers, repos et conférences en objets réutilisables au lieu de consommation épisodique.

Boucle Bill :
`URL/source -> transcript/metadata/keyframes/code refs -> claims/novelties/questions -> Discussion -> evidence refs -> design candidates`.

Réutiliser les capacités déjà présentes : transcript API, WATCH, yt-dlp, ffmpeg et les corpus de transcriptions existants.
Une source reste liée à son transcript, ses captures, son hash/provenance et ses hypothèses; aucun résumé ne remplace la source.

### Compose — Clara
Clara relie découvertes Bill + mémoire Graham + intention active.
Elle produit la topologie de mission : phases utiles, patterns imbriqués, capacités appelées, critères d'acceptation, boucles de retour et frontières de risque.### Execute — Ryan et les effecteurs
Ryan n'attend pas "la fin de Clara" comme un ticket suivant.
Dès qu'un sous-contrat est suffisamment borné et réversible, Ryan peut construire pendant que Bill/Clara continuent l'exploration ailleurs.
Jules ou d'autres workers peuvent être utilisés à l'intérieur du Build sans devenir la topologie globale.

### Verify / Observe
Yaz vérifie comportement et trajectoire; Clara vérifie cohérence du design; Graham vérifie état/provenance.
Ces vérifications peuvent être parallèles et provoquer une recomposition ciblée, pas un redémarrage complet.

### Dispatch / Ship — Nardole
Nardole ne "vient pas à la fin".
Il route les dépendances pendant toute la mission, matérialise les handoffs, réveille les capacités nécessaires et relie issue/discussion/PR/evidence.
Ship est un état de la boucle; Monitor peut réouvrir Triage.

## GitHub Top Bar comme organes d'une même Factory

- **Discussions** = divergence, signaux R&D, recherche, alternatives, décisions encore ouvertes.
- **Issues/Sub-issues** = unités exécutables bornées et récursives.
- **Projects** = projection de missions et de leurs coordonnées/états, jamais SSOT universel.
- **Actions** = middleware déterministe : validation, routing, evidence gates, automation.
- **PRs/Code** = propositions de mutation et histoire versionnée.
- **Wiki** = manuel de navigation et patterns réutilisables de la Forge.
- **Security** = système immunitaire / veto sur classes de mutations sensibles.

Discussion #185 est le premier bus vivant de ce modèle, pas le design complet de la Factory.## Antigravity : première implémentation et évolution attendue

Première matérialisation identifiée :
- commit `e0a342b3 feat(antigravity): materialize Council of Doctors and PDR runtime`;
- branche `feat/antigravity-council-of-doctors-2026-09-28`;
- draft PR #187;
- profils sous `.agents/agents/`;
- compétences `council-of-doctors`, `pdr-delegation`, `pdr-worker`, `jules-pdr-worker`;
- compiler `scripts/council_pdr.py`;
- runtime ensuite prouvé par `912b68d1`.

Ce runtime doit évoluer de "rôles qui se passent un PDR" vers "mission qui compose dynamiquement rôles + patterns + cycles".
La récursion native Antigravity est un moteur de cette composition, pas son modèle conceptuel unique.

## Invariant d'unicité

A'Space reste un seul système lorsque :
- chaque interaction conserve origin, provenance, acceptance et return-to;
- les mêmes capacités sont réutilisables à toutes les échelles;
- la mémoire de Graham précède les décisions durables et reçoit les preuves après exécution;
- Bill transforme le monde externe en signaux traçables;
- Clara compile la topologie de collaboration;
- Ryan matérialise;
- Yaz observe;
- Nardole maintient les connexions;
- Rick n'intervient que là où la mesh ne peut pas résoudre seule.

Le succès n'est pas "un beau lore cohérent".
Le succès est une idée externe qui entre par Bill, modifie un design Clara, devient un artefact Ryan, est vérifiée par Yaz, reliée par Nardole, mémorisée par Graham, puis réutilisée automatiquement dans une mission suivante.


## World federation application — Astra / Sol / Terra / Luna

Design-of-Design also compiles repository topology.

- Astra is the unified A'Space V3 world and registry/convergence surface.
- Sol is Agent OS, including the local Desktop on `127.0.0.1:5555`.
- Terra is Life OS 2026.
- Luna is not one repository: it is a federation of Business OS / The OMK Office repositories.

Local junctions and Codespaces symlinks are projections. They make worlds navigable together without pretending that independent Git histories are one filesystem or one release train.

Astra mounts Sol/Terra/Luna under `Worlds/`. The external sibling view is `C:/Users/amado/ASpace_Worlds/{Astra,Sol,Terra,Luna}`. Legacy `Agent_OS` and `Life_OS_2026` junctions remain compatibility aliases.
