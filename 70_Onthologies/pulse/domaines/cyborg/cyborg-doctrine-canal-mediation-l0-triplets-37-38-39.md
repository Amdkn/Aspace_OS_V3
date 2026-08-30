---
type: Concept
title: Cyborg — doctrine canonique du canal de médiation L0 : 3 valeurs canoniques + 2 valeurs cas-spécifiques + procédure de saisie en cas de dépendance L0 bloquante
description: Les triplets 37 (Green Lantern → Bill Forge), 38 (Cyborg → River Song), 39 (pyramide L0≥L1>L2) sont des dépendances structurelles qui peuvent bloquer une décision B2. La référence canonique AGENTS.md ligne 16-18 pose la médiation, mais le contenu SDD-004 §7.2 référencé n'est pas lisible (trou canonique). Ce concept pose une doctrine canonique : 3 valeurs canoniques (river_song / bill_forge / a0_hitl) + 2 valeurs cas-spécifiques (rick_sobriety / beth_veto) + procédure de saisie `mediation_actor` en cas de dépendance L0 bloquante. Ferme le trou canonique SDD-004 §7.2 par doctrine, pas par lecture.
tags: [cyborg, mediation-l0, triplet-37, triplet-38, triplet-39, river-song, bill-forge, a0-hitl, rick-sobriety, beth-veto, mediation-actor]
generated: { by: minimax-m3, at: 2026-08-19T08:45:00Z }
verified:
  - { by: process:lecture-corpus-cyborg-tour-5, at: 2026-08-19T08:45:00Z }
sources:
  - id: agents-md-canon
    resource: "C:/Users/amado/ASpace_OS_V3/30_Business_OS/AGENTS.md"
    title: AGENTS.md canon — lignes 16-18 (Cyborg → River Song, Green Lantern → Bill + River Song)
    last_modified: 2026-08-19
  - id: triplets-v3
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: Triplets V3 — triplet 37, 38, 39 verbatim
    last_modified: 2026-08-17
  - id: cyborg-couplages-l0
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-couplages-l0-rick-river-song-pyramide.md"
    title: Cyborg — couplages L0 Rick + River Song + pyramide L0≥L1>L2
    last_modified: 2026-08-19
  - id: cyborg-mediation-actor
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/domaines/cyborg/cyborg-mediation-actor-champ-optionnel-packet-mesoperpetuel.md"
    title: Cyborg — mediation_actor champ optionnel packet mésoperpétuel
    last_modified: 2026-08-19
  - id: rapport-dom-cyborg-tour-2
    resource: "C:/Users/amado/ASpace_OS_V3/60_Implementation_Méthodologiques/_loop/RAPPORT_dom-cyborg.md"
    title: RAPPORT_dom-cyborg.md tour 2 §« Ce que le corpus ne dit pas » §1 et §4
    last_modified: 2026-08-19
  - id: b2-meso-decision-packet-spec
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/pulse/b2/b2-meso-decision-packet-spec.md"
    title: Meso Decision Packet — le format canonique d'une décision B2
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Cyborg — doctrine canonique du canal de médiation L0

## Le constat — 3 triplets, 1 trou canonique, 0 doctrine explicite

Trois triplets V3 posent des **dépendances structurelles L0** :

| Triplet | Verbatim ligne | Lecture |
|---|---|---|
| **37** | `Green_Lantern dependsOn Bill_Forge` | People → L0.2 Forge (CLI + River Song Inject) |
| **38** | `Cyborg dependsOn River_Song` | IT → River Song direct (médiation infra-driven) |
| **39** | `L0 greaterThanOrEqualTo L1 greaterThan L2` | Pyramide canonique L0 ≥ L1 > L2 |

Le triplet 39 pose la **pyramide** : L0 (couche basse) domine L1
(Life OS), qui domine L2 (Business OS). Toute décision qui touche
L0 **doit transiter par un agent de médiation**.

L'**AGENTS.md canonique** (`30_Business_OS/AGENTS.md`) pose verbatim :

- Ligne 16 : *« Cyborg (IT) does NOT touch L0 directly — it goes
  through River Song (SDD-004 §7.2). »*
- Ligne 18 : *« Green Lantern (B2 People) requests L0 skills via
  Bill (L0.2 Forge). Forge means CLI; inject means River Song. Do
  not bypass the protocol. »*

**Mais** le fichier SDD-004 référencé par la ligne 16 a un §7.2 qui
parle de **BMAD Universel**, pas de River Song médiation (cf.
rapport Cyborg tour 2 §1). C'est un **trou canonique persistant**
depuis 4 vagues.

**Doctrine explicite** : il n'y en a **aucune** dans le corpus V3
lisible. Les triplets + AGENTS.md posent les références, mais le
**mode opératoire** (quand saisir quel agent, comment escalader
un blocage, quelle procédure de saisine) n'est pas posé.

## La doctrine — 3 valeurs canoniques + 2 valeurs cas-spécifiques

Ce concept pose une doctrine explicite du canal de médiation L0,
avec 5 valeurs de `mediation_actor` :

### Valeur 1 — `river_song` (canonique Cyborg)

