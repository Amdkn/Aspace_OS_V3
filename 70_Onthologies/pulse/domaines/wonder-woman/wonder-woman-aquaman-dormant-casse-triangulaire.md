---
type: Concept
title: Aquaman dormant casse le couplage triangulaire Sales×Finance×Legal — doctrine de fallback
description: Le couplage triangulaire Sales×Finance×Legal sur discount >15pct (concept 24) exige une co-signature Aquaman→WonderWoman→Sales. Si Aquaman est en état dormant (triplets 35-36 — depend on premier contrat signé), la chaîne est cassée en amont et le discount peut être conclu sans validation Legal. Cette page pose la doctrine de fallback : 4 cas asymétriques (Aquaman dormant >30j / Aquaman dormant mais signal B3 / Aquaman réveil / Aquaman SHADOW_ACTIVE), 3 mécanismes de compensation (escalade B1 Aquaman / signature WW seule avec clause reserve / gel discount), et le constat que la migration OMK Finance (concept 17) est plus urgente que Aquaman parce que Finance n'a pas de clause de dormance alors qu'Aquaman dort structurellement.
tags: [wonder-woman, finance, aquaman, legal, dormant, shadow-active, fallback, couplage-triangulaire, discount, escalation]
generated: { by: minimax-m3, at: 2026-08-19T06:55:00Z }
verified:
  - { by: process:lecture-corpus-tour-5, at: 2026-08-19T06:55:00Z }
sources:
  - id: aquaman-dormant
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-areas-dormants-doctrine.md"
    title: B2 Areas-dormants — la doctrine Aquaman
    last_modified: 2026-08-19
  - id: triplet-35
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 35 — Aquaman steward domaine-dormant"
    last_modified: 2026-08-17
  - id: triplet-36
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 36 — domaine-dormant depend on premier-contrat-signe"
    last_modified: 2026-08-17
  - id: omk-finance-control-room
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/06_Finance_WonderWoman_Thunderbolts/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: "OMK Finance — B2 Domain Control Room (status SHADOW_ACTIVE 2026-05-27)"
    last_modified: 2026-05-27
  - id: omk-aquaman-control-room
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: "Aquaman Legal — B2 Domain Control Room (status SHADOW_ACTIVE 2026-05-27)"
    last_modified: 2026-05-27
  - id: coupling-sales-discount
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-couplage-sales-discount-signoff.md"
    title: Couplage triangulaire Sales×Finance×Legal sur discount >15pct
    last_modified: 2026-08-19
  - id: f10-compliance
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-f10-compliance-veto-exception-clause.md"
    title: F10 Compliance fiscale — clause d'exception canonique
    last_modified: 2026-08-19
  - id: omk-finance-migration
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-omk-finance-active-migration-urgency.md"
    title: OMK Finance SHADOW_ACTIVE → ACTIVE migration urgence
    last_modified: 2026-08-19
  - id: b2-council-cadence
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-cadence-and-chair.md"
    title: B2 Council — cadence, présidence tournante, et mécanique de séance
    last_modified: 2026-08-19
  - id: vetos-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Aquaman dormant casse le couplage triangulaire Sales×Finance×Legal — doctrine de fallback

## Le problème posé en tour 4

Le tour 4 d'ETAT_DOMAINES (`ETAT_DOMAINES.md` ligne 21, WW tour 4) a
posé l'ouverture :

> Aquaman dormant casse régulièrement le couplage triangulaire
> Sales×Finance×Legal (renforce l'urgence migration OMK Finance→
> ACTIVE posé tour 3)

Le couplage triangulaire (concept 24) exige une co-signature en série
Aquaman (Legal) → Wonder Woman (Finance) → Sales (closing). Le triplet
35 pose Aquaman comme « steward domaine-dormant ». Le triplet 36 pose
« domaine-dormant depend on premier-contrat-signe ».

Tant qu'aucun contrat n'est signé, Aquaman est en état dormant — son
pair-check #7 (Legal → Growth) et #8 (Legal → Product) sont **non
déclenchés**. Le couplage triangulaire Sales × Finance × Legal est
cassé en amont.

