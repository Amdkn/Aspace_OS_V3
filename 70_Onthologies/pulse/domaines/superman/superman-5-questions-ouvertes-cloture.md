---
type: Concept
title: Superman Growth — clôture des 5 questions ouvertes du tour 1
description: Le tour 1 Superman a listé 5 questions ouvertes sans réponse formelle : (1) ICP canon vs projet, (2) périmètre Brand transverse, (3) analytics stack ownership, (4) DoD attention mesurable, (5) posture dormance vs active. Vague 2 fournit une réponse tranchée pour 3 d'entre elles (ICP co-signé, Brand reste People transverse, analytics reste arbitrage Council) et une projection en escalade B2 pour 2 (DoD attention, posture dormance — déjà tranchée dans la doctrine).
tags: [superman, growth, cloture, questions-ouvertes, icp, brand, analytics, dod-attention, dormance]
generated: { by: minimax-m3, at: 2026-08-19T05:50:00Z }
verified:
  - { by: process:lecture-corpus-superman-vague-2, at: 2026-08-19T05:50:00Z }
sources:
  - id: jtbd-emit-receive-tour1
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/jtbd-emit-receive.md"
    title: Superman JTBD tour 1 — 5 questions ouvertes liste
    last_modified: 2026-08-19
  - id: mql-sql-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-mql-sql-handoff-contract.md"
    title: Superman ↔ JohnJones contrat MQL-SQL
    last_modified: 2026-08-19
  - id: redflag-2-arbiter
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-redflag-2-arbiter.md"
    title: Red flag #2 arbiter
    last_modified: 2026-08-19
  - id: dormance-active-posture
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-dormance-active-posture.md"
    title: Superman dormance posture
    last_modified: 2026-08-19
  - id: domain-perimeter
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/domain-perimeter.md"
    title: Périmètre tour 1 — 3 frontières
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Superman Growth — clôture des 5 questions ouvertes du tour 1

## Les 5 questions non répondues au tour 1

Le tour 1 Superman a listé cinq questions ouvertes dans `ETAT_DOMAINES.md` sous `## Superman (Growth)` (cf. aussi `jtbd-emit-receive.md` §« Le 7ᵉ agent manquant — projection » + autres concepts) :

1. **ICP canon vs projet** — y a-t-il un ICP canonique Superman,
   ou chaque projet (US premium, EU SMB) définit son ICP ?
2. **Brand transverse** — Superman Growth tient-il le brand
   work, ou reste-t-il cantonné au périmètre attention ?
3. **Analytics stack ownership** — Superman ou Cyborg IT tient
   l'analytics stack (Mixpanel, Amplitude, PostHog) ?
4. **DoD attention mesurable** — quel DoD chiffré Superman
   porte-t-il quand l'attention est qualifiée mais pas
   convertie ?
5. **Dormance vs active** — Superman peut-il être dormant, ou
   reste-t-il structurellement actif ?

Vague 2 tranche trois questions et formalise une position pour les
deux autres.

## Question 1 — ICP canon vs projet : **ICP co-signé, pas de canon Superman**

### Réponse vague 2

L'ICP n'est **pas** un canon Superman. C'est un **contrat
co-signé** entre Superman (Growth) et JohnJones (Sales).

### Justification

Le canon Superman (V4) ne pose aucun ICP spécifique. L'ICP
dépend du mandat B1 (Summers) — pivot US premium, EU SMB,
etc. Chaque mandat produit son propre ICP, validé conjointement
par Superman (qualification amont) et JohnJones (qualification
aval). Le format est le contrat MQL-SQL (cf.
`superman-mql-sql-handoff-contract.md`) avec un
`mql_contract_id` unique par ICP.

### Conséquence opérationnelle

Superman Growth n'a pas de **doctrine ICP canonique** à
défendre. Il porte une **méthodologie de co-signature** ICP
(cf. les trois Seuils de qualification partagée : démographie,
intent, engagement). Le captain sponsor qui mandate Superman
sans ICP co-signé est en **red flag #2 actif** (cf.
`superman-redflag-2-arbiter.md`).

### Anti-pièce

Un arbitrage qui pose *« l'ICP canon Superman »* comme
référence contredit la doctrine de co-signature. Le Council
doit refuser ou exiger un ICP mandat-spécifique.

## Question 2 — Brand transverse : **People (Green Lantern) tient la doctrine Brand, Superman Growth exécute**

### Réponse vague 2

