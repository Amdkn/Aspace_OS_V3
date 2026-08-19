---
type: Concept
title: People (Green Lantern / X-Men) — périmètre et trois frontières floues
description: Le périmètre People canon V4 = People (domaine 07), B2 captain Green Lantern, B3 squad X-Men. Trois frontières contestées : avec IT Cyborg (tech-recruiting vs IT infra), avec Legal Aquaman (contrats de travail), avec Batman Ops (rotation de charge sur la livraison). Frontière canon = "qui tient le mandat de recrutement, qui tient la propriété de l'agent".
tags: [people, green-lantern, x-men, perimetre, frontiere, b2, canon-v4]
generated: { by: minimax-m3, at: 2026-08-19T04:00:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T04:00:00Z }
sources:
  - id: avengers-wheel-canon
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — mapping B2 → B3 canon
    last_modified: 2026-08-17
  - id: coach-os-domaine-01
    resource: "C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/coach-os/04_Business_Domains/01_RH_Meta_Gouvernance_GreenLantern_XMen/VP_AGENT.md"
    title: Coach OS — VP B2 Green Lantern (RH & Méta Gouvernance)
    last_modified: 2026-08-02
  - id: triplet-15-vp-mapping
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 15 — Green Lantern VP B2 commande X-Men (8 techniciens)"
    last_modified: 2026-08-17
  - id: triplet-33-34-prof-beast
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 33/34 — ProfessorX recruiting, Beast TechRecruiting"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# People (Green Lantern / X-Men) — périmètre et trois frontières floues

## Le périmètre canon V4

Le périmètre People canon (cf. `eight-domain-avengers-wheel.md`) est
**strict** :

- **Recrutement humain** — sourcing, lecture de profils, validation de
  l'adéquation, signature du contrat de travail.
- **Recrutement agent** — sélection d'un agent B3 (B3 squad Marvel ou
  agent générique) pour occuper un poste vacant ou créer un nouveau poste.
- **Assignation / désassignation** — qui porte un mandat, qui le libère.
- **Charge & capacité** — la wheel People tourne sur la question *« la
  charge est-elle tenable ? »* (cf. pair-check #9 *People → Tous*).

Le périmètre s'arrête où le **contrat de travail** ou le **mandat
d'agent** est signé. People ne porte pas l'exécution, ne porte pas le
code, ne porte pas le livrable. C'est un capitaine de **dotation**, pas
de **production**.

## Les trois frontières contestées

### 1. People ↔ IT Cyborg — qui recrute les techniciens ?

**Conflit observé.** Le triplet 33 attribue le **recruiting général** à
ProfessorX (X-Men / People). Le triplet 34 attribue le **TechRecruiting**
à Beast (X-Men / People lui aussi). Mais `business-wheel-harmonization-matrix`
place Product×IT sur la question *« le produit tourne-t-il, déploie,
récupère, est-il accessible ? »* — ce qui suppose que IT Cyborg est
**propriétaire du système**, pas du recrutement technique.

**Frontière canon (reconstituée)** :

| Décision | Owner |
|---|---|
| « avons-nous besoin d'un nouvel agent tech ? » | **B2 People** (charge, capacité) |
| « quel profil technique correspond au poste ? » | **B2 People / Beast** (TechRecruiting) |
| « où déploie-t-on l'agent, dans quel système ? » | **B2 IT Cyborg** (propriété système) |
| « l'agent a-t-il le skill L0 requis ? » | **B2 People** (escalade Bill L0.2 Forge, triplet 37 + 55) |

La règle implicite : People **choisit et mandate**, IT **héberge et
supervise**. Si People mandate un agent sans que IT puisse l'héberger,
c'est un red flag matrice *Product green / IT red* inversé en *People
green / IT red* — pas nommé dans la matrice canon, mais symétrique.

### 2. People ↔ Legal Aquaman — qui signe quoi ?

**Conflit observé.** Aquaman tient le veto *« engagement démarré sans
accord écrit sur le périmètre et la propriété du livrable »* (catalogue
8 vetos). People tient le veto *« recrutement sans mandat écrit + critère
de sortie »*. Les deux vetos portent sur **la même signature**, mais
avec des focales différentes.

**Frontière canon (reconstruite)** :

- **People** signe le **mandat de recrutement** (qui, pour quoi, jusqu'à
  quand, critère de sortie).
- **Legal** signe l'**accord de prestation** (périmètre du livrable,
  propriété intellectuelle, conditions de résiliation).
- Les deux signatures sont **obligatoires et séquentielles** : Legal ne
  peut pas démarrer une prestation avant que People ait mandaté le
  recrutement.

Un recrutement sans mandat People ne peut pas être transformé en
  prestation ; un mandat People sans accord Legal ne peut pas être
  activé. Cette double clef n'est pas explicitée dans la matrice — c'est
  une **reconstitution** à partir des deux vetos catalogue.

### 3. People ↔ Batman Ops — la charge de livraison

**Conflit observé.** La matrice pose le red flag #3 *« Sales green /
Ops+People red »* — risque de charge de livraison. Le pair-check #9
*People → Tous* teste *« la propriété et la charge sont-elles tenables
? »*. Batman Ops tient le veto *« procédure sans condition d'arrêt »*,
qui ne parle pas de charge mais de **qui arrête une procédure**.

**Frontière canon (reconstruite)** :

- **People** tient la **carte de charge** (qui porte combien de mandats).
- **Ops Batman** tient la **condition d'arrêt** (quand une procédure
  s'arrête, qui décide).
- Les deux se croisent quand un owner People est saturé mais qu'aucune
  condition d'arrêt Ops n'a été posée — la procédure continue, l'owner
  s'use, et la livraison dérive.

La frontière canon n'est pas écrite. Elle est **reconstituée** à partir
de la séparation veto (mandat vs procédure).

## Le cas limite : *« Méta Gouvernance »*

Coach OS nomme People *« RH & Méta Gouvernance »* (domaine 01 local),
ce qui ajoute la **gouvernance des skills L0** au périmètre People —
People sollicite Bill L0.2 Forge pour les injections de skills
(triplets 37 et 55). Le canon V4 ne dit pas si cette gouvernance
appartient à People ou à un domaine transverse (potentiellement IT).

**Standing** : divergence non arbitrée. Le corpus cite le canal Bill L0.2
Forge comme défini, mais ne dit pas qui en est propriétaire au rang B2.

## Liens

- [[green-lantern-people-veto-recrutement-sans-mandat]] — le veto qui
  tient le périmètre
- [[green-lantern-people-gats-assigned-needs-owner-dlq]] — les 3 états
  émis par ce périmètre
- [[green-lantern-people-raci-transverse-jamais-A]] — comment People
  agit quand une frontière est contestée
- [[b2-eight-domain-vetoes-catalogue]] — le veto Aquaman qui double le
  veto People côté Legal
- [[b2-pair-check-raci-by-rank]] — la matrice RACI par rang qui pose A
  = B2 en aval

## Note de confiance

**Reconstruit, à moitié étayé.** Le périmètre canon V4 est confirmé par
`eight-domain-avengers-wheel.md` + triplet 15. Les trois frontières
contestées sont **reconstruites** à partir des triplets 33/34 (People
vs TechRecruiting), du couple veto Aquaman × veto People (catalogue), et
du red flag #3 (charge). Le cas *« Méta Gouvernance »* est cité
verbatim dans Coach OS (`VP_AGENT.md`) mais le canon V4 ne le valide pas.
La numérotation Coach OS 01 vs canon 07 est documentée ailleurs (cf.
`batman-numerotation-coach-os-vs-canon-08.md` pour le même type de
divergence côté Ops).