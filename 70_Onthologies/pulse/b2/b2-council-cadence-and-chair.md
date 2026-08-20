---
type: Concept
title: B2 Council — cadence, présidence tournante, et mécanique de séance
description: Le B2 Council tient trois types de séances : hebdomadaire pendant les cycles de build actif (sprint du lundi), ad hoc sur veto ou red flag matrice, et bilan en fin de 12WY. La présidence est tournante par impacted captain — pas de président permanent. Le journal Council est append-only D4 ; le quorum est de 5 capitaines sur 8. La cadence est dérivée du cycle sprint hebdo des VP (triplet 10).
tags: [b2, council, cadence, presidence, quorum, seance, sprint, journal]
generated: { by: minimax-m3, at: 2026-08-19T02:25:00Z }
verified:
  - { by: process:lecture-b2-corpus, at: 2026-08-19T02:25:00Z }
  - { by: human:amdkn, at: 2026-08-20T09:00:00Z }
review:
  version: V0
  by: human:amdkn
  at: 2026-08-20T09:00:00Z
  note: "Revue V0 vague 1 — validee sur les videos et presentations PDF NotebookLM. Areas de Jerry actees en V0 ; role de Summers pour les Projets introduit en V0.1."
sources:
  - id: triplet-vp-sprint
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 10 — chaque VP cycle-hebdomadaire 4 sprints/mois"
    last_modified: 2026-08-17
  - id: triplet-batman-fait
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 56 — Batman remonte à Summers des faits, pas des décisions"
    last_modified: 2026-08-17
  - id: b2-council
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
  - id: fractal-arch
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/fractal-b1b2b3-architecture.md"
    title: Le fractal B1/B2/B3 — Areas perpétuelles vs Summer's Verse datées
    last_modified: 2026-08-17
  - id: batman-b2-control-room
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/04_Ops_Batman_Fantastic4/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: Batman Ops B2 Domain Control Room — cycle sprint hebdo
    last_modified: 2026-05-27
okf_version: "0.2"
---

# B2 Council — cadence, présidence tournante, et mécanique de séance

## Le principe

Le B2 Council est décrit comme *« huit capitaines en cercle »* dans
`B2_DC_DIRECTION_COUNCIL_WORKFLOW.md`. Le corpus ne précise ni quand
le cercle se réunit, ni qui le convoque, ni qui tranche si deux
capitaines sont en désaccord sur la présidence elle-même. Cette page
reconstruit la mécanique opérationnelle à partir du triplet 10 (cycle
sprint hebdo), du triplet 56 (Batman remonte des faits, pas des
décisions) et de la règle d'escalade canonique.

## Les trois types de séances

### 1. Séance hebdomadaire — pendant les cycles de build actif

**Quand** : le **lundi matin**, à l'ouverture du sprint (triplet 10 :
*« chaque VP coupe le rock en 4 sprints hebdomadaires ; le lundi
ouvre le sprint, le vendredi le clôt »*).

**Pourquoi le lundi** : le sprint hebdomadaire B2 commence le lundi.
Le Council statue sur les arbitrages en amont, pour que le sprint
démarre sans blocker.

**Quorum** : 5 capitaines sur 8. Si quorum non atteint, la séance est
reportée au mardi — sauf veto catalogue actif, auquel cas la séance
est convoquée le jour même avec les capitaines présents (minimum 3).

**Participants** : les 8 capitaines (titulaires). Un capitaine peut
déléguer son vote à un adjoint *par séance*, jamais par trimestre —
la délégation permanente n'est pas prévue dans la doctrine.

### 2. Séance ad hoc — sur veto ou red flag matrice

**Quand** : dès qu'un veto catalogue est opposé ou qu'un red flag
matrice d'harmonisation est détecté. La séance est convoquée dans les
**24 heures ouvrées**.

**Qui convoque** : le captain qui oppose le veto, ou le captain qui
détecte le red flag. La convocation se fait par ajout d'une ligne
`convocation: YYYY-MM-DD` en tête du journal Council, avec motif.

**Quorum** : 3 capitaines sur 8 (mode dégradé). Le Council en mode
dégradé peut statuer sur les arbitrages urgents mais ne peut pas
modifier la matrice d'harmonisation ou les vetos catalogue — c'est
une compétence de séance hebdomadaire plein quorum.

### 3. Séance bilan — fin de 12WY

**Quand** : la semaine qui clôt un cycle 12WY. La séance passe en
revue toutes les décisions mésoperpétuelles du cycle (cf.
`b2-meso-decision-packet-spec.md` §`next_review`) et statue sur :
- les décisions à **renouveler** (mode inchangé, cycle suivant) ;
- les décisions à **amender** (nouveau packet, mode révisé) ;
- les décisions à **caduquer** (packet marqué caduque par un packet
  séparé pointant sur l'id d'origine).

**Pourquoi fin de cycle** : le 12WY est l'horizon B1. Sans revue
explicite, les décisions mésoperpétuelles s'accumulent et deviennent
impossibles à ré-instruire.

## La présidence tournante

**Pas de président permanent.** Le Council est un cercle, pas une
hiérarchie. La présidence de chaque séance est tenue par **le captain
au centre de l'arbitrage** :

- Pour un arbitrage Growth × Sales, le président de séance est le
  captain **Sales** (le domaine en aval de la transition).
