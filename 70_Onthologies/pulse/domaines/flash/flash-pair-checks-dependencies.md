---
type: Concept
title: Flash Product — pair-checks et dépendances inter-domaines
description: Le domaine Product (03) est impliqué dans 4 pair-checks sur 9 (Product×Ops, Product×IT, Finance×Product, Legal×Product). Pour chaque pair-check, Flash est soit en aval (Accountable, A) soit en amont (Consulted, C). Le RACI par rang (cf. b2-pair-check-raci-by-rank) ancre cette matrice ; les couplages indirects (Sales→Product→Ops, IT→Product) restent non-canoniques.
tags: [flash, product, pair-check, dependencies, raci, rang, aval, amont, b2-council]
generated: { by: minimax-m3, at: 2026-08-19T04:30:00Z }
verified:
  - { by: process:lecture-corpus-flash, at: 2026-08-19T04:30:00Z }
sources:
  - id: harmonization
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/areas/business-wheel-harmonization-matrix.md"
    title: Harmonisation de la wheel — 9 pair checks
    last_modified: 2026-08-17
  - id: harmonization-exploitable
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-harmonization-matrix-exploitable.md"
    title: Matrice d'harmonisation B2 — forme exploitable (l. 46-58)
    last_modified: 2026-08-19
  - id: raci-by-rank
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang sur les 9 pair-checks — tableau l. 67-78
    last_modified: 2026-08-19
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — Flash = 03 Product
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Flash Product — pair-checks et dépendances

## Le périmètre des 4 pair-checks impliquant Product

La matrice d'harmonisation pose 9 pair-checks canoniques (cf. `business-wheel-harmonization-matrix.md` §« Les 9 pair checks canoniques »). Le domaine Product (03) est impliqué dans **4 d'entre eux** :

| # | Pair-check | Question de garde | Flash position | RACI par rang |
|---|---|---|---|---|
| 3 | Product → Ops | L'artefact est-il supportable opérationnellement ? | amont (C) | A = Ops, R = Fantastic Four, C = Product, I = B1, Avengers |
| 4 | Product → IT | Le produit tourne-t-il, déploie, récupère, est-il accessible ? | amont (C) | A = IT, R = Kang Dynasty, C = Product, I = B1, Avengers |
| 6 | Finance → Product | Le coût de build protège-t-il la marge ? | aval (A) | A = Product, R = Avengers, C = Finance, I = B1, Thunderbolts |
| 8 | Legal → Product | Les frontières IP/privacy/terms sont-elles claires ? | aval (A) | A = Product, R = Avengers, C = Legal, I = B1, Eternals |

**Flash est en aval (A) sur 2 pair-checks, en amont (C) sur 2 pair-checks.**

## Pair-check #3 — Product → Ops (Flash = C, Batman = A)

### Le transfert

Ops (Batman / Fantastic Four) reçoit l'artefact produit par Avengers et doit le **maintenir en run**. La question : *« l'artefact est-il supportable opérationnellement ? »* (maintenabilité, support, monitoring).

### Le RACI par rang

| Rôle | Acteur |
|---|---|
| **A** (Accountable) | Batman (Ops) |
| **R** (Responsible) | Fantastic Four |
| **C** (Consulted) | Flash (Product) |
| **I** (Informed) | B1, Avengers |

### Cas concret

Flash livre un artefact avec une logique de scoring algorithmique. Batman refuse de le maintenir en run parce que la complexité dépasse la SOP support standard. Flash est consulté (C) parce qu'il connaît l'artefact ; mais Batman arbitre (A) parce qu'il porte la responsabilité de la boucle.

**Trois issues** :
- Flash enrichit la documentation (runbook) → Batman accepte de maintenir
- Batman absorbe la complexité (formation squad Fantastic Four) → Flash accepte de payer la formation
- Scope réduit (Flash retire la logique algorithmique) → Batman accepte de maintenir le reste

**Mode Council** : **handoff** (Ops doit finir avant que la maintenance ne commence).

## Pair-check #4 — Product → IT (Flash = C, Cyborg = A)

### Le transfert

IT (Cyborg / Kang Dynasty) reçoit le code produit par Avengers et doit le **déployer, monitorer, sauvegarder, restaurer**. La question : *« le produit tourne-t-il, déploie, récupère, est-il accessible ? »* (run, déploiement, recovery, accessibilité).

### Le RACI par rang

| Rôle | Acteur |
|---|---|
| **A** (Accountable) | Cyborg (IT) |
| **R** (Responsible) | Kang Dynasty |
| **C** (Consulted) | Flash (Product) |
| **I** (Informed) | B1, Avengers |

### Cas concret

Flash produit une feature qui dépend d'une librairie open-source devenue vulnérable. Cyborg refuse de la redéployer tant que le refactor n'est pas fait. Flash est consulté sur le refactor, mais Cyborg arbitre sur la politique de sécurité.

