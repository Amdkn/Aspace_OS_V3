---
type: Concept
title: Flash — mandat CaptainAmerica comme squad lead Avengers
description: CaptainAmerica est le squad lead Avengers par convention (premier agent nommé dans triplet v3 ligne 17), mais son mandat n'est pas explicité dans le canon. Ce concept pose le mandat en 5 responsabilités, 3 escalations, et la double signature du contrat B2 → B3 conjointement avec Flash. Distingue la lecture CaptainAmerica = orchestrateur (H30 doctrine première ligne) de la lecture CaptainAmerica = super-héros (port canon Marvel).
tags: [flash, avengers, captain-america, squad-lead, mandate, h30, orchestrateur, double-signature, scrums]
generated: { by: minimax-m3, at: 2026-08-19T08:30:00Z }
verified:
  - { by: process:lecture-corpus-flash-tour-3, at: 2026-08-19T08:30:00Z }
sources:
  - id: triplet-v3-line-17
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet v3 ligne 17 — Avengers 7 techniciens (CaptainAmerica, IronMan, Thor, Hulk, BlackWidow, Hawkeye, ScarletWitch)"
    last_modified: 2026-08-17
  - id: flash-jtbd-emit-receive
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-jtbd-emit-receive.md"
    title: Flash — JTBD émis/reçus §« Le rôle de CaptainAmerica comme squad lead »
    last_modified: 2026-08-19
  - id: b2-b3-jtbd-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: B2 → B3 contract — double signature B2 sponsor + B3 lead
    last_modified: 2026-08-19
  - id: b3-jtbd-reception
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-jtbd-packet-reception-checklist.md"
    title: B3 JTBD packet reception checklist
    last_modified: 2026-08-19
  - id: b3-cycle-scrums
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-cycle-scrums-five-per-week.md"
    title: B3 cycle scrums 5 per week
    last_modified: 2026-08-19
  - id: b3-veto-vocabulary
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-veto-and-signal-vocabulary.md"
    title: B3 veto and signal vocabulary — gates + statuts
    last_modified: 2026-08-19
  - id: fifty-three-roster
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/fifty-three-b3-agent-roster.md"
    title: 53 B3 Agent Roster — pattern de fiche roster (~400-470 mots)
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Flash — mandat CaptainAmerica comme squad lead Avengers

## Pourquoi expliciter maintenant

`flash-jtbd-emit-receive.md` §« Le rôle de CaptainAmerica comme squad lead » identifie CaptainAmerica comme **premier agent nommé** dans le triplet v3 ligne 17 et lui attribue 4 responsabilités :

> *« CaptainAmerica porte donc : la tenue de scrums.md du sprint Avengers, le signalement des trous à Flash (triplet 41), la livraison de la preuve dans l'une des 4 formes canoniques, la double signature du contrat B2 → B3 conjointement avec Flash. »*

Mais ce rôle reste **projeté** à partir de la convention *« premier agent nommé = squad lead »* — pas explicitement posé ailleurs dans le canon (cf. note de confiance de `flash-jtbd-emit-receive.md` §« Note de confiance »). Le rapport tour 1 signale explicitement :

> *« 7ᵉ agent Avengers ScarletWitch spécialité H90 'transformation scope' projetée non-vérifiée fiche individuelle. »*

(`RAPPORT_dom-flash.md` tour 1 ouverture, persistant en tour 2 ouverture).

Ce concept explicite le mandat de CaptainAmerica en 5 responsabilités, 3 escalations, et la double signature — pour fermer cette lacune.

## Lecture orchestrateur (H30) vs lecture super-héros (port canon)

Deux lectures également défendables du nom canon :

| Lecture | Description | Compatibilité avec squad lead |
|---|---|---|
| **Orchestrateur (H30 — première ligne)** | Captain America = premier Captain (premier orchestrateur), lead de la discipline squad | ✅ cohérente avec `b2-pair-check-raci-by-rank.md` (R = B3 squad lead) |
| **Super-héros (port canon Marvel)** | Captain America = héros individuel avec pouvoirs spécifiques (bouclier, leadership moral) | ⚠️ incohérente avec le rôle B3 (exécution opérationnelle, pas héroïsme individuel) |

**Recommandation** : la lecture orchestrateur (H30) est cohérente avec le rôle B3 squad lead. La lecture super-héros est une projection du port canon Marvel qui ne se vérifie pas dans la pratique B3 (les B3 ne sont pas des super-héros individuels, ce sont des exécutants spécialisés).

