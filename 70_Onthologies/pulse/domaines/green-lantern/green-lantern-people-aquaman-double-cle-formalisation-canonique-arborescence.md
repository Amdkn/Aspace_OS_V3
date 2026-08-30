---
type: Concept
title: People × Aquaman — formalisation canonique de la double clef People + Legal
description: Le couplage People × Legal (cf. `green-lantern-people-couplages-invisibles.md` §« 5. People × Legal ») est reconstruit comme **double clef séquentielle** : People mandate (veto triplet 23), Aquaman acte (veto triplet 30). Le présent concept **formalise** la clef : 5 étapes séquentielles People → Legal, 3 cas d'application légitime, 3 cas d'application abusive, 4 cas de blocage d'une seule clef, et 1 clause de **passerelle** pour échec simultané. La double clef devient une **procédure catalogue** — pas un cas par cas.
tags: [people, green-lantern, legal, aquaman, double-clef, veto-sequentiel, formalisation, b2, catalogue]
generated: { by: minimax-m3, at: 2026-08-19T08:40:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-4, at: 2026-08-19T08:40:00Z }
sources:
  - id: couplages-invisibles-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-couplages-invisibles.md"
    title: "Tour 1 — Couplage People × Legal (double clef)"
    last_modified: 2026-08-19
  - id: veto-recrutement-tour-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-veto-recrutement-sans-mandat.md"
    title: "Tour 1 — Veto People triplet 23"
    last_modified: 2026-08-19
  - id: b2-eight-domain-vetoes-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: "B2 catalogue des 8 vetos — Aquaman Legal triplet 30"
    last_modified: 2026-08-19
  - id: triplet-30-aquaman-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 30 — Aquaman veto prestation sans accord écrit"
    last_modified: 2026-08-17
  - id: b2-council-arbitrage-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — règle d'arbitrage
    last_modified: 2026-08-19
  - id: perimetre-negatif-tour-3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/green-lantern/green-lantern-people-veto-perimetre-negatif.md"
    title: "Tour 3 — Veto People périmètre négatif"
    last_modified: 2026-08-19
okf_version: "0.2"
---

# People × Aquaman — formalisation canonique de la double clef

## Pourquoi formaliser maintenant

Le couplage People × Legal (cf. `green-lantern-people-couplages-invisibles.md`
§« 5. People × Legal ») est **reconstruit** depuis deux vetos catalogue
qui portent sur la **même signature** mais avec des focales
différentes :

- **Veto People (triplet 23)** — *« recrutement sans mandat écrit +
  critère de sortie »*. Focale : qui est recruté, pour quoi, jusqu'à
  quand.
- **Veto Aquaman Legal (triplet 30)** — *« engagement démarré sans
  accord écrit sur le périmètre et la propriété du livrable »*.
  Focale : périmètre du livrable, propriété intellectuelle,
  conditions de résiliation.

Le couplage est **double clef séquentielle** : People mandate, puis
Aquaman acte. Mais la **procédure** de la double clef n'est pas
formalisée — c'est un cas par cas reconstruit en pratique. Le présent
concept **formalise** la clef en **5 étapes séquentielles**, plus
**3 cas légitimes**, **3 cas abusifs**, **4 cas de blocage**, et
**1 clause de passerelle**.

## Les 5 étapes séquentielles

### Étape 1 — Mandat People (veto triplet 23)

**Acteur** : Green Lantern People (ou squad lead X-Men ProfessorX par
délégation).

**Output** : paquet People signé avec 5 champs obligatoires :

- **Rôle** — qui est recruté, périmètre fonctionnel.
- **Horizon** — date d'entrée, durée, cycle de revue.
- **Critère de sortie** — KPI tenure, livrable, condition de désassignation.
- **Sponsor B2** — captain B2 du domaine d'accueil.
- **Signature People** — Green Lantern ou délégation ProfessorX.

**Veto opposé** : mandat sans horizon, sans critère de sortie, sans
sponsor B2. Cf. `green-lantern-people-veto-recrutement-sans-mandat.md`
§« Cinq cas légitimes de veto ».

### Étape 2 — Pré-cadrage Aquaman (information)

**Acteur** : Aquaman Legal (capitaine) ou squad lead Eternals (Thena).

