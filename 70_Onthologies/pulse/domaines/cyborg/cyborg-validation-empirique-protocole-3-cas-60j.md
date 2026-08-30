---
type: Concept
title: Cyborg veto — protocole de validation empirique (cible 3 cas / 60 jours)
description: Le veto Cyborg (cloud-only sans chemin de sortie, triplet 29) est projeté par lecture critique du canon depuis le tour 1, mais n'a jamais été observé en cycle réel (convergence 8/8 domaines sur 0 packet mésoperpétuel, cf. ETAT_DOMAINES vague 2). Ce concept pose un protocole de validation empirique symétrique aux protocoles Superman/Flash/Batman tour 3 : 3 cas observés sur 60 jours, packet mésoperpétuel type par cas, 5 critères d'acceptance cumulatifs, 3 indicateurs globaux (couverture/distribution/vitesse), 3 conditions de mise à jour doctrine (confirmée/amendée/invalidée).
tags: [cyborg, it, veto, validation, empirique, protocole, 60-jours, cloud-only, chemin-sortie]
generated: { by: minimax-m3, at: 2026-08-19T08:10:00Z }
verified:
  - { by: process:lecture-corpus-cyborg-tour-4, at: 2026-08-19T08:10:00Z }
sources:
  - id: veto-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos — 3 propriétés obligatoires
    last_modified: 2026-08-19
  - id: cyborg-veto-concept
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-veto-cloud-only-sortie.md"
    title: Cyborg veto — cloud-only sans chemin de sortie (5 cas projetés + 4 abusifs)
    last_modified: 2026-08-19
  - id: superman-validation-protocole
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-veto-empirical-validation-protocole.md"
    title: Superman veto — protocole de validation empirique (cible 3 cas/60 jours)
    last_modified: 2026-08-19
  - id: flash-validation-protocole
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-veto-empirical-validation-protocole.md"
    title: Flash veto — protocole de validation empirique symétrique (vague 2)
    last_modified: 2026-08-19
  - id: triplet-cyborg-veto
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 29 (ligne 29) — Cyborg hasVetoOver cloud-only-sans-sortie"
    last_modified: 2026-08-17
  - id: b2-veto-amplification
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-veto-amplification-cycle.md"
    title: Amplification des vetos B2 — cycle, 3 conditions, D4
    last_modified: 2026-08-19
  - id: b2-meso-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — format canonique 7 champs obligatoires
    last_modified: 2026-08-19
  - id: cyborg-triplet-58
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-triplet-58-amplification-date-reversibilite-council-submission-draft.md"
    title: Cyborg — triplet 58 amplification date+réversibilité (draft Council)
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Cyborg veto — protocole de validation empirique

## Le problème — un veto projeté, jamais observé

`cyborg-veto-cloud-only-sortie.md` a projeté **5 cas concrets** de
déclenchement légitime du veto Cyborg (cloud-only sans chemin de
sortie documenté) :

1. Vendor SaaS GAFAM sans clause d'export — IaC absente.
2. Vendor PaaS avec IaC complète — clause contractuelle absente.
3. Migration cloud post-`ADR-OMK-004` (juin 2026) où le chemin
   de sortie n'est pas documenté pour Edge Runtime Vercel.
4. Self-host Dokploy (mort) — sandbox Dokploy résiduelle non
   réversible vers Coolify.
5. Variant AaaS Family/Home dormant Q3 2026 — infrastructure
   sans owner IT ni chemin de réversibilité.

**0 cas observé** en cycle réel (cf. ETAT_DOMAINES vague 2 convergence
*« 0 packet mésoperpétuel IT »* sur 8/8 domaines). Le veto est
**catégoriel** (cf. `b2-eight-domain-vetoes-catalogue.md` ligne 29
verbatim), mais sa propriété *« vérifiable par un tiers »* n'est
pas confirmée en pratique.

`superman-veto-empirical-validation-protocole.md` a posé le pattern
cible **3 cas / 60 jours** pour Superman (cf. vague 3). `flash-veto-
empirical-validation-protocole.md` (vague 2) a posé le même pattern
pour Flash. `batman-rapport-dom-tour-3` pose le pattern pour Batman.
Cyborg adopte le même protocole par symétrie avec les 4 autres
capitaines.

## La cible du protocole — 3 cas / 60 jours

### Pourquoi 3 cas

`b2-veto-amplification-cycle.md` §« Condition 1 » exige *« au moins
une observation documentée »* — c'est le minimum. Mais pour une
validation empirique du veto catalogue, **3 cas** est le seuil
canonique d'observation suffisante :

