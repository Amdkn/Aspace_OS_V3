---
type: Concept
title: People — dormance vs attente vs actif, trois états et leurs déclencheurs
description: Le canon B2 pose la doctrine de dormance pour les domaines B2 sans mandate B1 actif, mais ne distingue pas l'attente (signal en attente de B1) de la dormance (silence durable). Le concept propose trois états People — DORMANT, EN_ATTENTE, ACTIF — avec leurs déclencheurs d'entrée et de sortie, et un cas asymétrique pour People × IT (skills L0) qui ne tombe jamais en dormance complète. Reconstruit, à arbitrer par B2 Council.
tags: [people, green-lantern, dormance, attente, actif, shadow-active, b2, doctrine, evenement]
generated: { by: minimax-m3, at: 2026-08-19T05:20:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-2, at: 2026-08-19T05:20:00Z }
sources:
  - id: aquaman-dormant-tour-2
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-dormant-activation.md"
    title: "Aquaman tour 2 — doctrine dormant-activation 3 états"
    last_modified: 2026-08-19
  - id: b2-areas-dormants
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-areas-dormants-doctrine.md"
    title: B2 doctrine des domaines dormants
    last_modified: 2026-08-19
  - id: green-lantern-gates-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-gats-assigned-needs-owner-dlq.md"
    title: "Tour 1 — People 3 états ASSIGNED / NEEDS_OWNER / DLQ"
    last_modified: 2026-08-19
  - id: green-lantern-couplages-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-couplages-invisibles.md"
    title: "Tour 1 — People sept couplages invisibles"
    last_modified: 2026-08-19
  - id: triplet-37-forge
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 37 — Green Lantern sollicite Bill (L0.2 Forge) — canal non-contournable"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# People — dormance vs attente vs actif, trois états et leurs déclencheurs

## Le constat — la doctrine dormance existe, l'attente n'est pas articulée

Le B2 Council pose la doctrine des **domaines dormants** (cf.
`b2-areas-dormants-doctrine.md` cité par Aquaman tour 2) : un
domaine B2 sans mandate B1 actif pendant un cycle 12WY peut être
**mis en dormance**. Aquaman a explicité trois états pour son
domaine : **Dormant / SHADOW_ACTIVE / ACTIVE**, avec une
distinction Coach OS (dormant = périmètre non activé) vs OMK
(SHADOW_ACTIVE = périmètre activé sans owner principal).

Le concept Aquaman est un **précédent utile** mais **pas
transposable tel quel** à People. People a une particularité :
le gate `NEEDS_OWNER` permanent **n'est pas** un signal de
dormance — c'est un signal **actif** d'un poste vacant. Si
People passe en dormance sur un `NEEDS_OWNER` ouvert, le poste
ne sera jamais pourvu.

Le gap canonique #5 du RAPPORT tour 1 pose la question :
*« People est-il dormant quand B1 ne mandate pas RH ? »* La
réponse canonique n'existe pas. Le présent concept propose
**trois états People** — DORMANT, EN_ATTENTE, ACTIF — et leurs
déclencheurs d'entrée / sortie, en s'inspirant de la doctrine
Aquaman sans la dupliquer.

## Les trois états People

### État 1 — DORMANT (silence durable)

**Définition.** People n'a aucun signal en attente, aucun
mandate B1 actif, aucun `NEEDS_OWNER` ouvert, aucune sollicitation
Forge. La wheel People tourne à vide.

**Conditions d'entrée (toutes requises)** :

1. Aucun mandate B1 actif (B1 handoff queue vide côté People).
2. Aucun `NEEDS_OWNER` ouvert sur les 7 autres domaines.
3. Aucune sollicitation Forge en cours (triplets 37, 55).
4. Aucune escalade de vacance (cf.
   `green-lantern-people-seuil-vacance-tolerable.md` §« Étage 2 »)
   en attente.
5. **Cycle 12WY courant sans recrutement** (typiquement 13
   semaines depuis le dernier recrutement clos).

**Conséquence opérationnelle.** People est **en réserve** :

- ProfessorX (recrutement humain, triplet 33) et Beast
  (TechRecruiting, triplet 34) ne sont pas actifs. Les autres
  X-Men peuvent être réassignés temporairement à un autre
  domaine (Batman Ops, par exemple, sur une charge pic).
- Le veto People catalogue **continue de tenir** (un
  recrutement sans mandat reste bloqué — la dormance ne lève
  pas le veto).
- Green Lantern ne participe pas aux séances Council sauf
  si **sollicité** par un autre capitaine (par exemple, sur
  une question People × Legal).

**Conditions de sortie** :

- Un mandate B1 entre (People redevient ACTIF).
- Un `NEEDS_OWNER` s'ouvre (People passe en EN_ATTENTE).
- Une sollicitation Forge arrive (People passe en EN_ATTENTE).
- Le cycle 12WY se termine sans qu'aucune condition d'entrée
  en DORMANT se redéclenche (People reste en DORMANT).