**Output** : avis de cadrage Legal sur les **conditions de l'accord**
à venir (IP, propriété, résiliation). Pas une signature — un cadrage
préalable.

**Délai** : J+5 après réception du mandat People.

**Note** : cette étape est **optionnelle** dans le cas d'un mandat
**simple** (par exemple, recrutement d'un agent générique). Elle est
**obligatoire** dans le cas d'un mandat **complexe** (par exemple,
recrutement avec IP partagée ou résiliation anticipée).

### Étape 3 — Accord de prestation Aquaman (veto triplet 30)

**Acteur** : Aquaman Legal (signature finale).

**Output** : accord de prestation avec 4 champs obligatoires :

- **Périmètre du livrable** — ce que la prestation produit.
- **Propriété intellectuelle** — qui détient les outputs.
- **Conditions de résiliation** — date, motif, préavis.
- **Signature Aquaman** — Aquaman Legal.

**Veto opposé** : accord sans périmètre, sans propriété, sans
résiliation. Cf. `b2-eight-domain-vetoes-catalogue.md` §« Veto Aquaman ».

### Étape 4 — Activation conjointe

**Acteur** : conjoint (Green Lantern + Aquaman).

**Output** : packet mésoperpétuel `B2-MESO-DECISION-YYYY-NN` avec
double signature (cf. `b2-meso-decision-packet-spec.md`).

**Délai** : J+0 synchrone (les deux signatures simultanées).

**Statut** : `accepted`. Le recrutement peut démarrer.

### Étape 5 — Dispatch B3 X-Men

**Acteur** : Green Lantern (dispatch) + ProfessorX (squad lead X-Men
par défaut, non nommé cf. tour 4 concept `xmen-effectif-canon-recompte-disk`).

**Output** : JTBD packet `B3-JTBD-YYYY-NN` (cf. `b2-b3-jtbd-handoff-contract.md`).

**Délai** : J+0 après activation conjointe.

## Les 3 cas d'application légitime

1. **Recrutement humain standard** — embauche d'un opérateur avec
   profil défini, mandat People + accord Aquaman en séquence. Cas le
   plus fréquent.
2. **Recrutement agent générique** — activation d'un agent B3 sans
   IP partagée. Étape 2 (pré-cadrage Aquaman) est optionnelle.
3. **Recrutement avec IP partagée** — par exemple, co-développement
   avec un partenaire externe. Toutes les 5 étapes sont obligatoires,
   l'étape 2 est critique.

## Les 3 cas d'application abusive

1. **Invoquer la double clef pour un re-scope** (cf. périmètre négatif
   People tour 3 §« 5 cas hors-périmètre »). Le re-scope d'un mandat
   existant ≤ 30j et ≤ 20% scope n'est pas un recrutement — la
   double clef ne s'applique pas.
2. **Invoquer la double clef pour bloquer un recrutement déjà mandaté**.
   Si People a signé son mandat (étape 1), Aquaman ne peut pas utiliser
   la double clef pour **renégocier** le mandat People. Il peut
   amender l'accord de prestation (étape 3), pas le mandat People.
3. **Invoquer la double clef pour une succession interne**. Une
   succession interne (CaptainAmerica Avengers → Hulk Avengers) n'est
   pas un recrutement — pas de double clef. Cf. `green-lantern-people-veto-perimetre-negatif.md`
   §« Cas 4 succession interne ».

## Les 4 cas de blocage d'une seule clef

### Blocage People seul (étape 1 veto)

**Cas** : Mandat People sans critère de sortie.

**Effet** : People oppose veto, Aquaman ne peut pas démarrer. Le
demandeur amendé le mandat (ajoute critère de sortie daté).

**Lever** : amendment du mandat + re-signature People.

### Blocage Aquaman seul (étape 3 veto)

**Cas** : Accord Aquaman sans propriété intellectuelle.

**Effet** : Aquaman oppose veto, People a déjà signé. Le demandeur
amendé l'accord (ajoute clause IP).

**Lever** : amendment de l'accord + re-signature Aquaman.

### Blocage simultané (les 2 veto en même temps)

**Cas** : Mandat People sans sponsor B2 **ET** accord Aquaman sans
résiliation.

