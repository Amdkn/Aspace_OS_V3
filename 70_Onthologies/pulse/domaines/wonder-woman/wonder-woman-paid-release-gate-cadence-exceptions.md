---
type: Concept
title: Paid Release Gate Check — cadence d'ouverture, cycle de vie 5 phases, et 4 clauses d'exception
description: Le Paid Release Gate Check pose 4 conditions transverses sur toute release payante. La cadence d'ouverture du gate n'est pas explicitement posée. Le concept pose la cadence canonique (par release payante, T-1 sprint avant graduate) + 5 phases du cycle de vie (ouverture, preuve, revue, fermeture/consommation, post-mortem) + 4 clauses d'exception (compliance fiscale F10, prix stratégique, red flag #4 simultané, regression corrigée). Recommandation : ajouter un champ `gate_cadence_trigger` au packet mésoperpétuel.
tags: [b2, finance, paid-release-gate, cadence, cycle-de-vie, exceptions, build-gate, transversal, wonder-woman]
generated: { by: minimax-m3, at: 2026-08-19T05:45:00Z }
verified:
  - { by: process:lecture-corpus-wonder-woman-tour-3, at: 2026-08-19T05:45:00Z }
sources:
  - id: paid-release-gate-tour-2
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-paid-release-gate-finance.md"
    title: Build gate Paid Release Gate Check — la condition Finance transversale
    last_modified: 2026-08-19
  - id: omk-control-room-gate
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/06_Finance_WonderWoman_Thunderbolts/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: "OMK Finance — B2 Domain Control Room § Gate (4 conditions verbatim)"
    last_modified: 2026-05-27
  - id: thunderbolts-build-gates
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/06_Finance_WonderWoman_Thunderbolts/B3_Squad_Thunderbolts/00_B3_SQUAD_CANON.md"
    title: Thunderbolts canon — Build Gates types (SOPs + cadence)
    last_modified: 2026-05-28
  - id: sprint-cycle
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-cadence-and-chair.md"
    title: B2 Council — cadence hebdomadaire lundi matin
    last_modified: 2026-08-19
  - id: meso-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — le format canonique
    last_modified: 2026-08-19
  - id: f1-f25-mapping
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-finance-doctrine-f1-f25-mapping.md"
    title: Doctrine Finance F1-F25 — projection des 25 principes sur les outils
    last_modified: 2026-08-19
  - id: red-flag-4
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-red-flag-4-trigger.md"
    title: Red flag #4 — Finance red + Growth/Product green
    last_modified: 2026-08-19
  - id: f10-compliance-exception
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-f10-compliance-veto-exception-clause.md"
    title: F10 compliance fiscale — clause d'exception canonique au veto
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Paid Release Gate Check — cadence, cycle de vie 5 phases, clauses d'exception

## Le gate canonique et l'open question cadence

Le Paid Release Gate Check est posé verbatim dans
`00_B2_DOMAIN_CONTROL_ROOM.md` (OMK Finance, § « Gate ») :

> *« No paid release can graduate without price hypothesis, cost
> estimate, margin risk, and billing/collection path. »*

Le concept `wonder-woman-paid-release-gate-finance.md` (tour 2)
a posé le cycle de vie 5 phases (ouverture, preuve, revue,
fermeture, consommation par Product) et les 4 conditions
transverses. **La cadence d'ouverture du gate n'est pas
explicitement posée** — c'est un open question du rapport tour 2
(§ « Question 7 »).

## La cadence canonique recommandée — par release payante, T-1 sprint avant graduate

Trois cadences candidates examinées :

### Option 1 — Par release payante (recommandé)

Le gate s'ouvre **chaque fois qu'une release payante est prévue**.
C'est la cadence la plus stricte — elle garantit que **toute**
release payante passe par le gate.

**Avantage** : couverture 100% des releases payantes.
**Inconvénient** : coût opérationnel élevé si releases sont
fréquentes (>10/an).

**Déclencheur concret** : Wonder Woman ouvre le gate au début
du sprint B2 Finance **préalable** au sprint B3 Avengers qui
construit la release. Concrètement, **T-1 sprint** avant
graduate.

### Option 2 — Par sprint Finance (mensuel)

Le gate s'ouvre **à chaque sprint Finance** (4 sprints/mois,
cf. triplet 10). Si une release payante est prévue dans le
sprint, Wonder Woman ouvre le gate ; sinon, le gate reste
fermé.