People (Green Lantern) tient la **doctrine Brand** (capital
narratif de long terme). Superman Growth **exécute** du Brand
via StarLord_Story et Groot_Content, mais c'est un scope
**arbitré**, pas un périmètre acquis.

### Justification

Le triplet 19 (Coach OS V1) cite Superman comme *« People &
Brand »*, mais V4 sépare Superman (Growth) de Green Lantern
(People). Le Brand comme doctrine reste People — la production
Brand peut passer par la squad Guardians, mais le périmètre
doctrinal reste People (cf. `domain-perimeter.md` §« Frontière #2 »
+ `superman-v4-vs-v1-arbitration-rule.md`).

### Conséquence opérationnelle

Un mandat Brand mandaté par People sur Superman Growth doit
être **arbitré** par Council en mode parallel (livrable
interne) ou handoff (livrable public, validation People
requise). Superman ne signe pas de proof path Brand sans
validation People.

### Anti-pièce

Un Superman qui signe un proof path Brand comme Growth work
sans validation People est en **scope creep silencieux** (cf.
`b2-b3-jtbd-handoff-contract.md` §« Scope creep »). Le captain
sponsor doit refuser.

## Question 3 — Analytics stack ownership : **arbitrage Council, pas absorption Growth**

### Réponse vague 2

L'analytics stack (Mixpanel, Amplitude, PostHog) reste une
**infrastructure partagée Cyborg IT** avec **consommation
**Surveyman Growth. La frontière est tranchée par arbitrage
Council, pas par absorption Growth (qui absorberait Nebula_Analytics
comme 7ᵉ agent).

### Justification

Le couplage Superman↔IT est asymétrique (Superman dépend de
Cyborg pour l'infra, Cyborg ne dépend pas de Superman pour la
doctrine analytics — cf. `pair-checks-dependencies.md` §«
Couplage Superman ↔ IT »). Absorber l'analytics dans Growth
dissout la frontière sans l'arbitrer.

L'écartement de Nebula_Analytics (cf.
`superman-guardians-7th-agent-position.md` §« Pourquoi Peter_Quill_Orchestrator
plutôt que Nebula_Analytics ») repose sur cette asymétrie :
l'analytics reste Cyborg, Peter est le 7ᵉ agent Growth.

### Conséquence opérationnelle

Tout dashboard PostHog est déployé par Cyborg (matrice
d'harmonisation pair-check #4 Product → IT étendue à Growth →
IT). Superman configure les événements et lit les données.
Si le dashboard crashe, c'est Cyborg qui escalade (veto IT).
Si le dashboard est mal interprété, c'est Superman qui
escalade (veto Growth).

### Anti-pièce

Une absorption Nebula_Analytics dans la squad Growth **avant
arbitrage Council** est un **unilateralisme B2**. Le captain
sponsor doit refuser.

## Question 4 — DoD attention mesurable : **escalade B2 Council pour arbitrage chiffré**

### Réponse vague 2

Le DoD attention mesurable est une question **non tranchée**
par vague 2. Elle remonte au B2 Council pour arbitrage.

### Justification

Trois DoDs candidats sont concevables :

1. **MQL qualifiés** — `MQL qualifies ICP` (cf. contrat MQL-SQL).
3. **Taux de conversion MQL → SQL** — `conversion_rate: 30 %
   sur 30 jours` (à arbitrer).