- 1 cas = observation isolée.
- 2 cas = pattern naissant, fragile (deux confirmations par le même
  observateur ne confirment rien).
- 3 cas = pattern confirmé, **avec distribution vraisemblable** (au
  moins 2 cas sur des pair-checks différents OU 2 fournisseurs
  distincts).

### Pourquoi 60 jours

Cycle 12WY = 90 jours typique. 60 jours = **2/3 du cycle** = fenêtre
suffisante pour observer un build actif + un déploiement vendor + un
cycle de revue. Au-delà de 60 jours, le cycle change et le snapshot
devient **historique** plutôt que **courant**.

`b2-harmonization-matrix-exploitable.md` §« Le seuil déclencheur »
pose la cadence hebdomadaire pendant les cycles de build actif.
60 jours = ~8 séances B2 Council, suffisant pour capter 3 cas si le
pattern est réel.

## Le packet mésoperpétuel type — par cas observé

Chaque cas observé est consigné en **un packet mésoperpétuel**
distinct (D4 append-only) :

```yaml
meso_decision_id: B2-MESO-DECISION-2026-NN
source_mandate: B1-B2-MANDATE-2026-NN  # ou B2-PEER-2026-NN
mode: handoff | negotiation
impacted_domains:
  - it
  - <legal | finance | ops | autres>
veto_invoked:
  captain: cyborg
  classe: cloud-only-sans-sortie
  sous_classe: <ex: vendor-saas-sans-iac | vendor-paas-sans-clause |
                edge-runtime-vercel | dokploy-residuel |
                variant-aaas-dormant-sans-owner>
  source_observation: <chemin ou URL du vendor ou de l'infra>
  motif_verification: <ex: "IaC Terraform absente — triplet contrat
                       + IaC + failover incomplet ; réversibilité
                       non documentée">
tradeoff: "Veto tient : mandat amendé ou retiré. Voir next_review."
decision: accepted | blocked | escalate_to_B1
red_flag: <no if not applicable>
proof_expected:
  - B2 gate IT update (system_state: SYSTEM_READY | QUARANTINE)
  - B3 proof path (Kang_Dynasty_chemin_sortie_documented | vendor_rejected | migration_cyborg_acted)
validation_empirique:
  cas_id: <ex: cyborg-veto-cas-01>
  cycle: 12WY-2026-Qx
  trigger: <ex: "Vercel Edge Runtime — IaC Node.js standard proposée, Edge Runtime exclu de l'IaC, chemin de sortie non documenté pour Edge">
  reponse: <ex: "Veto opposé, mandat amendé avec IaC complète incluant Edge Runtime en parallèle">
  lag_indicator: <ex: "30 jours après amendement, IaC Edge Runtime documentée et exécutée">
next_review: <date or cycle>
```

## Les 5 critères d'acceptance par cas

Pour qu'un cas soit **validé empiriquement**, les 5 critères doivent
être remplis cumulativement.

### Critère 1 — Le veto a été opposé formellement

Un veto projeté puis levé sans observation n'est pas un cas. Le veto
doit être consigné dans le packet mésoperpétuel avec `veto_invoked:
cyborg` et `classe: cloud-only-sans-sortie`.

### Critère 2 — Le motif cite le triplet canon incomplet

`b2-eight-domain-vetoes-catalogue.md` exige la propriété *«
vérifiable »* — le motif doit citer **le triplet canonique contrat +
IaC + failover incomplet** (cf. `cyborg-couplage-aquaman-
reversibilite.md` §« Le triplet canonique réversibilité = contrat +
IaC + failover »). Sans cette référence explicite, le veto n'est pas
vérifiable et le cas ne compte pas.

C'est le **critère le plus important** pour Cyborg : le triplet
**contrat + IaC + failover** est le motif canonique de réversibilité
documentée. Un veto sans référence à ce triplet est invalide
procédurealement.

### Critère 3 — Le mandat a été amendé ou retiré

Une des 3 issues canoniques du catalogue 8 vetos (mandat amendé,
mandat retiré, veto escaladé B1) doit s'appliquer. Un veto opposé
sans issue n'est pas un cas complet.

### Critère 4 — Le proof path montre la conséquence opérationnelle

Le proof path doit montrer **l'effet observable** du veto :
- Vendor rejeté et alternative souveraine proposée, OU
- IaC complète documentée et exécutée, OU
- Clause contractuelle ajoutée post-veto par Aquaman (couplage
  Legal × IT), OU
