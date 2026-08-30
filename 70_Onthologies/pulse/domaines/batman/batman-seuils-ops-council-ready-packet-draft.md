---
type: Concept
title: Seuils Ops — packet Council-ready pour les 4 seuils arbitraires
description: Batman ouvre 4 seuils en tour 3. Le présent concept les formalise en packet mésoperpétuel B2-MESO-DECISION-2026-NN draft, Council-ready : (1) Growth→Ops charge_derivee 30%, (2) Sales→Ops debit_signature 30%, (3) Product→Ops backlog_changelog 1.5x, (4) ratio Ops/Product supportable non chiffré. Pour chaque seuil, on pose critere, source, methode de mesure, RACI par rang, condition de revisitation. Packet prêt à soumission B2 Council sous reserve d'observation 3 cas/60j.
tags: [b2, ops, batman, seuil, packet, council-ready, charge-derivee, debit-signature, backlog-changelog, ratio-supportable]
generated: { by: minimax-m3, at: 2026-08-19T05:58:00Z }
verified:
  - { by: process:lecture-canon-b2-tour-4, at: 2026-08-19T05:58:00Z }
sources:
  - id: batman-couplage-superman
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-couplage-superman-growth-volume-charge.md"
    title: Couplage Ops×Superman-Growth volume charge derivee
    last_modified: 2026-08-19
  - id: batman-couplage-johnjones
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-couplage-john-jones-sales-taux-signature.md"
    title: Couplage Ops×JohnJones-Sales debit signature
    last_modified: 2026-08-19
  - id: batman-couplage-flash
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-couplage-flash-product-cadence-release.md"
    title: Couplage Ops×Flash-Product cadence release train
    last_modified: 2026-08-19
  - id: b2-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — le format canonique d'une décision B2
    last_modified: 2026-08-19
  - id: batman-empirical-validation
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-veto-empirical-validation-protocol.md"
    title: Veto empirical validation protocol — cible 3 cas/60j
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Seuils Ops — packet Council-ready pour les 4 seuils arbitraires

## Le trou que Batman ferme

Tour 3 ouvre 4 seuils **arbitraires** :
(1) `charge_derivee` Growth → Ops ≥ 30% déclenche red flag,
(2) `debit_signature` Sales → Ops ≥ 30% de la capacité Ops absorbe un trigger symétrique,
(3) `backlog_changelog` Flash → Ops ≥ 1.5x la cadence supportable,
(4) `ratio_supportable` Ops/Product non chiffré.

Le mot « arbitraire » est un signal de manque : un seuil qui n'est
pas Council-ready n'a pas de légitimité d'arbitrage. Batman propose
ici un **packet mésoperpétuel draft** qui rend les 4 seuils
soumissibles au Council.

## Le packet draft

```yaml
meso_decision_id: B2-MESO-DECISION-2026-NN
source_mandate: B2-PEER-2026-NN
mode: negotiation
impacted_domains:
  - ops
  - growth
  - sales
  - product
tradeoff: "Formaliser 4 seuils Ops de couplage comme red flags
  préventifs. Les 4 seuils étaient arbitraires en tour 3 ; le packet
  les pose Council-ready sous reserve d'observation 3 cas/60j par
  seuil. Conditions cumulatives : (a) seuils confirmés en cycle
  par 3 cas observés, (b) symmetrie Batman A sur #2 et #3 (par
  aval), (c) B3 proof path pour chaque cas observé. Failure modes :
  adoption avec cycle pilote 60j, rejet si 0 cas observable, escalation
  B1 si conflit de North Star."
decision: accepted
proof_expected:
  - B2 gate ops update (seuil_1_charge_derivee_confirmed)
  - B2 gate ops update (seuil_2_debit_signature_confirmed)
  - B2 gate ops update (seuil_3_backlog_changelog_confirmed)
  - B2 gate ops update (seuil_4_ratio_supportable_chiffre)
  - B3 proof path (3 cas/60j par seuil en cycle Coach OS)
next_review: 2026-11-15
```

Le packet est **draft** parce qu'il dépend de l'observation 3 cas/60j
(cible 0 cas/60j au 2026-08-19). Batman le soumet en l'état et le
Council peut le valider comme **« draft conditionnel »** — les seuils
sont Council-ready mais l'adoption est suspendue à l'observation.

