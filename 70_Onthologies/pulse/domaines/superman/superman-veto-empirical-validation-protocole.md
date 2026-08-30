---
type: Concept
title: Superman veto — protocole de validation empirique (cible 3 cas / 60 jours)
description: Le veto Superman est projeté par lecture critique du canon (cf. veto-catalogue-concrete.md), pas observé en cycle réel. La doctrine canonique exige des vetos "vérifiables" et "catégoriels" — deux propriétés qui ne peuvent être confirmées qu'en cycle. Ce concept pose un protocole de validation empirique : 3 cas observés sur 60 jours, packet mésoperpétuel type par cas, 5 critères d'acceptance, 3 indicateurs de couverture/distribution/vitesse, 3 conditions de mise à jour doctrine.
tags: [superman, growth, veto, validation, empirique, protocole, 60-jours, doctrine]
generated: { by: minimax-m3, at: 2026-08-19T07:00:00Z }
verified:
  - { by: process:lecture-corpus-superman-vague-3, at: 2026-08-19T07:00:00Z }
sources:
  - id: veto-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos — 3 propriétés obligatoires
    last_modified: 2026-08-19
  - id: veto-catalogue-concrete
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/veto-catalogue-concrete.md"
    title: Veto Superman — 5 cas concrets (projetés) + 3 cas abusifs
    last_modified: 2026-08-19
  - id: council-cadence
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-cadence-and-chair.md"
    title: B2 Council — cadence hebdomadaire, revue des vetos en séance
    last_modified: 2026-08-19
  - id: triplet-58
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 58 — Wonder Woman étend doctrine (modèle d'amplification par cas)"
    last_modified: 2026-08-17
  - id: b2-meso-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — format canonique B2
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Superman veto — protocole de validation empirique

## Le problème — un veto projeté, pas observé

`veto-catalogue-concrete.md` a projeté **5 cas concrets** de
déclenchement légitime du veto Superman. Aucun n'a été
**observé en cycle réel** (cf. ETAT_DOMAINES vague 2 §Superman :
*« 0 cas observé de LAUNCH_READY rouge contesté par Summers en
cycle »* convergé sur 8 domaines). Les cas sont des
**projections critiques du canon**, pas des cas vécus.

Conséquence : la propriété *« vérifiable »* du veto n'est pas
confirmée en pratique. Le canon exige qu'un veto soit *«
vérifiable par un tiers qui n'est pas le captain »*, mais sans
cas observé, le motif du veto reste rhétorique.

## La cible du protocole — 3 cas / 60 jours

### Pourquoi 3 cas

`b2-veto-amplification-cycle.md` §« Condition 1 » exige *« au
moins une observation documentée »* — c'est le minimum. Mais
pour une validation empirique du veto catalogue, 1 cas est
insuffisant : un cas unique peut être un incident isolé.

**3 cas** est le seuil canonique d'**observation
suffisante** :

- 1 cas = observation isolée.
- 2 cas = pattern naissant, mais fragile (A/B identiques ne
  confirment rien si même observateur).
- 3 cas = pattern confirmé, **avec distribution vraisemblable**
  (au moins 2 cas sur des pair-checks différents ou des agents
  différents).

### Pourquoi 60 jours

Cycle 12WY = 90 jours typique. 60 jours = **2/3 du cycle** =
fenêtre suffisante pour observer un build actif + un launch +
un cycle de revue. Au-delà de 60 jours, le cycle 12WY change
et le snapshot devient **historique** plutôt que **courant**.

`b2-harmonization-matrix-exploitable.md` §« Le seuil
déclencheur » pose la cadence hebdomadaire pendant les cycles
de build actif. 60 jours = **~8 séances B2 Council**, suffisant
pour capter 3 cas par semaine si le pattern est réel.

## Le packet mésoperpétuel type — par cas observé

Chaque cas observé est consigné en **un packet mésoperpétuel**
distinct (D4 append-only). Le format type :

```yaml
meso_decision_id: B2-MESO-DECISION-YYYY-NN
source_mandate: B1-B2-MANDATE-YYYY-NN  # ou B2-PEER-YYYY-NN
mode: handoff | negotiation
impacted_domains:
  - growth
  - <autres>
veto_invoked:
  captain: superman
  classe: promesse-non-tenue
  sous_classe: <ex: claim-sans-date | demo-sans-dod |
                case-study-sans-contrat | integration-annoncee-avant-build |
                metrique-sans-source>
  source_observation: <chemin ou URL du livrable>
  motif_verification: <ex: pair-check #4 Product→IT non validé,
                       métrique return absente triplet 58>
tradeoff: "Veto tient : mandat amendé ou retiré. Voir
  next_review."
decision: accepted | blocked | escalate_to_B1
red_flag: <no if not applicable>
superman_reading: v4_canonical
proof_expected:
  - B2 gate update
  - B3 proof path
validation_empirique:
  cas_id: <ex: superman-veto-cas-01>
  cycle: 12WY-YYYY-Qx
  trigger: <ex: "Groot produit blog post ROI 30j non daté">
  reponse: <ex: "Veto oppose, mandat amendé avec date 30j">
  lag_indicator: <ex: "10 jours après amendement, livrable
                     publié avec date vérifiable">
next_review: <date or SALES_READY-event>
```

## Les 5 critères d'acceptance par cas

Pour qu'un cas soit **validé empiriquement**, les 5 critères
doivent être remplis cumulativement.

### Critère 1 — Le veto a été opposé formellement

Un veto projeté puis levé sans observation n'est pas un cas.
Le veto doit être consigné dans le packet mésoperpétuel avec
`veto_invoked: superman` et `classe: promesse-non-tenue`.

### Critère 2 — Le motif cite la pair-check matrice manquante

`b2-eight-domain-vetoes-catalogue.md` exige la propriété *«
vérifiable »* — le motif doit citer **la pair-check matrice
qui n'est pas validée** (cf. `veto-catalogue-concrete.md`
§« Pourquoi le veto Superman est le plus difficile à
opérationnaliser »).

