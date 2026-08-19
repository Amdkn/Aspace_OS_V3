---
type: Concept
title: Wonder Woman en C — pourquoi Finance est Consulted et pas Accountable sur les pair-checks #5 et #6
description: Le RACI par rang positionne Wonder Woman en C (Consulted) sur les pair-checks #5 (Finance→Growth) et #6 (Finance→Product). Ce n'est pas une faiblesse — c'est la conséquence directe de la règle ADR-MESH-L2-001 (« un datum, un owner »). Wonder Woman arbitre la cohérence financière globale (pair-check #4 transpose au red flag), pas la handoff entre le domaine amont et le domaine aval. Son pouvoir A effectif vient du droit de blocage hard sur la marge négative, pas du RACI.
tags: [b2, finance, raci, consulted, accountable, pair-check, wonder-woman, adr-mesh, blocking-authority]
generated: { by: minimax-m3, at: 2026-08-19T03:50:00Z }
verified:
  - { by: process:lecture-domaine-finance-corpus, at: 2026-08-19T03:50:00Z }
sources:
  - id: raci-by-rank
    resource: "C:/Usersado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang sur les 9 pair-checks
    last_modified: 2026-08-19
  - id: finance-principles
    resource: "C:/Usersado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/06_Finance_WonderWoman_Thunderbolts/03_WONDERWOMAN_FINANCE_PRINCIPLES.md"
    title: Wonder Woman Finance Principles (v4)
    last_modified: 2026-06-25
  - id: omk-control-room
    resource: "C:/Usersado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/06_Finance_WonderWoman_Thunderbolts/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: OMK Finance — B2 Domain Control Room
    last_modified: 2026-05-25
  - id: avengers-wheel
    resource: "C:/Usersado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel
    last_modified: 2026-08-17
  - id: council-rule
    resource: "C:/Usersado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Wonder Woman en C — pourquoi Finance est Consulted et pas Accountable sur les pair-checks #5 et #6

## La lecture RACI brute

Le tableau du RACI par rang
(`b2-pair-check-raci-by-rank.md`) pose :

| # | Pair-check | A | R | C | I |
|---|---|---|---|---|---|
| 5 | Finance → Growth | B2 Growth | B3 Guardians | **B2 Finance** | B1, B3 Thunderbolts |
| 6 | Finance → Product | B2 Product | B3 Avengers | **B2 Finance** | B1, B3 Thunderbolts |

Wonder Woman apparaît deux fois, deux fois en **C** (Consulted).
Elle n'est Accountable sur aucun des deux pair-checks. C'est
l'**unique** capitaine de la wheel avec une position C sur toutes
les transitions cross-domaines qui la concernent (Sales est A sur
Growth × Sales, Ops est A sur Sales × Ops ET Product × Ops, IT est
A sur Product × IT — seul People a une répartition analogue par
transversalité, pas par absence de Accountable).

## Pourquoi C, pas A — la raison racine

Le RACI par rang pose `A = B2 en aval de la transition` comme
**règle générale** (`b2-pair-check-raci-by-rank.md` §« Pourquoi A
= B2 en aval, pas B1 »). Pour les pair-checks #5 et #6, l'aval
n'est pas Finance — c'est Growth (pair-check #5) ou Product
(pair-check #6). Wonder Woman est upstream de la handoff, pas en
aval.

Cela vient directement de la règle **ADR-MESH-L2-001**
(`03_WONDERWOMAN_FINANCE_PRINCIPLES.md` §« Finance ↔ neighbours
boundary ») :

> « It consumes Sales' deal values, Growth's CAC, IT's compute
> cost, Ops' delivery cost, but **owns none of those source data**.
> »

Finance **lit** la donnée, **ne la possède pas**. Le ownership de
la donnée reste chez le domaine qui l'a produite. Une
consultation sur la transition teste la cohérence financière, pas
la propriété de la donnée. C'est cohérent avec le RACI C :
Wonder Woman **exprime un avis**, mais Superman ou Flash
**tranchent** parce que c'est leur donnée.

## Les deux asymétries clés — où Wonder Woman a plus que le RACI

### Asymétrie 1 — Droit de blocage hard sur la marge négative

`00_B2_DOMAIN_CONTROL_ROOM.md` §« Blocking Authority » pose :

> « Blocks Product when it creates hidden recurring cost, unclear
> pricing, or margin-negative delivery. »

Ce droit de blocage est **supérieur** au statut Consulted du
RACI : Wonder Woman peut bloquer un produit même si Flash (A) en
prend la responsabilité et même si le pair-check #6 passe au
vert. C'est une **autorité B2 effective** sur la viabilité
financière d'une release.

La doctrine sous-jacente : le pair-check #6 (« Le coût de build
protège-t-il la marge ? ») teste **la cohérence du transfert
croisé**. Le blocking authority teste **la solvabilité du
résultat**. Les deux sont distincts : un produit peut passer le
pair-check #6 (marge OK) mais être bloqué par Wonder Woman
durant l'exécution (marge passée en négatif à cause d'un coût
caché révélé plus tard).

