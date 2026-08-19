---
type: Concept
title: Couplage Ops (Batman) ↔ IT (Cyborg) — la chaîne Product→IT→Ops
description: Ops et IT sont les deux faces du red flag #1 — Product green, Ops/IT red. La frontière est nette : IT tient le système (déploiement, monitoring, récupération), Ops tient la procédure (runbook, escalation, condition d'arrêt). Mais la chaîne Product→IT→Ops traverse Batman deux fois (en A sur Product→Ops, et en dépendance côté IT). Le couplage Batman-Cyborg est ce qui ferme la porte de la livraison.
tags: [batman, cyborg, ops, it, couplage, red-flag, runbook, monitoring, b2]
generated: { by: minimax-m3, at: 2026-08-19T03:55:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T03:55:00Z }
sources:
  - id: harmonization-md
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation de la wheel — pair checks et red flags
    last_modified: 2026-08-17
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — IT = 05, Ops = 04
    last_modified: 2026-08-17
  - id: b2-pair-raci
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang — Batman A sur #3, Cyborg A sur #4
    last_modified: 2026-08-19
  - id: triplet-cyborg-cloud
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 28 — Cyborg bloque tout fournisseur cloud-only sans chemin de sortie documenté"
    last_modified: 2026-08-17
  - id: triplet-cyborg-river
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 38 — Cyborg ne touche pas L0 directement — passe par River Song"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Couplage Ops (Batman) ↔ IT (Cyborg) — la chaîne Product→IT→Ops

## Pourquoi Ops et IT sont inséparables dans la matrice

La matrice d'harmonisation pose **5 red flags** (arrêts durs). Le
premier est *« Product green, Ops/IT red — ne pas lancer »*. Les
deux domaines sont **groupés** dans le même red flag, pas parce qu'ils
sont équivalents, mais parce qu'ils sont **les deux conditions
nécessaires** pour qu'un produit livré soit tenable.

Le mapping 8-domain place Ops en **04** et IT en **05** — c'est
adjacent dans la wheel. Ce n'est pas un hasard d'ordre. La wheel est
lue comme un cercle, et Ops+IT sont les deux domaines qui ferment la
boucle de livraison : sans Ops, le produit n'est pas supporté ;
sans IT, le produit ne tourne pas.

## La frontière — Ops = procédure, IT = système

| Dimension | Ops (Batman) | IT (Cyborg) |
|---|---|---|
| **Tient** | la procédure (comment on répond, comment on escalade, comment on arrête) | le système (déploiement, monitoring, infrastructure, code de run) |
| **Produit** | runbooks, SOPs, matrices d'escalation, conditions d'arrêt | pipelines CI/CD, dashboards de monitoring, alertes, playbooks de recovery |
| **Question de garde** | *« est-ce qu'on sait répondre quand X arrive ? »* | *« est-ce que le système tient quand X arrive ? »* |
| **Veto catalogue** | procédure sans condition d'arrêt (triplet 24) | fournisseur cloud-only sans chemin de sortie (triplet 28) |
| **Cadence** | sprint hebdo +astreinte incidents | sprint hebdo +astreinte système |
| **Squad Marvel** | Fantastic Four (4 techniciens) | Kang Dynasty (6 techniciens) |

La frontière est nette mais **pas étanche**. Elle est poreuse sur
deux points :

### Porosité 1 — Le runbook peut avoir un versant IT

Un runbook Ops peut inclure une étape *« vérifier le dashboard
monitoring X »* — ce qui est une dépendance Ops vers IT. Batman
dépend de Cyborg pour que le dashboard existe ; Cyborg dépend de
Batman pour que le runbook soit suivi.

Concrètement : Batman ne peut pas écrire un runbook Ops qui exige un
monitoring que Cyborg n'a pas posé. Et Cyborg ne peut pas poser un
monitoring qui n'a pas de runbook Ops derrière — sinon une alerte
déclenche sans réponse.

### Porosité 2 — L'incident peut basculer Ops ↔ IT

Un incident qui commence côté Ops (un client ne reçoit pas son
livrable) peut basculer côté IT (le système a un bug) ou inversement.
HumanTorch (B3 Ops, Incidents) escalade à Batman ; Batman arbitre
s'il faut faire intervenir Cyborg. La règle est implicite dans la
matrice d'harmonisation : un incident **système** est IT, un incident
**procédure** est Ops. La distinction est dans la cause racine, pas
dans le symptôme.

## Le red flag #1 — la chaîne Product→IT→Ops traverse Batman deux fois