C'est le **critère le plus important** : sans pair-check
matrice manquante citée, le veto n'est pas vérifiable et le
cas ne compte pas.

### Critère 3 — Le mandat a été amendé ou retiré

Une des 3 issues canoniques du catalogue 8 vetos (mandat
amendé, mandat retiré, veto escaladé B1) doit s'appliquer.
Un veto opposé sans issue n'est pas un cas complet.

### Critère 4 — Le proof path montre la conséquence opérationnelle

Le proof path doit montrer **l'effet observable** du veto :
livrable amendé, livrable retiré, escalade B1. Sans proof
path, le cas n'a pas de **trace vérifiable** par un tiers.

### Critère 5 — Le lag indicator à J+30 confirme

Un cas validé à 1 jour est un cas projeté. Un cas validé à
**J+30 jours** (lag indicator) confirme que **la conséquence
du veto tient dans le temps** — pas seulement au moment de
l'opposition.

## Les 3 indicateurs globaux du protocole

Les 5 critères valent **par cas**. Les 3 indicateurs valent
**par cycle 60-jours**.

### Indicateur A — Couverture (nb pair-checks touchés)

Les 3 cas doivent toucher **au moins 2 pair-checks différents**
parmi #1 (Growth→Sales), #5 (Finance→Growth), #7 (Legal→Growth)
+ red flag #2 Growth green Sales red.

Cible : couverture ≥ 2 pair-checks sur 3 cas. Si 3 cas
touchent uniquement le pair-check #1, le pattern est trop
étroit.

### Indicateur B — Distribution (nb agents B3 différents)

Les 3 cas doivent impliquer **au moins 2 agents B3 Guardians
différents** parmi StarLord, Rocket, Gamora, Drax, Groot,
Mantis (sans Peter_Quill — non créé sur disque).

Cible : distribution ≥ 2 agents sur 3 cas. Si 3 cas
touchent uniquement Groot, le pattern est trop ciblé.

### Indicateur C — Vitesse (délai opposition → amendement)

Le délai entre **opposition veto** et **amendement mandat**
doit être ≤ **5 jours ouvrés**. Au-delà, le veto n'est pas
**opérationnel** — il traîne.

Cible : délai P50 ≤ 5 jours ouvrés, P90 ≤ 10 jours ouvrés.

## Les 3 conditions de mise à jour doctrine

À la fin des 60 jours, 3 issues selon les observations :

### Mise à jour 1 — Doctrine confirmée

Si les 3 cas remplissent les 5 critères + les 3 indicateurs
sont aux cibles, la doctrine catalogue Superman est
**confirmée** par observation. Le canon B2 catalogue 8 vetos
peut ajouter une note : *« Superman veto confirmé en cycle
2026-Qx »*.

### Mise à jour 2 — Doctrine amendée

Si 1+ indicateur est hors cible, la doctrine est **amendée**.
Cas typiques :

- Couverture insuffisante (< 2 pair-checks) → ajouter un cas
  forcé sur un pair-check différent en cycle suivant.
- Distribution insuffisante (< 2 agents) → diversifier les
  cas sur d'autres agents B3.
- Délai P90 > 10 jours → allonger le délai d'amendement
  (peut signaler un veto **trop strict** qui bloque la
  production).

