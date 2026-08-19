---
type: Concept
title: Collision SDD-006 — Business Pulse vs Définition DEAL H1 Isaac
description: Deux documents distincts portent simultanément le numéro SDD-006 : (a) la Pyramide L2 Business Pulse (vivante, amendée 2026-08-19) et (b) la Définition DEAL du H1 Isaac Curie (sous 04_From_V2_Root/_SPECS/SDD/). Le numéro devient ambigu dans toute citation.
tags: [sdd, collision, sdd-006, business-pulse, deal, isaac, curie, 12wy, ambiguite]
generated: { by: minimax-m3, at: 2026-08-19T14:45:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-19T14:45:00Z }
sources:
  - id: sdd-006-business-pulse
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-006_business-pulse-l2-pyramide.md"
    title: SDD-006 Business Pulse L2 Pyramide (lu — amendement 001)
    last_modified: 2026-08-19
  - id: sdd-006-deal-isaac
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/04_From_V2_Root/_SPECS/SDD/SDD-006_definition-deal-h1-isaac-12wy-curie.md"
    title: SDD-006 Définition DEAL du H1 Isaac (lu — 2026-07-12 scellé)
    last_modified: 2026-07-12
  - id: amendement-001-verbatim
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-006_business-pulse-l2-pyramide.md (lignes 1158-1185)"
    title: AMENDEMENT 001 — le 8e domaine : Sales (verbatim)
    last_modified: 2026-08-19
okf_version: "0.2"
---

# Collision SDD-006 — Business Pulse vs Définition DEAL H1 Isaac

## Le constat

Deux documents distincts partagent le numéro **SDD-006** sur le disque :

| Document | Chemin | Auteur · Date | Nature |
|---|---|---|---|
| **SDD-006 Business Pulse L2 Pyramide** | `05_From_V2_Domains/10_Tech_OS/12_Blueprints/01-SDD/SDD-006_business-pulse-l2-pyramide.md` | A0 (Claude Code — Rick Prime) · 2026-04-26 | Architecture L2 — Pyramide Jerry/Summer/DC/Marvel |
| **SDD-006 Définition DEAL H1 Isaac + 12WY Curie** | `04_From_V2_Root/_SPECS/SDD/SDD-006_definition-deal-h1-isaac-12wy-curie.md` | A+ verbatim 2026-07-12 23:59 | Protocole DEAL (D·E·A·L) + cadence 12WY |

## Verdict sur les deux

- **SDD-006 Business Pulse** : `synthese-datee` (amendé le 2026-08-19 —
  cf. [[concept-amendement-001-8e-domaine]]). Le corps reste canon
  pour la pyramide L2 ; le décompte « 7 domaines » est obsolète (8
  avec John Jones / Martian Manhunter / Sales).
- **SDD-006 Définition DEAL H1 Isaac** : `canon`. Verbatim A+ scellé
  le 2026-07-12, ACTIF selon la Constitution Article 5. Sister : SDD-001
  (matrice frameworks), W36 (loops self-évolutifs), ADR-L2-TRIPTYQUE-V3-001.

## Pourquoi c'est un problème

Le numéro sert de référence canonique dans le triplet
`supersedes`. Deux documents sous le même numéro rendent toute
citation **ambiguë** :

> « Selon SDD-006, le Jerry Prime gère LD01+LD02. »
> → S'agit-il du Business Pulse (qui ne mentionne pas explicitement
> cette attribution) ou de la Définition DEAL (qui ne parle pas de
> Jerry) ?

L'amendement 001 du 2026-08-19 nomme la collision :

> **Collision de numérotation.** Un autre document porte le même
> numéro : `04_From_V2_Root/_SPECS/SDD/SDD-006_definition-deal-h1-isaac-12wy-curie.md`
> (8,8 Ko). Dans un système où le numéro sert de référence, deux
> documents sous le même numéro rendent toute citation ambiguë.
>
> Ces deux points demandent une décision de renumérotation, qui
> dépasse cet amendement.
> — Amendement 001 (verbatim, lignes 1163-1170)

## Cause technique de la collision

Les deux documents ont été nommés indépendamment dans deux
**arborescences** distinctes :

1. La chaîne V2 vivante a été renommée `SDD-005 → SDD-006` lors du
   passage à `05_From_V2_Domains/`, sans mise à jour du corps (titre
   interne toujours SDD-005 — voir [[concept-sdd-renaming-no-content]]).
2. La chaîne `_SPECS/SDD/` du clone 04_From_V2_Root a utilisé `SDD-006`
   pour un nouveau document (la Définition DEAL), sans voir qu'il
   existait déjà un SDD-006 ailleurs.

## Décision proposée (non tranchée ici)

L'arbitrage n'appartient pas à cette vague. Trois issues
envisageables :

1. **Renommer** SDD-006_DEAL → SDD-011_DEAL (crée un slot, préserve
   l'ordre chronologique).
2. **Renommer** SDD-006_BusinessPulse → SDD-006_BusinessPulse_V2
   (suffixe, préserve le nom historique).
3. **Fusionner** la Définition DEAL en annexe de SDD-006_BusinessPulse
   (couplage lâche).

Le présent concept **documente** la collision. La décision est
du ressort du propriétaire du produit (cf. Amendement 001).

## Concepts liés

- [[concept-sdd-renaming-no-content]] — la cause technique (renommage
  de chaîne sans mise à jour du contenu).
- [[concept-amendement-001-8e-domaine]] — l'amendement 001 qui
  documente cette collision.
- [[concept-sdd-chain-numbered]] — la chaîne SDD numérotée où le
  Business Pulse vit.
