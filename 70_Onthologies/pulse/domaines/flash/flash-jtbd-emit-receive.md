---
type: Concept
title: Flash Product — paquets JTBD émis et reçus par le squad Avengers
description: Le domaine Product (03) captainé par Flash émet 3 signaux gate (PRODUCT_READY / NEEDS_SCOPE / BLOCKED_DELIVERY) et reçoit 6 types de paquets JTBD B2 entrants (depuis Growth, Sales, People, Finance, Legal, Ops). La squad Avengers (7 agents) consomme les paquets reçus en scrums quotidiens et produit les proof paths exigés par le contrat B2→B3.
tags: [flash, product, jtbd, emit, receive, avengers, packet, scrums, proof-path]
generated: { by: minimax-m3, at: 2026-08-19T04:25:00Z }
verified:
  - { by: process:lecture-corpus-flash, at: 2026-08-19T04:25:00Z }
sources:
  - id: avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — Flash = 03 Product = Avengers, gates PRODUCT_READY / NEEDS_SCOPE / BLOCKED_DELIVERY
    last_modified: 2026-08-17
  - id: b3-veto-vocabulary
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-veto-and-signal-vocabulary.md"
    title: B3 veto and signal vocabulary — les 8 gates READY/BLOCKED par domaine
    last_modified: 2026-08-19
  - id: b3-jtbd-reception
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-jtbd-packet-reception-checklist.md"
    title: B3 JTBD packet reception checklist — la vue B3 du contrat
    last_modified: 2026-08-19
  - id: b2-b3-contract
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-b3-jtbd-handoff-contract.md"
    title: B2 → B3 contract — quand une décision mésoperpétuelle devient un JTBD packet
    last_modified: 2026-08-19
  - id: b3-cycle-scrums
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b3/b3-cycle-scrums-five-per-week.md"
    title: B3 cycle scrums 5 per week — la mécanique de cadence B3
    last_modified: 2026-08-19
  - id: triplet-v3-line-17
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet v3 ligne 17 — Avengers = 7 techniciens (CaptainAmerica, IronMan, Thor, Hulk, BlackWidow, Hawkeye, ScarletWitch)"
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Flash Product — paquets JTBD émis et reçus

## Le triplet fondateur

Le triplet v3 ligne 17 pose la squad Avengers :

> *« Flash (VP B2 domaine 3 — Productization des Besoins) commande le
> squad Avengers (7 techniciens : CaptainAmerica, IronMan, Thor, Hulk,
> BlackWidow, Hawkeye, ScarletWitch). »*

7 agents, 5 scrums/semaine par agent (cf. `b3-cycle-scrums-five-per-week.md`), 4 sprints/mois par VP (triplet 10). La cadence combinée Avengers = **35 scrums/semaine**, soit ~140 par mois.

## Ce que Flash émet — les 3 signaux gate Product

Chaque transition impliquant Product émet l'un des 3 signaux du domaine 03 (cf. `eight-domain-avengers-wheel.md` §« Le mapping canonique ») :

| Signal | Quand | Action attendu du récepteur |
|---|---|---|
| `PRODUCT_READY` | L'artefact est supportable, le scope est tenu, la valeur d'artefact est indépendante de la personne | Ops peut maintenir, IT peut déployer, Sales peut reproduire le deal |
| `NEEDS_SCOPE` | Le besoin n'est pas formalisé, l'artefact ne peut pas être produit sans clarification amont | Growth ou Sales (selon la source) doit reformuler le scope |
| `BLOCKED_DELIVERY` | Le build ne tient pas la promesse de scope, le DoD n'est pas rempli | Batman Ops arbitre le handoff (transition Product → Ops) ou Cyborg IT arbitre le handoff (transition Product → IT) |

Le signal est émis **à chaque transition cross-domaine** impliquant Product. Un Produit qui ne passe jamais par ces trois états n'est pas en transition — il est en attente.

## Ce que Flash reçoit — 6 sources de paquets JTBD entrants

Flash ne produit pas ex nihilo. Le domaine Product **reçoit** des paquets JTBD de 6 sources amont :

### 1. Growth (Superman / Guardians)

**Type** : signal de besoin marché non qualifié
**Format** : `JTBD-FLASH-YYYY-NN` avec `intent: matérialiser_besoin_marché`
**Exemple** : *« matérialiser un MVP de coaching IA premium suite au signal paid media US »*

**Condition de réception** : Superman émet `GROWTH_READY` ET le besoin est qualifié en MQL.
**Cas `NEEDS_SCOPE`** : le besoin n'est pas formalisé, Flash remonte `NEEDS_SCOPE` à Superman.

### 2. Sales (JohnJones / Illuminati)

**Type** : deal signé avec scope client
**Format** : `JTBD-FLASH-YYYY-NN` avec `intent: produire_offre_pour_deal`
**Exemple** : *« produire le livrable 'coaching 6 mois premium' pour le client X signé le 2026-09-01 »*

