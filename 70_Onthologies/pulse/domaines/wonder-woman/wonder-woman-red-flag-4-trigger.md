---
type: Concept
title: Red flag #4 — Finance red + Growth/Product green : qui déclenche, comment ça se résout
description: Le red flag #4 de la matrice d'harmonisation (« Finance red + Growth/Product green — Ralentir ou re-pricer. Le cash ne suit pas. ») est l'arrêt dur qui protège contre les lancements solvables seulement sur le papier. Wonder Woman est la capitaine qui déclenche le red flag (Finance = son domaine). La résolution se joue entre 3 issues : (1) re-pricing (sortie par le haut, augmentant le prix), (2) ralentissement (sortie par le bas, ralentissant la cadence spend/growth), (3) escalade B1 (si la wheel 8-domain ne tient plus). Le red flag ne se confond pas avec le veto catalogue Finance — granularité différente (transverse vs unaire dépense).
tags: [b2, finance, red-flag, harmonization, matrix, gate, cashflow, runway, re-pricing, ralentissement]
generated: { by: minimax-m3, at: 2026-08-19T03:48:00Z }
verified:
  - { by: process:lecture-domaine-finance-corpus, at: 2026-08-19T03:48:00Z }
sources:
  - id: harmonization-matrix
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — forme exploitable
    last_modified: 2026-08-19
  - id: harmonization-source
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation de la wheel — pair checks et red flags
    last_modified: 2026-08-17
  - id: council-rule
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-arbitrage-rule.md"
    title: B2 Council — qui tranche quand deux domaines se contredisent
    last_modified: 2026-08-19
  - id: meso-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — le format canonique d'une décision B2
    last_modified: 2026-08-19
  - id: finance-principles
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/06_Finance_WonderWoman_Thunderbolts/03_WONDERWOMAN_FINANCE_PRINCIPLES.md"
    title: Wonder Woman Finance Principles (v4)
    last_modified: 2026-06-25
  - id: omk-control-room
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/06_Finance_WonderWoman_Thunderbolts/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: OMK Finance — B2 Domain Control Room
    last_modified: 2026-05-25
okf_version: "0.2"
---

# Red flag #4 — Finance red + Growth/Product green : qui déclenche, comment ça se résout

## Citation verbatim

Le red flag #4 est posé verbatim dans
`b2-harmonization-matrix-exploitable.md` §« Les 5 red flags — arrêts
durs » (et dans la matrice source
`business-wheel-harmonization-matrix.md`) :

> « **Finance red + Growth/Product green** : Ralentir ou re-pricer.
> Le cash ne suit pas. »

C'est un **arrêt dur** : un red flag suffit à bloquer un
lancement, même si les 8 domaines sont au vert sur le radar
(`b2-harmonization-matrix-exploitable.md` §« Pourquoi cette matrice
n'est pas lue comme un radar »).

## Qui déclenche

Le déclencheur du red flag est **toute information** qui
positionne Finance dans un état « red » pendant que Growth ou
Product (ou les deux) sont « green ». Trois déclencheurs typiques :

1. **Runway <12 mois** alors que Growth scale la paid media et
   que Product lance une feature payante.
2. **Margin nette <25%** alors que Growth continue à promettre des
   unit economics positives et que Product annonce une roadmap
   ambitieuse.
3. **Cash burn mensuel en hausse >15%** sur 3 mois consécutifs
   (toujours pendant que Growth/Product sont green).

Dans les trois cas, **Wonder Woman** (capitaine Finance) déclare
le red flag au Council, idéalement **avant** le lancement pour
que la wheel 8-domaines reste cohérente. Concrètement, le
déclencheur est posé par Wonder Woman **ou** par n'importe quel
B2 captain qui détecte l'asymétrie (le Council B2 est
transversal sur les red flags).

## Quand le red flag se déclenche — 3 scénarios concrets

### Scénario 1 — Lancement d'une offre premium à runway tendu