**Avantage** : cadence stable, alignée avec le cycle B2
hebdomadaire.
**Inconvénient** : risque d'oubli si la release payante est
prévue hors sprint Finance.
### Option 3 — Par trimestre

Le gate s'ouvre **une fois par trimestre** pour batch de
releases.

Le de tr trimestre est **anti-pattern** : il laisse passer des
releases sans gate. Le B2 Council doit refuser la cadence
trimestrielle.

## Recommandation recommandée — par release payante

La cadence **recommandée** est l'**Option 1** : par release
payante, T-1 sprint avant graduate.

**Pourquoi cette cadence** :

- **Cohérence 100%** — toute release payante passe par le gate.
- **Synchronisation B3 Avengers** — T-1 sprint avant graduate
  garantit que les Avengers ont le scope et le cost estimate
  avant la dernière ligne droite.
- **Granularité compatible avec le sprint B2 Finance hebdo**
  (cf. `b2-council-cadence-and-chair.md`).

**Action attendue** : Wonder Woman ouvre le gate au début de
chaque sprint B2 Finance **préalable** au sprint B3 Avengers qui
construit la release. Le gate est consigné dans le SPRINT Finance
(`B2-FINANCE-YYYY-NN`) avec un champ `gate_cadence_trigger:
per_release_payante`.

## Cycle de vie 5 phases — formalisation

Le cycle de vie 5 phases posé par
`wonder-woman-paid-release-gate-finance.md` (tour 2) est
formalisé ici avec horodatages canoniques :

| Phase | Action | Durée cible | Trigger |
|---|---|---|---|
| **1. Ouverture** | Wonder Woman ouvre le gate, pose les 4 conditions | T-7 jours | Release payante planifiée |
| **2. Preuve** | Avengers + Kang Dynasty produisent les 4 preuves | T-7 → T-1 jour | Sprint B3 Avengers en cours |
| **3. Revue** | Wonder Woman revoit les preuves, statue | T-1 jour → T+0 | Fin de sprint B3 |
| **4. Fermeture** | Gate `accepted` ou `blocked`, packet mésoperpétuel | T+0 → T+1 jour | Issue phase 3 |
| **5. Consommation par Product** | Flash consomme le gate fermé pour graduate | T+1 jour → T+2 jours | Après gate fermé |

**Horodatage total** : 7 jours du T-7 au T+2 (release payante
standard). Pour les releases majeures (refonte pricing), étendre
à 14 jours.

## Post-mortem Phase 6 — la révision que le cycle ne pose pas

Le concept `wonder-woman-paid-release-gate-finance.md` pose 5
phases. **La Phase 6 (post-mortem) manque** — c'est un trou
canonique. Le post-mortem est important parce que le gate est
**transverse** (touche 4 captains) et les apprentissages doivent
être capitalisés.

### Phase 6 — Post-mortem (T+30 jours après graduate)

Wonder Woman organise un post-mortem avec les 4 captains (Wonder
Woman + Flash + Superman + Cyborg) :

- **Qu'est-ce qui a marché** : les 4 conditions validées, le
  gate fermé, le graduate réussi.
- **Qu'est-ce qui a coincé** : une condition insuffisamment
  chiffrée, un coût caché révélé, un billing path incomplet.
- **Action d'amélioration** : amendment de la doctrine, ajout
  d'une 5ᵉ condition, extension du gate à un autre périmètre.

**Livrable** : `gate_post_mortem_<release_id>.md` consigné dans
le journal Council avec action tracking pour le prochain cycle.

## Les 4 clauses d'exception au gate

Le gate est transversal et strict. Mais **4 clauses d'exception**
sont nécessaires pour ne pas bloquer les cas légitimes.

### Clause 1 — Compliance fiscale F10

Les paiements de compliance fiscale (TVA, IS, CVAE) ne
déclenchent **pas** le gate Paid Release — ils relèvent de
l'exception F10 (cf.
`wonder-woman-f10-compliance-veto-exception-clause.md`). Le gate ne
s'applique **pas** aux paiements fiscaux récurrents.

### Clause 2 — Pricing stratégique >15% discount

Un deal qui dépasse 15% discount (sign-off Wonder Woman
obligatoire, cf. F23) déclenche une revue de pricing
**distincte** du gate Paid Release. Les deux procédures sont
parallèles mais distinctes — la revue de pricing ne dépend pas
du gate.

