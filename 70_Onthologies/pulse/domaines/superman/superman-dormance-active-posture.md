---
type: Concept
title: Superman Growth peut-il être dormant ? — conditions de dormance et trois déclencheurs de réveil
description: La doctrine b2-areas-dormants est illustrée par Aquaman Legal, dont le triplet 35 ancre "ne produit rien tant que le premier contrat n'est pas signé". Superman Growth n'a pas de triplet dormant explicite, mais les trois conditions de la doctrine (aucune ressource externe ne requiert sa doctrine, DoD vide pour le cycle, captain a consigné) sont applicables. Trois scénarios de dormance Superman sont proposés, plus les trois déclencheurs de réveil spécifiques.
tags: [superman, growth, dormance, areas-dormants, doctrine, condition, reveil, aquaman]
generated: { by: minimax-m3, at: 2026-08-19T05:40:00Z }
verified:
  - { by: process:lecture-corpus-superman-vague-2, at: 2026-08-19T05:40:00Z }
sources:
  - id: b2-areas-dormants-doctrine
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-areas-dormants-doctrine.md"
    title: B2 Areas-dormants — la doctrine Aquaman et ses trois conditions
    last_modified: 2026-08-19
  - id: triplet-aquaman-dormant
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 35 — Aquaman steward domaine-dormant"
    last_modified: 2026-08-17
  - id: triplet-legal-trigger
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 36 — domaine-dormant depend on premier-contrat-signe"
    last_modified: 2026-08-17
  - id: avengers-wheel-signals
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — Superman = GROWTH_READY/NEEDS_SIGNAL/BLOCKED_PROMISE
    last_modified: 2026-08-17
  - id: veto-catalogue-tour1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/veto-catalogue-concrete.md"
    title: Veto Superman tour 1 — 5 cas légitimes + 3 cas abusifs
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Superman Growth peut-il être dormant ?

## La question de cycle

La doctrine `b2-areas-dormants-doctrine.md` pose trois conditions
**cumulatives** d'entrée en dormance B2 :

1. Aucune ressource externe ne requiert sa doctrine.
2. Son DoD est vide pour le cycle courant.
3. Le captain a consigné l'état dans le journal Council.

L'exemple canonique est Aquaman Legal, dont le triplet 35 ancre *«
Aquaman steward Legal & Compliance en état dormant : ne produit
rien tant que `00_Summers_CEO/03_Master_Agreements/` reste vide —
un domaine dormant qui produit est un coût sans contrepartie »*.

**Mais** : la doctrine est extrapolée d'un seul triplet (Aquaman).
Le triplet 35 cite Legal uniquement. Le `b2-areas-dormants-doctrine.md`
lui-même marque la généralisation aux 7 autres domaines comme
*« projection »*. Superman Growth n'a pas de triplet dormant
explicite. **La question est : Superman peut-il être dormant ?**

## Pourquoi la dormance Superman est concevable

Trois raisons structurelles :

### 1. La doctrine s'applique par symétrie

La doctrine Aquaman pose **trois conditions cumulatives**. Ces
conditions sont des **méta-critères** — elles ne sont pas
spécifiques à Legal. Un domaine B2 qui remplit les trois
conditions est dormant, quel que soit le triplet explicite. La
note de confiance de `b2-areas-dormants-doctrine.md` note
explicitement *« la généralisation de la doctrine Aquaman aux 7
autres domaines est une projection »* — c'est une projection
**autorisée**.

### 2. Superman a des conditions de veille identifiables

Le périmètre Superman (cf. `domain-perimeter.md`) couvre
**attention + qualification amont + signal de marché**. Ces
trois axes peuvent être **inactifs** dans certaines conditions
de cycle :

