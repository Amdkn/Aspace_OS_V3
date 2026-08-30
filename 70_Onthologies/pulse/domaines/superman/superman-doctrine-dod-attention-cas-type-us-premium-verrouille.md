---
type: Concept
title: Superman DoD attention — verrouillage du cas-type US premium pivot Q4 2026
description: superman-dod-attention-procedure-canon.md (vague 3) pose 5 étapes pour fixer le DoD attention + 3 cas-types illustrés. Mais aucun DoD n'est verrouillé en packet mésoperpétuel. Ce concept applique la procédure au cas-type 1 (US premium pivot Q4 2026), produit le DoD chiffré avec 5 propriétés (catégoriel/vérifiable/non-négociable-mesoperpétuelle/daté/signé), et identifie les 3 leviers opérationnels (MQL qualifié, claim repositionné, post-mortem delivery).
tags: [superman, growth, dod-attention, verrouillage, us-premium, q4-2026, cas-type-1, packet]
generated: { by: minimax-m3, at: 2026-08-19T09:30:00Z }
verified:
  - { by: process:lecture-corpus-superman-vague-4, at: 2026-08-19T09:30:00Z }
sources:
  - id: dod-attention-procedure
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-dod-attention-procedure-canon.md"
    title: Superman DoD attention — procédure 5 étapes + 3 cas-types
    last_modified: 2026-08-19
  - id: mql-sql-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-mql-sql-handoff-contract.md"
    title: Superman MQL-SQL handoff contract — 3 seuils + 4 signaux
    last_modified: 2026-08-19
  - id: first-meso-packet
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-first-meso-decision-packet-template.md"
    title: Superman — template du premier packet mésoperpétuel
    last_modified: 2026-08-19
  - id: veto-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos — propriétés
    last_modified: 2026-08-19
  - id: b2-b3-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: B2 → B3 contract — DoD chiffré obligatoire
    last_modified: 2026-08-19
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — gates B2
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Superman DoD attention — verrouillage du cas-type US premium pivot Q4 2026

## Le problème — procédure sans DoD verrouillé

`superman-dod-attention-procedure-canon.md` (vague 3) pose **5
étapes** pour fixer le DoD attention + **3 cas-types** illustrés
(US premium, awareness prelaunch, SEO long terme). Mais le rapport
vague 3 note explicitement : *« aucun DoD canon n'est posé — la
procédure est mandat-spécifique »*.

**Ce concept applique la procédure au cas-type 1 (US premium pivot
Q4 2026)** et **verrouille** un DoD chiffré dans un format Council-
ready. Le verrouillage est la **différence** avec vague 3 : la
procédure vague 3 dit *comment fixer un DoD*, ce concept **applique
la procédure** pour un cas réel.

## Application des 5 étapes au cas US premium pivot Q4 2026

### Étape 1 — Mandat B1 reçu

Le mandat `B1-B2-MANDATE-2026-22` (cf.
`superman-first-meso-decision-packet-template.md` §« Le contexte
mandat B1 supposé ») pose le pivot US premium $7.5-25K ACV. B1
demande à B2 Council d'arbitrer les conflits cross-domaines.

### Étape 2 — 3 candidats DoD identifiés

`superman-dod-attention-procedure-canon.md` §« Étape 2 » identifie
3 candidats DoD pour le périmètre attention :

- **MQL qualifié** — le nombre de MQL premium par semaine.
- **Conversion MQL → SQL** — le taux de transformation Sales.
- **Reach** — le nombre d'impressions uniques sur LinkedIn ICP.

