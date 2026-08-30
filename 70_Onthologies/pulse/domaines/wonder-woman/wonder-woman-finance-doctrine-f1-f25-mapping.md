---
type: Concept
title: Doctrine Finance F1-F25 — projection des 25 principes sur les outils canoniques
description: Les 25 principes Finance (F1-F12 floor survie, F13-F18 ceiling Empire/Kardashev, F19-F22 trésorerie, F23-F25 AI-Agency economics) sont abstraits sans projection sur les outils B2 (veto catalogue, blocking authority, build gates, red flags). Cette cartographie montre quels principes déclenchent quel outil, et identifie 4 principes qui n'ont aucun outil canonique — ils restent à l'état de doctrine sans garde-fou opérationnel.
tags: [b2, finance, doctrine, principles, f1-f25, kardashev, treasury, ai-agency, mapping, tools, wonder-woman]
generated: { by: minimax-m3, at: 2026-08-19T04:30:00Z }
verified:
  - { by: process:lecture-domaine-finance-corpus, at: 2026-08-19T04:30:00Z }
sources:
  - id: spock-finance-principles
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/02_Areas_Spock/J01_Jerry_Prime_LD01_Business/B2_Area_Domains/06_Finance_WonderWoman_Thunderbolts/03_WONDERWOMAN_FINANCE_PRINCIPLES.md"
    title: "Wonder Woman Finance Principles (v4) — 25 principes F1-F25"
    last_modified: 2026-06-25
  - id: vetos-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — un par capitaine
    last_modified: 2026-08-19
  - id: omk-control-room
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/01_Projects_Picard/01-omk-business-os/B2_Business_Domains/06_Finance_WonderWoman_Thunderbolts/00_B2_DOMAIN_CONTROL_ROOM.md"
    title: OMK Finance — B2 Domain Control Room
    last_modified: 2026-05-25
  - id: harmonization-matrix
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — 9 pair-checks + 5 red flags
    last_modified: 2026-08-19
  - id: marvel-mesh-anchoring
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-marvel-mesh-anchoring.md"
    title: B2 Marvel Mesh — anchoring des squads sur les domaines
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Doctrine Finance F1-F25 — projection des 25 principes sur les outils canoniques

## Pourquoi une cartographie est nécessaire

La doctrine Finance (`03_WONDERWOMAN_FINANCE_PRINCIPLES.md`, v4,
status `CANONICAL_FROM_CANON`, 2026-06-25) pose **25 principes** —
F1 à F12 sur la survie, F13-F18 sur le ceiling Empire/Kardashev,
F19-F22 sur la trésorerie/leverage/roll-up, F23-F25 sur l'AI-Agency
economics. Ces principes sont la doctrine pérenne (Areas Spock).

**Le trou** : la doctrine est abstraite. Elle ne dit pas *quel
principe déclenche quel outil B2*. Un B3 Thunderbolts qui voit
qu'un client atteint le seuil F2 (« forecast pessimistically »)
ne sait pas s'il doit ouvrir un packet mésoperpétuel, escalader,
ou attendre le prochain KR hebdo.

Cette cartographie projette les 25 principes sur **4 outils
canoniques** :

1. **Veto catalogue Finance** — le veto unaire sur les dépenses
   récurrentes sans date + métrique (cf.
   [[wonder-woman-recurrent-spend-veto]]).
2. **Blocking authority sur marge négative** — le droit de bloquer
   Product indépendamment du pair-check #6 (cf.
   `00_B2_DOMAIN_CONTROL_ROOM.md` §« Blocking Authority »).
3. **Build gate « Paid Release Gate Check »** — les 4 conditions
   à valider pour toute release payante (cf.
   [[wonder-woman-paid-release-gate-finance]]).
4. **Red flag #4** — l'arrêt dur quand Finance red + Growth/Product
   green (cf. [[wonder-woman-red-flag-4-trigger]]).

## Cartographie F1-F12 (floor survie) — Bucky/Yelena/Ghost/Red Guardian/Taskmaster/U.S. Agent

