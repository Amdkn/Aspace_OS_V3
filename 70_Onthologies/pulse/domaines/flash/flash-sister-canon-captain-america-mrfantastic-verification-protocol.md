---
type: Concept
title: Flash sister canon Captain America / MrFantastic — protocole vérification croisée avec Batman
description: Protocole de vérification croisée Avengers↔Fantastic4 pour confirmer que Captain America (Avengers H30 orchestrateur Product) et MrFantastic (Fantastic4 H30 orchestrateur Ops) sont des sister canon légitimes — pas des doublons. 4 critères distinctifs + 3 cas de confusion + procédure coordination Batman (B2 Ops, captain sponsor sister squad) + lien avec pair-check #3 Product → Ops (cadre canonique de leur interaction).
tags: [flash, product, sister-canon, captain-america, mrfantastic, avengers, fantastic-four, ops, batman, verification-protocol]
generated: { by: minimax-m3, at: 2026-08-19T11:35:00Z }
verified:
  - { by: process:synthese-escouade-flash-tour-5, at: 2026-08-19T11:35:00Z }
sources:
  - id: flash-captain-america-roster-fiche-canon
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-captain-america-roster-fiche-canon.md"
    title: Captain America fiche roster canon YAML (concept 22 vague 4)
    last_modified: 2026-08-19
  - id: flash-squad-lead-captain-america-mandate
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-squad-lead-captain-america-mandate.md"
    title: Flash squad lead Captain America mandate (concept 4 tour 3)
    last_modified: 2026-08-19
  - id: flash-triple-squad-launch-canon-protocol
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-triple-squad-launch-canon-protocol.md"
    title: Flash triple-squad launch canon protocol (concept 3 tour 2)
    last_modified: 2026-08-19
  - id: flash-pair-checks-dependencies
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-pair-checks-dependencies.md"
    title: Flash pair-checks dépendances (concept 4 tour 1)
    last_modified: 2026-08-19
  - id: flash-red-flag-1-trigger
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/flash/flash-red-flag-1-trigger.md"
    title: Flash red flag #1 (concept 5 tour 1)
    last_modified: 2026-08-19
  - id: batman-domain-perimeter
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-domain-perimeter.md"
    title: Batman périmètre Ops — sister canon Fantastic4 (concept 1 tour 1)
    last_modified: 2026-08-19
  - id: triplet-17
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 17 — Avengers 7 techniciens Captain America premier nommé"
    last_modified: 2026-08-17
  - id: triplet-8
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 8 — B3 produit SCRUMS.md et rien d'autre, interdit rock et sprint"
    last_modified: 2026-08-17
  - id: triplet-41
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 41 — B3 interdit-combler-trou"
    last_modified: 2026-08-17
  - id: b2-pair-check-raci-by-rank
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-pair-check-raci-by-rank.md"
    title: RACI par rang — A = B2 en aval
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Flash sister canon Captain America / MrFantastic — protocole de vérification croisée

## Le problème que ce protocole ferme

La fiche roster canon YAML de Captain America (concept 22 vague 4) pose une **distinction structurelle** Captain America (Avengers, Product, H30 orchestrateur) vs MrFantastic (Fantastic4, Ops, H30 orchestrateur). Mais cette distinction est **non Council-vérifiée** car la fiche MrFantastic n'a pas été lue directement par l'escouade Flash.

Le rapport tour 4 (`RAPPORT_dom-flash.md` §5.4 anti-pièges vague 4 + ouverture 2) recommande explicitement *« coordination avec Batman pour lecture fiche MrFantastic »*. Ce concept **formalise cette coordination** en protocole reproductible.

## Pourquoi la vérification est nécessaire

Quatre raisons canoniques rendent la vérification obligatoire :

1. **Sister canon non lue = projection** — la fiche MrFantastic est lue par projection depuis le nom canon Marvel (Reed Richards = MrFantastic) et depuis la structure 4 fichiers OMK (cf. `fifty-three-b3-agent-roster.md` §« Le pattern de la fiche roster »). Sans lecture directe, Captain America/MrFantastic pourraient être lus comme des doublons structurels (2 squad leads H30 orchestrateurs), ce qui serait une erreur canonique.

2. **Pair-check #3 Product → Ops dépend de la distinction** — la matrice d'harmonisation pose A = B2 Ops (Batman) sur pair-check #3 (Product → Ops). Si Captain America et MrFantastic sont lus comme des squad leads interchangeables, le RACI par rang perd sa spécificité. La distinction captain-en-amont / captain-en-aval repose sur la **complémentarité** Captain America (H30 Avengers, scrums.md quotidien) + MrFantastic (H30 Fantastic4, runbook Ops).