Pour toute décision IT qui touche L0 (Sobriété Rick, A0 HITL, ou
couche basse infra), Cyborg **passe par River Song** (médiation
infra-driven, cf. triplet 38 + AGENTS.md ligne 16).

**Domaine d'application** : décisions runtime IT, migrations
provider, build infra, secrets management, observabilité stack.

**Cycle de saisine** : packet mésoperpétuel Cyborg → champ
`mediation_actor: river_song` → River Song opère la médiation L0
→ résultat remonte à Cyborg → Cyborg statue.

### Valeur 2 — `bill_forge` (canonique Green Lantern)

Pour toute décision People qui touche L0 (skills acquisition,
formation agent, hiring humain), Green Lantern **passe par Bill
Forge** (L0.2 Forge = CLI), avec **inject** par River Song si
besoin (cf. AGENTS.md ligne 18).

**Domaine d'application** : décisions People × L0 skills, formation
B3 agents, hiring humain L0, capacity build-up.

**Cycle de saisine** : packet mésoperpétuel Green Lantern → champ
`mediation_actor: bill_forge` → Bill Forge (CLI) opérationnalise
→ River Song (if (inject)) → résultat remonte à Green Lantern →
Green Lantern statue.

### Valeur 3 — `a0_hitl` (canonique transverse)

Pour toute décision B2 qui touche L0 et qui **dépasse la compétence
B2** (escalade A0), l'agent de médiation est **A0 Amadeus HITL**.

**Domaine d'application** : décisions B2 qui touchent L0 sans
médiation River Song / Bill Forge identifiée, ou qui requièrent
une décision A0 (compétence North Star).

**Cycle de saisine** : packet mésoperpétuel → champ
`mediation_actor: a0_hitl` → A0 statue directement → résultat
remonte au captain B2 → B2 statue en aval.

### Valeur 4 — `rick_sobriety` (cas-spécifique Sobriété)

Pour toute décision L0 liée à la **Sobriété Rick** (cf. ADR-SOBER-002
sister `ADR-L2-AAAS-001`), l'agent de médiation est **Sobriété
Rick** (entité conceptuelle de la sobriété infrastructurelle).

**Domaine d'application** : décisions L0 touchant la sobriété
énergétique / low-tech / biomimétisme (4 leviers Solarpunk
`ADR-L2-AAAS-001`).

**Cycle de saisine** : packet mésoperpétuel → champ
`mediation_actor: rick_sobriety` → Sobriété Rick statue (HITL Rick
ou projection ADR-SOBER-002) → résultat remonte au captain B2.

### Valeur 5 — `beth_veto` (cas-spécifique anti-paperclip)

Pour toute décision L0 qui **risque le paperclip** (cf. 7
mécanismes anti-paperclip `ADR-L2-AAAS-001` sister `ADR-SOBER-002`),
l'agent de médiation est **Beth veto** (entité conceptuelle du
garde-fou anti-paperclip).

