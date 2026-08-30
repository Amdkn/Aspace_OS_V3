---
type: Concept
title: Red flag #2 (Growth green, Sales red) — Superman arbitre et gèle le scaling
description: Le red flag #2 de la matrice d'harmonisation pose "valider l'offre avant de scaler l'attention". Superman Growth est le détecteur principal et le gélateur du scaling. Trois conditions de détection, trois issues (amendement mandat, gel, escalade B1), trois anti-pièges. La procédure est cumulative avec le contrat MQL-SQL : le gel du red flag #2 ne se lève pas tant que JohnJones n'émet pas SALES_READY.
tags: [superman, growth, sales, red-flag, harmonization, gel, scaling, escale]
generated: { by: minimax-m3, at: 2026-08-19T05:30:00Z }
verified:
  - { by: process:lecture-corpus-superman-vague-2, at: 2026-08-19T05:30:00Z }
sources:
  - id: red-flag-2-verbatim
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Red flag #2 verbatim — Growth green, Sales red
    last_modified: 2026-08-17
  - id: harmonization-exploitable
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — forme exploitable
    last_modified: 2026-08-19
  - id: avengers-wheel-signals
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — gates READY/BLOCKED par domaine
    last_modified: 2026-08-17
  - id: mql-sql-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/superman/superman-mql-sql-handoff-contract.md"
    title: Superman ↔ JohnJones contrat MQL-SQL — procédure de gel conjointe
    last_modified: 2026-08-19
  - id: council-arbitrage
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — quand escalader B1
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Red flag #2 (Growth green, Sales red) — Superman arbitre et gèle le scaling

## Le red flag verbatim

Matrice d'harmonisation `business-wheel-harmonization-matrix.md`
§« Les 5 red flags » :

> *« Growth green, Sales red : valider l'offre avant de scaler
> l'attention. »*

C'est le **seul red flag matrice qui impacte Superman directement**
sur les 5 red flags canoniques. Le red flag #1 vise Product (vs
Ops/IT), le red flag #3 vise Sales (vs Ops/People), le red flag #4
vise Finance (vs Growth/Product), le red flag #5 vise Legal (vs
public-facing work). Superman est cité **uniquement** dans le red
flag #2.

## Pourquoi Superman est le détecteur principal

Trois raisons structurelles :

### 1. Superman porte la croissance du signal

`eight-domain-avengers-wheel.md` ancre les trois états Superman :
`GROWTH_READY` (vert), `NEEDS_SIGNAL` (jaune), `BLOCKED_PROMISE`
(rouge). Superman **connaît** son propre état avant tout autre
capitaine. Si Superman est `GROWTH_READY` et que JohnJones est
`BLOCKED_COMMITMENT`, l'asymétrie est **immédiatement visible** du
côté Superman.

### 2. Le pair-check #1 (Growth → Sales) teste le franchissement

La matrice d'harmonisation pose le pair-check #1 *« l'attention
devient-elle opportunité qualifiée ? »*. Superman produit
l'attention ; JohnJones produit l'opportunité qualifiée. Si
Sales est red, l'attention ne franchit pas — le scaling
d'attention est une perte.

### 3. Superman est Consulted sur le pair-check #1

