---
type: Tradeoff
title: Rester natif (boucle.sh) — ce qu'on perd, ce qu'on garde
description: Inventaire honnête de ce que la décision « ne pas adopter LangChain/LangGraph/CrewAI/AutoGen » coûte, et de ce qu'elle préserve, pour que le choix soit tenu en connaissance de cause.
tags: [boucle-sh, langchain, langgraph, crewai, autogen, native, tradeoff]
generated: { by: minimax-m3, at: 2026-08-19T00:00:00Z }
verified:
  - { by: minimax-m3, at: 2026-08-19T00:00:00Z }
sources:
  - id: boucle-sh
    resource: "60_Implementation_Méthodologiques/_loop/boucle.sh"
    title: "Boucle d'implémentation native — rotation 10 paires, slots.sh, plafond 90 node"
    last_modified: 2026-08-19
  - id: etat-pulse
    resource: "70_Onthologies/pulse/ETAT.md"
    title: "ETAT.md — 6 concepts B1/B2/B3 sur 2 tours, 0 réécriture"
    last_modified: 2026-08-19
  - id: brief-frameworks
    resource: "60_Implementation_Méthodologiques/_loop/BRIEF_frameworks.md"
    title: "Brief — décision propriétaire de rester natif"
    last_modified: 2026-08-19
okf_version: "0.2"
---

> **Niveau de confiance : reconstruit.** L'inventaire des pertes est
> extrapolé de la pratique de la boucle (rotation, slots, plafond) et
> des features typiques des frameworks listés. Pas une comparaison
> benchmark.

# Cadrage

La décision du propriétaire du produit est **rester natif** :
parallélisme par extension de `_loop/boucle.sh`, pas LangChain ni aucun
framework d'orchestration. La boucle existe, tourne, 7 agents rendus,
0 échec mesuré, mémoire partagée (`ETAT.md`) qui compose d'un tour à
l'autre. Ce concept inventorie **ce qu'on perd** à rester natif pour que
le choix soit défendu en clarté, pas en ignorance.

# Ce qu'on garde en restant natif

1. **Lisibilité totale** — `boucle.sh` fait 84 lignes. Un nouvel agent
   peut le lire en 5 minutes. Un graphe LangGraph se lit en 30 minutes
   au mieux, et seulement après la doc du framework.
2. **Pas de dépendance npm au runtime** — `boucle.sh` n'a besoin que de
   bash, python (pour lire la clé API), et le binaire `claude`. Aucun
   risque de « la lib X a changé d'API en v0.4 ».
3. **Append-only natif** — `ETAT.md` est append-only par construction
   (le brief interdit la réécriture). Aucun framework n'impose cette
   discipline aussi strictement ; beaucoup la permettent.
4. **Coût minimal** — zéro coût de framework. Le coût est uniquement le
   LLM et le temps agent.
5. **Audit par le shell** — `git log`, `cat ETAT.md`, `ls frameworks/`
   suffisent à reconstituer l'état. Pas de tool propriétaire d'observabilité.
6. **Réversibilité** — supprimer `boucle.sh` ne casse rien d'autre.
   Adopter LangChain crée une dépendance qu'on ne voit plus après 6 mois.

# Ce qu'on perd en restant natif

1. **Pas de graphe d'état first-class**. LangGraph modélise des graphes
   cycliques avec état typé. Notre boucle est une **rotation linéaire**
   sur 10 paires. Un agent qui doit **revenir en arrière** sur un état
   passé (par exemple : reprendre un cycle interrompu) doit le faire à
   la main, dans le brief du tour suivant. Pas de primitive « checkpoint
   and rewind ».
2. **Pas de primitives de synchronisation riches**. CrewAI et AutoGen
   ont des primitives *speaking turn*, *group chat*, *consensus vote*,
   *broadcast*. Notre boucle se contente de *wait* après deux `lancer`
   en parallèle. Un vote entre 4 agents exige une étape externe —
   typiquement un concept B2 qui formule la décision.
3. **Pas de retry contextuel**. Si un agent échoue (exit ≠ 0), la boucle
   logue `tour $tour : $quoi tour $tour termine (exit=$code)` et passe
   au tour suivant. Pas de relance avec un brief amendé. LangChain a
   des `RetryPolicy` natives ; AutoGen a des `max_retries` par agent.
4. **Pas de tool registry partagé**. Chaque agent doit ré-importer ses
   outils. Un tool partagé (par exemple un cache de recherche corpus)
   doit être posé comme dépendance dans chaque brief. CrewAI a un
   shared tools registry.