**Effet** : les 2 veto ensemble — le recrutement est **gelé**.

**Lever** : la **clause de passerelle** (cf. § suivant).

### Blocage par un veto catalogue tierce

**Cas** : Batman Ops oppose veto *« procédure sans condition d'arrêt »*
sur le recrutement (par exemple, l'absence de condition d'arrêt
People → Aquaman).

**Effet** : veto tierce — les 2 clefs sont signées, mais le recrutement
est **bloqué** par Batman.

**Lever** : amendement de la condition d'arrêt (Batman) ou escalade
B1.

## 1 clause de passerelle — échec simultané

Quand les 2 clefs sont **simultanément bloquées** (rare mais prévu),
une **procédure de passerelle** est ouverte :

### Étape P1 — Constat Council

Le B2 Council **constate** l'échec simultané des 2 clefs. Le constat
est consigné en journal avec :

- **Les 2 vetos opposés** (motif verbatim).
- **Le captain demandeur** (qui a lancé le recrutement).
- **Le délai écoulé** depuis le constat.

### Étape P2 — Arbitrage Council

Le B2 Council tranche **3 issues** :

1. **Amendment conjoint** — le demandeur amende les 2 documents (mandat
   People + accord Aquaman). Les 2 captains resignent. **Résultat** :
   recrutement reprend.
2. **Escalade B1** — le Council ne peut pas trancher (par exemple,
   conflit de North Star). **Résultat** : `decision: escalate_to_B1`.
3. **Retrait du recrutement** — le demandeur retire le recrutement. **Résultat** :
   `decision: blocked`, motif double veto.

### Étape P3 — Consignation D4

L'issue est **consignée** dans le journal Council (D4 append-only).
La double clef devient un **précédent** pour les recrutements futurs.

## Anti-pièges

- **Confondre double clef et double signature.** Une **double signature**
  est un acte administratif (les 2 captains signent le même document). Une
  **double clef** est un **enchaînement** — chaque clef ouvre un
  cadenas différent. La passerelle ne fonctionne que sur la **double
  clef**, pas sur la double signature.
- **Pré-cadrage Aquaman ignoré.** L'étape 2 (pré-cadrage) est
  optionnelle pour les mandats simples, obligatoire pour les mandats
  complexes. Un recrutement à IP partagée qui omet l'étape 2 viole la
  procédure.
- **Activation conjointe sans pré-cadrage.** Si l'étape 2 est omise
  mais que l'étape 4 (activation) est tentée, les **deux** captains
  portent la responsabilité d'un démarrage sans cadrage. C'est un
  cas de **veto tierce potentiel** (Batman Ops *« procédure sans
  condition d'arrêt »*).
- **Clause de passerelle utilisée hors échec simultané.** La
  passerelle est **uniquement** pour les 2 clefs bloquées en même
  temps. Une seule clef bloquée **suit l'amendment** (cf. §« 4 cas
  de blocage »), pas la passerelle.

## Liens

- [[green-lantern-people-couplages-invisibles]] — le couplage source
- [[green-lantern-people-veto-recrutement-sans-mandat]] — veto People
- [[b2-eight-domain-vetoes-catalogue]] — veto Aquaman canonique
- [[green-lantern-people-veto-perimetre-negatif]] — périmètre négatif
- [[b2-council-arbitrage-rule]] — règle d'arbitrage Council
- [[b2-meso-decision-packet-spec]] — format packet mésoperpétuel
- [[green-lantern-people-council-submission-packet-draft-effectif]] — packet draft

## Note de confiance

**Reconstruit, à moitié étayé.** Le couplage People × Legal est
reconstruit depuis les triplets 23 et 30 (verbatim). Les 5 étapes
séquentielles sont **projetées** depuis la pratique RH et la
doctrine veto. Les 3 cas légitimes et 3 cas abusifs sont **projetés**
depuis les patterns typiques. Les 4 cas de blocage sont **projetés**
depuis la doctrine d'arbitrage Council. La clause de passerelle
est **projetée** depuis les 4 issues de la règle d'arbitrage
(amendé, retiré, escaladé, invalide). Le concept est un **draft
de procédure catalogue**, pas une procédure adoptée.