Le RACI par rang pose **Sales = Accountable, Growth = Consulted**.
Mais Superman n'est pas Responsible non plus — Superman est
l'**émetteur** du signal. Si l'émetteur ne détecte pas l'asymétrie,
personne ne la détecte (les Captains Sales et Production ne
surveillent pas la croissance d'attention en routine).

## Les trois conditions de détection

Le red flag #2 est **actif** quand les trois conditions sont
remplies cumulativement.

### Condition 1 — Superman en `GROWTH_READY`

Superman a publié son DoD amont (attention qualifiée, signal
stable, ICP signé ou supposé acquis). L'attention est prête à
scaler.

### Condition 2 — JohnJones en `BLOCKED_COMMITMENT`

`eight-domain-avengers-wheel.md` pose `BLOCKED_COMMITMENT` quand
Sales n'a pas validé d'offre tenable (pas d'ICP, pas de DoD SQL,
ou problème reformulé non-validé par client). C'est l'état **red**
canonique de Sales.

### Condition 3 — Le mandat B1 demande un scaling

Le mandat B1 (Summers) demande à Superman de scaler
l'attention — paid media, content amplification, outbound
programmatique. Sans mandat de scaling, Superman n'a rien à
geler.

## Les trois issues

Quand le red flag #2 est actif, Superman a trois issues possibles.

### Issue 1 — Amendement du mandat B1

**Procédure** : Superman remonte au B2 Council que le red flag #2
est actif. Le Council statue sur l'amendement : ajouter une
condition *« Sales doit être `SALES_READY` avant tout scaling »*.
Le mandat amendé est renvoyé à B1 pour signature.

**Cas d'usage** : mandat B1 *« scaler paid media US Q4 »* amendé
en *« scaler paid media US Q4 quand Sales émet `SALES_READY` »*.
B1 accepte l'amendement, mandate est exécuté en mode handoff.

### Issue 2 — Gel du scaling

**Procédure** : Superman consigne dans le journal Council
`red_flag: 2, source: sales_blocked_commitment, action:
geler_scaler_attention`. Superman **gèle** toute nouvelle
campagne de scaling. Les MQL existants continuent d'être
qualifiés au niveau baseline (paralle, pas handoff).

**Cas d'usage** : mandat B1 *« scaling immédiat Q4 »* non
amendé. Superman gèle sans escalader B1, parce que le gel est
l'application directe du canon matrice (pas une décision
discrétionnaire).

**Lever le gel** : Superman lève le gel **seulement** quand
JohnJones sort de `BLOCKED_COMMITMENT` et émet `SALES_READY`.
Le gel ne se lève pas par exception B1, par Superman seul, ou
par Summer's Verse datée.

### Issue 3 — Escalade B1

**Procédure** : Superman remonte au B2 Council que le red flag
#2 est actif **et** que B1 maintient le mandat de scaling
malgré l'amendement proposé. Le Council escalade B1 parce
que :

1. Le mandat B1 entre en conflit avec le canon matrice.
2. Le B2 ne peut pas amender un mandat B1 (cf.
   `b2-council-arbitrage-rule.md` §« Quand le Council escalade à B1 »).
3. Seul B1 peut ouvrir un cycle supplémentaire ou retirer le
   mandat.

**Cas d'usage** : mandat B1 *« scaling immédiat Q4, c'est
priorité absolue »* maintenu malgré amendement proposé. B2
escalade B1. B1 tranche entre pivot de cycle (renoncer au
scaling), réécriture du mandat (forcer Sales à monter en
Ready), ou dissolution du red flag #2 (ce qui est une
réécriture du canon — B1 ne le fait pas à la légère).

## Le format du packet mésoperpétuel — `decision: blocked`

Quand Superman gèle (Issue 2), le packet mésoperpétuel
ressemble à :

```yaml
meso_decision_id: B2-MESO-DECISION-YYYY-NN
source_mandate: B1-B2-MANDATE-YYYY-NN
mode: handoff
impacted_domains:
  - growth
  - sales
tradeoff: "Red flag #2 actif : Sales en BLOCKED_COMMITMENT, 
  scaling Growth gelé jusqu'à SALES_READY. MQL baseline continue."
decision: blocked
red_flag: 2
red_flag_source: sales_blocked_commitment
proof_expected:
  - B2 gate sales update (sales_ready_emit)
  - B2 gate growth update (scaling_unfrozen)
next_review: <date-or-SALES_READY-event>
```

Le packet est **append-only**. Le `decision: blocked` est un
état, pas une annulation — quand Sales émet `SALES_READY`, un
**nouveau** packet est créé avec `decision: accepted` qui pointe
sur le packet blocked.

## Le cas concret — pivot US Q4

Imaginons un mandat B1 *« pivoter US premium $7.5-25K ACV Q4 »*
(analogie au pivot US 2026-07-15 cité dans
`b2-meso-decision-packet-spec.md` §« Exemple »).

**État initial** : Superman Growth Ready (paid media US prêt,
ICP US supposé acquis). JohnJones Sales en `BLOCKED_COMMITMENT`
(parce qu'aucun ICP US n'a été co-signé, cf.
`superman-mql-sql-handoff-contract.md` §« Procédure de gel
conjointe »).

**Détection** : Superman consulte la matrice d'harmonisation
chaque semaine (cf. cadence canonique). Le red flag #2 est
actif.