### Mise à jour 3 — Doctrine invalidée

Si **0 cas** est observé en 60 jours (cible 3 cas non atteinte)
ou si **≥ 2 cas** sont des **veto abusifs** (rejected par
arbitrage Council), la doctrine Superman est **invalidée**.

L'invalidation n'est pas une dissolution du veto — c'est un
**retour à la case projet**. B1 doit réécrire la classe
catalogue Superman (pas une amplification, une réécriture).

## La responsabilité du protocole

### Superman porte la collecte

Superman collecte les 3 cas sur 60 jours. Le tri est **sa
responsabilité** en tant que captain du veto. Mais Superman ne
peut pas inventer des cas — chaque cas doit être **observé**
par un B3, un autre captain, ou un fait documenté.

### Le Council arbitre la validation

À la fin des 60 jours, Superman soumet le bilan au Council.
Le Council tranche entre les 3 issues (confirmé, amendé,
invalidé). Le packet mésoperpétuel bilan a la forme :

```yaml
meso_decision_id: B2-MESO-DECISION-2026-XX
source_mandate: B2-PEER-2026-XX
mode: parallel
impacted_domains:
  - growth
validation_empirique_bilan:
  captain: superman
  cycle: 12WY-2026-Qx
  cas_observés: 3
  cas_valides: <0|1|2|3>
  indicateur_couverture: <val>
  indicateur_distribution: <val>
  indicateur_vitesse_p50: <val>
  indicateur_vitesse_p90: <val>
  issue: confirmée | amendée | invalidée
  motif: <text>
decision: <accepted | blocked | escalate_to_B1>
superman_reading: v4_canonical
proof_expected:
  - B2 gate catalog update
  - B3 proof path : les 3 cas individuels
next_review: <date>
```

### B1 tranche l'invalidation

Si la doctrine est invalidée, B1 réécrit la classe catalogue
Superman. La réécriture est une **réécriture de veto** (pas
une amplification) — unanimité 8/8 Council + B1 requises.

## Anti-pièges

- **Protocole sans cible chiffrée.** Le 3 cas / 60 jours est
  précis. Sans cible chiffrée, le protocole est un voeu.
- **Cas comptés sans critère 2 (motif vérifiable).** Un veto
  sans pair-check matrice manquante citée n'est pas
  vérifiable — il ne compte pas.
- **Cas comptés sans lag indicator J+30.** Un cas validé à
  J+1 n'est pas un cas complet — la trace n'est pas confirmée
  dans le temps.
- **BilanCouncil sans 3 cas minimum.** Si Superman n'observe
  que 1 cas en 60 jours, le bilan remonte avec mention
  explicite : *« cycle incomplet, ré-évaluation dans 30
  jours »*.
- **Doctrine invalidée par 2 cas abusifs isolés.** 2 cas
  abusifs sur 3 observations = signal, pas invalidation.
  Invalidation seulement sur 0/3 ou ≥ 2 abusifs confirmés en
  arbitrage Council.

## Liens

- [[veto-catalogue-concrete]] — les 5 cas projetés
- [[veto-amplification-candidate]] — l'amplification candidate
- [[amplification-council-submission-draft]] — le draft Council
- [[b2-veto-amplification-cycle]] — la procédure canonique
- [[b2-eight-domain-vetoes-catalogue]] — propriétés des vetos
- [[b2-meso-decision-packet-spec]] — format packet
- [[b2-council-cadence-and-chair]] — cadence hebdomadaire

## Note de confiance

**Projets, à moitié étayé.** Le protocole cible 3 cas / 60
jours est **projeté** par lecture critique de `b2-veto-amplification-cycle.md`
§« Condition 1 » et de la cadence canonique matrice. Les 5
critères d'acceptance par cas sont **reconstruits** par
lecture des 3 propriétés obligatoires du catalogue 8 vetos +
la pratique documentée (pair-check matrice manquante citée,
proof path, lag indicator). Les 3 indicateurs globaux sont
**projetés** par analogie avec les indicateurs de validation
standard (couverture, distribution, vitesse). Les 3 conditions
de mise à jour doctrine sont **reconstruites** par lecture
critique de `b2-council-arbitrage-rule.md` + `b2-eight-domain-vetoes-catalogue.md`.
La responsabilité tripartite Superman/Council/B1 est **projetée**
par lecture critique de la doctrine RACI par rang + escalier
canonique. La cible 3 cas / 60 jours n'est **pas citée**
comme chiffre canonique dans le corpus — c'est une **cible
opérationnelle** dérivée des cadences et des conditions
d'amplification.
