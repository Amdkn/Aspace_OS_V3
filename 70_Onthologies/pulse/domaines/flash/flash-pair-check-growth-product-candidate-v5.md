---
type: Concept
title: Flash — pair-check Growth → Product candidat V5
description: Le couplage indirect Growth → Product est le dernier des 4 non-canoniques encore ouvert (cf. RAPPORT_dom-flash.md §5.2). Quand Superman signale un besoin ICP/persona sans scope formalisé, Flash reçoit en NEEDS_SCOPE. Sans matrice canonique, le B2 Council n'a pas de mécanisme pour bloquer le lancement d'un produit sans validation Growth. Ce concept propose l'amendement matrice V5 avec RACI Flash A / Superman C + 3 cas légitimes + 3 cas abusifs.
tags: [flash, growth, product, pair-check, growth-product, matrice-v5, amendment, icp, persona, scope]
generated: { by: minimax-m3, at: 2026-08-19T08:20:00Z }
verified:
  - { by: process:lecture-corpus-flash-tour-3, at: 2026-08-19T08:20:00Z }
sources:
  - id: flash-pair-checks-dependencies
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-pair-checks-dependencies.md"
    title: Flash Product — pair-checks et dépendances inter-domaines — §« Couplage indirect 3 — Growth → Product »
    last_modified: 2026-08-19
  - id: flash-pair-check-pp
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-pair-check-people-product-candidate-v5.md"
    title: Pair-check People → Product — candidat V5 (modèle structurel de ce concept)
    last_modified: 2026-08-19
  - id: b2-pair-check-raci
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang sur les 9 pair-checks (A = B2 en aval)
    last_modified: 2026-08-19
  - id: b2-veto-amplification
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-veto-amplification-cycle.md"
    title: Procédure d'amendement matrice (unanimité + escalate B1)
    last_modified: 2026-08-19
  - id: b2-harmonization-exploitable
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — 9 critères + 5 red flags
    last_modified: 2026-08-19
  - id: b3-veto-vocabulary
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-veto-and-signal-vocabulary.md"
    title: B3 gates — Flash = PRODUCT_READY / NEEDS_SCOPE / BLOCKED_DELIVERY
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Flash — pair-check Growth → Product candidat V5

## Le dernier couplage indirect ouvert

`flash-pair-checks-dependencies.md` §« Couplage indirect 3 — Growth → Product » pose l'asymétrie :

> *« Superman (Growth) signale un besoin marché. Flash doit matérialiser ce besoin en produit. Le transfert n'est pas formalisé dans la matrice — Growth est la source amont du signal, mais la matrice ne pose pas explicitement le pair-check Growth → Product. »*