Cette page pose la **doctrine de fallback** : 4 cas asymétriques selon
l'état d'Aquaman, 3 mécanismes de compensation.

## Les 4 états d'Aquaman (rappel)

D'après la doctrine `b2-areas-dormants-doctrine.md` :

| État | Description | Triplet |
|---|---|---|
| **DORMANT** | Aucun signal externe, DoD vide, captain consigné | 35 + 36 |
| **NEEDS_SIGNAL** | Signal externe détecté, attente déclencheur B3 | extension Superman 8×4 |
| **SHADOW_ACTIVE** | Premier contrat signé, doctrine activée | OMK 2026-05-27 |
| **ACTIVE** | Cadence normale, R R, A B2 sponsor | ACTIVE canonique |

**État actuel OMK Aquaman** (lecture `00_B2_DOMAIN_CONTROL_ROOM.md`) :
**SHADOW_ACTIVE 2026-05-27** — ni DORMANT, ni ACTIVE. Premier contrat
non signé, mais doctrine activée.

## Les 4 cas asymétriques (Wonder Woman × Aquaman)

### Cas 1 — Aquaman DORMANT (strict)

**Symptôme** : aucun contrat signé depuis >12 mois. Aquaman est en
DORMANT strict (triplets 35+36 cumulés). Le couplage triangulaire ne
peut pas déclencher.

**Mécanisme de fallback** :

1. **Gel discount** : Wonder Woman oppose le veto catalogue §06
   sur tout discount >15% invoqué par Sales, motif « absence de revue
   Legal amont — risque de non-conformité contractuelle ».
2. **Escalade B1** : Summers est saisi pour valider la procédure
   d'exception. La séance B2 ne peut pas trancher (Aquaman absent).
3. **Migration Aquaman trigger** : Summers peut déclencher la
   migration Aquaman SHADOW_ACTIVE → ACTIVE pour que le pair-check
   Legal reprenne.

**Implication WW** : ce cas est extrême. La doctrine F1-F25 impose un
runway floor — sans revue Legal, WW ne peut pas garantir que les
clauses contractuelles ne détruisent pas la valeur client.

### Cas 2 — Aquaman SHADOW_ACTIVE (actuel)

**Symptôme** : Aquaman est techniquement actif (doctrine activée), mais
sans closing réel. Le OMK Aquaman status SHADOW_ACTIVE 2026-05-27
correspond à cet état.

**Mécanisme de fallback** :

1. **Signature WW avec clause de réserve** : Wonder Woman signe le
   discount >15% avec une clause explicite « sous réserve validation
   Legal dès Aquaman ACTIVE ». Cette clause **n'est pas une renonciation**
   au veto — c'est une acceptation conditionnelle.
2. **Ping Aquaman** : Wonder Woman notifie Aquaman (par scrums.md ou
   par CaptainMarvel si Aquaman absent) que la signature est en
   attente d'activation Legal.
3. **Délai de grâce** : 30 jours après la signature WW, Aquaman
   doit avoir validé (ACTIF) ou contesté (veto §08). Sans réponse
   Aquaman sous 30j, escalade B1 Summers.

**Implication WW** : ce cas est le cas **actuel**. Le OMK Aquaman est
SHADOW_ACTIVE depuis 2026-05-27 (3 mois). La doctrine de fallback
doit prévoir un signal de transition (par ex. T+90j) avant que
l'absence Aquaman devienne structurelle.

### Cas 3 — Aquaman ACTIVE

**Symptôme** : Aquaman est en ACTIVE canonique — pair-checks #7, #8
déclenchés normalement. Le couplage triangulaire fonctionne en série.

**Mécanisme** : pas de fallback. Le concept 24 §« timing asymétrique
Aquaman 1-3j / WW 1-3j / Sales 3-9j » s'applique verbatim.

**Implication WW** : cas nominal. Pas d'adaptation nécessaire.

### Cas 4 — Aquaman NEEDS_SIGNAL (transitoire)

