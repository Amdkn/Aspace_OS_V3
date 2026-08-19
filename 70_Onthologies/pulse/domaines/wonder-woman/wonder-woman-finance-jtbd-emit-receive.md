---
type: Concept
title: Domaine Finance — paquets JTBD émis et reçus entre B2 (Wonder Woman) et B3 (Thunderbolts)
description: Le contrat bilatéral B2 → B3 Finance suit le gabarit canonique (B2-FINANCE-YYYY-NN pour les Rocks, B3-FINANCE-YYYY-NN pour les JTBD). Wonder Woman émet principalement vers B3 Thunderbolts (MRR reconciliation, margin analysis, cost hunt, compliance, reporting). Elle reçoit de B3 lespreuves (capture/log/métrique/témoignage) via les 4 formes canoniques. Trois failure modes typiques Finance : scope creep sur les "reports complets", silent rework sur les réconciliations, escalade tardive sur les runway <6 mois.
tags: [b2, b3, finance, jtbd, handoff, wonder-woman, thunderbolts, sprint, scrum, contract]
generated: { by: minimax-m3, at: 2026-08-19T03:44:00Z }
verified:
  - { by: process:lecture-domaine-finance-corpus, at: 2026-08-19T03:44:00Z }
sources:
  - id: jtbd-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: "B2 → B3 contract — quand une décision mésoperpétuelle devient un JTBD packet"
    last_modified: 2026-08-19
  - id: omk-rock-pipeline
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/06_Finance_WonderWoman_Thunderbolts/01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md"
    title: Rock → DoD → JTBD Pipeline
    last_modified: 2026-05-27
  - id: omk-swarm-protocol
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/06_Finance_WonderWoman_Thunderbolts/02_B3_SWARM_SUPERVISION_PROTOCOL.md"
    title: B3 Swarm Supervision Protocol (Finance)
    last_modified: 2026-05-27
  - id: thunderbolts-canon
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/06_Finance_WonderWoman_Thunderbolts/B3_Squad_Thunderbolts/00_B3_SQUAD_CANON.md"
    title: Thunderbolts — Finance Squad (CANON Notion)
    last_modified: 2026-05-28
  - id: finance-principles
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/06_Finance_WonderWoman_Thunderbolts/03_WONDERWOMAN_FINANCE_PRINCIPLES.md"
    title: Wonder Woman Finance Principles (v4)
    last_modified: 2026-06-25
okf_version: "0.2"
---

# Domaine Finance — paquets JTBD émis et reçus entre B2 (Wonder Woman) et B3 (Thunderbolts)

## Cadre : le contrat bilatéral canonique