Le rapport tour 2 (`RAPPORT_dom-flash.md` §5.2) identifie explicitement ce couplage comme **le dernier ouvert** après les amendements People → Product (concept #2 tour 2) :

> *« 3/4 fermés, 1/4 reste : Growth → Product. »*

Ce concept propose l'amendement matrice V5 avec RACI Flash A / Superman C, en miroir de la structure du pair-check People → Product (concept #2 tour 2).

## Le transfert Growth → Product — ce qui passe

### Le besoin amont (depuis Superman / Guardians)

Superman signale un **besoin marché** identifié par l'ICP (Ideal Customer Profile), la persona cible, ou un signal de demande non qualifiée. Le format canonique d'un signal Growth :

```yaml
signal_growth_id: B2-SIGNAL-GROWTH-YYYY-NN
source: paid_media | content | referral | churn_signal
icp: <description de la cible>
persona: <description du buyer>
intent: <besoin exprimé par le marché>
qualification: MQL | SQL | opportunity | commitment
```

**Condition de réception par Flash** : Superman émet `GROWTH_READY` ET le signal est qualifié en MQL minimum.

### Le transfert vers Flash

Flash reçoit le signal et doit :
1. **Qualifier en scope** (chiffrer en heures, DoD, livrables) — sans scope, Flash émet `NEEDS_SCOPE` (cf. `b3-veto-and-signal-vocabulary.md`).
2. **Mapper aux pair-checks canoniques** — le scope Growth → Product déclenche en cascade les pair-checks #6 (Finance → Product, budget de build) et #8 (Legal → Product, frontières IP/privacy/terms).
3. **Émettre `PRODUCT_READY`** quand le scope est formalisé et la squad Avengers peut livrer.

## Le RACI par rang proposé

| Rôle | Acteur |
|---|---|
| **A** (Accountable) | Flash (Product) |
| **R** (Responsible) | Avengers (squad B3) |
| **C** (Consulted) | Superman (Growth), Guardians (squad B3) |
| **I** (Informed) | B1, B3 Illuminati (Sales), B3 Thunderbolts (Finance) |

**Justification** : Flash porte la responsabilité de **transformer un signal non-scopé en artefact livrable**. Superman est consulté parce que le signal est son unité native de parole (la promesse marché) — mais c'est Flash qui décide si le scope est tenable. Cette asymétrie est cohérente avec le RACI par rang canonique (`b2-pair-check-raci-by-rank.md` §« Pourquoi A = B2 en aval, pas B1 ») : A est **toujours le B2 captain en aval de la transition**.

## Question de garde — formalisation V5

| # | Question | Réponse exigée pour passer le pair-check |
|---|---|---|
| 10 | **Growth → Product** | Le signal marché est-il transformé en scope reproductible ? |

**Critère d'acceptance chiffré** : le scope est formalisé dans un `JTBD-FLASH-YYYY-NN` avec :
- `intent` du signal Growth mappé sur un intent Product
- `heures_estimées` ou `points` chiffrés
- DoD explicite (≥ 1 critère de valeur, ≥ 1 critère de run, ≥ 1 critère de sunset — cf. `flash-doD-build-run-sunset-three-stages.md`)
- Squad B3 cible identifiée (Avengers CaptainAmerica squad lead)

## Trois cas de déclenchement légitimes

### Cas légitime 1 — Signal ICP-persona net

**Symptôme** : Superman qualifie un signal avec ICP précis (ex : *« coachs business premium US, $7.5-25K ACV, 50-200 employés SaaS »*) et persona identifié (ex : *« fondateur CEO, premier coach embauché, sensibilité méthode »*).

**Action Flash** :.scope reproductible (produit SaaS builder ciblé US premium), `PRODUCT_READY` en moins de 2 sprints.

**Justification RACI** : Superman a fait le travail amont (qualification), Flash matérialise. A = Flash est légitime.

### Cas légitime 2 — Signal churn_aggregation

**Symptôme** : Superman détecte un pattern de churn agrégé (≥ 5 clients sur 30 jours) qui pointe un défaut de scope produit (ex : *« feature X sous-utilisée par 30% des clients payants »*).

**Action Flash** : investigation scope (`NEEDS_SCOPE` ou re-build de feature X), `PRODUCT_READY` après pivot.

**Justification RACI** : Superman a remonté un signal marché (churn), Flash arbitre sur la réponse scope (deprecation, refonte, ou nouvelle feature).

### Cas légitime 3 — Signal content-amplification

**Symptôme** : Superman amplifie un contenu qui révèle un besoin non-anticipé (ex : *« 10K lectures sur 'comment scaler mon coaching premium' »*).

**Action Flash** : ajoute au backlog Product, qualification en `NEEDS_SCOPE` puis `PRODUCT_READY` après MVP.

**Justification RACI** : le signal est faiblement qualifié (MQL, pas SQL), mais c'est un signal de besoin marché légitime. Flash arbitre sur la matérialisation.

## Trois cas abusifs — où le pair-check **ne devrait pas** s'opposer

### Cas abusif 1 — Superman impose le scope

**Symptôme** : Superman qualifie un signal ET définit le scope technique (ex : *« ICP coachs US, scope = SaaS builder avec feature AI scoring intégrée »*). Superman impose une stack technique ou un périmètre fonctionnel.

**Distinction** : le veto porte sur l'**offre dépersonnalisée** (Flash), pas sur le **périmètre fonctionnel**. Si Superman définit le périmètre, c'est une violation de la matrice canonique (Flash = A sur scope, pas Superman).

**Refus** : Flash oppose son veto (catégoriel — `valeur-nominative` étendue) : *« Superman définit un périmètre technique qui rend la valeur d'artefact dépendante d'une stack particulière. »* Cf. `flash-veto-offre-depersonnalisee.md` cas 3 (single point of failure technique).

### Cas abusif 2 — Superman bloque le scope sans signal

**Symptôme** : Superman oppose un veto sur un scope Product sans qu'il y ait de signal marché identifié (ex : *« pas de MQL pour cette feature, ne pas développer »*).

**Distinction** : le veto Growth porte sur la **promesse publique** (Superman bloque ce que la delivery ne tient pas — cf. triplet v3 ligne 27). Il ne porte pas sur le scope technique. Si Superman bloque sans signal, c'est un abus de position.

**Refus** : Flash remonte le veto Growth non-étayé en séance Council, mode **negotiation**. Si Superman ne produit pas de signal Growth qualifiant, le veto tombe.

### Cas abusif 3 — Superman consumes Product sans feedback

**Symptôme** : Superman utilise un artefact Product pour scaler l'attention (campaign, content) sans donner de feedback à Flash sur la réception marché.

**Distinction** : le pair-check Growth → Product est **bidirectionnel** dans son effet, mais le RACI est单向 (A = Flash). Superman qui consomme sans feedback casse la boucle d'apprentissage.

**Refus** : Flash exige un retour Superman (`lag_indicator: feedback_loop_Growth`) dans le contrat B2 → B3 du paquet JTBD Avengers. Si Superman refuse, Flash consigne le déséquilibre dans le journal Council.

## La procédure d'amendement matrice V5

L'amendement matrice pour ajouter le pair-check #10 (People → Product, concept #2 tour 2) et #11 (Growth → Product, ce concept) exige la procédure canonique de `b2-veto-amplification-cycle.md` §« La procédure d'amendement » :

1. **Observation documentée** — cas réel de couplage Growth → Product non couvert par la matrice (déjà documenté dans `flash-pair-checks-dependencies.md` §« Couplage indirect 3 »).
2. **Draft d'amendement** en une phrase — *« ajouter le pair-check #11 Growth → Product avec RACI Flash A / Superman C / Avengers R / Guardians C / B1 I. »* (ce concept)
3. **Séance hebdomadaire B2 Council** — revue par les 7 autres capitaines.
4. **Trois issues** :
   - adoption (7/8 ou 8/8)
   - rejet (5/8 contre)
   - escalate_to_B1 (3/8 contre ou désaccord profond)
5. **Archivage D4** dans le journal Council — append-only.
6. **Effet** : le pair-check #11 est cité dans tous les packets mésoperpétuels où la transition Growth → Product est en cause, à partir de la date d'effet.

**Note procédurale** : la procédure d'amendement matrice exige l'**unanimité** + escalate B1, pas la majorité simple (cf. `b2-veto-amplification-cycle.md` §« Confondre amplification et amendement de matrice »). C'est plus lourd qu'une amplification.

## Le seuil déclencheur — quand le pair-check #11 doit être ré-évalué

Trois contextes où le pair-check #11 doit être ré-évalué explicitement :

1. **Hebdomadaire** pendant les cycles de build actif (parallèle au pair-check #1 Growth → Sales).
2. **Immédiatement avant** un launch Growth-driven (campagne paid media à fort budget).
3. **Après** un B3 Guardian signalant un blocker (ex : ICP non-qualifié en MQL).

Sans cette cadence, le pair-check #11 devient un voeu, pas une garde.

## Anti-pièges

- **Confondre amplification et amendement.** Un pair-check est un **amendement matrice** (unanimité + B1), pas une **amplification** (majorité simple). Les deux passent par le Council, mais avec des majorités différentes.
- **Pair-check #11 utilisé comme blocage Growth.** Le pair-check ne donne pas un veto à Superman sur Product — il donne un RACI A à Flash sur scope. Superman est C, pas A.
- **Bidirectionnalité implicite.** Le pair-check #11 teste le transfert Growth → Product, pas l'inverse. Si Product signale un scope à Growth (rare), c'est un autre pair-check (potentiel #12 Product → Growth, à arbitrer).
- **Dépendance cachée à People → Product.** Les pair-checks #10 (People → Product) et #11 (Growth → Product) peuvent converger sur le même scope (ex : Superman signale ICP + Green Lantern onboarde CaptainAmerica sur ce scope). Le B2 Council doit traiter les deux amendements dans la même séance pour éviter les contradictions.

## Liens

- [[flash-pair-checks-dependencies]] — les 4 pair-checks canoniques + 3 couplages indirects
- [[flash-pair-check-people-product-candidate-v5]] — le pair-check #10 jumeau (People → Product)
- [[flash-domain-perimeter]] — la frontière #1 Sales ↔ Product (différente du pair-check #11)
- [[flash-jtbd-emit-receive]] — les 6 sources JTBD entrantes dont Growth
- [[b2-pair-check-raci-by-rank]] — le RACI par rang qui ancre A = B2 en aval
- [[b2-veto-amplification-cycle]] — la procédure d'amendement unanimité + B1
- [[b2-harmonization-matrix-exploitable]] — les 9 critères actuels qui attendent le #11
- [[b3-veto-and-signal-vocabulary]] — la gate `NEEDS_SCOPE` que le pair-check #11 doit résoudre

## Note de confiance

**Reconstruit, à moitié étayé.** `flash-pair-checks-dependencies.md` §« Couplage indirect 3 » est cité verbatim. Le RACI par rang (A = B2 en aval) est **canonique** mais marqué « reconstruit » dans `b2-pair-check-raci-by-rank.md`. La procédure d'amendement unanimité + escalate B1 est **verbatim** de `b2-veto-amplification-cycle.md` §« Confondre amplification et amendement de matrice ». Les 3 cas légitimes (ICP-persona, churn_aggregation, content-amplification) sont **projetés** à partir des 3 sources JTBD Growth documentées dans `flash-jtbd-emit-receive.md` §« 1. Growth (Superman / Guardians) » — extrapolés comme cas de pair-check, pas étayés par triplet canonique. Les 3 cas abusifs sont **reconstruits** par symétrie avec les 3 cas abusifs du veto catalogue (`flash-veto-offre-depersonnalisee.md` §« Trois cas abusifs »). Le seuil déclencheur est **repris** de `b2-harmonization-matrix-exploitable.md` §« Le seuil déclencheur ». Standing : draft d'amendement matrice V5, à soumettre B2 Council en séance hebdomadaire avec le pair-check #10 (People → Product) pour traitement conjoint.