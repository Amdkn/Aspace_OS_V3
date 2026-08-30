---
type: Concept
title: Aquaman — catalogue concret des paquets JTBD émis vers Eternals et reçus des domaines amont
description: Quatre formes canoniques de paquets JTBD qu'Aquaman émet vers Eternals (privacy review, claim safety review, contract template build, defensibility doc build) avec leur JTBD packet YAML concret, et quatre paquets qu'Aquaman reçoit en amont de Flash, Superman, JohnJones, Cyborg. Chaque forme a sa preuve, son lead/lag indicator, et son couplage avec un veto catalogue. Tour 2 comble la question 3 du brief.
tags: [b2, aquaman, jtbd, emit, receive, eternals, packet, catalog, contract, privacy, claim]
generated: { by: minimax-m3, at: 2026-08-19T04:05:00Z }
verified:
  - { by: process:lecture-canon-aquaman-tour-2, at: 2026-08-19T04:05:00Z }
sources:
  - id: legal-swarm-supervision
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/02_B3_SWARM_SUPERVISION_PROTOCOL.md"
    title: B3 Swarm Supervision Protocol — JTBD Packet gabarit
    last_modified: 2026-05-27
  - id: legal-pipeline
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/08_Legal_Aquaman_Eternals/01_ROCK_TO_DOD_TO_JTBD_PIPELINE.md"
    title: Rock → DoD → JTBD Pipeline — B2 Rock Packet et DoD Quality Bar
    last_modified: 2026-05-27
  - id: b2-b3-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: B2 → B3 contract — quand une décision mésoperpétuelle devient un JTBD packet
    last_modified: 2026-08-19
  - id: b3-jtbd-reception
    resource: "C:/Users_amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-jtbd-packet-reception-checklist.md"
    title: B3 JTBD packet reception checklist
    last_modified: 2026-08-19
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — gates et B3 squads
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Aquaman — catalogue JTBD émis et reçus

## Pourquoi un catalogue, pas un gabarit

Le concept [[aquaman-squad-eternals-et-dormance]] donne le **gabarit
générique** d'un JTBD packet Legal (cf.
`02_B3_SWARM_SUPERVISION_PROTOCOL.md` §JTBD Packet). Ce concept-ci
donne les **formes canoniques** que ces paquets prennent en pratique,
avec les preuves, lead/lag indicators, et couplages veto associés.

Le catalogue est nécessaire parce que Aquaman opère dans un état
dormant (cf. [[aquaman-domaine-legal-perimetre]]) et n'a pas encore
produit de paquets mésoperpétuels. Les 4 formes ci-dessous sont
**projetées** depuis les 7 surfaces du périmètre Legal
([[aquaman-domaine-legal-perimetre]] §Ce que couvre le domaine) et
**non observées en cycle**.

## Les 4 formes émises par Aquaman vers Eternals

Chaque forme répond à *une* surface du périmètre. La somme des 4
formes couvre les 7 surfaces moins la *coordination* transversale
(IP + contract risk + claims + privacy + terms + compliance +
permissions & defensibility — les 4 formes ci-dessous en portent
chacune au moins une).

### Forme 1 — `B3-LEGAL-PRIVACY-REVIEW-YYYY-NN`

**Surface portée** : *privacy* + *compliance* (RGPD, sector rules).

**Déclencheur** : un Flash (Product) merge une feature qui touche de
la donnée personnelle, ou un Superman (Growth) prépare une page qui
collecte du consentement.

**JTBD packet** :

```yaml
jtbd_id: B3-LEGAL-PRIVACY-REVIEW-2026-03
source_rock_id: B2-LEGAL-2026-08
assigned_swarm: Eternals
job_statement: "When a Product feature collects or exposes personal data,
  produce a privacy review checklist covering RGPD art. 13, 14, and 30,
  so Aquaman can emit LEGAL_READY or BLOCKED_RISK."
input_artifacts:
  - path-to-feature-spec
  - path-to-data-flow-diagram
expected_output_artifacts:
  - privacy-review-checklist.md (signed by Ajak)
proof_required:
  - checklist signed
  - link to RGPD articles covered
lead_indicator: privacy review produced in <72h after feature merge
lag_indicator: 0 privacy incidents in 30d post-launch
coupling:
  veto_cible: aquaman-engagement-sans-perimetre (si périmètre feature flou)
  pair_check: #8 Legal → Product (Flash A, Aquaman C)
```