### Clause 3 — Red flag #4 simultané

Si un red flag #4 (Finance red + Growth/Product green) est posé
en parallèle du gate, le **red flag prime**. Le gate est suspendu
jusqu'à résolution du red flag (cf.
`wonder-woman-red-flag-4-trigger.md`).

### Clause 4 — Régression corrigée <24h

Une release payante qui graduate avec une régression connue
(corrigée en <24h par un hotfix) peut bypasser le gate. La
condition : la régression est documentée dans le `scrums.md` du
B3 squad lead avec horodatage de la correction. Wonder Woman
peut refuser cette clause si la régression touche la marge
directement (ex : facturation incorrecte).

## Le format packet mésoperpétuel avec gate_cadence_trigger

Pour rendre la cadence explicite, le packet mésoperpétuel porte
un nouveau champ :

```yaml
meso_decision_id: B2-MESO-DECISION-YYYY-NN
source_mandate: B1-B2-MAN-YYYY-NN
gate_cadence_trigger: per_release_payante | sprint_finance | quarterly
gate_id: <gate_id>
gate_phase: ouverture|preuve|revue|fermeture|consommation|post_mortem
gate_decision: accepted|conditional|blocked
gate_exceptions: [F10_compliance, pricing_strategique, red_flag_4, regression_hotfix]
impacted_domains:
  - finance
  - product
  - growth
  - it
decision: accepted | blocked | escalate_to_B1
```

Le champ `gate_cadence_trigger` est compatible avec
`b2-meso-decision-packet-spec.md` — c'est un champ additionnel
qui ne casse pas le gabarit canonique.

## Anti-pièges

- **Cadence trimestrielle par commodité administrative.** Le
  trimestriel est **anti-pattern** : il laisse passer des
  releases sans gate. Le B2 Council doit refuser la cadence
  trimestrielle.
- **Phase 6 post-mortem oubli.** Sans post-mortem, les
  apprentissages gate ne sont pas capitalisés. Wonder Woman doit
  exiger la Phase 6 systématique.
- **Clause 4 (régression hotfix) abusive.** Une régression qui
  touche la marge ou la facturation ne peut pas être couverte
  par la clause hotfix. Wonder Woman refuse explicitement.
- **Confondre gate et veto catalogue.** Le gate teste la release
  payante (granularité large, transverse). Le veto catalogue
  teste la dépense récurrente (granularité fine, unaire). Ce
  sont deux outils distincts.
- **Ouvrir le gate T-1 sprint sans le fermer.** Un gate ouvert
  sans fermeture explicite est un gate non-vérifiable. Wonder
  Woman doit fermer le gate `accepted` ou `blocked` avant
  consumption par Flash.

## Liens

- [[wonder-woman-paid-release-gate-finance]] — le gate canonique (tour 2)
- [[wonder-woman-red-flag-4-trigger]] — le red flag qui prime
- [[wonder-woman-f10-compliance-veto-exception-clause]] — exception F10
- [[wonder-woman-finance-doctrine-f1-f25-mapping]] — la cartographie F1-F25
- [[b2-council-cadence-and-chair]] — la cadence sprint VP
- [[b2-meso-decision-packet-spec]] — le format packet avec gate_cadence_trigger
- [[b2-three-cooperation-modes]] — les 3 modes parallèle/handoff/negotiation

## Note de confiance

**Confirmé par machine** sur les 4 conditions du gate (verbatim
control room OMK § « Gate ») et sur la cadence sprint hebdo
(triplet 10). **Reconstruit** sur la cadence recommandée
(Option 1 par release payante) — projection depuis la doctrine
D4 append-only + le sprint B2 Finance. **Reconstruit** sur le
cycle de vie 5 phases + Phase 6 — extrapolation depuis le
concept tour 2. **Reconstruit** sur les 4 clauses d'exception —
projection depuis la doctrine F1-F25 + F23 + red flag #4. **À
valider en cycle réel** : (1) la cadence par release payante est
tenable pour >10 releases/an ? (2) la Phase 6 post-mortem est
réaliste ? (3) les 4 clauses sont acceptables par le Council ?
(4) le champ `gate_cadence_trigger` est compatible avec tous les
éditeurs YAML ?
