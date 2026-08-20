---
type: Concept
title: B2 Council — qui tranche quand deux domaines se contredisent
description: Le B2 Direction Council est l'instance d'arbitrage mésoperpétuelle d'A'Space OS. Huit capitaines en cercle, trois modes de coopération (parallel/handoff/negotiation), escalation à B1 uniquement si la wheel 8-domain ne tient plus dans North Star.
tags: [b2, council, arbitrage, meso, escalation, modes]
generated: { by: minimax-m3, at: 2026-08-19T01:50:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T01:50:00Z }
  - { by: human:amdkn, at: 2026-08-20T09:00:00Z }
review:
  version: V0
  by: human:amdkn
  at: 2026-08-20T09:00:00Z
  note: "Revue V0 vague 1 — validee sur les videos et presentations PDF NotebookLM. Areas de Jerry actees en V0 ; role de Summers pour les Projets introduit en V0.1."
sources:
  - id: dc-workflow
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/B2_DC_DIRECTION_COUNCIL_WORKFLOW.md"
    title: B2 DC Direction Council Workflow
    last_modified: 2026-05-27
  - id: harmonization-md
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation de la wheel — pair checks et red flags
    last_modified: 2026-08-17
  - id: fractal-arch
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/fractal-b1b2b3-architecture.md"
    title: Le fractal B1/B2/B3 — Areas perpétuelles vs Summer's Verse datées
    last_modified: 2026-08-17
  - id: b1-stop-conditions
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b1/b1-stop-conditions-escalier.md"
    title: B1 stop conditions + escalier canonique
    last_modified: 2026-08-19
okf_version: "0.2"
---

# B2 Council — qui tranche quand deux domaines se contredisent

## La réponse à la question directrice

**Quand deux domaines veulent la même ressource, qui tranche ?**

Le **B2 Direction Council** — instance d'arbitrage mésoperpétuelle. Huit
capitaines en cercle (`B2_DC_DIRECTION_COUNCIL_WORKFLOW.md`), un
mandat : préserver la wheel 8-domain tout en restant dans North Star,
cycle, autorité et appétit pour le risque courants.

**Pas** B1. **Pas** B3. **Pas** A0 Amadeus. Le B2 Council est l'organe
qui a la **compétence locale** (lit les DoDs domain, les pair checks,
les red flags) et la **légitimité horizontale** (aucun capitaine ne
commande un autre).

## Composition et routine

**Membres** : les 8 hero-managers B2 — Superman (Growth), JohnJones
(Sales, ex-Martian Manhunter W40 V4), Flash (Product), Batman (Ops),
Cyborg (IT), Wonder Woman (Finance), Green Lantern (People), Aquaman
(Legal).

**Routine** :

1. Intake d'un mandate B1 (B1-B2-MANDATE-YYYY-NN) ou d'un problème B2
   pair.
2. Identification des domaines impactés (1, 2, ou plus).
3. Chaque B2 impacted énonce : son DoD, son blocker éventuel, son
   boundary non-négociable (veto catalogue — voir
   `b2-eight-domain-vetoes-catalogue.md`).
4. Sélection du mode (parallel / handoff / negotiation — voir
   `b2-three-cooperation-modes.md`).
5. Création ou update des Rocks et DoD.
6. Dispatch B3 JTBD.
7. Log de la décision meso (format — voir
   `b2-meso-decision-packet-spec.md`).

**Sortie** : un packet YAML court, une ligne par arbitrage validé, append
à `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` (registre append-only, D4).

## Quand le Council escalade à B1

> *« Escalade à B1 seulement si le Council ne peut pas préserver la
> wheel 8-domain tout en restant dans North Star, cycle, autorité et
> appétit pour le risque courants. »*
> — `B2_DC_DIRECTION_COUNCIL_WORKFLOW.md`

Trois situations concrètes où le Council **doit** escalader, pas
résoudre :

1. **Conflit de North Star.** Deux mandates B1 simultanés exigent des
   wheel-states incompatibles (ex : « pivoter US premium » ET «
   consolider EU SMB »). Le Council n'a pas la légitimité pour choisir
   entre deux directions.
2. **Violation de cycle.** Un arbitrage exige de dépasser le 12WY
   courant (rock B1 non livrable dans le trimestre). Le Council ne
   peut pas étendre l'horizon — seul B1 peut ouvrir un cycle
   supplémentaire.
3. **Boundary non-négociable tierce.** Un veto catalogue (cf.
   `b2-eight-domain-vetoes-catalogue.md`) s'oppose à un mandate B1
   lui-même. Le Council ne peut pas amender un mandate, seulement en
   suspendre l'application ; suspendre un mandate, c'est l'escalader.

## Trois modes de coopération entre B2

`B2_DC_DIRECTION_COUNCIL_WORKFLOW.md` §« Trois modes de coopération » :

- **parallel** : les domaines agissent indépendamment. Aucun séquencement
  requis. C'est le mode par défaut tant qu'aucun transfert cross-domaine
  n'est détecté.
- **handoff** : un domaine doit finir avant qu'un autre commence. La
  livraison devient un blocage pour la suivante. Le séquencement est
  tracé dans le packet.
- **negotiation** : deux DoDs ou plus sont en conflit et nécessitent
  un tradeoff. Le Council tranche sur la base de la matrice de
  prioritis ation (North Star > cycle > risque > effort).

Voir `b2-three-cooperation-modes.md` pour le détail.

## Pourquoi pas B1

B1 (direction) tient North Star, cycle, décision rights, handoff queue.
Il n'a pas la visibilité opérationnelle sur les DoDs de chaque domaine
ni la fréquence de revue requise (B1 cadence 12WY, B2 cadence
hebdomadaire). Un arbitrage B1 sur un conflit cross-domaine
typiquement inventé — soit B1 overreach (descend dans le DoD,
franchit la frontière d'autorité), soit B1 manque la nuance (8 VP
savent ce que B1 ne peut pas voir).

## Pourquoi pas A0 Amadeus

A0 tient l'arbitrage final quand l'OS lui-même est en jeu — Life OS
L1, projets transversaux, conflit de couche. Pour un conflit B2
standard, A0 est overreach.

## Pourquoi pas B3

B3 est l'exécution. B3 n'a pas la légitimité horizontale (les squads
sont verticales à leur capitaine). Un B3 qui tranche un conflit
cross-domaine court-circuite son propre VP, et le VP ne peut plus
défendre sa doctrine.

## Liens

- [[b2-harmonization-matrix-exploitable]] — les 9 critères + 5 red flags
- [[b2-three-cooperation-modes]] — parallel/handoff/negotiation en détail
- [[b2-meso-decision-packet-spec]] — le YAML de sortie
- [[b2-eight-domain-vetoes-catalogue]] — les 8 vetos que le Council respecte
- [[b1-stop-conditions-escalier]] — l'escalier canonique 5 échelons

## Note de confiance

**Confirmé par machine.** Composition, routine, et règle d'escalade
tirés verbatim de `B2_DC_DIRECTION_COUNCIL_WORKFLOW.md`. Le liste des
trois situations d'escalade explicites est **reconstruite** à partir
de la règle d'escalade canonique + triplet v3 + fractal — la matrice
ne nomme pas explicitement ces trois situations. Les raisons de ne
pas escalader à B1/B3/A0 sont **extrapolées** depuis la doctrine
fractal et la définition des rangs A/B.