**Symptôme** : Aquaman a détecté un signal externe (ex : prospect
multi-year), mais n'a pas encore signé de contrat. État transitoire
entre SHADOW_ACTIVE et ACTIVE.

**Mécanisme de fallback** :

1. **WW peut bloquer le discount** si la non-conformité contractuelle
   est probable (par ex. : clause de juridiction non négociée, IP non
   déclarée).
2. **WW peut autoriser le discount** si le signal externe est documenté
   (par ex. : LOI signée, term sheet non équivoque).
3. **Aquaman doit activer sous 14 jours** : la transition NEEDS_SIGNAL
   → ACTIVE est rapide (signée = contrat). Au-delà, Aquaman reste
   en NEEDS_SIGNAL et le fallback Cas 2 s'applique.

**Implication WW** : cas rare mais observable. La doctrine F10
compliance (concept 18) peut aider à qualifier le signal externe
(comme base réglementaire).

## Le constat asymétrique — pourquoi Wonder Woman est plus urgente

L'asymétrie structurelle entre Wonder Woman et Aquaman est **décisive**
pour la migration OMK (concept 17) :

| Critère | Aquaman (Legal) | Wonder Woman (Finance) |
|---|---|---|
| **Dormance doctrine** | Oui (triplets 35-36) | Non |
| **Signal déclencheur** | Premier contrat signé | Aucun — Finance opère en continu |
| **OMK status** | SHADOW_ACTIVE 2026-05-27 | SHADOW_ACTIVE 2026-05-27 |
| **Runway floor** | N/A (pas de cash géré) | Oui (F1 doctrine) |
| **Cycle naturel** | Sub-cycle — dormant jusqu'au 1er closing | Continu — chaque sprint |
| **Cas de compensation** | Dormant → fallback par Summers | Pas de dormance → pas de fallback |

**Constat** : Aquaman dort structurellement par doctrine. Wonder Woman
**ne peut pas dormir** parce que la doctrine F1-F25 impose un suivi
continu (runway, MRR, marge). Si Wonder Woman était SHADOW_ACTIVE sans
migration ACTIVE, la doctrine F1-F25 reste en cycle (le OMK suit),
mais le **rang B2** n'est pas posé — WW reste un captain « in
name only » sans arbitrage Council réel.

**Recommandation** (renforce concept 17) :

1. **Wonder Woman saisit packet mésoperpétuel** `B2-MESO-DECISION-2026-31`
   pour migration OMK Finance → ACTIVE avec calendrier T+30/T+60/T+90.
2. **Aquaman NE saisit PAS** de packet équivalent — sa dormance est
   canonique (triplets 35-36), il n'a pas besoin de migrer tant qu'il
   dort.
3. **Summers arbitre** la priorisation migration : Wonder Woman avant
   Aquaman, parce que la doctrine F1-F25 l'exige en continu.

## Mécanisme de compensation 1 — Escalade B1 Aquaman

Quand Aquaman est DORMANT strict (Cas 1), Wonder Woman **ne peut pas
compenser seule**. Le veto catalogue §06 (dépense récurrente sans
date + métrique) ne suffit pas — il faut une revue Legal pour valider
que le contrat ne contient pas de clause qui dégrade le cash.

**Procédure** :

1. WW identifie que le discount >15% invoqué par Sales exige une revue
   Legal (ex : IP non déclarée, juridiction non négociée, RGPD non
   conforme).
2. WW oppose le veto §06 sur le discount — motif : absence Legal
   amont.
3. Sales escalade B1 Summers — motif : couplage triangulaire cassé.
4. Summers arbitre :
   - **Option A** : migration Aquaman SHADOW_ACTIVE → ACTIVE (1 sprint)
   - **Option B** : gel discount jusqu'à migration Aquaman
   - **Option C** : escalade Aquaman B1 (Aquaman est un B2 captain
     inactif — la migration est de la responsabilité de B1 par défaut)

**Coût** : 1 sprint de latence sur le closing Sales. Sans compensation,
le closing rate chute — Aquaman dormant bloque Sales.