- **État** : Growth green (paid media performant, MRR +12% MoM),
  Product green (feature ship à l'heure, NPS > 40). Finance red :
  runway à 8 mois, marge nette à 22% (sous le seuil F4).
- **Déclencheur** : Wonder Woman détecte que la MRR增长的
  consumed cashflow pour atteindre 8 mois. Sans
  ralentissement, le runway tombera à 5 mois dans 2 trimestres
  (sous le seuil KR-5g d'escalade).
- **Red flag** : posé en Council hebdomadaire.

### Scénario 2 — Pivot US premium sans repriser

- **État** : Product green (offre US lancée, premiers deals
  signés). Growth green (attention US en hausse). Finance red :
  le pivot exige une dépense cloud supplémentaire (Vercel +
  Supabase US region) qui n'a pas de métrique de retour
  chiffrée dans le packet mésoperpétuel.
- **Déclencheur** : Wonder Woman oppose son veto catalogue
  (cf. [[wonder-woman-recurrent-spend-veto]]) ET lève le red
  flag #4 simultanément.
- **Résolution** : voir « trois issues » ci-dessous.

### Scénario 3 — Rebond de croissance caché sous un margin squeeze

- **État** : Growth green (rebond MQL +30% QoQ). Product green
  (rétention D30 en hausse). Finance red : la marge brute a
  chuté de 60% à 45% sans que les KRs Growth/Product ne le
  reflètent (probablement à cause d'un mix d'offres bas de
  gamme).
- **Déclencheur** : la réconciliation mensuelle SOP-L2-FINANCE-002
  révèle l'écart. Wonder Woman pose le red flag.

## Les trois issues — comment ça se résout

`business-wheel-harmonization-matrix.md` pose la règle de
résolution (`b2-harmonization-matrix-exploitable.md` §« La règle de
résolution — ce qui tranche quand deux domaines se contredisent »)
:

```
si 1 red flag touché :
    arrêt dur, B2 Council convoqué
```

Pour le red flag #4, **trois issues** sont possibles (par ordre
de fréquence) :

### Issue 1 — Re-pricing (sortie par le haut)

Wonder Woman propose une **augmentation ciblée du pricing** sur
les segments solvables (clients premium, ACV > seuil). C'est la
résolution préférée quand :

- La marge brute fond à cause d'un mix d'offres bas de gamme.
- Le pricing strategist Wonder Woman peut défendre une
  augmentation sans perdre les deals en cours.
- Le re-pricing est rapide (pas de re-engineering de
  l'offre).

**Conséquence opérationnelle** : packet mésoperpétuel avec
`decision: accepted`, mode `negotiation`, impacted_domains
incluant Sales (qui gère les renégociations clients). Preuve
attendue : nouvelle grille tarifaire + forecast margin post-re-pricing.

### Issue 2 — Ralentissement (sortie par le bas)

Wonder Woman propose un **ralentissement des dépenses payantes**
(paid media, recrutement, etc.) et une **réduction du scope de
lancement** (product lance en beta fermé, pas en GA). C'est la
résolution préférée quand :

- Le runway est structurellement bas (pas un effet de mix).
- Le re-pricing est lent à mettre en place (clients en
  contrats pluriannuels).
- La saisonnalité permet un slowing sans casse stratégique.

**Conséquence opérationnelle** : packet mésoperpétuel avec
`decision: accepted`, mode `negotiation`, impacted_domains
incluant Growth (qui suspend les dépenses) et Product (qui
restreint la sortie). Preuve attendue : forecast runway
post-ralentissement ≥12 mois.

### Issue 3 — Escalade B1 (sortie par le haut Conseil)

Si **les deux issues précédentes sont bloquées** (re-pricing
impossible par contrat, ralentissement impossible par engagement
public), le Council **escalade B1** avec un packet mésoperpétuel
`decision: escalate_to_B1`. B1 arbitre en acceptant de réécrire
la North Star ou en ré-ouvrant le cycle 12WY.

Concrètement, Wonder Woman pose le packet et Superman + Flash
notent leur désaccord. B1 choisit entre :

- **Pivot** (changer de marché ou de positionnement).
- **Réinjection de capital** (lever des fonds, ce qui n'est
  pas dans North Star si le bootstrap est la doctrine).
- **Réduction de cycle** (livrer moins cette année).

## Pourquoi le red flag #4 n'est pas le veto catalogue Finance

`b2-harmonization-matrix-exploitable.md` §« Les 5 red flags »
distingue les red flags (arrêts durs transverses) des vetos
catalogue (blocages unaires par classe). Le red flag #4 et le
veto catalogue Finance (cf.
[[wonder-woman-recurrent-spend-veto]]) ont **trois différences
majeures** :

| Critère | Red flag #4 | Veto catalogue Finance |
|---|---|---|
| Granularité | Transverse (Growth + Product + Finance) | Unaire (une dépense récurrente) |
| Déclencheur | État « Finance red » agrégé | Dépense spécifique sans forme (date + métrique) |
| Résolution | B2 Council, 3 issues | Captain Finance seul (mandat amendé/retiré) |
| RACI | A = Council, C = tous les impacted | A = Wonder Woman |
| Conséquence | Arrêt dur jusqu'à résolution | Blocage jusqu'à amendement |

Les deux peuvent se déclencher simultanément (scénario 2
ci-dessus). Le veto catalogue est **plus rapide à traiter**, le
red flag est **plus structurel**. Un audit qui confond les deux
manque un niveau de granularité.

## Le rôle exact de Wonder Woman

Wonder Woman n'est **pas Accountable** dans le RACI des pair-checks
#5 et #6 — elle est Consulted. Mais :

- Sur le red flag #4, elle est **déclencheur** (c'est son
  domaine qui passe en red).
- Elle propose **la résolution** (re-pricing ou ralentissement).
- Elle **arbitre** la cohérence avec les principes F1-F12
  (runway floor, margin floor).

Concrètement, le RACI du red flag #4 (par extension de la
matrice canonique) :