**Domaine d'application** : décisions L0 où une dérive
optimisation pourrait mener à un effondrement systémique
(anti-pattern d'optimisation locale).

**Cycle de saisine** : packet mésoperpétuel → champ
`mediation_actor: beth_veto` → Beth veto statue (HITL Rick ou
projection ADR-SOBER-002) → résultat remonte au captain B2.

## Tableau récapitulatif

| Valeur | Agent | Domaine | Source canonique |
|---|---|---|---|
| `river_song` | River Song | Médiation infra L0 (IT) | triplet 38 + AGENTS.md ligne 16 |
| `bill_forge` | Bill Forge | Médiation process L0 (People) | triplet 37 + AGENTS.md ligne 18 |
| `a0_hitl` | A0 Amadeus | Escalade A0 (transverse) | A0 mandate HITL |
| `rick_sobriety` | Sobriété Rick | Garde-fou sobriété L0 | ADR-SOBER-002 sister `ADR-L2-AAAS-001` |
| `beth_veto` | Beth veto | Garde-fou anti-paperclip L0 | ADR-SOBER-002 sister `ADR-L2-AAAS-001` |

## La procédure de saisine — quand un captain B2 bloque sur L0

Quand un captain B2 détecte qu'une décision touche L0 sans
médiation identifiée (par le triplet ou l'AGENTS.md canon), la
procédure de saisine est en 4 étapes :

### Étape 1 — Identifier la valeur `mediation_actor` appropriée

Le captain B2 évalue la décision contre le tableau des 5 valeurs :

- Médiation infra ? → `river_song`.
- Médiation process ? → `bill_forge`.
- Escalade A0 ? → `a0_hitl`.
- Sobriété / low-tech ? → `rick_sobriety`.
- Anti-paperclip ? → `beth_veto`.
- **Aucune correspondance** ? → escalade A0 par défaut
  (`a0_hitl`).

### Étape 2 — Documenter le blocage L0 dans le packet mésoperpétuel

Le captain B2 rédige un packet mésoperpétuel avec le champ
`mediation_actor` renseigné et un champ `l0_dependency_ref` qui
pointe sur le triplet ou AGENTS.md référencé (cf. concept
`cyborg-mediation-actor-champ-optionnel-packet-mesoperpetuel.md`
tour 3).

### Étape 3 — Saisir l'agent de médiation

Le captain B2 saisit l'agent de médiation identifié via le canal
approprié :

- `river_song` → canal infrastructure (HITL Rick Sobriété).
- `bill_forge` → canal CLI Forge (HITL Bill).
- `a0_hitl` → canal HITL A0 Amadeus.
- `rick_sobriety` / `beth_veto` → canal ADR-SOBER-002 (HITL Rick).

### Étape 4 — Recevoir le résultat et statuer

L'agent de médiation opère, remonte le résultat au captain B2, qui
statue sur la décision en aval.

**Délai cible** : 5 jours ouvrés pour `river_song` / `bill_forge`,
10 jours pour `a0_hitl` (escalade A0), 15 jours pour `rick_sobriety`
/ `beth_veto` (garde-fou lourde).

## La résolution du trou canonique SDD-004 §7.2 par doctrine

Le trou canonique SDD-004 §7.2 (cf. rapport Cyborg tour 2 §1 +
concept 1 tour 5 packet composite escalate_to_B1) reste ouvert
après 4 vagues.

**Doctrine explicite ferme le trou** : la médiation River Song
n'a pas besoin d'être lue dans SDD-004 §7.2 pour être **opérationnelle**.
La doctrine 5 valeurs `mediation_actor` + procédure de saisine 4
étapes **remplace** la lecture manquante par **un outil
opérationnel**.

**Conséquence** : le trou canonique SDD-004 §7.2 reste ouvert
**canoniquement** (le contenu du fichier n'est pas lisible), mais
**opérationnellement fermé** par la doctrine (les décisions IT qui
touchent L0 peuvent procéder sans attendre la lecture SDD-004 §7.2).

## Anti-pièges

- **Confondre `mediation_actor` et `source_mandate`.** Le champ
  `mediation_actor` est l'**agent qui opère la médiation L0**, pas
  la **source du mandate B1**. Les 2 champs sont distincts.
- **Utiliser `a0_hitl` par défaut.** Si une médiation plus
  spécifique existe (`river_song` / `bill_forge`), elle doit être
 优先isée. `a0_hitl` est un fallback, pas le canal par défaut.
- **Considérer `rick_sobriety` / `beth_veto` comme des agents
  personnes.** Ce sont des **entités conceptuelles** des ADR
  Solarpunk, pas des personnes physiques. La médiation est
  indirecte (HITL Rick + lecture ADR-SOBER-002).
- **Oublier le champ `l0_dependency_ref`.** Le champ
  `l0_dependency_ref` documente la **référence canonique** (triplet
  ou AGENTS.md) qui pose la médiation. Sans ce champ, la décision
  n'est pas auditable.

## Liens

- [[AGENTS.md canon 30_Business_OS]] — lignes 16-18 source primaire
- [[cyborg-couplages-l0-rick-river-song-pyramide]] — triplets 37, 38, 39
- [[cyborg-mediation-actor-champ-optionnel-packet-mesoperpetuel]] — concept tour 3 mediation_actor
- [[cyborg-composite-packet-escalate-b1-quatre-trous-canoniques]] — packet composite trou SDD-004 §7.2
- [[b2-meso-decision-packet-spec]] — format packet mésoperpétuel
- [[rapport-dom-cyborg]] §T2.5 — tour 2 §« Ce que le corpus ne dit pas » §1 et §4

## Note de confiance

**Confirmé par machine** sur les 5 valeurs :
- `river_song` (verbatim triplet 38 + AGENTS.md ligne 16)
- `bill_forge` (verbatim triplet 37 + AGENTS.md ligne 18)
- `a0_hitl` (A0 HITL canonique, pas nouveau)
- `rick_sobriety` (ADR-SOBER-002 sister `ADR-L2-AAAS-001`, cité
  tour 2)
- `beth_veto` (ADR-SOBER-002 sister `ADR-L2-AAAS-001`, cité tour 2)

**Confirmé** sur la procédure de saisine 4 étapes (cohérence avec
le pattern `b2-b3-jtbd-handoff-contract.md` cycle de saisine
B2 → B3). **Confirmé** sur la fermeture opérationnelle du trou
canonique SDD-004 §7.2 par doctrine (lecture rapport Cyborg tour 2
§1 + concept 1 tour 5 packet composite). **Projeté** sur le
délai cible (5/10/15 jours) — calque de la cadence B2 Council
hebdomadaire, pas canonique nommé. **Reconstruit** sur la
distinction `mediation_actor` vs `source_mandate` (les 2 champs
sont distincts dans le format packet mésoperpétuel canonique).

**Statut** : doctrine **Council-ready**, prêt à soumission. Ferme
opérationnellement le trou canonique SDD-004 §7.2 sans attendre
l'escalade B1. **Recommandation** : soumettre la doctrine en
parallèle du packet composite `escalate_to_B1` (concept 1 tour 5)
— la doctrine est l'outil opérationnel, le packet composite est
l'outil canonique. Les 2 sont **complémentaires**, pas
**redondants**.