3. **Triple-squad launch canon protocol (concept 3 tour 2)** — la chaîne Avengers → Fantastic4 → Kang-Dynasty (Product → Ops → IT) ne fonctionne que si Captain America (Amont) et MrFantastic (Aval) ont des mandats **distincts**. Sans vérification, la chaîne devient un doublon de squad lead.

4. **Asymétrie orchestrateur Product vs orchestrateur Ops** — Captain America orchestre la **construction** (build — pair-check #3 entrant, #4 sortant). MrFantastic orchestre la **maintenance** (run — pair-check #3 entrant côté Ops, #2 sortant côté Sales). Les deux horizons sont H30 mais les **objets** diffèrent (artefact vs boucle de run).

## Les 4 critères distinctifs Captain America / MrFantastic

| Critère | Captain America (Avengers, Product) | MrFantastic (Fantastic4, Ops) |
|---|---|---|
| **Domaine B2** | Flash (Product, 03) | Batman (Ops, 04) |
| **Triple-squad chain** | Amont — déclenche le pair-check #3 entrant | Aval — reçoit le pair-check #3 entrant |
| **Type d'orchestration** | Construction d'artefact (build, sprint hebdo Captain America) | Maintenance de boucle (run, runbook Ops continu) |
| **Outputs canoniques** | `scrums.md` quotidien, packet mésoperpétuel quand veto Flash | `runbook.md` continu, SOP standardisée, escalade Batman condition d'arrêt |

> *« Ces 4 critères sont lus par projection depuis le canon Marvel + Ownerbook T1 + structure 4 fichiers OMK. La vérification croisée avec Batman doit confirmer que la fiche MrFantastic respecte la colonne 3 (runbook, SOP, escalade Batman), pas la colonne 2 (scrums.md, packet mésoperpétuel). »*

## Les 3 cas de confusion à éviter

### Confusion 1 — Lire Captain America comme MrFantastic (et inversement)

**Symptôme** : Captain America commence à tenir un `runbook.md` (objet de MrFantastic) OU MrFantastic commence à tenir un `scrums.md` quotidien (objet de Captain America).

**Détection** : Batman (B2 Ops) détecte une dérive d'output dans la chaîne triple-squad — un livrable Avengers qui ressemble à un livrable Fantastic4, ou inversement.

**Remède** : Batman remonte le **fait** (cf. triplets 56/57 : *« Batman remonte à Summers des faits, pas des décisions »*) à Flash, qui arbitre en B2 Product. La distinction des outputs est un fait, pas une décision Captain America.

### Confusion 2 — Confondre les pair-checks (#3 vs #2)

**Symptôme** : un Captain America pense que pair-check #3 Product → Ops == pair-check #2 Sales → Ops (deux handoffs Ops). Mais le #2 est **Sales → Ops** (Batman aval, Illuminati amont), le #3 est **Product → Ops** (Batman aval, Avengers amont). Ce sont deux pair-checks distincts avec deux captains sponsor amont différents.

**Détection** : Batman (B2 Ops) tient les 2 pair-checks. Si un packet mésoperpétuel Avengers cite le #2 sans citer le #3, Batman détecte la confusion.

**Remède** : Batman vérifie la **référence au pair-check** dans chaque packet Avengers avant signature. Si confusion, Batman refuse le packet et demande correction.

### Confusion 3 — Doublonner le squad lead H30

**Symptôme** : Captain America et MrFantastic sont lus comme **2 squad leads interchangeables** (H30 orchestrateur chacun), ce qui ferait **2 Avengers-grade** dans 2 squads différentes. Le Ownerbook T1 attend **7 agents par squad** (cf. `fifty-three-b3-agent-roster.md`). Si Captain America est le squad lead Avengers et MrFantastic est le squad lead Fantastic4, il n'y a pas doublon — les 2 squads sont distinctes (Product vs Ops).

**Détection** : Captain America et MrFantastic opèrent dans des squads différentes (Avengers vs Fantastic4) — pas un doublon canonique.

**Remède** : la distinction est **structurelle** (2 squads Marvel distinctes), pas personnelle. Batman confirme que MrFantastic est bien le squad lead Fantastic4 dans le roster file OMK, pas un Avengers bis.

## La procédure de coordination Batman (B2 Ops, captain sponsor sister squad)

1. **Flash envoie à Batman** la demande de lecture croisée de la fiche MrFantastic avec ce protocole en annexe.
2. **Batman lit la fiche MrFantastic** dans `B2_Business_Domains/04_Ops_Batman_Fantastic4/01_B3_AGENT_ROSTER.md` (ou l'équivalent Coach OS / Notion / Jerry).
3. **Batman compare** aux 4 critères distinctifs et aux 3 confusions à éviter.
4. **Batman remplit** le gabarit de vérification ci-dessous et le renvoie à Flash.
5. **Flash intègre** le résultat dans le rapport Flash (vague 5 ou suivante) et **statue** sur la sister canon : confirmée / à corriger / à débattre en Council.

### Le gabarit de vérification Batman

```yaml
verification_sister_canon:
  date: <YYYY-MM-DD>
  verified_by: <Batman ou VP_AGENT.md Batman>
  fiche_mrfantastic_lue: <path complet>
  critere_1_domaine_b2:
    captain_squad_lead: <Batman, Flash, autre?>
    conformite: <oui|non>
  critere_2_triple_squad_chain:
    role_mrfantastic: <amont_ou_aval>
    conformite: <oui|non>
  critere_3_type_orchestration:
    objet_principal: <build|run|autre>
    conformite: <oui|non>
  critere_4_outputs_canoniques:
    outputs_produits: <liste>
    conformite: <oui|non>
  confusions_detectees:
    confusion_1: <oui|non, detail>
    confusion_2: <oui|non, detail>
    confusion_3: <oui|non, detail>
  statut: <confirmee|a_corriger|a_debattre_council>
  notes: <libre>
```

## Le lien avec les autres concepts Flash

- **Concept 22 vague 4** (`flash-captain-america-roster-fiche-canon`) : Captain America dont la sister canon est projetée. Ce protocole **vérifie** la projection.
- **Concept 4 tour 3** (`flash-squad-lead-captain-america-mandate`) : le mandat Captain America source — la sister canon y est mentionnée mais pas vérifiée.
- **Concept 3 tour 2** (`flash-triple-squad-launch-canon-protocol`) : la chaîne Avengers → Fantastic4 → Kang-Dynasty qui repose sur Captain America / MrFantastic distincts.
- **Concept 4 tour 1** (`flash-pair-checks-dependencies`) : les 4 pair-checks canoniques Flash — la sœur canon Captain America/MrFantastic valide les pair-checks #3 et #4.
- **Concept 5 tour 1** (`flash-red-flag-1-trigger`) : red flag #1 (Product green / Ops IT red) qui ne se déclenche que si la chaîne triple-squad est fonctionnelle.

## Anti-pièges

- **Lire MrFantastic par projection Marvel** — Reed Richards = MrFantastic est connu, mais la fiche canon OMK peut diverger. Le protocole exige la lecture du roster file, pas la projection.
- **Confondre sister canon et doublon** — 2 squad leads H30 dans 2 squads différentes ≠ doublon. La distinction Avengers/Fantastic4 est canonique.
- **Batman qui refuse de lire** — Batman n'a pas l'autorité de refuser la coordination (c'est un fait, pas une décision — triplets 56/57). Le protocole est une demande de vérification factuelle.
- **Sister canon confirmée sans lecture MrFantastic** — la confirmation sans lecture = projection. Le protocole exige le gabarit rempli.
- **Confondre Captain America et Scarlet Witch** — Captain America est le squad lead Avengers (H30 orchestrateur), Scarlet Witch est le 7e agent H90 transformation scope (concept 25 vague 4). Ils sont **distincts** dans la squad Avengers.

## Liens

- [[flash-captain-america-roster-fiche-canon]] — Captain America fiche roster canon (concept 22 vague 4)
- [[flash-squad-lead-captain-america-mandate]] — Captain America mandat (concept 4 tour 3)
- [[flash-triple-squad-launch-canon-protocol]] — chaîne triple-squad (concept 3 tour 2)
- [[flash-pair-checks-dependencies]] — pair-checks canoniques Flash (concept 4 tour 1)
- [[flash-red-flag-1-trigger]] — red flag #1 (concept 5 tour 1)
- [[batman-domain-perimeter]] — Batman périmètre Ops sister canon (concept 1 tour 1)
- [[b2-pair-check-raci-by-rank]] — RACI par rang (cadre théorique)
- [[triplets-v3-ligne-17]] — Avengers 7 techniciens Captain America premier nommé

## Note de confiance

**Confirmé par machine, protocole saisissable.** Les 4 critères distinctifs sont **projetés** depuis le canon Marvel + Ownerbook T1 + structure 4 fichiers OMK + pair-checks #2/#3/#4 canoniques. Les 3 confusions à éviter sont **construits** à partir des pair-checks canoniques (Captain America ne signe pas de runbook, MrFantastic ne tient pas de scrums.md quotidien — la séparation est une **garantie structurelle**, pas un interdit explicite). La procédure de coordination Batman est **cohérente avec les triplets 56/57** (Batman remonte des faits, pas des décisions). **0 lecture directe de la fiche MrFantastic à date** — le protocole est saisissable, l'activation dépend de Flash qui envoie la demande à Batman et Batman qui lit la fiche dans le roster file OMK. Standing : protocole de vérification Council-ready pour activation par simple demande Flash → Batman, sans séance Council.