---
type: Concept
title: Superman Growth — procédure canonique de fixation du DoD attention par mandat B1
description: La question ouverte "DoD attention mesurable" (cf. superman-5-questions-ouvertes-cloture.md §Question 4) n'a pas été tranchée en vague 2 — la vague 3 la ferme par une procédure canonique en 5 étapes : (1) mandat B1 propose un scope, (2) Superman propose 3 DoDs candidats (MQL/conversion/reach), (3) JohnJones arbitre le DoD final, (4) Council tranche en désaccord, (5) DoD chiffré par seuil verrouillé. Le DoD attention est mandat-spécifique, pas canon.
tags: [superman, growth, dod, attention, procedure, canon, mql, conversion, reach]
generated: { by: minimax-m3, at: 2026-08-19T07:30:00Z }
verified:
  - { by: process:lecture-corpus-superman-vague-3, at: 2026-08-19T07:30:00Z }
sources:
  - id: questions-ouvertes-tour2
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-5-questions-ouvertes-cloture.md"
    title: Superman — clôture des 5 questions ouvertes du tour 1 (Q4 escaladée)
    last_modified: 2026-08-19
  - id: mql-sql-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-mql-sql-handoff-contract.md"
    title: Superman ↔ JohnJones contrat MQL-SQL — DoD partagé
    last_modified: 2026-08-19
  - id: b2-b3-jtbd-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: B2 → B3 contract — DoD chiffré par seuil obligatoire
    last_modified: 2026-08-19
  - id: redflag-2-arbiter
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-redflag-2-arbiter.md"
    title: Red flag #2 — gel du scaling quand Sales est red
    last_modified: 2026-08-19
  - id: b2-three-cooperation-modes
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-three-cooperation-modes.md"
    title: Trois modes — negotiation = arbitrage DoD amendé
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Superman Growth — procédure canonique de fixation du DoD attention

## La question ouverte Q4 — arbitrer MQL vs conversion vs reach

La vague 2 Superman (cf. `superman-5-questions-ouvertes-cloture.md`
§« Question 4 — DoD attention mesurable ») a documenté **3
DoDs candidats** pour mesurer l'attention Superman :

1. **MQL qualifiés ICP** — `MQL qualifies ICP: 1000 en 90 jours`
   (lié au contrat MQL-SQL).
2. **Taux de conversion MQL → SQL** — `conversion_rate: 30 % sur
   30 jours`.
3. **Volume d'attention** — `reach: 10k visiteurs uniques par
   cycle`.

Aucun des 3 n'est ancré canoniquement. La vague 2 a
**escaladé** la question au B2 Council sans trancher.

Vague 3 ferme Q4 par une **procédure canonique** : le DoD
attention est **mandat-spécifique**, pas un canon fixe. La
procédure **arbitre** entre les 3 candidats pour chaque
mandat B1.

## Pourquoi le DoD attention ne peut pas être canonique

Trois raisons structurelles :

### 1. Le périmètre Superman est mandat-dépendant

`domain-perimeter.md` pose 3 axes pour Superman : attention,
qualification amont, signal marché. **Chaque axe peut être
le DoD** selon le mandat B1 :

- *« Pivoter US premium $7.5-25K ACV »* → axe qualification
  amont (MQL qualifies ICP US).
- *« Awareness pre-launch Q1 »* → axe attention (reach
  mémorisation).
- *« Contenu de fond SEO long terme »* → axe signal marché
  (trafic organique + position mots-clés).

Un DoD canon unique **forcerait** un mandat à s'aligner sur
un axe qui n'est pas le sien. C'est un **anti-pièges matrice**
(cf. `b2-harmonization-matrix-exploitable.md` §« Anti-pièges »).

### 2. La doctrine canonique exige un DoD chiffré par seuil

`b2-b3-jtbd-handoff-contract.md` §« Ce que B2 Council promet »
pose `dod_bornee: - critere: <text>, seuil: <chiffre>`. Le
DoD chiffré est **obligatoire**, mais le **contenu** du
critère est projet-métier.

### 3. Le contrat MQL-SQL co-signe déjà un DoD partagé

`superman-mql-sql-handoff-contract.md` pose le DoD MQL
co-signé par Superman et JohnJones. Si le DoD attention
canonique est MQL qualifies ICP, il **écrase** le contrat
MQL-SQL, qui est par construction **négocié** entre 2
capitaines (pas imposé par 1).

## La procédure canonique en 5 étapes

### Étape 1 — Le mandat B1 propose un scope

Le mandat B1 (cf. `b1-mandate-packet-spec.md`) inclut un
**scope** explicite : *« pivoter US premium »*, *« awareness
pre-launch »*, *« contenu SEO long terme »*, *« co-branding
partenaire Z »*, etc. Le scope **détermine l'axe** du DoD
attention.

**Qui décide** : Summers (B1) — c'est la direction. Mais
Summers ne **fixe pas** le DoD. Summers fixe le scope, le
DoD est arbitrée par Superman + JohnJones.

### Étape 2 — Superman propose 3 DoDs candidats

Pour le scope mandat, Superman propose **3 DoDs chiffrés**,
alignés sur les 3 axes (MQL/conversion/reach) :

```yaml
dod_candidats:
  - critere: "MQL qualifies ICP US premium"
    seuil: 1000
    fenetre: 90j
    axe: qualification_amont
  - critere: "Conversion rate MQL → SQL"
    seuil: 30%
    fenetre: 30j_post_qualification
    axe: qualification_amont
  - critere: "Reach visiteurs uniques"
    seuil: 10000
    fenetre: 90j
    axe: attention_brute
