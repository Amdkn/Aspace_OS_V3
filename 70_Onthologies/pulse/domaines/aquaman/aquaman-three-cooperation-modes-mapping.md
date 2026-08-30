---
type: Concept
title: Aquaman — mapping des 3 modes de coopération sur les 4 formes émises
description: [[b2-three-cooperation-modes]] pose 3 modes canoniques (parallel / handoff / negotiation). Aucune projection Aquaman-spécifique n'a formalisé *quel mode s'applique* pour les 4 formes émises (privacy review / claim safety / contract template / defensibility doc) ni pour les 5 couplages indirects (couplages-invisibles). Ce concept pose la table Aquaman × mode canonique, identifie les 4 cas ambigus (Aquaman peut basculer entre deux modes), et propose un test de mode : le packet mésoperpétuel doit déclarer le mode initial ET le mode final, conformément à [[b2-three-cooperation-modes]] §Anti-pièges.
tags: [b2, aquaman, cooperation, modes, parallel, handoff, negotiation, mode-mapping, 4-formes]
generated: { by: minimax-m3, at: 2026-08-19T06:30:00Z }
verified:
  - { by: process:lecture-b2-corpus-tour-5, at: 2026-08-19T06:30:00Z }
sources:
  - id: b2-three-cooperation-modes
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-three-cooperation-modes.md"
    title: Trois modes de coopération B2 — parallel / handoff / negotiation
    last_modified: 2026-08-19
  - id: aquaman-jtbd-emit-receive
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-jtbd-emit-receive.md"
    title: Aquaman — 4 formes émises + 4 reçues
    last_modified: 2026-08-19
  - id: aquaman-couplages-invisibles
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-couplages-invisibles.md"
    title: Aquaman — 5 couplages invisibles hors matrice
    last_modified: 2026-08-19
  - id: aquaman-defensibility-triple-signature
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-defensibility-triple-signature.md"
    title: Aquaman — triple signature phase 5
    last_modified: 2026-08-19
  - id: b2-council-cadence
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-council-cadence-and-chair.md"
    title: B2 Council — cadence, présidence tournante, mécanique de séance
    last_modified: 2026-08-19
  - id: b2-pair-check-raci
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang sur les 9 pair-checks
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Aquaman — mapping des 3 modes de coopération sur les 4 formes émises

## Le trou comblé — quel mode pour Aquaman ?

[[b2-three-cooperation-modes]] pose les 3 modes canoniques
(parallel / handoff / negotiation) avec leurs signaux de passage
et leurs anti-pièges. La doctrine est générale — elle ne dit pas
*quel mode s'applique* pour un domaine spécifique.

Les concepts Aquaman précédents ont utilisé les 3 modes *de
manière incidente* :

- **Tour 1 §5.1 couplage Aquaman ↔ Cyborg** : cas de
  `negotiation` (convergence de vetos).
- **Tour 2 §T5.2 catalog JTBD** : gating conditions côté reçu
  (suggère `handoff` implicite).
- **Tour 3 concept 11 defensibility** : triple signature
  séquentielle (suggère `handoff` strict).
- **Tour 4 concept 14 classification 4 formes** : 4 classes
  routables sans séquencement (suggère `parallel` par défaut).

Aucune projection cohérente n'a posé la **table Aquaman × mode**.
C'est l'objet de ce concept.

## La table Aquaman × mode canonique

