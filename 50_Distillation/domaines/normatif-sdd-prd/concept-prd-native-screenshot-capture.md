---
type: Concept
title: PRD-native-screenshot-capture — la capture drawbridge du Jumeau
description: PRD-native-screenshot-capture.md qui pose la capture d'écran native pour le drawbridge (pont A0 ↔ OS), placé dans 05_From_V2_Domains/00_Amadeus/05_OSS_Twin/_reference/drawbridge/.
tags: [prd, native, screenshot, capture, drawbridge, oss-twin, a0-jumeau]
generated: { by: minimax-m3, at: 2026-08-19T15:40:00Z }
verified:
  - { by: process:lecture_concepts_archives, at: 2026-08-19T15:40:00Z }
sources:
  - id: prd-native-direct
    resource: "C:/Users/amado/ASpace_OS_V2/20_Life_OS/24_PARA_Enterprise/03_Resources_Geordi/05_From_V2_Domains/00_Amadeus/05_OSS_Twin/_reference/drawbridge/PRD-native-screenshot-capture.md"
    title: PRD-native-screenshot-capture (lu directement)
    last_modified: 2026-07-12
okf_version: "0.2"
---

# PRD-native-screenshot-capture — la capture drawbridge du Jumeau

## Placement unique

Le seul PRD dans
`05_From_V2_Domains/00_Amadeus/05_OSS_Twin/_reference/drawbridge/` —
le **drawbridge** (pont) entre l'OS hôte et le Jumeau Numérique A0
(OSS_Twin = Open Source Software Twin). C'est l'unique PRD qui
décrit une capacité **native OS** (capture d'écran) plutôt qu'une
capacité **SaaS** ou **Web**.

## Verdict

**canon** — la capture native est l'une des briques fondamentales du
drawbridge. Sans capture, l'A0 Jumeau ne peut pas vérifier
visuellement l'état de l'OS hôte.

## Source du décompte

`find .../05_From_V2_Domains/00_Amadeus/05_OSS_Twin/_reference/drawbridge/`
→ 1 fichier `PRD-native-screenshot-capture.md`. Aucun autre PRD dans
ce drawbridge — c'est une **brique isolée**.

## Concepts liés

- [[concept-prd-b1-filter-m3-001]] — le filtre B1 qui s'applique à
  ce PRD (les captures sont délégables à M3).
- [[concept-sdd-chain-numbered]] — la chaîne SDD où le Jumeau A0
  est documenté (SDD-000c).
