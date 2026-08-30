---
type: Concept
title: Superman Growth ↔ JohnJones Sales — contrat bilatéral sur le pair-check #1 Growth → Sales
description: Le pair-check #1 (Growth → Sales) est la transition la plus scrutée de la wheel. Superman produit le MQL, JohnJones transforme en SQL. Le contrat bilatéral pose trois Seuils de qualification partagée, quatre signals de friction, et la procédure de gel conjointe quand Sales est red (red flag #2). Le DoD MQL est co-signé par les deux captains — Superman ne qualifie pas seul, JohnJones ne rejette pas seul.
tags: [superman, john-jones, growth, sales, mql, sql, pair-check, contract, red-flag-2]
generated: { by: minimax-m3, at: 2026-08-19T05:10:00Z }
verified:
  - { by: process:lecture-corpus-superman-vague-2, at: 2026-08-19T05:10:00Z }
sources:
  - id: harmonization-pair-check-1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthillation/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — pair-check #1 Growth → Sales
    last_modified: 2026-08-19
  - id: raci-by-rank
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang — Sales A sur #1, Growth C
    last_modified: 2026-08-19
  - id: red-flag-2
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Red flag #2 — Growth green, Sales red : valider l'offre avant de scaler l'attention
    last_modified: 2026-08-17
  - id: b2-b3-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: B2 → B3 contract — double signature B2 sponsor + B3 lead
    last_modified: 2026-08-19
  - id: domain-perimeter
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/domain-perimeter.md"
    title: Périmètre tour 1 — frontière #1 Superman vs Sales
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Superman Growth ↔ JohnJones Sales — contrat bilatéral sur le pair-check #1 Growth → Sales

## Pourquoi ce contrat est la pièce la plus sensible de la wheel

Le pair-check #1 (Growth → Sales) teste la transition *« l'attention
devient-elle opportunité qualifiée ? »*. Trois raisons pour qu'il soit
**la transition la plus scrutée** :

1. **Le passage de coût à revenu.** Avant la transition, tout le
   travail amont (paid media, content, outbound) est **coût sans
   contrepartie**. Après, c'est **potentiel de revenu**. La frontière
   est asymétrique : aucune marge d'erreur tolérée en aval.
2. **Le B2 Sales (JohnJones) porte l'arbitrage.** Le RACI par rang
   pose **Sales = Accountable** sur le pair-check #1. Superman est
   Consulted. Si la transition casse, c'est JohnJones qui escalade
   B2 Council — pas Superman.
3. **Le red flag #2 matrice d'harmonisation** vise *« Growth green,
   Sales red : valider l'offre avant de scaler l'attention »*. C'est
   le seul red flag matrice qui impacte Superman directement. Superman
   doit le détecter et geler sa propre course.

## Les trois Seuils de qualification partagée

Le DoD MQL est co-signé par Superman (qualification amont) et
JohnJones (qualification aval). Aucun des deux ne peut modifier le
DoD seul.

### Seuil 1 — Démographie d'entreprise

**Critère** : taille, secteur, géographie de l'entreprise contactée.

| Paramètre | Plage acceptée | Source de vérité |
|---|---|---|
| Taille | 50-2000 employés (par défaut — révisable par cycle) | ICP signé conjointement |
| Secteur | Liste explicite (ex : SaaS B2B, fintech, healthcare) | ICP signé conjointement |
| Géographie | EU + US (par défaut — révisable par pivot) | ICP signé conjointement |

**Qui décide** : Superman propose, JohnJones accepte ou conteste.
Si JohnJones conteste, **mode negotiation** au Council. Le DoD final
est co-signé.

### Seuil 2 — Intent minimum

**Critère** : signal d'intention (recherche active, contenu
consommé, événement déclencheur).

| Paramètre | Plage acceptée | Source de vérité |
|---|---|---|
| Profondeur d'intent | minimum 1 signal tracked (page pricing visitée, demo request, content > 3 pages) | Tracking PostHog / Mixpanel |
| Fraîcheur | < 30 jours (par défaut — révisable par cycle) | Fenêtre temporelle |

**Qui décide** : JohnJones propose le seuil, Superman vérif
l'instrumentation. Sans tracking valide, **Sales refuse le MQL** —
c'est un signal `NEEDS_TRACKING` qui remonte à Superman.

