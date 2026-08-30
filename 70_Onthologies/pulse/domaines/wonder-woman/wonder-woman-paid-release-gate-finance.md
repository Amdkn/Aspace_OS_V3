---
type: Concept
title: Build gate « Paid Release Gate Check » — la condition Finance transversale sur toute release payante
description: Le control room OMK pose un gate Finance transversal sur toute release payante : « No paid release can graduate without price hypothesis, cost estimate, margin risk, and billing/collection path ». Le gate est ouvert par Wonder Woman en début de sprint, fermé par la preuve des 4 conditions, et consommé par Product (Flash) pour autoriser le graduate. Le gate n'est ni un veto catalogue (il porte sur le produit, pas sur la dépense) ni un pair-check (il teste la sortie, pas la transition). C'est un outil distinct qui protège la solvabilité de chaque release.
tags: [b2, finance, build-gate, paid-release, gate, transversal, pricing, cost-estimate, margin, billing]
generated: { by: minimax-m3, at: 2026-08-19T04:45:00Z }
verified:
  - { by: process:lecture-domaine-finance-corpus, at: 2026-08-19T04:45:00Z }
sources:
  - id: omk-control-room
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/06_Finance_WonderWoman_Thunderbolts/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: OMK Finance — B2 Domain Control Room (§ Gate)
    last_modified: 2026-05-27
  - id: thunderbolts-canon
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/06_Finance_WonderWoman_Thunderbolts/B3_Squad_Thunderbolts/00_B3_SQUAD_CANON.md"
    title: "Thunderbolts canon — Build Gates types"
    last_modified: 2026-05-28
  - id: spock-finance-principles
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/06_Finance_WonderWoman_Thunderbolts/03_WONDERWOMAN_FINANCE_PRINCIPLES.md"
    title: "Wonder Woman Finance Principles (v4) — KR-5d..g + build gates"
    last_modified: 2026-06-25
  - id: harmonization-matrix
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — pair-checks et red flags
    last_modified: 2026-08-19
  - id: red-flag-4-trigger
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/wonder-woman/wonder-woman-red-flag-4-trigger.md"
    title: Red flag #4 — Finance red + Growth/Product green
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Build gate « Paid Release Gate Check » — la condition Finance transversale sur toute release payante

## La citation canonique du gate

Le control room OMK pose le gate verbatim dans `00_B2_DOMAIN_CONTROL_ROOM.md`
§ « Gate » :

> « **No paid release can graduate without price hypothesis, cost
> estimate, margin risk, and billing/collection path.** »

C'est un **arrêt transversal** — toute release payante (Solaris,
Nexus, Orbiter, Coach OS V2, etc.) doit franchir le gate avant
d'être promue en Business Done. Le gate est **souple dans la
forme** (les 4 conditions sont ouvertes, pas des cases à cocher
mécaniques) mais **strict dans la portée** (rien de payant ne
passe sans les 4).

**Qui tient le gate** : Wonder Woman (B2 captain Finance). Le
gate est ouvert par elle au début du sprint B2 Finance, fermé par
la preuve des 4 conditions, et consommé par Flash (Product) pour
autoriser le graduate de la release.

## Les 4 conditions explicites

| # | Condition | Contenu attendu | Source de vérité |
|---|---|---|---|
| 1 | **Price hypothesis** | Une hypothèse de prix chiffrée : setup fee, retainer, ACV cible, paliers. Posée par Wonder Woman + Flash en début de sprint. | Pricing source = Notion Catalogue Produits (mesh anchoring). |
| 2 | **Cost estimate** | Une estimation du coût de build (compute LLM, infra, support) et du coût récurrent (Hostinger, Vercel, Supabase, Stripe fees). | F4 + F22 + F24 (sovereignty). Estimé par B3 Avengers + B3 Kang Dynasty. |
| 3 | **Margin risk** | Une évaluation du risque de marge : scénarios optimiste/réaliste/pessimiste (F2). Risque de marge négative déclenche un re-pricing ou un ralentissement. | F4 « Real net margin » + F7 transparent reporting. |
| 4 | **Billing/collection path** | Le chemin de facturation défini : Stripe (collection), Wise (multi-devise), Airtable `Finance_Pulse` (réconciliation). Cadence <48h « Ready to bill ». | F11 invoice velocity + F12 reconciliation integrity. |

**Lecture** : les 4 conditions sont **posées par les 4 captains**
impliqués :

