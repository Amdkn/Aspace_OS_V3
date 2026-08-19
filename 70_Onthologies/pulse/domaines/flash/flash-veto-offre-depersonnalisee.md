---
type: Concept
title: Veto Flash — l'offre dépersonnalisée, 5 cas légitimes, 3 cas abusifs
description: Le triplet v3 ligne 25 cite verbatim « Flash bloque toute offre dont la valeur dépend d'une personne nommée ». Le veto catalogue (cf. b2-eight-domain-vetoes-catalogue) protège contre l'enfermement client dans une relation nominative. Cinq cas de déclenchement légitimes (consultant clé, expert signature, single point of failure, fondateur irremplaçable, équipe de star), trois cas abusifs (refus d'embauche senior sous prétexte nominatif, refus d'un pilote client sans engagement, refus d'une co-construction), et la procédure d'application (vérification de la valeur, escalade B2 Council).
tags: [flash, product, veto, offre-depersonnalisee, valeur-artefact, escalation, b2-council]
generated: { by: minimax-m3, at: 2026-08-19T04:20:00Z }
verified:
  - { by: process:lecture-corpus-flash, at: 2026-08-19T04:20:00Z }
sources:
  - id: triplet-v3-line-25
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet v3 ligne 25 — Flash hasVetoOver offre-depersonnalisee"
    last_modified: 2026-08-17
  - id: vetoes-catalogue
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-eight-domain-vetoes-catalogue.md"
    title: Catalogue des 8 vetos B2 — propriétés catégoriel/vérifiable/non-négociable
    last_modified: 2026-08-19
  - id: org-json
    resource: "C:/Users/amado/ASpace_OS_V2/30_Business_OS/10_Projects/coach-os/ORG.json"
    title: Coach OS ORG.json — 8 vetos catalogue (verbatim)
    last_modified: 2026-08-02
  - id: b1-omk-t1-mandate
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b1/b1-omk-t1-mandate.md"
    title: B1 OMK T1 mandate — veto-offre-depersonnalisee (l. 61-62)
    last_modified: 2026-08-19
  - id: batman-doctrine
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/batman/batman-doctrine-remonte-fait-non-decision.md"
    title: Batman doctrine — Flash parle en valeur d'artefact (l. 100-103)
    last_modified: 2026-08-19
  - id: veto-amplification
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-veto-amplification-cycle.md"
    title: Amplification des vetos B2 — 3 conditions, procédure d'amendement D4
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Veto Flash — l'offre dépersonnalisée

## Le canon verbatim

Le triplet v3 ligne 25 cite verbatim :

> *« Flash bloque toute offre dont la valeur dépend d'une personne nommée. »*

Le B1 OMK T1 mandate (cf. `b1-omk-t1-mandate.md` §« 4 contraintes ») reformule :

> *« Aucune offre dont la valeur repose sur une personne nommée — la
> valeur doit survivre au remplacement de l'opérateur (veto Flash —
> triplet v3 ligne 25, doctrine veto-offre-depersonnalisee). »*

Batman, dans sa doctrine de contraste des quatre capitaines, décrit l'unité de parole de Flash :

> *« Flash parle en valeur d'artefact. Son veto s'applique aux offres
> dont la valeur dépend d'une personne nommée. Flash peut bloquer une
> offre sans escalader — c'est un fait "la valeur est nominative". »*
> — `batman-doctrine-remonte-fait-non-decision.md` §« Le contraste avec les autres doctrines »

Trois énoncés convergent : le veto catalogue **est** la doctrine veto-offre-depersonnalisée, et son motif est la **valeur d'artefact**. Le veto n'est pas un outil de pouvoir — c'est un **garde-fou contre l'enfermement client**.

## Pourquoi le veto existe — le risque d'enfermement

Une offre dont la valeur dépend d'une personne nommée produit **trois risques systémiques** :