| # | Principe | Outil canonique | Trigger concret |
|---|---|---|---|
| **F1** | Runway is the survival metric | Red flag #4 (escalade KR-5g) | Runway <12 mois, escalade Jerry à <6 mois |
| **F2** | Forecast pessimistically | Build gate (étape 1) | Forecast sans scenario pessimiste → rejet gate |
| **F3** | MRR growth discipline >10% MoM | KR-5d hebdo (Pulse) | MoM <10% sans explication rationnelle → packet Council |
| **F4** | Real net margin, never gross theatre | Blocking authority | Marge nette <25% Solaris → blocage Product |
| **F5** | Hunt the phantom costs | JTBD récurrent B3-FINANCE-Ghost-Phantom-Charges | Charge fantôme détectée → JTBD sweep |
| **F6** | CAC payback discipline | KR partagé (pair-check #5) | CAC payback > >12 mois → Superman tranche via pair-check #5 |
| **F7** | Transparent reporting; no hidden losses | Anti-pattern DLQ route | Capture/log manifestement arrangé → Donna/DLQ |
| **F8** | Readable dashboards | Build gate (étape 4 — billing path lisible) | Dashboard illisible Jerry → rejet gate |
| **F9** | Reproducible accounting processes | Anti-pattern silencieuse rework | Process non-reproductible → escalade discipline |
| **F10** | Tax compliance, on time | Exception au veto catalogue | Filing fiscal hors cycle → non-veto (compliance prioritaire) |
| **F11** | Invoice velocity <48h « Ready to bill » | Lead indicator KR | <95% envoyées <48h → packet Council |
| **F12** | Reconciliation integrity 100% | Build gate + lead indicator | Réconciliation <100% → rejet gate + escalade |

**Lecture** : les 12 principes du floor sont **tous** projetables sur
au moins un outil canonique. F10 (tax compliance) est l'exception —
la doctrine l'exclut explicitement du veto catalogue (cf.
[[wonder-woman-recurrent-spend-veto]] §« Cas où le veto serait
ABUSIF »).

## Cartographie F13-F18 (ceiling Empire/Kardashev) — Jay-Z/Codie/YC/Money Radar

| # | Principe | Outil canonique | Trigger concret |
|---|---|---|---|
| **F13** | Two-horizon accounting | Extension CEO Dashboard | Pas d'outil B2 canonique — la lecture simultanée floor+ceiling est doctrine pérenne, pas garde-fou |
| **F14** | Ownership over income | (F14 — F1) — projection sur F1 runway | Le revenu n'est pas une métrique — l'asset base oui. Pas d'outil distinct |
| **F15** | Value per agent, not per employee | KR dérivé Pulse (extension F4) | Marge/agent vs marge/employee — pas d'outil canonique, projection par F4 |
| **F16** | Create/orchestrate markets | Pas d'outil canonique — doctrine stratégique B1 | Le choix de marché est North Star, pas arbitrage B2 |
| **F17** | Ride the great wealth transfer | Pas d'outil canonique — macro-positionnement | Macro allocation → F19-F22 trésorerie |
| **F18** | Earn the slogan (anti-PNL) | Red flag #4 (extension F18) | Claim ambitieux sans métrique chiffrée → équivalent red flag #4 sur la cohérence North Star |

**Lecture** : les 6 principes du ceiling sont **en majorité sans
outil canonique**. F13, F16, F17 sont des doctrines B1 (North Star),
pas des garde-fous B2. F14, F15, F18 se projettent sur les outils
F1-F12 du floor — pas d'outil additionnel. **C'est cohérent avec
la doctrine F1-F12 vs F13-F18** : le floor a des garde-fous, le
ceiling a une vision.

## Cartographie F19-F22 (trésorerie/leverage/roll-up) — Finary/Codie/YC

| # | Principe | Outil canonique | Trigger concret |
|---|---|---|---|
| **F19** | Treasury allocation by the investment pyramid | Pas d'outil canonique B2 — déclenche Jerry | Surplus >12 mois runway → escalate à Jerry (cf. `AREA_STANDARD` reinvestment rules) |
| **F20** | Climb the Leverage Ladder; own assets | Pas d'outil canonique — doctrine stratégique | Ownership d'asset vs billed hours — pas de garde-fou |
| **F21** | Roll-up consolidation | Pas d'outil canonique — doctrine stratégique B1 | Choix d'acquisition fragmented industry → B1 North Star |
| **F22** | Heavy-asset moat over thin wrappers | Couplage F22-IT P13 (veto Cyborg §07) | Wrapper SaaS sans chemin de sortie → Cyborg veto + Wonder Woman marge compression |

**Lecture** : F19-F22 sont des doctrines d'allocation stratégique.
**Aucun n'a d'outil B2 canonique dédié**. F22 est le seul qui
s'articule avec un veto pair (Cyborg veto §07 « fournisseur
cloud-only sans chemin de sortie »). Les trois autres passent
par Jerry en escalation, pas par un garde-fou automatique.

## Cartographie F23-F25 (AI-Agency economics) — Luuk Alleman blueprint

