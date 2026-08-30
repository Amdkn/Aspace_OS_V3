---
type: Concept
title: JohnJones — non-dormance « forçage zéro » formalisée vs doctrine Aquaman dormant (3 différences, 4 cas d'application, 2 abus)
description: Le tour 1 pose « JohnJones steward un état non-forcé — le domaine ne force pas la production quand la matière manque ». Mais cette doctrine n'est pas explicitée canoniquement. Ce concept formalise la non-dormance « forçage zéro » par opposition à la doctrine Aquaman dormant : 3 différences structurelles (catalogue vs fait, 0 packet vs 0 production, déclencheur B3 vs déclencheur client), 4 cas d'application (mois creux, rock B1 pas orienté client, prospect en validation lente, scope réorienté), 2 abus (déclarer non-forcé pour éviter accountability, confondre non-forcé et absence).
tags: [b2, johnjones, sales, dormance, non-dormance, aquaman, doctrine, forcing-zero, comparatif]
generated: { by: minimax-m3, at: 2026-08-19T07:50:00Z }
verified:
  - { by: process:lecture-corpus-sales-tour-4, at: 2026-08-19T07:50:00Z }
sources:
  - id: perimetre-domaine
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/john-jones/johnjones-domaine-sales-perimetre.md"
    title: JohnJones — domaine Sales & Cognition, périmètre 5 surfaces
    last_modified: 2026-08-19
  - id: aquaman-dormant-doctrine
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-areas-dormants-doctrine.md"
    title: B2 Areas-dormants — la doctrine Aquaman et ses trois conditions
    last_modified: 2026-08-19
  - id: aquaman-dormant-activation
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-dormant-activation.md"
    title: Aquaman — dormant activation 3 états
    last_modified: 2026-08-19
  - id: aquaman-classification-risques
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-classification-risques-4-formes.md"
    title: Aquaman — classification risques 4 formes
    last_modified: 2026-08-19
  - id: superman-needs-signal
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-needs-signal-vs-dormant-8domain-doctrine.md"
    title: Superman — NEEDS_SIGNAL vs DORMANT 8-domain doctrine
    last_modified: 2026-08-19
  - id: b2-eight-domain-vetoes-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2
    last_modified: 2026-08-19
okf_version: "0.2"
---

# JohnJones — non-dormance « forçage zéro »

## Le constat — un trou doctrinal

`johnjones-domaine-sales-perimetre.md` §« L'état dormant — pas une
singularité Aquaman » pose verbatim :

> *« Contrairement à Aquaman (Legal, dormant tant que
> `03_Master_Agreements/` est vide), JohnJones n'a pas d'état dormant
> canonique. Mais sa **production peut être à zéro sans que le
> domaine soit dormant** : un mois où aucun client n'est en
> discovery est un mois où le domaine n'écrit rien. Le veto tient,
> le squad est catalogué, mais les sprints sont vides. C'est une
> différence avec Aquaman : Aquaman steward explicitement un état
> dormant (triplet 35), JohnJones steward un état **non-forcé** —
> le domaine ne force pas la production quand la matière manque. »*

Cette doctrine **n'est pas explicitée canoniquement** ailleurs dans
le corpus. Le triplet 35 d'Aquaman pose verbatim *« Aquaman steward
domaine-dormant »*, mais il n'y a pas de triplet symétrique
*« JohnJones steward domaine-non-force »*. Conséquence : la
non-dormance reste une projection du tour 1.

`b2-areas-dormants-doctrine.md` §« Note de confiance » dit verbatim
> *« La généralisation de la doctrine Aquaman aux 7 autres domaines
> est une projection : seul Legal a un triplet dormant explicite. »*

C'est précisément ce trou que ce concept ferme.

## La doctrine formalisée — « forçage zéro »

**Définition** : un domaine B2 est en non-dormance *forçage zéro*
quand il n'a pas de matière à transformer (signal client absent,
mandate B1 absent, blocker B3 pair absent), et qu'il **n'écrit
rien** plutôt que de produire pour produire.