Le RACI par rang place Batman en **A** sur le pair-check #3
(Product → Ops) et Cyborg en **A** sur le pair-check #4 (Product →
IT). La chaîne canonique d'une feature livrée est :

```
Product (Flash) shippe la feature
       │
       ├──> IT (Cyborg, pair-check #4 A) : le système tourne ?
       │     monitoring, déploiement, recovery
       │
       └──> Ops (Batman, pair-check #3 A) : la procédure tourne ?
             runbook, support, condition d'arrêt
```

Batman est **dépendant** de Cyborg sur la sortie de #4 (le système
doit tourner pour que la procédure tienne), et **A** sur #3 (Batman
décide si la procédure tourne). Cyborg est **indépendant** de Batman
pour sa propre décision A sur #4 — mais le résultat de #4 conditionne
la faisabilité de #3.

Conséquence concrète : si Cyborg pose un veto (cloud-only sans
chemin de sortie — triplet 28), Batman remonte le fait à Summers et
**lance l'escalade B1**. Batman ne peut pas tourner autour du veto
IT — la dépendance est trop forte.

## La médiation Cyborg ↔ L0 — ce que Batman n'a pas à faire

Le triplet 38 dit *« Cyborg ne touche pas L0 directement — il passe
par River Song (SDD-004 §7.2), médiation agentique imposée »*.
C'est une dépendance IT qui ne touche pas Batman directement — mais
elle le touche **indirectement** : si Cyborg est bloqué en médiation
L0, Batman ne peut pas boucler #4. C'est un signal que Batman
remonte à Summers, pas un problème que Batman résout.

Triplet 39 confirme la pyramide L0 ≥ L1 > L2 (SDD-006 §1.1:59) :
L0 a autorité absolue, L1 a le veto (Beth), L2 exécute. Batman est
L2 — il ne statue pas sur L0/L1. Si une décision L0 bloque Ops
indirectement (ex : un skill L0 qui ne peut pas être invoqué),
Batman remonte, il ne contourne pas.

## Le couplage en une phrase

Batman ne peut rien lancer qu'il ne peut pas supporter ; Cyborg ne
peut rien faire tourner qu'il ne peut pas monitorer. Le couplage est
**une chaîne où la sortie d'un est la condition d'entrée de l'autre**
— et le red flag #1 de la matrice est l'expression canonique de
cette chaîne.

## Anti-pièges

- **Traiter Ops et IT comme synonymes.** Ops est la procédure ; IT
  est le système. Confondus, le veto IT (cloud-only sans chemin de
  sortie) est appliqué à tort par Batman, ou le veto Ops (procédure
  sans condition d'arrêt) est appliqué à tort par Cyborg.
- **Batman qui statue sur un incident IT.** Un incident système
  (panne serveur, base de données inaccessible) est IT. Batman ne
  pose pas le runbook de recovery — il remonte à Cyborg et suit la
  procédure que Cyborg a écrite.
- **Cyborg qui écrit un runbook Ops.** Le runbook est procédure Ops,
  pas système IT. Cyborg peut documenter le monitoring, mais la
  procédure d'escalade qui suit l'alerte est Batman.
- **Batman qui contourne un veto IT.** Si Cyborg oppose le veto
  cloud-only (triplet 28), Batman remonte le fait à Summers. Il ne
  dit pas *« OK on prend le risque »* — c'est une décision de cycle,
  pas une décision opérationnelle.

## Liens

- [[domaine-batman-ops-perimetre-frontieres]] — le périmètre Ops qui motive le couplage
- [[batman-pair-checks-jtbd-fantastic-four]] — Batman A sur #3, qui dépend de #4 (Cyborg)
- [[batman-veto-condition-arret-procedure]] — le veto Ops complémentaire au veto IT
- [[b2-pair-check-raci-by-rank]] — le tableau complet avec Cyborg A sur #4

## Note de confiance

**Confirmé par machine.** La frontière Ops/IT (procédure vs système)
est **reconstruite** à partir de la matrice d'harmonisation et du
mapping 8-domain. Les deux porosités (runbook avec versant IT,
incident basculant) sont **mon inférence** à partir du triplet 32
(HumanTorch décide de l'escalade). La chaîne Product→IT→Ops est
**reconstruite** à partir du RACI par rang et du red flag #1. La
règle *« Batman remonte si Cyborg est bloqué en L0 »* est **mon
raisonnement** à partir des triplets 38, 39 et de la doctrine fractal
d'escalade.