### État 2 — EN_ATTENTE (signal en attente)

**Définition.** People a un **signal** en attente d'arbitrage
B1 ou Council, mais aucun mandate B1 actif. Typiquement, un
`NEEDS_OWNER` ouvert, ou une sollicitation Forge, ou une
escalade de vacance en étage 1-2.

**Conditions d'entrée (une requise)** :

1. Un `NEEDS_OWNER` est ouvert sur un des 7 autres domaines
   (par exemple, Batman Ops signale un owner manquant).
2. Une sollicitation Forge est en cours (par exemple, un
   recrutement agent attend la confirmation de Bill L0.2
   Forge).
3. Une escalade de vacance est en cours (par exemple, un
   mandat vacant depuis 60 jours sans issue).
4. Un arbitrage Council est en attente d'une position People
   (par exemple, un conflit People × Legal non tranché).

**Conséquence opérationnelle.** People est **réactif** :

- ProfessorX et Beast sont en **veille active** (pas
  dormants, mais pas en recrutement non plus).
- Le veto People catalogue tient.
- Green Lantern **participe** aux séances Council en
  **C** systématique (position transverse, cf.
  `green-lantern-people-raci-transverse-jamais-A.md`).
- Green Lantern **ne mandate pas** de recrutement sans
  l'arbitrage B1 ou Council — il **signale**, il ne
  **décide** pas.

**Conditions de sortie** :

- Le signal est **résolu** (mandate B1 entre → ACTIF, ou
  signal retiré → DORMANT).
- L'arbitrage B1 ou Council rend une décision (People
  mandate selon la décision → ACTIF).

### État 3 — ACTIF (mandate B1 en cours)

**Définition.** People exécute un mandate B1 actif — un
recrutement humain, un recrutement agent, une sollicitation
Forge, un re-scope, une succession. La wheel People tourne
à charge pleine.

**Conditions d'entrée (une requise)** :

1. Un mandate B1 entre (B1 mandate People directement).
2. Un arbitrage Council mandate People (par exemple, People
  × Legal en escalade B1 → arbitrage Council → ACTIF).
3. Un recrutement ProfessorX / Beast est en cours.

**Conséquence opérationnelle.** People est **exécutif** :

- ProfessorX et Beast sont à charge pleine.
- Le veto People catalogue tient.
- Green Lantern **participe** aux séances Council en
  **A** (Accountable) sur le mandate en cours, en **C**
  sur les autres mandates.
- Green Lantern **décide** des recrutements (mandate, signe,
  mandate B3 X-Men, suit les lead indicators).

**Conditions de sortie** :