4. **Volume d'attention** — `reach: 10k visiteurs uniques par
   cycle` (trop facile à gonfler, signal faible).

Aucun des trois n'est ancré canoniquement. La forme du DoD
attention dépend du mandat B1 :

- Un mandat *« pivoter US premium »* appelle un DoD **MQL
  qualifies ICP US**.
- Un mandat *« awareness pre-launch »* appelle un DoD
  **reach + mémorisation**.
- Un mandat *« contenu de fond SEO »* appelle un DoD
  **trafic organique + position mots-clés**.

La doctrine canonique du DoD est **chiffré par seuil** (cf.
`b2-b3-jtbd-handoff-contract.md` §« dod_bornee »), mais le
**contenu du seuil** est mandat-spécifique.

### Conséquence opérationnelle

Superman mandate au B2 Council une **procédure de fixation du
DoD attention** par mandat B1. La procédure proposée :

1. Le mandat B1 propose un scope (US premium, EU SMB, etc.).
2. Superman propose trois DoDs candidats (MQL / conversion /
   reach).
3. JohnJones (Sales) arbitre le DoD final — le DoD qui
   traverse le pair-check #1.
4. Le Council tranche en cas de désaccord.

### Action concrète vague 2

Cette escouade **ne tranche pas** le DoD attention canonique.
Elle consigne la **procédure de fixation** dans le journal
Council comme `decision: open_question, domaine: growth,
motif: dod-attention-mesurable, depuis: YYYY-MM-DD,
escalade_b2_council: true`.

## Question 5 — Dormance vs active : **dormance concevable, trois conditions cumulatives**

### Réponse vague 2

Superman Growth **peut être dormant** quand les trois
conditions canoniques sont remplies cumulativement (cf.
`superman-dormance-active-posture.md`). La doctrine est
extrapolée d'Aquaman, mais elle s'applique par symétrie.

### Justification

Trois scénarios de dormance Superman sont identifiables :

1. Pas de mandat B1 de scaling (DoD vide).
2. Marché sans vague d'attention (`NEEDS_SIGNAL` permanent).
3. Sales en `BLOCKED_COMMITMENT` prolongé (dormance croisée).

### Conséquence opérationnelle

La posture dormance est documentée dans le journal Council
avec `decision: dormant, domaine: growth`. La doctrine des
trois conditions + trois déclencheurs + sept règles est posée
par `superman-dormance-active-posture.md`.

### Anti-pièce

Une dormance déclarée sans les trois conditions cumulatives
est refusée par le Council. Une dormance qui ne se réveille
pas après > 1 cycle 12WY escalade B1 pour dissolution.

## Récapitulatif vague 2 — réponses apportées aux questions ouvertes

| Question | Réponse vague 2 | Statut |
|---|---|---|
| ICP canon vs projet | ICP co-signé, pas de canon Superman | **Tranchée** |
| Brand transverse | People doctrine, Superman execution arbitrée | **Tranchée** |
| Analytics stack ownership | Arbitrage Council, pas absorption Growth | **Tranchée** |
| DoD attention mesurable | Procédure de fixation par mandat B1 | **Escalade B2 Council** |
| Dormance vs active | Dormance concevable, 3 conditions cumulatives | **Tranchée** |

Quatre questions sur cinq sont tranchées. Une seule (DoD
attention) reste ouverte — elle est consignée en escalade B2
Council pour arbitrage chiffré.

## Anti-pièges transversal

- **Question tranchée puis ré-ouverte.** Une question tranchée
  en vague 2 peut être ré-ouverte par un arbitrage Council
  ultérieur. La clôture vague 2 n'est pas **permanente**.
- **Escalade B2 oubliée.** La question 4 (DoD attention)
  doit être **explicitement escaladée** au Council, pas
  seulement consignée dans ce concept.
- **Anti-pièce unilatérale.** Une décision vague 2 sur les
  questions tranchées (1, 2, 3, 5) peut être **invalide** par
  le Council si elle manque une propriété (catégoriel,
  vérifiable, non-négociable au niveau mésoperpétuel).

## Liens

- [[jtbd-emit-receive]] — les 5 questions ouvertes liste
- [[superman-mql-sql-handoff-contract]] — Q1 réponse
- [[superman-v4-vs-v1-arbitration-rule]] — Q2 Brand transverse
- [[superman-guardians-7th-agent-position]] — Q3 analytics écart Nebula
- [[superman-dormance-active-posture]] — Q5 dormance
- [[superman-redflag-2-arbiter]] — Q4 lien red flag #2 / DoD attention
- [[domain-perimeter]] — Q2 Brand transverse ancrage

## Note de confiance

**Confirmé par machine pour 3 réponses (Q1, Q2, Q3) ; reconstruit
pour Q5 ; escaladé pour Q4.** Q1 (ICP co-signé) est ancrée par
le contrat MQL-SQL (cf. `superman-mql-sql-handoff-contract.md`).
Q2 (Brand transverse) est ancrée par le triplet 19 lecture V4 vs
V1 + la doctrine People (cf. `superman-v4-vs-v1-arbitration-rule.md`).
Q3 (analytics arbitrage) est ancrée par la matrice d'harmonisation
pair-check #4 Product → IT étendue + le couplage asymétrique
Superman↔IT (cf. `pair-checks-dependencies.md` tour 1). Q5
(dormance) est **reconstruite** par symétrie avec Aquaman (cf.
`superman-dormance-active-posture.md`). Q4 (DoD attention) est
**escaladée** comme open question au B2 Council — cette escouade
ne tranche pas. La procédure de fixation proposée (4 étapes) est
**projetée** à partir du format packet mésoperpétuel canonique +
la doctrine `b2-b3-jtbd-handoff-contract.md` §« dod_bornee ».