### Seuil 3 — Engagement produit

**Critère** : interaction avec le produit (trial, POC, intégration
testée).

| Paramètre | Plage acceptée | Source de vérité |
|---|---|---|
| Trial activé | Oui/Non (binaire) | Système produit |
| Profondeur POC | Au moins 1 fonctionnalité cœur testée | Logs produit |
| Fenêtre | < 60 jours | Logs produit |

**Qui décide** : Flash (Product) arbitre si Superman et JohnJones
sont en conflit. Le signal `NEEDS_PRODUCT_TELEMETRY` remonte à Flash.

## Le format du DoD MQL partagé

```yaml
mql_contract_id: MQL-CONTRACT-YYYY-NN
contract_signed:
  b2_growth: superman
  b2_sales: john_jones
  signed_at: YYYY-MM-DD
dod_mql:
  demography:
    taille: [min, max]
    secteur: [list]
    geographie: [list]
  intent:
    profondeur: <signal-name>
    fraicheur_jours: <N>
  engagement:
    trial_requis: true|false
    profondeur_min: <feature-name>
    fenetre_jours: <N>
rejection_protocol:
  signal: NEEDS_QUALIFICATION_REVISIT
  escalation: b2_council | b1 (si red flag #2)
renouvellement:
  cycle: 12WY
  revue: YYYY-MM-DD
```

Le contrat est **versionné** et co-signé. Une révision ouvre un
nouveau `mql_contract_id`. D4 append-only.

## Les quatre signals de friction inter-capitaine

Quand la qualification est disputée, les deux captains utilisent des
signals standardisés :

### Signal A — `NEEDS_QUALIFICATION_REVISIT` (Sales → Growth)

JohnJones constate que **> 30 %** des MQL Superman sont rejetés par
Sales sur un sprint. Il émet le signal pour demander une révision
du DoD MQL. Superman doit répondre en J+2 ouvré.

### Signal B — `NEEDS_SIGNAL_DEEPER` (Growth → Sales)

Superman constate que **< 10 %** des MQL qu'il qualifie deviennent
des SQL après 30 jours. Il émet le signal pour demander à Sales
d'investiguer pourquoi les MQL qualifiés ne se transforment pas.
JohnJones doit répondre en J+2 ouvré.

### Signal C — `NEEDS_TRACKING` (Sales → Growth)

JohnJones constate que les MQL Superman n'ont pas l'instrumentation
requise (PostHog event manquant). Il refuse les MQL non-trackés.
Superman doit corriger l'instrumentation avant de reprendre la
qualification.

### Signal D — `NEEDS_PRODUCT_TELEMETRY` (Growth ou Sales → Flash)

L'un des deux captains constate que le signal d'engagement produit
n'est pas émis par le système. Il escalade Flash (Product) pour
ajout de télémétrie.

## La procédure de gel conjointe — quand Sales est red (red flag #2)

Si JohnJones est en `BLOCKED_COMMITMENT` (cf.
`eight-domain-avengers-wheel.md` §Signal Sales), le red flag #2
matrice se déclenche : *« Growth green, Sales red : valider l'offre
avant de scaler l'attention »*.

**Procédure** :

1. **Détection** : Superman consulte la matrice d'harmonisation
   chaque semaine (cf. cadence canonique). Si Sales est red, le red
   flag #2 est **actif**.
2. **Déclaration** : Superman consigne dans le journal Council
   `red_flag: 2, source: sales_blocked_commitment, action:
   geler_scaler_attention`.
3. **Gel** : Superman **gèle** toute nouvelle campagne de scaling
   (paid media, content amplification). Les MQL existants continuent
   d'être qualifiés au niveau baseline.
4. **Lever le gel** : Superman lève le gel **seulement** quand
   JohnJones sort de `BLOCKED_COMMITMENT` et émet `SALES_READY`. Le
   gel ne se lève pas par exception B1 — seul le retour de Sales à
   Ready tranche.

**Cas concret** : un mandate B1 *« scaler US premium Q4 »* demande
à Superman d'augmenter le paid media de 50 %. JohnJones est en
`BLOCKED_COMMITMENT` parce qu'aucun ICP US n'a été validé. Superman
**refuse** de scaler tant que JohnJones n'a pas validé l'ICP US.
C'est un arbitrage **handoff** : Superman attend l'ICP avant de
démarrer la campagne.