- Migration infra engagée avec chemin de sortie vérifié.

Sans proof path, le cas n'a pas de **trace vérifiable** par un tiers.

### Critère 5 — Le lag indicator à J+30 confirme

Un cas validé à 1 jour est un cas projeté. Un cas validé à
**J+30 jours** confirme que **la conséquence du veto tient dans le
temps** — pas seulement au moment de l'opposition. Pour Cyborg, le
lag indicator type est : *« IaC Edge Runtime documentée et exécutée
30 jours après amendement »* ou *« vendor alternatif souverain signé
et déployé 30 jours après rejet »*.

## Les 3 indicateurs globaux du protocole

Les 5 critères valent **par cas**. Les 3 indicateurs valent
**par cycle 60-jours**.

### Indicateur A — Couverture (nb sous-classes touchées)

Les 3 cas doivent toucher **au moins 2 sous-classes distinctes**
parmi : vendor-saas-sans-iac, vendor-paas-sans-clause,
edge-runtime-vercel, dokploy-residuel, variant-aaas-dormant-sans-owner.

Cible : couverture ≥ 2 sous-classes sur 3 cas. Si 3 cas touchent
uniquement *vendor-saas-sans-iac*, le pattern est trop étroit.

### Indicateur B — Distribution (nb agents B3 Kang Dynasty touchés)

Les 3 cas doivent impliquer **au moins 2 agents B3 Kang Dynasty
différents** parmi Kang Prime, Iron Lad, Scarlet Centurion,
Immortus, Victor Timely, Rama Tut.

Cible : distribution ≥ 2 agents sur 3 cas. Si 3 cas touchent
uniquement Kang Prime, le pattern est trop ciblé.

### Indicateur C — Vitesse (délai opposition → amendement)

Le délai entre **opposition veto** et **amendement mandat** doit
être ≤ **5 jours ouvrés**. Au-delà, le veto n'est pas **opérationnel**
— il traîne.

Cible : délai P50 ≤ 5 jours ouvrés, P90 ≤ 10 jours ouvrés.

## Les 3 conditions de mise à jour doctrine

À la fin des 60 jours, 3 issues selon les observations.

### Mise à jour 1 — Doctrine confirmée

Si les 3 cas remplissent les 5 critères + les 3 indicateurs sont aux
cibles, la doctrine catalogue Cyborg est **confirmée** par
observation. Le canon B2 catalogue 8 vetos peut ajouter une note :
*« Cyborg veto confirmé en cycle 2026-Qx »*.

### Mise à jour 2 — Doctrine amendée

Si 1+ indicateur est hors cible, la doctrine est **amendée**. Cas
typiques :

- Couverture insuffisante (< 2 sous-classes) → diversifier les cas
  sur les 5 sous-classes en cycle suivant.
- Distribution insuffisante (< 2 agents) → diversifier les cas sur
  d'autres agents Kang Dynasty.
- Délai P90 > 10 jours → allonger le délai d'amendement (peut
  signaler un veto **trop strict** qui bloque la production).

L'amendement peut aussi déclencher l'**amplification triplet 58**
déjà proposée par Cyborg (`cyborg-triplet-58-amplification-date-
reversibilite-council-submission-draft.md` tour 3) : *« date de
revue ≤30j + métrique de réversibilité »*.

### Mise à jour 3 — Doctrine invalidée

Si **0 cas** est observé en 60 jours (cible 3 cas non atteinte) ou
si **≥ 2 cas** sont des **veto abusifs** (rejected par arbitrage
Council), la doctrine Cyborg est **invalidée**.

L'invalidation n'est pas une dissolution du veto — c'est un **retour
à la case projet**. B1 doit réécrire la classe catalogue Cyborg (pas
une amplification, une réécriture).

## La responsabilité du protocole

### Cyborg porte la collecte

Cyborg collecte les 3 cas sur 60 jours. Le tri est **sa
responsabilité** en tant que captain du veto. Mais Cyborg ne peut
pas inventer des cas — chaque cas doit être **observé** par un B3,
un autre captain (Aquaman co-signe souvent le triplet réversibilité),
ou un fait documenté.

### Le Council arbitre la validation

À la fin des 60 jours, Cyborg soumet le bilan au Council. Le
Council tranche entre les 3 issues (confirmé, amendé, invalidé). Le
packet mésoperpétuel bilan a la forme :

