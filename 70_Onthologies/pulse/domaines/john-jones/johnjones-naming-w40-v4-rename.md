---
type: Concept
title: JohnJones — renommage W40 V4, living canon et cohérence cross-projet
description: Le captain B2 Sales est renommé MartianManhunter → JohnJones en W40 V4. Ownerbook T1 OMK cite ce renommage. Les nouveaux dossiers portent runent, les anciens conservent l'ancien nom. Conséquence opérationnelle : un arbitrage Council daté d'avant W40 V4 peut mentionner MartianManhunter ; un arbitrage post-W40 V4 doit dire JohnJones. Le concept, lui, ne change pas.
tags: [b2, johnjones, martian-manhunter, naming, w40-v4, living-canon, renommage, cross-projet]
generated: { by: minimax-m3, at: 2026-08-19T04:35:00Z }
verified:
  - { by: process:lecture-corpus-sales, at: 2026-08-19T04:35:00Z }
sources:
  - id: avengers-wheel-naming
    resource: "C:/Users/amado/ASpace_OS_V3/50_Distillation/projets/eight-domain-avengers-wheel.md"
    title: Eight Domain Avengers Wheel — Note sur la nomenclature Sales
    last_modified: 2026-08-17
  - id: triplet-18-martian
    resource: "C:/Users/amado/ASpace_OS_V3/70_Onthologies/triplets/v3-business.jsonl"
    title: "Triplet 18 — Martian Manhunter pairedWith Illuminati"
    last_modified: 2026-08-17
  - id: vp-agent-sales
    resource: "C:/Users/amado/ASpace_OS_V3/30_Business_OS/10_Projects/coach-os/04_Business_Domains/04_Sales_et_Cognition_MartianManhunter_Illuminati/VP_AGENT.md"
    title: VP_AGENT — Martian Manhunter (legacy) JohnJones (W40 V4)
    last_modified: 2026-08-02
okf_version: "0.2"
---

# JohnJones — renommage W40 V4

## Le signal canonique

`eight-domain-avengers-wheel.md` §« Note sur la nomenclature Sales »
cite verbatim l'Ownerbook T1 OMK :

> *« B2 Sales domain control room (note: legacy naming MartianManhunter,
> W40 V4 rename JohnJones) »*

Le verbe *« rename »* est l'information clé : un renommage, pas
une substitution. Le concept (B2 captain Sales, domaine 02,
Illuminati squad, veto reformulation-validée) ne change pas — seul
le nom du capitaine évolue.

## Pourquoi un renommage en W40 V4

Le triplet 18 cite verbatim *« Martian Manhunter pairedWith
Illuminati »* et la wheel 8-domain canonique aligne Sales sur
*« JohnJones (W40 V4) »* (cf. `eight-domain-avengers-wheel.md`
tableau mapping ligne 41). C'est un signal de **living canon** : la
nomenclature capitaine B2 évolue quand le canon W40 change.

`avengers-wheel` §« Note sur la nomenclature Sales » explicite :

> *« C'est un signal de living canon — la nomenclature B2 capitaine
> évolue quand le canon W40 change, et les nouveaux chartes/runbooks
> OMK portent le nouveau nom pendant que les anciens dossiers
> conservent l'ancien. »*

Hypothèses explicites sur la motivation du renommage (non étayées
par triplet canonique) :

- **Cohérence cross-projet** : le nom *MartianManhunter* est long
  et peut créer des collisions dans des paths de fichiers. *JohnJones*
  est plus court et reste dans le Marvel Multiverse (John Jones est
  le nom humain de Martian Manhunter dans Detective Comics).
- **Lecture méta** : John Jones est l'identité humaine secrète de
  Martian Manhunter. Le renommage explicite que **le captain est un
  humain qui opère sous une identité de superpower**, pas
  l'inverse.
- **V40 framing** : la W40 V4 introduit une nouvelle grille de
  lecture où les capitaines B2 sont des humains avec une charge
  cognitive, pas des superpowers désincarnés. Le renommage porte
  cette grille.

Le corpus **ne tranche pas** entre ces hypothèses. La lecture
prudente : un renommage cosmétique + canonique, sans changement de
périmètre.

## La situation cross-projet

Quatre projets utilisent la nomenclature B2 :

1. **Coach OS V3** — `04_Business_Domains/04_Sales_et_Cognition_MartianManhunter_Illuminati/`
   Le nom de dossier conserve *MartianManhunter*. Le `VP_AGENT.md`
   commence par *« AGENT — Martian Manhunter · VP Sales & Cognition »*.