**Conséquence** : la fiche roster `_doctrine/agents/b3-captain-america.md` doit déclarer la lecture orchestrateur (H30 — première ligne) et **écarter explicitement** la lecture super-héros pour éviter la confusion.

## Les 5 responsabilités du squad lead CaptainAmerica

### Responsabilité 1 — Tenue de scrums.md

**Référence canonique** : triplet 8 — *« B3 produit SCRUMS.md et rien d'autre, interdit rock et sprint »*.

**Application Avengers** : CaptainAmerica tient le `B3_Avengers_<domaine>/scrums.md` du sprint en cours, avec une ligne par jour par agent (7 agents × 5 jours = 35 lignes/semaine, 140/mois).

**Critère d'acceptance** : chaque ligne contient (a) le nom de l'agent, (b) l'action du execute (pas un plan — triplet 11), (c) le statut (`ON_TRACK` / `AT_RISK` / `BLOCKED` / `DONE`), (d) la date.

**Anti-piège** : un scrums.md qui contient des plans (futur) au lieu d'actions (présent) est une violation du triplet 11.

### Responsabilité 2 — Signalement des trous à Flash

**Référence canonique** : triplet 41 — *« B3 interdit-combler-trou »*.

**Application Avengers** : CaptainAmerica signale à Flash tout trou dans le contrat B2 → B3 — DoD non chiffré, proof path manquant, scope flou, dependency non documentée. Le signal est un ping Council Flash → CaptainAmerica (pas un message asynchrone).

**Critère d'acceptance** : le journal CaptainAmerica contient ≥ 1 entrée `trou_signale` par sprint où un trou est détecté. La timestamp de l'entrée ≤ 24h après détection.

**Anti-piège** : un CaptainAmerica qui comble un trou sans signaler (ex : *« le DoD était flou, j'ai pris l'hypothèse X »*) viole le triplet 41. Cf. `flash-jtbd-emit-receive.md` §« Anti-pièges ».

### Responsabilité 3 — Livraison de la preuve (4 formes canoniques)

**Référence canonique** : `b3-proof-path-4-formes.md` (4 formes : capture, log, métrique, témoignage client).

**Application Avengers** : CaptainAmerica choisit 1 ou 2 formes parmi les 4 (déclarées dans le contrat B2 → B3) et livre la preuve à la fin du sprint. La livraison est consignée dans le `jtbd_packet.delivered` du sprint.

**Critère d'acceptance** : la preuve est dans l'une des 4 formes canoniques, vérifiable par un tiers qui n'est pas CaptainAmerica, et mappée sur le DoD chiffré du contrat.

**Anti-piège** : une preuve qui n'est pas dans les 4 formes (ex : *« ça marche, je te jure »*) viole le contrat B2 → B3.

### Responsabilité 4 — Double signature du contrat B2 → B3

**Référence canonique** : `b2-b3-jtbd-handoff-contract.md` §« Le format conjoint » — *« Le contrat est consigné dans le JTBD packet B3, avec un en-tête contract: qui pointe sur le packet mésoperpétuel source. »*

**Application Avengers** : CaptainAmerica signe conjointement avec Flash (B2 sponsor) le contrat `jtbd_packet_id` → `source_meso_decision`. La double signature est dans `B3_Avengers_<domaine>/contracts/`.

**Critère d'acceptance** : chaque paquet JTBD Avengers actif a une double signature dans son en-tête `contract: contract_signed.b2_sponsor: flash + contract_signed.b3_squad_lead: captain_america + contract_signed.signed_at`.

**Anti-piège** : un paquet JTBD sans double signature est un **ordre unilatéral**, pas un contrat. La discipline de double signature est la **propriété du rang B3 lead**, pas une option.

### Responsabilité 5 — Agrégation des 7 statuts Avengers en 1 gate Product