```

**Qui décide** : Superman — c'est son périmètre. Mais
Superman ne tranche pas seul. Les 3 candidats sont proposés
au Council.

### Étape 3 — JohnJones arbitre le DoD final

Le DoD final est **arbitré par JohnJones** (Sales), parce
que le DoD traverse le pair-check #1 (Growth → Sales). Si
le DoD est MQL qualifies ICP, JohnJones doit valider qu'il
**peut réceptionner** les MQL (son ICP, son équipe, sa
capacité). Si le DoD est conversion, JohnJones doit valider
que les MQL deviennent SQL — ce qui dépend de son pipeline.

**Qui décide** : JohnJones — arbitre du pair-check #1.

**Issue** : JohnJones choisit un des 3 candidats, ou en
propose un 4ᵉ qu'il chiffre (ex : *« pipeline value créé »
*).

### Étape 4 — Le Council tranche en cas de désaccord

Si Superman et JohnJones ne s'accordent pas sur un DoD
parmi les 3 (ou 4), le Council tranche en mode `negotiation`
(cf. `b2-three-cooperation-modes.md`).

**Qui décide** : le Council, sur la base de North Star >
cycle > risque > effort.

**Issue** : DoD amendé, pas DoD retiré (cf.
`b2-three-cooperation-modes.md` §« Negotiation — conflit de
DoDs »). Le remplacement est documenté dans le packet.

### Étape 5 — Le DoD chiffré est verrouillé en packet mésoperpétuel

Le DoD final est consigné dans un packet mésoperpétuel
`decision: accepted, mode: <parallel|handoff|negotiation>`,
avec le DoD dans `proof_expected` ou en champ dédié :

```yaml
meso_decision_id: B2-MESO-DECISION-2026-XX
source_mandate: B1-B2-MANDATE-2026-XX
mode: negotiation
impacted_domains:
  - growth
  - sales
tradeoff: "DoD attention fixé : MQL qualifies ICP US,
  1000 unités en 90 jours. Remplacement de 'reach 10k' par
  'MQL qualifies ICP'."
decision: accepted
dod_attention:
  critere: MQL qualifies ICP US premium
  seuil: 1000
  fenetre: 90j
  signe: superman (proposition) + john_jones (arbitrage)
proof_expected:
  - B2 gate growth update (doD atteint à J+90)
  - B2 gate sales update (MQL réceptionnés en pipeline)
  - B3 proof path (Rocket_Auto automation active)