| # | Principe | Outil canonique | Trigger concret |
|---|---|---|---|
| **F23** | Price the value, sell setup + retainer | Anti-pattern « Discounter sans approval » (Illuminati cross) | Discount >15% → Wonder Woman sign-off obligatoire (cf. `03_WONDERWOMAN_FINANCE_PRINCIPLES.md` §« Wonder Woman B2 ownership ») |
| **F24** | Sovereign-infra arbitrage drives net margin toward 90%+ | Couplage F24-IT P13 (Cyborg veto) | Vendor SaaS tiers détecté → Cyborg veto + Wonder Woman demande migration |
| **F25** | Plan on the Wright's-law tailwind | Pas d'outil canonique — modèle économique | Inference cost halving → réinvestissement pricing, pas de garde-fou B2 |

**Lecture** : F23 se projette sur le mécanisme de ** discount
>15% sign-off** (anti-pattern partagé avec Sales/Illuminati). F24
se couple avec le veto Cyborg §07. F25 reste doctrinal — la
déflation Wright's-law est un modèle de prévision, pas un
déclencheur de garde-fou.

## Les 4 principes sans outil canonique — un risque opérationnel

Quatre principes sont posés doctrinally mais **n'ont aucun outil
canonique** pour les opérationnaliser :

1. **F16** (create/orchestrate trillion markets) — North Star, pas
   garde-fou. Cohérent : c'est une décision B1, pas B2.
2. **F17** (ride the great wealth transfer) — macro-positionnement,
   projection F19-F22. Cohérent.
3. **F19** (treasury allocation pyramid) — escalade Jerry, pas
   garde-fou B2. **Incohérence partielle** : la trésorerie peut
   dégrader la solvabilité court terme (ex : immobilier illiquide
   vs runway 6 mois). Aucun veto Finance ne déclenche sur ce cas.
4. **F20** (Leverage Ladder) — pas de garde-fou. Cohérent : c'est
   une doctrine de croissance.

**Point d'attention** : F19 peut mener à des allocations de trésorerie
qui dégradent le floor F1 (runway). Wonder Woman n'a pas d'outil
pour bloquer une allocation F19 imprudente — elle ne peut qu'escalader
Jerry. Le Council B2 ne voit pas le dossier tant que le runway n'est
pas franchi. **C'est un trou de garde-fou** que la doctrine ne
couvre pas explicitement.

## Anti-pièges de la cartographie

- **Principe sans outil ≠ principe mort.** F16 et F17 sont des
  doctrines B1, pas des lacunes B2. Les principes sans outil
  canonique sont des doctrines de vision, pas des oublis.
- **Outil sans principe ≠ outil orphelin.** Le veto catalogue
  Finance est un outil unaire qui couvre une classe de dépenses
  (récurrentes sans forme). Le principe sous-jacent implicite est
  « la transparence des engagements récurrents ». Pas de F-numéro
  nommé, mais cohérent avec F7 (transparent reporting).
- **Confondre cartographie et amplifications.** L'amplification
  candidate « date ou horizon mesurable » (cf. triplet 58 « Wonder
  Woman etend ») **étend** le veto catalogue — elle ne projette pas
  un nouveau principe sur un outil. C'est une évolution de
  l'outil, pas une nouvelle cartographie.
- **Dormance vs cartographie.** Aquaman (Legal) est dormant tant
  qu'aucun contrat n'est signé (triplet 35-36). Wonder Woman n'est
  **pas** dormant — sa doctrine F1-F25 a des outils actifs sur
  presque tous les cycles. La différence entre un capitaine dormant
  et un capitaine actif n'est pas le nombre de principes mais
  l'existence de signaux entrants.

## Liens

- [[wonder-woman-recurrent-spend-veto]] — l'outil veto catalogue
- [[wonder-woman-red-flag-4-trigger]] — l'outil red flag #4
- [[wonder-woman-paid-release-gate-finance]] — l'outil build gate
- [[wonder-woman-finance-frontiers]] — le périmètre Finance
- [[wonder-woman-pair-check-consulted-role]] — le statut C
- [[b2-eight-domain-vetoes-catalogue]] — la théorie des vetos

## Note de confiance

**Confirmé par machine** sur les 25 principes (lus verbatim de la
doctrine F1-F25). **Reconstruit** sur la projection outils :
chaque ligne du tableau est une inférence depuis la doctrine F +
les 4 outils canoniques + les pair-checks RACI. La liste des
« 4 principes sans outil canonique » est une **projection** — le
canon n'établit pas explicitement la liste des principes qui
n'ont pas de garde-fou.