**Forme de preuve canonique** (cf. `b3-proof-path-4-formes`) :
**artefact** — la checklist signée est l'artefact, vérifiable par un
tiers qui n'est pas Aquaman (le triplet 22 liste Ajak compliance —
Ajak signe, Aquaman émet `LEGAL_READY` ou `BLOCKED_RISK` sur la base
de la signature).

### Forme 2 — `B3-LEGAL-CLAIM-SAFETY-YYYY-NN`

**Surface portée** : *claims* + *defensibility*.

**Déclencheur** : un Superman (Growth) veut publier une claim
publique (landing page, ad copy, press release) qui engage
l'organisation.

**JTBD packet** :

```yaml
jtbd_id: B3-LEGAL-CLAIM-SAFETY-2026-04
source_rock_id: B2-LEGAL-2026-09
assigned_swarm: Eternals
job_statement: "When a public claim names a measurable outcome, produce
  a defensibility analysis covering substantiation, comparative
  language, and disclaimer scope, so Aquaman can emit LEGAL_READY or
  BLOCKED_RISK on the public-facing work."
input_artifacts:
  - claim text
  - substantiation evidence (logs, metrics, customer quotes)
expected_output_artifacts:
  - defensibility-memo.md (signed by Thena)
proof_required:
  - memo signed
  - substantiation evidence linked
lead_indicator: claim review produced in <48h before publication date
lag_indicator: 0 FTC/regulator complaints in 90d post-publication
coupling:
  veto_cible: aquaman-engagement-sans-perimetre (si périmètre claim flou)
  pair_check: #7 Legal → Growth (Superman A, Aquaman C)
```

**Forme de preuve** : **artefact + métrique** — le mémo signé est
l'artefact ; la métrique est *0 plainte sur 90 jours* (lag indicator).

### Forme 3 — `B3-LEGAL-CONTRACT-TEMPLATE-YYYY-NN`

**Surface portée** : *contract risk* + *terms* + *IP*.

**Déclencheur** : un JohnJones (Sales) signe un nouveau type de
contrat client (premier client d'un segment, premier deal d'un ACV
donné, premier partenariat multi-parties).

**JTBD packet** :

```yaml
jtbd_id: B3-LEGAL-CONTRACT-TEMPLATE-2026-05
source_rock_id: B2-LEGAL-2026-10
assigned_swarm: Eternals
job_statement: "When Sales opens a new contract category, produce a
  contract template covering scope, IP retention, liability cap,
  termination, and data ownership, so Aquaman can stamp LEGAL_READY
  and Aquaman/People co-sign the matrix."
input_artifacts:
  - sales-brief with deal structure
  - prior contracts in 03_Master_Agreements/ (if any)
expected_output_artifacts:
  - contract-template-v1.md
  - ip-clauses.md (signed by Phastos)
  - ownership-matrix.md (co-signed by Green Lantern)
proof_required:
  - template in versioned location
  - IP clauses signed
  - ownership matrix signed
lead_indicator: template ready in <5 working days after Sales brief
lag_indicator: 0 contract disputes in 6 months post-signing
coupling:
  veto_cible: aquaman-engagement-sans-perimetre (le veto catalogue lui-même)
  pair_check: hors matrice (couplage indirect Aquaman ↔ JohnJones)
```

**Forme de preuve** : **artefact tripartite** — le template, les
clauses IP signées par Phastos, et la matrice de signature co-signée
par Aquaman + Green Lantern. Trois artefacts, trois signataires — la
triple signature est ce qui rend le livrable *vérifiable*.

### Forme 4 — `B3-LEGAL-DEFENSIBILITY-DOC-YYYY-NN`

**Surface portée** : *permissions & defensibility* (audit,
contentieux, incident response).

**Déclencheur** : un Batman (Ops) signale un incident, ou un Cyborg
(IT) signale une breach de données, ou un Aquaman lui-même initie
une revue de defensibilité proactive (régulation sectorielle qui
change).

**JTBD packet** :