```yaml
meso_decision_id: B2-MESO-DECISION-2026-XX
source_mandate: B2-PEER-2026-XX
mode: parallel
impacted_domains:
  - it
validation_empirique_bilan:
  captain: cyborg
  cycle: 12WY-2026-Qx
  cas_observés: 3
  cas_valides: <0|1|2|3>
  indicateur_couverture: <val>
  indicateur_distribution: <val>
  indicateur_vitesse_p50: <val>
  indicateur_vitesse_p90: <val>
  issue: confirmée | invalidée
  motif: <text>
decision: <accepted | blocked | escalate_to_B1>
proof_expected:
  - B2 gate catalog update
  - B3 proof path : les 3 cas individuels
next_review: <date>
```

### B1 tranche l'invalidation

Si la doctrine est invalidée, B1 réécrit la classe catalogue Cyborg.
La réécriture est une **réécriture de veto** (pas une amplification)
— unanimité 8/8 Council + B1 requises.

## Anti-pièges

- **Protocole sans cible chiffrée.** Le 3 cas / 60 jours est précis.
  Sans cible chiffrée, le protocole est un voeu.
- **Cas countedus sans critère 2 (motif triplet canon).** Un veto
  sans référence explicite au triplet *contrat + IaC + failover* n'est
  pas vérifiable — il ne compte pas. Spécificité Cyborg vs autres
  capitaines.
- **Cas countedus sans lag indicator J+30.** Un cas validé à J+1
  n'est pas un cas complet.
- **Bilan Council sans 3 cas minimum.** Si Cyborg n'observe que 1
  cas en 60 jours, le bilan remonte avec mention explicite : *«
  cycle incomplet, ré-évaluation dans 30 jours »*.
- **Doctrine invalidée par 2 cas abusifs isolés.** 2 cas abusifs sur
  3 observations = signal, pas invalidation. Invalidation seulement
  sur 0/3 ou ≥ 2 abusifs confirmés en arbitrage Council.
- **Confondre validation empirique et amplification triplet 58.**
  La validation empirique confirme ou amende la doctrine catalogue
  existante. L'amplification triplet 58 ajoute une exigence (date de
  revue + métrique réversibilité). Les deux sont cumulatives :
  validation empirique peut déclencher l'amplification, mais ne la
  substitue pas.

## Liens

- [[cyborg-veto-cloud-only-sortie]] — les 5 cas projetés + 4 abusifs
- [[b2-veto-amplification-cycle]] — la procédure d'amplification canonique
- [[b2-eight-domain-vetoes-catalogue]] — les 3 propriétés du veto
- [[b2-meso-decision-packet-spec]] — format packet canonique
- [[cyborg-couplage-aquaman-reversibilite]] — triplet canonique réversibilité
- [[cyborg-triplet-58-amplification-date-reversibilite-council-submission-draft]] — amplification candidate
- [[superman-veto-empirical-validation-protocole]] — modèle
- [[flash-veto-empirical-validation-protocole]] — symétrie Flash
- [[batman-rapport-dom-tour-3]] — symétrie Batman
- [[aquaman-couplages-invisibles-legal-it]] — couplage Legal × IT

## Note de confiance

**Projets, à moitié étayé.** Le protocole cible 3 cas / 60 jours est
**projeté** par lecture critique de `b2-veto-amplification-cycle.md`
§« Condition 1 » et de la cadence canonique matrice. Les 5 critères
d'acceptance par cas sont **reconstruits** par lecture des 3
propriétés obligatoires du catalogue 8 vetos + la pratique documentée
sur 3 autres capitaines (Superman, Flash, Batman). Le critère 2
(motif triplet canonique réversibilité) est **spécifique Cyborg**
parce que le veto cloud-only-sans-sortie **est** le triplet canon
contrat + IaC + failover — symétrie avec Aquaman §« Triplet canonique
réversibilité ». Les 3 indicateurs globaux sont **projetés** par
analogie avec les indicateurs de validation standard (couverture,
distribution, vitesse). Les 3 conditions de mise à jour doctrine
sont **reconstruites** par lecture critique de `b2-council-arbitrage-
rule.md` + `b2-eight-domain-vetoes-catalogue.md`. La responsabilité
tripartite Cyborg/Council/B1 est **projetée** par lecture critique
de la doctrine RACI par rang + escalier canonique. La cible 3 cas /
60 jours n'est **pas citée** comme chiffre canonique dans le corpus
— c'est une **cible opérationnelle** dérivée des cadences et des
conditions d'amplification.

**Statut** : protocole Cyborg posé en symétrie Superman/Flash/Batman,
en attente de soumission B2 Council (mode parallel, impacted_domains:
[it]). Compatible D4 append-only.