La non-dormance se distingue de :

- **Dormance Aquaman** — un acte explicite consigné dans le
  journal Council avec `decision: dormant` (cf.
  `b2-areas-dormants-doctrine.md` §Condition 3).
- **Absence** — un capitaine qui ne produit pas sans le consigner.
  La non-dormance forçage zéro n'est pas une absence — c'est une
  **non-production par absence de matière**.
- **Production forcée** — un captain qui produit pour montrer
  qu'il existe (rapports sans lecteur, dashboards sans usage).
  C'est l'anti-pièce canonique de la doctrine Aquaman
  *« un domaine dormant qui produit est un coût sans contrepartie »*
  (triplet 35).

## 3 différences structurelles avec Aquaman dormant

### Différence #1 — Catalogue vs fait

**Aquaman** : la doctrine dormant est posée dans un triplet canonique
(triplet 35) et un condition de réveil (triplet 36). C'est un
**catalogue** : la dormance est une classe documentée, avec
déclencheurs explicites.

**JohnJones** : la non-dormance n'est pas dans un triplet. C'est un
**fait observé** — la production peut être zéro, le veto tient, le
squad est catalogué, mais aucun packet mésoperpétuel ne consigne
l'état.

Conséquence : Aquaman a unCouncil-ready act (decision:dormant),
JohnJones n'en a pas. Le Council peut vérifier la dormance Aquaman
en lisant le journal ; il ne peut pas vérifier la non-dormance
JohnJones sans observer le compteur production.

### Différence #2 — 0 packet vs 0 production

**Aquaman** : 0 packet mésoperpétuel **accompagné** de
l'enregistrement `decision: dormant`. Le captain a fait l'acte de
consigner — la trace existe.

**JohnJones** : 0 packet mésoperpétuel **sans** enregistrement. La
production Sprint peut être à 0 (cf. SPRINT 2026-08 §« Mois 2026-08
» qui montre 4 sprints sans veto opposé), mais aucun packet
n'est créé.

Conséquence : Aquaman dormant est **vérifiable** par le journal
Council. JohnJones non-forcé est **invérifiable** sans observer
SPRINTS.md ou B3 SCRUMS.md.

### Différence #3 — Déclencheur B3 vs déclencheur client

**Aquaman** : le réveil suit le triplet 36 *« depend on
premier-contrat-signe »*. Le déclencheur est un **événement externe
client** (contrat signé dans `03_Master_Agreements/`).