- Wonder Woman pose #1 (pricing) et #4 (billing/collection).
- Flash (Product) et Superman (Growth) posent #1 (validation prix
  marché).
- Cyborg (IT) pose #2 (cost estimate) — sovereignty F24, compute
  cost F22.
- Wonder Woman arbitre #3 (margin risk) sur la base des autres
  trois.

## Le cycle de vie du gate

Cinq phases :

### Phase 1 — Ouverture (début de sprint)

Wonder Woman ouvre le gate **avant** que Product ne commence le
build. La trace est dans le SPRINT Finance (`B2-FINANCE-YYYY-NN`).
L'ouverture pose :

- Le périmètre de la release payante (Produit + segments clients).
- Les 4 conditions à remplir.
- Le délai attendu pour la fermeture (typiquement : fin de sprint,
  T+5 jours pour une release incrémentale, T+15 pour une release
  majeure).

### Phase 2 — Preuve (pendant le sprint)

B3 Avengers et B3 Kang Dynasty produisent les preuves pendant
l'exécution :

- **Price hypothesis** : A/B test pricing, segmentation, ACV
  cible. Preuve : capture Notion Catalogue + log test.
- **Cost estimate** : facture compute projetée, infra cost.
  Preuve : log Vercel/Hostinger + spreadsheet Airtable.
- **Margin risk** : 3 scénarios (optimiste/réaliste/pessimiste).
  Preuve : métrique chiffrée dans Airtable `Finance_Pulse`.
- **Billing path** : Stripe test mode, Wise multi-devise test,
  Airtable réconciliation setup. Preuve : capture + log.

### Phase 3 — Revue (fin de sprint)

Wonder Woman revoit les 4 preuves contre les 4 conditions. Trois
issues possibles :

- **Accepted** : les 4 conditions sont remplies avec preuve.
  Le gate est fermé. Flash peut promouvoir la release.
- **Conditional accepted** : 1-2 conditions remplies, les autres
  sont en cours avec un horizon défini. Le gate reste ouvert
  pour X jours.
- **Blocked** : 1+ condition manque structurellement (ex : marge
  négative garantie). Le gate est bloqué, la release ne peut
  pas graduate.

### Phase 4 — Fermeture ou escalade

- **Fermeture** : gate `accepted` ou → `conditional` (accepted
  après délai). Le packet mésoperpétuel B2 consigne la décision.
- **Escalade** : si le gate est bloqué et que Wonder Woman ne
  peut pas trancher seule (par exemple : re-pricing impacte un
  contrat Sales signé), escalade au B2 Council avec un packet
  `decision: blocked` ou `decision: escalate_to_B1`.

### Phase 5 — Consommation par Product

Flash consomme le gate fermé pour autoriser le graduate de la
release. **Pas de gate fermé = pas de graduate**. C'est un
**verrou hard**, pas un avis.

## La différence avec les autres outils Finance

| Outil | Granularité | Déclencheur | Conséquence |
|---|---|---|---|
| Veto catalogue Finance | Unaire (une dépense récurrente) | Dépense sans date + métrique | Blocage jusqu'à amendement |
| Blocking authority | Produit (une release) | Marge négative | Blocage release |
| **Paid Release Gate Check** | **Release payante (transverse)** | **4 conditions sur le graduate** | **Verrou transversal** |
| Red flag #4 | Cycle (runway/marge agrégé) | Finance red + Growth/Product green | Arrêt dur Council |

**Lecture** : les 4 outils sont **complémentaires**, pas
redondants. Chaque outil a une granularité différente :

- Le veto catalogue teste la **dépense** (granularité fine).
- Le blocking authority teste le **produit** (granularité moyenne).
- Le Paid Release Gate teste la **release payante** (granularité
  large, transversal).
- Le red flag teste le **cycle** (granularité méso, Council).

Un audit qui réduit Wonder Woman à un seul outil manque la
**complémentarité des granulités**.

## Pourquoi le gate est transversal, pas un pair-check

Le gate Paid Release **aurait pu** être un pair-check (Finance →
Product, le pair-check #6 canonique). Il ne l'est **pas**. Trois
raisons :

### 1. Le gate teste la sortie, pas la transition

Le pair-check #6 teste « le coût de build protège-t-il la marge ? »
— c'est une question sur la **transition** (handoff du coût vers
la marge). Le Paid Release Gate teste les 4 conditions de la
**sortie** (la release peut-elle graduate ?). La transition est
en amont de la sortie.

### 2. Le gate implique 4 captains, pas 2