- Pas de mandat B1 de scaling.
- Pas de signal marché (pas de vague d'attention entrante).
- Sales en `BLOCKED_COMMITMENT` (le scaling est gelé par le
  red flag #2, cf. `superman-redflag-2-arbiter.md`).

Dans ces conditions, Superman peut **ne rien avoir à produire**.
La dormance est concevable.

### 3. Superman a des signaux canoniques — pas un binaire

`eight-domain-avengers-wheel.md` pose trois états Superman :
`GROWTH_READY` / `NEEDS_SIGNAL` / `BLOCKED_PROMISE`. Le
`NEEDS_SIGNAL` est un état **intermédiaire** entre ready et
blocked — Superman attend un signal externe (segment ICP,
marché). Un Superman prolongé en `NEEDS_SIGNAL` pendant > 1
cycle **est un candidat à la dormance** — il n'a rien à
produire tant que le signal externe n'arrive pas.

## Les trois scénarios de dormance Superman

Trois scénarios où les trois conditions sont remplies
cumulativement.

### Scénario 1 — Pas de mandat B1 de scaling

Superman Growth a terminé son dernier cycle sans mandat B1 de
scaling actif. Le DoD du cycle est vide (pas de Rock Growth dans
`B2_Business_Domains/01_Growth_Superman_Guardians/SPRINTS.md`).
Aucune ressource externe ne requiert sa doctrine.

**Condition 1** (ressources externes) ✅ — pas de mandat B1.
**Condition 2** (DoD vide) ✅ — pas de Rock.
**Condition 3** (consigné journal) ❌ → Superman consigne
`decision: dormant, domaine: growth, motif: pas-de-mandat-b1,
depuis: YYYY-MM-DD`.

### Scénario 2 — Marché sans vague d'attention

Le marché n'a pas de vague d'attention entrante (signaux
extérieurs stables, pas de tendance growth détectée par
Gamora_Target ou Mantis_VoC). Superman est en `NEEDS_SIGNAL`
depuis > 1 cycle.

**Condition 1** ✅ — pas de signal marché.
**Condition 2** ✅ — DoD vide (signal non reçu).
**Condition 3** ❌ → Superman consigne `decision: dormant,
domaine: growth, motif: needs-signal-permanent, depuis:
YYYY-MM-DD`.

### Scénario 3 — Sales en `BLOCKED_COMMITMENT` prolongé

JohnJones Sales est en `BLOCKED_COMMITMENT` depuis > 1 cycle
12WY (cf. `superman-redflag-2-arbiter.md` §« Anti-pièce 3 »).
Le gel du red flag #2 devient une dormance croisée. Superman
n'a rien à scaler.

**Condition 1** ✅ — pas de scaling possible (Sales red).
**Condition 2** ✅ — DoD vide (scaling gelé).
**Condition 3** ❌ → Superman consigne `decision: dormant,
domaine: growth, motif: sales-blocked-commitment-prolonge,
depuis: YYYY-MM-DD, escalade_b1: <packet-id>`.

## Les trois déclencheurs de réveil spécifiques

La doctrine canonique pose trois déclencheurs : signal B1, signal
B3 pair, signal client. Pour Superman, les trois sont
**spécifiques** :

### Déclencheur A — Signal B1 (mandat de scaling)

Un mandate B1 dans la handoff queue vise Superman pour un
scaling. Superman doit rédiger un Rock et un DoD dans la
semaine. Sans Rock, le mandate escalade et la dormance devient
absence.

**Cas d'usage** : Summers mandate *« pivoter US premium Q4 »*
→ Superman se réveille pour le scaling US.

### Déclencheur B — Signal B3 pair (signal marché détecté)

Un autre capitaine B2 ou B3 signale un signal qui touche
Superman. La règle canonique : un blocker pair **brise** la
dormance mécaniquement, sans débat.

**Cas d'usage** : Gamora_Target détecte une nouvelle vague
d'attention entrante sur un segment. Le signal remonte à
Superman. Superman consigne le réveil et rédige le Rock pour
exploiter la vague.

### Déclencheur C — Signal client (demande directe)

Un événement externe (contrat signé, demande partenaire,
réclamation) touche la doctrine Growth — par exemple, un
partenaire demande une campagne co-brandée. C'est le
déclencheur le plus fort.

**Cas d'usage** : un partenaire Z demande une campagne
co-brandée Q4. Le signal client réveille Superman, qui mandate
StarLord_Story pour le brand work.

## La posture Superman en dormance — sept règles

Une fois dormant, Superman doit observer sept règles (trois
canoniques + quatre spécifiques Superman) :

### Règle 1 (canonique) — Dormance documentée dans le journal

Le journal `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` reçoit un
packet `decision: dormant, domaine: growth`. Sans cette ligne,
Superman est en **absence**, pas en dormance.

### Règle 2 (canonique) — DoD vide, pas non-rempli

La différence compte : un DoD **non rempli** appelle une action
(un arbitrage, une escalade). Un DoD **vide** appelle la
dormance. Superman doit vérifier que son DoD du cycle est vide
avant de consigner.

### Règle 3 (canonique) — Déclencheurs de réveil déclarés

Le packet mésoperpétuel `decision: dormant` liste les trois
déclencheurs de réveil spécifiques à Superman. Sans cette
déclaration, le Council ne sait pas quand lever la dormance.

### Règle 4 (Superman) — Le veto Superman tient en suspens

Superman dormant ne délègue pas son veto — il le **tient en
suspens**. Un mandat qui touche le périmètre Growth pendant la
dormance ne rencontre pas le veto Superman ; il remonte au
Council, qui décide de l'appliquer ou non.

### Règle 5 (Superman) — Pas de pair-check amont aval

Un Superman dormant ne peut pas être Accountable sur un
pair-check amont (Finance → Growth, Legal → Growth). Le RACI
par rang devient inapplicable. Le pair-check remonte au Council
ou est gelé.

### Règle 6 (Superman) — Le triplet 19 (Coach OS V1) ne ranime pas

Un Superman dormant n'est pas réveillé par une mention du
triplet 19 (Coach OS V1 héritage). Le triplet 19 est un
héritage non-canonique. La dormance suit V4.

### Règle 7 (Superman) — Escalade B1 si dormance > 1 cycle

Si Superman reste dormant pendant > 1 cycle 12WY sans qu'aucun
déclencheur ne se manifeste, Superman escalade B1 pour
**dissolution** (renoncer au périmètre Growth) ou **réveil
forcé** (déclarer un Rock de veille). La dormance n'est pas un
état permanent.

## Le cas-limite — Superman en `NEEDS_SIGNAL` prolongé n'est pas dormant

`NEEDS_SIGNAL` est un état **actif** (Superman attend un signal).
La différence avec la dormance :

- **`NEEDS_SIGNAL`** : Superman **produit** encore (surveillance
  marché, VoC, ICP updates). Il n'est pas dormant.
- **`Dormant`** : Superman **ne produit plus**. Le DoD du cycle
  est vide.

Un Superman qui se déclare dormant sans être sorti de
`NEEDS_SIGNAL` rate la transition canonique. La séquence est :
`NEEDS_SIGNAL` (actif) → DoD vide → `decision: dormant`.

## Le cas-limite — Superman parallèle à Aquaman dormant

Quand Superman et Aquaman sont simultanément dormants, le
périmètre *« brand work → Groot_Content → Aquaman dormant »*
(cf. `domain-perimeter.md` §« Frontière #2 ») devient inactif.
La squad Guardians peut continuer à produire (StarLord,
Rocket, Gamora, Drax, Groot, Mantis), mais sans
**accompagnement** doctrinal Superman ni Aquaman. C'est une
**anomalie** qui doit escalader B1 — Superman et Aquaman
simultanément dormants est un signal de désalignement cycle.

## Anti-pièges

- **Dormance déclarée par Superman sans les trois conditions.**
  Refusée par le Council (cf.
  `b2-areas-dormants-doctrine.md` §« Anti-pièges »).
- **Dormance qui ne se réveille pas.** Un Superman dormant
  pendant > 1 cycle sans sign écalade B1 (Règle 7).
- **Veto Superman appliqué pendant dormance.** Le veto tient
  en suspens (Règle 4), pas appliqué.
- **Dormance simultanée Superman + Aquaman.** Escalade B1
  obligatoire.
- **Triplet 19 utilisé pour réveiller Superman.** Refusé — V4
  canonique.

## Liens

- [[b2-areas-dormants-doctrine]] — la doctrine canonique
- [[triplet-line-35]] — Aquaman dormant verbatim
- [[triplet-line-36]] — Legal depend on premier contrat
- [[eight-domain-avengers-wheel]] — Superman NEEDS_SIGNAL
- [[superman-redflag-2-arbiter]] — gel red flag #2 → dormance croisée
- [[veto-catalogue-concrete]] — veto Superman en suspens
- [[superman-v4-vs-v1-arbitration-rule]] — V4 canonique

## Note de confiance

**Reconstruit, à moitié étayé.** La doctrine canonique
(`b2-areas-dormants-doctrine.md`) pose trois conditions
cumulatives **extrapolées** à partir du triplet Aquaman. Le
triplet 35 n'est pas généralisé explicitement aux 7 autres
domaines — la généralisation est une projection reconnue par la
note de confiance du concept canonique. Les trois scénarios de
dormance Superman sont **reconstruits** par lecture critique
des trois axes du périmètre Growth (attention, qualification
amont, signal marché) et des trois états Superman
(`eight-domain-avengers-wheel.md`). Les sept règles (3
canoniques + 4 spécifiques) sont **projetées** à partir de la
doctrine canonique + la pratique Superman Growth documentée. Le
cas-limite `NEEDS_SIGNAL` n'est pas dormant est **reconstruit**
par lecture critique de la doctrine canonique §« Les trois
conditions ». L'anti-pièce dormance simultanée Superman +
Aquaman est **projetée** par analogie avec la doctrine
d'escalade canonique.