- A = B2 Finance (Wonder Woman) sur le déclencheur et la
  proposition de résolution
- C = B2 Growth (Superman) et B2 Product (Flash)
- I = B1, autres B2 captains

C'est l'**exception** à la règle RACI par rang — Wonder Woman
passe de C (pair-checks #5 et #6) à A (red flag #4) parce que la
**décision vient de son domaine**.

## Le format du packet mésoperpétuel

Un red flag #4 posé produit typiquement :

```yaml
meso_decision_id: B2-MESO-DECISION-YYYY-NN
source_mandate: B1-B2-MANDATE-YYYY-NN  # ou B2-PEER-YYYY-NN
mode: negotiation
impacted_domains:
  - growth
  - product
  - finance
tradeoff: |
  Runway à X mois, marge nette à Y%, pendant que Growth et Product
  sont green. Cashflow ne suit pas. Choix : re-pricing,
  ralentissement, ou escalade B1.
decision: accepted  # ou escalate_to_B1
proof_expected:
  - B2 gate finance update (runway_cible_rétabli)
  - B2 gate growth update (dépenses_re_qualifiées)
  - B2 gate product update (scope_lancement_réduit)  # si issue 2
  - B3 proof path (Finance_Thunderbolts_forecast_runway_12mo)
next_review: 2026-MM-DD  # ou 12WY-2026-QX
```

Le packet est conforme au gabarit
`b2-meso-decision-packet-spec.md`.

## Anti-pièges

- **Confondre green/Finance red avec une périodicité météo**.
  Le red flag n'est pas un ralentissement saisonnier — c'est un
  état structurel qui exige une décision, pas une attente.
- **Re-pricing comme issue par défaut**. Le re-pricing est
  l'issue **préférée** quand le mix d'offres est en cause.
  Ralentissement et escalade B1 sont les autres issues. Choisir
  re-pricing par défaut masque les cas où le re-pricing est
  contractuellement bloqué.
- **Escalade B1 tardive**. Si Wonder Woman détecte le red flag
  mais attend 2-3 cycles avant de poser le packet mésoperpétuel,
  l'escalade B1 arrive en urgence avec un runway à 4 mois. Le
  red flag doit être posé **au moment de la détection**, pas
  quand la situation devient intenable.
- **Radar Finance au vert trompeur**. Le radar 8-domaines peut
  afficher Finance green (par exemple sur la MRR) pendant que
  le runway est rouge. Le red flag teste **l'état financier
  agrégé**, pas la MRR isolée. Wonder Woman doit déclarer le
  red flag sur runway/marge, pas attendre que la MRR chute.

## Liens

- [[wonder-woman-recurrent-spend-veto]] — le veto catalogue
  complémentaire
- [[wonder-woman-finance-frontiers]] — le périmètre Finance
- [[wonder-woman-pair-check-consulted-role]] — l'asymétrie C vs A
- [[b2-harmonization-matrix-exploitable]] — la matrice canonique
- [[b2-council-arbitrage-rule]] — qui tient le Council

## Note de confiance

**Confirmé par machine.** Le red flag #4 est cité verbatim de la
matrice d'harmonisation (deux sources concordantes). Les 3 issues
sont **projetées** depuis la doctrine Finance (F4 margin, F1
runway, F13 deux-horizons, F25 Wright's law) et le gabarit packet
mésoperpétuel. Le RACI « A = Finance sur red flag #4 » est
**extrapolé** par symétrie : puisque le déclencheur vient du
domaine Finance, A bascule. À vérifier en cycle réel : est-ce
que le Council accepte cette bascule A, ou est-ce que l'A
reste au B2 sponsor Growth/Product même quand c'est Finance qui
déclenche ?