Le pair-check #6 implique Wonder Woman (Finance) + Flash (Product).
Le Paid Release Gate implique Wonder Woman + Flash + Superman
(Growth pricing) + Cyborg (IT cost). C'est un **construit
transversal**, pas une transition binaire.

### 3. Le gate a un cycle de vie propre

Le pair-check #6 est une décision binaire (OK ou pas OK) à un
moment T. Le Paid Release Gate a un **cycle de vie** (ouverture,
preuve, revue, fermeture, consommation). C'est un objet temporel,
pas une décision instantanée.

## Les 4 cas d'abus du gate

Le gate peut être **abusif** dans 4 cas :

1. **Gate utilisé comme veto politique.** Wonder Woman qui
   bloque le gate systématiquement sur les releases Growth/Product
   sans motif vérifiable utilise le gate comme un veto politique.
   Le packet Council doit signaler le pattern.
2. **Gate sans preuve suffisante.** Wonder Woman ferme le gate
   sur la base d'une « intuition » sans preuve chiffrée sur les
   4 conditions. C'est un gate **non-vérifiable** — il manque la
   propriété du veto légitime.
3. **Gate contourné par urgence business.** Flash qui promeut
   une release payante sans gate fermé sous prétexte d'urgence
   business. C'est une violation du verrou — le packet mésoperpétuel
   doit documenter l'exception et Wonder Woman peut émettre un
   blocking authority rétroactif.
4. **Gate non-ouvert en début de sprint.** Wonder Woman qui
   ouvre le gate en fin de sprint, après que le produit est déjà
   construit, ne peut pas influencer le pricing ou le cost
   estimate. Le gate devient une formalité, pas un garde-fou.

## Les 4 cas où le gate est légitime

Le gate est légitime dans 4 cas :

1. **Release avec coût caché détecté.** Une feature révèle un
   coût récurrent (LLM API tier) non chiffré. Le gate bloque
   jusqu'à ce que le coût soit négocié (F4 + F5).
2. **Release sans pricing hypothesis.** Un produit part en GA
   sans hypothèse de prix chiffrée. Le gate exige le pricing
   avant graduate (F23).
3. **Release avec billing path incomplet.** Un produit part
   sans Stripe/Wise/Airtable réconciliation testée. Le gate
   bloque jusqu'à ce que le billing path soit prouvé (F11 + F12).
4. **Release avec marge négative garantie.** Un produit dont
   la marge nette est structurellement <25% Solaris. Le gate
   exige un re-pricing ou un ralentissement avant graduate
   (F4 + F7).

## Anti-pièges

- **Confondre gate et veto catalogue.** Le veto catalogue porte
  sur une dépense récurrente. Le gate porte sur une release.
  Granularités différentes.
- **Gate = case à cocher.** Le gate n'est pas une checklist
  mécanique. Les 4 conditions doivent être prouvées avec
  métriques, pas avec « « oui c'est fait ».
- **Gate = avis Flash.** Wonder Woman tient le gate. Flash
  consomme le gate. Si Flash peut fermer le gate, la séparation
  des rôles est cassée.
- **Gate = Build Done.** Le gate ferme la **release payante**.
  Pas le build B3, pas la merge PR, pas le deploy. Le gate est
  en **aval** du build, pas au milieu.

## Liens

- [[wonder-woman-recurrent-spend-veto]] — le veto catalogue (granularité fine)
- [[wonder-woman-red-flag-4-trigger]] — le red flag #4 (granularité cycle)
- [[wonder-woman-pair-check-consulted-role]] — le rôle C/A bascule
- [[wonder-woman-finance-doctrine-f1-f25-mapping]] — la cartographie F1-F25
- [[b2-harmonization-matrix-exploitable]] — la matrice d'harmonisation

## Note de confiance

**Confirmé par machine** sur les 4 conditions du gate (lues
verbatim du control room OMK § « Gate »). **Confirmé** sur le
mapping 4 conditions → 4 captains (Wonder Woman + Flash +
Superman + Cyborg — chaque condition a un owner lisible). **Reconstruit**
sur le cycle de vie 5 phases — la doctrine B2 a un cycle de vie
générique pour les gates (cf. `b2-b3-jtbd-handoff-contract.md` § « Le
rôle du B3 squad lead »), instancié pour le gate Finance. **Projeté**
sur les 4 cas d'abus et 4 cas légitimes — extrapolation depuis les
anti-pièges veto catalogue et les doctrines F1-F25.