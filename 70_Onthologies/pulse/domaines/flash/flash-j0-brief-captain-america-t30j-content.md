---
type: Concept
title: Flash brief J+0 Captain America — contenu détaillé pour activer le programme T-30j
description: Brief J+0 que Captain America (squad lead Avengers, concept 22 vague 4) doit délivrer aux 7 agents Avengers pour activer le programme d'observation T-30j (concept 23 vague 4). 5 sections : 3 scénarios déclencheurs / 5 réflexes détection / 1 runbook Captain America / 1 gabarit fiche « mécanisme de reprise » / 1 calendrier consolidé J+0 → J+30. Sans ce brief, le programme T-30j reste saisissable mais non activé.
tags: [flash, product, j0-brief, captain-america, t-30j, programme-activation, observation-protocol, mechanism-reprise]
generated: { by: minimax-m3, at: 2026-08-19T11:30:00Z }
verified:
  - { by: process:synthese-escouade-flash-tour-5, at: 2026-08-19T11:30:00Z }
sources:
  - id: flash-veto-amplification-observation-protocole-T-30j
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-veto-amplification-observation-protocole-T-30j.md"
    title: Flash veto amplification — protocole d'observation T-30j (concept 23 vague 4)
    last_modified: 2026-08-19
  - id: flash-captain-america-roster-fiche-canon
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-captain-america-roster-fiche-canon.md"
    title: Captain America fiche roster canon YAML (concept 22 vague 4)
    last_modified: 2026-08-19
  - id: flash-veto-offre-depersonnalisee
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-veto-offre-depersonnalisee.md"
    title: Veto Flash — offre dépersonnalisée (concept 2 tour 1)
    last_modified: 2026-08-19
  - id: flash-veto-empirical-validation-protocol
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-veto-empirical-validation-protocol.md"
    title: Veto empirical validation protocol 3 cas/60j (concept 4 tour 2)
    last_modified: 2026-08-19
  - id: flash-amplification-mecanisme-reprise
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-amplification-mecanisme-reprise.md"
    title: Amplification mécanisme de reprise — draft libre (concept 1 tour 2)
    last_modified: 2026-08-19
  - id: triplet-25
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 25 — Flash hasVetoOver offre-depersonnalisee"
    last_modified: 2026-08-17
  - id: triplet-17
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 17 — Avengers 7 techniciens Captain America premier nommé"
    last_modified: 2026-08-17
  - id: b2-veto-amplification-cycle
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-veto-amplification-cycle.md"
    title: Amplification des vetos B2 — 3 conditions cumulatives
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Flash brief J+0 Captain America — contenu détaillé

## Le problème que ce brief ferme

Le programme T-30j (concept 23 vague 4) pose un **catalogue de détection** : 3 cas-limites observationnels (livraison Sopra-Sodia, onboarding consultant dédié, garantie produit ingénieur-dépendant). Mais le programme **ne démarre pas tout seul** — il faut un brief J+0 que Captain America délivre aux 7 agents Avengers pour leur dire : *« quoi chercher, comment le signaler, à qui, sous quel format »*.

Le rapport tour 3 (`RAPPORT_dom-flash.md` §3.5 vague 3) avait explicitement noté cette dépendance : *« sans brief J+0 = sans démarrage »*. Le rapport tour 4 a reconfirmé l'ouverture (cf. `RAPPORT_dom-flash.md` §5.4 vague 4 anti-pièges + ouverture 4).

Ce concept **ferme l'ouverture 4 vague 4** en proposant un brief J+0 détaillé, prêt à être délivré.

## Le brief J+0 Captain America — 5 sections

### Section 1 — Les 3 scénarios déclencheurs

> *« Pendant les 30 prochains jours, vous allez observer 3 types de situations. Une situation qui matche l'un des 3 = entrée dans `scrums.md` section blockers. »*