```yaml
jtbd_id: B3-LEGAL-DEFENSIBILITY-DOC-2026-06
source_rock_id: B2-LEGAL-2026-11
assigned_swarm: Eternals
job_statement: "When an incident triggers audit, litigation, or
  regulator inquiry risk, produce a defensibility binder covering
  timeline, decisions, evidence trail, and named accountable owners,
  so Aquaman can co-sign with Batman/Ops and route to B1 if escalation
  is needed."
input_artifacts:
  - incident timeline
  - decisions log
  - evidence trail (commits, screenshots, signed contracts)
expected_output_artifacts:
  - defensibility-binder.md
  - accountable-owners-roster.md
proof_required:
  - binder signed by Thena
  - owners roster signed by Aquaman + Batman
lead_indicator: binder ready in <24h after incident declared
lag_indicator: 0 successful plaintiff claims in 12 months post-incident
coupling:
  veto_cible: n/a (pas un veto déclenché, c'est une production en aval)
  pair_check: hors matrice (couplage indirect Aquaman ↔ Batman)
```

**Forme de preuve** : **artefact signé double** — le binder signé
par Thena (Eternals defense, cf. triplet 22), le owners roster
co-signé par Aquaman + Batman. La double signature externe au
domaine Legal est ce qui rend le binder *admissible* en cas de
litige.

## Les 4 formes reçues par Aquaman depuis les domaines amont

Aquaman ne produit pas dans le vide. Il reçoit des déclencheurs de
4 domaines distincts. Chaque forme reçue a sa propre *gating
condition* — Aquaman ne peut pas démarrer le JTBD émis sans
l'input reçu.

### Reçu 1 — de Flash (Product) : feature spec + data flow

**Forme** : packet `B2-PRODUCT-FEATURE-YYYY-NN` qui contient la
spécification feature, le data flow diagram, et la liste des
third-party assets touchés.

**Gating condition** : Aquaman ne peut pas émettre le
`B3-LEGAL-PRIVACY-REVIEW` sans ce reçu. Si Flash tarde, Aquaman
retourne `BLOCKED_RISK` *en amont* — un Aquaman qui produit un
privacy review sans data flow diagram fait de la fiction.

**Couplage** : pair-check #8 (Legal → Product) — Aquaman est C, Flash
est A. Le blocage se signale en C, mais l'arbitrage final est chez
Flash.

### Reçu 2 — de Superman (Growth) : claim draft + substantiation

**Forme** : packet `B2-GROWTH-CLAIM-YYYY-NN` qui contient le draft
de claim, l'évidence de substantiation (métriques, logs, témoignages),
et la date de publication prévue.

**Gating condition** : Aquaman ne peut pas émettre le
`B3-LEGAL-CLAIM-SAFETY` que si Superman a écrit la claim *avant*
de demander la review. Un Superman qui demande *« peux-tu valider ce
que je n'ai pas encore écrit ? »* oblige Aquaman à refuser ou à
clarifier (anti-bottleneck rule : *« Rewrite the job, not the swarm
»*).

**Couplage** : pair-check #7 (Legal → Growth) — Aquaman est C,
Superman est A.

### Reçu 3 — de JohnJones (Sales) : deal structure + reformulation client validée

**Forme** : packet `B2-SALES-DEAL-YYYY-NN` qui contient la structure
du deal (ACV, durée, périmètre fonctionnel), le problem statement
reformulé par le client (cf. veto catalogue JohnJones), et le
contrat-type pressenti.

**Gating condition** : Aquaman ne peut pas émettre le
`B3-LEGAL-CONTRACT-TEMPLATE` sans la reformulation client validée
par JohnJones (sinon Aquaman produit un contrat sur un problème non
qualifié — le veto Aquaman *engagement-sans-périmètre* bloque en
amont).

**Couplage** : couplage indirect Aquaman ↔ JohnJones (cf.
[[aquaman-couplages-invisibles]] §Couplage 4). **Ce couplage n'est
pas dans la matrice d'harmonisation** — un pipeline Sales → Legal
explicite reste à poser (cf. rapport tour 1 §4.4 et §5.1).

### Reçu 4 — de Cyborg (IT) : privacy implémentation spec

**Forme** : packet `B2-IT-PRIVACY-SPEC-YYYY-NN` qui contient les
choix d'implémentation privacy (chiffrement at rest / in transit, IAM
model, retention period, modèle de menace).

**Gating condition** : Aquaman ne peut pas signer le privacy review
de Forme 1 (émise) sans la spec IT. Si Cyborg tarde, Aquaman émet
`NEEDS_REVIEW` (pas `LEGAL_READY`) — un privacy review sans spec IT
est une fiction.