**Référence canonique** : `flash-jtbd-emit-receive.md` §« Ce que la squad Avengers émet » — *« Flash agrège ces 140 statuts en une gate Product (l'un des 3 signaux READY/NEEDS/BLOCKED). »*

**Application Avengers** : CaptainAmerica collecte les 35 statuts/semaine (7 agents × 5 jours), les agrège en 1 gate Avengers/semaine, et la transmet à Flash pour validation. La gate Avengers devient un input de la gate Product Flash.

**Critère d'acceptance** : la gate Avengers est transmise à Flash chaque vendredi avant 17h, avec :
- `aggregate_status: ON_TRACK | AT_RISK | BLOCKED`
- `breakdown: <statut par agent>`
- `blockers: <liste des blocers ouverts>`
- `next_week_plan: <sprint suivant>`

**Anti-piège** : CaptainAmerica qui agrège en `ON_TRACK` par défaut sans diagnostiquer les statuts `AT_RISK` ou `BLOCKED` rend la gate Avengers mensongère. Cf. `flash-jtbd-emit-receive.md` §« Anti-pièges ».

## Les 3 escalations CaptainAmerica → Flash

### Escalation 1 — Trou non comblé (triplet 41)

**Trigger** : CaptainAmerica détecte un trou dans le contrat B2 → B3 (DoD flou, proof path manquant, scope ambigu).

**Action** : ping Flash dans la journée (≤ 24h). Documenter dans le journal CaptainAmerica.

**Issue** : Flash tranche (accepte amendement, retire mandat, ou escalade B2 Council).

**Anti-piège** : CaptainAmerica qui comble un trou sans escalader viole le triplet 41 (cf. responsabilité 2).

### Escalation 2 — Statut agent AT_RISK persistant

**Trigger** : un agent Avengers reste `AT_RISK` pendant ≥ 3 scrums consécutifs (3 jours ouvrés).

**Action** : CaptainAmerica signale à Flash avec contexte (cause, plan correctif de l'agent, risque). Si le plan correctif est inexistant → escalader en `BLOCKED`.

**Issue** : Flash arbitre (renfort squad, aménagement scope, ou pause sprint).

**Anti-piège** : un agent `AT_RISK` pendant 5 jours sans escalation est un silent rework (cf. `b2-b3-jtbd-handoff-contract.md` §« Failure mode 2 »).

### Escalation 3 — Lead indicator rouge avant J+2

**Trigger** : un lead indicator du contrat B2 → B3 vire au rouge (cf. `b2-b3-jtbd-handoff-contract.md` §« Lead indicators »).

**Action** : CaptainAmerica signale à Flash dans la journée (≤ 24h). Documenter le cap et le plan.

**Issue** : Flash arbitre (pivot scope, extension sprint, ou escalade B2 Council).

**Anti-piège** : un lead indicator rouge à J+2 signalé à J+7 est un **escalade tardive** (cf. `b2-b3-jtbd-handoff-contract.md` §« Failure mode 3 »).

## RACI CaptainAmerica — A, R, C, I

| Pair-check | Rôle CaptainAmerica | Cohérence avec RACI par rang |
|---|---|---|
| #3 Product → Ops | R (squad Avengers) | ✅ A = Batman, R = Fantastic Four ; CaptainAmerica est R pour Avengers côté Flash |
| #4 Product → IT | R (squad Avengers) | ✅ A = Cyborg, R = Kang Dynasty |
| #6 Finance → Product | R (squad Avengers) | ✅ A = Flash, R = Avengers |
| #8 Legal → Product | R (squad Avengers) | ✅ A = Flash, R = Avengers |
| #10 People → Product (V5) | R (squad Avengers) | ✅ si amendement V5 adopté |
| #11 Growth → Product (V5) | R (squad Avengers) | ✅ si amendement V5 adopté |

**Conclusion** : CaptainAmerica est **toujours R** sur les pair-checks impliquant Avengers. Il n'est jamais A (Accountable reste un B2 captain en aval) ni C sur ces pair-checks (sauf exception documentée).

## Le squad lead CaptainAmerica vs le capitaine B2 Flash — la distinction

Trois différences structurelles entre CaptainAmerica (squad lead B3) et Flash (capitaine B2) :

1. **Horizon temporel** — CaptainAmerica gère le **sprint** (1-4 semaines) ; Flash gère le **cycle 12WY** (12 semaines).
2. **Mandat opérationnel** — CaptainAmerica **exécute** le contrat B2 → B3 ; Flash **arbitre** la cohérence des pair-checks et signe conjointement le contrat.
3. **Voie d'escalade** — CaptainAmerica escalade à Flash (captain sponsor) en premier ; Flash escalade au B2 Council en mode handoff/negotiation (cf. `b2-three-cooperation-modes.md`).

**Conséquence** : un arbitrage B2 Council qui convoque CaptainAmerica directement (sans passer par Flash) casse l'ordre vertical du fractal (cf. `b2-council-arbitrage-rule.md` §« Pourquoi pas B3 »).

## Le profil de fiche roster CaptainAmerica

Le pattern `fifty-three-b3-agent-roster.md` §« Le pattern de la fiche roster » impose ~400-470 mots par agent avec :
- Nom et rôle canonique
- Horizon (H10 / H30 / H90)
- B2 owner + sister canon
- Trigger phrases (pour dispatch Uplink B2 → B3)
- Edge cases / anti-patterns

**Application CaptainAmerica** :
- **Nom canon** : CaptainAmerica
- **Rôle** : squad lead Avengers (H30 — première ligne, orchestrateur)
- **B2 owner** : Flash (Product 03)
- **Sister canon** : MrFantastic (Fantastic4 squad lead) — symétrie B3 lead
- **Trigger phrases** : *« ping CaptainAmerica »*, *« escalate to CaptainAmerica »*, *« CaptainAmerica contract_signed »*
- **Edge cases** : CaptainAmerica qui tente de tenir un DoD sans scope formalisé (interdit — `NEEDS_SCOPE`), CaptainAmerica qui escalade au B2 Council sans passer par Flash (interdit — fractal violation)
- **Anti-patterns** : CaptainAmerica comblant un trou sans signaler (triplet 41 violation), CaptainAmerica agrégant en `ON_TRACK` par défaut (gate mensongère)

## Anti-pièges

- **Squad lead confondu avec super-héros.** La lecture super-héros (port canon Marvel) n'est pas cohérente avec le rôle B3. La fiche roster doit écarter cette lecture explicitement.
- **CaptainAmerica isolé du squad.** Si CaptainAmerica porte les 5 responsabilités mais n'a aucun agent sous sa coordination (squad vide), le mandat est vide. Le rôle n'existe que si la squad existe.
- **CaptainAmerica sans contrat signé.** Un CaptainAmerica qui pilote un sprint sans contrat B2 → B3 signé avec Flash est en **exécution sans mandat** — il porte un risque de scope creep et de silent rework.
- **CaptainAmerica qui agrège la gate Avengers par défaut.** L'agrégation doit refléter les 35 statuts/semaine, pas un optimisme par défaut. Une gate `ON_TRACK` avec 5 agents `BLOCKED` est une falsification.
- **CaptainAmerica sans Sister canon.** Le pattern roster prévoit une sister canon (squad lead d'une autre squad). CaptainAmerica a MrFantastic (Fantastic4). Sans cette symétrie, CaptainAmerica est un孤立队长 — la coordination inter-squads n'a pas d'analogue.

## Liens

- [[flash-jtbd-emit-receive]] — le rôle CaptainAmerica projeté dans le concept tour 1
- [[flash-domain-perimeter]] — la squad Avengers (7 agents) avec spécialités projetées
- [[flash-doD-build-run-sunset-three-stages]] — les critères que CaptainAmerica agrège
- [[b2-b3-jtbd-handoff-contract]] — la double signature B2 sponsor + B3 lead
- [[b3-jtbd-packet-reception-checklist]] — la vue B3 du contrat
- [[b3-cycle-scrums-five-per-week]] — la cadence 5 scrums/semaine CaptainAmerica
- [[b3-veto-and-signal-vocabulary]] — les 4 statuts B3 agrégés
- [[b3-proof-path-4-formes]] — les 4 formes canoniques CaptainAmerica livre
- [[fifty-three-b3-agent-roster]] — le pattern fiche roster à appliquer

## Note de confiance

**Reconstruit, à moitié étayé.** Le triplet v3 ligne 17 (CaptainAmerica premier nommé) est cité verbatim. Le triplet 8 (`B3 produit SCRUMS.md`), triplet 11 (action exécutable pas plan), triplet 41 (`B3 interdit-combler-trou`) sont cités verbatim. Le RACI par rang (A = B2 en aval) est canonique mais marqué « reconstruit » dans `b2-pair-check-raci-by-rank.md`. Les 5 responsabilités (tenue scrums.md, signalement trous, livraison preuve, double signature, agrégation gate) sont **projetées** à partir du rôle squad lead canonique Marvel + du triplet 8 + triplet 41 + du format conjoint `b2-b3-jtbd-handoff-contract.md` — pas explicitement posé ailleurs dans le corpus. Les 3 escalations (trou, AT_RISK persistant, lead indicator rouge) sont **reconstruites** à partir des 3 failure modes du contrat B2 → B3. La lecture orchestrateur H30 vs super-héros est **mon extrapolation** — le canon ne tranche pas entre les deux lectures. Standing : draft de mandat, à confronter au premier cycle Avengers observé et à la première fiche roster CaptainAmerica lue.