5. **Pas d'observabilité native**. Pas de traces, pas de spans, pas de
   timeline. On a `BOUCLE.log` et `journal_<quoi>_t<n>.log` — du log
   brut, pas une trace structurée. LangSmith / LangChain trace est
   natif ; ici, c'est un rebuild si on en a besoin.
6. **Pas de conditional edges first-class**. Si le résultat d'un agent
   doit déclencher un autre agent (par exemple : B2 rejette → B1 reprend),
   c'est une **décision de tour** dans la rotation, pas une arête
   conditionnelle. LangGraph exprime ça en 3 lignes ; ici, ça demande
   un tour de boucle complet.
7. **Pas de state partagé typé**. `ETAT.md` est du markdown append-only.
   Pas de schéma. Pas de validation. Un agent qui écrit une ligne
   mal-formée casse la composition pour les autres. LangGraph a des
   `State` typés (TypedDict / Pydantic) qui rejettent à l'écriture.
8. **Pas de memory long-terme first-class**. La KB canonique
   (`40_Memory_Wiki_OKF`) est lue à chaque session par convention
   (cf. CLAUDE.md). Mais aucun framework ne force sa consultation —
   c'est une règle de poste, pas une garantie runtime. AutoGen et
   CrewAI ont des memory stores par agent qui peuvent être curés.
9. **Pas de scheduler intégré**. La boucle tourne tant que l'échéance
   n'est pas atteinte et qu'un jeton n'est pas libre. Pas de
   priorité entre jobs, pas de préemption, pas d'expression cron
   arbitraire. Un scheduler comme Temporal ou Airflow le fait nativement.
10. **Pas de gestion de concurrence au-delà de 2**. La boucle lance
    `deux` agents en parallèle (`lancer a &` puis `sleep 45` puis
    `lancer b &` puis `wait`). C'est délibéré (cf. CLAUDE.md §1 piège
    5 : le wrapper npm est un fichier unique que Windows verrouille).
    LangChain / CrewAI ne partagent pas cette contrainte — ils peuvent
    fan-out à N agents. **C'est une perte**, mais c'est aussi ce qui
    rend la boucle fiable.

# Ce qui est irremplaçable dans un framework

À ce jour, **rien n'est irremplaçable**. Les 10 pertes listées sont
couvrables par :
- (1, 2, 6, 9) : un brief bien écrit.
- (3) : un fichier `STOP` et un slot libéré — déjà en place.
- (4, 7) : un `index.md` lu par chaque brief — déjà en place.
- (5) : un `BOUCLE.log` et `journal_*.log` — déjà en place.
- (8) : le CLAUDE.md et le canon OKF — déjà en place.
- (10) : la borne de 2 est volontaire, pas un manque.

Aucune perte ne crée un blocage pour la production actuelle
(7 agents rendus, 0 échec). Le seul cas où un framework deviendrait
nécessaire : si la rotation 10-paires saturait et qu'on ait besoin d'un
fan-out plus large avec conditional edges. **Ce n'est pas le cas
aujourd'hui.**

# Ce qui rendrait le regret justifié dans 6 mois

1. **Saturation de la rotation 10-paires**. Si on doit servir 20 agents
   avec conditional edges, le bash `wait` ne suffit plus. Mais on est
   à 7 agents ; la marge est large.
3. **Coût d'observabilité**. Si un incident de tour exige 30 minutes
   de reconstruction à partir des logs bruts, c'est le signe qu'on
   a besoin d'un outil de trace. Mais aucun incident ne l'a encore
   justifié.
4. **Dette de relecture**. Si les briefs deviennent trop gros pour être
   lus en 5 minutes par un agent, un framework qui découpe en graphes
   devient tentant. Mais la discipline « brief en 1 page » tient
   depuis août.

# Décision de fait

**Rester natif.** Les pertes sont recensées, aucune n'est irremplaçable
aujourd'hui, aucune ne crée de blocage. La réversibilité est totale
(supprimer `boucle.sh` ne casse rien). Adopter un framework ajouterait
une dépendance sans supprimer une perte — c'est un coût net négatif.

Le jour où un framework deviendrait nécessaire, ce serait pour
**une** des trois raisons :
- Fan-out > 10 avec conditional edges
- Observabilité structurée (≥ 1 incident non reconstructible)
- Briefs ingérables (> 5 pages par brief)

Tant qu'aucune de ces trois raisons n'est mesurée, rester natif est
la décision la moins coûteuse.