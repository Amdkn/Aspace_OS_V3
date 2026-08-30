---
type: Concept
title: Dormance procedure — la 6ᵉ dimension à côté de la dormance domaine B2
description: La doctrine `b2-areas-dormants-doctrine` couvre la dormance d'un capitaine B2 (Batman SHADOW_ACTIVE vs ACTIVE). Elle ne dit rien sur la dormance d'une *procedure* au sein d'un domaine ACTIVE. Batman propose de distinguer explicitement les deux : un domaine ACTIVE peut avoir 0 procedure ACTIVE (si toutes sont en pilote), ou 1+ procedure dormante (procédure conçue mais jamais déclenchée). La distinction évite qu'une absence de cycle ne soit confondue avec un défaut de couverture.
tags: [b2, ops, batman, dormance, procedure, 6e-dimension, doctrine-extension]
generated: { by: minimax-m3, at: 2026-08-19T05:55:00Z }
verified:
  - { by: process:lecture-canon-b2-tour-4, at: 2026-08-19T05:55:00Z }
sources:
  - id: b2-areas-dormants
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-areas-dormants-doctrine.md"
    title: B2 Areas Dormants Doctrine — état dormant vs SHADOW_ACTIVE vs ACTIVE
    last_modified: 2026-08-19
  - id: batman-cycle-5-phases
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-cycle-vie-procedure-ops-cinq-phases.md"
    title: Cycle de vie procedure Ops en 5 phases
    last_modified: 2026-08-19
  - id: batman-launch-ready
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-launch-ready-portique-final-transverse.md"
    title: LAUNCH_READY — portique final transverse
    last_modified: 2026-08-19
  - id: triplets-v3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: Triplets V3 — domaines B2 et gates
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Dormance procedure — la 6ᵉ dimension à côté de la dormance domaine B2

## Le trou que Batman voit

`b2-areas-dormants-doctrine` pose trois états pour un **capitaine B2** :
`DORMANT` (capitaine non nommé), `SHADOW_ACTIVE` (nommé mais sans
packets mésoperpétuels émis), `ACTIF` (au moins 1 packet mésoperpétuel
émis). La doctrine est par **domaine**, pas par **procedure**.

Conséquence : un domain BATMAN ACTIF pourrait, en théorie, n'avoir
**aucune procedure ACTIVE** — toutes à l'état `pilote` ou `dormante`.
Le radar 8-domain affichera Batman vert, mais le portfolio procedure
Ops est vide. C'est le scenario que `batman-launch-ready-portique-final-transverse`
décrit : `LAUNCH_READY` rouge parce que la procedure Ops n'a pas
d'historique d'exécution, même si Batman est au vert.

## Les 6 dimensions

| Dimension | Valeur | Source canon |
|---|---|---|
| 1. Capitaine nommé | oui / non | `b2-areas-dormants-doctrine` |
| 2. Squad B3 affectée | oui / non | `ORG.json` |
| 3. Packet mésoperpétuel émis (≥1) | oui / non | `B2_DC_DIRECTION_COUNCIL_DECISIONS.md` |
| 4. Procedure active (≥1 en production) | oui / non | `batman-cycle-vie-procedure-ops-cinq-phases` |
| 5. Procedure en pilote (≥1 en phase 2) | oui / non | idem |
| 6. Procedure conçue (≥1, jamais déclenchée) | oui / non | idem |

Les **dimensions 1-3** sont la doctrine dormance domaine B2 existante.
Les **dimensions 4-6** sont la **dormance procedure** que Batman
propose d'ajouter. La distinction est utile parce qu'elle a des
conséquences operationnelles differentes.

## Pourquoi la dormance procedure n'est pas la dormance domaine

Batman ACTIF + 0 procedure ACTIVE = **domaine prêt, mais sans actif
operationnel**. C'est typiquement le cas d'un domaine qui vient de
finir un cycle de build sans avoir déclenché de run. La wheel affiche
Batman vert, mais le portfolio procedure est vide. Le portique
`LAUNCH_READY` rouge n'est pas un bug — il reflète la dimension 4.

Batman ACTIF + 0 procedure ACTIVE + 1+ procedure dormante = **domaine
pret avec procedure conçue mais non déclenchée**. Cas typique : une
procedure de rollback a été conçue en phase 1, n'a jamais été
déclenchée parce que la feature correspondante n'a pas regressé.
La procedure est **disponible**, pas **rodée**.

