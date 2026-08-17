---
type: Concept
title: Le vocabulaire d'agents a changé entre 2026-05 et 2026-08
description: En comparant les specs legacy (jusqu'au 2026-05-22) et l'état archivé/canonique (2026-08), le vocabulaire d'agents a été refondu : A'0 GravityClaw → A0 Amadeus, A'1 Rick → A1 Beth, A'2 Doctors → A2 Computer (Picard/Spock/Geordi), A3 Gemini CLI/IronClaw → A3 Data. Un projet RDF doit choisir quel vocabulaire porte l'URI canonique.
tags: [vocabulaire, agents, legacy, gravityclaw, amadeus, rick, beth, doctors, computer, data, gemini-cli, ironclaw, renommage]
generated: { by: minimax-m3, at: 2026-08-18T00:05:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-18T00:05:00Z }
sources:
  - id: sdd-v05
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/Legacy_LifeOS_App_Specs_2026-05-22/_SPECS/SDD-V0.5_SovereignConstitution.md"
    title: Frontmatter SDD V0.5 — auteur A'0 GravityClaw, architecte A'1 Rick/A'2 Doctors, exécutant A3 Gemini CLI/IronClaw
    last_modified: 2026-05-22
  - id: openclaw-legacy
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/03_OpenClaw_Body_Legacy/openclaw.json"
    title: openclaw.json (version 2026.2.1) — modèle primaire GPT-5.2 Codex + fallbacks Claude
    last_modified: 2026-03-01
  - id: a3-spec
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/A3_Data_Archives_Spec.md"
    title: A3_Data_Archives_Spec — Data = officier A3 PARA, vocabulaire actuel
    last_modified: 2026-06-21
  - id: adr-index
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/04_Archives_Data/_V3_STRUCTURE_2026-08-02/_SPECS/ADR/INDEX.md"
    title: INDEX ADR — ADRs actuels datent 2026-05-11 (RICK-001) à 2026-06-21 (SOBER-002)
    last_modified: 2026-06-21
okf_version: "0.2"
---

# Le vocabulaire d'agents a changé entre 2026-05 et 2026-08

## Les deux vocabulaires

### Legacy (jusqu'au 2026-05-22, figé dans `Legacy_LifeOS_App_Specs_2026-05-22/`)

Lecture directe du frontmatter du `SDD-V0.5_SovereignConstitution.md` :

| Niveau | Identifiant legacy | Identité |
|---|---|---|
| A'0 | GravityClaw | (l'auteur du SDD) |
| A'1 | Rick | (architecte ciblé) |
| A'2 | Doctors | (architecte ciblé, pluriel) |
| A3 | Gemini CLI / IronClaw | (exécutant ciblé) |

Notes :
- **Prime** sur A'0 et A'1/A'2 — une notation différente du niveau 0/1/2.
- **A2 pluriel** : « Doctors » (Docteurs), pas un seul agent.
- **A3** lié à des **produits** (Gemini CLI, IronClaw), pas à un rôle
  conceptuel.

### Actuel (à partir de 2026-06-21 environ, post-plan fancy-hugging-bengio)

| Niveau | Identifiant actuel | Identité |
|---|---|---|
| A0 | Amadeus | divinité / utilisateur (board observer) |
| A1 | Beth | (rédacteur Ikigai, par exemple) |
| A2 | Picard / Spock / Geordi / Holo-Janeway / Computer | 4 vaisseaux A2 nommés |
| A3 | Data | officier d'archives PARA |

Notes :
- A0 = Amadeus, **n'est pas un LLM** : c'est l'utilisateur (ou la
  divinité du système).
- A1 = Beth, **un seul** agent à ce niveau (Ikigai, etc.).
- A2 = **plusieurs agents nommés** (4+ navires thématiques de Star Trek).
- A3 = **Data**, un officier conceptuel (officier d'archives).

## Six mois de transition

La transition s'étale sur **février → août 2026** (6 mois), observable
via les artefacts datés :

| Date | Artefact | Vocabulaire |
|---|---|---|
| 2026-02-03 | `openclaw.json` wizard onboard | (pré-vocabulaire, OpenClaw runtime) |
| 2026-02-16 | OpenClaw `AGENTS.md` | (pré-vocabulaire) |
| 2026-05-11 | ADR-RICK-001 ratifié | (transition : RICK cité comme entité, pas comme A'1) |
| 2026-05-22 | Legacy specs scellés | **A'0/A'1/A'2/A3 legacy** (verrouillage) |
| 2026-06-08 | ADR-META-001 ACCEPTED | (canon actuel émerge) |
| 2026-06-21 | Patch A3 + ADR-SOBER-002 RATIFIED | **A0/A1/A2/A3 actuel** (verrouillage) |
| 2026-08-01 | Décision D-2026-08-01-#1 (Geordi racine unique) | (canon actuel) |
| 2026-08-02 | Versement V3 → Archives | (canon actuel) |

**Le 2026-05-22 est un sceau** : le legacy est figé dans
`Legacy_LifeOS_App_Specs_2026-05-22/`. Le 2026-06-21 est l'**émergence
verrouillée** du canon actuel.

## Pourquoi le vocabulaire a changé

**Hypothèse 1 — ré-ancrage Star Trek**. Le vocabulaire actuel utilise
nommément les officiers de Star Trek TNG (Picard, Spock, Geordi, Data).
L'ancien utilisait des « Doctors » pluriels (aussi Star Trek, mais
féminin pluriel) et des produits (Gemini CLI, IronClaw). L'ancrage
s'est resserré.

**Hypothèse 2 — maturité du modèle A0 = humain**. Le legacy traitait
A'0 comme un **produit** (GravityClaw). L'actuel traite A0 comme
**l'utilisateur** (Amadeus = persona, divinité board observer). C'est
un changement philosophique : la machine n'est plus au centre, l'humain
l'est.

**Hypothèse 3 — dissociation runtime / vocabulaire**. OpenClaw était
un **runtime** (avec son vocabulaire) ; Claude Code est un **autre
runtime** (avec un autre vocabulaire). Le vocabulaire suit le runtime.

**Le substrat ne tranche pas.** Trois hypothèses coexistent, plausibles
conjointement.

## Impact sur le graphe RDF

Pour chaque entité « agent » du graphe, le RDF doit décider :

1. **Quel vocabulaire porte l'URI canonique ?**
2. **Comment relier legacy ↔ actuel ?**

Proposition :

```turtle
<aspace:agent/gravityclaw> a aspace:Agent ;
    rdfs:label "A'0 GravityClaw"@fr ;
    aspace:legacyFor <aspace:agent/amadeus> ;
    aspace:vocabulary "legacy" ;
    prov:invalidatedAt "2026-06-21T00:00:00Z"^^xsd:dateTime .

<aspace:agent/amadeus> a aspace:Agent ;
    rdfs:label "A0 Amadeus"@fr ;
    aspace:replaces <aspace:agent/gravityclaw> ;
    aspace:vocabulary "current" ;
    aspace:role "board_observer" .
```

C'est un graphe où **les deux vocabulaires coexistent**, avec une
relation `aspace:replaces` qui marque la succession et un
`prov:invalidatedAt` qui marque la date de la succession.

## Concepts liés

- [[openclaw-body-legacy]] — le runtime d'avant la transition.
- [[legacy-lifeos-app-specs-evolution]] — les specs qui portent l'ancien vocabulaire.
- [[data-role-a3-archives-officer]] — le rôle A3 dans le vocabulaire actuel.
- [[archive-v3-structure-snapshot-2026-08-02]] — l'archive qui capture la transition.