| Aquaman situation | Mode canonique | Pourquoi | Source / projection |
|---|---|---|---|
| Privacy review seul (sur actif IT Cyborg, sans interaction client) | **parallel** | Pas de couplage détecté. Aquaman produit seul. | Étude couplage-invisible #1 (Cyborg) — pas de veto Convergence |
| Claim safety pour Superman | **negotiation** | Convergence possible (Aquaman bloque claim, Superman tient canal diffusion). Reformulation coûteuse côté Superman. | [[b2-three-cooperation-modes]] exemple : Finance ↔ Growth |
| Contract template pour JohnJones | **handoff** | Sequencement strict : reformulation client (Sales) → perimeter (Legal) → signature | Pair-check #11 [[aquaman-sales-pipeline-hand-over]] handoff strict |
| Defensibility doc (Binder phase 5) | **handoff + triple signature** | Sequencement triple (Aquaman → Batman → Thena) avec signature conjointe | [[aquaman-defensibility-triple-signature]] tour 3 |
| Périmètre Privacy + IP (cycle 5 phases) | **handoff intra-Aquaman** | Sequencement phase 2 (scoping) → phase 3 (drafting) → phase 4 (review) [[aquaman-cycle-de-vie-legal-5-phases]] | Cycle 5 phases |
| Privacy review sur actif avec IP tierce | **negotiation Aquaman-Cyborg** | Convergence possible (Aquaman privacy IP, Cyborg cloud-only veto) | [[aquaman-couplages-invisibles]] couplage #1 |
| Honoraires avocats externes (Wonder Woman) | **negotiation Aquaman-WW** | Aquaman qualité review, WW viabilité économique. Tradeoff explicite. | [[aquaman-couplages-invisibles]] couplage #2 |
| Réécriture claim bloquée (Superman) | **handoff inverse** | Superman doit *consommer* le blocker Aquaman et traduire en claim corrigée | [[aquaman-couplages-invisibles]] couplage #3 |
| Handoff Sales → Legal (template pair-check #11) | **handoff structuré** | Sequencement standard Sales → Legal → Ops | [[aquaman-sales-pipeline-hand-over]] tour 4 |
| Owners signataires (Green Lantern) | **handoff négocié** | Aquaman attend matrice signature People, escalade si manquante | [[aquaman-couplages-invisibles]] couplage #5 |

**Trois constats majeurs** :

1. **Le handoff domine** la matrice Aquaman × mode. La majorité des
   cas Aquaman sont des handoffs (sequencements stricts).
2. **Le parallel est minoritaire** — il concerne les cas où
   Aquaman produit seul (privacy review standalone, par exemple).
3. **Le negotiation apparaît toujours par convergence** —
   Aquaman opposant son veto face à un autre captain qui tient
   une exigence contradictoire.

## Les 4 cas ambigus (Aquaman peut basculer entre deux modes)

Quatre cas où l'Aquaman mode choice peut basculer entre deux
modes :

| # | Cas | Mode initial | Mode basculé | Signal de bascule |
|---|---|---|---|---|
| 1 | Privacy review autonome qui devient conflit IP tierce | parallel | negotiation | IP tierce détectée par Cyborg → bascule Aquaman-Cyborg convergence |
| 2 | Claim safety pour Superman sans reformulation préalable | handoff (implicite) | negotiation | Superman publie malgré veto shadow → bascule en negotiation Aquaman-Superman reformulation |
| 3 | Contract template pour JohnJones sans gating inputs amont | handoff | negotiation | Cycle Aquaman handoff bloqué par gating input manquant → bascule en negotiation Aquaman-JohnJones |
| 4 | Defensibility doc en triple signature avec Batman absent | handoff séquentiel | negotiation | Batman retarde ou refuse → bascule Aquaman-Batman séquence aquaman-batman |

**Subtilité du cas 4** : un Aquaman ACTIVE qui signe un binder
sans Batman bloque la production. La bascule en negotiation
nécessite l'accord de Batman.

## Le test de mode — comment trancher en pratique

[[b2-three-cooperation-modes]] pose les anti-pièges *« Changement
de mode silencieux »* : *« Le packet de sortie doit contenir le
mode initial ET le mode final. Si vous ne pouvez pas le documenter,
le changement n'a pas eu lieu. »*

Test de mode applicable à Aquaman :

```
1. Aquaman reçoit une demande (engagement, packet Council, deal amont)
2. Aquaman identifie les autres domaines impactés :
   - Aucun → parallel
   - Sequencement strict détecté (handoff) → handoff
   - Conflit de DoDs détecté → negotiation
3. Si ambiguous (4 cas ci-dessus) → appliquer le test de gating :
   - Tous les gating inputs sont-ils présents ?
     - Oui → mode initial = handoff possible
     - Non → mode initial = parallel (Aquaman produit en shadow)
4. Documenter mode initial dans le packet B2-MESO-DECISION
5. Si mode bascule en cours d'exécution, créer un packet Council
   séparé pointant sur l'id d'origine (D4 append-only)
```

**Cas spécial** : Aquaman en mode **Dormant** (cf.
[[aquaman-dormance-doctrine-canonique-alignement]]) — le mode
applicable est **forcément parallel**, parce qu'Aquaman ne peut
ni handoff (pas de production) ni negotiation (pas de veto
opposable). Cette règle triviale mais souvent oubliée évite les
erreurs d'application de mode à un Aquaman en sommeil.

## Le diagramme Aquaman × mode état

```
État Aquaman × couplage :
├── Dormant
│   └── parallel (triviale — pas de production, pas de veto opposable)
├── SHADOW_ACTIVE
│   ├── parallel (production shadow sans couplage)
│   ├── handoff (sequencement strict amont→aval)
│   └── negotiation (veto shadow oppose mais ne bloque pas, juste signale)
└── ACTIVE
    ├── parallel (production standard sans couplage)
    ├── handoff (sequencement strict amont→aval avec veto opposable)
    └── negotiation (veto opposable, peut bloquer production)
```

**Conséquence** : un Aquaman SHADOW_ACTIVE qui opère en
negotiation émet un veto *information*, pas *arrêt* (cf.
[[aquaman-dormant-activation]] §Asymétrie 2 — le veto). Un
Superman qui publie la claim malgré le veto shadow engage sa
propre responsabilité — Aquaman reste Consulted.

## Le couplage avec la triple signature phase 5

[[aquaman-defensibility-triple-signature]] pose la triple
signature Aquaman + Batman + Thena. Cette triple signature est un
**handoff séquentiel avec consignature**. Le mode canonique est
`handoff`, mais il a la particularité d'inclure **2 capitaines B2**
(Aquaman + Batman) et **1 squad lead B3** (Thena).

**Trois cosignataires, un handoff** : la signature conjointe
remplace la signature isolée de chaque cosignataire (qui reste
nécessaire pour les phases 1-4). Phase 5 uniquement.

**Couplage mode ↔ doctrine** : la triple signature est **uniquely
ACTIVE** — un Aquaman SHADOW_ACTIVE ne peut pas produire un
binder triple-signé. Le passage SHADOW_ACTIVE → ACTIVE est forcé
par la phase 5 Binder (cf. cycle 5 phases concept tour 5 #2).

## L'application asymétrique aux 5 couplages invisibles

Reprenons les 5 couplages invisibles de
[[aquaman-couplages-invisibles]] et le mode applicable à chacun :

| Couplage | Mode canonique applicable | Conséquence |
|---|---|---|
| Aquaman ↔ Cyborg (privacy IT) | **negotiation** | Convergence de vetos possible (cycle 5 phases sortie) |
| Aquaman ↔ Wonder Woman (honoraires avocats) | **negotiation** | Tradeoff qualité/coût explicite |
| Aquaman ↔ Superman (réécriture claims) | **handoff inverse** ou **negotiation** | Selon le cas (claim réécrite facilement vs reformulation lourde) |
| Aquaman ↔ JohnJones (clauses commerciales) | **handoff structuré** (pair-check #11) | Sequencement strict |
| Aquaman ↔ Green Lantern (owners signataires) | **handoff négocié** | Sequencement + escalade si matrice signature manquante |

**Subtilité** : les 5 couplages ne sont pas tous du même mode.
L'application asymétrique est un fait doctrinal à documenter dans
chaque packet mésoperpétuel Aquaman.

## Anti-pièges

- **Parallel par défaut sans scan**. Sans scan matrice
  d'harmonisation, Aquaman déclare parallel des cas qui sont
  en fait handoff ou negotiation. C'est l'anti-piège canon
  [[b2-three-cooperation-modes]] §Anti-pièges.
- **Handoff strict alors que rework possible**. Si le deuxième
  domaine peut commencer avec une version dégradée, c'est
  negotiation, pas handoff. Pour Aquaman, un dossier Binder peut
  commencer en signature partielle Batman-only, mais ce n'est
  plus un handoff strict.
- **Negotiation sans DoD de remplacement**. Aquaman qui négocie
  un honoraires externes sans poser de DoD de remplacement (par
  exemple honoraires internes) crée un abandon déguisé. C'est
  l'anti-piège canon *« Negotiation avec un DoD abandonné »*.
- **Mode figé en début de cycle**. Le mode peut basculer (4 cas
  ambigus) — figer le mode au début de cycle sans possibilité
  de bascule produit un packet figé qui ne reflète pas la
  réalité.
- **Aquaman Dormant en negotiation**. Mode forcé parallel pour
  Aquaman Dormant. Toute tentative de negotiation est overreach.

## Liens

- [[b2-three-cooperation-modes]] — la doctrine des 3 modes
- [[aquaman-jtbd-emit-receive]] — les 4 formes émises qui
  supportent le mapping
- [[aquaman-couplages-invisibles]] — les 5 couplages dont le mode
  est asymmetric
- [[aquaman-cycle-de-vie-legal-5-phases]] — le cycle 5 phases dont
  les phases 2-3-4 sont en handoff interne
- [[aquaman-defensibility-triple-signature]] — la triple
  signature phase 5 qui force ACTIVE
- [[aquaman-dormant-activation]] — la tri-partition qui force
  parallel pour Dormant
- [[aquaman-sales-pipeline-hand-over]] — le handoff pair-check
  #11 type
- [[b2-council-cadence-and-chair]] — la mécanique de séance qui
  tranche les modes ambigus

## Note de confiance

**Reconstruit à partir de la doctrine canonique.**

- ✅ `b2-three-cooperation-modes.md` cité verbatim (3 modes,
  signaux de passage, anti-pièges).
- ✅ 5 couplages invisibles, 4 formes émises, 5 phases cycle
  Aquaman : cités depuis concepts tour 1 à 4.
- 🟡 La table Aquaman × mode est une **projection depuis la
  doctrine canonique** et les concepts Aquaman précédents. **Pas
  de triplet canonique** sur la projection Aquaman × mode.
- 🟡 Les 4 cas ambigus sont des **cas-types opérationnels**
  projetés depuis la pratique — pas observés en cycle.
- ❌ Non vérifié en cycle : aucun packet mésoperpétuel Aquaman
  n'a été émis en Vague 2. Le mapping est **prospectif**.