next_review: <date J+90>
superman_reading: v4_canonical
```

Le packet est **append-only D4** — un DoD différent produit
un **nouveau** packet, pas une édition.

## Les trois propriétés du DoD attention verrouillé

Un DoD attention verrouillé doit respecter **3 propriétés**,
héritées du catalogue 8 vetos :

### Propriété 1 — Catégoriel

Le DoD cible **une classe** : qualification amont (MQL),
conversion (taux), attention brute (reach). Pas une classe
mixée (*« je veux MQL et reach et conversion »* — c'est une
**liste de courses**, pas un DoD).

### Propriété 2 — Vérifiable

Le DoD porte **un seuil chiffré** (cf.
`b2-b3-jtbd-handoff-contract.md` §`dod_bornee`). Un DoD *«
améliorer la satisfaction client »* est insuffisant — il
faut *« NPS ≥ 40 sur 100 réponses mesurées »*.

### Propriété 3 — Non-négociable au niveau mésoperpétuel

Une fois verrouillé en packet mésoperpétuel, le DoD ne
**peut pas** être modifié sans un **nouveau** packet. Le
B2 sponsor ne peut pas le re-trancher seul. Seul B1
(escalade) peut amender un DoD verrouillé.

## Le lien avec le red flag #2

Le DoD attention est **l'instrument de mesure** qui permet
au red flag #2 (cf. `superman-redflag-2-arbiter.md`) de
fonctionner. Sans DoD chiffré, le red flag #2 ne peut pas
déclencher — la condition 1 (Superman `GROWTH_READY`) n'est
pas vérifiable.

**Cascade** :

1. Le mandat B1 fixe le scope.
2. Superman propose 3 DoDs.
3. JohnJones arbitre.
4. Le DoD est verrouillé.
5. Superman émet `GROWTH_READY` (DoD chiffré connu).
6. Le red flag #2 peut déclencher sur **DoD chiffré non-tenu**
   (métrique de retour).

## Le lien avec le contrat MQL-SQL

Le DoD attention peut être **identique** au DoD MQL du
contrat MQL-SQL si Superman et JohnJones s'accordent sur
*« MQL qualifies ICP »*. Dans ce cas :

1. Le DoD attention porte sur MQL qualifies ICP.
2. Le contrat MQL-SQL est **étendu** — il porte à la fois sur
   le DoD partagé (qualification amont) et sur le DoD
   attention (mesure de croissance Growth).

Si le DoD attention est **reach** (pas MQL), le contrat
MQL-SQL reste **distinct** — Superman mesure reach, JohnJones
mesure MQL→SQL. C'est un **double DoD**, ce qui complique le
rapport sans le rendre impossible.

## Les trois cas-types

Pour illustrer la procédure, 3 cas-types de mandat B1 et
leur DoD attention attendu.

### Cas-type 1 — « Pivoter US premium $7.5-25K ACV Q4 »

- **Scope** : qualification amont US premium.
- **Superman propose** : MQL qualifies ICP US (1000 en 90j) ;
  conversion MQL→SQL (30 % en 30j) ; reach US geo (50k en
  90j).
- **JohnJones arbitre** : **MQL qualifies ICP US (1000 en
  90j)**. Conversion ne tient pas — Salesforce pipeline
  capacity limite. Reach ne tient pas — pas d'ICP, on jette
  l'attention.
- **Council tranche** : accepté sans désaccord.
- **DoD verrouillé** : MQL qualifies ICP US, 1000, 90j.

### Cas-type 2 — « Awareness pre-launch Q1 »

- **Scope** : attention brute pre-launch.
- **Superman propose** : reach (50k en 60j) ; mémorisation
  (60 % recall survey) ; intent (10k page pricing visits en
  60j).
- **JohnJones arbitre** : **reach (50k en 60j)**. Mémorisation
  trop cher à mesurer. Intent trop tardif — la cible est en
  pre-launch.
- **Council tranche** : accepté.
- **DoD verrouillé** : reach 50k, 60j.

### Cas-type 3 — « Contenu SEO long terme »

- **Scope** : signal marché long terme.
- **Superman propose** : trafic organique (10k visites/mois) ;
  position mots-clés (top 3 sur 50 mots-clés) ; backlinks
  (100 domaines référents).
- **JohnJones arbitre** : **trafic organique + position mots-clés
  combinés**. Backlinks trop tardif à mesurer.
- **Council tranche** : accepté avec amendement — DoD
  combiné (10k visites/mois ET top 3 sur 50 mots-clés).
- **DoD verrouillé** : trafic 10k/mois + top 3 sur 50 KW,
  12WY-2026-Q3.

## Anti-pièges

- **DoD canon unique imposé.** Refusé — le DoD est
  mandat-spécifique par les 3 raisons structurelles ci-dessus.
- **DoD sans seuil chiffré.** Refusé — DoD *« améliorer »* est
  insuffisant (cf. propriété 2).
- **DoD modifié sans nouveau packet.** Refusé — D4 append-only.
  Tout DoD différent = nouveau packet.
- **DoD décidé par Summers seul.** Refusé — Summers fixe le
  scope, pas le DoD. Le DoD est arbitré Superman + JohnJones,
  avec Council en cas de désaccord.
- **DoD attention qui écrase le contrat MQL-SQL.** Acceptable
  s'il est explicitement combiné, refusé si implicite.

## Liens

- [[superman-5-questions-ouvertes-cloture]] — Q4 escaladée
- [[superman-mql-sql-handoff-contract]] — le contrat MQL-SQL
- [[superman-redflag-2-arbiter]] — le red flag #2
- [[b2-b3-jtbd-handoff-contract]] — DoD chiffré obligatoire
- [[b2-three-cooperation-modes]] — negotiation = DoD amendé
- [[b1-mandate-packet-spec]] — le mandat B1 source

## Note de confiance

**Confirmé par machine pour la procédure (5 étapes), reconstruit
pour les 3 DoDs candidats.** La procédure 5 étapes est
**reconstruite** par lecture critique de `b2-three-cooperation-modes.md`
+ `b2-b3-jtbd-handoff-contract.md` + `b2-meso-decision-packet-spec.md`
+ la pratique Superman documentée dans `domain-perimeter.md`.
Les 3 DoDs candidats (MQL/conversion/reach) sont **projetés**
par lecture critique de la pratique documentée et du contrat
MQL-SQL. Les 3 cas-types sont **projetés** par analogie avec
des mandats B1 plausibles (pivot US 2026-07-15 cité dans
`b2-meso-decision-packet-spec.md` §« Exemple »). Les 3
propriétés du DoD verrouillé sont **projetées** par lecture
critique de `b2-eight-domain-vetoes-catalogue.md` §« Les trois
propriétés d'un veto légitime ». Le lien avec le red flag #2
est **confirmé** par `superman-redflag-2-arbiter.md` §« Pourquoi
Superman est le détecteur principal ».