**Condition de réception** : JohnJones émet `SALES_READY` ET le contrat est signé.
**Cas `BLOCKED_DELIVERY`** : le scope signé est irréalisable par la squad Avengers dans le cadre d'exécution promis.

### 3. People (Green Lantern / X-Men)

**Type** : onboarding squad Avengers ou formation agent existant
**Format** : `JTBD-FLASH-YYYY-NN` avec `intent: onboarder_agent_b3`
**Exemple** : *« onboarder ScarletWitch sur la pratique 'transformation scope' »*

**Condition de réception** : Green Lantern émet `ASSIGNED` ET le profil agent est documenté dans `_doctrine/agents/b3-*.md`.
**Cas `NEEDS_SCOPE`** : le profil agent n'a pas de mandat écrit ou de critère de sortie vérifiable.

### 4. Finance (Wonder Woman / Thunderbolts)

**Type** : budget de build alloué
**Format** : `JTBD-FLASH-YYYY-NN` avec `intent: consommer_budget_build`
**Exemple** : *« consommer 50K€ sur Q3 pour la squad Avengers build SaaS builder »*

**Condition de réception** : Wonder Woman émet `FINANCE_READY` ET la métrique de retour est chiffrée.
**Cas `BLOCKED_DELIVERY`** : le build consomme plus que le budget alloué sans ROI démontrable — Wonder Woman oppose son veto-dépense récurrente.

### 5. Legal (Aquaman / Eternals)

**Type** : cadre IP/privacy/terms à appliquer
**Format** : `JTBD-FLASH-YYYY-NN` avec `intent: formaliser_frontieres_juridiques`
**Exemple** : *« formaliser les CGU, la propriété intellectuelle du livrable, et la politique RGPD pour l'artefact Y »*

**Condition de réception** : Aquaman émet `LEGAL_READY` ET les frontières sont déclarées.
**Cas `NEEDS_SCOPE`** : les frontières IP/privacy/terms ne sont pas déclarées, Flash ne peut pas produire.

### 6. Ops (Batman / Fantastic Four)

**Type** : procédure de maintenance ou runbook attendu
**Format** : `JTBD-FLASH-YYYY-NN` avec `intent: preparer_maintenance_artefact`
**Exemple** : *« préparer le runbook de l'artefact Y avant le launch 2026-10-15 »*

**Condition de réception** : Batman émet (en transition vers Product, rare) ou la procédure de maintenance est documentée.

## Ce que la squad Avengers émet — 4 statuts par agent par scrum

Chaque agent Avengers tient un **scrum quotidien** (5/semaine) avec un statut à 4 états (cf. `b3-veto-and-signal-vocabulary.md` §« Couche 3 ») :

| Statut | Quand | Action Flash |
|---|---|---|
| `ON_TRACK` | Le scrum est dans le plan, pas de blocker | RAS |
| `AT_RISK` | Le scrum dérape mais l'agent a un plan correctif | Flash surveille ; peut demander un ping pair |
| `BLOCKED` | Le scrum est arrêté sur un blocker (pair, veto, trou de paquet) | Flash arbitre — pair-unblock upward, escalation, ou intervention directe |
| `DONE` | Le livrable est produit avec preuve | Flash consigne, marque le sous-paquet |

