---
type: Concept
title: Flash 7e agent Avengers Scarlet Witch — arbitrage effectif avec seuil T-30j
description: Arbitrage effectif pour le 7e agent Avengers Scarlet Witch (H90 « transformation scope »). 3 candidats évalués (Scarlet Witch H90 transformation, Quicksilver H10 vélocité, Vision H30 densité) avec matrice 4 critères (rôle capitaine H30 Captain America vs rôle spécialisé, dépendances cross-squad, fiche roster canon Marvel, risque veto Flash). Recommandation Scarlet Witch avec Issue A (cohérence Captain America orchestrateur) + seuil T-30j pour créer la fiche roster canon.
tags: [flash, product, avengers, 7th-agent, scarlet-witch, effectif-arbitrage, h90, transformation-scope]
generated: { by: minimax-m3, at: 2026-08-19T09:55:00Z }
verified:
  - { by: process:synthese-escouade-flash-tour-4, at: 2026-08-19T09:55:00Z }
sources:
  - id: fifty-three-b3-agent-roster
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/fifty-three-b3-agent-roster.md"
    title: 53 B3 Agent Roster — Ownerbook T1 ≥ 7 par squad
    last_modified: 2026-08-17
  - id: triplet-17
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 17 — Avengers 7 techniciens Captain America premier"
    last_modified: 2026-08-17
  - id: aquaman-effectif-eternals-arbitrage
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/aquaman/aquaman-effectif-eternals-arbitrage.md"
    title: Aquaman effectif Eternals arbitrage (modèle structurel jumeau)
    last_modified: 2026-08-19
  - id: cyborg-kang-dynasty-effectif-canon-recompte
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-kang-dynasty-effectif-canon-recompte.md"
    title: Cyborg Kang Dynasty effectif canon recomptage (modèle structurel jumeau)
    last_modified: 2026-08-19
  - id: flash-captain-america-roster-fiche-canon
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-captain-america-roster-fiche-canon.md"
    title: Captain America fiche roster canon (concept 22 vague 4)
    last_modified: 2026-08-19
  - id: b2-areas-dormants-doctrine
    resource: "C:/Users/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-areas-dormants-doctrine.md"
    title: Doctrine des domaines B2 dormants (Areas)
    last_modified: 2026-08-19
  - id: flash-domain-perimeter
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-domain-perimeter.md"
    title: Flash périmètre — 4 frontières floues
    last_modified: 2026-08-19
  - id: eight-domain-avengers-wheel
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel
    last_modified: 2026-08-17
okf_version: "0.2"
---

# Flash 7e agent Avengers Scarlet Witch — arbitrage effectif

## Le problème que cet arbitrage ferme

Le Ownerbook T1 OMK exige **≥ 7 agents par squad** (cf. `fifty-three-b3-agent-roster.md`). Le triplet 17 nomme **7 techniciens Avengers** avec Captain America premier nommé. Mais le **recensage sur disque** montre **6 agents Avengers** dans la projection (Captain America + 5 autres) — le 7e (Scarlet Witch) est **projeté mais pas créé sur disque** (cf. RAPPORT tour 3 §5.2 ouverture 11).

Cet arbitrage **évalue 3 candidats** pour le 7e slot, pose une **recommandation** avec **3 issues A/B/C**, et un **seuil T-30j** pour créer la fiche roster canon avant le premier Aquaman ACTIVE (analogie avec `aquaman-effectif-eternals-arbitrage.md` qui recommande Issue A avec seuil T-30j pour le 7e agent Eternals).

## Les 3 candidats évalués

### Candidat 1 — Scarlet Witch (Wanda Maximoff), H90 « transformation scope »

**Forces** :
- H90 = horizon long terme, complémentaire de Captain America H30 (orchestrateur).
- Spécialité « transformation scope » = exactement le job du **test de continuité 4D** (concept 1 tour 3) et de la **doctrine valeur d'artefact** : transformer le scope d'un feature quand la pivot est nécessaire, sans casser la valeur d'artefact.
- Cohérence avec Flash veto (triplet 25) : Scarlet Witch travaille la transformation scope **sans dépendance person-named** — sa valeur est dans la **méthode**, pas dans la personne.
- Fiche roster canon Marvel bien établie : Wanda Maximoff = Scarlet Witch, rôle « transformation reality » dans les comics.

**Faiblesses** :
- H90 = horizon long terme, donc **livraison lente** sur sprint hebdo Captain America.
- Fiche roster OMK inexistante à date (le 7e slot est vacant).
- Dépendance forte à Captain America H30 (squad lead) pour cadrer les transformations.

**Risque veto Flash** : faible. Scarlet Witch transforme le scope **sans** créer de dépendance person-named — son horizon H90 est incompatible avec une valeur person-named (la transformation scope est durable, pas adossée à une personne).