## Le rôle de Superman dans le contrat

Superman est **Consulted**, pas Accountable. Son rôle se limite à :

1. **Produire les MQL** selon le DoD co-signé.
2. **Signaler les frictions** (Signal B, Signal D).
3. **Détecter le red flag #2** et geler le scaling.
4. **Reprendre la qualification** après correction (Signal A,
   Signal C répondus).
5. **Ne pas escalader B1 sauf veto Superman** — un conflit MQL vs
   SQL ne justifie pas une escalade B1, c'est un arbitrage
   Council.

## Le rôle de JohnJones dans le contrat

JohnJones est **Accountable**. Son rôle est plus large :

1. **Valider l'ICP** avant tout DoD MQL co-signé.
2. **Recevoir les MQL** et les transformer en SQL.
3. **Rejeter les MQL hors DoD** via Signal A ou Signal C.
4. **Détecter le besoin de télémétrie produit** via Signal D.
5. **Escalader B2 Council** si Superman persiste à qualifier hors
   DoD après Signal A.

## Le cas-limite — Superman qualifie seul

Si Superman mandate Gamora_Target (B3 Targeting) sans contrat MQL
co-signé avec JohnJones, **le travail est parallèle** mais **non
acquis** : les MQL produits ne sont pas reconnus par Sales comme
opportunités qualifiées. C'est un **scope Superman seul** qui
produit du coût sans contrepartie.

**Le contrat MQL n'est pas obligatoire** — Superman peut qualifier
seul pour ses propres analyses (ex : A/B test de canaux paid). Mais
**les MQL non co-signés** ne traversent pas le pair-check #1. Ils
restent dans le périmètre Growth seul.

## Anti-pièges

- **Contrat MQL sans signature conjointe.** Un DoD MQL signé par
  Superman seul est un DoD unilatéral. JohnJones peut le refuser
  sans négocier. Le DoD unilatéral n'a pas de force d'arbitrage.
- **Red flag #2 ignoré.** Superman qui scale malgré Sales red
  consomme du budget paid media sans output SQL. C'est un veto
  Wonder Woman indirect (dépense récurrente non-justifiée) + un
  veto Aquaman indirect (parole publique non-tenable).
- **Signals non répondus.** Un Signal A ou B non répondu en J+2
  ouvré est un signal de friction **non-escaladé**. Le captain
  récepteur doit escalader B2 Council.
- **Gel levé par exception.** Le gel du red flag #2 ne se lève
  pas par B1, Summers, ou Superman seul. Seul le retour de Sales
  à Ready tranche.
- **Seuil 2 (intent) sans tracking.** Un DoD MQL avec intent mais
  sans instrumentation PostHog/Mixpanel est un DoD **non
  vérifiable**. Le captain sponsor doit refuser le DoD avant
  signature.

## Liens

- [[b2-harmonization-matrix-exploitable]] — le pair-check #1 + red flag #2
- [[b2-pair-check-raci-by-rank]] — Sales A, Growth C
- [[b2-b3-jtbd-handoff-contract]] — la mécanique B2 → B3 appliquée
- [[domain-perimeter]] — la frontière #1 Superman vs Sales
- [[superman-v4-vs-v1-arbitration-rule]] — règle de lecture V4 vs V1
- [[superman-redflag-2-arbiter]] — la procédure de gel détaillée

## Note de confiance

**Confirmé par machine pour la structure ; reconstruit pour les
trois Seuils et les quatre signals.** La position RACI (Sales A,
Growth C) est tirée verbatim du RACI par rang. Le red flag #2 est
tiré verbatim de la matrice d'harmonisation. Le format YAML du
contrat est **projeté** à partir du packet mésoperpétuel canonique
(D4 append-only). Les trois Seuils (démographie, intent,
engagement) sont **reconstruits** par lecture critique de la
pratique MQL/SQL B2B standard et des triplets 41/56/57 (Batman
remonte des faits). Les quatre signals sont **projetés** à partir
de la doctrine des 3 états de gates (`eight-domain-avengers-wheel.md`)
et des triplet 13 (B3 dependsOn B2-sprint). La procédure de gel
conjointe est **reconstruite** à partir du red flag #2 verbatim +
la doctrine `b2-three-cooperation-modes.md` §« Handoff ».