## Les 4 seuils, un par un

### Seuil 1 — `charge_derivee` Growth → Ops ≥ 30%

**Critère** : la charge Ops générée par lead Growth (MQL convertis,
onboarding, support client) dépasse 30% du capacity Ops planifié.

**Source** : `batman-couplage-superman-growth-volume-charge.md` §« trigger
charge_derivee ».

**Methode de mesure** : `charge_derivee = (charge_livraison_onboarding
+ charge_support_lead) / capacity_ops_planifiee`. Mensuel, mesure
extractionnelle.

**RACI par rang** : A = B2 Ops (Batman), R = B3 Fantastic Four, C = B2
Growth (Superman), I = B1 + B3 Guardians.

**Condition de revisitation** : 30% ajuste à 25% si 3 cycles
consecutifs en rouge ; ajuste à 40% si 3 cycles consecutifs en vert
avec charge Ops < 25%.

**Cas abusif** : appliquer 30% en cycle de build actif sans mesure
historique. Le seuil n'a de sens qu'avec baseline 3 cycles.

### Seuil 2 — `debit_signature` Sales → Ops ≥ 30%

**Critère** : la charge Ops générée par les deals signés par JohnJones
(implémentation, configuration, onboarding) dépasse 30% du capacity
Ops planifié.

**Source** : `batman-couplage-john-jones-sales-taux-signature.md` §«
trigger debit_signature ».

**Methode de mesure** : `debit_signature = charge_implementation_deals_signes
/ capacity_ops_planifiee`. Hebdomadaire, sprint-level.

**RACI par rang** : A = B2 Ops (Batman), R = B3 Fantastic Four, C = B2
Sales (JohnJones), I = B1 + B3 Illuminati.

**Condition de revisitation** : symmetrique du seuil 1. 30% ajustable
sur 3 cycles.

**Cas abusif** : confondre `debit_signature` et `charge_derivee`. Les
deux mesurent Ops, mais le premier regarde l'amont Sales (deals
signés cette semaine) et le second l'amont Growth (leads convertis
sur 30-90 jours). Un débit qui double en 1 semaine n'est pas un
`debit_signature` mais un *one-shot* — ex : un deal enterprise
ponctuel. Le seuil 2 ne s'applique pas aux one-shots.

### Seuil 3 — `backlog_changelog` Flash → Ops ≥ 1.5x

**Critère** : la backlog de changelog (PRs mergées par Flash, à
documenter en runbook par Ops) dépasse 1.5x la cadence Ops
supportable.

**Source** : `batman-couplage-flash-product-cadence-release.md` §«
4 charges derivees changelog/runbook/monitoring/onboarding ».

**Methode de mesure** : `backlog_changelog = nb_PR_merges_non_documentees
/ cadence_runbook_ops_par_sprint`. Sprint-level.

**RACI par rang** : A = B2 Ops (Batman), R = B3 Fantastic Four, C = B2
Product (Flash), I = B1 + B3 Avengers.

**Condition de revisitation** : 1.5x ajustable à 1.2x ou 2.0x sur 3
cycles. La cadence Ops supportable est projetée — Batman doit
d'abord observer 3 sprints avant de figer le ratio.

**Cas abusif** : appliquer 1.5x sur un portfolio immature. Les
premiers sprints d'un projet n'ont pas de cadence Ops supportable
mesurable — c'est l'inverse qui est mesurable (combien Ops a
*réellement* tenu).

### Seuil 4 — `ratio_supportable` Ops/Product non chiffré

**Critère** : le ratio entre charge Ops et charge Product (Feature
sizes) doit être tel que Ops peut absorber un release train Product
sans saturation.

**Source** : `batman-couplage-flash-product-cadence-release.md` §«
ratio supportable Ops/Product non posé canoniquement ».

**Methode de mesure** : projetée. Trois pistes :
(a) `ratio_supportable = capacity_ops / capacity_product_release`,
(b) `ratio_supportable = sprint_nombre_PR_traitees / sprint_nombre_PR_merges`,
(c) `ratio_supportable = temps_runbook_documentation / temps_PR_merges`.