Le contrat B2 → B3 est posé dans `b2-b3-jtbd-handoff-contract.md` :
B2 promet (DoD + impacted domains + proof_expected + next_review),
B3 promet (sprint d'exécution + proof path + lead/lag indicators +
chemin d'escalade). Pour le domaine Finance, ce contrat prend sa
forme canonique dans `01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md` (OMK) :
« B2 converts B1 vision into execution-ready swarm work without
collapsing into babysitting. »

Le format des identifiants est imposé :

- **B2-FINANCE-YYYY-NN** pour un Rock Finance (créé par Wonder Woman)
- **B3-FINANCE-YYYY-NN** pour un JTBD Finance (dispatché vers les Thunderbolts)

Cf. OMK `01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md` §« B2 Rock Packet ».

## Ce que Wonder Woman émet vers les Thunderbolts

### Catégorie 1 — Reconciliation et reporting (cadence calendaire)

Quatre paquets récurrents posés par la doctrine (SOPs canoniques) :

| Source Rock | JTBD type | SOP / KR | Cadence |
|---|---|---|---|
| B2-FINANCE-Recurring-Monthly-Reconciliation | B3-FINANCE-Monthly-MRR-Recon | SOP-L2-FINANCE-002 + F12 | Mensuelle (T+5) |
| B2-FINANCE-Recurring-Quarterly-Margin | B3-FINANCE-Quarterly-Margin-Analysis | SOP-L2-FINANCE-003 + F4 | Trimestrielle |
| B2-FINANCE-Recurring-Annual-Tax | B3-FINANCE-Annual-Tax-Filing | SOP-L2-FINANCE-004 + F10 | Annuelle |
| B2-FINANCE-Recurring-Pulse-Weekly | B3-FINANCE-Weekly-KPI-Pulse | KR-5d..g | Hebdomadaire |

Tous ces paquets ont une DoD **vérifiable par un tiers** (la règle
« DoD quality bar » du même fichier) : taux de réconciliation
≥100%, marge chiffrée, runway chiffré en mois.

### Catégorie 2 — Cost hunting et pricing (cadence à la demande)

| Source Rock | JTBD type | Principe F |
|---|---|---|
| B2-FINANCE-Phantom-Cost-Sweep | B3-FINANCE-Ghost-Phantom-Charges | F5 |
| B2-FINANCE-Pricing-Hypothesis-New-Offer | B3-FINANCE-Pricing-Hypothesis-Cost-Build | F4, F23 |
| B2-FINANCE-Recurring-Spend-Gate | B3-FINANCE-Recurring-Spend-Audit | Veto catalogue |
| B2-FINANCE-Reinvestment-Surplus | B3-FINANCE-Treasury-Allocation | F19-F22 |

Le **Recurring-Spend-Audit** est déclenché par le veto catalogue :
chaque dépense récurrente détectée dans un packet mésoperpétuel
sans date de revue ni métrique produit un B3-FINANCE-Recurring-Spend-Audit
consigné en marge du packet source.

### Catégorie 3 — Gates transverses (Build Gates)

Le control room OMK pose un gate Finance qui traverse **tout**
release payant :

> « No paid release can graduate without price hypothesis, cost
> estimate, margin risk, and billing/collection path. »
> — `00_B2_DOMAIN_CONTROL_ROOM.md` §« Gate »

Cela donne un paquet transverse :

- **B3-FINANCE-Paid-Release-Gate-Check** — ouvert par Wonder Woman
  en début de sprint, fermé par la preuve que les 4 conditions sont
  remplies (hypothèse de prix, estimation de coût, risque de marge,
  chemin de billing).

## Ce que Wonder Woman reçoit des Thunderbolts

Le contrat B2 → B3 prévoit 4 formes de preuve canoniques
(`b3-proof-path-4-formes`, cité dans
`b2-b3-jtbd-handoff-contract.md`). Pour Finance, ces 4 formes ont
des déclinaisons spécifiques :

| Forme canonique | Déclinaison Finance | Exemple |
|---|---|---|
| Capture | Capture d'écran Airtable `Finance_Pulse` KPI | Screenshot du dashboard Stripe |
| Log | Log Stripe / log Airtable / log code pipeline | Trace d'exécution du cron SOP-L2-FINANCE-002 |
| Métrique | Métrique chiffrée avec seuil | MRR ≥ X€, runway ≥ Y mois, overdue < 7j |
| Témoignage client | Témoignage Jerry/A0 sur lisibilité du dashboard | Validation verbale que le KPI est actionnable |

Wonder Woman **refuse** une preuve « capture » pour une métrique
qui exige un chiffre (un screenshot sans valeur ne prouve rien, F8
« readable dashboards »). Inversement, **refuse** une preuve
« métrique » pour une conformité binaire (F10 « filings on time »
ne se prouve pas par une moyenne, mais par un commit horodaté).

## Lead et lag indicators côté Finance

Le format conjoint du contrat B2 → B3 demande 1-3 lead indicators
(pendant l'exécution) et 1-2 lag indicators (après). Pour Finance,
les standards :

- **Lead — recouvrement** : % d'invoices envoyées <48h « Ready to
  bill » (cible 100%, alerte <95%).
- **Lead — réconciliation** : % de match Stripe ↔ Airtable sur la
  semaine courante (cible 100%).
- **Lag — MRR growth** : delta MoM (cible >10%, KR-5d).
- **Lag — runway** : mois restants au burn actuel (cible ≥12, alerte
  <6 = escalade Jerry, KR-5g).

## Trois failure modes typiques Finance

`b2-b3-jtbd-handoff-contract.md` §« Les trois failure modes » liste
scope creep, silent rework, escalade tardive. Pour Finance, leur
incarnation concrète :

### 1. Scope creep — le « reporting complet »

Symptôme : B3 Thunderbolts produit un rapport financier qui
couvre **plus** que ce que le JTBD demandait (par exemple : le
MRR mensuel demandé, plus un audit annuel complet, plus une revue
de pricing stratégique).

Cause typique : B3 confond « DoD rempli + scope élargi » avec
« valeur ajoutée ». Pour Finance c'est l'inverse — élargir le
scope sans amendement du packet mésoperpétuel dilue la proof path
et invalide la réconciliation.

Remède : Wonder Woman refuse la livraison excédentaire, consigne
le scope creep dans le journal Council, B3 réapprend la discipline
du périmètre.

### 2. Silent rework — la réconciliation non signalée

Symptôme : le B3 Thunderbolts a livré une réconciliation MRR,
mais a refait en cours d'exécution sans escalader. Le proof path
est conforme, mais le temps consommé a dépassé le cadre d'exécution
promis.

Cause typique : source Stripe ou Airtable a bougé pendant le
sprint (nouveau client, refund, dispute), B3 a corrigé sans
escalader.

Remède : Wonder Woman ouvre un arbitrage « rework non-escaladé »
en séance hebdomadaire. La sanction est sur la **discipline**, pas
sur le résultat — le B3 squad n'est pas puni pour avoir reworked,
mais pour ne pas l'avoir signalé. En Finance, ne pas signaler un
rework sur une réconciliation peut masquer un trou de runway
pendant 30 jours.

### 3. Escalade tardive — le runway bas tu

Symptôme : le B3 Thunderbolts a tenu jusqu'au bout du sprint
mensuel, puis a escaladé un runway de 5,5 mois (sous le seuil
KR-5g d'escalade à 6 mois). Le packet mésoperpétuel est exécuté
tard.

Cause typique : B3 a détecté la dérive à J+15 mais ne l'a pas
signalée — pensant que la moyenne du mois resterait au-dessus du
seuil.

Remède : Wonder Woman exige un « escalator register » pour le
sprint suivant — un journal court des blocers détectés, chacun
avec son horodatage et son escalade (ou son absence d'escalade).
Et escalade immédiate à Jerry si runway <6 mois sans attendre la
fin du sprint.

## Squad mapping — Thunderbolts members vs JTBD types

Le canon Notion (`00_B3_SQUAD_CANON.md`) attribue chaque membre
Thunderbolts à un principe :

| Membre | Principes | Type de JTBD dominant |
|---|---|---|
| Bucky Barnes (Lead) | F1, F4, F11 | Cadre d'exécution global, lead role |
| Yelena Belova | F2, F3 | Forecasting, scénarios pessimistes |
| Red Guardian | F7, F8 | Reporting, dashboards |
| Ghost | F5 | Phantom-cost sweep |
| Taskmaster | F9, F12 | Reconciliation, reproductibilité |
| U.S. Agent | F10 | Compliance, tax |

Le B3 squad lead (Bucky) signe conjointement le contrat B2 → B3.
Les autres membres opèrent sous son autorité directe sur des JTBD
ciblés. Le mapping est **indicatif** — un sprint peut mobiliser
plusieurs membres sur un même JTBD si la DoD le demande.

## Le rôle de Donna Safety Exit

`02_B3_SWARM_SUPERVISION_PROTOCOL.md` §« Donna Safety Exit » pose
une règle spécifique Finance :

> « If the swarm loops, fabricates proof, or keeps asking for
> permission instead of executing inside the contract, route the
> case to Donna/DLQ for safety review. »

Pour Finance, le loop typique est : B3 re-essaye la réconciliation
MRR après un échec sans escalader, refait la même erreur, jusqu'à
épuisement du cadre d'exécution. Le route vers Donna (DLQ) coupe
le cycle et force un arbitrage B2 sur le scope ou les sources.

Trois signaux de loop à observer :

1. **Reproductibilité cassée** (F9) — la même procédure donne un
   résultat différent sans changement de source.
2. **Preuve fabriquée** (F7) — log ou capture manifestement
   arrangée.
3. **Permissions-seeking répété** (anti-pattern B3) — B3 demande
   de l'approbation au lieu d'exécuter dans le contrat.

## Anti-pièges spécifiques au contrat Finance

- **Confondre cadence et urgence**. Les paquets « recurring » ont
  une cadence fixe (T+5 mensuelle, etc.). Wonder Woman qui ouvre
  un JTBD récurrent hors cadence doit justifier le déclencheur
  dans le packet.
- **Confondre preuve Finance et preuve Produit**. Une capture
  d'écran Stripe n'est pas une preuve Produit (et inversement).
  Chaque domaine a ses propres formes canoniques.
- **Cadre d'exécution trop court pour la réconciliation**. SOP
  -002 demande une réconciliation mensuelle T+5. Si le sprint
  B3 est de 2 semaines, le cadre est OK. Si le sprint est de 3
  jours, il est sous-dimensionné et la cadence mensuelle ne
  pourra pas être tenue.
- **JTBD Finance signé par un B3 squad autre que Thunderbolts**.
  Le format `B3-FINANCE-YYYY-NN` assigne implicitement la squad
  Thunderbolts. Wonder Woman ne signe pas un JTBD Finance avec un
  squad Avengers ou Guardians — c'est un mésusage du contrat.

## Liens

- [[wonder-woman-finance-frontiers]] — le périmètre racine
- [[wonder-woman-finance-couplings]] — qui dépend de Wonder Woman
- [[wonder-woman-recurrent-spend-veto]] — le veto catalogue
- [[b2-b3-jtbd-handoff-contract]] — la théorie du contrat
- [[b2-meso-decision-packet-spec]] — le format source

## Note de confiance

**Confirmé par machine.** Le format B2-FINANCE-YYYY-NN et B3-FINANCE-YYYY-NN
est cité verbatim d'OMK `01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md` et
`02_B3_SWARM_SUPERVISION_PROTOCOL.md`. Les 4 formes de preuve sont
posées dans `b2-b3-jtbd-handoff-contract.md`. Les 4 catégories de
JTBD (reconciliation, cost hunting, gates, pricing) sont **projetées**
à partir des SOPs canoniques (SOP-L2-FINANCE-001 à -004) et des
principes F1-F25. Les 3 failure modes sont **projetés** depuis la
théorie générale (`b2-b3-jtbd-handoff-contract.md` §« Les trois
failure modes ») instanciés sur les cas Finance typiques (recon,
rework, runway).