Pour le pivot US premium, **MQL qualifié** est le candidat principal
— la métrique est la plus directement liée à la **prise de parole
publique** (claim repositionné → MQL premium qualifié). Conversion
est secondaire (elle dépend de Sales). Reach est trop faible signal
(beaucoup d'impressions ne valent pas une parole utile).

### Étape 3 — Arbitrage JohnJones sur la conversion

Le candidat retenu par Superman Growth (MQL qualifié) doit être
**arbitré** par JohnJones Sales sur sa cohérence avec le contrat
MQL-SQL (cf. `superman-mql-sql-handoff-contract.md`). JohnJones
peut amender le DoD pour y ajouter une **composante conversion**
(exigence : *« 30 MQL premium/semaine ET taux conversion ≥25% »*).
**Dans notre cas**, JohnJones accepte MQL seul (la conversion est
suivie mais pas exigée dans le DoD).

### Étape 4 — Council désaccord → escalade B1

Si Superman et JohnJones sont en désaccord (par exemple Superman
veut 50 MQL/semaine, JohnJones veut 25 MQL/semaine + conversion
≥30%), **B2 Council tranche** selon la matrice de priorisation
(North Star > cycle > risque > effort). Si Council ne tranche pas,
**escalade B1**.

Dans notre cas, **pas de désaccord** — Superman propose 30 MQL
premium/semaine, JohnJones accepte. Le DoD est verrouillé sans
escalade B1.

### Étape 5 — Packet mésoperpétuel verrouillé

Le DoD est verrouillé dans un packet mésoperpétuel (cf.
`superman-first-meso-decision-packet-template.md`) avec
`proof_expected` qui inclut le compteur MQL.

## Le DoD verrouillé — 5 propriétés

Le DoD attention pour le cas US premium pivot Q4 2026 est :

```yaml
dod_attention_us_premium_q4_2026:
  énoncé: "Atteindre 30 MQL premium qualifiés par semaine pendant
    12 semaines (Q4 2026 : 13/10-31/12), avec taux de conversion
    MQL→SQL ≥25% suivi mais non-exigé."
  propriétés:
    catégoriel: |
      Le DoD porte sur la CLASSE "MQL premium qualifié" — pas sur
      une semaine particulière. Un DoD *« atteindre 30 MQL à la
      semaine 6 »* serait spécifique (pas catégoriel).
    vérifiable: |
      Le compteur MQL premium est mesuré par le dashboard ABM
      (B3 Guardians Peter_Quill orchestrateur). La métrique est
      exportée et vérifiable par un tiers (B2 Council, B3
      Illuminati, A0 audit).
    non_negociable_mesoperpetuelle: |
      Le seuil 30 MQL premium/semaine est verrouillé par packet
      mésoperpétuel B2-MESO-DECISION-2026-22. Le modifier
      nécessite un nouveau packet mésoperpétuel, pas un
      ajustement tactique.
    daté: |
      Horizon Q4 2026 (13/10-31/12). Après 31/12, le DoD est
      caduque et doit être renégocié pour Q1 2027.
    signé: |
      Double signature B2 sponsor (Superman) + B3 squad lead
      (Guardians — squad lead pas encore nommé, cf. vague 4
      concept Peter_Quill). La signature est dans le packet
      mésoperpétuel, avec mention explicite du trou squad lead.
  leviers_opérationnels:
    - MQL_qualifié: 30/semaine pendant 12 semaines
    - claim_repositionné: 5 claims repositionnés sur LinkedIn
      ICP US premium (cf. veto Superman catalogue)
    - post_mortem_delivery: revue mensuelle des claims émis vs
      delivery tenue (veto Superman respecté)
```

## Les 3 leviers opérationnels

Le DoD est **chiffré** par 3 leviers :

### Levier 1 — MQL qualifié

Métrique principale : **30 MQL premium qualifiés par semaine
pendant 12 semaines**. Total Q4 2026 : **360 MQL premium**.

Source de mesure : dashboard ABM (B3 Guardians Peter_Quill
orchestrateur + squad B3). Le seuil 30/semaine est aligné sur
l'ACV $7.5-25K (un commercial B3 Illuminati ferme en moyenne 12%
des MQL premium → 30 MQL × 12% = 3.6 deals/semaine ≈ 43 deals
Q4 → $7.5K ACV mid = $325K pipeline Q4).

### Levier 2 — Claim repositionné

Métrique secondaire : **5 claims repositionnés sur LinkedIn ICP US
premium** pendant Q4. Chaque claim est revu par Superman pour
**conformité veto** (la delivery doit tenir la promesse).

C'est l'application opérationnelle du veto Superman catalogue —
non pas en bloquant, mais en **reformulant** avant publication. Le
risque de veto opposé *post-publication* (delivery non tenue) est
réduit par la relecture préventive.

### Levier 3 — Post-mortem delivery

Métrique tierce : **revue mensuelle** des claims émis vs delivery
tenue. Trois signaux àtracker :