## Les trois transitions dormance procedure

```
procedure conçue (DORMANT-PROC)
   ↓ B2 captain autorise passage phase 2 pilote
procedure en pilote (PILOT-PROC)
   ↓ sprint execute, DoD chiffré tenu
procedure ACTIVE (ACTIVE-PROC)
   ↓ incident conécutif sans précédent OU cycle sunset
procedure sunset (SUNSET-PROC)
```

Pas de transition `ACTIVE-PROC → DORMANT-PROC`. Une procedure qui
n'est plus ACTIVE passe en `SUNSET-PROC`, pas en dormant. La raison
est dans `batman-cycle-vie-procedure-ops-cinq-phases.md` §« Phase 5
arrêt » : une procedure arrêtée ne revient pas sans un nouveau cycle
de conception.

## Les couplages implicites

- **Vs People (Green Lantern)** : le coupleur People×Ops sur `owner-absent`
  (cf. `batman-couplage-people-green-lantern-owner-absent.md`) détecte
  quand la dimension 4 chute à zéro par manque de captain. C'est le
  seul cas où dormance procedure et dormance domaine se touchent.
- **Vs Aquaman (Legal)** : la triple signature `Aquaman+Batman+Thena`
  (cf. Aquaman tour 3) impose qu'une procedure dormant qui touche une
  frontière IP reste soumise à defensibilite juridique même sans
  exécution. Le portique `LAUNCH_READY` vérifie la defensibilite, pas
  l'exécution.
- **Vs Flash (Product)** : la decomposition DoD build/run/sunset (cf.
  Flash tour 3) donne 3 stades côté B3. La dormance procedure donne 3
  états côté B2. Les deux modèles sont orthogonaux — Batman×Flash
  traitent le même objet (procedure) à deux niveaux differents.

## Pourquoi cette 6ᵉ dimension importe pour le veto

Le veto Batman « procedure-sans-condition-arret » porte sur la **forme**
de la procedure, pas sur son **état d'exécution**. Une procedure dormante
peut rester sans condition d'arrêt — c'est même son défaut de départ,
et le veto ne s'oppose pas à sa conception. Le veto s'oppose à la
**transition DORMANT-PROC → ACTIVE-PROC** sans condition d'arrêt.

C'est une clarification qui change le rayon d'application : le veto
ne bloque pas la conception, il bloque la mise en production. Sans
cette clarification, une procedure dormante sans condition d'arrêt
serait en infraction permanente — un faux positif qui rend le veto
inoperant.

## Anti-pièges

- **Confondre dormance procedure et dormance capitaine.** Les 6
  dimensions sont indépendantes. Un capitaine DORMANT peut avoir
  une procedure DORMANT-PROC documentée (legacy) — la dimension 1
  ne détermine pas la dimension 6.
- **Compter 0 procedure ACTIVE comme Batman rouge.** Batman rouge =
  capitaine DORMANT/SHADOW_ACTIVE (dimensions 1-3). Batman jaune =
  procédure dormante (dimension 4-6). Radar wheel 8-domain confond
  les deux — c'est precisely ce que la matrice d'harmonisation
  corrige.
- **Revenir en DORMANT-PROC après un sunset.** Une procedure sunset
  est morte. La ressusciter exige un nouveau cycle de conception, pas
  unflip d'état.

## Liens

- [[b2-areas-dormants-doctrine]] — la doctrine source (dimensions 1-3)
- [[batman-cycle-vie-procedure-ops-cinq-phases]] — les 5 phases qui produisent les transitions
- [[batman-launch-ready-portique-final-transverse]] — la vérification de la dimension 4
- [[b2-council-arbitrage-rule]] — qui arbitre un portique rouge sur dimensions 4-6

## Note de confiance

**Reconstruit, à moitié étayé.** Les 6 dimensions sont projetées à
partir de 3 sources distinctes (doctrine dormance, cycle 5 phases,
portique LAUNCH_READY) — la doctrine canonique ne pose pas
explicitement la distinction dormance domaine vs dormance procedure.
L'argument que le veto porte sur la transition DORMANT-PROC → ACTIVE-PROC
est cohérent avec `batman-veto-condition-arret-procedure.md` mais
n'est pas cité comme un bloc canonique. La triple transition
DORMANT-PILOT-ACTIVE-SUNSET est alignée sur
`batman-cycle-vie-procedure-ops-cinq-phases.md` §« Phase 5 arrêt » et
projetée symétriquement.