- Pour un arbitrage Sales × Ops, le président est le captain **Ops**.
- Pour une séance bilan, le président est le captain dont le domaine
  a le plus de décisions mésoperpétuelles ouvertes dans le cycle.

Le président de séance a trois prérogatives :

1. **Poser l'ordre du jour** — chaque capitaine impacté énonce son
   DoD, son blocker, son veto éventuel.
2. **Tenir le minutage** — la séance ne dépasse pas 60 minutes ; un
   arbitrage non résolu escalade B1.
3. **Signer le packet** de sortie — la signature du président vaut
   cosignataire des 8 capitaines (le Council tranche en cercle, mais le
   journal porte une signature).

## Le journal Council — append-only D4

Le fichier `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` est append-only.
Aucune ligne existante n'est éditée. Chaque séance produit :

- une **ligne d'ouverture** : `seance: YYYY-MM-DD-HH, type: weekly|adhoc|bilan, president: <captain>, quorum: N/8, agenda: …` ;
- une ou plusieurs **lignes de décision** : un packet mésoperpétuel
  par arbitrage (cf. `b2-meso-decision-packet-spec.md`) ;
- une **ligne de clôture** : `cloture: HH:MM, decisions: N, escalations: M, dormant: K, wake: L`.

La règle D4 (cf. `omk-business-os.md` §« Doctrine — D4, D6, Spec-Loop
») s'applique intégralement. Une ligne erronée est corrigée par un
packet séparé qui pointe sur l'id d'origine.

## Le lien avec le cycle sprint hebdo des VP

Le triplet 10 ancre le VP dans un cycle **mensuel** : *« chaque VP
coupe le rock en 4 sprints hebdomadaires »*. La cadence du Council
est calée sur cette coupe :

| Sprint VP | Action Council |
|---|---|
| **Lundi matin** | Séance hebdomadaire — arbitrage des conflits du sprint |
| **Mardi–Jeudi** | Séances ad hoc si veto ou red flag |
| **Vendredi matin** | Revue des arbitrages en cours — préparation clôture |
| **Vendredi soir** | Clôture sprint — packet mésoperpétuel signé si arbitrage clos |

Le Council n'est pas une instance de **production** — c'est une
instance d'**arbitrage**. Il n'écrit pas de sprint, il tranche les
sprints qui se contredisent.

## Pourquoi la présidence tournante

Trois raisons :

1. **Pas de capital politique.** Un président permanent accumule un
   pouvoir qui déforme les arbitrages — les capitaines hésitent à
   contredire le président sur des cas limites. La rotation par
   arbitrage recentre le pouvoir sur le cas, pas sur la personne.
2. **Pas de domaine orphelin.** Un président permanent est tenté de
   privilégier son domaine. La rotation garantit que chaque captain
   préside au moins une fois par cycle.
3. **Légitimité du captain en aval.** Le captain en aval de la
   transition (Sales dans Growth × Sales) porte la responsabilité
   opérationnelle de la transition. C'est lui qui en subit les effets,
   c'est lui qui préside l'arbitrage.

## Anti-pièges

- **Président permanent de facto.** Si le même captain préside trois
  séances d'affilée, le Council a dérivé vers une présidence
  permanente. Le Council doit refuser la quatrième.
- **Quorum en cascade.** Si trois séances hebdomadaires d'affilée
  n'atteignent pas le quorum, le Council escalade B1 — la mésoperpétuité
  est en panne.
- **Convocation par un non-capitaine.** Un B3 ou un B1 ne convoque
  pas le Council. La convocation est un acte de captain, sinon le
  Council devient une instance B1-bis.
- **Séance bilan sans revue des décisions ouvertes.** Une séance bilan
  qui ne passe pas en revue les `next_review` du cycle n'a pas eu
  lieu. C'est une formalité, pas une séance.
- **Confondre séance et consultation.** Le Council tranche en séance,
  pas par consultation écrite asynchrone. Une décision par message
  privé n'a pas de force d'arbitrage.

## Liens

- [[b2-council-arbitrage-rule]] — qui tient le Council et pourquoi
- [[b2-meso-decision-packet-spec]] — le format des décisions en séance
- [[b2-areas-dormants-doctrine]] — quand le Council statue sur un réveil
- [[b2-b3-jtbd-handoff-contract]] — la sortie du Council vers B3
- [[b1-stop-conditions-escalier]] — quand une séance escalade B1

## Note de confiance

**Reconstruit.** Les trois types de séances (hebdomadaire / ad hoc /
bilan) sont **projetés** à partir du triplet 10 (cycle sprint hebdo
des VP) et de la cadence canonique B2 hebdomadaire (fractal
§« Quand le Council escalade à B1 »). La présidence tournante et la
règle de quorum 5/8 sont **extrapolées** à partir du triplet 56
(Batman remonte des faits, pas des décisions) et de la doctrine
d'absence de hiérarchie horizontale entre capitaines. Le lien entre
séance hebdomadaire et lundi du sprint est cohérent avec la cadence
mensuelle 4 sprints/mois du triplet 10. Aucun élément de cette page
n'est cité verbatim du canon — la doctrine est reconstruite par
synthèse. À vérifier en séance réelle : (1) le quorum 5/8 tient-il
sur un cycle complet ?, (2) la présidence tournante est-elle
acceptable par les capitaines ?, (3) la cadence bilan fin-de-12WY
est-elle tenable sans saturer la séance hebdomadaire ?