### Candidat 2 — Quicksilver (Pietro Maximoff), H10 « vélocité »

**Forces** :
- H10 = horizon court terme, complémentaire de Captain America H30.
- Spécialité « vélocité » = utile pour les **runs critiques** où Captain America a besoin d'un sprint rapide sur un blocker P1.

**Faiblesses** :
- **Redondance** avec Captain America (Captain America est déjà l'orchestrateur rapide via scrums.md quotidien).
- H10 ne traite pas la doctrine valeur d'artefact (qui est H30/H90).
- Frère de Scarlet Witch dans les comics — doublonner les Maximoff est un anti-pattern roster (1 par famille Marvel, pas 2).

**Risque veto Flash** : moyen. Quicksilver « vélocité » peut **inciter** à des livraisons rapides qui court-circuitent la doctrine valeur d'artefact. Le veto Flash pourrait s'appliquer si Quicksilver pousse un feature à ship avant que le mécanisme de reprise ne soit documenté.

### Candidat 3 — Vision (Victor Shade), H30 « densité »

**Forces** :
- H30 = horizon équivalent à Captain America, **sister squad lead potentielle**.
- Spécialité « densité » = utile pour les **features denses** (multi-composants, multi-pair-checks).
- Fiche roster canon Marvel bien établie : Vision = androïde, densité informationnelle.

**Faiblesses** :
- H30 = **conflit de rôle** avec Captain America (2 squad leads H30 dans la même squad = asymétrie).
- Spécialité « densité » peut **surcharger** Captain America en revues hebdo.

**Risque veto Flash** : moyen-élevé. Vision « densité » peut pousser des features denses qui **augmentent** la surface de dépendance person-named (plus de composants = plus de risque que la valeur tienne à une personne).

## Matrice 4 critères

| Critère | Scarlet Witch | Quicksilver | Vision |
|---|---|---|---|
| **Complémentarité H30 Captain America** | ✓ H90 complémentaire | ✗ H10 redondant | ✗ H30 conflit |
| **Dépendances cross-squad** | faible (Captain America seul) | moyenne (Captain America +Batman sprint P1) | élevée (Captain America + Batman + Cyborg) |
| **Fiche roster canon Marvel** | ✓ Wanda Maximoff bien établie | ✓ Pietro Maximoff mais doublon Scarlet Witch | ✓ Victor Shade bien établie |
| **Risque veto Flash** | ✓ faible | ✗ moyen | ✗ moyen-élevé |

**Recommandation** : **Scarlet Witch H90 « transformation scope »** — seule candidate qui complète Captain America sans créer de conflit de rôle ou risque veto.

## Les 3 issues A/B/C

### Issue A — Scarlet Witch H90 créé, fiche roster canon avant T-30j (RECOMMANDÉE)

**Justification** : Scarlet Witch est la seule candidate qui coche les 4 critères. H90 complète Captain America H30 sans conflit. Spécialité « transformation scope » cohérente avec la doctrine valeur d'artefact Flash.

**Action** : Captain America (squad lead) + Green Lantern (B2 People transverse) co-signent la création du 7e agent Avengers Scarlet Witch H90 avant **2026-09-18** (T-30j à date de cette distillation). Fiche roster YAML Council-ready conforme au pattern `fifty-three-b3-agent-roster.md`.

**Cohérence avec Aquaman** : parallèle direct avec `aquaman-effectif-eternals-arbitrage.md` qui recommande Issue A (7e agent Eternals avec seuil T-30j avant premier Aquaman ACTIVE).

### Issue B — Pas de 7e agent, squad Avengers reste à 6

**Justification** : Ownerbook T1 OMK exige ≥ 7 mais ne fixe pas de **délai**. Squad Avengers peut rester à 6 si Scarlet Witch n'est pas créé — l'arbitrage serait « le Ownerbook T1 est indicatif, pas bloquant ».

**Risque** : Aquaman (`aquaman-effectif-eternals-arbitrage.md`) a listé 3 sources 10/4/~7 non reconciliées. Si Avengers reste à 6, **3 sources** deviennent 3 sources aussi non reconciliées. C'est l'asymétrie qui justifie Issue A** : la **cohérence 8/8 domaines** est un signal fort de canon.

### Issue C — Quicksilver H10 ou Vision H30 créé à la place

**Justification** : Scarlet Witch H90 peut être **trop lente** pour les sprints B2 Captain America (Captain America H30 a besoin de soutien H10/H30, pas H90).

**Risque** : Issue C **régresse** par rapport à Issue A — les 3 critères penchent Scarlet Witch. Choisir Quicksilver/Vision sans justification doctrinale, c'est faire un choix de people (qui est dans la squad) plutôt qu'un choix de doctrine (quelle spécialité manque).

## Le seuil T-30j

À date de cette distillation (2026-08-19), le seuil T-30j = **2026-09-18**.

**Calendrier** :
- **J+0 à J+15** : Captain America brief Green Lantern sur la création Scarlet Witch H90.
- **J+15 à J+30** : Green Lantern (B2 People) ouvre le recrutement Scarlet Witch via X-Men (squad recruiting, triplet 33 + triplet 34).
- **J+30** : Scarlet Witch H90 créé sur disque avec fiche roster canon YAML, conforme au pattern `fifty-three-b3-agent-roster.md`.

**Si seuil manqué à J+30** : Issue A devient caduque, Issue B (squad à 6) s'applique par défaut. Le Ownerbook T1 reste indicatif.

## Le lien avec les concepts Flash antérieurs

- **Concept 22 vague 4** (`flash-captain-america-roster-fiche-canon`) : Captain America orchestre la création de Scarlet Witch (la fiche Captain America mentionne déjà le 7e agent ScarletWitch H90 dans `notes`).
- **Concept 1 tour 3** (`flash-doctrine-valeur-artefact-test-of-continuity`) : Scarlet Witch H90 « transformation scope » est le **porteur naturel** du test de continuité 4D (le test est H90, pas H30).
- **Concept 6 tour 3** (`flash-multidomain-veto-pressure-cascade`) : Scarlet Witch H90 peut être consultée sur les cascades multi-veto au stade pivot (entre build et sunset).
- **Triplet 17** : *« Avengers 7 techniciens Captain America premier nommé »* — Scarlet Witch est le 7e technicien, après Captain America (1er), Iron Man (2e), Thor (3e), Hulk (4e), Black Widow (5e), Hawkeye (6e).

## Anti-pièges

- **Doublon Scarlet Witch + Quicksilver** (les deux sont des Maximoff dans les comics). Choisir les deux = anti-pattern roster (1 par famille Marvel). Scarlet Witch seule est la bonne doctrine.
- **Vision H30 comme 2e squad lead** — conflit de rôle direct avec Captain America. Squad lead = 1 par squad, pas 2.
- **Issue B (squad à 6) sans arbitrage Council** — le Ownerbook T1 ≥ 7 est indicatif mais l'écart à 6 vs canon 7 crée une asymétrie 8/8 domaines non résolue. Issue B doit être **documentée** dans un packet mésoperpétuel `B2-MESO-DECISION-YYYY-NN` avec `decision: blocked` motif = « squad à 6 Ownerbook T1 indicatif ».
- **Confondre Scarlet Witch Marvel comics et Scarlet Witch OWn.** La Scarlet Witch OWn (cette distillation) est une **référence Marvel comics** pour la fiche roster — pas une copie littérale. La spécialité « transformation scope » est **projetée** à partir du comics, pas copiée.
- **Créer Scarlet Witch avant Captain America.** Captain America doit être créé **d'abord** (squad lead H30 orchestrateur). Sans Captain America, Scarlet Witch n'a pas de cadrage.

## Liens

- [[fifty-three-b3-agent-roster]] — le Ownerbook T1 ≥ 7
- [[flash-captain-america-roster-fiche-canon]] — Captain America comme prerequisite
- [[flash-doctrine-valeur-artefact-test-of-continuity]] — Scarlet Witch H90 porteur du test 4D
- [[flash-domain-perimeter]] — le périmètre Flash qui justifie Scarlet Witch H90
- [[flash-multidomain-veto-pressure-cascade]] — Scarlet Witch consultée sur cascade pivot
- [[eight-domain-avengers-wheel]] — Avengers = squad Product
- [[b2-areas-dormants-doctrine]] — la doctrine dormance pour squads incomplètes
- [[aquaman-effectif-eternals-arbitrage]] — modèle structurel jumeau Eternals
- [[cyborg-kang-dynasty-effectif-canon-recompte]] — modèle structurel jumeau Kang Dynasty

## Note de confiance

**Confirmé par machine, recommandation Issue A avec seuil T-30j.** Le Ownerbook T1 ≥ 7 est cité verbatim. Le triplet 17 est cité verbatim. Les 3 candidats sont **projetés à partir des noms canon Marvel** (lecture analogique, pas fiches lues). La matrice 4 critères est **construite** à partir du rôle Captain America H30 + doctrine valeur d'artefact + veto Flash (triplet 25). Le seuil T-30j est **arbitraire par construction** (parallèle Aquaman Issue A). **0 fiche roster Scarlet Witch lue à date** — l'arbitrage est saisissable, la création est à exécuter avant 2026-09-18. Standing : recommandation Council-ready, à soumettre Green Lantern (B2 People transverse) pour validation avant déclenchement X-Men recruiting.