**Scénario 1 — Livraison Sopra-Sodia avec knowledge person-named**
Une promesse client (deal Sopra-Sodia signé — pair-check #1 Growth → Sales) où la **présence continue d'un consultant nommé** est dans la promesse (« Marie, votre consultante dédiée, vous accompagne 12 mois »). Sans mécanisme de reprise documenté, la valeur de l'offre dépend d'une personne nommée → veto Flash (triplet 25).

**Scénario 2 — Onboarding client avec consultant dédié non documenté**
Pendant l'onboarding (handoff Sales → Ops — pair-check #2), le consultant dédié au client **n'a pas de fiche de poste, pas de checklist de passation, pas de date de revue**. La dépendance person-named est **cachée dans l'opération**, pas dans la promesse commerciale.

**Scénario 3 — Garantie produit dépendante d'un ingénieur**
Une feature ship (pair-check #3 Product → Ops) inclut une **garantie client** qui dépend d'un **ingénieur nommé** sans procédure de rotation. Si l'ingénieur quitte, la garantie est en défaut.

> *« Pour chaque scénario, le test est : si l'opérateur principal (consultant, ingénieur) part demain, est-ce qu'un autre agent Avengers peut continuer sans formation spécifique ? Si non = dépendance person-named = veto Flash potentiel. »*

### Section 2 — Les 5 réflexes détection

> *« Quand vous observez un cas, suivez ces 5 réflexes dans l'ordre. »*

1. **Référence au deal** — noter l'identifiant du deal (pas le nom du client), pas le nom de la personne. Le brief anonymise par défaut (D4 append-only ne stocke pas de PII).
2. **Type de dépendance** — livraison / onboarding / garantie (1 mot-clé parmi les 3 scénarios).
3. **Présence de mécanisme de reprise** — oui (référence au runbook/transformation) / non (manquant).
4. **Format de l'entrée** — exactement : `[J+X] scenario=N, deal_id=<id>, type_person_named=<oui|non>, mechanism_reprise=<ref|manquant>`. Pas plus, pas moins. Le format permet à Captain America de consolider en revue quotidienne.
5. **Section `scrums.md`** — l'entrée va dans la section « blockers », pas dans une autre section. C'est l'unique section que Captain America lit en revue quotidienne.

### Section 3 — Le runbook Captain America

> *« En tant que squad lead, voici ma routine pour traiter vos entrées. »*

- **Revue quotidienne** : Captain America lit la section « blockers » de chaque agent Avengers (5 minutes / agent × 7 agents = 35 minutes).
- **Classification en E1/E2/E3** : si l'entrée matche scénario 1 = E1, scénario 2 = E2, scénario 3 = E3. Le `E` court pour « Escalation Flash », pas pour « Emergency ».
- **Cas E1** : Captain America escalade à Flash dans les **24h ouvrées** avec packet mésoperpétuel `B2-MESO-DECISION-YYYY-NN` (cf. concept 23 vague 4 procédure de signalement).
- **Cas E2** : Captain America escalade à Flash **avant** que l'onboarding soit complété (stade build). Si l'entrée signale un onboarding déjà complété = escalade rétroactive + revue post-mortem.
- **Cas E3** : Captain America escalade à Flash **ET** Aquaman (Legal) conjointement, format packet mésoperpétuel Flash avec co-signature Aquaman (le cas 3 touche la clause de garantie contractuelle, qui est du périmètre Legal).

### Section 4 — Le gabarit « mécanisme de reprise »

> *« Si le mécanisme de reprise existe (réflexe 3 = oui), voici le format de référence. »*

```yaml
mechanism_reprise:
  primary_operator: <id_pas_nom>
  backup_operators:
    - <id_1>
    - <id_2>
  rotation_trigger: "<X jours d'absence>"
  takeover_procedure: "<référence runbook section Y>"
  competence_equivalence: "<description des compétences équivalentes>"
  next_review: <YYYY-MM-DD>
```

> *« Si le gabarit n'est pas rempli pour le primary operator, le mécanisme est incomplet = veto Flash. »*

### Section 5 — Le calendrier consolidé J+0 → J+30

| Jour | Action | Owner | Output |
|---|---|---|---|
| **J+0** | Brief Captain America aux 7 agents Avengers (ce brief, 5 sections) | Captain America | Note de brief dans `scrums.md` section « program-t30j » |
| **J+1 à J+15** | Phase 1 — détection des 3 cas-limites dans les deals en cours | Avengers 7 | Entrées `scrums.md` section « blockers » |
| **J+15** | Checkpoint mi-parcours — Captain America consolide | Captain America | Rapport mi-parcours 1 page à Flash |
| **J+16 à J+30** | Phase 2 — escalade veto pour les cas confirmés | Captain America + Flash | 1 à 3 packets mésoperpétuels Flash |
| **J+30** | Bilan — packet B2-MESO-DECISION-2026-32 amendé avec cas observés | Captain America + Flash | Packet saisissable au Council avec condition 1 remplie |
| **J+30 + 7j** | Distribution packet amendé aux 8 capitaines | Flash | Packet Council-ready avec 7 jours de lecture |
| **J+30 + 14j** | Soumission Council (séance hebdomadaire ordinaire) | Flash + Council | Décision Council (adoption / rejet / escalate B1) |

> *« Le calendrier n'est pas négociable sauf cas de force majeure (perte d'un agent Avengers critique, par exemple). Le seuil J+30 est aligné sur le seuil T-30j parallèle Aquaman (cf. `aquaman-effectif-eternals-arbitrage.md`). »*

## Le lien avec les autres concepts Flash

- **Concept 23 vague 4** (`flash-veto-amplification-observation-protocole-T-30j`) : la matrice du programme (3 cas-limites, 5 critères acceptance, calendrier). Ce concept 26 **est l'application opérationnelle** : le brief Captain America qui active la matrice.
- **Concept 22 vague 4** (`flash-captain-america-roster-fiche-canon`) : Captain America comme owner du brief (responsabilité 1 + escalation E1 fiche canon).
- **Concept 5 tour 3** (`flash-veto-amplification-council-submission-draft`) : le packet `B2-MESO-DECISION-2026-32` saisissable que les cas observés doivent renforcer pour passer la condition 1 (observation documentée).
- **Concept 4 tour 2** (`flash-veto-empirical-validation-protocol`) : le protocole 3 cas/60 jours source, dont ce brief est l'application T-30 jours.
- **Concept 1 tour 2** (`flash-amplification-mecanisme-reprise`) : le draft libre source, dont ce brief opérationnalise le « mécanisme de reprise ».

## Anti-pièges

- **Brief J+0 sans calendrier** — un brief qui liste les 3 scénarios + 5 réflexes mais omet le calendrier ne démarre pas le programme. Le calendrier est ce qui contraint Captain America à checkpoint J+15.
- **Cas observés sur 1 seul scénario** — si les 3 entrées sont scénario 1, la distribution est insuffisante (1/3 scénarios). Captain America doit varier les sources.
- **Cas observé sans référence au deal** — sans `deal_id` ou `feature_id`, le cas n'est pas vérifiable. Le réflexe 1 (anonymisation) est non-négociable.
- **Mécanisme de reprise incomplet** — un mécanisme qui liste `backup_operators: [<id_1>]` sans `takeover_procedure` ou `competence_equivalence` est **incomplet**. Le veto Flash s'applique quand même.
- **Confondre E1/E2/E3 et « Emergency »** — le E1/E2/E3 désigne le scénario (1, 2 ou 3), pas un niveau d'urgence. Un cas E3 (garantie produit) peut être moins urgent qu'un cas E1 (livraison Sopra-Sodia).
- **J+0 sans section « program-t30j » dans `scrums.md`** — sans cette section, le brief est livré mais pas tracé. La trace permet de dater l'activation.

## Liens

- [[flash-veto-amplification-observation-protocole-T-30j]] — le programme T-30j matriciel (concept 23 vague 4)
- [[flash-captain-america-roster-fiche-canon]] — Captain America fiche roster (concept 22 vague 4)
- [[flash-veto-offre-depersonnalisee]] — le veto canonique (concept 2 tour 1)
- [[flash-veto-empirical-validation-protocol]] — protocole 3 cas/60j source (concept 4 tour 2)
- [[flash-veto-amplification-council-submission-draft]] — packet B2-MESO-DECISION-2026-32 saisissable (concept 5 tour 3)
- [[flash-amplification-mecanisme-reprise]] — draft libre source (concept 1 tour 2)
- [[b2-veto-amplification-cycle]] — la procédure 5/8 + D4 cible

## Note de confiance

**Confirmé par machine, brief saisissable.** Les 3 scénarios sont projetés à partir des pair-checks canoniques (#1 Growth → Sales, #2 Sales → Ops, #3 Product → Ops) — ce sont les 3 transitions où une dépendance person-named est la plus probable. Le calendrier T-30j + checkpoint J+15 sont parallèles au seuil Aquaman Issue A (cf. `aquaman-effectif-eternals-arbitrage.md`), sans validation canonique commune (signal d'asymétrie à noter pour le rapport tour 5). Les 5 réflexes détection sont **construits** à partir du triplet 25 + protocole empirique 3 cas/60j (concept 4 tour 2). Le runbook Captain America est cohérent avec la fiche roster canon YAML (concept 22 vague 4 responsabilité 1 + escalation E1). Le gabarit « mécanisme de reprise » est cohérent avec `flash-amplification-mecanisme-reprise.md` §« 4 conditions cumulatives ». **0 cas réel observé à date** — le brief est saisissable, l'activation dépend de Captain America qui le livre à J+0. Standing : brief Council-ready pour activation avant fin 12WY Q3 2026 (seuil T-30j = 2026-09-18).