- Claim émis J → delivery tenue J+30 → OK (veto respecté).
- Claim émis J → delivery non tenue J+30 → alerte (veto enfreint
  a posteriori).
- Claim émis J → delivery non vérifiable J+30 → escalade Council.

Le post-mortem est la **boucle de rétroaction** qui valide (ou
invalide) le DoD en fin de cycle.

## Pourquoi ce DoD est tenable

Trois raisons défensables :

1. **Catégoriel et chiffré** — le DoD porte sur la classe *« MQL
   premium »* et le seuil 30/semaine est un chiffre mesurable, pas
   une intention.
2. **Vérifiable indépendamment** — le dashboard ABM est exporté,
   la métrique est lisible par un tiers (B2 Council, B3
   Illuminati, A0 audit). La propriété *« vérifiable »* du veto
   catalogue est restaurée par le DoD chiffré.
3. **Non-négociable au niveau mésoperpétuel** — toute modification
   du seuil 30/semaine exige un nouveau packet mésoperpétuel, pas
   un ajustement tactique. C'est la **protection contre le scope
   creep**.

## Anti-pièges

- **DoD canon unique pour Superman.** Non — le DoD est
  **mandat-spécifique**. Le cas US premium Q4 2026 a son DoD, le
  cas awareness prelaunch aura le sien, etc. Il n'y a pas de DoD
  canon Superman — il y a des DoDs mandat-spécifiques
  (vague 3 `superman-dod-attention-procedure-canon.md` §« Question
  ouverte #1 »).
- **30 MQL/semaine = chiffre arbitraire.** C'est un seuil projeté
  depuis l'ACV et le taux de conversion. Il **peut être ajusté**
  par packet mésoperpétuel amendé — mais l'ajustement doit être
  documenté, pas tacite.
- **Confondre MQL et conversion.** Le DoD exige MQL qualifié. La
  conversion est **suivie** mais pas exigée. Si Sales (JohnJones)
  veut imposer un seuil de conversion, c'est un DoD amendé, pas
  le DoD initial.
- **Oublier le trou squad lead.** La double signature B2 sponsor +
  B3 squad lead n'est **pas tenable** tant que le squad lead
  Guardians n'est pas nommé. C'est un **trou canonique** signalé
  par le concept Peter_Quill vague 4.

## Statut canonique

**Council-ready, pas Council-adopted.** Ce DoD est :

- **Proposé** par cette escouade Superman vague 4.
- **Formaté** selon les 5 propriétés catalogue (catégoriel /
  vérifiable / non-négociable-mesoperpétuelle / daté / signé).
- **Aligné** sur le mandat B1-US-premium-Q4-2026 (projeté par
  vague 3 procédure DoD attention).
- **Non soumis** — la procédure d'adoption est B2 Council + B1 +
  packet mésoperpétuel.

**Confiance** : *haute* sur la structure du DoD (5 propriétés
catalogue + 3 leviers), *moyenne* sur le seuil 30 MQL/semaine
(projection depuis ACV + taux conversion, pas mesuré en cycle).

## Liens

- [[superman-dod-attention-procedure-canon]] — la procédure 5 étapes
- [[superman-first-meso-decision-packet-template]] — le packet mésoperpétuel où ce DoD se loge
- [[superman-mql-sql-handoff-contract]] — le contrat MQL-SQL sous-jacent
- [[superman-peter-quill-7th-agent-mandate-spec]] — le mandat Peter_Quill orchestrateur
- [[b2-eight-domain-vetoes-catalogue]] — les 5 propriétés héritées
- [[b2-b3-jtbd-handoff-contract]] — DoD chiffré obligatoire
- [[superman-veto-catalogue-concrete]] — le veto Superman catalogue
- [[superman-veto-cycle-observation-empirical-gap]] — le gap 0/3 à diagnostiquer

## Note de confiance

**Verrouillage Council-ready.** Le DoD est verrouillé en suivant la
procédure vague 3, avec 5 propriétés catalogue explicites et 3
leviers opérationnels chiffrés. Le seuil 30 MQL/semaine est projeté
depuis ACV + taux conversion (12% — référence OMK), pas mesuré en
cycle. Le trou squad lead est signalé, pas résolu. **Confiance
haute** sur la structure, *moyenne* sur le seuil chiffré. **À
tester en cycle réel** par un mandat B1-US-premium-Q4-2026 reçu.
