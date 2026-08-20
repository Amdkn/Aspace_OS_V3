---
type: Concept
title: Trois modes de coopération B2 — parallel / handoff / negotiation
description: Quand un arbitrage B2 isolate les domaines sans séquencement, c'est parallel. Quand un domaine doit finir avant qu'un autre commence, c'est handoff. Quand deux DoDs sont en conflit, c'est negotiation. Le passage d'un mode à l'autre suit trois signaux explicites.
tags: [b2, modes, cooperation, parallel, handoff, negotiation, escalation]
generated: { by: minimax-m3, at: 2026-08-19T01:55:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T01:55:00Z }
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
  - id: b1-mandate
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b1/b1-mandate-packet-spec.md"
    title: B1 mandate packet spec
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Trois modes de coopération B2 — parallel / handoff / negotiation

## Le principe

Un arbitrage B2 Council produit **un mode**, pas une négociation :
les domaines impactés sont déclarés *parallel*, *handoff*, ou
*negotiation*. Le mode est ce qui détermine la suite — séquencement,
propriété, packet de sortie.

> *« parallel : les domaines peuvent agir indépendamment. handoff : un
> domaine doit finir avant qu'un autre commence. negotiation : deux
> DoDs ou plus sont en conflit et nécessitent un tradeoff. »*
> — `B2_DC_DIRECTION_COUNCIL_WORKFLOW.md`

## Les trois modes

### Parallel — mode par défaut

**Quand** : aucun transfert cross-domaine n'est détecté sur les 9
critères de la matrice d'harmonisation. Les 8 domaines peuvent agir
sans blocage mutuel.

**Qui décide** : chaque capitaine B2 dans son propre domaine, sans
passage au Council. Le Council n'est pas convoqué.

**Example** : Growth lance une campagne paid media sur un segment déjà
qualifié. Sales n'est pas sollicité. Product n'est pas sollicité. Ops
n'est pas sollicité. **Parallel, pas de packet.**

**Risque** : nommer parallel un cas qui ne l'est pas. Le signal : un
B3 signale un blocker cross-domaine (B3 escalate B2 → B2 captain
constate cross-effect → retour au Council). Si le cas était parallel
mais a posteriori ne l'était pas, **c'est une erreur de scan B1**, pas
de Council.

### Handoff — séquencement explicite

**Quand** : un transfert obligatoire a été détecté. La sortie d'un
domaine est l'entrée d'un autre, et le second ne peut pas commencer
sans la première.

**Qui décide** : le Council, avec le mandat B1 source. Le séquencement
est tracé dans le packet.

**Example** : Product (Flash) livre une feature qui nécessite une
revue Legal (Aquaman) avant qu'Ops (Batman) puisse l'ouvrir au public.
La chaîne est *Product → Legal → Ops*. Le packet handoff déclare
l'ordre, le DoD par étape, et le B3 squad qui prend en charge.

**Risque** : confondre handoff avec negotiation. Le signal : si le
deuxième domaine **peut** commencer avant que le premier finisse (au
prix d'un rework), ce n'est pas handoff, c'est negotiation. Handoff
n'a pas de rework acceptable.

### Negotiation — conflit de DoDs

**Quand** : deux DoDs ou plus sont en conflit et nécessitent un
tradeoff. Tradeoff = on renonce à quelque chose pour gagner autre
chose.

**Qui décide** : le Council tranche sur la matrice de prioritis
ation (North Star > cycle > risque > effort). Le résultat est un
**DoD amendé**, pas un DoD retiré.

**Example** : Finance (Wonder Woman) bloque une dépense récurrente
qui n'a pas de métrique de retour chiffrée (vet catalogue). Growth
(Superman) en a besoin pour scaler l'attention. Negotiation : la
dépense est approuvée avec une métrique de retour à 30 jours et une
date de revue. Si la métrique n'est pas tenue, la dépense est coupée
sans nouveau arbitrage.

**Risque** : confondre negotiation avec abandon. Le signal : un DoD
abandonné sans nouveau DoD équivalent est **une perte**, pas un
tradeoff. Le packet doit documenter le *ce qui remplace*, pas
seulement le *ce qui est retiré*.

## Les trois signaux de passage d'un mode à l'autre

| Passage | Signal | Action |
|---|---|---|
| parallel → handoff | un B3 signale un blocker cross-domaine | retour au Council, mode re-évalué |
| handoff → negotiation | le deuxième domaine propose un rework acceptable | retour au Council, mode re-évalué |
| negotiation → escalate B1 | un veto catalogue tient face au tradeoff | packet escalade B1 avec motif |

**Tous les passages sont tracés** dans le packet de sortie. Un
changement de mode en cours d'exécution n'est **pas** un changement
de décision — c'est une nouvelle décision. Append-only.

## Pourquoi ne pas inventer un quatrième mode

Trois modes couvrent l'espace des cas cross-domaines B2 :

- *parallel* : pas de couplage.
- *handoff* : couplage séquentiel.
- *negotiation* : couplage contradictoire.

Un quatrième mode (*async*, *broadcast*, *merge*, *fork*) duplique l'un
des trois ou fait intervenir un autre rang (B1 cycle, B3 JTBD). Le
Council ne légifère pas sur les noms — il applique la règle.

## Anti-pièges

- **Parallel par défaut sans scan.** Sans la matrice d'harmonisation
  en amont, le Council déclare parallel des cas qui sont en fait
  handoff. C'est ce qui produit les échecs de lancement « radar au
  vert, transition rouge ».
- **Handoff avec rework possible.** Si le deuxième domaine peut
  commencer avec une version dégradée, c'est negotiation, pas handoff.
- **Negotiation avec un DoD abandonné.** Si aucun DoD ne remplace,
  c'est un escalade B1 (le North Star est en jeu), pas une résolution
  mésoperpétuelle.
- **Changement de mode silencieux.** Le packet de sortie doit contenir
  le mode initial ET le mode final. Si vous ne pouvez pas le
  documenter, le changement n'a pas eu lieu.

## Liens

- [[b2-council-arbitrage-rule]] — qui tient le Council
- [[b2-harmonization-matrix-exploitable]] — les 9 critères qui détectent les transferts
- [[b2-meso-decision-packet-spec]] — le format qui contient le mode
- [[b1-mandate-packet-spec]] — le mandat B1 qui déclenche le Council

## Note de confiance

**Confirmé par machine.** Les trois modes (parallel/handoff/negotiation)
tirés verbatim de `B2_DC_DIRECTION_COUNCIL_WORKFLOW.md`. Le passage
entre modes (tableau 3 signaux) est **reconstruit** à partir de la
règle d'escalade canonique. Les 4 anti-pièges sont **extrapolés** à
partir des erreurs typiques d'arbitrage documentées dans le fractal
(qui ne les nomme pas explicitement).