1. **Risque de rétention opérateur.** Si l'opérateur quitte (démission, burnout, désaccord), l'offre **meurt avec lui**. Le client perd sa prestation, le fournisseur perd son revenu. Aucun mécanisme de reprise n'est prévu, parce que la valeur n'a jamais été formalisée.
2. **Risque d'extraction de rente.** Une fois le client dépendant de l'opérateur nommé, le fournisseur peut **augmenter le prix** sans concurrence possible (l'opérateur est irremplaçable à court terme). Le client paie la dépendance, pas la valeur.
3. **Risque de scaling impossible.** Une offre nominative **ne scale pas** : chaque nouveau client exige un nouvel opérateur nommé (même talent, même disponibilité, même tarification). Le coût marginal est élevé, le plafond de croissance est atteint rapidement.

Le veto catalogue pose la question inverse : *quand une offre est-elle en droit de se taire ?* — quand sa valeur n'a pas été formalisée.

## Cinq cas de déclenchement légitimes

Les cinq cas où le veto Flash **doit** s'opposer à un mandat B1, un arbitrage B2, ou une proposition B3 :

### Cas 1 — Consultant clé non-remplaçable

L'offre repose sur un consultant senior dont la valeur est explicitement nommée dans la proposition commerciale (signature, expertise personnelle, marque individuelle). Le mandat B1 ne prévoit pas de mécanisme de reprise (pas de partner, pas de squad back-up, pas de documentation de la méthode).

**Signal concret** : la proposition client cite *« coaching par Amadou Kone »* (et non *« coaching par l'équipe Coach OS »*), et le contrat n'inclut pas de clause de continuité.

### Cas 2 — Expert signature (thought leader)

L'offre est positionnée sur un thought leader dont le nom est la marque (ex : *« la méthode X de Y »*). Sans Y, la méthode n'a pas de valeur perçue par le marché.

**Signal concret** : le site web, les supports marketing, les contrats citent le nom de l'expert comme actif principal.

### Cas 3 — Single point of failure technique

L'offre repose sur un artefact technique (code, modèle algorithmique, infrastructure) que **seule une personne** sait maintenir. Si cette personne part, l'artefact devient inutilisable.

**Signal concret** : pas de documentation, pas de pair programming, pas de revue de code, dépendances critiques comprises par une seule personne.

### Cas 4 — Fondateur irremplaçable (early-stage)

L'offre early-stage repose sur la présence du fondateur dans la relation client (pitch, onboarding, escalation). Le fondateur **est** l'offre.

**Signal concret** : le fondateur est cité nommément dans tous les deals, sans processus de délégation de la relation client.

### Cas 5 — Équipe de star (collective single point)

L'offre repose sur une **équipe précise** (noms cités) plutôt que sur un rôle reproductible. Si un membre quitte, l'équipe perd sa valeur, même si chaque rôle individuellement est remplaçable.

**Signal concret** : la proposition cite *« l'équipe Amadou Kone / Marie Dupont / Pierre Martin »*, pas *« une équipe de trois coachs seniors »*.

## Trois cas abusifs — où le veto **ne devrait pas** s'opposer

Trois cas où le veto Flash peut être invoqué à tort, par erreur politique ou par excès de zèle :

### Cas abusif 1 — Refus d'embauche senior sous prétexte nominatif

Un capitaine B2 refuse l'embauche d'un expert senior sous prétexte que *« sa valeur est nominative »*. **C'est un abus** : la valeur de l'expert peut être **formalisée** (méthode, documentation, mentorat). Le veto porte sur l'**offre commercialisée**, pas sur l'**embauche**.

**Distinction canonique** : People (Green Lantern) tient le veto sur le recrutement sans mandat écrit + critère de sortie vérifiable (cf. `b3-veto-and-signal-vocabulary.md`). Flash ne statue pas sur la composition de la squad, sauf si la **valeur commercialisée** en dépend.

### Cas abusif 2 — Refus d'un pilote client sans engagement

Un capitaine B2 refuse un pilote client *« parce que c'est sur mesure »*. **C'est un abus** : un pilote est, par définition, une co-construction avec un client identifié. La valeur n'est **pas** nominative au sens du veto (le pilote ne crée pas une offre reproductible au catalogue).

**Distinction canonique** : le veto porte sur l'**offre au catalogue**, pas sur les pilotes de validation. Un pilote peut être nominatif tant qu'il ne devient pas une offre commercialisée à d'autres clients.

### Cas abusif 3 — Refus d'une co-construction interne

Un capitaine B2 refuse un travail conjoint entre Avengers parce que *« CaptainAmerica ne peut pas porter seul »*. **C'est un abus** : la co-construction produit une valeur d'équipe (qui peut être formalisée et reproduite), pas une valeur nominative.

**Distinction canonique** : le veto porte sur l'**offre** dont la valeur **dépend** d'une personne, pas sur le **travail** qui implique une personne. Un B3 CaptainAmerica peut porter un travail seul — c'est sa **reproductibilité** qui est en cause, pas sa **présence**.

## Les trois propriétés du veto (cf. b2-eight-domain-vetoes-catalogue)

Le veto Flash hérite des trois propriétés canoniques d'un veto légitime :

### 1. Catégoriel

Le veto porte sur une **classe** d'offres (les offres à valeur nominative), pas sur une offre individuelle. Flash peut bloquer *« toute offre à valeur nominative »*, pas *« cette offre »*.

Conséquence : si Flash oppose son veto sur un cas spécifique sans invoquer la classe, le veto est invalide. Le B2 Council peut passer outre.

### 2. Vérifiable

Le motif du veto est **écrit** dans le packet mésoperpétuel, le journal Council, ou `ORG.json`. Le motif doit être vérifiable **par un tiers qui n'est pas Flash**.

Forme canonique du motif :
> *« Offre {nom}, valeur portée par {personne nommée}, pas de mécanisme de reprise documenté dans le contrat. Cf. `contrat.pdf` page N, absence de clause de continuité. »*

Un veto Flash qui s'énonce *« cette offre me dérange »* n'est pas vérifiable. Le Council peut passer outre.

### 3. Non-négociable au niveau mésoperpétuel

Un capitaine B2 ne peut pas passer outre le veto Flash sans escalader B1. **Mais** le veto est levé par **amendement du mandat** (le demandeur ajoute un mécanisme de reprise) ou par **retrait du mandat** (B1 ou le porteur retire). L'issue la plus fréquente est l'amendement : 90% des vetos Flash sont levés par ajout d'une clause de continuité (partner back-up, documentation, squad de reprise).

## La procédure d'application — quatre étapes

### Étape 1 — Détection

Le veto se déclenche sur **détection** d'un des cinq cas légitimes. La détection peut être :
- **Examen de la proposition commerciale** (par CaptainAmerica ou Hawkeye lors de la pré-étude)
- **Revue de contrat** (par Aquaman Legal en transverse — mais le motif reste Flash)
- **Signal client** (réclamation sur dépendance)
- **Signal squad Avengers** (BlackWidow QA remonte une valeur nominative)

### Étape 2 — Documentation

Le motif est écrit dans un packet mésoperpétuel ou un ping Council pair. Format :
```
veto_id: B2-VETO-FLASH-YYYY-NN
captain: flash
classe: offre-depersonnalisee
motif: <cas légitime détecté>
source: <chemin proposition/contrat/observation>
```

### Étape 3 — Communication au porteur du mandat

Le porteur du mandat (B1 ou B2 commanditaire) est notifié. Le mandat est **suspendu** (pas exécuté B3 tant que le veto n'est pas levé).

### Étape 4 — Issue

Quatre issues possibles (cf. `b2-eight-domain-vetoes-catalogue.md` §« La règle de résolution quand un veto est opposé ») :
1. **Mandat amendé** (ajout mécanisme de reprise) — veto levé
2. **Mandat retiré** — veto tient, arbitrage clos avec `decision: blocked`
3. **Veto escaladé à B1** — pour réécriture de la règle catalogue (rare)
4. **Veto invalide** (manque une propriété) — Council passe outre

## Pourquoi Flash peut bloquer sans escalader (différence avec Batman)

Le triplet 57 cite Batman qui **escalade toujours** quand il oppose son veto (triplet 56-57). Flash, à l'inverse, **peut bloquer sans escalader** :

> *« Flash peut bloquer une offre sans escalader — c'est un fait
> "la valeur est nominative". »*
> — `batman-doctrine-remonte-fait-non-decision.md` §« Le contraste avec les autres doctrines »

La différence est dans la **catégorie de décision** :
- Batman statue sur la **condition d'arrêt d'une procédure** — c'est une décision de **cycle** (12WY, rock B1). Batman n'a pas ce mandat, donc il escalade.
- Flash statue sur la **valeur d'artefact** d'une **offre** — c'est une décision **opérationnelle** (commercialisation, scope). Flash a le mandat, donc il bloque.

Conséquence : un veto Flash **sans escalade** est légitime s'il est documenté et vérifiable. Un veto Batman **sans escalade** est invalide.

## Amplification candidate du veto Flash

Le triplet 58 ancre l'amplification Wonder Woman (dépense récurrente → métrique de retour chiffrée). Aucune amplification Flash n'est citée dans le triplet 58.

Trois amplifications candidates projetées pour le Council futur :

1. **Mécanisme de reprise documenté** — l'offre doit non seulement ne pas dépendre d'une personne, mais aussi **documenter explicitement** le mécanisme de reprise (partner, squad, documentation). Plus strict que le veto canonique.
2. **Continuité mesurée** — un test de continuité (l'opérateur part 30 jours, l'offre reste fonctionnelle) doit être passé avant commercialisation. Plus opérationnel que le veto canonique.
3. **Clause de transition client** — en cas de départ opérateur, le client a droit à une **transition gratuite** de 30 jours vers le remplaçant. Plus client-centric que le veto canonique.

Les trois sont **projetées** — le triplet 58 ne les ancre pas. Une amplification Flash doit être soumise à majorité simple 5/8 du Council (cf. `b2-veto-amplification-cycle.md` §« La procédure d'amendement »).

## Anti-pièges

- **Veto utilisé comme outil anti-personnalisation abusive.** Le veto porte sur l'**offre commercialisée**, pas sur l'**expérience client**. Un client pilote peut avoir une expérience sur mesure tant que l'offre reproductible reste dépersonnalisée.
- **Veto opposé puis levé sans amendement.** Si le veto est levé sans amendement visible du mandat, c'est un veto qui n'a pas servi. Le packet doit documenter l'amendement.
- **Confondre veto catalogue et refus individuel.** Un capitaine qui refuse systématiquement les propositions de valeur forte sans invoquer la classe rend le catalogue ineffectif.
- **Veto sans test de continuité.** Un veto Flash qui se base uniquement sur l'observation (*« cette offre me semble nominative »*) sans proposer un test vérifiable (*« si l'opérateur part, l'offre tient-elle ? »*) n'est pas vérifiable.

## Liens

- [[b2-eight-domain-vetoes-catalogue]] — les 8 vetos et leurs 3 propriétés
- [[b2-council-arbitrage-rule]] — qui tient le Council et arbitre les vetos
- [[b2-veto-amplification-cycle]] — l'amplification potentielle du veto Flash
- [[flash-domain-perimeter]] — le périmètre où s'applique le veto
- [[flash-doctrine-valeur-artefact]] — pourquoi le veto porte sur la valeur d'artefact
- [[flash-pair-checks-dependencies]] — les pair-checks où le veto peut se déclencher
- [[b1-omk-t1-mandate]] — le mandat B1 qui cite verbatim la doctrine
- [[batman-doctrine-remonte-fait-non-decision]] — le contraste Flash/Batman sur l'escalade

## Note de confiance

**Confirmé par machine.** Le triplet v3 ligne 25, le triplet v3 ligne 17 (source Coach OS), le B1 OMK T1 mandate §« 4 contraintes » (l. 61-62), et `batman-doctrine-remonte-fait-non-decision.md` §« Le contraste avec les autres doctrines » (l. 100-103) sont cités verbatim et convergent. Les cinq cas légitimes sont **projetés** à partir de la doctrine de valeur d'artefact et de la pratique observée (consultant clé, expert signature, SPOF, fondateur irremplaçable, équipe de star). Les trois cas abusifs sont **reconstruits** à partir du risque d'instrumentalisation politique d'un veto catégorie. La procédure d'application en 4 étapes est **empruntée** au pattern veto canonique de `b2-eight-domain-vetoes-catalogue.md`. La distinction Flash-bloque-sans-escalader / Batman-escalade-toujours est **reconstruite** à partir des triplets 56-57 et de la doctrine de Batman — assumée comme projection logique.