**Couplage** : convergence de vetos potentielle (cf.
[[aquaman-couplages-invisibles]] §Couplage 1). Aquaman peut exiger *«
pas de cloud-only »* pour des raisons privacy, Cyborg peut bloquer
le même mandat pour des raisons souveraineté IT — c'est un cas de
mode `negotiation` au Council.

## Synthèse — la matrice emit × receive

| Aquaman émet | Aquaman reçoit de | Sans le reçu, Aquaman émet |
|---|---|---|
| `B3-LEGAL-PRIVACY-REVIEW` | Flash (feature spec + data flow) | `BLOCKED_RISK` par défaut |
| `B3-LEGAL-CLAIM-SAFETY` | Superman (claim draft + substantiation) | `BLOCKED_RISK` par défaut |
| `B3-LEGAL-CONTRACT-TEMPLATE` | JohnJones (deal + reformulation validée) | Veto veto engagement-sans-périmètre |
| `B3-LEGAL-DEFENSIBILITY-DOC` | Batman (incident) ou Cyborg (breach) ou Aquaman (proactive) | n/a (peut produire sur sa propre initiative) |

Cette table est la **lecture opérationnelle** de la question 3 du
brief — *quels paquets JTBD ce domaine émet vers B3, et lesquels il
reçoit ?*. La réponse est : **4 émis, 4 reçus, avec gating conditions
explicites**.

## Anti-pièges spécifiques au catalogue

- **Produire un paquet émis sans le reçu correspondant.** Un privacy
  review sans data flow diagram est de la fiction. Aquaman doit
  refuser ou escalader, pas produire.
- **Confondre gating condition et veto catalogue.** Le gating est un
  *pré-requis d'input* ; le veto est un *blocage de démarrage*. Les
  deux se ressemblent (les deux bloquent la production) mais le
  gating est sur l'input, le veto est sur le périmètre. Un Aquaman
  qui oppose le veto au lieu de signaler un gating fait de
  l'overreach.
- **Produire un défensibility binder sans owner roster signé.** Le
  binder sans owners est un document sans responsable. La double
  signature Aquaman + Batman est ce qui rend le binder opérationnel,
  pas l'existence du fichier.
- **Considérer les 4 formes comme exhaustives.** Les 4 formes
  couvrent les 7 surfaces du périmètre *par combinaison*, pas une
  par une. Privacy + compliance dans Forme 1 ; claims + defensibility
  dans Forme 2 ; contract risk + terms + IP dans Forme 3 ;
  permissions + defensibility dans Forme 4. Si une 8ᵉ surface
  apparaît (par exemple *régulation sectorielle émergente*), il faut
  une Forme 5.

## Liens

- [[aquaman-squad-eternals-et-dormance]] — le gabarit JTBD packet
  générique et la tension effectif Eternals
- [[aquaman-domaine-legal-perimetre]] — les 7 surfaces que les 4
  formes couvrent par combinaison
- [[aquaman-veto-engagement-sans-perimetre]] — le veto qui bloque
  Forme 3 sans reformulation client
- [[aquaman-gates-et-pair-checks]] — les 3 gates qui résultent des
  4 formes (LEGAL_READY / NEEDS_REVIEW / BLOCKED_RISK)
- [[aquaman-couplages-invisibles]] — les 4 couplages indirects qui
  correspondent aux 4 reçus
- [[b2-b3-jtbd-handoff-contract]] — le contrat bilatéral qui
  structure chaque paquet émis

## Note de confiance

**Reconstruit, projeté depuis le canon, non observé en cycle.** Les
4 formes émises sont **projetées** à partir des 7 surfaces du
périmètre Legal et du gabarit JTBD packet. Les 4 formes reçues sont
**projetées** à partir des pair-checks #7 #8 et des 5 couplages
indirects. La table emit × receive est **reconstruite** à partir du
concept [[aquaman-couplages-invisibles]] et du veto catalogue. Aucun
de ces 8 paquets n'a été émis ou reçu en cycle — la Vague 2 a
travaillé sur les protocoles, pas sur l'exécution. **À vérifier** :
quand le premier Master Agreement est signé, le paquet Forme 3 doit
être émis *avant* la signature client, pas *après*.