**JohnJones** : le « réveil » suit un **blocage B3** (par exemple,
un MQL non qualifié en attente d'un Captain qui alloue MrFantastic).
C'est un signal B3 pair, pas un signal client.

Conséquence : Aquaman dormant se réveille sur contrat signé.
JohnJones non-forcé n'a pas d'état à réveiller — il **démarre** sur
un signal B3 pair (ou B1 mandate, ou Superman Growth MQL).

## 4 cas d'application de la non-dormance forçage zéro

### Cas #1 — Mois creux sans prospect

**Scénario** : aucun MQL Superman Growth ne descend vers Sales en
mois M. JohnJones n'écrit rien dans SPRINTS.md. Le compteur
production = 0.

**Statut** : non-dormance forçage zéro (matière absente en amont).
Le veto catalogue tient (cf.
`b2-eight-domain-vetoes-catalogue.md` triplet 26 *« Martian
Manhunter hasVetoOver proposition-sans-reformulation »*). Le squad
Illuminati est catalogué.

**Détection** : lecture SPRINTS.md du mois M — table vide.

### Cas #2 — Rock B1 pas orienté client

**Scénario** : le rock B1 du 12WY courant est *« consolidation
infrastructure IT »* (Batman IT) ou *« audit fiscal »* (Wonder
Woman Finance). Sales n'a rien à reformuler.

**Statut** : non-dormance forçage zéro (matière B1 absente pour
Sales). Le SPRINT B2 Sales est vide.

**Détection** : lecture B1 mandate packet — aucun mandate
touchant Sales.

### Cas #3 — Prospect en validation lente

**Scénario** : un prospect est en Phase 3 (Validation) depuis 8
semaines sans `CLIENT_VALIDATION_*.md`. Le SPRINT B2 Sales montre
l'impasse, mais aucune propale n'est envoyée (donc aucun veto à
opposer).

**Statut** : non-dormance forçage zéro avec **impasse documentée**.
Le Captain consigne l'impasse dans le journal Council mais ne
produit rien d'autre.

**Détection** : SPRINT.md avec Phase 3 sans issue > 4 semaines.

### Cas #4 — Scope réorienté vers un autre domaine

**Scénario** : un prospect intéressant est repris par Aquaman
(Legal) sur un sujet contractuel complexe, ou par Wonder Woman
(Finance) sur un F19-F22 allocation. Sales n'a plus de matière
directe.

**Statut** : non-dormance forçage zéro avec **transfert de scope**.
Le Captain consigne le transfert mais ne produit pas de reformulation
sur le prospect.

**Détection** : arbitrage Council sur transfert de scope.

## 2 abus à éviter

### Abus #1 — Déclarer non-forcé pour éviter accountability

**Scénario** : un Captain Sales déclare *« forçage zéro »* quand
le Council demande pourquoi 0 packet mésoperpétuel sur 3 vagues.
C'est un abus — la non-dormance n'est pas une exemption
d'accountability.

**Détection** : un arbitrage Council qui demande des comptes, et
le Captain répond *« forçage zéro »* sans cycle de vie ni phase
documentée.

**Remède** : le Council exige la lecture SPRINTS.md + scrums.md
avant d'accepter la non-dormance. Si la production est à 0 sans
trace de cycle de vie, c'est une absence déguisée.

### Abus #2 — Confondre non-forcé et absence

**Scénario** : un Captain Sales disparaît sans consigner, et
revient en invoquant *« forçage zéro »* a posteriori. C'est une
absence — pas une non-dormance.

**Détection** : aucun journal Council pendant > 4 semaines, aucun
SPRINT.md mis à jour, aucun packet mésoperpétuel.

**Remède** : la non-dormance forçage zéro doit être **active** —
le Captain peut ne pas produire, mais il consigne (dans SPRINTS.md
ou journal Council) qu'il n'a pas produit et pourquoi. L'absence
de consignation est une absence.

## Comparaison avec Superman NEEDS_SIGNAL

`superman-needs-signal-vs-dormant-8domain-doctrine.md` pose la
doctrine 8-domain NEEDS_SIGNAL vs DORMANT. Pour Sales, la
non-dormance forçage zéro est **distincte** de NEEDS_SIGNAL :

| État | Superman (Growth) | JohnJones (Sales) |
|---|---|---|
| **DORMANT** | Acte Council, condition 3 | n/a — pas de triplet |
| **NEEDS_SIGNAL** | Actif, attend signal B1/B3/client | Actif, attend signal MQL Growth ou B1 |
| **Forçage zéro** | n/a | Actif, n'écrit rien sans matière |
| **READY** | Growth_READY | Sales_READY (post-reformulation) |

Pour Sales, **forçage zéro** est un 4ᵉ état qui n'a pas d'équivalent
canonique pour Superman. La doctrine 8×4 de Superman ne couvre pas
cet état.

## Pourquoi cette doctrine n'est pas un « SALES_DORMANT »

`johnjones-gates-et-pair-checks.md` §« Le pattern de gates Sales »
note verbatim *« Il n'y a pas de gate `SALES_DORMANT` ou
`SALES_OUT_OF_SCOPE` — contrairement à Aquaman (Legal) qui a un
état dormant canonique. JohnJones steward un état non-forcé. »*

C'est cohérent avec la doctrine Aquaman : ajouter `SALES_DORMANT`
dans la matrice 8 gates serait un **alignement par mimétisme**, pas
par une lecture du domaine Sales. La doctrine forçage zéro préserve
la spécificité du domaine Sales (attente d'un signal MQL amont) sans
l'aplatir sur le modèle Aquaman.

## Anti-pièges

- **Ajouter `SALES_DORMANT` comme 4ᵉ gate.** C'est un mimétisme
  Aquaman. La doctrine forçage zéro est un état **hors gate** — le
  Captain n'émet pas de gate quand il ne produit pas.
- **Confondre non-dormance et zéro packet mésoperpétuel.** Le
  compteur 0 packet mésoperpétuel Sales sur 3 vagues est un
  **diagnostic**, pas une doctrine. La doctrine forçage zéro dit
  que la production peut être 0 sans que le domaine soit dormant —
  elle ne dit pas que les packets mésoperpétuels sont absents.
- **Activer la non-dormance sur des cycles courts (< 4 semaines).**
  La non-dormance se constate sur un 12wy, pas un sprint. Un sprint
  vide n'est pas forçage zéro, c'est un sprint sans matière (cycle
  de vie Phase 1-5 sans entrée).
- **Ignorer Aquaman quand le signal client arrive.** Si un
  contrat est signé, Aquaman dormant se réveille (triplet 36). Si
  un MQL arrive, JohnJones forçage zéro **démarre** une discovery
  (cycle de vie Phase 1). Les deux réactivations sont distinctes.
- **Forcer la production quand la matière manque.** C'est
  l'anti-pièce canonique — *« un domaine dormant qui produit est un
  coût sans contrepartie »* (triplet 35).

## Liens

- [[johnjones-domaine-sales-perimetre]] — la doctrine non-forcé du
  tour 1
- [[johnjones-protocole-empirique-zero-cas-procedure-remplacement]] —
  0 cas sur compteur discriminant
- [[johnjones-trigger-risk-charge-livraison-calibration-proxy]] —
  proxy sur Batman `ops_handoff_accepted`
- [[b2-areas-dormants-doctrine]] — la doctrine Aquaman dont
  forçage zéro se distingue
- [[aquaman-dormant-activation]] — Aquaman 3 états Dormant/SHADOW_ACTIVE/ACTIVE
- [[superman-needs-signal-vs-dormant-8domain-doctrine]] — la table
  8×4 NEEDS_SIGNAL
- [[b2-eight-domain-vetoes-catalogue]] — veto catalogue JohnJones
  triplet 26

## Note de confiance

**Confirmé par machine, à moitié.** La doctrine *« forçage zéro »*
est **reconstruite** depuis la phrase du tour 1 *« JohnJones steward
un état non-forcé »* et l'asymétrie observée vs Aquaman. La
différence #1 (catalogue vs fait) est **projetée** depuis le
constat que seul Legal a un triplet dormant explicite (cf.
`b2-areas-dormants-doctrine.md` §Note de confiance).

Les 4 cas d'application sont **projetés** par analogie avec la
pratique SPRINT 2026-08 et les ouvertures tour 3 (4 zones
structurellement hors-périmètre Captain Sales). Les 2 abus sont
**projetés** depuis `b2-areas-dormants-doctrine.md` §Anti-pièges
*« Dormance déclarée sans signal »* et *« Confondre dormance et
délégation de veto »*.

La comparaison avec Superman NEEDS_SIGNAL est **projetée** depuis
la table 8×4 dans `superman-needs-signal-vs-dormant-8domain-doctrine.md`
— le 4ᵉ état forçage zéro n'est pas posé ailleurs dans le corpus.

À vérifier en cycle réel : (1) la doctrine forçage zéro est-elle
tenable quand le SPRINT B2 Sales est attendu par B1 mandate ? (2)
le compteur 0 packet mésoperpétuel sur 3 vagues est-il
symptomatique d'une absence déguisée ? (3) Aquaman accepte-t-il
que Sales n'ait pas de gate `SALES_DORMANT` symétrique ?