**Trois issues** :
- Flash refactore (mise à jour dépendance) → Cyborg redéploie
- Flash retire la feature du scope → Cyborg déploie sans la feature
- Cyborg absorbe le risque (exception documentée) → Flash accepte le risque résiduel

**Mode Council** : **handoff** (IT doit finir avant que le déploiement ne soit validé).

## Pair-check #6 — Finance → Product (Flash = A, Wonder Woman = C)

### Le transfert

Finance (Wonder Woman / Thunderbolts) alloue un budget de build, et Flash (Avengers) doit produire l'artefact **dans le budget**. La question : *« le coût de build protège-t-il la marge ? »* (coût de construction vs marge brute).

### Le RACI par rang

| Rôle | Acteur |
|---|---|
| **A** (Accountable) | Flash (Product) |
| **R** (Responsible) | Avengers |
| **C** (Consulted) | Wonder Woman (Finance) |
| **I** (Informed) | B1, Thunderbolts |

### Cas concret

Wonder Woman alloue 50K€ sur Q3 pour la squad Avengers build SaaS builder. Avengers consomme 75K€ sans ROI démontrable. Wonder Woman oppose son veto-dépense récurrente sur l'outil de monitoring (cf. `flash-domain-perimeter.md` §« Frontière 4 »). Flash est Accountable parce qu'il porte la responsabilité de **tenir la marge** ; Wonder Woman est Consulted sur le coût de build, mais le DoD de la marge reste chez Flash.

**Trois issues** :
- Flash réduit le scope pour tenir le budget → Wonder Woman accepte
- Flash démontre un ROI supérieur (lead indicators) → Wonder Woman libère un budget complémentaire
- Flash consomme plus et accepte une marge plus faible → B1 arbitre le risque d'ensemble