**Combinaison Avengers** : 7 agents × 5 scrums/semaine × 4 sprints/mois = 140 statuts/mois. Flash agrège ces 140 statuts en une **gate Product** (l'un des 3 signaux READY/NEEDS/BLOCKED).

## Le contrat B2 → B3 appliqué à Avengers

Le contrat B2 → B3 (cf. `b2-b3-jtbd-handoff-contract.md`) se déploie comme suit pour Avengers :

### Ce que Flash (B2 sponsor) promet

Pour chaque paquet JTBD Avengers :
- **Cadre d'exécution** : durée maximale du sprint B3 (semaines), squad Avengers ciblée, captain B2 sponsor (Flash lui-même)
- **Bornes DoD explicites** : seuils chiffrés (ex : *« taux de support Ops < 5 incidents/mois »*, *« NPS artefact ≥ 40 »*, *« marge brute ≥ 60% »*)
- **Preuves attendues par forme** : 1 ou 2 parmi capture/log/métrique/témoignage client

### Ce que le squad lead Avengers (CaptainAmerica) promet

- **Plan de livraison** : sprint d'exécution, dates de scrums intermédiaires, squad lead responsable
- **Lead indicators** : 1 à 3 métriques pendant l'exécution (ex : couverture tests, vélocité burndown)
- **Lag indicators** : 1 à 2 métriques après l'exécution (ex : NPS post-delivery, taux de churn)
- **Chemin d'escalade** : première remontée à Flash (captain sponsor), pas directement au Council

## Trois failure modes Avengers-spécifiques

Les trois failure modes du contrat B2 → B3 se déclinent pour Avengers :

### 1. Scope creep — l'élargissement silencieux

**Symptôme Avengers** : ScarletWitch produit un re-design de scope non demandé, « parce que le besoin client a évolué ». Le scope élargi est livré avec un proof path plus large que le JTBD packet.

**Détection** : la diff entre `jtbd_packet.received` et `jtbd_packet.delivered` est non vide.

**Remède** : Flash refuse la livraison excédentaire, consigne le scope creep dans le journal Council, et **réapprend** la discipline à CaptainAmerica (qui répercute à ScarletWitch).

### 2. Silent rework — la reprise non signalée

**Symptôme Avengers** : Hulk re-travaille la robustesse après la première livraison interne, sans escalader. Le proof path est conforme, mais le temps consommé a dépassé le cadre d'exécution.

**Détection** : le log d'exécution Avengers montre des commits de rework après la première livraison interne.

**Remède** : Flash ouvre un arbitrage *« rework non-escaladé »* en séance hebdomadaire.

### 3. Escalade tardive — le signal trop tardif

**Symptôme Avengers** : Hawkeye détecte une dérive métrique à J+2, ne signale pas, attend J+7 pour escalader.

**Détection** : le post-mortem Avengers mentionne un blocker connu mais non escaladé.

**Remède** : Flash exige un *« escalator register »* pour le sprint suivant (cf. `b2-b3-jtbd-handoff-contract.md` §« Escalade tardive »).

## Le rôle de CaptainAmerica comme squad lead

Le triplet v3 ligne 17 positionne CaptainAmerica comme **premier nommé** dans la liste Avengers. Par convention de la fiche roster B3 (cf. `fifty-three-b3-agent-roster.md`), le **premier agent nommé est le squad lead**. CaptainAmerica porte donc :

- La **tenue de scrums.md** du sprint Avengers (cf. triplet 8 — *« B3 produit SCRUMS.md et rien d'autre »*)
- Le **signalement des trous** à Flash (triplet 41 — *« B3 interdit-combler-trou »*)
- La **livraison de la preuve** dans l'une des 4 formes canoniques (cf. `b3-proof-path-4-formes.md`)
- La **double signature** du contrat B2 → B3 conjointement avec Flash

## Anti-pièges

- **Paquet JTBD émis sans scope formalisé.** Flash qui envoie un paquet JTBD aux Avengers avec un scope en prose est responsable du `NEEDS_SCOPE` en aval. Le scope doit être chiffré (heures, DoD, livrables nommés).
- **Avengers qui consomme un paquet sans contrat signé.** Un paquet JTBD Avengers sans `contract_signed` Flash + CaptainAmerica est un ordre, pas un contrat. Le scope creep est ouvert.
- **Gate Product émis sans lead indicators.** Flash qui émet `PRODUCT_READY` sans avoir vu les lead indicators (couverture tests, vélocité) rate la discipline de la double signature.
- **Confondre signal B2 → B3 et statut B3 → B2.** Le signal Flash est une **gate** (READY/NEEDS/BLOCKED) ; le statut Avengers est un **rapport d'exécution** (ON_TRACK/AT_RISK/BLOCKED/DONE). Le B2 sponsor émet le premier, le B3 squad émet le second.
- **CaptainAmerica qui escalade au Council sans passer par Flash.** L'escalade au Council sans passer par le B2 sponsor casse l'ordre vertical du fractal.

## Liens

- [[b2-b3-jtbd-handoff-contract]] — le contrat bilatéral B2 → B3
- [[b3-jtbd-packet-reception-checklist]] — la vue B3 du contrat
- [[b3-cycle-scrums-five-per-week]] — la cadence 5 scrums/semaine par agent
- [[b3-proof-path-4-formes]] — les 4 formes canoniques de preuve
- [[b3-veto-and-signal-vocabulary]] — les 8 gates et les 4 statuts
- [[flash-domain-perimeter]] — le périmètre du domaine Flash
- [[flash-pair-checks-dependencies]] — les pair-checks où Avengers est en interface
- [[flash-red-flag-1-trigger]] — la conséquence si Ops/IT sont rouges pendant que Product est vert
- [[eight-domain-avengers-wheel]] — le mapping Flash/Avengers

## Note de confiance

**Confirmé par machine, à moitié.** Le triplet v3 ligne 17 est cité verbatim (Avengers = 7 agents nommés). Les 3 signaux gates Flash sont verbatim `eight-domain-avengers-wheel.md`. Les 4 statuts B3 sont verbatim `b3-veto-and-signal-vocabulary.md`. La liste des 6 sources JTBD entrantes est **reconstruite** à partir de la matrice d'harmonisation (4 pair-checks impliquant Product) + 2 sources additionnelles (People onboarding, Ops handoff inverse). Le rôle CaptainAmerica comme squad lead est **projeté** à partir de la convention *« premier agent nommé = squad lead »* — pas explicitement posé ailleurs dans le corpus. La cadence 35 scrums/semaine est calculée (7×5), le calcul est trivial. Les 3 failure modes Avengers-spécifiques sont **reconstruits** à partir des 3 failure modes canoniques du contrat B2 → B3 — la spécialisation Avengers (ScarletWitch scope, Hulk robustesse, Hawkeye signal) est **projetée** à partir des noms canon Marvel.