## Mécanisme de compensation 2 — Signature WW avec clause de réserve

Quand Aquaman est SHADOW_ACTIVE (Cas 2), Wonder Woman signe le discount
>15% avec une **clause de réserve** explicite. Format packet :

```yaml
meso_decision_id: B2-MESO-DECISION-YYYY-NN
mode: negotiation
impacted_domains:
  - sales
  - finance
  - legal
tradeoff: "Discount prospect ACME 22pct — Aquaman SHADOW_ACTIVE (3 mois),
  Wonder Woman signe avec clause de réserve 'sous réserve validation
  Legal dès Aquaman ACTIVE'. Sales closing protégé."
decision: accepted
proof_expected:
  - B2 gate sales update (closing_pipeline_protected)
  - B2 gate finance update (discount_signoff_reserve)
  - B2 gate legal update (aquaman_activation_signal_received)
  - B3 proof path (Illuminati_ABM_discount_audit)
legal_reserve: true
legal_reserve_deadline: 30 jours après signature WW
next_review: 12WY-2026-Q4
```

**Champ `legal_reserve: true`** est **non-canonique** — projeté pour
adoption Council.

**Mécanisme juridique** : la clause de réserve n'est pas une
renonciation au veto — c'est une acceptation conditionnelle. Si Aquaman
conteste sous 30j, le discount est révoqué. Si Aquaman valide (ACTIF),
la clause devient caduque.

**Limite** : la clause ne couvre pas les cas où Aquaman dort
structurellement (Cas 1). Elle suppose qu'Aquaman peut valider sous
30j — si Aquaman reste SHADOW_ACTIVE 6 mois, la clause devient
caduque sans validation.

## Mécanisme de compensation 3 — Gel discount Aquaman dormant

Quand Aquaman est DORMANT strict ET le signal B1 n'aboutit pas (Cas 1
persistent), Wonder Woman peut opposer un **gel discount** cumulatif
avec le veto §06 :

```yaml
decision: blocked
motif: "Aquaman Legal dormant >12 mois — couplage triangulaire cassé.
  Wonder Woman oppose veto §06 cumul avec gel discount jusqu'à
  Aquaman ACTIVE ou escalade B1 formelle."
```

**Effet** : Sales ne peut pas close >15% discount tant qu'Aquaman
n'est pas ACTIF. Le pipeline commercial dégrade — c'est un trade-off
explicite : cash runway (sans Aquaman) vs closing rate (avec Aquaman).

**Coût** : Sales peut contester en Council — mais Aquaman étant dormant,
le Council ne peut pas trancher (pair-check Legal manquant). L'arbitrage
remonte Summers — la décision finale est B1.

## Recommandation — doctrine de fallback standard

Face aux 4 cas asymétriques, Wonder Woman pose la doctrine de fallback
standard suivante :

| État Aquaman | Action WW | Délai | Escalade |
|---|---|---|---|
| DORMANT > 12 mois | Gel discount cumul veto §06 | immédiat | B1 Summers |
| DORMANT 3-12 mois | Signature avec clause de réserve + ping Aquaman | 14j | B1 si Aquaman silencieux |
| SHADOW_ACTIVE | Signature avec clause de réserve + ping Aquaman | 30j | B1 si Aquaman silencieux T+90 |
| NEEDS_SIGNAL | Signature ou veto selon signal externe | 14j | B1 si Aquaman non ACTIF |
| ACTIVE | Signature normale (concept 24 timing) | 1-3j | aucune |

**Note** : les seuils 12 mois, 3 mois, 30 jours, 14 jours sont des
**extensions opérationnelles** projetées depuis la doctrine Aquaman
dormant. La doctrine canonique ne pose pas ces seuils.

## 4 cas abusifs à éviter

### Abus 1 — WW utilise Aquaman dormant comme excuse

Si WW invoque « Aquaman dormant » pour bloquer un discount qu'elle
refuse pour d'autres raisons (politique, défense de territoire),
c'est un **abus** — Aquaman dormant devient un prétexte. Anti-piège
analogue à `b2-eight-domain-vetoes-catalogue.md` §« Anti-pièges ».