**Mode Council** : **negotiation** (les deux DoDs — coût Finance, marge Product — sont légitimes et s'opposent).

## Pair-check #8 — Legal → Product (Flash = A, Aquaman = C)

### Le transfert

Legal (Aquaman / Eternals) déclare les frontières IP/privacy/terms, et Flash (Avengers) doit **appliquer** ces frontières dans le code et l'UI. La question : *« les frontières IP/privacy/terms sont-elles claires ? »* (propriété intellectuelle, vie privée, conditions générales).

### Le RACI par rang

| Rôle | Acteur |
|---|---|
| **A** (Accountable) | Flash (Product) |
| **R** (Responsible) | Avengers |
| **C** (Consulted) | Aquaman (Legal) |
| **I** (Informed) | B1, Eternals |

### Cas concret

Aquaman Legal déclare que les CGU doivent inclure une clause RGPD spécifique. Avengers produit le code mais oublie la clause dans l'UI on-boarding. Aquaman est consulté (C) sur les frontières, mais Flash est Accountable parce qu'il porte la responsabilité de **l'application** des frontières dans l'artefact.

**Trois issues** :
- Flash corrige le code et l'UI → Aquaman valide la conformité
- Aquaman amende les frontières (assouplissement) → Flash applique la version amendée
- B1 mandate une revue de conformité → pause du launch jusqu'à validation

**Mode Council** : **handoff** (Legal doit finir avant que le launch public ne soit validé).

## Pourquoi Flash porte 2A et 2C — l'asymétrie aval/amont

L'asymétrie est significative : Flash est **Accountable** sur les pair-checks où il est **en aval** (Finance → Product, Legal → Product) — il reçoit un input (budget, cadre légal) et doit produire un output (artefact dans la marge, artefact conforme). Flash est **Consulted** sur les pair-checks où il est **en amont** (Product → Ops, Product → IT) — il produit un input (artefact) et l'aval doit le consommer.

Cette asymétrie correspond à la doctrine RACI par rang (cf. `b2-pair-check-raci-by-rank.md` §« Pourquoi A = B2 en aval, pas B1 ») :

> *« Règle de lecture : A est toujours le B2 captain en aval de la
> transition (le domaine qui reçoit). C'est la position b2-b3-jtbd-handoff-contract.md
> §« Le rôle du capitaine B2 sponsor » qui devient une matrice systématique. »*

Conséquence opérationnelle : un arbitrage sur un conflit pair-check impliquant Product doit faire venir **Flash en aval** (pour décider) ou en **amont** (pour être consulté), mais pas comme arbitre final — c'est Batman, Cyborg, Wonder Woman ou Aquaman qui arbitrent, selon la transition.

## Les couplages indirects — Sales → Product, People → Product, Growth → Product

La matrice d'harmonisation pose 9 pair-checks explicites. Trois couplages impliquant Product **ne sont pas dans la matrice** mais sont opérationnellement critiques :

### Couplage indirect 1 — Sales → Product

JohnJones (Sales) signe un deal avec un client. Flash doit matérialiser l'artefact promis. **Le transfert n'est pas formalisé** dans la matrice d'harmonisation canonique — Sales est la **source amont** du scope, mais la matrice ne pose pas explicitement le pair-check Sales → Product.

**Risque** : un deal signé par Sales sans scope formalisé arrive chez Flash en `NEEDS_SCOPE`. Sans matrice, le B2 Council n'a pas de mécanisme automatique pour bloquer le deal. Conséquence : `flash-domain-perimeter.md` §« Frontière 1 » documente cette frontière comme **floue**.

### Couplage indirect 2 — People → Product

Green Lantern (People) onboarde ou forme les Avengers. La **composition de la squad** est une décision People, mais la **capacité de production** dépend de cette composition. Sans matrice, le Council ne teste pas la cohérence People × Product.

**Risque** : un recrutement Avengers sans critère de sortie (veto Green Lantern non opposé) produit une squad stable mais sans discipline de renouvellement. À 18 mois, la squad Avengers perd 30% de ses agents sans plan de relève.

### Couplage indirect 3 — Growth → Product

Superman (Growth) signale un besoin marché. Flash doit matérialiser ce besoin en produit. **Le transfert n'est pas formalisé** dans la matrice — Growth est la **source amont** du signal, mais la matrice ne pose pas explicitement le pair-check Growth → Product.

**Risque** : un signal marché non qualifié (sans ICP, sans churn, sans validation) arrive chez Flash en `NEEDS_SCOPE`. Sans matrice, le Council ne peut pas bloquer le lancement d'un produit sans validation Growth.

## Pourquoi ces couplages indirects existent

La matrice d'harmonisation est **une heuristique à 9 entrées**, pas une carte exhaustive des transitions. Les couplages indirects sont **révélés en cycle réel** quand un arbitrage B2 échoue à trouver la ligne canonique. Le triplet 56-57 cite Batman qui **remonte les faits** — c'est précisément le mécanisme par lequel les couplages indirects deviennent visibles.

**Conséquence** : ces trois couplages indirects sont **des candidats pour un futur amendement de la matrice** (cf. `b2-veto-amplification-cycle.md` §« La procédure d'amendement »). L'amendement exige l'unanimité du Council + escalate B1 — c'est une décision lourde, justifiée par une pratique observée.

## Anti-pièges

- **Confondre A et R.** Flash est Accountable sur les pair-checks en aval, mais c'est **Avengers** (B3 squad) qui est Responsible de l'exécution. Flash arbitre, CaptainAmerica exécute.
- **Flash qui consulte Wonder Woman sur le scope technique.** Wonder Woman est Consulted sur le **coût** (Finance → Product), pas sur le **scope technique**. Si Flash demande l'avis de Wonder Woman sur la stack technique, il brouille la matrice.
- **Batman qui consulte Flash sur la SOP support.** Flash est Consulted sur l'**artefact** (Product → Ops), pas sur la **SOP support**. Si Batman demande l'avis de Flash sur la SOP, il brouille la matrice.
- **Couplage indirect utilisé pour justifier une escalade B1.** Les couplages Sales → Product, People → Product, Growth → Product ne sont **pas** dans la matrice canonique. Un arbitrage qui s'appuie sur un couplage indirect doit le **déclarer** explicitement, pas le présenter comme une entrée canonique.

## Liens

- [[b2-harmonization-matrix-exploitable]] — les 9 critères cross-domaines
- [[b2-pair-check-raci-by-rank]] — la matrice RACI par rang
- [[b2-council-arbitrage-rule]] — qui tient le Council et arbitre les pair-checks
- [[flash-domain-perimeter]] — le périmètre et les 4 frontières floues
- [[flash-jtbd-emit-receive]] — les paquets JTBD émis/reçus
- [[flash-red-flag-1-trigger]] — la conséquence si Ops/IT sont rouges pendant que Product est vert
- [[eight-domain-avengers-wheel]] — la cartographie 8-domaines V4

## Note de confiance

**Confirmé par machine, à moitié étayé.** Les 4 pair-checks impliquant Product (#3, #4, #6, #8) sont **verbatim** de la matrice d'harmonisation + RACI par rang. Le RACI par rang (A = B2 en aval) est reconstruit dans `b2-pair-check-raci-by-rank.md` (à moitié étayé, cf. §« Note de confiance » du concept). Les 3 cas concrets (logique algorithmique Product → Ops, dépendance vulnérable Product → IT, dépassement budget Finance → Product) sont **projetés** à partir de la pratique observée — pas explicitement documentés dans le canon. Les 3 couplages indirects (Sales → Product, People → Product, Growth → Product) sont **reconstruits** à partir des frontières floues documentées dans `flash-domain-perimeter.md` — pas une catégorie canonique du corpus.