2. **OMK Business OS** — la numérotation 02 n'apparaît pas dans
   les `B2_Business_Domains/` (seuls 03-08 sont présents — cf. supra).
   Le renommage est documenté dans l'Ownerbook T1 OMK.
3. **Eight-domain-avengers-wheel** — utilise *JohnJones* dans le
   tableau canonique 02 et la note de nomenclature.
4. **Triplets v3** — triplet 18 cite *Martian Manhunter pairedWith
   Illuminati*. Pas de renommage explicite dans le triplet.

**Trois projets utilisent MartianManhunter** (Coach OS V3, OMK,
triplets v3) et **un seul utilise JohnJones** (eight-domain wheel).
La migration est **incomplète**.

## Conséquence opérationnelle : datation des arbitrages

`avengers-wheel` §« Note sur la nomenclature Sales » pose la règle
de datation :

> *« un arbitrage Council daté d'avant W40 V4 peut mentionner
> MartianManhunter ; un arbitrage post-W40 V4 doit dire JohnJones.
> Le concept, lui, ne change pas. »*

Application concrète :

- **Avant W40 V4** : un packet mésoperpétuel mentionne *« Martian
  Manhunter a opposé son veto reformulation-non-validée sur la
  proposition X »*. Le packet est valide.
- **Post W40 V4** : un packet mésoperpétuel doit dire *« JohnJones
  a opposé son veto reformulation-non-validée sur la proposition X »*.
  Une mention de MartianManhunter seule (sans note *« legacy »*) est
  **non canonique**.
- **Cas de mixité** : un arbitrage qui cite un pré-W40-V4 packet
  mésoperpétuel doit **traduire** la mention en JohnJones, avec une
  note *« legacy MartianManhunter »* pour la traçabilité.

W40 V4 est une référence temporelle du canon — la date exacte n'est
pas dans le corpus visible. Une hypothèse raisonnable : V4 = version
4 du canon W40, où W40 est le cycle de référence (40ᵉ semaine
canonique Ownerbook T1). La date serait autour de 2026-W40
(septembre-octobre 2026).

## Le squad Illuminati et le renommage

Le squad Illuminati n'est **pas renommé** — c'est toujours
*Illuminati*. Conséquence : un arbitrage Council qui mentionne le
squad B3 dit *« Illuminati »*, et le captain est *« JohnJones »*
(post-W40 V4) ou *« MartianManhunter »* (legacy).

Le mapping cross-projet devient :

| | Captain B2 | Squad B3 |
|---|---|---|
| Coach OS V3 | MartianManhunter (dossier) | Illuminati |
| OMK (Ownerbook T1) | JohnJones (W40 V4) | Illuminati |
| Eight-domain wheel (canonique) | JohnJones | Illuminati |
| Triplets v3 | Martian Manhunter | Illuminati |

Trois projets utilisent un nom, un projet utilise l'autre. La wheel
canonique a tranché (JohnJones), mais la migration est **inachevée**
sur le disque.

## Anti-pièges

- **Citer MartianManhunter dans un arbitrage post-W40 V4 sans note
  legacy.** Le packet est non canonique.
- **Citer JohnJones dans un arbitrage pré-W40 V4.** Le packet est
  anachronique — W40 V4 n'était pas l'usage à l'époque.
- **Renommer le dossier Coach OS V3** (`04_Sales_et_Cognition_MartianManhunter_Illuminati/`)
  sans packet mésoperpétuel. Le renommage est cosmétique mais
  impacte les paths, les liens, les triplets. Sans Council, c'est
  une décision unilatérale.
- **Croire que le concept a changé.** Le périmètre, le veto, les
  pair-checks, les gates — tout est inchangé. Seul le nom du
  capitaine a bougé.

## Liens

- [[eight-domain-avengers-wheel]] — la wheel canonique qui tranche
  JohnJones
- [[b2-council-arbitrage-rule]] — datation des arbitrages Council
- [[johnjones-domaine-sales-perimetre]] — le périmètre inchangé
- [[johnjones-veto-reformulation-validee]] — le veto inchangé

## Note de confiance

**Confirmé par machine.** Le renommage W40 V4 est cité verbatim de
l'Ownerbook T1 OMK (via `eight-domain-avengers-wheel.md` §Note). La
règle de datation (avant/après W40 V4) est citée verbatim. La
migration inachevée est **observée** (Coach OS V3 dossiers
conservent MartianManhunter). Les hypothèses sur la motivation du
renommage sont **projetées** (cohérence cross-projet, lecture
méta, V40 framing) — non étayées par triplet canonique. La date
W40 V4 est **projetée** (2026-W40, septembre-octobre 2026) — non
explicitée dans le corpus visible.