- Le mandate B1 est clos (People passe en EN_ATTENTE si
  d'autres signaux, ou en DORMANT si vide).
- Le mandate B1 est retiré (même issue).

## Le tableau récapitulatif

| État | Conditions d'entrée | Veto People | Green Lantern au Council | Recrutement actif |
|---|---|---|---|---|
| **DORMANT** | 5 conditions cumulatives | Tient | Sur sollicitation | Non |
| **EN_ATTENTE** | 1 condition sur 4 | Tient | C systématique | Non (signale) |
| **ACTIF** | 1 condition sur 3 | Tient | A sur mandate / C ailleurs | Oui |

## Le cas asymétrique — People × IT (skills L0)

Le couplage People × IT (skills L0) ne tombe **jamais** en
dormance complète. Trois raisons :

1. **Le canal Forge est non-contournable** (triplet 37) —
   une sollicitation Forge peut arriver à tout moment, même
   si People n'a aucun autre signal.
2. **Le veto People catalogue** (recrutement sans mandat)
   doit tenir **même en dormance** — une demande de
   recrutement non-mandatée peut survenir à tout moment.
3. **Le lag indicator succession** (cf.
   `green-lantern-people-lag-indicator-succession.md`) tourne
   en continu — un owner peut partir sans prévenir, et le
   lag doit être publié même si People n'a aucun mandate.

**Conséquence** : People × IT est un **canal toujours actif**,
même quand People (sur ses autres périmètres) est DORMANT.
C'est une **exception structurelle** à la tri-état — pas un
quatrième état, mais un **sous-état permanent** de People.

**Justification.** Si People tombait en DORMANCE complète
sur les skills L0, alors un blocage Forge en attente ne
serait pas traité. Le canal People → Forge (triplet 37) est
**non-contournable** — c'est un **canal chaud**, pas un
canal en veille.

## Le cas asymétrique — People × Brand (co-sponsorat)

Le couplage People × Brand (cf.
`green-lantern-people-couplages-invisibles.md` §7, et
concept #6 du présent tour 2) a une logique différente :

- Si Superman Growth (Brand) est **ACTIF** (mandate B1
  sur la marque), People est en **EN_ATTENTE** (le
  co-sponsorat attend un signal de Superman).
- Si Superman Growth est **DORMANT**, People n'a aucune
  raison d'être EN_ATTENTE sur la marque — People × Brand
  est **gelé** jusqu'au réveil de Superman.

**Conséquence** : People × Brand **suit** l'état de Superman
Growth, pas son propre état. C'est un couplage **passif**,
contrairement à People × IT qui est **actif**.

## Le mécanisme d'escalade inter-états

Quand People doit changer d'état, l'escalade suit un
**mécanisme en trois temps** :

1. **Détection** — un captain B2 (Batman Ops typiquement)
   détecte un `NEEDS_OWNER`, ou Green Lantern détecte
   lui-même un signal Forge, ou B1 mandate People.
2. **Consignation** — le changement d'état est consigné
   dans le journal Council hebdomadaire, avec **horodatage**
   et **motif**.
3. **Confirmation** — le Council **valide** le changement
   d'état en séance hebdomadaire. Si le Council refuse
   (par exemple, le signal n'est pas un vrai signal mais
   une erreur de diagnostic), People reste dans l'état
   précédent.

**Pas d'auto-proclamation.** People ne **décide pas** seul
de son état — le Council **confirme**. Cela évite que
People reste en DORMANT par confort, ou passe en ACTIF
sans mandate réel.

## Anti-pièges

- **Dormance par confort.** Un People qui n'a pas de
  mandate B1 depuis deux cycles peut être **tenté** de
  rester en DORMANT pour éviter la charge Council. C'est
  un abus — la dormance est un **état de réserve**, pas
  un **congé**. Le Council doit vérifier que les
  conditions d'entrée en DORMANT sont **toutes** remplies.
- **Attente éternelle.** Un People en EN_ATTENTE depuis
  plusieurs cycles sans qu'aucun signal ne soit résolu
  doit **escaler** au Council pour amender la situation.
  L'attente n'est pas un état permanent — c'est un état
  **transitoire** vers ACTIF ou DORMANT.
- **ACTIF auto-proclamé.** Un People qui se proclame ACTIF
  sans mandate B1 réel (par exemple, en prétextant un
  « recrutement stratégique ») **usurpe** B1. Le Council
  doit refuser l'auto-proclamation et exiger un mandate
  B1 documenté.
- **Dormance sur le canal Forge.** Un People qui
  prétend être en DORMANT mais qui **continue** de
  traiter les sollicitations Forge est **incohérent**.
  Le sous-état People × IT (cf. §« Le cas asymétrique »)
  doit être **explicite** dans le journal.
- **Confondre DORMANT et inactif.** Le DORMANT People
  continue de **tenir le veto catalogue** (un recrutement
  sans mandat reste bloqué). Un DORMANT **inactif** (qui
  ne tient plus le veto) est un People qui a **abandonné**
  sa fonction — c'est un cas d'escalade B1 par défaut.

## Liens

- [[green-lantern-people-gats-assigned-needs-owner-dlq]] — les
  3 états B2 (ASSIGNED / NEEDS_OWNER / DLQ) que les 3 états
  People (DORMANT / EN_ATTENTE / ACTIF) **englobent**
- [[green-lantern-people-couplages-invisibles]] — §3 ownership
  vacant × tous (le signal qui maintient People en EN_ATTENTE)
- [[green-lantern-people-seuil-vacance-tolerable]] — la
  procédure d'escalade qui peut faire passer People d'EN_ATTENTE
  à ACTIF (étage 2 escalade B1 → arbitrage Council → ACTIF)
- [[green-lantern-people-meta-gouvernance-skills-l0]] — le
  cas asymétrique People × IT (canal Forge toujours actif)
- [[green-lantern-people-formule-charge-carte]] — la charge
  calculée qui sert de **signal** pour les transitions d'état
- [[aquaman-dormant-activation]] — la doctrine Aquaman
  dont ce concept s'inspire (sans la dupliquer)

## Note de confiance

**Reconstruit, à moitié étayé.** La tri-état (DORMANT /
EN_ATTENTE / ACTIF) est **projetée** depuis la doctrine
Aquaman dormant-activation et depuis la pratique Council.
Les conditions d'entrée et de sortie sont **reconstituées**
depuis les triplets 33, 34, 37, 55, et depuis la matrice
d'harmonisation (red flag #3). Le cas asymétrique People × IT
(sous-état permanent) est **projeté** depuis le triplet 37
*« le protocole ne se contourne pas »*. Le cas asymétrique
People × Brand (suivi de Superman) est **projeté** depuis le
couplage People × Growth (cf. concept #6 du présent tour 2).
Le mécanisme d'escalade inter-états (détection / consignation
/ confirmation) est **ajouté** : pas de source canonique, mais
cohérent avec la doctrine D4 append-only. **À arbitrer par
B2 Council.**