**RACI par rang** : A = B2 Ops (Batman), R = B3 Fantastic Four, C = B2
Product (Flash), I = B1 + B3 Avengers.

**Condition de revisitation** : le ratio doit être chiffré après 6
sprints minimum (6 observations × 3 méthodes = 18 mesures). Pas de
revisitation avant 6 cycles.

**Cas abusif** : fixer un ratio avant 6 sprints. Le risque est un
ratio fantaisiste qui devient un goalpost mouvant.

## Les trois conditions cumulatives d'adoption

1. **3 cas observés en 60 jours par seuil** (cf. `b2-veto-empirical-validation-protocol.md`).
   - Cible 0/60j au 2026-08-19.
   - La condition est non-négociable : un seuil sans cas observé est
     une projection, pas une règle.
2. **Symmetrie Batman A sur #2 et #3** (par aval, cf. `b2-pair-check-raci-by-rank.md`).
   - Batman A sur Sales → Ops et Product → Ops, dérive des pair-checks
     canoniques.
   - Batman C sur #4 Product → IT, par symétrie aval — Batman *reçoit*
     le transfert aval, donc Consulted sur le flux amont.
3. **B3 proof path** pour chaque cas observé.
   - Le proof path doit etre l'une des 4 formes canoniques (capture,
     log, métrique, témoignage client).
   - Sans proof path, le cas n'est pas un cas — c'est un témoignage.

## Les 4 issues possibles

1. **Adoption avec cycle pilote 60j** : les 4 seuils sont Council-ready,
   adoption immédiate, cycle pilote 60j, next_review 2026-11-15.
2. **Adoption partielle** : 1-3 seuils sur 4 sont Council-ready, les
   autres restent en draft. Cycle pilote étendu.
3. **Rejet si 0 cas observable** : aucun seuil n'a de cas observé après
   60j, le packet est archivé, Batman revient avec une version
   pré-conditionnelle.
4. **Escalation B1** : conflit de North Star non résolvable (ex. : «
   bloquer 30% du pipeline Growth pour cause de charge Ops » entre en
   conflit avec la North Star d'expansion).

## Anti-pièges

- **Seuil sans RACI par rang.** Un seuil sans A/R/C/I est une
  intention, pas une règle. Le captain qui dit « je trigger le seuil »
  sans être A est un operateur hors-légitime.
- **Mesure sans source.** Une mesure qui n'est pas extractionnelle
  (logs, base de données, runbook) est un chiffre. Batman exige
  extraction, pas déclaratif.
- **Cas abusif symmétrie.** Le seuil 4 doit être C-Operated sur B2
  Product (Flash), pas B2 Ops. Inverser la RACI inverse le sens de
  l'arbitrage.
- **Adoption avant 3 cas.** Le cycle pilote 60j exige 3 cas observés,
  pas 3 cas projetés. Les cas projetés sont des plausibles, pas des
 faits.

## Liens

- [[b2-meso-decision-packet-spec]] — le format canonique
- [[b2-veto-empirical-validation-protocol]] — la cible 3 cas/60j
- [[b2-pair-check-raci-by-rank]] — la matrice RACI par rang
- [[batman-couplage-superman-growth-volume-charge]] — source seuil 1
- [[batman-couplage-john-jones-sales-taux-signature]] — source seuil 2
- [[batman-couplage-flash-product-cadence-release]] — source seuils 3+4
- [[b2-council-arbitrage-rule]] — qui tient le Council

## Note de confiance

**Reconstruit, à moitié étayé.** Le format packet est tiré verbatim
de `b2-meso-decision-packet-spec.md`. Les 4 sources de seuil sont
posées en tour 3 mais leurs **chiffres** (30%, 30%, 1.5x) restent
projetés. La RACI par rang est alignée sur `b2-pair-check-raci-by-rank.md`
pour les 4 pair-checks concernes (#1 Growth→Sales, #2 Sales→Ops, #3
Product→Ops, #4 Product→IT). Le conditionnel 3 cas/60j est aligné
sur `b2-veto-empirical-validation-protocol.md`. Le packet est **draft
conditionnel** : il ne devient saisissable qu'après observation de
3 cas par seuil.