### Abus 2 — Clause de réserve sans ping Aquaman

Si WW signe avec clause de réserve mais ne ping pas Aquaman (pas de
trace dans `signalements.md` ou scrums.md), la clause est non-vérifiable.
Aquaman ne sait pas qu'il doit valider. Le packet mésoperpétuel est
invalide.

### Abus 3 — Gel discount permanent

Si WW oppose le gel discount sansescalade B1, c'est une violation de
la cadence canonique — le gel doit être temporary, pas permanent.
Anti-piège : un gel > 90j sans escalade B1 = veto politique.

### Abus 4 — Migration Aquaman trigger par WW seule

WW ne peut pas déclencher la migration Aquaman SHADOW_ACTIVE → ACTIVE
— c'est une décision B1 (Summers arbitre) ou Aquaman lui-même (par
premier contrat signé). Si WW force la migration, elle franchit sa
frontière d'autorité.

## Anti-pièges globaux

- **Confondre Aquaman dormant et Aquaman inactif.** Un Aquaman dormant
  est un état canonique (triplets 35-36) ; un Aquaman inactif serait
  une dérive. Le OMK SHADOW_ACTIVE est dormant, pas inactif.
- **Croire que le couplage triangulaire fonctionne en DORMANT.** Il ne
  fonctionne pas — la doctrine est claire.
- **Considérer que le signal Aquaman ACTIVE est permanent.** Aquaman
  ACTIVE n'est pas un état figé ; il peut retomber en SHADOW_ACTIVE
  si le contrat expire. La doctrine de fallback doit s'appliquer
  continûment.
- **Penser que la migration OMK Finance ACTIVE résout le problème.**
  La migration WW ne change pas l'état Aquaman — Aquaman reste
  SHADOW_ACTIVE. WW ACTIVE + Aquaman SHADOW_ACTIVE = le couplage est
  fonctionnel côté WW mais cassé côté Aquaman.

## Liens

- [[b2-areas-dormants-doctrine]] — la doctrine Aquaman dormant
- [[b2-eight-domain-vetoes-catalogue]] — le veto §06 Wonder Woman
- [[b2-council-cadence-and-chair]] — l'escalade B1 par présidence tournante
- [[wonder-woman-couplage-sales-discount-signoff]] — couplage triangulaire
- [[wonder-woman-f10-compliance-veto-exception-clause]] — F10 compliance clause
- [[wonder-woman-omk-finance-active-migration-urgency]] — migration OMK Finance
- [[wonder-woman-veto-cascade-with-batman-ops]] — veto cascade Batman×WW
- [[wonder-woman-paid-release-gate-cadence-exceptions]] — cadence Paid Release Gate

## Note de confiance

**Confirmé par machine, à moitié.** Les triplets 35-36 et la doctrine
`b2-areas-dormants-doctrine.md` sont **lus** verbatim. Le statut OMK
SHADOW_ACTIVE 2026-05-27 est **cité** depuis `00_B2_DOMAIN_CONTROL_ROOM.md`.
L'asymétrie Aquaman dormant vs Wonder Woman non-dormant est
**construite** par lecture des triplets et de la doctrine F1-F25.
Les 4 cas asymétriques (DORMANT strict / SHADOW_ACTIVE / ACTIVE /
NEEDS_SIGNAL) sont **projetés** depuis les 4 états de la doctrine
Aquaman. Les 3 mécanismes de compensation (escalade B1 / clause de
réserve / gel discount) sont des **projections** depuis les outils
canoniques (veto §06, mésoperpétuel packet, escalade B1). Les seuils
12 mois / 3 mois / 30 jours / 14 jours sont des **extensions
opérationnelles** non-canoniques. Le champ packet `legal_reserve:
true` est **projeté** pour adoption Council. La recommandation
« Wonder Woman saisit packet mésoperpétuel migration avant Aquaman »
est une **remontée** vers B2 Council, pas une adoption.