**Issue 2 appliquée** : Superman consigne le gel. Le pivot US
Q4 **ne démarre pas** le scaling paid media. Les MQL baseline
continuent d'être qualifiés (paralle, pas handoff).

**Lever le gel** : JohnJones et Superman co-signent un ICP US
(un `mql_contract_id` avec démographie US uniquement), JohnJones
émet `SALES_READY`. Superman lève le gel. Le scaling US
démarre.

**Coût du gel** : 2-4 semaines de scaling US non-démarré.
**Coût du scaling sans gel** : paid media brûlé sans output
SQL, campagne US sans ICP, capital Mark wasted. Le gel est
**moins coûteux** que l'absence de gel.

## La coordination avec le contrat MQL-SQL

Le red flag #2 et le contrat MQL-SQL (cf.
`superman-mql-sql-handoff-contract.md`) sont **cumulatifs** :

- Le contrat MQL-SQL pose le DoD partagé.
- Le red flag #2 pose la détection de l'asymétrie.
- Le gel du red flag #2 ne se lève **que** par `SALES_READY`,
  qui peut impliquer un nouveau contrat MQL-SQL ou un amendement.

Concrètement : un red flag #2 levé peut produire un
**nouveau** `mql_contract_id` (par exemple, ICP US co-signé).
Le packet mésoperpétuel de levée de gel pointe sur le nouveau
contrat.

## Les trois anti-pièges

### Anti-pièce 1 — Scaling par exception B1

Un captain Superman qui lève le gel par exception B1 casse la
doctrine. Le gel est l'application directe du canon matrice —
il ne se lève pas par exception. Seul le retour de Sales à
Ready tranche. Summers lui-même ne peut pas forcer le scaling
sans escalader B2 Council pour réécriture du red flag #2 (ce
qui est une décision B2, pas B1 — B1 n'est pas habilité à
réécrire la matrice).

### Anti-pièce 2 — Gel déclaré sans les trois conditions

Un gel sans les trois conditions cumulatives (Superman Ready,
Sales Blocked, mandat de scaling) est un gel **non-étayé**.
Le captain sponsor doit refuser le gel ou exiger les
conditions. Sans les trois conditions, le gel est un acte
discrétionnaire qui peut masquer un veto Superman abusif (cf.
`veto-catalogue-concrete.md` §« Pourquoi le veto Superman est le
plus difficile à opérationnaliser »).

### Anti-pièce 3 — Gel permanent par absence de Sales

Si JohnJones reste en `BLOCKED_COMMITMENT` pendant > 1 cycle
12WY, le gel du red flag #2 devient une **dormance croisée**.
C'est un signal d'escalade B1 : Summers doit arbitrer entre
pivoter Sales (réécrire l'offre) ou pivoter Growth (changer
le scope). Le gel ne peut pas rester permanent par défaut
Sales.

## Liens

- [[business-wheel-harmonization-matrix]] — red flag #2 verbatim
- [[b2-harmonization-matrix-exploitable]] — la matrice d'harmonisation
- [[eight-domain-avengers-wheel]] — gates Sales `BLOCKED_COMMITMENT`
- [[superman-mql-sql-handoff-contract]] — le contrat MQL-SQL
- [[b2-council-arbitrage-rule]] — quand escalader B1
- [[b2-meso-decision-packet-spec]] — le format packet mésoperpétuel

## Note de confiance

**Confirmé par machine pour le red flag et les 3 conditions ;
reconstruit pour la procédure.** Le red flag #2 verbatim est cité
depuis `business-wheel-harmonization-matrix.md`. Les 3 états
Superman (`GROWTH_READY`/`NEEDS_SIGNAL`/`BLOCKED_PROMISE`) sont
tirés verbatim de `eight-domain-avengers-wheel.md`. Les 3 issues
(amendement, gel, escalade B1) sont **reconstruites** à partir
de la matrice d'harmonisation + `b2-council-arbitrage-rule.md`
§« Quand le Council escalade à B1 » + `b2-meso-decision-packet-spec.md`.
Le format YAML du packet est **projeté** à partir du format
canonique mésoperpétuel (D4 append-only). Le cas concret du pivot
US Q4 est **analogie** au pivot US 2026-07-15 cité dans le packet
spec — pas un cas réel observé. L'anti-pièce 3 (dormance croisée)
est **projetée** par lecture critique de `b2-areas-dormants-doctrine.md`
appliquée à un blocage persistant.