### Asymétrie 2 — Veto catalogue Finance (granularité unaire)

Le veto catalogue de Wonder Woman (cf.
[[wonder-woman-recurrent-spend-veto]]) est **unidimensionnel** :
une dépense récurrente sans date de revue et sans métrique. Ce
veto est **indépendant** du RACI — Wonder Woman peut l'opposer
même quand elle est C sur le pair-check amont. Le veto est un
**arrêt de granularité fine**, pas un arbitrage de transition.

### Asymétrie 3 — A bascule sur le red flag #4

Le red flag #4 (« Finance red + Growth/Product green ») renverse
le RACI pour Wonder Woman : la décision vient de **son** domaine
(le déclencheur est Finance), donc A bascule à Wonder Woman
(selon mon extrapolation, à confirmer en cycle réel — voir « Note
de confiance »). Cf. [[wonder-woman-red-flag-4-trigger]].

## Pourquoi cette répartition est cohérente avec la doctrine

La règle `A = B2 en aval` a un corollaire non-écrit mais
reconstructible : un capitaine qui n'a jamais Accountable sur
aucune transition **est par construction un coordinateur**, pas
un owner. Mais Wonder Woman n'est pas un coordinateur — elle est
un capitaine **de vérité et solvabilité**. La doctrine
reconstruit l'asymétrie comme suit :

1. **A sur la vérité comptable interne** : la réconciliation,
   la cohérence des sources, le reporting — c'est le périmètre
   Finance racine.
2. **A sur le pricing et le reinvestissement** : décisions
   internes sans跨-domain handoff immédiat — c'est la propriété
   explicite posée dans `03_WONDERWOMAN_FINANCE_PRINCIPLES.md`
   §« Wonder Woman (B2 owner) is non-délégable on pricing
   strategy and reinvestment allocation ».
3. **C sur les transitions cross-domaines** : le pair-check
   teste la cohérence d'une handoff où Finance est upstream.
   L'aval (Growth, Product) possède la décision ; Finance
   remontent la cohérence.
4. **A bascule** quand le déclencheur vient de Finance (red flag
   #4) ou quand un blocage hard (marge négative) s'oppose à un
   lancement.

La matrice n'est pas un tableau d'autorité unique ; c'est un
**patchwork de positions** dont la cohérence est tenue par la
doctrine sous-jacente, pas par la case du tableau.

## L'inverse côté Growth et Product — pourquoi eux sont A

Superman (Growth) est A sur pair-check #5 parce que la transition
teste « la dépense est-elle justifiée par l'apprentissage ou la
traction ? ». **L'apprentissage et la traction sont des KRs
Growth** (KR-4b CAC payback est partagé mais l'apprentissage est
essentiellement Growth, F6). Superman tranche sur sa donnée.

Flash (Product) est A sur pair-check #6 parce que la transition
teste « le coût de build protège-t-il la marge ? ». **Le coût de
build est un input Product** (cf. `00_B2_DOMAIN_CONTROL_ROOM.md`
§« Required Input From Product »). Flash fournit l'estimation ;
Wonder Woman remontent l'arbitrage financier.

Le couple **C sur pair-check + A sur vérité** est ce qui rend
Wonder Woman **utile sans être envahissante**. Une capitaine qui
serait A sur les pair-checks #5 et #6 reviendrait à **aspirer la
propriété** des coûts et de l'apprentissage chez Finance, en
violation de l'ADR-MESH-L2-001.

## L'asymétrie cachée — Wonder Woman A sur quasi-zéro pair-check

Comparaison rapide avec les autres capitaines :

| Capitaine | Pair-checks où A | Pair-checks où C | Pair-checks où R |
|---|---|---|---|
| Superman (Growth) | 1, 5, 7 | — | — |
| JohnJones (Sales) | (Growth×Sales) | — | — |
| Flash (Product) | 3, 4, 6, 8 | — | — |
| Batman (Ops) | 2, 3 | — | — |
| Cyborg (IT) | 4 | — | — |
| **Wonder Woman (Finance)** | — | **5, 6** | — |
| Green Lantern (People) | — | 9 | — |
| Aquaman (Legal) | — | 7, 8 | — |

Wonder Woman et Aquaman sont les deux capitaines **sans aucun A
sur les 9 pair-checks canoniques**. Wonder Woman arbitre la
vérité et la solvabilité ; Aquaman arbitre la conformité. Les
deux sont des **gardiens**, pas des **producteurs de transition**.
Leur pouvoir A effectif passe par d'autres mécanismes (vetos,
build gates, blocking authority, red flags).

C'est cohérent avec la doctrine fractal : **les gardiens
s'opposent, les producteurs tranchent**. Wonder Woman est un
gardien de la cohérence financière ; Superman et Flash sont les
producteurs de croissance et de produit.

## Le piège si on lit le RACI au premier degré

Un lecteur hostile du RACI pourrait dire : « Wonder Woman est
faible, elle n'a aucun A. Superman et Flash peuvent l'ignorer. »
C'est **faux** pour quatre raisons :

1. **Le veto catalogue** bloque les dépenses récurrentes sans
   forme — granularité fine qui touche les paquets B2.
2. **Le blocking authority** sur marge négative bloque le
   produit indépendamment du pair-check #6.
3. **Le red flag #4** renverse le RACI vers Finance.
4. **L'escalade B1 directe** : Wonder Woman peut escalader B1
   sans passer par Superman/Flash si la solvabilité est en
   jeu (KR-5g, runway <6 mois).

Autrement dit, le RACI est la **carte des positions en régime
normal** ; les vetos, gates, red flags, et escalades B1 sont la
**carte des positions en régime de stress**. Wonder Woman est
faible en régime normal, forte en régime de stress. C'est le
profil type d'un gardien.

## Anti-pièges — erreurs à éviter

- **Croire que C =旁观者**. C = avis obligatoire, pas silence.
  Wonder Woman qui reste silencieuse sur un pair-check #6 où
  elle a un input financier trahit sa responsabilité.
- **Ignorer le veto catalogue** parce que le RACI est C.
  Le veto est unaire, transversal au RACI. Wonder Woman peut
  bloquer une dépense récurrente même si Superman est A sur
  le pair-check amont.
- **Escalader systématiquement à B1**. Le blocage hard et le
  red flag sont des outils de granularité mésoperpétuelle. Si
  Wonder Woman escalade chaque marge négative à B1, elle casse
  l'escalier canonique. Le B2 Council arbitrage le cas normal ;
  B1 arbitre les wheel-states en conflit, pas les blocages
  unaires.
- **Confondre C sur pair-check avec C sur red flag**. Le RACI
  pair-check reste C. Le red flag #4 renverse A à Wonder Woman.
  Ce sont deux postures distinctes, pas une seule.

## Liens

- [[wonder-woman-finance-frontiers]] — le périmètre Finance
- [[wonder-woman-finance-couplings]] — les 7 couplages
- [[wonder-woman-red-flag-4-trigger]] — le basculement A
- [[b2-pair-check-raci-by-rank]] — la matrice RACI source
- [[b2-eight-domain-vetoes-catalogue]] — le veto complémentaire

## Note de confiance

**Confirmé par machine.** Le statut C de Wonder Woman sur
pair-checks #5 et #6 est cité verbatim du RACI par rang. Les deux
asymétries (blocking authority + veto catalogue) sont **posées
explicitement** dans `00_B2_DOMAIN_CONTROL_ROOM.md` §« Blocking
Authority » et `b2-eight-domain-vetoes-catalogue.md` ligne 28.
L'asymétrie « A bascule sur red flag #4 » est **projetée** —
elle n'est pas écrite littéralement dans le corpus. Le profil de
Wonder Woman comme « gardien vs producteur » est **reconstruit**
par comparaison avec Superman/Flash : Superman et Flash sont
producteurs de croissance et de produit, Wonder Woman et Aquaman
sont gardiens de cohérence (financière et légale). La phrase « un
datum, un owner » (ADR-MESH-L2-001) est citée textuellement.
